---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Adversarially Robust Vision Transformers"
authors: ["Edoardo Debenedetti"]
date: 2022-05-12T12:33:57Z
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-12T12:33:57Z

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["7"]

# Publication name and optional abbreviated publication name.
publication: "Adversarially Robust Vision Transformers"
publication_short: ""

abstract: "Machine learning models are vulnerable to adversarial examples: perturbations added to benign inputs in order to fool a model into making a wrong prediction. The most successful approach to defend against adversarial examples is adversarial training, a training technique which is theoretically principled and highly effective in practice. Adversarially trained models are more robust to adversarial perturbations, albeit at the expense of the accuracy on clean samples, leading to a robustness-accuracy trade-off. Currently, the community resorts to deeper and wider models to improve this trade-off, hence decreasing the efficiency and practicality of adversarial training. In this work we show that, by switching to Vision Transformers (in particular XCiT, a Vision Transformer variation) than the ones most commonly used (ResNets and WideResNets), we can improve this trade-off without the need to use larger models, hence improving the practicality of adversarial training. We manage to do so by finding a tailored adversarial training recipe -different from the default recipe for standard training- which leads to state-of-the-art results by a significant margin. We also show that this setup scales to larger variants of XCiT, and that models trained with this setup can be fine-tuned on other smaller datasets, such as CIFAR-10, Caltech-101, and Oxford Flowers. Moreover, we compare the adversarial perturbations of our robust XCiT to those of a robust ResNet, quantifying that the former captures more semantic attributes than the latter. To the best of our knowledge, this is the first work to establish superiority of Vision Transformer over CNNs in robust machine learning. Thus, we highly recommend the use of ViTs for adversarial training."

# Summary. An optional shortened abstract.
summary: "My Master's thesis done at EPFL under the supervision of Princeton's Vikash Sehwag and Prof. Prateek Mittal, and EPFL's Prof. Troncoso. We show that we can obtain state of the art results in adversarial training using Vision Transformers (in particular with XCiT) on ImageNet."

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

url_pdf: /thesis.pdf
url_code:
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
