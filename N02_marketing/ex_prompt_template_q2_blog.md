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
quality: 8.8
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
related:
  - p03_sp_brand_nucleus
  - p02_agent_commercial_nucleus
  - p03_sp_commercial_nucleus
  - p11_qg_brand_artifacts
  - examples_prompt_template_builder
  - spec_n06_brand_verticalization
  - p12_dr_commercial
  - p02_agent_brand_nucleus
  - p01_kc_seo_content_strategy_ecommerce
  - p07_sr_5d_marketing
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_brand_nucleus]] | related | 0.22 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.20 |
| [[p03_sp_commercial_nucleus]] | related | 0.20 |
| [[p11_qg_brand_artifacts]] | downstream | 0.19 |
| [[examples_prompt_template_builder]] | downstream | 0.18 |
| [[spec_n06_brand_verticalization]] | downstream | 0.18 |
| [[p12_dr_commercial]] | downstream | 0.18 |
| [[p02_agent_brand_nucleus]] | upstream | 0.17 |
| [[p01_kc_seo_content_strategy_ecommerce]] | upstream | 0.17 |
| [[p07_sr_5d_marketing]] | downstream | 0.17 |
