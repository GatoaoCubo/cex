---
id: p04_ex_content_monetization_saas
kind: content_monetization
pillar: P11
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n06_commercial
title: "Example — Content Monetization: SaaS (Stripe, USD, Monthly/Yearly)"
tags: [example, content-monetization, saas, stripe, usd, subscription, N06]
tldr: "SaaS content monetization config: free/pro/enterprise tiers, Stripe, USD cents, monthly+yearly billing, content credits per tier."
quality: 9.1
domain: content-monetization
use_case: saas-international
---

# Example: Content Monetization — SaaS (Stripe / USD)

**Use case**: B2B SaaS product selling AI-generated content (ad copy, course outlines, email sequences) on a subscription model. USD billing via Stripe.

## Configuration

```yaml
payment_provider: stripe
currency: USD
currency_unit: cents           # integer cents — no floats
mode: LIVE                     # TEST for QA, MOCK for CI

pipeline_costs:
  PESQUISA: 10                 # $0.10 per research operation
  ANUNCIO: 8                   # $0.08 per ad generation
  FOTO: 15                     # $0.15 per image generation
  FULL: 30                     # $0.30 full pipeline bundle

tiers:
  free:
    monthly_credits: 100       # $1.00 equivalent
    stripe_price_id: null      # No charge
    features: [1 course outline, 2 ad copies, 1 email sequence]
    checkout_required: false
  pro:
    monthly_credits: 2500      # $25.00 equivalent
    stripe_price_id: price_pro_monthly_usd
    price_monthly_usd: 2900    # $29.00/month (cents)
    price_yearly_usd: 27900    # $279.00/year — 20% discount
    features: [unlimited courses, 50 ads/month, 10 email sequences, priority queue]
    checkout_required: true
  enterprise:
    monthly_credits: 20000     # $200.00 equivalent
    stripe_price_id: price_enterprise_monthly_usd
    price_monthly_usd: 9900    # $99.00/month
    price_yearly_usd: 95000    # $950.00/year
    features: [everything pro, custom pipeline_costs, dedicated support, SSO, API access]
    checkout_required: true
    custom_pipeline_costs: true

webhooks:
  provider: stripe
  event: checkout.session.completed
  verification: stripe-signature
  idempotency_field: event_id
  endpoint: /webhooks/stripe/checkout
```

## Function Call Example

```python
result = await monetize_content(
    product={
        "name": "ContentAI Pro",
        "category": "saas",
        "audience": "marketing teams at B2B companies"
    },
    pricing_tier="pro",
    payment_provider="stripe",
    currency="USD"
)
```

## Expected Output

```json
{
  "status": "success",
  "checkout_url": "https://checkout.stripe.com/pay/cs_live_...",
  "credits_consumed": 30,
  "credits_remaining": 2470,
  "course_outline_id": "outline_contentai_pro_v1",
  "ad_validation_score": 0.94,
  "emails_queued": 3,
  "monetization_config_id": "p04_ex_content_monetization_saas",
  "steps_completed": ["PARSE", "PRICING", "CREDITS", "CHECKOUT", "COURSES", "ADS", "EMAILS", "VALIDATE", "DEPLOY"]
}
```

## Revenue Model

| Tier | Price | Credits | Est. Monthly Users | MRR |
|------|-------|---------|-------------------|-----|
| Free | $0 | 100/mo | 500 | $0 |
| Pro | $29/mo | 2500/mo | 200 | $5,800 |
| Enterprise | $99/mo | 20000/mo | 20 | $1,980 |
| **Total** | | | 720 | **$7,780** |

Yearly discount (20%) converts ~40% of Pro users → ARR uplift $13,872/yr.
