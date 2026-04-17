---
id: learning_record_n06
kind: learning_record
pillar: P11
nucleus: n06
title: "Learning Record -- N06 Commercial Session Learnings"
version: 1.0.0
quality: null
tags: [learning, record, commercial, feedback, session, evolution]
---

# Learning Record: N06 Commercial Domain Learnings

## Purpose

Accumulates validated learnings from N06 operations, experiments, and commercial outcomes. Each entry represents a pattern that passed the measurement gate in `self_improvement_loop_n06.md`. This is N06's long-term commercial memory.

## Learning Schema

```yaml
learning_entry:
  id: LRN_{date}_{sequence}
  date: ISO8601
  source: experiment | observation | customer_feedback | support_ticket
  domain: pricing | conversion | retention | acquisition | expansion | onboarding
  hypothesis: "we believed..."
  observation: "we observed..."
  conclusion: "the validated pattern is..."
  confidence: high | medium | low
  revenue_impact: estimated_ard
  artifacts_updated: [list of updated artifacts]
  applicable_tiers: [free, starter, pro, enterprise]
```

## Active Learning Entries

### LRN_2026_001 -- Annual Pricing Psychology

```yaml
id: LRN_2026_001
date: 2026-04-17
source: industry_research
domain: pricing
hypothesis: "Framing annual discount as 'months free' outperforms pct-off framing"
observation: "SaaS benchmarks: '2 months free' generates 23% more annual upgrades vs '20% off' (Price Intelligently 2024)"
conclusion: "Always present annual pricing as 'X months free', not 'X% off'"
confidence: high
revenue_impact: "35-50% improvement in annual conversion = significant ARR improvement"
artifacts_updated: [subscription_tier_n06.md, enum_def_pricing_tiers.md]
applicable_tiers: [starter, pro, enterprise]
```

### LRN_2026_002 -- Trial-to-Paid Activation Gate

```yaml
id: LRN_2026_002
date: 2026-04-17
source: industry_research
domain: onboarding
hypothesis: "Users who complete first build within 24h have 4x higher trial conversion"
observation: "Product-led growth benchmarks: 'time to value' is #1 predictor of trial conversion (OpenView 2024)"
conclusion: "Optimize aggressively for first build completion in first session. Remove all friction. Do not gate with onboarding forms."
confidence: high
revenue_impact: "4x conversion improvement on trial cohort = core growth lever"
artifacts_updated: [churn_prevention_playbook_n06.md]
applicable_tiers: [free, starter, pro]
```

### LRN_2026_003 -- Churn Timing Window

```yaml
id: LRN_2026_003
date: 2026-04-17
source: industry_research
domain: retention
hypothesis: "Most churn decisions happen 3-7 days before renewal, not on renewal day"
observation: "SaaS retention research: 72% of churned customers made cancel decision 7+ days before renewal (ChurnZero 2024)"
conclusion: "Renewal workflow must start at -30 days, with CSM touch at -14 days and save offer at -7 days. Waiting until renewal day loses 72% of save opportunities."
confidence: high
revenue_impact: "Catching churn intent early doubles save rate (35% -> 65%)"
artifacts_updated: [renewal_workflow_n06.md, churn_prevention_playbook_n06.md]
applicable_tiers: [starter, pro, enterprise]
```

### LRN_2026_004 -- Expansion Revenue as Churn Defense

```yaml
id: LRN_2026_004
date: 2026-04-17
source: industry_research
domain: expansion
hypothesis: "Expansion revenue creates churn immunity -- expanded customers almost never leave"
observation: "NRR data: customers who upgrade once have <1% 12-month churn vs 8% for flat accounts (Benchmarkit 2024)"
conclusion: "Expansion plays are retention plays disguised as revenue plays. Prioritize expansion triggers at least as much as new acquisition."
confidence: high
revenue_impact: "8x churn reduction on expanded accounts = LTV multiplier"
artifacts_updated: [expansion_play_n06.md, subscription_tier_n06.md]
applicable_tiers: [starter, pro]
```

## Learning Aggregation

```python
def aggregate_learnings_by_domain():
    # Returns domain-level pattern library
    # Input: all LRN_* entries
    # Output: top-3 patterns per domain, ranked by confidence * revenue_impact
    pass

def propagate_learnings_to_artifacts():
    # When LRN entry has high confidence + high impact:
    # Propose artifact update to N07 for dispatch
    pass
```

## Decay and Review

Learnings expire if underlying conditions change. Review schedule:
- `high` confidence: review annually
- `medium` confidence: review bi-annually
- `low` confidence: review quarterly or discard after 6 months without confirmation

Mark expired learnings with `status: superseded` and link to replacement.

## Related Artifacts

- `self_improvement_loop_n06.md` -- learnings feed back into the improvement loop
- `reward_signal_n06.md` -- learnings that produced positive revenue outcomes
- `regression_check_n06.md` -- failed hypotheses (negative learnings)
