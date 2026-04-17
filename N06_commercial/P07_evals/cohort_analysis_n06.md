---
id: cohort_analysis_n06
kind: cohort_analysis
pillar: P07
nucleus: n06
title: "Cohort Analysis -- Revenue Cohort Framework by Channel, Plan, and Period"
version: 1.0.0
quality: 9.0
tags: [cohort, analysis, revenue, retention, commercial, channel, plan]
density_score: 1.0
updated: "2026-04-17"
---

# Cohort Analysis: Revenue Cohort Framework

## Purpose

Segments customer behavior by acquisition cohort to understand true retention, expansion, and LTV by channel, plan, and signup month. Cohort analysis reveals what aggregate churn rates hide: which customers are thriving, which are churning, and why.

## Cohort Dimensions

### Primary Cohort: Acquisition Month

```
Group customers by: month of first paid subscription
Track for: 12 months post-acquisition

Why: reveals true retention curve per vintage.
Insight: if January cohort retains better than August cohort,
the product change or acquisition channel shift between those months is the cause.
```

### Segmentation Dimensions

| Dimension | Values | Insight |
|-----------|--------|---------|
| Acquisition channel | organic, paid, referral, outbound, event | Which channels deliver highest-LTV customers |
| Starting plan | starter, pro, enterprise | Which tier has best retention and expansion |
| ICP score bucket | 0-33 (low), 34-66 (med), 67-100 (high) | Confirms ICP qualification value |
| Company size | 1, 2-10, 11-50, 51-200, 200+ | Best-fit company size |
| Industry | edtech, fintech, agency, saas, other | Vertical with best unit economics |
| Trial vs no trial | trial | annual | Does trial experience predict retention |

## Cohort Matrix Structure

### Retention Cohort Table

```
         Month 0  Month 1  Month 2  Month 3  Month 6  Month 12
Jan 2026:  100%     85%      78%      72%      65%      58%
Feb 2026:  100%     88%      82%      77%      [live]   [future]
Mar 2026:  100%     91%      [live]   [future]
Apr 2026:  100%     [live]
```

Target retention curve (benchmark SaaS):
- Month 1: >80%
- Month 3: >70%
- Month 6: >60%
- Month 12: >50%

### Revenue Cohort Table (NRR by vintage)

```
         Month 0   Month 3   Month 6   Month 12
Jan 2026:  100%     105%      112%      118%   <- expansion > churn (healthy)
Feb 2026:  100%     98%       95%       [live] <- contraction > expansion (warning)
```

NRR > 100% at Month 12 means the cohort is growing net revenue despite some churn.
Target: NRR > 110% at Month 12 for each cohort.

## Cohort Analysis Queries

### By Acquisition Channel

```sql
SELECT
    acquisition_channel,
    DATE_TRUNC('month', created_at) AS cohort_month,
    COUNT(*) AS cohort_size,
    AVG(lifetime_revenue_cents) / 100 AS avg_ltv_usd,
    AVG(DATEDIFF(day, created_at, churned_at)) AS avg_lifespan_days,
    SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS current_retention_pct
FROM customers
GROUP BY acquisition_channel, cohort_month
ORDER BY cohort_month DESC, avg_ltv_usd DESC;
```

### By Starting Plan

```sql
SELECT
    starting_plan_tier,
    COUNT(*) AS cohort_size,
    AVG(months_to_upgrade) AS avg_months_to_upgrade,
    SUM(CASE WHEN ever_upgraded THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS upgrade_rate_pct,
    AVG(lifetime_revenue_cents) / 100 AS avg_ltv_usd
FROM customer_cohorts
GROUP BY starting_plan_tier;
```

### Referral vs Organic Comparison

```sql
SELECT
    CASE WHEN referral_code_used IS NOT NULL THEN 'referral' ELSE 'organic' END AS source_type,
    AVG(monthly_churn_rate) AS avg_churn_rate,
    AVG(time_to_first_build_minutes) AS avg_ttfb,
    AVG(lifetime_revenue_cents) / 100 AS avg_ltv,
    AVG(health_score) AS avg_health_score
FROM customers
GROUP BY source_type;
```

## Key Hypotheses to Test

| Hypothesis | Measurement | Action if True |
|-----------|-------------|---------------|
| Referral customers retain 20% better | 12m retention by source | Increase referral spend; double K-factor target |
| Annual plan customers churn 50% less | Survival curves by billing_cycle | More aggressively push annual at checkout |
| ICP score predicts 12m LTV | Correlation: icp_score vs 12m revenue | Tighten ICP qualification; exclude low-score leads |
| Faster activation -> better retention | Corr: time_to_first_build vs 6m retention | Prioritize onboarding optimization |
| PRO users who use 3+ nuclei don't churn | Churn rate by feature_breadth | Invest in feature onboarding per persona |

## Reporting Cadence

```
Monthly: full cohort matrix refresh + channel comparison
Quarterly: deep dive on oldest cohorts (6m, 12m milestone)
  - Which cohorts are outperforming?
  - What changed in acquisition or product for those cohorts?
  - Where is the bottom of the retention curve?
Ad hoc: after major pricing change, new feature launch, or acquisition channel change
```

## Cohort Health Signals

```python
def flag_cohort_health(cohort: dict) -> list[str]:
    flags = []
    
    if cohort["month_1_retention"] < 0.75:
        flags.append("ACTIVATION_PROBLEM: early churn suggests onboarding failure")
    
    if cohort["month_3_nrr"] < 100:
        flags.append("EXPANSION_GAP: expansion < churn in first 90 days")
    
    if cohort["avg_ltv"] < cohort["avg_cac"] * 3:
        flags.append("UNIT_ECONOMICS_RISK: LTV:CAC below 3x for this cohort")
    
    if cohort["referral_rate"] < 0.10:
        flags.append("LOW_VIRALITY: cohort not generating referrals, check NPS")
    
    return flags
```

## Related Artifacts

- `eval_metric_commercial.md` -- aggregate metrics that cohort analysis decomposes
- `self_improvement_loop_n06.md` -- cohort insights generate improvement hypotheses
- `entity_memory_customer.md` -- customer entity stores cohort identifiers
- `referral_program_n06.md` -- cohort analysis validates referral program ROI
