---
kind: examples
id: bld_examples_social_publisher
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of social publisher configs
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: social-publisher-builder

## Golden Example — Pet Shop ({{BRAND_NAME}})
INPUT: "Create social publisher config for {{BRAND_NAME}}, a minimalist cat accessories brand on IG and FB"
OUTPUT:
```yaml
identity:
  empresa: {{BRAND_NAME}}
  handle: "@{{BRAND_DOMAIN}}"
  nicho: pet
  tom: casual, acolhedor
  persona: Ro
  bio: "Design minimalist para gatos exigentes"
platforms: [instagram, facebook]
schedule:
  timezone: America/Sao_Paulo
  calendar:
    monday: { type: educational, time: "12:00" }
    tuesday: { type: tips, time: "19:00" }
    wednesday: { type: product, time: "13:00" }
    thursday: { type: educational, time: "12:00" }
    friday: { type: trend, time: "19:00" }
    saturday: { type: tips, time: "10:00" }
    sunday: { type: product, time: "11:00" }
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
publisher:
  type: ayrshare
  api_key_env: AYRSHARE_API_KEY
  batch_size: 3
  retry: { max: 3, backoff: exponential, base_seconds: 30 }
hashtags:
  brand: ["{{BRAND_NAME}}", "{{BRAND_DOMAIN}}"]
  niche: ["produtosparagatos", "designminimalist", "petlovers"]
  max_per_post: 10
notifications:
  discord_webhook_env: DISCORD_WEBHOOK_URL
```
WHY GOOD: Zero hardcoded secrets, all company data in config, percentages sum to 100, retry defined, timezone explicit.

## Anti-Example — Hardcoded System
```python
# BAD: company name hardcoded everywhere
COMPANY = "{{BRAND_NAME}}"
API_KEY = "sk-abc123..."  # LEAKED SECRET
def post_to_instagram():
    caption = f"Nova collection {COMPANY}! 🐱"  # hardcoded template
    ayrshare.post(caption, api_key=API_KEY)   # no retry
```
WHY BAD: Hardcoded name, plaintext API key, no retry, no rotation, single platform, no quality gate.

## Golden Example — SaaS B2B
```yaml
identity:
  empresa: CloudMetrics
  handle: "@cloudmetrics"
  nicho: saas
  tom: professional, data-driven
  persona: Alex
platforms: [linkedin, twitter]
content_mix: { product: 30, educational: 40, tips: 20, trends: 10 }
catalog:
  type: api
  url_env: CMS_API_URL
  key_env: CMS_API_KEY
  cooldown_days: 7
publisher:
  type: postiz
  base_url_env: POSTIZ_URL
  api_key_env: POSTIZ_KEY
  batch_size: 2
  retry: { max: 3, backoff: exponential, base_seconds: 60 }
```
WHY GOOD: Different niche, different platforms, different API — same config schema works.

## Exemplar Requirements

1. Score 9.0+ to qualify as few-shot reference
2. Demonstrate ideal structure for this artifact kind
3. Populate all frontmatter fields with realistic values
4. Use domain-specific content not generic placeholders
5. Enable retrieval via tags and TF-IDF matching

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | social publisher construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
