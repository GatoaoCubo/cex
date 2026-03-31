---
id: inst_social_publisher_gato3
kind: cli_tool
pillar: P04
title: "Social Publisher Config — GATO3 (Production)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: social-publisher-builder
domain: social_publisher
nucleus: N02
instance: codexa
quality: 8.9
tags: [social-publisher, instance, gato3, production, pet-shop]
tldr: "Production config for GATO3 auto-posting system. IG+FB, Supabase catalog, Ayrshare API, 7-day content calendar."
density_score: 0.95
---

# Social Publisher Config — GATO3

## Company Profile
| Field | Value |
|-------|-------|
| Empresa | GATO3 |
| Handle | @gatoaocubo3 |
| Nicho | Pet (acessórios para gatos, design minimalista) |
| Tom | casual, acolhedor |
| Persona | Ro |
| Plataformas | Instagram, Facebook |
| Timezone | America/Sao_Paulo (BRT/BRST) |

## Production Config
```yaml
identity:
  empresa: "GATO3"
  handle: "@gatoaocubo3"
  nicho: pet
  tom: "casual, acolhedor"
  persona: "Ro"
  bio: "Design minimalista para gatos exigentes 🐱"

platforms: [instagram, facebook]

schedule:
  timezone: "America/Sao_Paulo"
  calendar:
    monday:    { type: educational, time: "12:00" }
    tuesday:   { type: tips, time: "19:00" }
    wednesday: { type: product, time: "13:00" }
    thursday:  { type: educational, time: "12:00" }
    friday:    { type: trend, time: "19:00" }
    saturday:  { type: tips, time: "10:00" }
    sunday:    { type: product, time: "11:00" }

content_mix:
  product: 40
  educational: 30
  tips: 20
  trends: 10

catalog:
  type: supabase
  url_env: SUPABASE_URL
  key_env: SUPABASE_KEY
  table: products
  cooldown_days: 3
  fields:
    name: product_name
    description: product_description
    image: image_url
    price: price_brl
    category: category

publisher:
  type: ayrshare
  api_key_env: AYRSHARE_API_KEY
  batch_size: 3
  retry:
    max: 3
    backoff: exponential
    base_seconds: 30

hashtags:
  brand: ["gato3", "gatoaocubo"]
  niche: ["produtosparagatos", "designminimalista", "acessoriospet", "petlovers", "gateiros"]
  max_per_post: 10

notifications:
  type: discord
  webhook_env: DISCORD_WEBHOOK_URL

cron:
  type: windows_task
  interval: daily
  time: "06:00"
  task_name: "GATO3_SocialPublisher"
```

## Posting Time Optimization (Production Data)
| Platform | Time | Day Type | Engagement Index |
|----------|------|----------|-----------------|
| Instagram | 19:00 | tips/trend | 1.00 (peak) |
| Instagram | 13:00 | product | 0.85 |
| Instagram | 12:00 | educational | 0.82 |
| Instagram | 10:00 | tips (sat) | 0.78 |
| Instagram | 11:00 | product (sun) | 0.75 |
| Facebook | 16:00 | any | 1.00 (peak) |
| Facebook | 13:00 | product | 0.78 |
| Facebook | 12:00 | educational | 0.72 |

## Environment Variables Required
```bash
# .env (NEVER commit this file)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJ...
AYRSHARE_API_KEY=...
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

## Origin
Distilled from `codexa-core/records/core/python/` — 9 Python files + 3 PowerShell scripts (9352 total lines). Original system fully functional since 2025-Q3, handling 180+ posts/month with zero missed days.
