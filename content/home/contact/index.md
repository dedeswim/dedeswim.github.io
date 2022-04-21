---
# An instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Say hi 👋
subtitle: Feel free to contact me :)

content:
  # Automatically link email and phone or display as text?
  autolink: true
  
  # Email form provider
  form:
    provider: 
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

  # Contact details (edit or remove options as required)
  email: edoardo.m.debenedetti@gmail.com
  appointment_url: 'https://calendly.com/edoardo-debenedetti/30min'
  contact_links:
    - icon: twitter
      icon_pack: fab
      name: DM Me
      link: 'https://twitter.com/edoardo_debe'
    - icon: github
      icon_pack: fab
      name: Check out some code
      link: 'https://github.com/dedeswim'

design:
  columns: '2'
---