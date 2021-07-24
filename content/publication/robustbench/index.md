---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "RobustBench: A standardized benchmark for adversarial robustness"
authors: ["Francesco Croce", "Maksym Andriushchenko", "Vikash Sehwag", "Edoardo Debenedetti", "Nicolas Flammarion", "Mung Chiang", "Prateek Mittal", "Matthias Hein"]
date: 2021-03-29T10:44:04+02:00
doi: ""
math: true

# Schedule page publish date (NOT publication's date).
publishDate: 2021-03-29T10:44:04+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "ICLR 2021 Workshop on Security and Safety in Machine Learning Systems"
publication_short: "ICLR 2021 MLSec Workshop"

abstract: "Evaluation of adversarial robustness is often error-prone leading to overestimation of the true robustness of models. Our goal is to establish a *standardized benchmark* of adversarial robustness, which as accurately as possible reflects the robustness of the considered models within a reasonable computational budget. This requires to impose some restrictions on the admitted models to rule out defenses that only make gradient-based attacks ineffective without improving actual robustness. We evaluate robustness of models for our benchmark with AutoAttack, an ensemble of white- and black-box attacks which was recently shown to improve almost all robustness evaluations compared to the original publications. Our leaderboard aims at reflecting the current state of the art in the $\\ell_\\infty$- and $\\ell_2$-threat models and on common image corruptions, with possible extensions in the future. Additionally, we open-source a library that provides unified access to state-of-the-art robust models to facilitate their downstream applications. Finally, we analyze general trends in $\\ell_p$-robustness and its impact on other tasks such as robustness to various distribution shifts and out-of-distribution detection."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: "https://arxiv.org/abs/2010.09670"
url_code: "https://github.com/RobustBench/robustbench"
url_dataset:
url_poster:
url_project: "https://robustbench.github.io"
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ["robustbench"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
