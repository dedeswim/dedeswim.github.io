---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models"
authors: ["Patrick Chao", "Edoardo Debenedetti", "Alexander Robey", "Maksym Andriushchenko", "Francesco Croce", "Vikash Sehwag", "Edgar Dobriban", "Nicolas Flammarion", "George J. Pappas", "Florian Tramer", "Hamed Hassani", "Eric Wong"]
date: 2024-12-09T14:11:22Z
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2024-10-09T14:11:22Z

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "NeurIPS 2024 Datasets and Benchmarks Track"
publication_short: "NeurIPS D&B 2024"

abstract: "Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not reproducible, as they withhold adversarial prompts, involve closed-source code, or rely on evolving proprietary APIs. To address these challenges, we introduce JailbreakBench, an open-sourced benchmark with the following components: (1) an evolving repository of state-of-the-art adversarial prompts, which we refer to as jailbreak artifacts; (2) a jailbreaking dataset comprising 100 behaviors -- both original and sourced from prior work (Zou et al., 2023; Mazeika et al., 2023, 2024) -- which align with OpenAI's usage policies; (3) a standardized evaluation framework at [this https URL](https://github.com/JailbreakBench/jailbreakbench) that includes a clearly defined threat model, system prompts, chat templates, and scoring functions; and (4) a leaderboard at [this https URL](https://jailbreakbench.github.io/) that tracks the performance of attacks and defenses for various LLMs. We have carefully considered the potential ethical implications of releasing this benchmark, and believe that it will be a net positive for the community."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://arxiv.org/abs/2404.01318
url_code: https://github.com/JailbreakBench/jailbreakbench
url_dataset:
url_poster:
url_project: https://jailbreakbench.github.io
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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
