---
id: bld_output_template_landing_page
kind: output_template
pillar: P05
builder: landing-page-builder
version: 1.0.0
quality: 9.0
title: "Output Template Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
---
# Output Template: Landing Page

```markdown
---
id: landing_page_{{BRAND_SLUG}}
kind: landing_page
pillar: P05
title: "{{PAGE_TITLE}}"
version: 1.0.0
created: {{DATE}}
author: landing-page-builder
quality: null
tags: [landing-page, {{BRAND_SLUG}}, {{STACK}}, responsive, dark-mode]
stack: {{STACK}}
sections_count: {{SECTIONS_COUNT}}
responsive: true
dark_mode: true
a11y: AA
seo:
  title: "{{SEO_TITLE}}"
  description: "{{SEO_DESCRIPTION}}"
  og_image: "{{OG_IMAGE_URL}}"
---

# Landing Page: {{BRAND_NAME}}

## Design Tokens
| Token | Value |
|-------|-------|
| Primary | {{COLOR_PRIMARY}} |
| Secondary | {{COLOR_SECONDARY}} |
| Font Heading | {{FONT_HEADING}} |
| Font Body | {{FONT_BODY}} |

## Sections
{{SECTIONS_CHECKLIST}}

## Code

\`\`\`html
{{FULL_HTML_CODE}}
\`\`\`

## Deploy Instructions
1. Save as `index.html`
2. Replace placeholder images with real assets
3. Replace {{BRAND_*}} variables with actual brand values
4. Deploy to: Vercel (`vercel deploy`) / Netlify (`netlify deploy`) / GitHub Pages
5. Test on mobile (375px) and desktop (1440px)
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
