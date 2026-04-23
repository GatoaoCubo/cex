---
kind: schema
id: bld_schema_content_monetization
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for content_monetization config
pattern: CONFIG derives from this. TEMPLATE renders this.
quality: 9.1
title: "Schema Content Monetization"
version: "1.0.0"
author: n03_builder
tags: [content_monetization, builder, examples]
tldr: "Golden and anti-examples for content monetization construction, demonstrating ideal structure and common pitfalls."
domain: "content monetization construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_social_publisher
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_research_pipeline
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_bugloop
  - bld_schema_sandbox_config
  - bld_schema_optimizer
---

# Schema: content_monetization

## Config Schema (the YAML every company fills)

### identity (required)
| Field | Type | Required | Example |
|-------|------|----------|---------|
| empresa | string | YES | "CODEXA" |
| domain | string | YES | "ai_tools" |
| currency | enum(BRL,USD,EUR) | YES | "BRL" |
| currency_unit | enum(centavos,cents) | YES | "centavos" |
| country | enum(BR,US,EU,UK,LATAM) | YES | "BR" |

### pricing (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| strategy | enum(freemium,tiered,usage,credit_pack,hybrid) | YES | "tiered" |
| tiers | list[tier_object] | YES | - |
| tier.name | string | YES | "pro" |
| tier.price_monthly | integer (centavos/cents) | YES | 4990 |
| tier.price_yearly | integer | NO | 49900 |
| tier.credits_monthly | integer | YES | 1000 |
| tier.features | list[string] | YES | ["research", "publish"] |
| floor_margin_pct | float (0.0-1.0) | YES | 0.30 |
| trial_days | integer | NO | 7 |

### credits (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| pipeline_costs | map[string,int] | YES | {research: 50} |
| packs | list[pack] | NO | - |
| overdraft_policy | enum(block,notify_then_block,allow_negative) | YES | "block" |
| rollover | boolean | NO | false |

### checkout (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| provider | enum(stripe,hotmart,kiwify,monetizze,eduzz,digistore24) | YES | "stripe" |
| webhook_url | string (URL) | YES | - |
| webhook_secret_env | string (ENV_VAR) | YES | "CHECKOUT_WEBHOOK_SECRET" |
| idempotency | boolean | YES | true |
| success_redirect | string (URL) | YES | - |
| cancel_redirect | string (URL) | YES | - |
| mock_mode | boolean | NO | true |

### checkout_ds24 (when provider=digistore24)
| Field | Type | Default |
|-------|------|---------|
| ds24_product_id | string | - |
| ds24_api_key_env | ENV_VAR | "DS24_API_KEY" |
| ipn_url | URL | - |
| ipn_passphrase_env | ENV_VAR | "DS24_IPN_PASSPHRASE" |
| ipn_format | const | "form-encoded" |
| ipn_response | const | "OK" |
| signature_algo | const | "sha512" |
| merchant_of_record | enum(ds24,self) | "ds24" |
| eu_vat_included | boolean | true |

### checkout_hotmart (when provider=hotmart)
| Field | Type | Default |
|-------|------|---------|
| hotmart_product_id | string | - |
| hotmart_token_env | ENV_VAR | "HOTMART_TOKEN" |
| hottok_env | ENV_VAR | "HOTMART_HOTTOK" |
| webhook_format | const | "json" |
| signature_algo | const | "sha256_hmac" |

### courses (optional)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| enabled | boolean | YES | false |
| modules | list[module_object] | COND | - |
| module.title | string | YES | - |
| module.lessons | list[lesson_object] | YES | - |
| module.drip_days | integer | NO | 0 |
| certification | boolean | NO | false |
| completion_threshold | float (0.0-1.0) | NO | 0.80 |

### ads (optional)
| Field | Type | Default |
|-------|------|---------|
| platforms | list[enum(meta,google,tiktok,linkedin)] | - |
| monthly_budget | int (centavos) | - |
| pixel_env | ENV_VAR | "META_PIXEL_ID" |

### emails (optional)
| Field | Type | Default |
|-------|------|---------|
| provider | enum(resend,sendgrid,ses,mailchimp) | "resend" |
| api_key_env | ENV_VAR | "EMAIL_API_KEY" |
| sequences | list[sequence] | - |

### validation (required)
margin_check: true, webhook_test: true, mock_before_live: true

## Rules
1. Prices in centavos/cents (integers). 2. floor_margin >= 0.30.
3. Secrets: ENV_VAR only. 4. mock_mode: true in dev. 5. Min 1 tier.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_social_publisher]] | sibling | 0.59 |
| [[bld_schema_usage_report]] | sibling | 0.56 |
| [[bld_schema_quickstart_guide]] | sibling | 0.55 |
| [[bld_schema_research_pipeline]] | sibling | 0.54 |
| [[bld_schema_dataset_card]] | sibling | 0.54 |
| [[bld_schema_reranker_config]] | sibling | 0.54 |
| [[bld_schema_pitch_deck]] | sibling | 0.53 |
| [[bld_schema_bugloop]] | sibling | 0.52 |
| [[bld_schema_sandbox_config]] | sibling | 0.52 |
| [[bld_schema_optimizer]] | sibling | 0.51 |
