---
id: p04_ex_content_monetization_ecommerce
kind: content_monetization
8f: F6_produce
pillar: P11
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
title: "Example — Content Monetization: E-commerce (MercadoPago, BRL centavos, PIX, BaseLinker ERP)"
tags: [example, content-monetization, ecommerce, mercadopago, pix, brl, baselinker, erp, N06]
tldr: "E-commerce content monetization: MercadoPago + PIX, BRL centavos integer, 10% PIX discount, BaseLinker ERP sync for order/stock management."
quality: 9.0
domain: content-monetization
use_case: ecommerce-brazil
related:
  - p04_tpl_content_monetization
  - kc_mercadopago_pix
  - n06_kc_content_monetization
  - p04_fn_content_monetization
  - p12_wf_content_monetization
  - p04_ex_content_monetization_saas
  - p04_ex_content_monetization_infoproduct
  - p12_dr_content_monetization
  - p01_kc_content_monetization
  - n06_integration_content_factory
---

# Example: Content Monetization — E-commerce (MercadoPago / BRL / PIX)

**Use case**: Brazilian e-commerce store generating AI product descriptions, ad copy, and email campaigns. BRL billing via MercadoPago with PIX. BaseLinker ERP sync for order and stock management.

## Configuration

```yaml
payment_provider: mercadopago
currency: BRL
currency_unit: centavos         # integer centavos — 1 BRL = 100 centavos
mode: LIVE                      # TEST for QA, MOCK for CI

pipeline_costs:
  PESQUISA: 75                  # R$0.75 per research/SEO operation
  ANUNCIO: 50                   # R$0.50 per ad generation
  FOTO: 100                     # R$1.00 per product image description
  FULL: 200                     # R$2.00 full pipeline (outline+ad+email)

pix_discount:
  enabled: true
  discount_pct: 10              # 10% discount for PIX payment
  display: "10% OFF no PIX"

packs:
  - name: starter
    price_brl_centavos: 500     # R$5,00
    credits: 500
    discount_pct: 0
  - name: standard
    price_brl_centavos: 2000    # R$20,00
    credits: 2100               # +5% bonus
    discount_pct: 5
  - name: pro
    price_brl_centavos: 6000    # R$60,00
    credits: 6600               # +10% bonus
    discount_pct: 10

tiers:
  free:
    monthly_credits: 0
    features: [trial only — purchase a pack to start]
    checkout_required: false
  lojista:                      # Store owner tier (Brazilian e-commerce primary persona)
    monthly_credits: 3000       # R$30.00 equivalent
    price_monthly_brl_centavos: 9900   # R$99,00/mês
    features: [unlimited products, 100 ads/month, PIX checkout, ERP sync, email sequences]
    checkout_required: true

webhooks:
  provider: mercadopago
  event: payment.approved
  verification: HMAC-SHA256     # x-idempotency-key header
  idempotency_field: event_id
  endpoint: /webhooks/mercadopago/ipn
  retry_policy: 3x_exponential_backoff

erp_integration:
  provider: baselinker
  sync_on: [order.created, stock.updated]
  models: [ERPProduct, ERPOrder, ERPStockItem]
  oauth2_refresh: true
  rate_limit: 100_req_per_min
```

## Function Call Example

```python
result = await monetize_content(
    product={
        "name": "Cama Retrátil Casal Queen",
        "category": "ecommerce",
        "audience": "compradores de móveis planejados BR"
    },
    pricing_tier="lojista",
    payment_provider="mercadopago",
    currency="BRL"
)
```

## Expected Output

```json
{
  "status": "success",
  "checkout_url": "https://mercadopago.com.br/checkout/v1/redirect?pref_id=123456",
  "pix_url": "https://mercadopago.com.br/checkout/v1/pix?pref_id=123456",
  "credits_consumed": 200,
  "credits_remaining": 2800,
  "course_outline_id": null,
  "ad_validation_score": 0.91,
  "emails_queued": 2,
  "erp_sync_status": "queued",
  "monetization_config_id": "p04_ex_content_monetization_ecommerce",
  "steps_completed": ["PARSE", "PRICING", "CREDITS", "CHECKOUT", "ADS", "EMAILS", "VALIDATE", "DEPLOY"]
}
```

## BRL Display Formatting

```python
# ALWAYS display from centavos — never store or compute in floats
balance_centavos = 2800
display = f"R${balance_centavos/100:,.2f}"   # → "R$28,00"
pack_price = 6000
display = f"R${pack_price/100:,.2f}"          # → "R$60,00"

# PIX discount
original = 6000
discounted = original * 90 // 100             # integer math, 10% off → 5400
display = f"R${discounted/100:,.2f} no PIX"   # → "R$54,00 no PIX"
```

## ERP Sync Flow

```
[checkout.session.completed / payment.approved]
         │
         ▼
[BaseLinkerConnector.create_order(ERPOrder)]
         │
         ▼
[ERPStockItem.decrement(sku, qty=1)]
         │
         ▼
[signal: erp_synced] → .cex/runtime/signals/n06_erp.json
```

## Revenue Notes

- PIX offers 40% lower abandonment rate vs credit card for BR e-commerce
- Standard pack (R$20) is highest volume — most lojistas start here
- Boleto option for unbanked / older demographics (3-day payment window)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tpl_content_monetization]] | sibling | 0.50 |
| [[kc_mercadopago_pix]] | upstream | 0.49 |
| [[n06_kc_content_monetization]] | upstream | 0.47 |
| [[p04_fn_content_monetization]] | upstream | 0.38 |
| [[p12_wf_content_monetization]] | downstream | 0.34 |
| [[p04_ex_content_monetization_saas]] | sibling | 0.32 |
| [[p04_ex_content_monetization_infoproduct]] | sibling | 0.31 |
| [[p12_dr_content_monetization]] | downstream | 0.28 |
| [[p01_kc_content_monetization]] | related | 0.25 |
| [[n06_integration_content_factory]] | sibling | 0.22 |
