---
id: seed_execution_log_20260410
kind: learning_record
pillar: P11
title: "Seed Execution Log: 103 Content Items to Supabase"
version: 1.0.0
quality: null
date: 2026-04-10
nucleus: N03
tags: [seed, supabase, content-pipeline, gato3]
---

# Seed Execution Log -- 2026-04-10

## Command

```bash
python N03_engineering/tools/seed_content_pipeline.py --clear
```

## Target

- **Supabase project**: fuuguegkqnpzrrhwymgw
- **Tables**: content_items, content_schedule
- **Operation**: clear + reseed (idempotent)

## Results

| Metric | Value |
|--------|-------|
| Blog posts inserted | 26/26 |
| Instagram posts inserted | 77/77 |
| Schedule entries created | 103/103 |
| Failures | 0 |
| Total items | 103 |

## Content Type Breakdown

| Type | Count |
|------|-------|
| blog_post | 26 |
| instagram_carrossel | 19 |
| instagram_feed | 19 |
| instagram_reel | 26 |
| instagram_story | 13 |

## Category Distribution

| Category | Count | Percent |
|----------|-------|---------|
| educativo | 55 | 53.4% |
| meme_humor | 20 | 19.4% |
| produto | 20 | 19.4% |
| seasonal | 8 | 7.8% |

## Date Range

- **Start**: 2026-04-15
- **End**: 2026-07-13
- **Weeks**: 13 (7 items week 1, 8 items weeks 2-13)

## Verification

Post-seed REST API query confirmed:
- `content_items`: 103 rows
- `content_schedule`: 103 rows
- Content type distribution matches source data

## Source Data

- Blog: `N02_marketing/content_pipeline/blog/` (26 .md files)
- Instagram: `N02_marketing/content_pipeline/instagram/` (13 week .md files)
- Decision manifest: `.cex/runtime/decisions/decision_manifest.yaml`
