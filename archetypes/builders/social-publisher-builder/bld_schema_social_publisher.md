---
kind: schema
id: bld_schema_social_publisher
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for social_publisher config
pattern: CONFIG derives from this. TEMPLATE renders this.
quality: 9.2
title: "Schema Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: social_publisher

## Config Schema (the YAML every company fills)

### identity (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| empresa | string | YES | "{{BRAND_NAME}}" |
| handle | string | YES | "@{{BRAND_DOMAIN}}" |
| nicho | enum(pet,food,saas,fashion,fitness,beauty,tech,education,costm) | YES | "pet" |
| tom | string | YES | "casual, acolhedor" |
| persona | string | YES | "Ro" |
| bio | string(≤160) | YES | "Design minimalist para gatos" |

### platforms (required)
| Type | Constraint | Example |
|------|-----------|---------|
| list[enum] | min 1, values: instagram,facebook,tiktok,linkedin,twitter,youtube | [instagram, facebook] |

### schedule (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| timezone | IANA timezone string | YES | "America/Sao_Paulo" |
| calendar | map[weekday → {type, time}] | YES | see template |
| calendar.*.type | enum(product,educational,tips,trends) | YES | "product" |
| calendar.*.time | HH:MM (24h) | YES | "19:00" |

### content_mix (required)
| Field | Type | Required | Constraint |
|-------|------|----------|-----------|
| product | int(0-100) | YES | sum=100 |
| educational | int(0-100) | YES | sum=100 |
| tips | int(0-100) | YES | sum=100 |
| trends | int(0-100) | YES | sum=100 |

### catalog (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| type | enum(supabase,shopify,airtable,csv,api,manual) | YES | "supabase" |
| url_env | string (ENV_VAR name) | YES | "SUPABASE_URL" |
| key_env | string (ENV_VAR name) | CONDITIONAL | "SUPABASE_KEY" |
| table | string | CONDITIONAL | "products" |
| cooldown_days | int(1-30) | YES | 3 |

### publisher (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| type | enum(ayrshare,postiz,meta_graph) | YES | "ayrshare" |
| api_key_env | string (ENV_VAR name) | YES | "AYRSHARE_API_KEY" |
| batch_size | int(1-10) | YES | 3 |
| retry.max | int(1-5) | YES | 3 |
| retry.backoff | enum(exponential,linear,fixed) | YES | "exponential" |
| retry.base_seconds | int(10-300) | YES | 30 |

### hashtags (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| brand | list[string] | YES | ["{{BRAND_NAME}}", "{{BRAND_DOMAIN}}"] |
| niche | list[string] | YES | ["petlovers"] |
| max_per_post | int(1-30) | YES | 10 |

### notifications (optional)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| type | enum(discord,slack,email,none) | NO | "discord" |
| webhook_env | string (ENV_VAR name) | CONDITIONAL | "DISCORD_WEBHOOK_URL" |

### cron (optional)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| type | enum(windows_task,crontab,systemd) | NO | "windows_task" |
| interval | string | NO | "daily" |

## Validation Rules
1. content_mix values MUST sum to exactly 100
2. All *_env fields MUST be SCREAMING_SNAKE_CASE
3. No plaintext secrets anywhere in the config
4. At least 1 platform in platforms list
5. cooldown_days >= 1 (never 0 — prevents spam)
