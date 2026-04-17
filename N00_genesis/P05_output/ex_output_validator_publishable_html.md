---
id: ex_output_validator_publishable_html
kind: output_validator
pillar: P05
title: "Example Output Validator: Publishable HTML"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.6
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
tags: [output_validator, html, publishing, n02]
tldr: "Validator contract for HTML or rich content before it is pushed into CMS or social publishing systems."
density_score: 0.89
---

# Validation Checklist

- HTML is well-formed.
- Links resolve to `{{BRAND_DOMAIN}}` or approved external domains.
- Headings follow a logical structure.
- Images include alt text.
- CTA blocks render as expected.
- Tracking parameters exist where required.

## Output

```yaml
valid: true
errors: []
warnings: []
normalized_payload:
  html:
  metadata:
    title:
    description:
    canonical_url:
```

