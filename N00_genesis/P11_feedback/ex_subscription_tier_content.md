---
id: ex_subscription_tier_content
kind: subscription_tier
pillar: P11
version: 1.0.0
title: "Subscription Tier Template -- Content Factory / AI Platform"
description: "Three-tier subscription model for content-as-a-service or AI platform products. Free/Creator/Pro/Enterprise with per-format credits, usage limits, and annual discount."
domain: content_monetization
nucleus: N06
quality: null
tags: [subscription-tier, content-factory, pricing, saas, credits, freemium, ai-platform]
brand_placeholders:
  - BRAND_NAME
  - BRAND_CURRENCY
  - BRAND_SUBSCRIPTION_PRICE_TIER_1
  - BRAND_SUBSCRIPTION_PRICE_TIER_2
  - BRAND_SUBSCRIPTION_PRICE_TIER_3
  - BRAND_DOMAIN
  - BRAND_PARTNER_EMAIL
---

# Subscription Tier Template -- Content Factory / AI Platform

> Three-tier model with credit-based usage. All prices in `{{BRAND_CURRENCY}}`.
> Example values shown as "illustrative" -- replace with your cost basis.

---

## 1. Tier Overview

| Tier | Name | Price/month | Target persona |
|------|------|------------|----------------|
| T0 | Free | 0 | Try before buy |
| T1 | Creator | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_1}} | Solopreneur, <5 pieces/month |
| T2 | Pro | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_2}} | Small team, 20-50 pieces/month |
| T3 | Enterprise | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_3}} | Agency or large brand, 100+ pieces/month |

> Illustrative price ranges: T1 ~49-89, T2 ~149-299, T3 ~499+.
> Your actual prices must reflect your cost basis + target margin.

---

## 2. Credit System

```
1 credit = {{BRAND_CURRENCY}} 1.00 (integer, no decimals)
Minimum credit purchase: 50 credits
Credits do NOT expire within the billing period
Unused credits roll over for 1 month only
```

### 2.1 Credit Costs by Format

| Format | Free allowance | Creator | Pro | Enterprise |
|--------|---------------|---------|-----|------------|
| Blog post (1500w) | 2/month | 8 credits | 6 credits | 4 credits |
| Social media set (5 platforms) | 1/month | 12 credits | 9 credits | 6 credits |
| Video script (90s) | 1/month | 5 credits | 4 credits | 3 credits |
| Video produced (90s) | -- | 25 credits | 18 credits | 12 credits |
| Podcast episode | 1/month | 10 credits | 7 credits | 5 credits |
| Email sequence (5 emails) | -- | 8 credits | 6 credits | 4 credits |
| Landing page (HTML) | -- | 15 credits | 11 credits | 8 credits |
| Course module | -- | 40 credits | 28 credits | 20 credits |

> Note: Credit costs above are examples. Recalculate from your actual LLM + infra cost basis + target margin.

---

## 3. Feature Matrix

| Feature | Free | Creator | Pro | Enterprise |
|---------|------|---------|-----|------------|
| Credits included | 20/month | 100/month | 350/month | 1,500/month |
| Additional credit purchase | NO | YES | YES | YES |
| Brand voice config | 1 preset | 1 voice | 3 voices | Unlimited |
| Output formats | 3 | All | All | All |
| API access | NO | NO | YES | YES |
| White-label | NO | NO | NO | YES |
| Custom integrations | NO | NO | Limited | Full |
| Priority queue | NO | NO | YES | YES |
| Support | FAQ | Email | Chat | Dedicated |
| Team seats | 1 | 1 | 3 | Unlimited |

---

## 4. Annual Discount

```
Annual plan = 2 months free (pay 10, get 12)
Effective monthly: -16.7% off monthly rate

Annual commitment: credit pool is annual; use at any pace within 12 months.
```

---

## 5. Upgrade Triggers (Automated)

| Trigger | Action |
|---------|--------|
| Free: 80% of monthly allowance used | In-app upgrade prompt |
| Creator: 90% of credits used | "Add credits or upgrade to Pro" |
| Pro: 3 consecutive months at max credits | "Upgrade to Enterprise" prompt |
| Enterprise: volume > plan cap | Automatic capacity review call |

---

## 6. Margin Analysis (example framework)

> Replace with your actual cost data:

| Tier | Monthly revenue | Direct cost (example) | Gross margin (example) |
|------|----------------|----------------------|----------------------|
| Creator ({{BRAND_SUBSCRIPTION_PRICE_TIER_1}}/mo) | {{BRAND_SUBSCRIPTION_PRICE_TIER_1}} | ~30% of price | ~70% |
| Pro ({{BRAND_SUBSCRIPTION_PRICE_TIER_2}}/mo) | {{BRAND_SUBSCRIPTION_PRICE_TIER_2}} | ~20% of price | ~80% |
| Enterprise ({{BRAND_SUBSCRIPTION_PRICE_TIER_3}}/mo) | {{BRAND_SUBSCRIPTION_PRICE_TIER_3}} | ~15% of price | ~85% |

> LLM cost at scale (example): ~R$0.50-1.50 per 1000 output tokens.
> Dominant cost driver: video production (TTS narration). Text-only formats are near-zero marginal cost.

---

## 7. Refund Policy

- Free: no payment, no refund
- Creator/Pro/Enterprise: 7-day full refund window (no questions)
- After 7 days: pro-rata credit for unused months
- Disputes: {{BRAND_PARTNER_EMAIL}}

---

## New Brand Variables

- `BRAND_SUBSCRIPTION_PRICE_TIER_1` -- Creator tier monthly price
- `BRAND_SUBSCRIPTION_PRICE_TIER_2` -- Pro tier monthly price
- `BRAND_SUBSCRIPTION_PRICE_TIER_3` -- Enterprise tier monthly price
- `BRAND_CURRENCY` -- currency code (BRL, USD, EUR, etc.)
