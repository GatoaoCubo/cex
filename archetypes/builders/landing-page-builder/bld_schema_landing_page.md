---
id: bld_schema_landing_page
kind: schema
pillar: P06
builder: landing-page-builder
version: 1.0.0
---
# Schema: Landing Page Output

```yaml
# Required frontmatter
id: string               # unique landing page artifact id
kind: landing_page
pillar: P05
title: string            # page title (also <title> tag)
version: string
created: date
author: string
quality: null            # never self-score
tags: [landing-page, ...]
stack: enum[html-tailwind, react, nextjs, astro]
sections_count: integer  # number of sections
responsive: true
dark_mode: true
a11y: AA

# Body: the actual code
# Single HTML file OR component file(s)

# Metadata block (in frontmatter or separate)
seo:
  title: string
  description: string    # max 160 chars
  og_image: string       # Open Graph image URL
  canonical: string
  json_ld_type: enum[Organization, Product, SoftwareApplication, Course]

design_tokens:
  colors: {primary, secondary, accent, bg, text, muted}
  fonts: {heading, body, mono}
  radius: string
  shadow: string

sections:
  - id: string
    type: enum[hero, problem, solution, features, social-proof, how-it-works, pricing, testimonials, faq, cta, footer, meta]
    has_cta: boolean
    responsive: boolean
```
