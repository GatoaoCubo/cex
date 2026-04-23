---
id: ex_social_publisher_saas
kind: cli_tool
pillar: P04
title: "Social Publisher — B2B SaaS (Professional Niche)"
version: 1.0.0
created: 2026-03-31
author: social-publisher-builder
domain: social_publisher
quality: 9.0
tags: [social-publisher, example, saas, b2b, linkedin, twitter]
tldr: "Config for B2B SaaS — LinkedIn+Twitter, CMS API catalog, thought-leadership content strategy with business-hours posting."
density_score: 0.88
updated: "2026-04-07"
related:
  - bld_examples_social_publisher
  - tpl_social_publisher
  - bld_output_template_social_publisher
  - ex_social_publisher_bakery
  - n02_kc_social_publishing
  - ex_social_publisher_clothing
  - bld_schema_social_publisher
  - p03_sp_social_publisher_builder
  - bld_knowledge_card_social_publisher
  - bld_instruction_social_publisher
---

# Social Publisher — B2B SaaS

## About
Config for a B2B SaaS analytics platform. LinkedIn and Twitter focused, with thought-leadership content and data-driven case studies. Business-hours posting aligned to US Eastern timezone.

## Config
```yaml
identity:
  empresa: "CloudMetrics"
  handle: "@cloudmetrics"
  nicho: saas
  tom: "professional, data-driven, authoritative"
  persona: "Alex"
  bio: "Real-time analytics for modern engineering teams 📊"

platforms: [linkedin, twitter]

schedule:
  timezone: "US/Eastern"
  calendar:
    monday:    { type: educational, time: "09:00" }
    tuesday:   { type: product, time: "10:00" }
    wednesday: { type: tips, time: "09:00" }
    thursday:  { type: educational, time: "10:00" }
    friday:    { type: trend, time: "09:00" }
    saturday:  { type: educational, time: "10:00" }
    sunday:    { type: tips, time: "11:00" }

content_mix:
  product: 25
  educational: 40
  tips: 25
  trends: 10

catalog:
  type: api
  url_env: CMS_API_URL
  key_env: CMS_API_KEY
  table: blog_posts
  cooldown_days: 7

publisher:
  type: postiz
  base_url_env: POSTIZ_URL
  api_key_env: POSTIZ_API_KEY
  batch_size: 2
  retry:
    max: 3
    backoff: exponential
    base_seconds: 60

hashtags:
  brand: ["cloudmetrics", "realtimeanalytics"]
  niche: ["devtools", "observability", "dataengineering", "saas"]
  max_per_post: 5

notifications:
  type: slack
  webhook_env: SLACK_WEBHOOK_URL

cron:
  type: crontab
  interval: daily
```

## Niche Notes
- **LinkedIn dominance**: B2B audience is on LinkedIn 9-11am; Twitter supplements with quick takes
- **High educational %** (40): SaaS buyers research before purchase → thought leadership builds trust
- **Low product %** (25): direct promotion on LI/TW feels spammy → wrap in case studies
- **Long cooldown** (7 days): B2B content has longer shelf life, reposting feels repetitive
- **Postiz (self-hosted)**: SaaS companies prefer self-hosted for data control and no vendor lock-in
- **Twitter brevity**: 280 chars forces punchy, data-driven hooks ("We analyzed 10M events...")
- **Weekend posting** (Sat/Sun reduced): B2B engagement drops 60% on weekends

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_social_publisher_saas`
- **Tags**: [social-publisher, example, saas, b2b, linkedin, twitter]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_social_publisher]] | downstream | 0.46 |
| [[tpl_social_publisher]] | sibling | 0.45 |
| [[bld_output_template_social_publisher]] | downstream | 0.44 |
| [[ex_social_publisher_bakery]] | sibling | 0.33 |
| [[n02_kc_social_publishing]] | upstream | 0.30 |
| [[ex_social_publisher_clothing]] | sibling | 0.26 |
| [[bld_schema_social_publisher]] | downstream | 0.25 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.23 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.23 |
| [[bld_instruction_social_publisher]] | upstream | 0.22 |
