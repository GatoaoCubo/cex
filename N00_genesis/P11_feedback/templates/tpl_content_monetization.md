---
id: p04_tpl_content_monetization
kind: content_monetization
pillar: P11
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
title: "Template — Content Monetization Tool"
tags: [template, content-monetization, billing, checkout, credits, courses, PIX, Stripe, N06]
tldr: "Config-driven template for content monetization function_def artifacts. Covers payment_provider, currency (BRL centavos), pipeline_costs, credit packs, pricing tiers, and quality gates."
quality: 9.1
density_score: 1.0
related:
  - p04_fn_content_monetization
  - n06_kc_content_monetization
  - p04_ex_content_monetization_saas
  - p04_ex_content_monetization_ecommerce
  - bld_instruction_content_monetization
  - n06_content_factory_pricing
  - bld_architecture_content_monetization
  - n06_integration_content_factory
  - p12_wf_content_monetization
  - kc_credit_system_design
---

# Template: Content Monetization Tool

Use this template when building a `function_def` for any content monetization pipeline involving billing, credit wallets, checkout, course generation, ad validation, or email dispatch.

## Configuration YAML

```yaml
# ── Core Config ──────────────────────────────────────────
payment_provider: [PROVIDER]       # stripe | mercadopago | mock
currency: [CURRENCY]               # BRL | USD
currency_unit: centavos            # BRL: integer centavos; USD: integer cents
mode: [MODE]                       # LIVE | TEST | MOCK

# ── Pipeline Costs ───────────────────────────────────────
pipeline_costs:
  PESQUISA: [COST_CENTAVOS]        # e.g., 75
  ANUNCIO: [COST_CENTAVOS]         # e.g., 50
  FOTO: [COST_CENTAVOS]            # e.g., 100
  FULL: [COST_CENTAVOS]            # e.g., 200 (bundle)

# ── Credit Packs ─────────────────────────────────────────
packs:
  - name: starter
    price_brl: [PRICE_BRL]         # e.g., 5.00
    credits: [CREDITS]             # e.g., 500
    discount_pct: 0
  - name: standard
    price_brl: [PRICE_BRL]         # e.g., 20.00
    credits: [CREDITS]             # e.g., 2100
    discount_pct: [DISCOUNT]       # e.g., 5
  - name: pro
    price_brl: [PRICE_BRL]         # e.g., 60.00
    credits: [CREDITS]             # e.g., 6600
    discount_pct: [DISCOUNT]       # e.g., 10

# ── Pricing Tiers ────────────────────────────────────────
tiers:
  free:
    monthly_credits: [CREDITS]     # e.g., 0
    features: [[FEATURE_LIST]]
    checkout_required: false
  pro:
    monthly_credits: [CREDITS]     # e.g., 2000
    features: [[FEATURE_LIST]]
    checkout_required: true
    price_monthly_brl: [PRICE]
  enterprise:
    monthly_credits: [CREDITS]     # e.g., custom
    features: [[FEATURE_LIST]]
    checkout_required: true
    price_monthly_brl: [PRICE]

# ── Webhook Config ───────────────────────────────────────
webhooks:
  mercadopago:
    event: payment.approved
    verification: HMAC-SHA256
    idempotency_field: event_id
  stripe:
    event: checkout.session.completed
    verification: stripe-signature header
    idempotency_field: event_id
  hotmart:
    events: [PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED, PURCHASE_CHARGEBACK]
    verification: sha256_hmac (HOTMART_HOTTOK)
    format: json
    idempotency_field: transaction_id
  digistore24:
    events: [on_payment, on_refund, on_chargeback, on_rebill_resumed, on_rebill_cancelled]
    verification: sha512 (DS24_IPN_PASSPHRASE)
    format: form-encoded   # NOT JSON
    response: "OK"         # exact string required
    idempotency_field: order_id
    merchant_of_record: ds24  # auto EU VAT
```

## Capability Table

| Capability | Supported | Notes |
|-----------|-----------|-------|
| PIX checkout | ✅ (MercadoPago) | Lower abandonment for BR market |
| Boleto | ✅ (MercadoPago) | 3-day expiry |
| Credit card | ✅ (both providers) | Installments via MP |
| Subscriptions | ✅ (both) | Preapproval (MP) / Subscriptions API (Stripe) |
| Credit wallet | ✅ | BRL centavos, idempotent |
| Course generation | ✅ | LLM sequential chain, Pydantic-validated |
| Ad validation | ✅ | confidence_score >= 0.7 gate |
| Mock mode | ✅ | All paths have mock — no real API calls |
| BRL formatting | ✅ | centavos → "R$X,XX" display |
| ERP sync | ✅ (via N06+N05) | BaseLinker / Bling v3 |

## Function Schema (Filled Template)

```json
{
  "name": "monetize_[PRODUCT_TYPE]",
  "description": "[1-2 sentence description specific to this product monetization context]",
  "parameters": {
    "type": "object",
    "properties": {
      "product": {
        "type": "object",
        "description": "Product descriptor: {name, category, audience}"
      },
      "pricing_tier": {
        "type": "string",
        "enum": ["free", "pro", "enterprise"]
      },
      "payment_provider": {
        "type": "string",
        "enum": ["[PROVIDER_1]", "[PROVIDER_2]", "mock"]
      },
      "currency": {
        "type": "string",
        "enum": ["[CURRENCY]"],
        "default": "[DEFAULT_CURRENCY]"
      }
    },
    "required": ["product", "pricing_tier", "payment_provider"]
  }
}
```

## Quality Gate Checklist

- [ ] `payment_provider` has mock mode — no real API calls in CI
- [ ] All credit values are integer centavos — no floats
- [ ] Every billing call has idempotency_key — double-webhooks safe
- [ ] `check_sufficient` called BEFORE service execution — never charge then execute
- [ ] PIPELINE_COSTS referenced by name — no inline integers
- [ ] Pricing margins > 30% for all operations — verify cost-plus calculation
- [ ] Course LLM chain uses Pydantic output models — schema validated each step
- [ ] Ad validation gate present — confidence_score >= 0.7 required
- [ ] Webhook verification configured — HMAC-SHA256 for MP, signature for Stripe
- [ ] BRL display format: `f"R${amount/100:,.2f}"` — centavos to display

## Adaptation Notes

- **For BRL/Brazil**: Default to `mercadopago` + PIX. Use centavos integer. PIPELINE_COSTS in BRL.
- **For USD/International**: Use `stripe` + standard checkout. Currency unit = cents integer.
- **For dev/CI**: Always set `payment_provider=mock`. Returns fake URLs. No side effects.
- **For enterprise**: Override `pipeline_costs` with negotiated rates. Skip pack logic. Direct billing.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_content_monetization]] | upstream | 0.46 |
| [[n06_kc_content_monetization]] | upstream | 0.44 |
| [[p04_ex_content_monetization_saas]] | sibling | 0.43 |
| [[p04_ex_content_monetization_ecommerce]] | sibling | 0.42 |
| [[bld_instruction_content_monetization]] | upstream | 0.36 |
| [[n06_content_factory_pricing]] | sibling | 0.34 |
| [[bld_architecture_content_monetization]] | upstream | 0.33 |
| [[n06_integration_content_factory]] | sibling | 0.33 |
| [[p12_wf_content_monetization]] | downstream | 0.32 |
| [[kc_credit_system_design]] | upstream | 0.28 |
