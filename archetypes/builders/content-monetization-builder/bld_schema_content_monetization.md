---
kind: schema
id: bld_schema_content_monetization
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for content_monetization config
pattern: CONFIG derives from this. TEMPLATE renders this.
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
| unit_name | string | YES | "credit" |
| pipeline_costs | map[string,integer] | YES | {research: 50, publish: 10} |
| packs | list[pack_object] | NO | - |
| pack.name | string | YES | "starter_pack" |
| pack.credits | integer | YES | 500 |
| pack.price | integer (centavos) | YES | 2990 |
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

### checkout_ds24 (required when provider=digistore24)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| ds24_product_id | string | YES | - |
| ds24_api_key_env | string (ENV_VAR) | YES | "DS24_API_KEY" |
| ipn_url | string (URL) | YES | - |
| ipn_passphrase_env | string (ENV_VAR) | YES | "DS24_IPN_PASSPHRASE" |
| ipn_format | const("form-encoded") | YES | "form-encoded" |
| ipn_response | const("OK") | YES | "OK" |
| signature_algo | const("sha512") | YES | "sha512" |
| merchant_of_record | enum(ds24,self) | YES | "ds24" |
| eu_vat_included | boolean | YES | true |
| languages | list[enum(de,en,es,fr,it,nl,pl)] | NO | ["de","en"] |
| payment_methods | map[country_code, list[string]] | NO | - |

### checkout_hotmart (required when provider=hotmart)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| hotmart_product_id | string | YES | - |
| hotmart_token_env | string (ENV_VAR) | YES | "HOTMART_TOKEN" |
| hottok_env | string (ENV_VAR) | YES | "HOTMART_HOTTOK" |
| webhook_format | const("json") | YES | "json" |
| signature_algo | const("sha256_hmac") | YES | "sha256_hmac" |
| affiliate_enabled | boolean | NO | false |
| affiliate_commission_pct | float (0.0-1.0) | NO | 0.40 |

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
| Field | Type | Required | Default |
|-------|------|----------|---------|
| enabled | boolean | YES | false |
| platforms | list[enum(meta,google,tiktok,linkedin)] | COND | - |
| monthly_budget | integer (centavos) | COND | - |
| target_cpa | integer (centavos) | NO | - |
| pixel_env | string (ENV_VAR) | COND | "META_PIXEL_ID" |

### emails (optional)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| provider | enum(resend,sendgrid,ses,mailchimp) | COND | "resend" |
| api_key_env | string (ENV_VAR) | COND | "EMAIL_API_KEY" |
| sequences | list[sequence_object] | COND | - |
| sequence.name | string | YES | "onboarding" |
| sequence.trigger | string | YES | "signup" |
| sequence.emails | list[email_step] | YES | - |

### validation (required)
| Field | Type | Required | Default |
|-------|------|----------|---------|
| margin_check | boolean | YES | true |
| webhook_test | boolean | YES | true |
| mock_before_live | boolean | YES | true |

## Validation Rules
1. All price fields in centavos/cents — NEVER decimals
2. floor_margin_pct >= 0.30 (30% minimum margin)
3. API keys/secrets: NEVER plaintext → always ENV_VAR (SCREAMING_SNAKE_CASE)
4. webhook_secret_env must end with _SECRET or _KEY
5. credits.pipeline_costs values must be positive integers
6. tiers must have at least 1 entry (free tier counts)
7. mock_mode: true in dev/staging, false only in production
