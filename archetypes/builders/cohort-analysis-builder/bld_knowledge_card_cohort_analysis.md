---
kind: knowledge_card
id: bld_knowledge_card_cohort_analysis
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for cohort_analysis production
quality: 9.2
title: "Knowledge Card Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, knowledge_card]
tldr: "Domain knowledge for cohort_analysis production"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Cohort analysis groups users by shared characteristics (e.g., acquisition date, first event, plan tier) and tracks how each group behaves over time -- measuring retention, engagement, and lifetime value (LTV). In product analytics, the canonical cohort definition is acquisition date (D0), with retention measured at D1, D7, D30, and D90. Tools like Mixpanel and Amplitude provide cohort retention curves out-of-the-box. For LTV prediction, the BG/NBD (Beta Geometric/Negative Binomial) model (Fader & Hardie, 2009) is the industry standard for non-contractual settings; Kaplan-Meier survival curves are used for contractual/subscription churn. RFM (Recency, Frequency, Monetary) scoring overlays behavioral segmentation on top of cohort groups.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| Cohort | Group of users sharing a defining event (e.g., sign-up date, first purchase) | Mixpanel Cohort Docs |
| D1/D7/D30/D90 Retention | Percentage of cohort active 1/7/30/90 days after D0 | Amplitude Retention Benchmarks |
| Acquisition Cohort | Users grouped by first-seen date (most common cohort type) | Google Analytics 4 |
| Behavioral Cohort | Users grouped by a shared action (e.g., "sent first message") | Mixpanel, Amplitude |
| Retention Rate | cohort_active_at_day_N / cohort_size | Standard product metric |
| Churn Rate | 1 - retention_rate per period | SaaS standard |
| LTV (Lifetime Value) | Sum of predicted revenue per cohort user over lifetime | Fader & Hardie (2009) |
| BG/NBD Model | Probabilistic LTV model for non-contractual settings | Fader & Hardie (2005, 2009) |
| Kaplan-Meier Survival | Non-parametric estimator for time-to-churn in subscriptions | Standard statistics |
| RFM Analysis | Recency, Frequency, Monetary behavioral scoring layer on cohorts | Marketing Science Institute (1990) |
| Cohort Heatmap | Grid visualization: rows = cohort, columns = day/week/month | Amplitude, Mixpanel UI |
| LTV:CAC Ratio | LTV divided by Customer Acquisition Cost -- segment health metric | SaaStr, a16z |

## Day-N Retention Benchmarks (SaaS)

| Day | Mobile Apps | B2C SaaS | B2B SaaS | Source |
|-----|------------|---------|---------|--------|
| D1 | 25-40% | 40-60% | 50-70% | Amplitude 2024 Benchmarks |
| D7 | 10-20% | 20-35% | 35-55% | Mixpanel Industry Report |
| D30 | 5-10% | 10-20% | 25-45% | Andreessen Horowitz |
| D90 | 2-5% | 5-15% | 20-40% | OpenView SaaS benchmarks |

## LTV Model Comparison

| Model | Setting | Requires | Accuracy | Tool Support |
|-------|---------|---------|---------|-------------|
| BG/NBD | Non-contractual (e-comm) | Transaction history | High | lifetimes (Python) |
| Kaplan-Meier | Contractual (SaaS) | Subscription events | Medium | scikit-survival |
| Simple CLV | Any | ARPU + churn rate | Low-Medium | Manual / Excel |
| Pareto/NBD | Non-contractual | Buy-till-you-die | High | lifetimes (Python) |

## Industry Standards
- Amplitude Retention Chart methodology (event-based cohort grouping)
- Mixpanel Cohort Analysis (behavioral cohort + retention curves)
- BG/NBD probabilistic CLV model -- Fader & Hardie (2005, 2009)
- Kaplan-Meier survival analysis (standard for subscription churn)
- RFM Model -- Marketing Science Institute (1990)
- Andreessen Horowitz / OpenView SaaS retention benchmarks

## Common Patterns
1. Always define cohort D0 event explicitly: sign-up, first payment, or first key action.
2. Measure D1/D7/D30/D90 retention at minimum; add D180/D365 for SaaS.
3. Build cohort heatmaps to identify which acquisition periods have best retention.
4. Use BG/NBD for LTV in e-commerce; Kaplan-Meier for subscription SaaS.
5. Layer RFM scoring on top of cohorts to create actionable re-engagement segments.
6. Compare cohort LTV:CAC by acquisition channel to optimize marketing mix.

## Pitfalls
- Using calendar cohorts (monthly) when event cohorts (first purchase) give more signal.
- Small cohort sizes invalidating retention percentages -- set minimum cohort size (n >= 100).
- Confusing retention (returning users) with engagement (session count).
- Not controlling for seasonality: acquisition cohorts from holiday periods behave differently.
- Overfitting LTV models to short historical windows -- need 12+ months for reliable BG/NBD.
