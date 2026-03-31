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

## Anti-Example
```yaml
price: 49.90         # FAIL: float not centavos
api_key: sk_live_xxx # FAIL: plaintext secret
margin: unknown      # FAIL: no floor margin
webhook: none        # FAIL: no webhook
mock_mode: false     # FAIL: live in dev
overdraft: unlimited # FAIL: no policy
```
