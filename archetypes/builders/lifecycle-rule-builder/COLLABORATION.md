```yaml
---
pillar: P12
llm_function: COLLABORATE
purpose: How lifecycle-rule-builder works in crews
---
```

# Collaboration: lifecycle-rule-builder

## My Role
I define WHEN artifacts change state and WHO decides. I do not implement the transition logic (hook-builder [PLANNED]).
I do not measure quality at a point in time (quality-gate-builder).
I GOVERN artifact freshness so consumers always trust what they read.

## Crew: "Full Governance for New Type"
```
  1. quality-gate-builder      -> defines HARD/SOFT gates for artifact quality
  2. lifecycle-rule-builder    -> defines freshness policy and state transitions
  3. guardrail-builder         -> defines safety boundaries
```

## Crew: "Content Maintenance Pipeline"
```
  1. lifecycle-rule-builder    -> defines when KCs/model_cards go stale
  2. hook-builder [PLANNED]    -> implements cron jobs for staleness detection
  3. signal-builder [PLANNED]  -> defines staleness notification signals
```

## Handoff Protocol
### I Receive
- seeds: scope (what artifact kind), domain, freshness hint
- optional: existing quality_gate, domain volatility data, usage metrics

### I Produce
- lifecycle_rule artifact in P11_feedback/examples/
- committed to: cex/P11_feedback/examples/p11_lc_{rule_slug}.yaml

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- quality-gate-builder: provides quality thresholds that inform entry states

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder [PLANNED] | Implements automated transitions defined by lifecycle_rule |
| optimizer-builder [PLANNED] | Uses freshness metrics as optimization targets |
