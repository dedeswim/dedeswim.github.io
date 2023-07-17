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
      title: News
      count: 3
      text: "{{< readfromfile \"/content/newslist.md\" 5 >}}"
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
  - block: collection
    id: publications
    content:
      title: Publications
      count: 3
      text: 
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      columns: '2'
      view: citation
  - block: contact
    id: contact
    content:
      title: Say hi 👋
      subtitle: Feel free to contact me :)
      text: 
      contact_links:
        - icon: envelope
          icon_pack: fas
          name: edebenedetti@inf.ethz.ch (academic stuff)
          link: 'mailto:edebenedetti@inf.ethz.ch'
        - icon: inbox
          icon_pack: fas
          name: edoardo.m.debenedetti@gmail.com (personal stuff)
          link: 'edoardo.m.debenedetti@gmail.com'
        - icon: twitter
          icon_pack: fab
          name: DM Me
          link: 'https://twitter.com/edoardo_debe'
        - icon: github
          icon_pack: fab
          name: Check out some code
          link: 'https://github.com/dedeswim'
      # Automatically link email and phone or display as text?
      autolink: true
    design:
      columns: '2'
---
