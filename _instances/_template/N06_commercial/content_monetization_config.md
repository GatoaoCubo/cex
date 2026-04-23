---
id: tpl_content_monetization_config
kind: env_config
pillar: P09
version: 1.0.0
created: 2026-03-31
author: content-monetization-builder
domain: content_monetization
quality: 9.0
tldr: "Instance template for content monetization — fill [PLACEHOLDERS] for any business"
tags: [template, monetization, config, hotmart, digistore24, multi-platform]
density_score: 1.0
related:
  - bld_examples_content_monetization
  - bld_tools_content_monetization
  - kc_content_platform_comparison
  - bld_knowledge_card_content_monetization
  - tpl_pricing_model
  - tpl_launch_checklist
  - bld_architecture_content_monetization
  - bld_instruction_content_monetization
  - bld_config_content_monetization
  - p06_schema_env_contract
---

# Content Monetization Config — Instance Template

> Copy this file to `_instances/{empresa}/N06_commercial/content_monetization_config.md`
> Replace ALL `[PLACEHOLDER]` values with your business specifics.
> Zero hardcoded values — every field is parameterized.

## Identity

```yaml
identity:
  empresa: "[EMPRESA_NOME]"
  domain: "[VERTICAL — e.g. ai_tools, pet_education, fitness, finance]"
  vertical: "[educacao|saas|consultoria|coaching|comunidade|infoproduto]"
  currency_primary: "[BRL|EUR|USD]"
  currency_unit: "[centavos|cents]"
  region_primary: "[BR|LATAM|EU|DACH|US|GLOBAL]"
  languages: ["[pt-BR|de|en|es|fr|it|nl|pl]"]
```

## Platforms

```yaml
platforms:
  tier_1:
    brasil:
      provider: "[hotmart|kiwify|eduzz|monetizze|none]"
      product_id: "[HOTMART_PRODUCT_ID]"
      token_env: "[HOTMART_TOKEN]"
      affiliate_program: "[true|false]"
      affiliate_commission_pct: "[PERCENTUAL — e.g. 0.40]"
    internacional:
      provider: "[digistore24|teachable|thinkific|none]"
      product_id: "[DS24_PRODUCT_ID]"
      api_key_env: "[DS24_API_KEY]"
      affiliate_enabled: "[true|false]"
      affiliate_commission_pct: "[PERCENTUAL — e.g. 0.50]"
      merchant_of_record: "[ds24|self]"
  tier_2:
    - provider: "[udemy|clickbank|gumroad|none]"
      purpose: "[mass_niche|passive_income|lead_magnet]"
```

## Products

```yaml
products:
  - tipo: "[curso|ebook|mentoria|comunidade|template|saas|workshop]"
    nome: "[PRODUTO_NOME]"
    slug: "[produto-slug]"
    preco_brl: "[PRECO_CENTAVOS — e.g. 9990]"
    preco_eur: "[PRECO_CENTS — e.g. 2990]"
    preco_usd: "[PRECO_CENTS — e.g. 2990]"
    checkout_br: "[hotmart|kiwify]"
    checkout_int: "[digistore24|teachable]"
    entrega: "[hotmart_club|ds24_member|teachable|custom_lms]"
    upsell_to: "[NEXT_PRODUCT_SLUG|none]"
    downsell_to: "[LOWER_PRODUCT_SLUG|none]"
```

## Webhooks

```yaml
webhooks:
  hotmart:
    hottok_env: "[HOTMART_HOTTOK]"
    endpoint: "[URL_WEBHOOK_HOTMART — e.g. https://api.empresa.com/webhooks/hotmart]"
    events:
      - PURCHASE_COMPLETE
      - PURCHASE_CANCELED
      - PURCHASE_REFUNDED
      - PURCHASE_CHARGEBACK
      - SUBSCRIPTION_CANCELLATION
      - SWITCH_PLAN
    signature: "sha256 HMAC (X-Hotmart-Hottok header)"
    format: "JSON"
    idempotency_key: "[transaction_id|purchase_id]"

  digistore24:
    api_key_env: "[DS24_API_KEY]"
    ipn_passphrase_env: "[DS24_IPN_PASSPHRASE]"
    endpoint: "[URL_WEBHOOK_DS24 — e.g. https://api.empresa.com/webhooks/ds24]"
    events:
      - on_payment
      - on_refund
      - on_chargeback
      - on_rebill_resumed
      - on_rebill_cancelled
      - on_affiliatelink
      - on_invoice_created
      - on_payment_missed
    signature: "sha512 hash verification"
    format: "form-encoded (NOT JSON)"
    response: "body must be exact string 'OK'"
    idempotency_key: "[order_id|transaction_id]"
```

## Affiliates

```yaml
affiliates:
  hotmart:
    programa_url: "[LINK_PROGRAMA_AFILIADOS_HOTMART]"
    comissao_pct: "[PERCENTUAL — e.g. 0.40]"
    cookie_days: "[DIAS — e.g. 180]"
    marketplace_listed: "[true|false]"
  digistore24:
    affiliate_enabled: "[true|false]"
    comissao_pct: "[PERCENTUAL — e.g. 0.50]"
    marketplace_listed: "[true|false]"
    promo_tools_url: "[URL_DS24_PROMO_TOOLS]"
```

## Compliance

```yaml
compliance:
  # GDPR (required for EU sales via DS24)
  gdpr:
    dpa_signed: "[true|false]"
    double_optin: "[true|false]"
    data_erasure_process: "[manual|automated]"
    privacy_policy_url: "[URL_PRIVACY_POLICY]"

  # EU-specific (required for DS24/DACH region)
  eu:
    impressum_url: "[URL_IMPRESSUM — required DACH region]"
    widerrufsrecht_url: "[URL_CANCELLATION_POLICY — 14-day cooling-off]"
    cookie_consent_provider: "[cookiebot|onetrust|custom|none]"
    vat_handling: "[ds24_merchant_of_record|self_registered|not_applicable]"

  # BR-specific (required for Hotmart)
  br:
    cnpj: "[CNPJ_EMPRESA]"
    nota_fiscal: "[manual|automated|not_applicable]"
    consumidor_gov: "[true|false]"
```

## Analytics

```yaml
analytics:
  tracking:
    utm_convention: "[source]_[medium]_[campaign]_[content]"
    pixel_meta_env: "[META_PIXEL_ID]"
    pixel_google_env: "[GOOGLE_ADS_TAG]"
    pixel_tiktok_env: "[TIKTOK_PIXEL_ID|none]"
  kpis:
    cac_target: "[VALOR_CENTAVOS — e.g. 5000]"
    ltv_target: "[VALOR_CENTAVOS — e.g. 50000]"
    churn_max_monthly_pct: "[PERCENTUAL — e.g. 0.05]"
    conversion_rate_target: "[PERCENTUAL — e.g. 0.03]"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_content_monetization]] | upstream | 0.37 |
| [[bld_tools_content_monetization]] | downstream | 0.33 |
| [[kc_content_platform_comparison]] | upstream | 0.32 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.32 |
| [[tpl_pricing_model]] | sibling | 0.31 |
| [[tpl_launch_checklist]] | sibling | 0.31 |
| [[bld_architecture_content_monetization]] | upstream | 0.28 |
| [[bld_instruction_content_monetization]] | upstream | 0.28 |
| [[bld_config_content_monetization]] | related | 0.28 |
| [[p06_schema_env_contract]] | upstream | 0.24 |
