---
id: ex_cohort_analysis_content
kind: cohort_analysis
pillar: P11
version: 1.0.0
title: "Cohort Analysis -- Content-Driven Customer Acquisition"
description: "Cohort analysis framework for D2C ecommerce brands using content as primary acquisition channel. Segments customers by acquisition source, measures LTV, retention, and content-to-purchase attribution by cohort."
domain: analytics
nucleus: N06
quality: 9.0
tags: [cohort-analysis, content, d2c, ltv, retention, acquisition, ecommerce]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_VERTICAL
  - BRAND_AOV
  - BRAND_UTM_SOURCE
  - BRAND_GA4_ID
density_score: 1.0
related:
  - kc_cohort_analysis
  - p10_mem_cohort_analysis_builder
  - cohort-analysis-builder
  - bld_instruction_cohort_analysis
  - bld_knowledge_card_cohort_analysis
  - p03_sp_cohort_analysis_builder
  - leverage_map_v2_n06_verification
  - bld_examples_cohort_analysis
  - p01_kc_marketing_best_practices
  - n06_funnel_cex_product
---

# Cohort Analysis -- Content-Driven Customer Acquisition

> Framework for measuring whether content investment produces better-quality customers.
> Replace `{{BRAND_*}}` vars. Example values are illustrative benchmarks.

---

## 1. Cohort Definitions

### 1.1 Acquisition Source Cohorts

| Cohort ID | Definition | UTM tag |
|-----------|-----------|---------|
| C_ORGANIC | Direct / typed URL | utm_source=direct |
| C_INSTAGRAM | Instagram referral | utm_source=instagram |
| C_BLOG | Blog post referral | utm_source=blog |
| C_EMAIL | Email campaign | utm_source=email |
| C_PAID | Paid ads | utm_source=paid |
| C_AFFILIATE | Affiliate / partner link | utm_source=affiliate |
| C_B2B | B2B channel | utm_source=b2b |

### 1.2 Temporal Cohorts

Group customers by first-purchase month:

```
Cohort: [YYYY-MM]
Members: all customers whose first order was in that month
Observation window: 12 months from first purchase
```

---

## 2. Key Metrics per Cohort

| Metric | Formula | Why it matters |
|--------|---------|---------------|
| Cohort size | count(customers) | Volume signal |
| Avg order value at acquisition | sum(first_order_value) / cohort_size | Quality signal |
| M1 retention rate | customers who ordered in M+1 / cohort_size | Stickiness |
| M3 retention rate | customers who ordered in M+3 / cohort_size | Long-term signal |
| M6 LTV | sum(all_orders_within_6mo) / cohort_size | Revenue signal |
| M12 LTV | sum(all_orders_within_12mo) / cohort_size | Full LTV signal |
| AOV trend | avg order value over 12 months | Upsell signal |
| Churn month | month where retention drops below 10% | Lifecycle stage |

---

## 3. Content Attribution Model

### 3.1 Attribution Rules

```
Last-click: UTM source on checkout page
First-click: first session UTM source (stored in user profile)
Multi-touch: weighted across sessions
  - First touch: 30%
  - Middle touches: 40% (shared equally)
  - Last touch: 30%
```

**Recommended model for content brands**: First-touch dominant (40/30/30),
because content creates the initial relationship; last-click often gives credit
to retargeting ads that merely closed content-originated leads.

### 3.2 UTM Convention

```
utm_source={{BRAND_UTM_SOURCE}}        # channel: instagram, blog, email
utm_medium=social|organic|email|paid
utm_campaign={pillar}_{YYYY-MM}        # e.g. educational_2026-04
utm_content={post_id}                  # optional, post-level tracking
```

### 3.3 GA4 Event Tracking

| Event | Trigger | Parameters |
|-------|---------|-----------|
| `content_view` | Blog post view | post_id, pillar, utm_source |
| `product_click` | Product link in content | product_id, source_content |
| `add_to_cart` | Cart action | product_id, source, value |
| `purchase` | Checkout complete | order_id, value, source, content_id |

---

## 4. Cohort Analysis SQL Template

```sql
-- Replace {{BRAND_CRM_TABLE_PREFIX}} with your prefix
-- Monthly cohort retention

WITH cohorts AS (
  SELECT
    customer_id,
    DATE_TRUNC('month', MIN(created_at)) AS cohort_month,
    utm_source AS acquisition_source
  FROM {{BRAND_CRM_TABLE_PREFIX}}_orders
  GROUP BY customer_id, utm_source
),
orders_with_cohort AS (
  SELECT
    o.customer_id,
    c.cohort_month,
    c.acquisition_source,
    DATE_TRUNC('month', o.created_at) AS order_month,
    o.total_amount
  FROM {{BRAND_CRM_TABLE_PREFIX}}_orders o
  JOIN cohorts c ON o.customer_id = c.customer_id
)
SELECT
  cohort_month,
  acquisition_source,
  order_month,
  COUNT(DISTINCT customer_id) AS active_customers,
  ROUND(AVG(total_amount), 2) AS avg_order_value,
  SUM(total_amount) AS cohort_revenue
FROM orders_with_cohort
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3;
```

---

## 5. Benchmark Targets (Example ranges)

> Adjust for your vertical `{{BRAND_VERTICAL}}` and market.

| Metric | Example range | Target |
|--------|--------------|--------|
| M1 retention (blog cohort) | 20-35% | (your data) |
| M1 retention (paid ads cohort) | 12-20% | (your data) |
| Blog cohort AOV vs average | +10-25% premium | (your data) |
| M12 LTV / CAC ratio | >3x | (your data) |
| Content cohort payback period | 2-4 months | (your data) |

---

## 6. Dashboard Views

| View | Chart type | Axis |
|------|-----------|------|
| Retention heatmap | Grid heatmap | Rows=cohort_month, Cols=months_since_first_order |
| LTV by acquisition source | Bar chart | X=source, Y=M12 LTV |
| Cohort AOV trend | Line chart | X=months, Y=avg_order_value, Lines=acquisition_source |
| Content vs paid LTV delta | Side-by-side bar | Compares organic/content vs paid cohorts |

---

## New Brand Variables

- `BRAND_UTM_SOURCE` -- primary UTM source used in content links
- `BRAND_GA4_ID` -- Google Analytics 4 measurement ID (G-XXXXXXXX)
- `BRAND_AOV` -- current average order value (used as baseline)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_cohort_analysis]] | upstream | 0.39 |
| [[p10_mem_cohort_analysis_builder]] | upstream | 0.34 |
| [[cohort-analysis-builder]] | upstream | 0.34 |
| [[bld_instruction_cohort_analysis]] | upstream | 0.34 |
| [[bld_knowledge_card_cohort_analysis]] | upstream | 0.33 |
| [[p03_sp_cohort_analysis_builder]] | upstream | 0.31 |
| [[leverage_map_v2_n06_verification]] | upstream | 0.27 |
| [[bld_examples_cohort_analysis]] | upstream | 0.24 |
| [[p01_kc_marketing_best_practices]] | upstream | 0.24 |
| [[n06_funnel_cex_product]] | related | 0.23 |
