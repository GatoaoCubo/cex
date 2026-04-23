---
id: api_reference_stripe
kind: api_reference
pillar: P06
nucleus: n06
title: "API Reference -- Stripe Payment Integration (N06 Commercial)"
version: 1.0.0
quality: 9.0
tags: [stripe, api, payment, checkout, webhook, commercial, revenue]
density_score: 1.0
updated: "2026-04-17"
related:
  - kc_stripe_patterns
  - bld_examples_integration_guide
  - bld_schema_subscription_tier
  - bld_examples_api_reference
  - bld_schema_api_reference
  - bld_examples_faq_entry
  - p04_ex_content_monetization_saas
  - bld_memory_subscription_tier
  - n06_integration_content_factory
  - bld_examples_webhook
---

# API Reference: Stripe Payment Integration

## Scope

Canonical reference for N06's Stripe integration surface. Covers checkout session creation, webhook event processing, subscription management, and revenue reporting API calls.

## Authentication

```
Authorization: Bearer sk_live_<key>        (server-side)
X-Stripe-Version: 2024-06-20               (pin API version)
```

All keys stored in `secret_config` (P09). Never hardcode. Rotate via N05 ops pipeline.

## Core Endpoints

### 1. Create Checkout Session

```
POST https://api.stripe.com/v1/checkout/sessions
```

**Request:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `line_items[0].price` | string | YES | Stripe Price ID (`price_*`) |
| `line_items[0].quantity` | integer | YES | Min 1 |
| `mode` | string | YES | `payment`, `subscription`, `setup` |
| `success_url` | string | YES | Must include `{CHECKOUT_SESSION_ID}` |
| `cancel_url` | string | YES | Return path on abandon |
| `customer_email` | string | NO | Pre-fill email field |
| `customer` | string | NO | Existing `cus_*` ID |
| `allow_promotion_codes` | boolean | NO | Enables discount code field |
| `subscription_data.trial_period_days` | integer | NO | Free trial length |
| `metadata` | object | NO | UTM, referral, affiliate |

**Response (200):**
```json
{
  "id": "cs_live_...",
  "url": "https://checkout.stripe.com/pay/cs_live_...",
  "payment_status": "unpaid",
  "status": "open",
  "customer": null,
  "amount_total": 9900,
  "currency": "usd"
}
```

**Revenue note:** Redirect user to `response.url`. Session expires in 24h. Track session ID in `metadata` for attribution.

---

### 2. Create Subscription (Server-Side)

```
POST https://api.stripe.com/v1/subscriptions
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `customer` | string | YES | `cus_*` ID |
| `items[0].price` | string | YES | Stripe Price ID |
| `trial_period_days` | integer | NO | Overrides price's trial setting |
| `cancel_at_period_end` | boolean | NO | Cancels at period end vs immediate |
| `metadata` | object | NO | `plan_tier`, `nucleus`, `referral_code` |

---

### 3. Retrieve Subscription

```
GET https://api.stripe.com/v1/subscriptions/{sub_id}
```

Key response fields for churn analysis:
- `status`: `trialing | active | past_due | canceled | unpaid | paused`
- `current_period_end`: Unix timestamp -- trigger renewal_workflow at -7 days
- `cancel_at_period_end`: Boolean -- flag for churn_prevention_playbook
- `items.data[0].price.unit_amount`: Current MRR in cents

---

### 4. Update Subscription (Upgrade/Downgrade)

```
POST https://api.stripe.com/v1/subscriptions/{sub_id}
```

For plan changes:
```json
{
  "items": [{"id": "si_*", "price": "price_new_plan"}],
  "proration_behavior": "create_prorations"
}
```

`proration_behavior` options:
- `create_prorations` -- credit unused time (recommended for upgrades)
- `none` -- no proration, starts new period (use for downgrades)
- `always_invoice` -- immediate invoice

---

### 5. Cancel Subscription

```
DELETE https://api.stripe.com/v1/subscriptions/{sub_id}
```

Or soft cancel (at period end):
```
POST https://api.stripe.com/v1/subscriptions/{sub_id}
Body: {"cancel_at_period_end": true}
```

N06 rule: always use `cancel_at_period_end: true` first. Run churn_prevention_playbook before hard cancel.

---

## Webhook Events

All events arrive at `POST /webhook/stripe` with `Stripe-Signature` header.

```python
# Signature verification (Python)
import stripe
event = stripe.Webhook.construct_event(
    payload, sig_header, webhook_secret
)
```

### Critical N06 Events

| Event | Trigger | N06 Action |
|-------|---------|-----------|
| `checkout.session.completed` | Successful payment | Provision access, trigger onboarding |
| `customer.subscription.created` | New subscription | Set entity_memory health=new |
| `customer.subscription.updated` | Plan change | Update tier in entity_memory |
| `customer.subscription.deleted` | Cancellation | Trigger win-back sequence |
| `invoice.payment_failed` | Payment failure | Trigger churn_prevention_playbook |
| `invoice.upcoming` | 7 days pre-renewal | Trigger renewal_workflow |
| `customer.subscription.trial_will_end` | 3 days before trial end | Trigger conversion sequence |
| `charge.refunded` | Refund | Flag for cohort_analysis |

---

## Revenue Reporting

### MRR Calculation via Stripe

```
GET https://api.stripe.com/v1/subscriptions?status=active&limit=100
```

Aggregate: `sum(item.price.unit_amount * item.quantity)` for monthly, divide annual by 12.

### Cohort Data

Use `created` timestamp on `customer` object for cohort bucketing.
Cross-reference with `metadata.utm_source` for channel cohort.

---

## Error Codes

| Code | Meaning | N06 Recovery |
|------|---------|-------------|
| `card_declined` | Card rejected | Retry prompt + backup payment method |
| `insufficient_funds` | Insufficient funds | Offer installment or downgrade |
| `expired_card` | Card expired | Email update request |
| `invalid_cvc` | CVC mismatch | Re-prompt checkout |
| `rate_limit` | API rate limited | Exponential backoff, max 3 retries |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_stripe_patterns]] | upstream | 0.58 |
| [[bld_examples_integration_guide]] | downstream | 0.36 |
| [[bld_schema_subscription_tier]] | related | 0.33 |
| [[bld_examples_api_reference]] | downstream | 0.31 |
| [[bld_schema_api_reference]] | related | 0.30 |
| [[bld_examples_faq_entry]] | downstream | 0.30 |
| [[p04_ex_content_monetization_saas]] | downstream | 0.29 |
| [[bld_memory_subscription_tier]] | downstream | 0.29 |
| [[n06_integration_content_factory]] | downstream | 0.29 |
| [[bld_examples_webhook]] | upstream | 0.29 |
