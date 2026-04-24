---
id: n06_integration_content_factory
kind: content_monetization
8f: F6_produce
pillar: P11
title: "Content Factory Integration Spec -- Pricing x Pipeline x Checkout"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: content-factory-integration
quality: 8.9
tags: [integration, content-factory, pricing, pipeline, checkout, stripe, hotmart, eduzz, brand-price-variables]
tldr: "Integration spec connecting N06 pricing artifacts to N03 pipeline workflow. Covers: checkout flow via Stripe/Hotmart/Eduzz, credit system architecture, {{BRAND_PRICE_*}} variable injection, webhook event flow, subscription lifecycle, and cross-nucleus data contracts."
density_score: 0.94
depends_on:
  - pricing_content_factory
  - funnel_content_factory
  - spec_content_factory_v1
linked_artifacts:
  primary: pricing_content_factory
  related:
    - funnel_content_factory
    - roi_content_factory
    - dag_cf_master
    - wf_cf_publish_hotmart
related:
  - n06_content_factory_pricing
  - n06_pricing_content_factory
  - kc_credit_system_design
  - n06_funnel_cex_product
  - p01_kc_content_monetization
  - content-monetization-builder
  - p03_sp_content_monetization_builder
  - p04_tpl_content_monetization
  - n06_kc_content_monetization
  - p12_dr_content_monetization
---

# Content Factory Integration Spec -- Pricing x Pipeline x Checkout

> Pricing decisions are worthless without checkout integration.
> This spec connects N06's pricing model to N03's production pipeline
> and N05's payment infrastructure.

---

## 1. System Architecture

```
CUSTOMER
    |
    v
[LANDING PAGE] ---- N03 builds, N06 provides {{BRAND_PRICE_*}} variables
    |
    | Selects tier / buys Content Pack
    v
[CHECKOUT] -------- Stripe (INT) / Hotmart (BR courses) / Eduzz (BR products)
    |
    | Payment confirmed (webhook)
    v
[CREDIT SYSTEM] --- N05 manages (Supabase)
    |
    | Credits allocated
    v
[CONTENT FACTORY PIPELINE] --- N03 executes (dag_cf_master)
    |
    | Produces 7+ outputs
    v
[DELIVERY] -------- Email + dashboard + download links
    |
    | Usage tracked
    v
[BILLING] --------- Overage billing / subscription renewal
```

---

## 2. Checkout Integration Points

### 2.1 Stripe (Primary -- International + Subscriptions)

**Status**: CONFIGURED (STRIPE_SECRET_KEY in env)

| Integration | Endpoint | Purpose | CEX Artifact |
|------------|----------|---------|-------------|
| Subscription products | `POST /v1/products` | 5 tiers (Free/Creator/Pro/Studio/Factory) | pricing_content_factory.md |
| Price objects | `POST /v1/prices` | Monthly + annual pricing per tier | pricing_content_factory.md |
| Checkout sessions | `POST /v1/checkout/sessions` | One-click purchase flow | funnel_content_factory.md |
| Customer portal | Stripe hosted | Self-service upgrade/downgrade/cancel | -- |
| Webhooks | `POST /api/stripe/webhook` | Payment events -> credit allocation | This spec |
| Credit pack products | `POST /v1/products` | 5 credit pack SKUs | pricing_content_factory.md |
| Usage records | `POST /v1/subscription_items/{id}/usage_records` | Metered billing for overage | This spec |

**Stripe Product Structure**:

```yaml
products:
  - name: "Content Factory Creator"
    id: prod_cf_creator
    prices:
      - id: price_cf_creator_monthly
        amount: 14700  # R$147.00 in centavos
        currency: brl
        recurring: { interval: month }
      - id: price_cf_creator_annual
        amount: 11700  # R$117.00/mo billed annually
        currency: brl
        recurring: { interval: month, interval_count: 12 }
  - name: "Content Factory Pro"
    id: prod_cf_pro
    prices:
      - id: price_cf_pro_monthly
        amount: 49700
        currency: brl
        recurring: { interval: month }
  - name: "Content Factory Studio"
    id: prod_cf_studio
    prices:
      - id: price_cf_studio_monthly
        amount: 149700
        currency: brl
        recurring: { interval: month }
  - name: "Content Factory Factory"
    id: prod_cf_factory
    prices:
      - id: price_cf_factory_monthly
        amount: 399700
        currency: brl
        recurring: { interval: month }

credit_packs:
  - name: "Credit Pack Starter (50)"
    id: prod_cp_starter
    price: 6000  # R$60.00
    metadata: { credits: 50 }
  - name: "Credit Pack Standard (200)"
    id: prod_cp_standard
    price: 20000
    metadata: { credits: 200 }
  - name: "Credit Pack Pro (500)"
    id: prod_cp_pro
    price: 42500
    metadata: { credits: 500 }
  - name: "Credit Pack Bulk (1000)"
    id: prod_cp_bulk
    price: 75000
    metadata: { credits: 1000 }
  - name: "Credit Pack Enterprise (5000)"
    id: prod_cp_enterprise
    price: 325000
    metadata: { credits: 5000 }
```

### 2.2 Hotmart (Courses -- BR Market)

**Status**: CONFIGURED (MCP wired to N06)

| Integration | Purpose | CEX Artifact |
|------------|---------|-------------|
| Product creation | Course "CEX na Pratica" (R$497 / R$997) | output_monetization_business_plan.md |
| Checkout page | Hosted by Hotmart (zero dev effort) | funnel_content_factory.md |
| Affiliate program | 25% commission, Hotmart handles payouts | funnel_content_factory.md |
| Webhook: purchase | `PURCHASE_APPROVED` -> grant course access | This spec |
| Webhook: refund | `PURCHASE_REFUNDED` -> revoke access | This spec |
| Student area | Hotmart hosts course modules | spec_content_factory_v1.md |

**Hotmart Products**:

| Product | Price | Commission | Affiliate % |
|---------|-------|-----------|------------|
| CEX Builder (course) | R$497 | R$24.85 (Hotmart 5%) | 25% (R$124.25) |
| CEX Master (course) | R$997 | R$49.85 (Hotmart 5%) | 25% (R$249.25) |

### 2.3 Eduzz (Alternative -- BR Market)

**Status**: Not yet configured. Backup for Hotmart.

| Integration | Purpose | Priority |
|------------|---------|---------|
| Product listing | Mirror Hotmart products | Low (only if Hotmart issues) |
| Checkout | Alternative payment processor | Low |
| Webhook | Same flow as Hotmart | Low |

**When to activate Eduzz**: If Hotmart account issues arise, or if A/B testing shows higher conversion on Eduzz checkout pages.

---

## 3. Credit System Architecture

### 3.1 Data Model (Supabase)

```sql
-- Credit accounts (1 per customer)
CREATE TABLE credit_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES customers(id),
    stripe_customer_id TEXT,
    tier TEXT NOT NULL DEFAULT 'free',
    credits_balance INTEGER NOT NULL DEFAULT 0,
    credits_allocated INTEGER NOT NULL DEFAULT 0,  -- monthly allocation
    credits_used_this_period INTEGER NOT NULL DEFAULT 0,
    period_start TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    period_end TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Credit transactions (audit trail)
CREATE TABLE credit_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES credit_accounts(id),
    amount INTEGER NOT NULL,  -- positive = credit, negative = debit
    type TEXT NOT NULL,  -- 'allocation', 'usage', 'purchase', 'refund', 'overage'
    description TEXT,
    format TEXT,  -- which content format consumed credits
    brief_id UUID,  -- links to the content brief
    stripe_payment_id TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Content briefs (links to pipeline)
CREATE TABLE content_briefs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES credit_accounts(id),
    topic TEXT NOT NULL,
    audience TEXT,
    formats JSONB NOT NULL,  -- ["blog", "social", "video_short"]
    credits_estimated INTEGER NOT NULL,
    credits_actual INTEGER,
    status TEXT NOT NULL DEFAULT 'pending',  -- pending, processing, complete, failed
    pipeline_run_id TEXT,  -- links to dag_cf_master execution
    outputs JSONB,  -- URLs/paths to produced content
    quality_score REAL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);
```

### 3.2 Credit Allocation by Tier

| Tier | Monthly Credits | Overage Rate | Reset Policy |
|------|---------------|-------------|-------------|
| Free | 15 (capped per format) | N/A | Monthly reset, no rollover |
| Creator | 150 | R$1.20/credit | Monthly reset, no rollover |
| Pro | 600 | R$1.00/credit | Monthly reset, 50 credits rollover max |
| Studio | 2,000 | R$0.85/credit | Monthly reset, 200 credits rollover |
| Factory | 6,000 | R$0.70/credit | Monthly reset, 500 credits rollover |

### 3.3 Credit Deduction Flow

```
Customer submits brief
    |
    v
Estimate credits needed (based on formats selected)
    |
    v
Check balance >= estimate?
    |
    +--> YES: Reserve credits (soft lock)
    |         |
    |         v
    |    Run dag_cf_master pipeline
    |         |
    |         v
    |    Deduct actual credits used (may differ from estimate)
    |    Release excess reservation
    |         |
    |         v
    |    Deliver outputs
    |
    +--> NO: Check overage policy
              |
              +--> Overage allowed (paid tier): Proceed, bill overage via Stripe
              +--> No overage (Free): Return error "Upgrade to continue"
```

---

## 4. {{BRAND_PRICE_*}} Variable Injection

### 4.1 Variable Registry

These variables are injected into landing pages, emails, and sales copy by `brand_inject.py`:

| Variable | Value (Current) | Source | Used In |
|----------|----------------|--------|---------|
| `{{BRAND_PRICE_FREE}}` | R$0 | pricing_content_factory.md | Landing page, comparison table |
| `{{BRAND_PRICE_CREATOR}}` | R$147/mo | pricing_content_factory.md | Pricing page, checkout |
| `{{BRAND_PRICE_CREATOR_ANNUAL}}` | R$117/mo | pricing_content_factory.md | Annual toggle |
| `{{BRAND_PRICE_PRO}}` | R$497/mo | pricing_content_factory.md | Pricing page, checkout |
| `{{BRAND_PRICE_PRO_ANNUAL}}` | R$397/mo | pricing_content_factory.md | Annual toggle |
| `{{BRAND_PRICE_STUDIO}}` | R$1,497/mo | pricing_content_factory.md | Pricing page, checkout |
| `{{BRAND_PRICE_FACTORY}}` | R$3,997/mo | pricing_content_factory.md | Pricing page, checkout |
| `{{BRAND_PRICE_TRIPWIRE}}` | R$19 | funnel_content_factory.md | Tripwire landing |
| `{{BRAND_PRICE_CORE_OFFER}}` | R$147 | funnel_content_factory.md | Core offer landing |
| `{{BRAND_PRICE_COURSE_BUILDER}}` | R$497 | output_monetization_business_plan.md | Hotmart checkout |
| `{{BRAND_PRICE_COURSE_MASTER}}` | R$997 | output_monetization_business_plan.md | Hotmart checkout |
| `{{BRAND_PRICE_CREDIT_STARTER}}` | R$60 (50 credits) | pricing_content_factory.md | Credit pack purchase |
| `{{BRAND_PRICE_CREDIT_PRO}}` | R$425 (500 credits) | pricing_content_factory.md | Credit pack purchase |
| `{{BRAND_PRICE_SAVINGS_VS_AGENCY}}` | R$42,411/mo | roi_content_factory.md | ROI section |
| `{{BRAND_PRICE_BREAK_EVEN}}` | <2 days | roi_content_factory.md | Sales copy |

### 4.2 How Injection Works

```
N03 builds landing page with {{BRAND_PRICE_*}} placeholders
    |
    v
brand_inject.py reads .cex/brand/brand_config.yaml + pricing artifacts
    |
    v
Replaces all {{BRAND_PRICE_*}} with current values
    |
    v
Output: production-ready HTML with real prices
```

**Why variables, not hardcoded prices?** When pricing changes (A/B test, annual adjustment, regional pricing), update 1 source file -> all landing pages, emails, and sales copy update automatically. Zero manual find-and-replace.

### 4.3 Adding Price Variables to brand_config.yaml

```yaml
# Add to .cex/brand/brand_config.yaml under pricing: section
pricing:
  BRAND_PRICING_MODEL: "hybrid"
  BRAND_PRICE_FREE: 0
  BRAND_PRICE_CREATOR: 14700       # centavos (R$147.00)
  BRAND_PRICE_CREATOR_ANNUAL: 11700
  BRAND_PRICE_PRO: 49700
  BRAND_PRICE_PRO_ANNUAL: 39700
  BRAND_PRICE_STUDIO: 149700
  BRAND_PRICE_FACTORY: 399700
  BRAND_PRICE_TRIPWIRE: 1900
  BRAND_PRICE_CORE_OFFER: 14700
  BRAND_PRICE_COURSE_BUILDER: 49700
  BRAND_PRICE_COURSE_MASTER: 99700
  BRAND_PRICE_CREDIT_STARTER: 6000
  BRAND_PRICE_CREDIT_STANDARD: 20000
  BRAND_PRICE_CREDIT_PRO: 42500
  BRAND_PRICE_CREDIT_BULK: 75000
  BRAND_PRICE_CREDIT_ENTERPRISE: 325000
  BRAND_CHECKOUT_PRIMARY: "stripe"
  BRAND_CHECKOUT_SECONDARY: "hotmart"
  BRAND_CURRENCY_PRIMARY: "BRL"
  BRAND_CURRENCY_SECONDARY: "USD"
```

---

## 5. Webhook Event Flow

### 5.1 Stripe Webhook Events

| Event | Action | Owner |
|-------|--------|-------|
| `checkout.session.completed` | Create credit_account, allocate credits for tier | N05 |
| `customer.subscription.created` | Initialize subscription, set period_start/end | N05 |
| `customer.subscription.updated` | Update tier, adjust credits (upgrade/downgrade) | N05 |
| `customer.subscription.deleted` | Set tier=free, stop credit allocation | N05 |
| `invoice.paid` | Reset monthly credits, log allocation transaction | N05 |
| `invoice.payment_failed` | Flag account, send retry email, grace period 3 days | N05 |
| `charge.succeeded` (one-time) | Add credits from credit pack purchase | N05 |
| `charge.refunded` | Deduct credits, flag if negative balance | N05 |

### 5.2 Hotmart Webhook Events

| Event | Action | Owner |
|-------|--------|-------|
| `PURCHASE_APPROVED` | Grant course access, create student record | N06 |
| `PURCHASE_REFUNDED` | Revoke access, log refund | N06 |
| `PURCHASE_CHARGEBACK` | Block account, flag for review | N06 |
| `SUBSCRIPTION_CANCELLATION` | Remove from community, send win-back email | N06 |

### 5.3 Webhook Security

```yaml
webhook_security:
  stripe:
    endpoint_secret: "whsec_..." # in env, never in code
    signature_header: "Stripe-Signature"
    verification: "stripe.Webhook.construct_event(payload, sig, secret)"
  hotmart:
    hottok: "..." # in env
    verification: "X-Hotmart-Hottok header matches stored hottok"
  eduzz:
    api_key: "..." # in env
    verification: "HMAC-SHA256 signature validation"
```

---

## 6. Cross-Nucleus Data Contracts

### 6.1 N06 (Commercial) -> N03 (Pipeline)

When a customer submits a brief:

```yaml
# Contract: N06 sends to N03 via dag_cf_master
brief_request:
  brief_id: "uuid"
  customer_id: "uuid"
  topic: "string"
  audience: "string"
  formats:
    - blog
    - social_set
    - video_short
    - podcast
    - course_module
    - ebook_chapter
    - presentation
    - email_sequence
    - landing_page
  brand_config_path: ".cex/brand/customer_{id}/brand_config.yaml"
  quality_tier: "basic"  # or "premium"
  credits_budget: 140
  callback_url: "/api/brief/{brief_id}/complete"
```

### 6.2 N03 (Pipeline) -> N06 (Commercial)

When pipeline completes:

```yaml
# Contract: N03 returns to N06
brief_result:
  brief_id: "uuid"
  status: "complete"  # or "partial" or "failed"
  formats_produced:
    blog:
      path: "output/customer_{id}/blog_{topic}.md"
      credits_used: 8
      quality_score: 9.1
    social_set:
      path: "output/customer_{id}/social_{topic}/"
      credits_used: 12
      quality_score: 8.7
    # ... etc for each format
  total_credits_used: 138
  total_quality_avg: 8.9
  pipeline_duration_seconds: 480
  errors: []
```

### 6.3 N06 (Commercial) -> N05 (Operations)

Billing instructions:

```yaml
# Contract: N06 sends to N05 for billing
billing_instruction:
  account_id: "uuid"
  action: "debit_credits"
  amount: 138
  brief_id: "uuid"
  overage: false  # true if exceeds monthly allocation
  stripe_customer_id: "cus_..."
```

### 6.4 N05 (Operations) -> N06 (Commercial)

Usage reports for pricing optimization:

```yaml
# Contract: N05 sends monthly to N06
usage_report:
  period: "2026-04"
  total_customers: 135
  by_tier:
    creator: { count: 78, avg_usage: 68%, churn: 5.2% }
    pro: { count: 42, avg_usage: 72%, churn: 4.1% }
    studio: { count: 12, avg_usage: 61%, churn: 2.8% }
    factory: { count: 3, avg_usage: 45%, churn: 0% }
  top_formats: ["blog", "social_set", "email_sequence"]
  overage_revenue: 4520  # R$45.20
  credit_pack_revenue: 28500  # R$285.00
```

---

## 7. Subscription Lifecycle

```
SIGNUP (checkout.session.completed)
    |
    v
ONBOARDING (Day 0-7)
    |  Email: "Welcome + first brief tutorial"
    |  Action: Allocate monthly credits
    |  Goal: First brief within 24h
    |
    v
ACTIVATION (Day 1-14)
    |  Trigger: 3+ briefs completed
    |  Email: "Your first month: X hours saved, Y pieces created"
    |  Goal: Habit formation
    |
    v
RETENTION (Month 2+)
    |  Monthly: "Your content report" email with ROI data
    |  Trigger: Usage < 30% -> "Content ideas for this month" email
    |  Trigger: Usage > 80% -> "Upgrade to save on overages" prompt
    |
    v
EXPANSION (Month 3+)
    |  Trigger: Hit credit limit 2x -> "Upgrade" CTA
    |  Trigger: 6 months active -> "Go annual, save 20%"
    |  Trigger: Agency signals (multiple brands) -> "Studio is for you"
    |
    v
AT RISK (signals)
    |  No brief in 30 days -> "We miss you" + free credit bonus
    |  Payment failed -> Grace period 3 days + retry email
    |  Cancel intent -> "Before you go: here's your ROI this year"
    |
    v
CHURNED (subscription deleted)
    |  Exit survey (1 question: "Why?")
    |  Win-back email at Day 30 + Day 90 ("We improved X")
    |  Data retained 12 months for potential return
```

---

## 8. Implementation Priority

| # | Integration | Owner | Dependencies | Priority | Effort |
|---|------------|-------|-------------|---------|--------|
| 1 | Stripe products + prices (5 tiers) | N05 | Stripe MCP | **P0** | 2h |
| 2 | Credit account schema (Supabase) | N05 | Supabase | **P0** | 3h |
| 3 | Checkout session + webhook handler | N05 | Stripe #1 | **P0** | 4h |
| 4 | {{BRAND_PRICE_*}} variables in brand_config | N06 | brand_inject.py | **P1** | 1h |
| 5 | Credit deduction on brief completion | N05 | Credit schema #2 | **P1** | 2h |
| 6 | Landing page with pricing variables | N03 | Brand variables #4 | **P1** | 3h |
| 7 | Hotmart course products + webhooks | N06 | Hotmart MCP | **P2** | 3h |
| 8 | Overage billing automation | N05 | Stripe metered billing | **P2** | 4h |
| 9 | Usage dashboard (customer-facing) | N03 | Credit transactions | **P2** | 6h |
| 10 | Eduzz backup integration | N05 | -- | **P3** | 4h |

**Total estimated effort**: ~32 hours across N03/N05/N06

---

*Generated by N06 Commercial Nucleus -- Content Factory Integration Spec*
*Connects pricing to pipeline to checkout. Every variable has a source.*
*Zero hardcoded prices. One YAML change updates all surfaces.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_content_factory_pricing]] | sibling | 0.41 |
| [[n06_pricing_content_factory]] | sibling | 0.36 |
| [[kc_credit_system_design]] | upstream | 0.35 |
| [[n06_funnel_cex_product]] | sibling | 0.34 |
| [[p01_kc_content_monetization]] | related | 0.34 |
| [[content-monetization-builder]] | related | 0.33 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.32 |
| [[p04_tpl_content_monetization]] | sibling | 0.31 |
| [[n06_kc_content_monetization]] | upstream | 0.30 |
| [[p12_dr_content_monetization]] | downstream | 0.30 |
