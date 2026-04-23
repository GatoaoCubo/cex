---
id: pricing_experiment_tool
kind: tool_card
pillar: P11
title: "Pricing Experiment Tool — A/B Testing Framework"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: pricing_experiments
quality: 9.0
tags: [tool, pricing, experiment, A/B, N06, testing]
tldr: "Structured experiment design for pricing changes: hypothesis → test → measure → decide. Prevents gut-feel pricing adjustments."
density_score: 0.90
related:
  - p08_pat_pricing_framework
  - pricing_optimization_memory
  - p01_kc_ab_testing_content_optimization
  - experiment-config-builder
  - bld_collaboration_experiment_config
  - ab-test-config-builder
  - p03_sp_experiment_config_builder
  - bld_schema_experiment_config
  - p01_kc_experiment_driven_development
  - bld_knowledge_card_experiment_config
---

# Pricing Experiment Tool

## Purpose

Pricing changes without measurement are gambling. This tool defines a structured experiment protocol so every pricing adjustment is hypothesis-driven, measured, and recorded.

**ROI**: One well-run pricing experiment that finds a 10% revenue improvement pays for itself in the first month. One gut-feel change that drops conversion by 15% costs months to recover.

---

## Experiment Protocol

### Step 1: Define Hypothesis

```yaml
experiment:
  id: "PX-YYYY-MM-DD-NNN"
  product: "product_name"
  hypothesis: "Changing [variable] from [A] to [B] will [metric] by [expected %]"
  variable: "price | tier_features | billing_cycle | trial_length | discount"
  metric: "conversion_rate | revenue_per_visitor | arpu | trial_to_paid"
  expected_lift: "+X%"
  risk: "What could go wrong?"
  rollback_plan: "How to undo if it fails"
```

### Step 2: Design Test

```yaml
test_design:
  type: "A/B | sequential | cohort"
  
  # A/B test (sufficient traffic: >1000 visitors/variant)
  ab_test:
    variant_a: "control — current pricing"
    variant_b: "test — proposed change"
    traffic_split: "50/50"
    min_sample_size: 1000  # per variant for 95% confidence
    duration_days: 14  # minimum 2 weeks to capture weekly patterns
    
  # Sequential test (low traffic: <1000/week)
  sequential_test:
    week_1: "price_high — measure conversion"
    week_2: "price_mid — measure conversion"
    week_3: "price_low — measure conversion"
    analysis: "revenue_optimizing_price = argmax(price × conversion)"
    
  # Cohort test (existing customers)
  cohort_test:
    group_a: "existing customers — no change"
    group_b: "new customers — new pricing"
    duration: "30 days"
    metric: "LTV comparison at day 30, 60, 90"
```

### Step 3: Run & Measure

```yaml
measurement:
  primary_metric: "revenue_per_visitor"  # not just conversion!
  secondary_metrics:
    - conversion_rate
    - average_order_value
    - churn_rate_delta
    - customer_satisfaction  # if measurable
  
  data_sources:
    - "Stripe MCP: payment data"
    - "Analytics: visitor counts, funnel progression"
    - "Support: complaint volume"
  
  statistical_rigor:
    confidence_level: 0.95
    min_effect_size: 0.05  # 5% minimum detectable effect
    power: 0.80
```

### Step 4: Decide

```yaml
decision_matrix:
  strong_positive:  # lift > expected, p < 0.05
    action: "adopt variant B"
    next: "log to pricing_optimization_memory.md"
    
  weak_positive:  # lift > 0 but p > 0.05
    action: "extend test duration or increase sample"
    next: "re-evaluate in 1 week"
    
  neutral:  # no significant difference
    action: "keep current (avoid change cost)"
    next: "log insight, try different variable"
    
  negative:  # variant B worse
    action: "revert immediately"
    next: "analyze why, update anti-pattern list"
```

### Step 5: Record

Every completed experiment → append to `pricing_optimization_memory.md`:

```yaml
result:
  experiment_id: "PX-YYYY-MM-DD-NNN"
  outcome: "positive | neutral | negative"
  variant_a_metric: 0.0
  variant_b_metric: 0.0
  lift_pct: 0.0
  confidence: 0.0
  decision: "adopt | extend | keep_current | revert"
  learning: "What we learned for future experiments"
  date_completed: "YYYY-MM-DD"
```

---

## Experiment Types by Variable

| Variable | Test Type | Duration | GDP? |
|----------|----------|----------|------|
| Base price change | A/B or sequential | 14-28 days | Yes |
| Adding/removing tier | Sequential | 30 days | Yes |
| Annual discount % | A/B | 14 days | No |
| Trial length (7→14 days) | Cohort | 60 days | No |
| Feature gating changes | A/B | 14 days | Yes |
| Checkout flow optimization | A/B | 7-14 days | No |
| Payment options (add crypto, etc.) | A/B | 14 days | Yes |

---

## Common Experiments to Run First

### Experiment 1: Price Sensitivity
**Hypothesis**: Current price is within 20% of optimal.
**Method**: Sequential test at -20%, current, +20%.
**Metric**: Revenue per visitor (not just conversion).
**Expected duration**: 3 weeks.

### Experiment 2: Annual Discount Impact
**Hypothesis**: Offering 20% annual discount increases annual plan adoption.
**Method**: A/B (show/hide annual toggle).
**Metric**: Annual plan adoption rate, 12-month revenue projection.
**Expected duration**: 2 weeks.

### Experiment 3: Free Tier Conversion Gate
**Hypothesis**: Moving feature X behind paywall increases free→pro conversion.
**Method**: A/B (feature available vs. gated).
**Metric**: Free→pro upgrade rate, churn impact.
**Expected duration**: 30 days.

---

## Integration

| CEX Component | Role |
|---------------|------|
| `pricing_optimization_memory.md` | Stores all experiment results |
| Stripe MCP | Pulls revenue/subscription data |
| `cex_evolve.py` | Can auto-evolve pricing page copy between experiments |
| `brand_audit.py` | Verifies pricing changes align with brand positioning |
| `scoring_rubric_commercial.md` | Quality gate for experiment design |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_pricing_framework]] | upstream | 0.36 |
| [[pricing_optimization_memory]] | upstream | 0.35 |
| [[p01_kc_ab_testing_content_optimization]] | upstream | 0.29 |
| [[experiment-config-builder]] | upstream | 0.28 |
| [[bld_collaboration_experiment_config]] | downstream | 0.28 |
| [[ab-test-config-builder]] | related | 0.28 |
| [[p03_sp_experiment_config_builder]] | upstream | 0.26 |
| [[bld_schema_experiment_config]] | upstream | 0.24 |
| [[p01_kc_experiment_driven_development]] | upstream | 0.24 |
| [[bld_knowledge_card_experiment_config]] | upstream | 0.23 |
