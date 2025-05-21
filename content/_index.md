---
# Page title
title:
# Page type - we want a landing page (such as a homepage)
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: about.biography
    id: about
    content:
      title: 
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: edoardo
  - block: markdown
    content:
      title: Current Work
      count: 3
      text: "{{< readfromfile \"/content/current-work.md\" 5 >}}"
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
  - block: markdown
    content:
      title: News
      count: 3
      text: "{{< readfromfile \"/content/newslist.md\" 5 >}}"
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
  # - block: collection
  #   id: publications
  #   content:
  #     title: Publications
  #     count: 3
  #     text: 
  #     filters:
  #       folders:
  #         - publication
  #       exclude_featured: false
  #   design:
  #     columns: '2'
  #     view: citation
---
