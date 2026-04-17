---
id: ex_cohort_analysis_attribution
kind: cohort_analysis
pillar: P11
version: 1.0.0
title: "Attribution Framework -- Content + Promo Multi-Touch"
description: "Multi-touch attribution framework for content-driven ecommerce. Defines attribution models, UTM taxonomy, GA4 event contracts, and cohort segmentation by promo participation."
domain: analytics
nucleus: N06
quality: null
tags: [cohort-analysis, attribution, multi-touch, utm, ga4, promo, content, ecommerce]
brand_placeholders:
  - BRAND_DOMAIN
  - BRAND_UTM_SOURCE
  - BRAND_GA4_ID
  - BRAND_CURRENCY
  - BRAND_PROMO_DATES
---

# Attribution Framework -- Content + Promo Multi-Touch

> Answers: which content produces revenue, and which promos produce loyal customers?
> Replace `{{BRAND_*}}` vars. Requires GA4 + Supabase event data.

---

## 1. Attribution Models Supported

| Model | Logic | Best for |
|-------|-------|---------|
| Last-click | 100% credit to final touchpoint before purchase | Evaluating closing channels |
| First-click | 100% credit to acquisition touchpoint | Evaluating awareness channels |
| Linear | Equal credit across all touchpoints | Balanced view |
| Time-decay | More credit to recent touchpoints | Short sales cycles |
| Position-based (40/20/40) | 40% first + 20% middle + 40% last | Content brands (recommended) |
| **Content-first (30/40/30)** | 30% first + 40% middle (content) + 30% last | When content is primary mid-funnel driver |

> Recommended for {{BRAND_NAME}}: **Content-first (30/40/30)**.
> Rationale: content drives consideration; retargeting/promo closes. Last-click alone
> undervalues content investment by attributing sales to closing ads.

---

## 2. UTM Taxonomy (Full Spec)

```yaml
# UTM parameter spec for {{BRAND_DOMAIN}}
utm_parameters:
  utm_source:
    description: "Primary acquisition channel"
    allowed_values:
      - instagram       # Instagram organic + promoted
      - facebook        # Facebook organic + promoted
      - blog            # {{BRAND_DOMAIN}}/blog referral
      - email           # Email campaign
      - whatsapp        # WhatsApp broadcast
      - youtube         # YouTube channel
      - google          # Google organic search
      - paid_google     # Google Ads
      - paid_meta       # Meta Ads (unified)
      - affiliate       # Affiliate / partner link
      - direct          # Typed URL / unknown

  utm_medium:
    allowed_values:
      - social          # Organic social
      - paid            # Paid media
      - email           # Email
      - sms             # SMS
      - messaging       # WhatsApp / DM
      - organic         # Organic search
      - referral        # External site link
      - affiliate       # Affiliate program

  utm_campaign:
    format: "{pillar}_{YYYY-MM}"
    examples:
      - educational_2026-04
      - black_friday_2026
      - mothers_day_2026
      - product_launch_donut_2026

  utm_content:
    format: "{format}_{sequence}"
    examples:
      - reel_01
      - carousel_03
      - email_subject_A
      - blog_post_enrichment

  utm_term:
    description: "Optional. Used for paid keyword or discount code."
    examples:
      - 20off
      - feline_anxiety
```

---

## 3. Event Contract (GA4)

### 3.1 Required Events

| Event name | Trigger | Required params |
|------------|---------|----------------|
| `page_view` | Every page | page_path, page_title |
| `content_view` | Blog post open | content_id, pillar, utm_source |
| `product_view` | Product page open | product_id, product_name, value |
| `add_to_cart` | Cart add | product_id, value, utm_source |
| `begin_checkout` | Checkout start | cart_value, num_items |
| `purchase` | Order confirmed | transaction_id, value, items[], coupon |

### 3.2 Custom Events (Content Attribution)

| Event name | Trigger | Params |
|------------|---------|--------|
| `content_product_click` | Product link clicked inside blog post | content_id, product_id |
| `persona_chat_start` | AI persona chat opened | source_page |
| `persona_recommendation_click` | Product rec clicked in chat | product_id, recommendation_rank |
| `promo_banner_view` | Promo banner rendered | promo_id, placement |
| `affiliate_link_click` | Affiliate UTM link clicked | affiliate_id, product_id |

### 3.3 GA4 Configuration

```javascript
// Measurement ID: {{BRAND_GA4_ID}}
// Recommended: enable Google Signals + User-ID for cross-device

gtag('config', '{{BRAND_GA4_ID}}', {
  send_page_view: true,
  user_id: '<authenticated_user_id>',  // when logged in
  custom_map: {
    dimension1: 'acquisition_source',
    dimension2: 'content_pillar',
    metric1: 'content_influenced_revenue'
  }
})
```

---

## 4. Promo Cohort Segmentation

### 4.1 Cohort Types

| Cohort | Definition | Metric hypothesis |
|--------|-----------|-------------------|
| Promo-acquired | First purchase during a promo event | Higher CAC, lower LTV |
| Organic-acquired | First purchase without promo code | Lower CAC, higher LTV |
| Content-acquired (blog) | First session via blog UTM | Premium AOV, high M6 retention |
| Influencer-acquired | First session via affiliate UTM | Variable quality, track individually |

### 4.2 Promo Participation Cohorts

| Cohort | Definition |
|--------|-----------|
| Promo-only buyers | Purchased exclusively during promo windows |
| Full-price buyers | Never used a promo code |
| Occasional promo | Mixed behavior |

**Key insight to track**: LTV of promo-only cohort vs full-price cohort over 12 months.
If promo-only LTV < 2x CAC, promo strategy is value-destructive.

---

## 5. Attribution SQL Template

```sql
-- Multi-touch attribution by UTM source
-- Replace {{BRAND_CRM_TABLE_PREFIX}}

WITH sessions_ranked AS (
  SELECT
    session_id,
    customer_id,
    utm_source,
    utm_campaign,
    session_time,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY session_time ASC)  AS first_rank,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY session_time DESC) AS last_rank,
    COUNT(*) OVER (PARTITION BY customer_id) AS total_sessions
  FROM {{BRAND_CRM_TABLE_PREFIX}}_sessions
  WHERE customer_id IN (SELECT customer_id FROM {{BRAND_CRM_TABLE_PREFIX}}_orders)
)
SELECT
  utm_source,
  utm_campaign,
  COUNT(DISTINCT customer_id) AS customers,
  ROUND(AVG(order_value), 2) AS avg_order_value,
  SUM(order_value) AS total_revenue,
  -- Position-based credit (40/20/40 simplified)
  ROUND(SUM(order_value) * CASE
    WHEN first_rank = 1 THEN 0.4
    WHEN last_rank = 1  THEN 0.4
    ELSE 0.2 / NULLIF(total_sessions - 2, 0)
  END, 2) AS attributed_revenue
FROM sessions_ranked
JOIN {{BRAND_CRM_TABLE_PREFIX}}_orders USING (customer_id)
GROUP BY 1, 2
ORDER BY attributed_revenue DESC;
```

---

## 6. Reporting Cadence

| Report | Frequency | Audience | Key metrics |
|--------|-----------|---------|-------------|
| Channel attribution summary | Weekly | Marketing | Revenue by UTM source (last-click) |
| Content LTV comparison | Monthly | Leadership | Blog vs paid cohort LTV at M3/M6 |
| Promo cohort analysis | Post-promo | Commercial | Promo buyer retention + repeat rate |
| Full attribution model compare | Quarterly | Strategy | All models side-by-side |

---

## New Brand Variables

- `BRAND_UTM_SOURCE` -- default UTM source for primary content channel
- `BRAND_GA4_ID` -- GA4 measurement ID
- `BRAND_PROMO_DATES` -- list of planned promo dates for cohort labeling
