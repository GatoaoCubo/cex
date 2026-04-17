---
id: p05_out_cf_actions_and_distribution
kind: output_template
pillar: P05
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Content Factory Wave 2 — Action Prompts + Distribution Workflows"
mission: MISSION_content_factory_wave2
nucleus: N02
task: build_action_prompts_and_distribution_workflows
status: complete
artifacts_produced: 12
domain: "content_factory"
quality: 9.1
tags: [output, content_factory, wave2, n02]
tldr: "N02 output: 7 action prompts + 5 distribution workflows for Content Factory"
density_score: 0.90
---

# N02 Output: Content Factory — Action Prompts + Distribution Workflows

## Summary

Produced **12 artifacts** for Content Factory Wave 2:
- 7 Action Prompts (P03) — content generation triggers
- 5 Workflows (P12) — distribution orchestration

All artifacts follow 8F pipeline, builder schemas, quality=null, and reference the 4 configured APIs
(Canva Business, Ayrshare, YouTube, Hotmart).

## Action Prompts Produced

| # | ID | Action | Path |
|---|-----|--------|------|
| 1 | p03_ap_cf_generate_course | Generate structured course from topic | P03_prompts/actions/content_factory/ |
| 2 | p03_ap_cf_generate_video | Generate video script + production brief | P03_prompts/actions/content_factory/ |
| 3 | p03_ap_cf_generate_ebook | Generate eBook from topic + chapter plan | P03_prompts/actions/content_factory/ |
| 4 | p03_ap_cf_generate_presentation | Generate slide deck from topic | P03_prompts/actions/content_factory/ |
| 5 | p03_ap_cf_generate_podcast | Generate podcast episode script | P03_prompts/actions/content_factory/ |
| 6 | p03_ap_cf_generate_campaign | Generate multi-platform social campaign | P03_prompts/actions/content_factory/ |
| 7 | p03_ap_cf_publish | Route + publish content to channels | P03_prompts/actions/content_factory/ |

## Workflows Produced

| # | ID | What It Does | Execution | Steps |
|---|-----|-------------|-----------|-------|
| 1 | p12_wf_cf_publish_youtube | Upload → metadata → thumbnail → publish | sequential | 5 |
| 2 | p12_wf_cf_publish_social | Adapt → visuals → schedule → verify via Ayrshare | mixed | 4 |
| 3 | p12_wf_cf_publish_hotmart | Validate → upload → checkout → landing → go live | sequential | 5 |
| 4 | p12_wf_cf_promote | Extract hooks → posts + Canva → schedule 7 days | mixed | 4 |
| 5 | p12_wf_cf_email_launch | Generate 5-email sequence → automate → schedule → activate | sequential | 4 |

## Content Factory Flow (how pieces connect)

```
[User Intent] → [Action Prompt] → [Content Generated] → [Workflow] → [Published]

"Crie um curso"  → ap_cf_generate_course  → course structure  → wf_cf_publish_hotmart → Hotmart live
"Crie um video"  → ap_cf_generate_video   → video script      → wf_cf_publish_youtube → YouTube live
"Crie um ebook"  → ap_cf_generate_ebook   → ebook manuscript  → wf_cf_promote         → Social campaign
"Promova X"      → ap_cf_generate_campaign → campaign posts    → wf_cf_publish_social  → Ayrshare scheduled
"Publique X"     → ap_cf_publish           → publish manifest  → (routes to correct wf) → Multi-channel
"Lance por email" → (content ready)        → email sequence    → wf_cf_email_launch    → Email automated
```

## API Integration Map

| API | Used By | Purpose |
|-----|---------|---------|
| Canva Business | wf_cf_publish_youtube, wf_cf_publish_social, wf_cf_promote | Thumbnails, carousels, stories |
| Ayrshare | wf_cf_publish_social, wf_cf_promote | Multi-platform social scheduling |
| YouTube Data v3 | wf_cf_publish_youtube | Video upload, metadata, publish |
| Hotmart | wf_cf_publish_hotmart | Course upload, checkout, landing page |
| Email Provider | wf_cf_email_launch | Automation, scheduling, sends |

## Quality Gate Summary

- All 7 action_prompts: id pattern ✓, frontmatter 21 fields ✓, 5 body sections ✓, edge_cases ≥2 ✓, quality=null ✓
- All 5 workflows: id pattern ✓, frontmatter complete ✓, 4 body sections ✓, steps_count matches ✓, quality=null ✓
- Zero new kinds created (used existing: action_prompt, workflow)
- All artifacts reference {{BRAND_*}} injection for brand consistency
