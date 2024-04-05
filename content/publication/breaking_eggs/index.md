---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Evading Black-box Classifiers Without Breaking Eggs"
authors: ["Edoardo Debenedetti", "Nicholas Carlini", "Florian Tramèr"]
date: 2024-01-06T15:33:16Z
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2023-06-06T15:33:16Z

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "2nd IEEE Conference on Secure and Trustworthy Machine Learning, 2024"
publication_short: "IEEE SaTML 2024"

abstract: "Decision-based evasion attacks repeatedly query a black-box classifier to generate adversarial examples. Prior work measures the cost of such attacks by the total number of queries made to the classifier. We argue this metric is flawed. Most security-critical machine learning systems aim to weed out \"bad\" data (e.g., malware, harmful content, etc). Queries to such systems carry a fundamentally *asymmetric cost*: queries detected as \"bad\" come at a higher cost because they trigger additional security filters, e.g., usage throttling or account suspension. Yet, we find that existing decision-based attacks issue a large number of \"bad\" queries, which likely renders them ineffective against security-critical systems. We then design new attacks that reduce the number of bad queries by $1.5$-$7.3\\times$, but often at a significant increase in total (non-bad) queries. We thus pose it as an open problem to build black-box attacks that are more effective under realistic cost metrics."

# Summary. An optional shortened abstract.
summary: "We propose a new real-world oriented metric for black-box decision-based attacks on security-critical systems"

tags: ["Distinguished Paper Award Runner-up"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://arxiv.org/abs/2306.02895
url_code: https://github.com/ethz-spylab/realistic-adv-examples
url_dataset:
url_poster: poster.pdf
url_project:
url_slides: slides.pdf
url_source:
url_video: https://slideslive.com/39006203/evading-blackbox-classifiers-without-breaking-eggs?ref=speaker-22359

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
