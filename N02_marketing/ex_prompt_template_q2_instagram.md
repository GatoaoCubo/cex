---
id: ex_prompt_template_q2_instagram
kind: prompt_template
pillar: P03
title: "Example Prompt Template: Q2 Instagram Format"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: q2_content_pipeline
quality: 8.6
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
  - BRAND_DOMAIN
tags: [prompt_template, instagram, editorial, q2, n02]
tldr: "Reusable format prompt for weekly Instagram production rather than one template per post."
density_score: 0.92
---

# Prompt

```text
Create a one-week Instagram package for {{BRAND_NAME}}.

Brand voice:
{{BRAND_VOICE}}

Tone:
{{BRAND_TONE}}

Audience:
{{BRAND_AUDIENCE}}

Content themes:
{{BRAND_CONTENT_THEMES}}

For this week, generate:
- 3 feed posts
- 2 carousel ideas
- 1 reel concept
- 1 story prompt

For each asset include:
- objective
- hook
- caption
- visual direction
- CTA
- link target using {{BRAND_DOMAIN}} when relevant

Keep the mix balanced across education, demand capture, and community.
```

