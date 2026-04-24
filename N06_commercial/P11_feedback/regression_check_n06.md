---
id: regression_check_n06
kind: regression_check
8f: F7_govern
pillar: P07
nucleus: n06
title: "Regression Check -- Revenue Strategy Anti-Patterns and Failed Hypotheses"
version: 1.0.0
quality: 8.9
tags: [regression, anti-pattern, commercial, revenue, failed-hypothesis]
density_score: 0.91
updated: "2026-04-17"
related:
  - p08_pat_pricing_framework
  - pricing_optimization_memory
  - pricing_experiment_tool
  - p02_ax_commercial_nucleus
  - n06_funnel_cex_product
  - kc_pricing_strategy
  - p11_qg_subscription_tier
  - n06_monetization_audit_2026_04_08
  - p01_kc_commercial_nucleus
  - n06_pricing_content_factory
---

# Regression Check: Revenue Strategy Anti-Patterns

## Purpose

Documents failed hypotheses and revenue anti-patterns so N06 never repeats them. Strategic Greed without memory repeats expensive mistakes. This is the "do NOT do this" registry.

## Anti-Pattern Schema

```yaml
regression_entry:
  id: REG_{date}_{sequence}
  date: ISO8601
  domain: pricing | conversion | retention | acquisition | expansion
  pattern: description of what was tried
  expected_result: what we thought would happen
  actual_result: what actually happened
  root_cause: why it failed
  cost: revenue lost or opportunity cost
  do_not: specific behavior to avoid
  correct_approach: what to do instead
  artifacts_affected: [list]
```

## Active Regression Entries

### REG_2026_001 -- Freemium Without Friction

```yaml
id: REG_2026_001
date: 2026-04-17
domain: pricing
pattern: "Remove all limits from FREE tier to maximize top-of-funnel"
expected_result: "More free users -> more eventual conversions"
actual_result: "Unlimited free tier kills conversion. 98% stay free indefinitely."
root_cause: "If FREE does the job, there is no reason to pay. Freemium only works when the paid feature is genuinely necessary for the user's primary workflow."
cost: "Lost conversion revenue; high infrastructure cost from free users"
do_not: "Remove limits from FREE tier to compete on freemium. Do not make FREE 'good enough.'"
correct_approach: "FREE must create desire AND hit a hard wall at the exact moment of highest value delivery. 10 builds limit is correct -- user sees value, then hits the wall."
artifacts_affected: [enum_def_pricing_tiers.md, subscription_tier_n06.md]
```

### REG_2026_002 -- Premature Annual Push

```yaml
id: REG_2026_002
date: 2026-04-17
domain: pricing
pattern: "Push annual upgrade in first checkout session before user has activated"
expected_result: "Capture annual revenue immediately, reduce churn"
actual_result: "Annual-first increases checkout abandonment 35%. Users distrust annual commitment before experiencing value."
root_cause: "Trust must precede commitment. Annual = high trust requirement. Monthly = low trust. Push annual after activation milestone (3+ builds), not at first checkout."
cost: "35% fewer completions on checkout sessions that led with annual"
do_not: "Default to annual on first checkout. Do not lead with annual on pricing page hero."
correct_approach: "Default to monthly on first purchase. Surface annual as the obvious choice after activation: 'You've built X times this month -- switch to annual and save $Y.'"
artifacts_affected: [subscription_tier_n06.md]
```

### REG_2026_003 -- Discount as Default Retention

```yaml
id: REG_2026_003
date: 2026-04-17
domain: retention
pattern: "Auto-offer 30% discount to every customer who attempts to cancel"
expected_result: "High save rate from price-sensitive churners"
actual_result: "Trains customers to threaten cancel to get discount. Destroys pricing integrity. Creates entitlement cycle."
root_cause: "Discounting on cancel intent selects for price-motivated customers. These customers are the lowest-LTV segment. Saving them at 70% price only delays the inevitable while training behavior."
cost: "Margin erosion; normalized cancel-to-discount cycle; devalues product"
do_not: "Auto-discount on cancel. Do not make discount the first save play."
correct_approach: "Lead with value play (onboarding, use case reminder). Offer pause before discount. Reserve discount for genuinely price-blocked customers where no other play worked."
artifacts_affected: [churn_prevention_playbook_n06.md]
```

### REG_2026_004 -- Feature Parity as Competitive Strategy

```yaml
id: REG_2026_004
date: 2026-04-17
domain: acquisition
pattern: "Match every competitor feature to eliminate objections"
expected_result: "Fewer lost deals due to feature gaps"
actual_result: "Feature parity commoditizes the product. Race-to-feature-parity has no end. Customers make commodity purchases on price, not value."
root_cause: "Feature parity erodes differentiation. If CEX has the same features as competitors, the only differentiator is price -- a war we lose to funded competitors."
do_not: "Roadmap based on competitor feature matching. Do not respond to 'competitor has X' with 'add X to CEX.'"
correct_approach: "Double down on unique CEX capabilities (8F pipeline, sin-lens nuclei, 257 kinds, typed knowledge). Win on what competitors cannot replicate, not on what they already have."
artifacts_affected: [sales_playbook_n06.md, discovery_questions_n06.md]
```

## Quality Gates for Regressions

Before executing any pricing, conversion, or retention change, N06 runs:

```python
def regression_check(proposed_action: str) -> list[str]:
    """Returns list of matching regression anti-patterns."""
    warnings = []
    for reg in REGRESSION_REGISTRY:
        if pattern_matches(proposed_action, reg["do_not"]):
            warnings.append(f"REG WARNING {reg['id']}: {reg['do_not']}")
    return warnings
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_pricing_framework]] | downstream | 0.37 |
| [[pricing_optimization_memory]] | downstream | 0.35 |
| [[pricing_experiment_tool]] | downstream | 0.26 |
| [[p02_ax_commercial_nucleus]] | upstream | 0.26 |
| [[n06_funnel_cex_product]] | downstream | 0.24 |
| [[kc_pricing_strategy]] | upstream | 0.24 |
| [[p11_qg_subscription_tier]] | downstream | 0.22 |
| [[n06_monetization_audit_2026_04_08]] | upstream | 0.22 |
| [[p01_kc_commercial_nucleus]] | upstream | 0.21 |
| [[n06_pricing_content_factory]] | downstream | 0.20 |
