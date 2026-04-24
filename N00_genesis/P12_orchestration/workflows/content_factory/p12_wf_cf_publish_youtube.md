---
id: p12_wf_cf_publish_youtube
kind: workflow
8f: F8_collaborate
pillar: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Publish Video to YouTube"
steps_count: 5
execution: sequential
agent_groups: [n02_marketing, n05_operations]
timeout: 300
retry_policy: per_step
depends_on: [p03_ap_cf_generate_video]
signals: [complete, error]
spawn_configs: []
domain: "content_factory"
quality: 9.0
tags: [workflow, content_factory, youtube, publish, video]
tldr: "Upload video to YouTube with metadata, thumbnail, captions, and publish — 5 sequential steps with retry"
density_score: 0.91
related:
  - p12_wf_content_factory_v1
  - p12_wf_builder_8f_pipeline
  - p12_wf_cf_promote
  - p12_wf_cf_publish_social
  - p12_wf_cf_publish_hotmart
  - p12_wf_engineering_pipeline
  - bld_architecture_chain
  - p01_kc_youtube_api
  - p12_wf_brand_pipeline
  - p12_wf_orchestration_pipeline
---

## Purpose
Publishes a generated video to YouTube end-to-end. Takes the video file and script metadata
from ap_cf_generate_video, uploads to YouTube via API, sets SEO metadata, generates and uploads
a thumbnail via Canva, adds captions, and publishes. Designed for zero-touch operation after
the video script and recording are complete.

## Steps

### Step 1: Validate Assets [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Verify video file exists, script metadata is complete, brand_config loaded
- **Input**: video file path + script YAML from ap_cf_generate_video
- **Output**: validated asset manifest (file, title, description, tags confirmed)
- **Signal**: validate_assets_complete
- **Depends on**: none
- **Timeout**: 30s
- **On failure**: abort (missing assets cannot be recovered)

### Step 2: Upload Video [n05_operations]
- **Agent**: n05_operations
- **Action**: Upload video file to YouTube via API, set as unlisted during processing
- **Input**: video file path from Step 1 manifest
- **Output**: YouTube video ID + upload confirmation
- **Signal**: upload_complete
- **Depends on**: Step 1
- **Timeout**: 120s
- **On failure**: retry (max 2, network issues common)

### Step 3: Set Metadata [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Apply title, description, tags, category, and end-screen settings via YouTube API
- **Input**: YouTube video ID + script metadata (title ≤60 chars, description, tags)
- **Output**: metadata confirmation with SEO score estimate
- **Signal**: metadata_complete
- **Depends on**: Step 2
- **Timeout**: 30s
- **On failure**: retry (API rate limits)

### Step 4: Generate and Upload Thumbnail [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Create thumbnail via Canva Business API using brand template, upload to YouTube
- **Input**: thumbnail_text from script + brand_config.colors + Canva template ID
- **Output**: thumbnail URL + Canva design ID
- **Signal**: thumbnail_complete
- **Depends on**: Step 2
- **Timeout**: 60s
- **On failure**: skip (video can publish without custom thumbnail)

### Step 5: Publish [n05_operations]
- **Agent**: n05_operations
- **Action**: Change video status from unlisted to public, verify accessibility
- **Input**: YouTube video ID from Step 2
- **Output**: public video URL + publish timestamp
- **Signal**: wf_cf_publish_youtube_complete
- **Depends on**: Steps 3, 4
- **Timeout**: 30s
- **On failure**: abort (publish failure needs manual review)

## Dependencies
- Video file must exist at specified path (from recording step, external to this workflow)
- Script metadata from ap_cf_generate_video must be available
- YouTube API credentials configured in .cex/brand/api_keys (YouTube Data API v3)
- Canva Business API access for thumbnail generation

## Signals
- **On step complete**: {step_name}_complete signal emitted per step
- **On workflow complete**: wf_cf_publish_youtube_complete with video URL
- **On error**: wf_cf_publish_youtube_error with failed step ID and error message

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_content_factory_v1]] | sibling | 0.39 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.39 |
| [[p12_wf_cf_promote]] | sibling | 0.34 |
| [[p12_wf_cf_publish_social]] | sibling | 0.33 |
| [[p12_wf_cf_publish_hotmart]] | sibling | 0.30 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.28 |
| [[bld_architecture_chain]] | upstream | 0.28 |
| [[p01_kc_youtube_api]] | upstream | 0.28 |
| [[p12_wf_brand_pipeline]] | sibling | 0.27 |
| [[p12_wf_orchestration_pipeline]] | sibling | 0.27 |
