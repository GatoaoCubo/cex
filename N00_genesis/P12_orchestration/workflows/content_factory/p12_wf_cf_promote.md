---
id: p12_wf_cf_promote
kind: workflow
8f: F8_collaborate
pillar: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Promote Content Across Channels"
steps_count: 4
execution: mixed
agent_groups: [n02_marketing, n05_operations]
timeout: 300
retry_policy: per_step
depends_on: [p03_ap_cf_generate_campaign]
signals: [complete, error]
spawn_configs: []
domain: "content_factory"
quality: 9.1
tags: [workflow, content_factory, promotion, social_media, canva]
tldr: "Extract hooks from content, generate social posts + Canva thumbnails, schedule 7-day promotion campaign"
density_score: 0.91
related:
  - p12_wf_cf_publish_social
  - p12_wf_content_factory_v1
  - p12_wf_builder_8f_pipeline
  - p12_wf_marketing_pipeline
  - p12_wf_cf_publish_youtube
  - p12_wf_cf_email_launch
  - bld_architecture_chain
  - p12_wf_create_orchestration_agent
  - p12_wf_engineering_pipeline
  - p12_wf_brand_pipeline
---

## Purpose
Promotes any content factory output (course, video, ebook, podcast) through a 7-day social
media campaign. Extracts engagement hooks from the content, generates platform-adapted posts
with Canva visuals, and schedules the full campaign. This is the go-to workflow when content
is created but needs audience reach.

## Steps

### Step 1: Extract Hooks [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Analyze content to extract 5-7 engagement hooks (pain points, benefits, quotes, stats)
- **Input**: content asset path or summary
- **Output**: hook list with type classification (pain, benefit, quote, stat, question)
- **Signal**: extract_hooks_complete
- **Depends on**: none
- **Timeout**: 45s
- **On failure**: abort (no hooks = no campaign)

### Step 2: Generate Posts + Visuals [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Generate 7 days of posts per platform + Canva thumbnails/carousels using brand templates
- **Input**: hooks from Step 1 + brand_config + platform list
- **Output**: post array with text + Canva export URLs + hashtags
- **Signal**: generate_posts_complete
- **Depends on**: Step 1
- **Timeout**: 120s
- **On failure**: retry (max 1, Canva API may timeout on batch)

### Step 3: Schedule Campaign [n05_operations]
- **Agent**: n05_operations
- **Action**: Push all posts to Ayrshare with 7-day schedule, optimal times per platform
- **Input**: post array from Step 2 with schedule times
- **Output**: Ayrshare campaign ID + per-post schedule confirmation
- **Signal**: schedule_campaign_complete
- **Depends on**: Step 2
- **Timeout**: 60s
- **On failure**: retry (max 2, Ayrshare rate limits)

### Step 4: Confirm and Report [n05_operations]
- **Agent**: n05_operations
- **Action**: Verify all posts are queued, generate campaign summary report
- **Input**: Ayrshare campaign ID + post IDs
- **Output**: campaign report (total posts, platforms, schedule range, first publish date)
- **Signal**: wf_cf_promote_complete
- **Depends on**: Step 3
- **Timeout**: 30s
- **On failure**: skip (report is informational)

## Dependencies
- Content asset must exist (any content factory output)
- ap_cf_generate_campaign or equivalent hook extraction input
- Ayrshare API + Canva Business API credentials
- Brand templates in Canva for visual generation

## Signals
- **On step complete**: {step_name}_complete per step
- **On workflow complete**: wf_cf_promote_complete with campaign summary
- **On error**: wf_cf_promote_error with failed step + recovery suggestion

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `workflow`
- **Artifact ID**: `p12_wf_cf_promote`
- **Tags**: [workflow, content_factory, promotion, social_media, canva]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `workflow` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_cf_publish_social]] | sibling | 0.64 |
| [[p12_wf_content_factory_v1]] | sibling | 0.41 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.40 |
| [[p12_wf_marketing_pipeline]] | sibling | 0.34 |
| [[p12_wf_cf_publish_youtube]] | sibling | 0.32 |
| [[p12_wf_cf_email_launch]] | sibling | 0.31 |
| [[bld_architecture_chain]] | upstream | 0.30 |
| [[p12_wf_create_orchestration_agent]] | sibling | 0.30 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.30 |
| [[p12_wf_brand_pipeline]] | sibling | 0.28 |
