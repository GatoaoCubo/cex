---
id: bld_output_template_landing_page
kind: output_template
pillar: P05
builder: landing-page-builder
version: 1.0.0
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
