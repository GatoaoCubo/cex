---
id: tpl_pricing_model
kind: env_config
pillar: P09
version: 1.0.0
created: 2026-03-31
author: content-monetization-builder
domain: pricing_strategy
quality: 9.0
tldr: "Pricing strategy template — value ladder, PPP, coupons, metrics for any content business"
tags: [template, pricing, ladder, ppp, monetization, hotmart, digistore24]
density_score: 1.0
related:
  - tpl_content_monetization_config
  - bld_knowledge_card_content_monetization
  - bld_instruction_content_monetization
  - bld_architecture_content_monetization
  - kc_content_platform_comparison
  - bld_examples_content_monetization
  - tpl_launch_checklist
  - bld_config_content_monetization
  - p12_wf_cf_publish_hotmart
---

# Pricing Model — Instance Template

> Copy to `_instances/{empresa}/N06_commercial/pricing_model.md`
> Replace ALL `[PLACEHOLDER]` values. Prices in centavos/cents (integers, never floats).

## Value Ladder

```yaml
value_ladder:
  # Stage 0: Lead Magnet (free — captures email)
  freebie:
    nome: "[FREEBIE_NOME — e.g. 'Guia Gratuito de X']"
    tipo: "[ebook|checklist|mini_curso|template|webinar_replay]"
    entrega: "[email|landing_page|hotmart_club|ds24_member]"
    objetivo: "captura de email → nurture → low-ticket"

  # Stage 1: Low-Ticket (impulse buy, qualifies buyer)
  low_ticket:
    nome: "[PRODUTO_LOW — e.g. 'Workshop Intensivo']"
    preco_brl: "[PRECO_CENTAVOS — e.g. 4700]"
    preco_eur: "[PRECO_CENTS — e.g. 970]"
    preco_usd: "[PRECO_CENTS — e.g. 970]"
    checkout_br: "[hotmart|kiwify]"
    checkout_int: "[digistore24]"
    margem_minima_pct: 0.60
    objetivo: "converter lead frio → buyer, cobrir CAC"

  # Stage 2: Mid-Ticket (core offer, main revenue)
  mid_ticket:
    nome: "[PRODUTO_MID — e.g. 'Curso Completo de X']"
    preco_brl: "[PRECO_CENTAVOS — e.g. 49700]"
    preco_eur: "[PRECO_CENTS — e.g. 9970]"
    preco_usd: "[PRECO_CENTS — e.g. 9970]"
    checkout_br: "[hotmart|kiwify]"
    checkout_int: "[digistore24]"
    margem_minima_pct: 0.50
    parcelamento_br: "[max_parcelas — e.g. 12]"
    objetivo: "receita principal, LTV builder"

  # Stage 3: High-Ticket (premium, high-touch)
  high_ticket:
    nome: "[PRODUTO_HIGH — e.g. 'Mentoria Premium']"
    preco_brl: "[PRECO_CENTAVOS — e.g. 297000]"
    preco_eur: "[PRECO_CENTS — e.g. 59700]"
    preco_usd: "[PRECO_CENTS — e.g. 59700]"
    checkout_br: "[hotmart|kiwify|manual_invoice]"
    checkout_int: "[digistore24|manual_invoice]"
    margem_minima_pct: 0.70
    vagas_limitadas: "[NUMERO|unlimited]"
    objetivo: "margem alta, relacionamento, caso de sucesso"

  # Stage 4: Recurrence (subscription, predictable revenue)
  recorrencia:
    nome: "[PRODUTO_RECORRENTE — e.g. 'Comunidade Premium']"
    preco_mensal_brl: "[PRECO_CENTAVOS — e.g. 9990]"
    preco_mensal_eur: "[PRECO_CENTS — e.g. 1990]"
    preco_mensal_usd: "[PRECO_CENTS — e.g. 1990]"
    preco_anual_brl: "[PRECO_CENTAVOS — e.g. 99900 (2 meses gratis)]"
    preco_anual_eur: "[PRECO_CENTS — e.g. 19900]"
    checkout_br: "[hotmart|kiwify]"
    checkout_int: "[digistore24]"
    margem_minima_pct: 0.40
    trial_days: "[DIAS — e.g. 7]"
    objetivo: "receita previsivel, retenção, comunidade"
```

## Purchasing Power Parity (PPP)

```yaml
ppp:
  strategy: "[auto_discount|regional_pricing|single_price]"
  regions:
    tier_1_high:
      countries: [US, UK, DE, CH, NO, SE, DK, AU, CA]
      multiplier: 1.0
      currency: "[USD|EUR]"
    tier_2_medium:
      countries: [BR, MX, AR, CO, PL, PT, ES, IT]
      multiplier: "[0.50-0.70]"
      currency: "[BRL|EUR|USD]"
    tier_3_low:
      countries: [IN, NG, PH, VN, EG, BD]
      multiplier: "[0.25-0.40]"
      currency: "[USD]"
  implementation:
    hotmart: "manual — create separate offer links per region"
    digistore24: "built-in PPP via coupon codes per country"
    stripe: "use Stripe Pricing Tables with geo-detection"
```

## Coupons & Promotions

```yaml
coupons:
  launch:
    code: "[CUPOM_LANCAMENTO — e.g. LAUNCH50]"
    discount_pct: "[PERCENTUAL — e.g. 0.50]"
    valid_from: "[YYYY-MM-DD]"
    valid_until: "[YYYY-MM-DD]"
    max_uses: "[NUMERO|unlimited]"
    platforms: [hotmart, digistore24]

  evergreen:
    code: "[CUPOM_EVERGREEN — e.g. WELCOME20]"
    discount_pct: "[PERCENTUAL — e.g. 0.20]"
    trigger: "[exit_intent|email_sequence_day_5|abandoned_cart]"
    platforms: [hotmart, digistore24]

  seasonal:
    black_friday:
      code: "[CUPOM_BF]"
      discount_pct: "[PERCENTUAL — e.g. 0.40]"
      valid_from: "[YYYY-MM-DD]"
      valid_until: "[YYYY-MM-DD]"
    back_to_school:
      code: "[CUPOM_BTS]"
      discount_pct: "[PERCENTUAL — e.g. 0.30]"

  rules:
    stackable: "[true|false]"
    min_purchase: "[VALOR_CENTAVOS|none]"
    floor_margin_after_discount: 0.30
```

## Metrics & Targets

```yaml
metrics:
  acquisition:
    cac_target_brl: "[VALOR_CENTAVOS — e.g. 5000]"
    cac_target_eur: "[VALOR_CENTS — e.g. 1000]"
    cac_channels:
      organic: "[PERCENTUAL — e.g. 0.40]"
      paid_meta: "[PERCENTUAL — e.g. 0.30]"
      paid_google: "[PERCENTUAL — e.g. 0.15]"
      affiliates: "[PERCENTUAL — e.g. 0.15]"

  retention:
    ltv_target_brl: "[VALOR_CENTAVOS — e.g. 50000]"
    ltv_target_eur: "[VALOR_CENTS — e.g. 10000]"
    churn_max_monthly_pct: "[PERCENTUAL — e.g. 0.05]"
    ltv_to_cac_ratio_min: 3.0

  conversion:
    landing_page_conversion_pct: "[PERCENTUAL — e.g. 0.03]"
    email_open_rate_target: "[PERCENTUAL — e.g. 0.25]"
    email_click_rate_target: "[PERCENTUAL — e.g. 0.04]"
    checkout_completion_rate: "[PERCENTUAL — e.g. 0.60]"

  revenue:
    mrr_target: "[VALOR_CENTAVOS — monthly recurring]"
    arr_target: "[VALOR_CENTAVOS — annual recurring]"
    floor_margin_pct: 0.30
    break_even_months: "[MESES — e.g. 6]"
```

## Pricing Review Cadence

```yaml
review:
  frequency: "[monthly|quarterly]"
  triggers:
    - "churn > [THRESHOLD] for 2 consecutive months"
    - "CAC > LTV/3 for 30 days"
    - "competitor price change > 20%"
    - "new platform launch (e.g. Kiwify feature parity)"
  owner: "[ROLE — e.g. Head of Product]"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_content_monetization_config]] | sibling | 0.40 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.22 |
| [[bld_instruction_content_monetization]] | upstream | 0.21 |
| [[bld_architecture_content_monetization]] | upstream | 0.18 |
| [[kc_content_platform_comparison]] | upstream | 0.18 |
| [[bld_examples_content_monetization]] | upstream | 0.17 |
| [[tpl_launch_checklist]] | sibling | 0.17 |
| [[bld_config_content_monetization]] | related | 0.16 |
| [[p12_wf_cf_publish_hotmart]] | downstream | 0.16 |
