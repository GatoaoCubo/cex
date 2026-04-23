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
related:
  - schedule_instagram_content_plan
  - tpl_content_distribution_plan
  - p01_kc_brand_voice_consistency_channels
  - spec_n06_brand_verticalization
  - p03_sp_brand_nucleus
  - brand_voice_templates
  - p01_kc_cex_as_digital_asset
  - p07_sr_5d_brand_evaluation
  - action-prompt-builder
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[schedule_instagram_content_plan]] | related | 0.32 |
| [[tpl_content_distribution_plan]] | sibling | 0.22 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.18 |
| [[spec_n06_brand_verticalization]] | downstream | 0.17 |
| [[p03_sp_brand_nucleus]] | related | 0.17 |
| [[brand_voice_templates]] | sibling | 0.16 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.16 |
| [[p07_sr_5d_brand_evaluation]] | downstream | 0.15 |
| [[action-prompt-builder]] | related | 0.15 |
