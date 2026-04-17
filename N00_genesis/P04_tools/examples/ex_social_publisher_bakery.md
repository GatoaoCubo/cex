---
id: ex_social_publisher_bakery
kind: cli_tool
pillar: P04
title: "Social Publisher — Artisan Bakery (Food Niche)"
version: 1.0.0
created: 2026-03-31
author: social-publisher-builder
domain: social_publisher
quality: 9.0
tags: [social-publisher, example, bakery, food, instagram, tiktok]
tldr: "Config for artisan bakery — IG+TikTok, Shopify catalog, visual-first content strategy with morning posting."
density_score: 0.88
updated: "2026-04-07"
---

# Social Publisher — Artisan Bakery

## About
Config for a local artisan bakery posting daily on Instagram and TikTok. Visual-first strategy emphasizing food photography and behind-the-scenes baking content.

## Config
```yaml
identity:
  empresa: "Forno & Massa"
  handle: "@fornoemmassa"
  nicho: food
  tom: "warm, artisanal, sensory"
  persona: "Chef Ana"
  bio: "Pão artesanal feito com amor e fermentação natural 🍞"

platforms: [instagram, tiktok]

schedule:
  timezone: "America/Sao_Paulo"
  calendar:
    monday:    { type: product, time: "07:30" }
    tuesday:   { type: educational, time: "11:00" }
    wednesday: { type: product, time: "07:30" }
    thursday:  { type: tips, time: "19:00" }
    friday:    { type: product, time: "07:30" }
    saturday:  { type: trend, time: "10:00" }
    sunday:    { type: educational, time: "09:00" }

content_mix:
  product: 45
  educational: 25
  tips: 15
  trends: 15

catalog:
  type: shopify
  url_env: SHOPIFY_STORE_URL
  key_env: SHOPIFY_API_KEY
  table: products
  cooldown_days: 2

publisher:
  type: ayrshare
  api_key_env: AYRSHARE_API_KEY
  batch_size: 2
  retry:
    max: 3
    backoff: exponential
    base_seconds: 30

hashtags:
  brand: ["fornoemmassa", "paoartesanal"]
  niche: ["fermentacaonatural", "sourdough", "padaria", "bakerylife", "foodporn"]
  max_per_post: 12

notifications:
  type: slack
  webhook_env: SLACK_WEBHOOK_URL

cron:
  type: crontab
  interval: daily
```

## Niche Notes
- **Morning posting** (07:30): bakery audience checks IG before work → "fresh bread" impulse
- **TikTok evening** (19:00): behind-the-scenes baking videos perform best after dinner
- **Higher product %** (45): visual food products drive direct sales more than educational
- **Short cooldown** (2 days): bakeries rotate inventory faster than other niches
- **Sensory language**: captions emphasize smell, texture, warmth — food engagement drivers

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_social_publisher_bakery`
- **Tags**: [social-publisher, example, bakery, food, instagram, tiktok]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |
