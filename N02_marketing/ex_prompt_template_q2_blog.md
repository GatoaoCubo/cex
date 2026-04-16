---
id: ex_prompt_template_q2_blog
kind: prompt_template
pillar: P03
title: "Example Prompt Template: Q2 Blog Format"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: q2_content_pipeline
quality: null
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
  - BRAND_DOMAIN
tags: [prompt_template, blog, editorial, q2, n02]
tldr: "Reusable long-form prompt for weekly Q2 blog production with strong brand adaptation."
density_score: 0.91
---

# Prompt

```text
Write a blog article for {{BRAND_NAME}} in a voice defined as {{BRAND_VOICE}}.

Audience:
{{BRAND_AUDIENCE}}

Theme pool:
{{BRAND_CONTENT_THEMES}}

Topic:
{{TOPIC}}

Target outcome:
{{EDITORIAL_GOAL}}

Requirements:
1. open with a concrete tension or question
2. teach something useful before selling
3. include one brand-relevant recommendation only when justified
4. include SEO title, meta description, slug, and CTA
5. route readers to {{BRAND_DOMAIN}}

Output:
- SEO package
- outline
- article
- CTA block
```

## New Brand Variables

- `EDITORIAL_GOAL`: the conversion or education objective for the article.

