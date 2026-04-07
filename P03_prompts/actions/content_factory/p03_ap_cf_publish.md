---
id: p03_ap_cf_publish
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Publish Content to Distribution Channels"
action: "Route and publish a content asset to specified distribution channels with platform-specific formatting"
input_required:
  - "content_path: string — path to content asset (markdown, yaml, or compiled)"
  - "channels: list[string] — target channels (youtube, instagram, linkedin, twitter, hotmart, email)"
  - "publish_mode: enum — immediate, scheduled, draft"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Publish manifest with per-channel status, formatted payloads, and confirmation or error details"
purpose: "Unified publish action that routes any content to any channel through the correct workflow"
steps_count: 4
timeout: "60s"
edge_cases:
  - "Content type incompatible with channel (e.g. ebook → twitter) — generate excerpt + link instead"
  - "Channel API unavailable — queue for retry, mark status as 'pending_retry'"
  - "publish_mode=scheduled but no schedule_time provided — default to next optimal slot"
constraints:
  - "Do NOT modify original content — create channel-specific copies"
  - "Do NOT publish without brand_config validation — reject if brand incomplete"
  - "All API calls through configured providers (Ayrshare, YouTube API, Hotmart API)"
domain: "content_factory"
quality: 9.1
tags: [action_prompt, content_factory, publish, distribution, multi_channel]
tldr: "Route and publish content to multiple channels (YouTube, social, Hotmart, email) with per-channel formatting"
density_score: 0.92
---

## Context
The publish action is the final mile of Content Factory — it takes any generated content
and routes it to the appropriate distribution channels. It acts as a dispatcher, selecting
the right workflow (YouTube, social, Hotmart, email) based on the channels list.
Purpose: single entry point for all content distribution, regardless of channel.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| content_path | string | Relative file path to content asset | YES |
| channels | list[string] | Channel identifiers | YES |
| publish_mode | enum | immediate, scheduled, draft | YES |
| brand_config | object | {{BRAND_*}} YAML variables | YES |
| schedule_time | datetime | ISO 8601 | NO (required if scheduled) |

## Execution
1. Validate brand_config completeness and content_path accessibility
2. For each channel, select the corresponding distribution workflow
3. Format content payload per channel requirements (metadata, thumbnails, descriptions)
4. Dispatch to workflow and return publish manifest with per-channel status

## Output
Format: YAML
Structure:
```yaml
publish_manifest:
  content: "{{content_path}}"
  timestamp: "{{ISO_8601}}"
  channels:
    youtube:
      workflow: "wf_cf_publish_youtube"
      status: "published"
      url: "{{result_url}}"
    instagram:
      workflow: "wf_cf_publish_social"
      status: "scheduled"
      scheduled_at: "{{datetime}}"
    hotmart:
      workflow: "wf_cf_publish_hotmart"
      status: "draft"
      draft_id: "{{id}}"
  errors: []
```

## Validation
- Every channel in input has a corresponding status in manifest
- No channel left without workflow mapping (unknown channels → error entry)
- Brand_config validated before any API call
- Edge case: incompatible content type handled with excerpt fallback
- publish_mode respected across all channels consistently

## References
- wf_cf_publish_youtube, wf_cf_publish_social, wf_cf_publish_hotmart, wf_cf_email_launch
- Ayrshare API, YouTube API, Hotmart API
- brand_config.yaml (validation gate)
