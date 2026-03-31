---
kind: examples
id: bld_examples_social_publisher
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of social publisher configs
pattern: few-shot learning — LLM reads these before producing
---

# Examples: social-publisher-builder

## Golden Example — Pet Shop (GATO3)
INPUT: "Create social publisher config for GATO3, a minimalist cat accessories brand on IG and FB"
OUTPUT:
```yaml
identity:
  empresa: GATO3
  handle: "@gatoaocubo3"
  nicho: pet
  tom: casual, acolhedor
  persona: Ro
  bio: "Design minimalista para gatos exigentes"
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
  brand: ["gato3", "gatoaocubo"]
  niche: ["produtosparagatos", "designminimalista", "petlovers"]
  max_per_post: 10
notifications:
  discord_webhook_env: DISCORD_WEBHOOK_URL
```
WHY GOOD: Zero hardcoded secrets, all company data in config, percentages sum to 100, retry defined, timezone explicit.

## Anti-Example — Hardcoded System
```python
# BAD: company name hardcoded everywhere
COMPANY = "GATO3"
API_KEY = "sk-abc123..."  # LEAKED SECRET
def post_to_instagram():
    caption = f"Nova colecao {COMPANY}! 🐱"  # hardcoded template
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
