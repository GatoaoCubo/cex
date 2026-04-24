---
id: eval_metric_commercial
kind: eval_metric
8f: F7_govern
pillar: P07
nucleus: n06
title: "Eval Metric -- Commercial KPI Framework"
version: 1.0.0
quality: 9.0
tags: [eval-metric, kpi, commercial, mrr, arr, churn, ltv, cac, revenue]
density_score: 1.0
related:
  - n06_roi_content_factory
  - n06_monetization_audit_2026_04_08
  - p08_pat_pricing_framework
  - bld_knowledge_card_subscription_tier
  - p08_pat_funnel_architecture
  - bld_memory_subscription_tier
  - pricing_optimization_memory
  - p02_ax_commercial_nucleus
  - leverage_map_v2_n06_verification
  - bld_knowledge_card_expansion_play
---

# Eval Metric: Commercial KPI Framework

## Purpose

Defines the canonical commercial metrics N06 tracks, their formulas, targets, and evaluation cadence. Every commercial decision, experiment, and self-improvement loop cycle references this framework.

## Metric Taxonomy

### L1: North Star Metrics (Executive Level)

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| MRR (Monthly Recurring Revenue) | sum(active_subscription_amounts) | +10% MoM | Daily |
| ARR (Annual Recurring Revenue) | MRR * 12 | Milestone-based | Monthly |
| Net Revenue Retention (NRR) | (MRR_end - churn + expansion) / MRR_start * 100 | >110% | Monthly |
| Customer Count (paid) | count(active_paid_subscriptions) | +15% MoM | Daily |

### L2: Growth Health Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| New MRR | sum(new_subscription_MRR) | Positive trend | Weekly |
| Expansion MRR | sum(upgrade_MRR_additions) | >20% of new MRR | Weekly |
| Contraction MRR | sum(downgrade_MRR_reductions) | <5% of total MRR | Weekly |
| Churned MRR | sum(cancelled_subscription_MRR) | <2% of total MRR | Weekly |
| Gross Revenue Retention | 1 - (churned_MRR / MRR_start) | >90% | Monthly |

### L3: Unit Economics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Customer Acquisition Cost (CAC) | total_sales_marketing_spend / new_customers | <$150 blended | Monthly |
| Payback Period | CAC / (MRR_per_customer * gross_margin) | <6 months | Monthly |
| LTV (Lifetime Value) | ARPU / churn_rate | >$1,200 blended | Quarterly |
| LTV:CAC Ratio | LTV / CAC | >3x | Quarterly |
| Average Revenue Per User (ARPU) | MRR / active_customers | Tier-weighted | Monthly |

### L4: Funnel Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Trial signup rate | trial_starts / pricing_page_visits | >5% | Weekly |
| Trial-to-paid conversion | paid_conversions / trial_starts | >25% | Weekly |
| Free-to-starter conversion | starter_upgrades / free_accounts | >8% monthly | Monthly |
| Starter-to-pro conversion | pro_upgrades / starter_accounts | >15% over 90d | Monthly |
| Checkout completion | completed_checkouts / started_checkouts | >70% | Daily |
| Time to first build | median(first_build_ts - signup_ts) | <30 minutes | Weekly |

### L5: Retention Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Monthly customer churn | churned_customers / start_customers | <2% | Monthly |
| Monthly revenue churn | churned_MRR / total_MRR | <2% | Monthly |
| Average customer lifespan | 1 / monthly_churn_rate | >50 months target | Quarterly |
| Reactivation rate | reactivated_accounts / churned_previous_period | >10% | Monthly |
| Renewal rate | accounts_renewed / accounts_due | >85% | Monthly |

### L6: Revenue Mix and Quality

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Annual plan mix | annual_MRR / total_MRR | >45% | Monthly |
| Self-serve vs sales-assisted ratio | self_serve_MRR / sales_MRR | >70% self-serve | Monthly |
| Referral revenue share | referred_customer_MRR / total_MRR | >20% | Monthly |
| NPS score | (promoters - detractors) / total * 100 | >50 | Quarterly |
| Health score distribution | avg and P25/P50/P75 of health_scores | P50 > 65 | Weekly |

## Metric Definitions (Precise)

```python
# MRR -- only ACTIVE subscriptions, excludes trials, paused, past_due
MRR = sum(
    subscription.items.data[0].price.unit_amount / 100  # if monthly
    OR subscription.items.data[0].price.unit_amount / 100 / 12  # if annual
    for subscription in stripe.subscriptions.list(status="active")
)

# NRR -- measures revenue retention quality, expansion included
NRR_pct = (
    (MRR_start - churned_MRR + expansion_MRR - contraction_MRR)
    / MRR_start * 100
)

# LTV -- simple average lifespan model
LTV = ARPU / (monthly_churn_rate / 100)

# CAC -- all growth-related costs divided by new customers
CAC = (marketing_spend + sales_spend + csm_onboarding_cost) / new_paid_customers
```

## Metric Evaluation Schedule

```
Daily: MRR, new customers, churn events, checkout completion, payment failures
Weekly: funnel metrics (signup->trial->paid), health score distribution, expansion MRR
Monthly: full unit economics, NRR, cohort retention, channel CAC, ARPU by tier
Quarterly: LTV:CAC, pricing review, ICP recalibration, N06 portfolio gap scan
```

## Alert Thresholds

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Monthly churn | >3% | >5% | Activate churn_prevention_playbook immediately |
| Checkout completion | <60% | <50% | Audit checkout flow for friction/bugs |
| Trial-to-paid | <20% | <15% | Audit onboarding + activation sequence |
| MRR growth MoM | <5% | Negative | Revenue review with full funnel audit |
| NRR | <100% | <90% | Retention emergency -- fix before acquisition |

## Dashboard Structure

```
Section 1: Health at a Glance (MRR, NRR, Active Customers, Churn Rate)
Section 2: Funnel (Signups -> Trial -> Paid -> Retained)
Section 3: Expansion (Upgrade rate, Annual conversion, Expansion MRR)
Section 4: Unit Economics (CAC, LTV, LTV:CAC, Payback Period)
Section 5: Cohort Analysis (link to cohort_analysis_n06.md)
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_roi_content_factory]] | downstream | 0.28 |
| [[n06_monetization_audit_2026_04_08]] | upstream | 0.25 |
| [[p08_pat_pricing_framework]] | downstream | 0.24 |
| [[bld_knowledge_card_subscription_tier]] | upstream | 0.23 |
| [[p08_pat_funnel_architecture]] | downstream | 0.22 |
| [[bld_memory_subscription_tier]] | downstream | 0.21 |
| [[pricing_optimization_memory]] | downstream | 0.21 |
| [[p02_ax_commercial_nucleus]] | upstream | 0.20 |
| [[leverage_map_v2_n06_verification]] | upstream | 0.20 |
| [[bld_knowledge_card_expansion_play]] | upstream | 0.18 |
