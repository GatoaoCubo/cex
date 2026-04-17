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

