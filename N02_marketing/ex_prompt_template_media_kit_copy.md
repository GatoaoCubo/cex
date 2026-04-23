---
id: ex_prompt_template_media_kit_copy
kind: prompt_template
pillar: P03
title: "Example Prompt Template: Media Kit Copy"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: media_kit_generator
quality: 8.7
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_AUDIENCE
  - BRAND_DOMAIN
tags: [prompt_template, media-kit, sales-enablement, n02]
tldr: "Prompt for generating a compact media kit with copy blocks, proof points, and asset requirements."
density_score: 0.9
related:
  - p07_sr_5d_marketing
  - ad_copy_template
  - p03_sp_marketing_nucleus
  - bld_collaboration_landing_page
  - landing_page_template
  - brand_voice_templates
  - bld_system_prompt_landing_page
  - landing-page-builder
  - p03_pt_brand_task_driver
  - p03_sp_commercial_nucleus
---

# Prompt

```text
Generate a media kit for {{BRAND_NAME}}.

Voice:
{{BRAND_VOICE}}

Tone:
{{BRAND_TONE}}

Audience:
{{BRAND_AUDIENCE}}

Offer details:
{{OFFER_DETAILS}}

Include:
- one-line description
- three headline options
- audience fit
- proof points
- partnership angles
- CTA and destination on {{BRAND_DOMAIN}}
- list of visuals needed

Keep the final package compact enough for sales decks, creator outreach, and landing-page modules.
```

## New Brand Variables

- `OFFER_DETAILS`: structured summary of the product, service, or campaign being packaged.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_5d_marketing]] | downstream | 0.19 |
| [[ad_copy_template]] | sibling | 0.19 |
| [[p03_sp_marketing_nucleus]] | related | 0.19 |
| [[bld_collaboration_landing_page]] | downstream | 0.19 |
| [[landing_page_template]] | sibling | 0.18 |
| [[brand_voice_templates]] | sibling | 0.17 |
| [[bld_system_prompt_landing_page]] | related | 0.17 |
| [[landing-page-builder]] | downstream | 0.17 |
| [[p03_pt_brand_task_driver]] | sibling | 0.17 |
| [[p03_sp_commercial_nucleus]] | related | 0.16 |
