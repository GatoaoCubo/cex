---
kind: examples
id: bld_examples_content_monetization
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of content monetization configs
pattern: few-shot learning — LLM reads these before producing
---

# Examples: content-monetization-builder

## Golden — SaaS (Stripe, BR)
INPUT: "Monetization config for AI research platform, BR"
```yaml
identity: { empresa: "CODEXA", domain: ai_tools, currency: BRL, currency_unit: centavos, country: BR }
pricing:
  strategy: hybrid
  floor_margin_pct: 0.35
  tiers:
    - { name: free, price_monthly: 0, credits_monthly: 50, features: [basic_search] }
    - { name: pro, price_monthly: 9990, credits_monthly: 1000, features: [research, publish] }
credits: { pipeline_costs: { research: 50, publish: 10 }, overdraft_policy: notify_then_block }
checkout: { provider: stripe, webhook_secret_env: STRIPE_WEBHOOK_SECRET, idempotency: true, mock_mode: true }
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Hybrid pricing, centavos, ENV_VAR secrets, idempotent, mock on.

## Golden — Course (Hotmart, BR)
INPUT: "Pet care course, Hotmart, BR"
```yaml
identity: { empresa: "PetVida", domain: pet_education, currency: BRL, currency_unit: centavos, country: BR }
pricing: { strategy: tiered, floor_margin_pct: 0.70, tiers: [{ name: basico, price_monthly: 4990 }, { name: completo, price_monthly: 9990 }] }
checkout: { provider: hotmart, webhook_secret_env: HOTMART_HOTTOK, signature: sha256_hmac, format: json, idempotency: true, mock_mode: true }
courses: { enabled: true, modules: [{ title: "Nutrição", drip_days: 0 }, { title: "Saúde", drip_days: 7 }], certification: true }
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Course-focused, Hotmart webhook (JSON/sha256), drip, 70% margins.

## Golden — Coaching (Digistore24, EU)
INPUT: "Coaching program, Digistore24, DACH market"
```yaml
identity: { empresa: "MindsetPro", domain: coaching, currency: EUR, currency_unit: cents, country: EU }
pricing: { strategy: tiered, floor_margin_pct: 0.65, tiers: [{ name: starter, price_monthly: 4900 }, { name: premium, price_monthly: 14900 }] }
checkout: { provider: digistore24, api_key_env: DS24_API_KEY, ipn_passphrase_env: DS24_IPN_PASSPHRASE, ipn_format: form-encoded, ipn_response: "OK", signature: sha512, merchant_of_record: ds24, languages: [de, en], idempotency: true, mock_mode: true }
compliance: { gdpr_dpa: true, double_optin: true, impressum_url: "/impressum", widerrufsrecht: "14-day", eu_vat: "ds24_mor" }
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: DS24, EUR, sha512 IPN "OK", GDPR+Impressum+Widerrufsrecht, DS24 as MoR.

## Golden — Multi-Platform (Hotmart BR + DS24 INT)
INPUT: "Sell course in BR and EU simultaneously"
```yaml
identity: { empresa: "GlobalEdu", domain: education, currencies: [BRL, EUR], regions: [BR, EU] }
pricing: { strategy: tiered, floor_margin_pct: 0.55, tiers: [{ name: essencial, price_brl: 19700, price_eur: 3900 }, { name: completo, price_brl: 49700, price_eur: 9900 }] }
checkout:
  platforms:
    hotmart: { token_env: HOTMART_TOKEN, webhook_secret_env: HOTMART_HOTTOK, signature: sha256_hmac, format: json }
    digistore24: { api_key_env: DS24_API_KEY, ipn_passphrase_env: DS24_IPN_PASSPHRASE, signature: sha512, format: form-encoded, response: "OK" }
  routing: "geo-detect → BR=hotmart, EU/INT=ds24"
  idempotency: true
  mock_mode: true
validation: { margin_check: true, webhook_test: true, mock_before_live: true }
```
WHY GOOD: Dual-platform, geo-routed, both webhook formats, EUR+BRL.

## Anti-Example
```yaml
price: 49.90         # FAIL: float not centavos
api_key: sk_live_xxx # FAIL: plaintext secret
margin: unknown      # FAIL: no floor margin
mock_mode: false     # FAIL: live in dev
ds24_response: "{}"  # FAIL: must respond "OK" not JSON
ds24_format: json    # FAIL: DS24 IPN is form-encoded
hotmart_only: true   # FAIL: no international reach
```
