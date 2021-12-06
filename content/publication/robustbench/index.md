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
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track"
publication_short: "NeurIPS 2021 Datasets and Benchmarks Track"

abstract: "As a research community, we are still lacking a systematic understanding of the progress on adversarial robustness which often makes it hard to identify the most promising ideas in training robust models. A key challenge in benchmarking robustness is that its evaluation is often error-prone leading to robustness overestimation. Our goal is to establish a standardized benchmark of adversarial robustness, which as accurately as possible reflects the robustness of the considered models within a reasonable computational budget. To this end, we start by considering the image classification task and introduce restrictions (possibly loosened in the future) on the allowed models and evaluate adversarial robustness with AutoAttack, an ensemble of white- and black-box attacks, which was recently shown in a large-scale study to improve almost all robustness evaluations compared to the original publications. To prevent overadaptation of new defenses to AutoAttack, we welcome external evaluations based on adaptive attacks, especially where AutoAttack flags a potential overestimation of robustness. Our leaderboard, hosted at https://robustbench.github.io/, contains evaluations of 120+ models and aims at reflecting the current state of the art in image classification on a set of well-defined tasks in $\\ell_2$- and $\\ell_\\infty$-threat models and on common corruptions, with possible extensions in the future. Additionally, we open-source the library https://github.com/RobustBench/robustbench that provides unified access to 80+ robust models to facilitate their downstream applications. Finally, based on the collected models, we analyze the impact of robustness on the performance on distribution shifts, calibration, out-of-distribution detection, fairness, privacy leakage, smoothness, and transferability. "

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

url_pdf: "https://openreview.net/forum?id=SSKZPJCt7B"
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
