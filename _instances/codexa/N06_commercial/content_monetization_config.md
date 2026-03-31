---
id: instance_n06_content_monetization_config
kind: function_def
pillar: P04
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
title: "Codexa Instance — N06 Content Monetization Config"
tags: [instance, content-monetization, codexa, mercadopago, brl, pipeline-costs, N06]
tldr: "Codexa-specific content monetization config for N06. MercadoPago primary, BRL centavos, PIPELINE_COSTS from credit_system.py, mock mode for CI."
quality: null
domain: content-monetization
instance: codexa
---

# Codexa Instance: N06 Content Monetization Config

This is the live configuration for Codexa's content monetization pipeline, derived from `credit_system.py` and `billing_executor.py` in codexa-core. All values are production-verified.

## Active Configuration

```yaml
# ── Instance Identity ─────────────────────────────────────
instance: codexa
nucleus: N06
environment: LIVE                 # Reads from ENV: BILLING_MODE (LIVE|TEST|MOCK)

# ── Primary Payment Provider ──────────────────────────────
payment_provider: mercadopago
currency: BRL
currency_unit: centavos           # integer BRL centavos — no floats ever
fallback_provider: stripe         # USD international fallback

# ── PIPELINE_COSTS (from credit_system.py) ───────────────
# Source: CreditSystem.PIPELINE_COSTS dict
pipeline_costs:
  PESQUISA: 75                    # R$0.75 — web research + SEO analysis
  ANUNCIO: 50                     # R$0.50 — ad copy generation
  FOTO: 100                       # R$1.00 — product image description/generation
  FULL: 200                       # R$2.00 — full pipeline bundle

# ── DEFAULT_PACKS (from credit_system.py) ────────────────
# Source: CreditSystem.DEFAULT_PACKS
packs:
  starter:
    price_brl_centavos: 500       # R$5,00
    credits: 500
    pix_discount: 0
  standard:
    price_brl_centavos: 2000      # R$20,00
    credits: 2100                 # 5% bonus
    pix_discount: 5
  pro:
    price_brl_centavos: 6000      # R$60,00
    credits: 6600                 # 10% bonus
    pix_discount: 10

# ── MercadoPago Config ────────────────────────────────────
mercadopago:
  mode: LIVE                      # From ENV: MP_MODE
  access_token_env: MP_ACCESS_TOKEN
  public_key_env: MP_PUBLIC_KEY
  webhook_endpoint: /webhooks/mercadopago/ipn
  webhook_verification: HMAC-SHA256
  idempotency_header: x-idempotency-key
  payment_methods: [PIX, boleto, credit_card, debit_card]
  default_method: PIX             # Lowest abandonment for BR
  subscription_api: Preapproval

# ── Stripe Config (USD fallback) ─────────────────────────
stripe:
  mode: TEST                      # Upgrade to LIVE for USD billing
  secret_key_env: STRIPE_SECRET_KEY
  webhook_endpoint: /webhooks/stripe/checkout
  webhook_secret_env: STRIPE_WEBHOOK_SECRET
  payment_methods: [card, link]
  subscription_mode: recurring

# ── BillingExecutor Modes ─────────────────────────────────
# Source: BillingExecutor class modes
billing_modes:
  LIVE:
    description: Real charges, real webhooks
    env_check: BILLING_MODE=LIVE
  TEST:
    description: Stripe test mode + MP sandbox
    env_check: BILLING_MODE=TEST
  MOCK:
    description: In-memory, no API calls — safe for dev/CI
    env_check: BILLING_MODE=MOCK
    returns_fake_urls: true

# ── Course Generation (CursosExecutor) ───────────────────
courses:
  llm_model: claude-sonnet-4-6
  chain: [OutlineOutput, ModuleOutput, SalesPageOutput, EmailSequenceOutput]
  pydantic_strict: true
  mock_fallback: true             # Returns stub objects on LLM quota exceeded
  max_modules: 8
  lessons_per_module: 5
  email_sequence_length: 5

# ── Ad Validation (AnuncioValidator) ─────────────────────
ad_validation:
  confidence_min: 0.70
  fabrication_detection: true
  retry_strategy: regenerate_flagged_sections
  max_retries: 2

# ── Email Templates ───────────────────────────────────────
email_templates:
  engine: TEMPLATES_dict          # From email_templates.py
  brl_format: "R${amount/100:,.2f}"
  transactional: [purchase_confirmation, credit_alert, checkout_expired, credit_consumed]
  marketing: [launch_day, content_preview, objection_handler, last_chance, post_purchase, upsell]

# ── ERP Integration (ERPConnector) ───────────────────────
erp:
  primary: baselinker
  fallback: bling_v3
  sync_events: [order.created, stock.updated, product.synced]
  oauth2_refresh: true
  rate_limit: 100_req_per_min
  models: [ERPProduct, ERPOrder, ERPStockItem]
```

## Environment Variables Required

```bash
# Required for LIVE mode
MP_ACCESS_TOKEN=APP_USR-...
MP_PUBLIC_KEY=APP_USR-...
BILLING_MODE=LIVE               # LIVE | TEST | MOCK

# Optional (USD fallback)
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# ERP (if enabled)
BASELINKER_API_KEY=...
BLING_CLIENT_ID=...
BLING_CLIENT_SECRET=...
```

## Operational Notes

- **Centavos only**: All CreditSystem operations use integer centavos. Never pass floats.
- **Idempotency**: Every billing call must include `idempotency_key = f"{user_id}:{operation}:{session_id}"`.
- **Mock in CI**: Set `BILLING_MODE=MOCK` in GitHub Actions — prevents real charges.
- **Webhook retry**: MercadoPago IPN retries 3× on failure. Handler must be idempotent.
- **Credit lock order**: `check_sufficient` → `lock` → `execute service` → `consume` → `confirm`. Never skip lock.
- **PIX priority**: Always offer PIX as first payment option — 40% lower abandonment for BR market.
- **Course mock**: If LLM quota exceeded, `mock_fallback=true` returns deterministic stub Pydantic objects.
