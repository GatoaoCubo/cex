---
id: ex_social_publisher_ayrshare
kind: social_publisher
pillar: P05
title: "Example Social Publisher: Ayrshare Routing"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.7
brand_placeholders:
  - BRAND_NAME
  - BRAND_AYRSHARE_API_KEY
  - BRAND_DOMAIN
tags: [social_publisher, ayrshare, distribution, n02]
tldr: "Publishing contract for shipping approved social assets through Ayrshare with brand-safe metadata."
density_score: 0.88
related:
  - p12_wf_cf_publish_social
  - p01_kc_social_publisher
  - p11_qg_runtime_state
  - bld_knowledge_card_social_publisher
  - p11_qg_chunk_strategy
  - n02_tool_social_publisher
  - p11_qg_quality_gate
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_handoff_protocol
---

# Publish Contract

```yaml
provider: ayrshare
auth_env: BRAND_AYRSHARE_API_KEY
required_fields:
  - channel
  - text
  - media_urls
  - publish_at
  - canonical_url
optional_fields:
  - first_comment
  - alt_text
  - tags
  - campaign_id
```

## Rules

- Publish only assets that passed the quality gate.
- Set `canonical_url` to a `{{BRAND_DOMAIN}}` destination when one exists.
- Attach platform-specific alt text when media is present.
- Log publish ID, channel, scheduled time, and retry state.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_cf_publish_social]] | downstream | 0.22 |
| [[p01_kc_social_publisher]] | upstream | 0.20 |
| [[p11_qg_runtime_state]] | downstream | 0.18 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.17 |
| [[p11_qg_chunk_strategy]] | downstream | 0.17 |
| [[n02_tool_social_publisher]] | upstream | 0.17 |
| [[p11_qg_quality_gate]] | downstream | 0.17 |
| [[p11_qg_memory_scope]] | downstream | 0.16 |
| [[p11_qg_retriever_config]] | downstream | 0.16 |
| [[p11_qg_handoff_protocol]] | downstream | 0.16 |
