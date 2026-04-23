---
kind: quality_gate
id: p11_qg_social_publisher
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of social publisher configs
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Gate: social_publisher"
version: 1.0.0
author: n03_engineering
tags: [quality-gate, social-publisher, P11, automation, governance]
tldr: "Gates for social publisher artifacts — config completeness, pipeline coverage, security, and reusability."
domain: social_publisher
created: 2026-03-31
updated: 2026-03-31
density_score: 1.0
related:
  - bld_examples_social_publisher
  - bld_output_template_social_publisher
  - tpl_social_publisher
  - bld_instruction_social_publisher
  - p03_sp_social_publisher_builder
  - bld_schema_social_publisher
  - n02_tool_social_publisher
  - p11_qg_quality_gate
  - ex_social_publisher_bakery
  - ex_social_publisher_saas
---

## Quality Gate

# Gate: social_publisher

## Definition
| Field | Value |
|-------|-------|
| Kind | social_publisher (cli_tool/workflow instances) |
| Pillar | P04 (tools) |
| Function | CALL (automation pipeline) |
| Threshold | 8.0 minimum |

## HARD Gates (fail = reject)
| # | Gate | Check |
|---|------|-------|
| H1 | Config completeness | All 7 required sections present (identity, platforms, schedule, content_mix, catalog, publisher, hashtags) |
| H2 | Zero hardcoded secrets | No API keys, tokens, or passwords in plaintext — only ENV_VAR references |
| H3 | Pipeline coverage | All 10 steps documented (LOAD through ROTATE) |
| H4 | Mix sum validation | content_mix percentages sum to exactly 100 |
| H5 | Platform validity | All listed platforms are supported (ig/fb/tt/li/tw/yt) |
| H6 | Retry defined | publisher.retry section present with max, backoff, base_seconds |
| H7 | Timezone explicit | schedule.timezone is valid IANA timezone string |

## SOFT Gates (warn, don't reject)
| # | Gate | Check | Weight |
|---|------|-------|--------|
| S1 | Company-agnostic | No hardcoded company names outside identity section | 1.0 |
| S2 | Multi-provider | At least 2 publisher types documented | 0.8 |
| S3 | Cooldown defined | catalog.cooldown_days >= 1 | 0.7 |
| S4 | Notification channel | notifications section present and configured | 0.5 |
| S5 | Cron scheduling | cron section with type and interval | 0.5 |
| S6 | Caption guidelines | Min/max caption length per platform | 0.6 |
| S7 | Hashtag strategy | Brand + niche hashtags defined, max_per_post set | 0.7 |
| S8 | Failure modes | Each pipeline step has documented failure → recovery | 0.8 |
| S9 | A/B testing | Config supports variant testing for captions | 0.3 |
| S10 | Analytics hook | Post-publish metrics collection defined | 0.4 |

## Scoring Formula
```
score = (HARD_pass_count / 7) * 6.0 + (SOFT_weighted_sum / max_weight) * 4.0
```
All 7 HARD must pass for score >= 6.0. SOFT gates add up to 4.0 bonus.

## Quality Tiers
| Tier | Score | Meaning |
|------|-------|---------|
| REJECT | < 8.0 | Missing required sections or security violation |
| PUBLISH | 8.0-8.9 | Config complete, pipeline documented, secure |
| EXEMPLARY | 9.0+ | Multi-provider, full failure modes, A/B support |

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental social_publisher artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
