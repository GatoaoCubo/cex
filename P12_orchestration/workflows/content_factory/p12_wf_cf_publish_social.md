---
id: p12_wf_cf_publish_social
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Publish Content to Social Media Platforms"
steps_count: 4
execution: mixed
agent_groups: [n02_marketing, n05_operations]
timeout: 240
retry_policy: per_step
depends_on: [p03_ap_cf_generate_campaign]
signals: [complete, error]
spawn_configs: []
domain: "content_factory"
quality: 9.0
tags: [workflow, content_factory, social_media, ayrshare, publish]
tldr: "Adapt content per platform, create visuals via Canva, schedule and publish via Ayrshare — 4 mixed steps"
density_score: 0.92
---

## Purpose
Takes campaign output from ap_cf_generate_campaign and publishes to multiple social platforms
via Ayrshare API. Each platform gets adapted copy (respecting character limits and hashtag
conventions), Canva-generated visuals, and optimized scheduling. Supports Instagram, LinkedIn,
Twitter/X, and TikTok simultaneously.

## Steps

### Step 1: Adapt Content Per Platform [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Transform campaign posts into platform-specific payloads with character limits and format rules
- **Input**: campaign YAML from ap_cf_generate_campaign
- **Output**: per-platform payload array (text, hashtags, media_type, dimensions)
- **Signal**: adapt_content_complete
- **Depends on**: none
- **Timeout**: 45s
- **On failure**: abort (content must be adapted before any publish)

### Step 2: Generate Visual Assets [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Create platform-specific visuals via Canva Business API (carousel, story, post, reel cover)
- **Input**: visual directions from campaign + brand_config templates
- **Output**: Canva export URLs per post (PNG/MP4)
- **Signal**: visuals_complete
- **Depends on**: Step 1
- **Timeout**: 90s
- **On failure**: skip (text-only posts as fallback)

### Step 3: Schedule via Ayrshare [n05_operations]
- **Agent**: n05_operations
- **Action**: Send payloads + media to Ayrshare API with scheduled publish times
- **Input**: adapted payloads from Step 1 + visual URLs from Step 2 + schedule times
- **Output**: Ayrshare post IDs + scheduled timestamps per platform
- **Signal**: schedule_complete
- **Depends on**: Steps 1, 2
- **Timeout**: 60s
- **On failure**: retry (max 2, API rate limits)

### Step 4: Verify Publication [n05_operations]
- **Agent**: n05_operations
- **Action**: Poll Ayrshare for publication confirmation on each scheduled post
- **Input**: Ayrshare post IDs from Step 3
- **Output**: publication status per platform (published, scheduled, failed)
- **Signal**: wf_cf_publish_social_complete
- **Depends on**: Step 3
- **Timeout**: 45s
- **On failure**: skip (verification is non-blocking, posts are already scheduled)

## Dependencies
- Campaign data from ap_cf_generate_campaign must exist
- Ayrshare API key configured in .cex/brand/api_keys
- Canva Business API access for visual generation
- Brand templates registered in Canva team account

## Signals
- **On step complete**: {step_name}_complete per step
- **On workflow complete**: wf_cf_publish_social_complete with per-platform status summary
- **On error**: wf_cf_publish_social_error with platform + error detail

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `workflow`
- **Artifact ID**: `p12_wf_cf_publish_social`
- **Tags**: [workflow, content_factory, social_media, ayrshare, publish]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `workflow` | Artifact type |
| Pipeline | 8F (F1→F8) |
