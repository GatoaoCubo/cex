---
kind: examples
id: bld_examples_content_monetization
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of content monetization configs
pattern: few-shot learning — LLM reads these before producing
---

# Examples: content-monetization-builder

## Golden Example — SaaS AI Tool (CODEXA)
INPUT: "Monetization config for AI research platform, BR"
```yaml
identity: { empresa: "CODEXA", domain: ai_tools, currency: BRL, currency_unit: centavos, country: BR }
pricing:
  strategy: hybrid
  floor_margin_pct: 0.35
  trial_days: 7
  tiers:
    - { name: free, price_monthly: 0, credits_monthly: 50, features: [basic_search] }
    - { name: pro, price_monthly: 9990, credits_monthly: 1000, features: [research, publish, analytics] }
    - { name: enterprise, price_monthly: 29990, credits_monthly: 5000, features: [research, publish, analytics, api] }
credits:
  unit_name: credit
  pipeline_costs: { research: 50, publish: 10, analyze: 30, export: 5 }
  packs: [{ name: booster_500, credits: 500, price: 2990 }]
  overdraft_policy: notify_then_block
checkout: { provider: stripe, webhook_secret_env: STRIPE_WEBHOOK_SECRET, idempotency: true, mock_mode: true }
emails:
  provider: resend
  api_key_env: RESEND_API_KEY
  sequences:
    - { name: onboarding, trigger: signup, emails: [{ delay_hours: 0, template: welcome }, { delay_hours: 72, template: pro_upsell }] }
    - { name: churn_prevention, trigger: credits_below_10pct, emails: [{ delay_hours: 0, template: low_credits }] }
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Hybrid (tier + packs), margins >30%, centavos, ENV_VAR secrets, idempotent webhook, mock on, behavioral triggers.

## Golden Example — Course (Hotmart)
INPUT: "Monetize pet care course, Hotmart, BR"
```yaml
identity: { empresa: "PetVida", domain: pet_education, currency: BRL, currency_unit: centavos, country: BR }
pricing:
  strategy: tiered
  floor_margin_pct: 0.70
  tiers:
    - { name: basico, price_monthly: 4990, features: [course_basic] }
    - { name: completo, price_monthly: 9990, features: [course_basic, course_advanced, certificate] }
checkout: { provider: hotmart, webhook_url: "https://api.petvida.com/webhooks/hotmart", webhook_secret_env: HOTMART_WEBHOOK_SECRET, idempotency: true, mock_mode: true }
courses:
  enabled: true
  modules:
    - { title: "Nutrição Canina", lessons: [{ title: "Fundamentos", type: video }, { title: "Quiz", type: quiz }], drip_days: 0 }
    - { title: "Saúde Preventiva", lessons: [{ title: "Vacinação", type: video }, { title: "Prática", type: assignment }], drip_days: 7 }
  certification: true
  completion_threshold: 0.80
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Course-focused, drip content, certification, 70% margins, Hotmart for BR.

## Golden Example — Infoproduct Funnel (Kiwify)
INPUT: "Ads → course → upsell, Kiwify, BR"
```yaml
identity: { empresa: "DigitalPro", domain: digital_marketing, currency: BRL, currency_unit: centavos, country: BR }
pricing: { strategy: tiered, floor_margin_pct: 0.60, tiers: [{ name: starter, price_monthly: 2990, features: [course_intro] }, { name: master, price_monthly: 14990, features: [course_intro, course_advanced, mentoria] }] }
checkout: { provider: kiwify, webhook_secret_env: KIWIFY_WEBHOOK_SECRET, idempotency: true, mock_mode: true }
ads: { enabled: true, platforms: [meta, google], monthly_budget: 500000, target_cpa: 5000, pixel_env: META_PIXEL_ID }
emails: { provider: resend, api_key_env: RESEND_API_KEY, sequences: [{ name: onboarding, trigger: purchase, emails: [{ delay_hours: 0, template: welcome }] }] }
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```

## Golden Example — EU Infoproduct (Digistore24)
INPUT: "Online coaching program, Digistore24, DACH market"
```yaml
identity: { empresa: "MindsetPro", domain: coaching, currency: EUR, currency_unit: cents, country: EU }
pricing:
  strategy: tiered
  floor_margin_pct: 0.65
  tiers:
    - { name: starter, price_monthly: 4900, features: [course_basic, community] }
    - { name: premium, price_monthly: 14900, features: [course_basic, course_advanced, community, live_calls, certificate] }
    - { name: vip, price_monthly: 49900, features: [all_courses, community, live_calls, certificate, mentoring_1on1] }
checkout:
  provider: digistore24
  api_key_env: DS24_API_KEY
  ipn_url: "https://api.mindsetpro.de/webhooks/ds24"
  ipn_passphrase_env: DS24_IPN_PASSPHRASE
  ipn_format: form-encoded
  ipn_response: "OK"
  signature: sha512
  idempotency: true
  mock_mode: true
  payment_methods:
    DE: [sepa, sofort, cards, paypal]
    NL: [ideal, cards, paypal]
    US: [cards, paypal]
  languages: [de, en, es, fr]
  merchant_of_record: ds24
affiliates:
  enabled: true
  commission_pct: 0.50
  marketplace_listed: true
  promo_tools: true
compliance:
  gdpr_dpa: true
  double_optin: true
  impressum_url: "https://mindsetpro.de/impressum"
  widerrufsrecht: "14-day cooling-off, digital waiver with consent"
  eu_vat: "handled by DS24 as Merchant of Record"
  cookie_consent: cookiebot
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: DS24-native, EUR pricing, sha512 IPN with "OK" response, per-country payment methods, GDPR+Impressum+Widerrufsrecht, DS24 as MoR handles VAT, affiliate marketplace enabled.

## Golden Example — Multi-Platform (Hotmart BR + DS24 INT)
INPUT: "Sell course in BR and EU simultaneously"
```yaml
identity: { empresa: "GlobalEdu", domain: education, currencies: [BRL, EUR], regions: [BR, EU] }
pricing:
  strategy: tiered
  floor_margin_pct: 0.55
  tiers:
    - { name: essencial, price_brl: 19700, price_eur: 3900, features: [course_core] }
    - { name: completo, price_brl: 49700, price_eur: 9900, features: [course_core, mentoria, certificate] }
checkout:
  platforms:
    hotmart:
      product_id_env: HOTMART_PRODUCT_ID
      token_env: HOTMART_TOKEN
      webhook_url: "https://api.globaledu.com/webhooks/hotmart"
      webhook_secret_env: HOTMART_HOTTOK
      signature: sha256_hmac
      format: json
    digistore24:
      product_id_env: DS24_PRODUCT_ID
      api_key_env: DS24_API_KEY
      ipn_url: "https://api.globaledu.com/webhooks/ds24"
      ipn_passphrase_env: DS24_IPN_PASSPHRASE
      signature: sha512
      format: form-encoded
      response: "OK"
  routing: "geo-detect → BR=hotmart, EU/INT=ds24"
  idempotency: true
  mock_mode: true
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Dual-platform, geo-routed checkout, both webhook formats handled, EUR+BRL pricing.

## Anti-Example
```yaml
price: 49.90         # FAIL: float not centavos
api_key: sk_live_xxx # FAIL: plaintext secret
margin: unknown      # FAIL: no floor margin
webhook: none        # FAIL: no webhook
mock_mode: false     # FAIL: live in dev
overdraft: unlimited # FAIL: no policy
ds24_response: "{}"  # FAIL: DS24 IPN must respond "OK" not JSON
ds24_format: json    # FAIL: DS24 IPN is form-encoded not JSON
hotmart_only: true   # FAIL: single-platform lock-in, no international reach
```
