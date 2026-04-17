---
id: ex_schedule_promo_calendar
kind: schedule
pillar: P12
version: 1.0.0
title: "Promo Calendar Schedule Template -- Quarterly Overlay"
description: "Quarterly promotional calendar with holiday triggers, content-promo alignment, UTM tagging, and channel-specific rules. Generic template with {{BRAND_*}} placeholders."
domain: content_monetization
nucleus: N06
quality: 9.0
tags: [schedule, promo-calendar, quarterly, ecommerce, utm, campaigns, content-alignment]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_REGION
  - BRAND_VERTICAL
  - BRAND_PROMO_DATES
  - BRAND_UTM_SOURCE
  - BRAND_GA4_ID
  - BRAND_CURRENCY
density_score: 1.0
---

# Promo Calendar Schedule Template -- Quarterly Overlay

> Quarterly promotional rhythm for {{BRAND_NAME}}.
> Replace `{{BRAND_PROMO_DATES}}` with your actual promotional dates.
> Holiday list assumes Brazilian market; adjust for `{{BRAND_REGION}}`.

---

## 1. Calendar Structure

```
QUARTER = 13 weeks
  |-- AWARENESS WEEK (w1-w2): brand content, no hard sell
  |-- CONSIDERATION PHASE (w3-w10): product content + soft CTAs
  |-- CONVERSION SPRINT (w11-w12): promo + urgency
  |-- RETENTION WEEK (w13): thank you + next cycle setup
```

---

## 2. Trigger Categories

### 2.1 Hard Date Triggers ({{BRAND_REGION}} defaults)

| Date | Event | Promo type |
|------|-------|-----------|
| Jan 20-31 | Post-holiday recovery | Clearance + new arrivals |
| Feb 12 | Valentine's Day | Gift bundles |
| Mar 08 | International Women's Day | Cause-aligned campaign |
| Apr/May | Easter (variable) | Seasonal + gifting |
| May 12 | Mothers Day (BR) | High-conversion window |
| Jun 12 | Lovers Day (BR) | Gift bundles |
| Jul 15-31 | Winter clearance (BR) | Category discounts |
| Aug | Gato Day? / niche date | Vertical-specific |
| Sep 07 | Brazil Independence Day | Patriotic theme (optional) |
| Oct 12 | Children's Day (BR) | Gift + family content |
| Nov 1-29 | Pre-Black Friday buildup | Hype + waitlist |
| Nov last Fri | Black Friday | Peak conversion |
| Nov Mon | Cyber Monday | Digital + bundles |
| Dec 1-25 | Christmas buildup | Gift guide + urgency |
| Dec 25 | Christmas | Peak gifting |
| Dec 26-31 | Year-end clearance | Last chance |

> Replace dates and events with `{{BRAND_PROMO_DATES}}` from your config.

---

## 3. Promo Types + Mechanics

| Type | Mechanic | When to use |
|------|---------|------------|
| Percentage discount | 10-30% off | High-volume triggers (BF, XMAS) |
| Free shipping | No threshold fee | AOV below {{BRAND_CURRENCY}} (threshold) |
| Bundle deal | Buy 2 get 1 / kit discount | Shoulder periods |
| Flash sale | 4-24h offer | Mid-week engagement spike |
| Early access | VIP list gets deal 24h early | Loyalty + B2B channel |
| Coupon code | Affiliate / influencer specific | Attribution tracking |

---

## 4. Content-Promo Alignment Rules

| Weeks before promo | Content action |
|-------------------|----------------|
| -4 weeks | Educational content introduces product category |
| -2 weeks | Social proof + testimonials for key products |
| -1 week | Urgency signals + "coming soon" teaser |
| Promo week | Daily content with offer + countdown |
| +1 week | Thank you content + nurture for non-purchasers |

---

## 5. UTM Tagging Convention

```
Base URL: https://{{BRAND_DOMAIN}}/{product_or_collection}

Promo campaign UTM:
  utm_source={{BRAND_UTM_SOURCE}}
  utm_medium=social|email|sms|whatsapp
  utm_campaign={promo_name}_{year}   # e.g. black_friday_2026
  utm_content={creative_id}          # e.g. carousel_01
  utm_term={discount_pct}            # optional, e.g. 20off

Example:
  https://{{BRAND_DOMAIN}}/produtos?
    utm_source=instagram&
    utm_medium=social&
    utm_campaign=black_friday_2026&
    utm_content=carousel_01
```

---

## 6. Channel-Specific Rules

| Channel | Lead time | Max frequency during promo | Tone |
|---------|-----------|---------------------------|------|
| Instagram feed | 2 days | 1 post/day | Aspirational + urgent |
| Instagram stories | Same day | 3 stories/day | Direct + urgent |
| WhatsApp blast | 1 day | 1 message/week max | Personal + warm |
| Email | 3 days | 1 per day (promo week) | Benefit-led |
| Blog | 1 week | 1 post per promo | SEO + evergreen |

---

## 7. GA4 Event Tracking for Promos

| Event | Trigger | Key params |
|-------|---------|-----------|
| `promo_view` | User sees promo banner/post | promo_id, channel |
| `promo_click` | Click on promo CTA | promo_id, discount_pct |
| `coupon_applied` | Coupon used at checkout | coupon_code, order_value |
| `purchase` (with promo flag) | Promo-attributed purchase | promo_id, discount_pct, order_value |

```javascript
// GA4 measurement ID: {{BRAND_GA4_ID}}
gtag('event', 'promo_view', {
  promo_id: 'black_friday_2026',
  channel: 'instagram',
  discount_pct: '20'
})
```

---

## 8. Post-Promo Retrospective Template

| Metric | Target | Actual | Delta |
|--------|--------|--------|-------|
| Revenue during promo | (plan) | (actual) | -- |
| New customers acquired | (plan) | (actual) | -- |
| Avg order value | {{BRAND_CURRENCY}} {{BRAND_AOV}} | (actual) | -- |
| Top-performing channel | (predicted) | (actual) | -- |
| Coupon redemption rate | (plan) | (actual) | -- |
| Return rate | <10% | (actual) | -- |

---

## New Brand Variables

- `BRAND_PROMO_DATES` -- comma-separated list of planned promo dates
- `BRAND_REGION` -- geographic region (affects holiday calendar)
- `BRAND_GA4_ID` -- Google Analytics 4 ID for event tracking
