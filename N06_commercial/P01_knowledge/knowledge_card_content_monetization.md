---
id: n06_kc_content_monetization
kind: knowledge_card
8f: F3_inject
pillar: P01
title: Content Monetization — Billing, Credits, Courses & Checkout
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
domain: content-monetization
quality: 9.2
tags: [content-monetization, billing, credits, checkout, courses, PIX, MercadoPago, Stripe, N06]
tldr: Distilled knowledge for N06 content monetization pipeline — BRL credit wallet, payment providers, course LLM generation, ad validation, email automation, and ERP sync.
when_to_use: When implementing or reasoning about content monetization flows involving billing, credits, course generation, checkout, ad validation, or ERP integration.
keywords: [monetization, billing, credits, checkout, PIX, subscription, course, course-generation, ad-validation, email-automation, content-factory, credit-wallet, payment-provider]
long_tails:
  - "How to integrate MercadoPago PIX with integer-centavo credit wallet"
  - "Sequential LLM pipeline for course generation: outline to module to sales page to email"
  - "Prepaid credit wallet architecture with per-operation PIPELINE_COSTS"
  - "Stripe vs MercadoPago checkout comparison: LIVE/TEST/MOCK modes"
  - "Ad content validation with fabrication detection and confidence scoring"
  - "Idempotent webhook handling for double-charge prevention"
axioms:
  - "ALWAYS store credit balances in BRL centavos (integer) — float rounding causes billing drift."
  - "NEVER charge credits before consuming the service — consume+refund pattern prevents double-spend."
  - "ALWAYS implement MOCK mode for all payment providers — eliminates test card debt in staging."
  - "NEVER hardcode pipeline costs — reference PIPELINE_COSTS dict, never inline integers."
linked_artifacts:
  primary: p04_fn_content_monetization
  related:
    - p12_dr_content_monetization
    - p12_wf_content_monetization
    - p01_kc_hotmart_api
    - p01_kc_hotmart_club
    - p01_kc_hotmart_marketplace
    - p01_kc_digistore24_api
    - p01_kc_digistore24_ipn
    - p01_kc_digistore24_marketplace
    - p01_kc_content_platform_compliance
    - p01_kc_content_platform_comparison
density_score: null
data_source: codexa-core (billing_executor, credit_system, cursos_executor, erp_connector, anuncio_validator, email_templates, mercadopago_executor)
related:
  - p04_tpl_content_monetization
  - p12_wf_content_monetization
  - p04_fn_content_monetization
  - p04_ex_content_monetization_ecommerce
  - kc_credit_system_design
  - p03_sp_content_monetization_builder
  - bld_instruction_content_monetization
  - n06_integration_content_factory
  - p11_qg_content_monetization
  - kc_mercadopago_pix
---

# Content Monetization — Billing, Credits, Courses & Checkout

## Quick Reference

```yaml
domain: content-monetization
nucleus: N06
pipeline: PARSE→PRICING→CREDITS→CHECKOUT→COURSES→ADS→EMAILS→VALIDATE→DEPLOY
providers: [stripe, mercadopago, hotmart, digistore24]
currency: BRL centavos (integer)
modes: [LIVE, TEST, MOCK]
credit_unit: centavo BRL (1 BRL = 100 créditos)
```

## Core Concepts

### Credit Wallet (BRL Centavos)
Prepaid wallet where all values are stored as integer centavos to avoid float rounding errors.
- `add_credits(user_id, amount_centavos, idempotency_key)` — top-up with dedup key
- `consume(user_id, operation, idempotency_key)` — deduct PIPELINE_COSTS[operation]
- `refund(user_id, operation, idempotency_key)` — rollback on downstream failure
- `check_sufficient(user_id, operation)` — gate before execution, NOT after

### PIPELINE_COSTS Reference
| Operation | Cost (centavos) | Margin (cost-plus) |
|-----------|----------------|-------------------|
| PESQUISA  | 75             | 44% over API cost |
| ANUNCIO   | 50             | 55% over API cost |
| FOTO      | 100            | 47% over API cost |
| FULL      | 200            | bundle discount   |

### Payment Modes (BillingExecutor)
| Mode | Behavior | Use Case |
|------|----------|----------|
| LIVE | Real charges, real webhooks | Production |
| TEST | Stripe test mode / MP sandbox | QA |
| MOCK | In-memory, no API calls | Dev/CI |

Mode auto-detected from env vars — never hardcode.

### Pack Architecture
Default packs with tiered discount:
| Pack | BRL | Credits | Bonus |
|------|-----|---------|-------|
| Starter | R$5 | 500 | 0% |
| Standard | R$20 | 2100 | 5% |
| Pro | R$60 | 6600 | 10% |

PIX always available for purchase_pack_pix (MercadoPago) — lower friction than card for BR market.

## Strategy Phases (Pipeline)

### PARSE
- Extract intent: product_type, target_audience, monetization_goal
- Resolve payment_provider from config (default: mercadopago for BRL)
- Validate required fields

### PRICING
- Load PIPELINE_COSTS for estimated operation count
- Apply pricing_tier logic (free/pro/enterprise)
- Calculate expected credit consumption

### CREDITS
- `check_sufficient(user_id, estimated_cost)`
- On insufficient: return checkout_url for pack purchase
- On sufficient: lock credits (idempotency_key = session_id)

### CHECKOUT
- Stripe: `create_checkout_session(product, price_id, customer_id)`
- MercadoPago: `create_preference(title, unit_price, payer_email)` → PIX/boleto/card
- Webhook on `checkout.session.completed` / IPN payment.approved
- Idempotent: event_id as idempotency key prevents double-credit

### COURSES (LLM Sequential Chain)
```
outline(topic, audience) → ModuleOutput × N → SalesPageOutput → EmailSequenceOutput
```
Each step validates Pydantic model. Mock fallback if LLM quota exceeded.

### ADS
- `AnuncioValidator.validate(ad_content, product_facts)`
- FABRICATION_PATTERNS regex scan → confidence_score
- Retry-with-sections if score < 0.7: regenerate flagged sections only

### EMAILS
- `TEMPLATES[email_type]` dict lookup → personalize with BRL formatting
- Transactional (purchase confirmation, credit alert) vs marketing (launch sequence)
- BRL: `f"R${amount/100:,.2f}"` — always display from centavos

### VALIDATE → DEPLOY
- Final gate: pricing margins > 30%, mock fallback exists, webhook idempotent
- Deploy: write monetization_config to instance, signal N06 complete

## Golden Rules

1. Integer centavos only. All credit math uses integer arithmetic — float rounding causes billing drift at scale.
2. Idempotency everywhere. Every billing call carries a unique key — double-webhooks are safe, replay-safe.
3. Mock is mandatory. Every payment path has a MOCK mode — zero real charges in CI/staging environments.
4. Check-lock-execute-confirm. Validate credit balance before gating — never charge then fail. Refund on downstream error.
5. Sequential course generation. Each LLM step validates Pydantic output before passing to next — broken chains waste credits.
6. Fabrication detection is non-negotiable. All ad content passes confidence_score >= 0.7 — false claims destroy trust and trigger platform bans.
7. PIX-first for BR market. Always offer PIX as default payment — 40% lower cart abandonment vs card for Brazilian users.

## Visual Flow

```
[intent]
    │
    ▼
[PARSE] ──── payment_provider, product_type, audience
    │
    ▼
[PRICING] ── tier resolution, cost estimation
    │
    ▼
[CREDITS] ── check_sufficient → lock
    │         ▼ (insufficient)
    │     [CHECKOUT] ── PIX/Stripe session
    │
    ▼
[COURSES] ── outline→module→sales_page→emails (sequential LLM chain)
    │
    ▼
[ADS] ────── validate, confidence_score >= 0.7
    │
    ▼
[EMAILS] ── templates, BRL formatting
    │
    ▼
[VALIDATE] ─ gates: margin, mock, idempotent
    │
    ▼
[DEPLOY] ─── monetization_config saved, signal sent
```

## Payment Provider Comparison

| Dimension | Stripe | MercadoPago | Hotmart | Digistore24 |
|-----------|--------|-------------|---------|-------------|
| Market | International | Brazil/LATAM | BR infoproducts | EU/DACH/Global |
| PIX | No | Yes (native) | No (card/boleto) | No |
| Boleto | No | Yes | Yes | No |
| Currency | USD/multi | BRL native | BRL | EUR (multi) |
| Webhook | checkout.session.completed | IPN payment.approved | JSON, sha256 HMAC | form-encoded, sha512 |
| IPN response | HTTP 200 | HTTP 200 | HTTP 200 | exact "OK" |
| MoR | Seller | Seller | Seller | DS24 (auto EU VAT) |
| Affiliates | No | No | Marketplace 500K+ | DS24 Marketplace |
| Fee range | 2.9% + $0.30 | 3.49% + BRL | 9.9% (includes MoR) | 7.9% + $1 (includes MoR) |
| Best for | SaaS global | E-commerce BR | Infoproduct BR/LATAM | Infoproduct EU/DACH |

**Multi-platform strategy**: MercadoPago (e-commerce BR, lowest fees) + Hotmart (infoproduct BR, built-in affiliates) + DS24 (infoproduct international, EU VAT handled)

## Platform KCs (Phase 2 — 8 Research KCs)

| KC | ID | Focus |
|----|----|-------|
| Hotmart API | kc_hotmart_api | REST API, OAuth2, webhook JSON sha256 HMAC |
| Hotmart Club | kc_hotmart_club | Native member area, course delivery, drip |
| Hotmart Marketplace | kc_hotmart_marketplace | 500K+ affiliates, BR/LATAM reach |
| Digistore24 API | kc_digistore24_api | REST API, Merchant of Record, auto EU VAT |
| Digistore24 IPN | kc_digistore24_ipn | form-encoded IPN, sha512, respond "OK" |
| Digistore24 Marketplace | kc_digistore24_marketplace | EU affiliates, multi-language |
| Platform Compliance | kc_content_platform_compliance | GDPR, EU VAT, Widerrufsrecht, Impressum |
| Platform Comparison | kc_content_platform_comparison | Hotmart vs DS24 vs Teachable vs Kiwify |

## Downstream Artifacts

| Artifact | ID | Purpose |
|----------|----|---------|
| function_def   | p04_fn_content_monetization | Tool callable by LLM |
| dispatch_rule  | p12_dr_content_monetization | Routing keywords → builder |
| workflow       | p12_wf_content_monetization | Full execution flow |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tpl_content_monetization]] | downstream | 0.51 |
| [[p12_wf_content_monetization]] | downstream | 0.45 |
| [[p04_fn_content_monetization]] | downstream | 0.43 |
| [[p04_ex_content_monetization_ecommerce]] | downstream | 0.39 |
| [[kc_credit_system_design]] | sibling | 0.37 |
| [[p03_sp_content_monetization_builder]] | downstream | 0.34 |
| [[bld_instruction_content_monetization]] | downstream | 0.34 |
| [[n06_integration_content_factory]] | downstream | 0.32 |
| [[p11_qg_content_monetization]] | downstream | 0.31 |
| [[kc_mercadopago_pix]] | sibling | 0.31 |
