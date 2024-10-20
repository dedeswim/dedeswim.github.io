---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Scaling Compute Is Not All You Need for Adversarial Robustness"
authors: ["Edoardo Debenedetti", "Zishen Wan", "Maksym Andriushchenko", "Vikash Sehwag", "Kshitij Bhardwaj", "Bhavya Kailkhura"]
date: 2024-05-11T12:22:26Z
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2024-10-20T12:22:26Z

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "ICLR 2024 Workshop on Reliable and Responsible Foundation Models"
publication_short: "ICLR 2024 R2FM Workshop"

abstract: "The last six years have witnessed significant progress in adversarially robust deep learning. As evidenced by the CIFAR-10 dataset category in RobustBench benchmark, the accuracy under ℓ∞ adversarial perturbations improved from 44% in Madry et al. (2018) to 71% in Peng et al. (2023). Although impressive, existing state-of-the-art is still far from satisfactory. It is further observed that best-performing models are often very large models adversarially trained by industrial labs with significant computational budgets. In this paper, we aim to understand: \"how much longer can computing power drive adversarial robustness advances?\" To answer this question, we derive *scaling laws for adversarial robustness* which can be extrapolated in the future to provide an estimate of how much cost we would need to pay to reach a desired level of robustness. We show that increasing the FLOPs needed for adversarial training does not bring as much advantage as it does for standard training in terms of performance improvements. Moreover, we find that some of the top-performing techniques are difficult to exactly reproduce, suggesting that they are not robust enough for minor changes in the training setup. Our analysis also uncovers potentially worthwhile directions to pursue in future research. Finally, we make our benchmarking framework (built on top of `timm`) publicly available to facilitate future analysis in efficient robust deep learning."

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

url_pdf: https://arxiv.org/abs/2312.13131
url_code: http://github.com/dedeswim/timm-adv-training/
url_dataset:
url_poster:
url_project:
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
