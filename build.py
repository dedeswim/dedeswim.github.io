# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bibtexparser>=1.4.4",
#     "jinja2>=3.1.6",
# ]
# ///
"""Build script: reads publications.bib and renders index.html via Jinja2."""

import re
import shutil
from pathlib import Path

import bibtexparser
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
BUILD_DIR = ROOT / "_site"
TEMPLATE_DIR = ROOT / "templates"
BIB_FILE = ROOT / ".." / "cv" / "publications.bib"
STATIC_DIR = ROOT / "static"


def clean_latex(text: str) -> str:
    """Remove LaTeX markup from a string."""
    text = text.replace("{", "").replace("}", "")
    text = text.replace("\\textbf", "")
    text = text.replace("\\emph", "")
    # Handle \`e -> è, \'e -> é, \"o -> ö, \c{c} -> ç, etc.
    accent_map = {
        "`": "\u0300",  # grave
        "'": "\u0301",  # acute
        '"': "\u0308",  # diaeresis
        "^": "\u0302",  # circumflex
        "~": "\u0303",  # tilde
    }
    for latex_acc, unicode_comb in accent_map.items():
        # Match \`{e} or \`e
        text = re.sub(
            rf"\\{re.escape(latex_acc)}(\w)", lambda m: m.group(1) + unicode_comb, text
        )
    # \c{c} -> ç
    text = re.sub(r"\\c\s*(\w)", lambda m: m.group(1) + "\u0327", text)
    # Greek letters
    greek = {
        "\\alpha": "\u03b1", "\\beta": "\u03b2", "\\gamma": "\u03b3",
        "\\delta": "\u03b4", "\\epsilon": "\u03b5", "\\lambda": "\u03bb",
        "\\mu": "\u03bc", "\\pi": "\u03c0", "\\sigma": "\u03c3",
    }
    for cmd, char in greek.items():
        text = text.replace(cmd, char)
    # Normalize unicode combining chars
    import unicodedata

    text = unicodedata.normalize("NFC", text)
    # Remove any remaining backslashes from LaTeX commands
    text = re.sub(r"\\[a-zA-Z]+\s*", "", text)
    # Clean up dollar signs
    text = text.replace("$", "")
    return text.strip()


def parse_authors(raw: str) -> list[str]:
    """Parse 'Last, First and Last, First' into ['First Last', ...], keeping * markers."""
    authors = []
    for part in raw.split(" and "):
        part = part.strip()
        if "," in part:
            last, first = part.split(",", 1)
            authors.append(f"{first.strip()} {last.strip()}")
        else:
            authors.append(part)
    return [clean_latex(a) for a in authors]


def get_highlight_index(entry: dict) -> int | None:
    """Get the 1-based author index to highlight from author+an field."""
    an = entry.get("author+an", "")
    match = re.search(r"(\d+)=highlight", an)
    return int(match.group(1)) if match else None


def parse_bib(bib_path: Path) -> list[dict]:
    """Parse a .bib file and return structured entries."""
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with open(bib_path) as f:
        library = bibtexparser.load(f, parser=parser)

    entries = []
    for entry in library.entries:
        authors = parse_authors(entry.get("author", ""))
        highlight_idx = get_highlight_index(entry)
        # Map keywords to categories
        kw = entry.get("keywords", "conference")
        if "workshop" in kw:
            category = "workshop"
        elif "manuscript" in kw:
            category = "manuscript"
        else:
            category = "conference"

        raw_note = entry.get("note", "")
        note = clean_latex(raw_note)
        # Notes containing \textbf in the original are awards/highlights
        is_award = "\\textbf" in raw_note
        addendum = clean_latex(entry.get("addendum", ""))

        entries.append(
            {
                "key": entry.get("ID", ""),
                "title": clean_latex(entry.get("title", "")),
                "authors": authors,
                "highlight_idx": highlight_idx,
                "venue": clean_latex(entry.get("booktitle", "")),
                "year": int(entry.get("year", "0")),
                "url": entry.get("url", ""),
                "note": note,
                "is_award": is_award,
                "addendum": addendum,
                "category": category,
            }
        )
    # Sort by year descending, then by title
    entries.sort(key=lambda e: (-e["year"], e["title"]))
    return entries


def build():
    # Parse publications
    entries = parse_bib(BIB_FILE)

    # Group all papers by year
    pubs_by_year: dict[int, list[dict]] = {}
    for pub in entries:
        pubs_by_year.setdefault(pub["year"], []).append(pub)
    years = sorted(pubs_by_year.keys(), reverse=True)

    # Render template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=True)
    template = env.get_template("index.html")
    html = template.render(
        pubs_by_year=pubs_by_year,
        years=years,
    )

    # Write output
    BUILD_DIR.mkdir(exist_ok=True)
    (BUILD_DIR / "index.html").write_text(html)

    # Copy static files
    if STATIC_DIR.exists():
        for f in STATIC_DIR.iterdir():
            if f.is_file():
                shutil.copy2(f, BUILD_DIR / f.name)
            elif f.is_dir():
                shutil.copytree(f, BUILD_DIR / f.name, dirs_exist_ok=True)

    # Copy CV from cv repo if available
    cv_src = ROOT / ".." / "cv" / "cv.pdf"
    if cv_src.exists():
        (BUILD_DIR / "files").mkdir(exist_ok=True)
        shutil.copy2(cv_src, BUILD_DIR / "files" / "cv.pdf")

    # Copy avatar
    avatar_src = ROOT / "content" / "authors" / "edoardo" / "avatar.jpeg"
    if avatar_src.exists():
        shutil.copy2(avatar_src, BUILD_DIR / "avatar.jpeg")

    print(f"Built site in {BUILD_DIR}")


if __name__ == "__main__":
    build()
