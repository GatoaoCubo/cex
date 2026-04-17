---
id: self_improvement_loop_n06
kind: self_improvement_loop
pillar: P11
nucleus: n06
title: "Self-Improvement Loop -- N06 Autonomous Revenue Strategy Evolution"
version: 1.0.0
quality: null
tags: [self-improvement, evolution, feedback, autonomous, commercial, revenue]
---

# Self-Improvement Loop: N06 Autonomous Revenue Strategy Evolution

## Purpose

N06's commercial portfolio must evolve faster than the market. This artifact defines the autonomous loop by which N06 scans revenue performance, identifies strategy gaps, generates improvement hypotheses, tests them, and integrates validated improvements back into its artifact portfolio.

## Loop Architecture

```
SCAN (weekly)
  |
  v
DIAGNOSE (identify gaps vs targets)
  |
  v
HYPOTHESIZE (generate improvement candidates)
  |
  v
RANK (by expected revenue impact / effort)
  |
  v
DISPATCH (to N06 or N02/N01 via N07)
  |
  v
MEASURE (A/B test or before/after)
  |
  v
INTEGRATE (update artifacts) or DISCARD (log as failed hypothesis)
  |
  v
SCAN (next cycle)
```

## SCAN: Metrics to Monitor

```yaml
revenue_signals:
  core_metrics:
    - mrr_growth_pct_mom           # target: >10%
    - churn_rate_pct               # target: <2%
    - net_revenue_retention_pct    # target: >110%
    - trial_to_paid_conversion_pct # target: >25%
    - cac_by_channel               # target: <90 days payback
    - expansion_revenue_pct        # target: >20% of new MRR
  
  funnel_signals:
    - pricing_page_ctr_to_checkout # target: >8%
    - checkout_completion_rate     # target: >70%
    - free_to_starter_activation   # target: >8%
    - starter_to_pro_upgrade_rate  # target: >15%
    
  engagement_signals:
    - builds_per_active_user_week  # target: >5
    - feature_adoption_breadth     # target: >3 features used
    - time_to_first_build_minutes  # target: <30 min
    - nps_score                    # target: >50
```

## DIAGNOSE: Gap Detection Rules

```python
def diagnose_gaps(metrics: dict) -> list[str]:
    gaps = []
    
    if metrics["churn_rate_pct"] > 3.0:
        gaps.append("HIGH_CHURN: run churn_prevention_playbook analysis")
    
    if metrics["trial_to_paid_conversion_pct"] < 20.0:
        gaps.append("LOW_CONVERSION: audit onboarding + value delivery in trial")
    
    if metrics["net_revenue_retention_pct"] < 100.0:
        gaps.append("NEGATIVE_NRR: expansion < churn, fix retention before acquisition")
    
    if metrics["expansion_revenue_pct"] < 15.0:
        gaps.append("LOW_EXPANSION: expansion_play underperforming, audit upgrade triggers")
    
    if metrics["checkout_completion_rate"] < 60.0:
        gaps.append("CHECKOUT_ABANDONMENT: pricing friction or UX issue")
    
    if metrics["time_to_first_build_minutes"] > 60:
        gaps.append("SLOW_ONBOARDING: high activation friction, users churning before value")
    
    return gaps
```

## HYPOTHESIZE: Improvement Playbook

| Gap | Hypothesis | Artifact to Update | Test Type |
|-----|-----------|-------------------|-----------|
| HIGH_CHURN | Proactive CSM outreach at day 30 reduces churn 20% | churn_prevention_playbook_n06 | A/B |
| LOW_CONVERSION | Adding ROI calculator to pricing page increases conversion 15% | pricing_page + roi_calculator | A/B |
| LOW_EXPANSION | In-app usage bar at 80% quota increases upgrades 30% | expansion_play_n06 | A/B |
| CHECKOUT_ABANDONMENT | Removing credit card for trial increases trial starts 40% | input_schema_checkout | A/B |
| SLOW_ONBOARDING | Interactive walkthrough reduces time-to-first-build by 50% | onboarding_flow (N05) | Before/After |
| NEGATIVE_NRR | Pause option reduces cancellations 25% vs hard cancel | churn_prevention_playbook | A/B |

## RANK: Prioritization Matrix

Score each hypothesis: `(revenue_impact * probability_of_success) / effort`

```
HIGH impact: >$10K ARR potential per month
MED impact: $1K-$10K ARR potential per month
LOW impact: <$1K ARR potential per month

HIGH probability: historical evidence or industry data
MED probability: logical but untested
LOW probability: speculative

HIGH effort: >40 engineer hours
MED effort: 8-40 engineer hours
LOW effort: <8 engineer hours

Priority = (impact_score * probability_score) / effort_score
Run highest priority first.
```

## MEASURE: Success Criteria

```yaml
experiment_success_criteria:
  minimum_sample_size: 100_per_arm
  minimum_duration_days: 14
  statistical_significance: 95_pct
  primary_metric: conversion_rate_or_churn_rate
  guardrail_metrics:
    - revenue_per_user_must_not_decrease
    - nps_must_not_decrease_by_5_points
```

## INTEGRATE: Artifact Update Protocol

When hypothesis validated:
1. Update the relevant N06 artifact (e.g., `churn_prevention_playbook_n06.md`)
2. Update `eval_metric_commercial.md` with new baseline
3. Add to `reward_signal_n06.md` as validated pattern
4. Log to `.cex/experiments/results.tsv` with: `date | hypothesis | metric | result | artifact_updated`
5. If pattern is generalizable: propose to N07 for cross-nucleus adoption

When hypothesis fails:
1. Log to `regression_check_n06.md` as failed pattern
2. Document WHY it failed (counter-intuitive learning is high value)
3. Keep experiment data for future meta-analysis

## Loop Cadence

```
Weekly: SCAN + DIAGNOSE (automated, N06 reads metrics + runs diagnose_gaps())
Bi-weekly: HYPOTHESIZE + RANK (N06 proposes top-3 experiments to N07)
Monthly: INTEGRATE / DISCARD (review running experiments, integrate winners)
Quarterly: Strategic portfolio review (which artifacts need full rebuild vs patch)
```

## Related Artifacts

- `eval_metric_commercial.md` -- metrics data source for SCAN
- `cohort_analysis_n06.md` -- cohort segmentation for DIAGNOSE
- `reward_signal_n06.md` -- validated patterns library
- `regression_check_n06.md` -- failed patterns library
- `churn_prevention_playbook_n06.md` -- primary improvement target
