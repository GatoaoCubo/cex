---
id: ex_social_publisher_clothing
kind: cli_tool
pillar: P04
title: "Social Publisher — Fashion Brand (Clothing Niche)"
version: 1.0.0
created: 2026-03-31
author: social-publisher-builder
domain: social_publisher
quality: 9.1
tags: [social-publisher, example, fashion, clothing, instagram, tiktok, pinterest]
tldr: "Config for fashion brand — IG+TikTok+Pinterest, Airtable catalog, visual-driven strategy with evening posting."
density_score: 0.88
updated: "2026-04-07"
related:
  - bld_output_template_social_publisher
  - tpl_social_publisher
  - ex_social_publisher_bakery
  - bld_examples_social_publisher
  - ex_social_publisher_saas
  - n02_kc_social_publishing
  - bld_schema_social_publisher
  - p12_wf_weekly_fashion_content
  - bld_instruction_social_publisher
  - p03_sp_social_publisher_builder
---

# Social Publisher — Fashion Brand

## About
Config for a contemporary women's fashion brand. Instagram, TikTok, and Pinterest — visual platforms where fashion content performs best. Evening posting optimized for browse-and-buy behavior.

## Config
```yaml
identity:
  empresa: "Atelier Noa"
  handle: "@ateliernoa"
  nicho: fashion
  tom: "elegant, contemporary, empowering"
  persona: "Noa"
  bio: "Moda contemporânea para mulheres que lideram ✨"

platforms: [instagram, tiktok, pinterest]

schedule:
  timezone: "America/Sao_Paulo"
  calendar:
    monday:    { type: product, time: "19:00" }
    tuesday:   { type: educational, time: "12:00" }
    wednesday: { type: product, time: "19:00" }
    thursday:  { type: trend, time: "20:00" }
    friday:    { type: product, time: "18:00" }
    saturday:  { type: tips, time: "11:00" }
    sunday:    { type: educational, time: "10:00" }

content_mix:
  product: 45
  educational: 20
  tips: 15
  trends: 20

catalog:
  type: airtable
  url_env: AIRTABLE_API_URL
  key_env: AIRTABLE_API_KEY
  table: collection_ss26
  cooldown_days: 4

publisher:
  type: ayrshare
  api_key_env: AYRSHARE_API_KEY
  batch_size: 3
  retry:
    max: 3
    backoff: exponential
    base_seconds: 30

hashtags:
  brand: ["ateliernoa", "noafashion"]
  niche: ["modacontemporanea", "fashionbrasil", "ootd", "streetstyle", "lookdodia"]
  max_per_post: 15

notifications:
  type: discord
  webhook_env: DISCORD_WEBHOOK_URL

cron:
  type: windows_task
  interval: daily
```

## Niche Notes
- **3 platforms**: fashion thrives on visual platforms; Pinterest drives long-tail traffic
- **Evening posting** (18-20h): fashion audience browses after work → highest impulse purchase window
- **Higher trends %** (20): fashion is trend-driven; seasonal/collection content must stay current
- **Pinterest strategy**: pins have 4-month average lifespan vs 24h for IG → SEO value
- **Airtable catalog**: fashion brands manage seasonal collections → Airtable enables collection-based filtering
- **Higher hashtag limit** (15): fashion IG posts benefit from more hashtags (discoverability)
- **4-day cooldown**: fashion products need variety — same dress 2x/week kills exclusivity perception
- **TikTok evening** (20h): Gen-Z fashion audience peaks at 20-22h — try-on hauls, styling tips

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_social_publisher_clothing`
- **Tags**: [social-publisher, example, fashion, clothing, instagram, tiktok, pinterest]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_social_publisher]] | downstream | 0.46 |
| [[tpl_social_publisher]] | sibling | 0.43 |
| [[ex_social_publisher_bakery]] | sibling | 0.40 |
| [[bld_examples_social_publisher]] | downstream | 0.38 |
| [[ex_social_publisher_saas]] | sibling | 0.32 |
| [[n02_kc_social_publishing]] | upstream | 0.32 |
| [[bld_schema_social_publisher]] | downstream | 0.29 |
| [[p12_wf_weekly_fashion_content]] | downstream | 0.28 |
| [[bld_instruction_social_publisher]] | upstream | 0.23 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.22 |
