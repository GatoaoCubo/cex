---
id: tpl_social_publisher
kind: cli_tool
pillar: P04
title: "Social Publisher — Config-Driven Auto-Posting Pipeline"
version: 1.0.0
created: 2026-03-31
author: social-publisher-builder
domain: social_publisher
quality: 9.1
tags: [social-publisher, automation, template, pipeline, social-media]
tldr: "Template for config-driven social media auto-posting. Fill 1 YAML = automated posting to IG/FB/TT/LI/TW."
density_score: 1.0
updated: "2026-04-07"
related:
  - bld_output_template_social_publisher
  - bld_knowledge_card_social_publisher
  - bld_examples_social_publisher
  - ex_social_publisher_saas
  - p03_sp_social_publisher_builder
  - bld_instruction_social_publisher
  - n02_tool_social_publisher
  - n02_kc_social_publishing
  - bld_schema_social_publisher
  - ex_social_publisher_bakery
---

# Social Publisher — Template

## Overview
Config-driven pipeline for automated social media posting. Any business fills ONE YAML config file and gets scheduled posting across Instagram, Facebook, TikTok, LinkedIn, and Twitter.

## Pipeline (10 Steps)
| Step | Name | Input | Output |
|------|------|-------|--------|
| 1 | LOAD | config YAML path | parsed config |
| 2 | FETCH | catalog source (API/DB/CSV) | content list |
| 3 | SELECT | content list + rotation state | next item (cooldown-aware) |
| 4 | GENERATE | item + persona + tone | caption text via LLM |
| 5 | OPTIMIZE | platform + timezone | best posting datetime |
| 6 | HASHTAGS | niche + brand tags + limits | hashtag string |
| 7 | PUBLISH | caption + media + API config | post ID + URL |
| 8 | LOG | post result + metadata | structured JSON log |
| 9 | NOTIFY | post URL + channel config | notification sent |
| 10 | ROTATE | posted item ID + cooldown | rotation state updated |

## Config Schema (what the business fills)
```yaml
identity:
  empresa: "{{COMPANY_NAME}}"
  handle: "{{SOCIAL_HANDLE}}"
  nicho: "{{NICHE}}"           # pet, food, saas, fashion, fitness
  tom: "{{TONE}}"              # casual, professional, playful
  persona: "{{PERSONA_NAME}}"
  bio: "{{BRAND_BIO}}"

platforms: [{{PLATFORMS}}]      # instagram, facebook, tiktok, linkedin, twitter

schedule:
  timezone: "{{TIMEZONE}}"     # IANA: America/Sao_Paulo, US/Eastern
  calendar:
    monday:    { type: "{{TYPE}}", time: "{{HH:MM}}" }
    tuesday:   { type: "{{TYPE}}", time: "{{HH:MM}}" }
    wednesday: { type: "{{TYPE}}", time: "{{HH:MM}}" }
    thursday:  { type: "{{TYPE}}", time: "{{HH:MM}}" }
    friday:    { type: "{{TYPE}}", time: "{{HH:MM}}" }
    saturday:  { type: "{{TYPE}}", time: "{{HH:MM}}" }
    sunday:    { type: "{{TYPE}}", time: "{{HH:MM}}" }

content_mix:               # MUST sum to 100
  product: {{PCT}}
  educational: {{PCT}}
  tips: {{PCT}}
  trends: {{PCT}}

catalog:
  type: "{{SOURCE}}"       # supabase, shopify, airtable, csv, api
  url_env: "{{URL_ENV}}"
  key_env: "{{KEY_ENV}}"
  table: "{{TABLE}}"
  cooldown_days: {{DAYS}}

publisher:
  type: "{{API}}"          # ayrshare, postiz, meta_graph
  api_key_env: "{{API_KEY_ENV}}"
  batch_size: {{N}}
  retry:
    max: {{N}}
    backoff: exponential
    base_seconds: {{N}}

hashtags:
  brand: [{{BRAND_TAGS}}]
  niche: [{{NICHE_TAGS}}]
  max_per_post: {{N}}

notifications:
  type: "{{CHANNEL}}"      # discord, slack, email, none
  webhook_env: "{{WEBHOOK_ENV}}"

cron:
  type: "{{SCHEDULER}}"    # windows_task, crontab, systemd
  interval: "{{INTERVAL}}" # daily, every_6h, cron expression
```

## Quality Gates
| Gate | Rule | Severity |
|------|------|----------|
| Config complete | All 7 required sections present | HARD |
| No secrets | Zero plaintext API keys | HARD |
| Mix sum | content_mix = 100 | HARD |
| Timezone valid | IANA format | HARD |
| Retry defined | max + backoff + base_seconds | HARD |
| Cooldown >= 1 | No spam | HARD |
| Multi-provider | Supports 2+ publisher APIs | SOFT |

## Supported Publishers
| Provider | Type | Networks | Auth |
|----------|------|----------|------|
| Ayrshare | SaaS | 6+ networks | Bearer token |
| Postiz | Self-hosted OSS | 6+ networks | API key |
| Meta Graph | Direct API | IG + FB only | OAuth token |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_social_publisher]] | downstream | 0.48 |
| [[bld_knowledge_card_social_publisher]] | upstream | 0.40 |
| [[bld_examples_social_publisher]] | downstream | 0.39 |
| [[ex_social_publisher_saas]] | sibling | 0.36 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.36 |
| [[bld_instruction_social_publisher]] | upstream | 0.35 |
| [[n02_tool_social_publisher]] | sibling | 0.34 |
| [[n02_kc_social_publishing]] | upstream | 0.33 |
| [[bld_schema_social_publisher]] | downstream | 0.33 |
| [[ex_social_publisher_bakery]] | sibling | 0.32 |
