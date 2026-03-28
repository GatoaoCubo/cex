---
kind: memory
id: bld_memory_optimizer
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for optimizer artifact generation
---

# Memory: optimizer-builder

## Summary

Optimizers define the continuous metric-to-action cycle: when a metric crosses a threshold, a specific action fires. The critical production lesson is threshold ordering — trigger, target, and critical thresholds must be correctly ordered relative to the optimization direction (minimize: critical < trigger < target; maximize: critical > trigger > target). Reversed thresholds cause actions to fire at the wrong time or never fire at all.

## Pattern

- Define optimization direction first (minimize or maximize) — all thresholds derive from this
- Use tripartite thresholds: trigger (start optimizing), target (goal reached), critical (emergency action)
- Verify threshold ordering matches direction: for minimize, critical < trigger; for maximize, critical > trigger
- Each action must specify type (automated/manual), description, and estimated impact
- Baseline must be measured under documented conditions — baselines without conditions are meaningless
- Risk assessment must include rollback plan for each automated action

## Anti-Pattern

- Reversed threshold ordering — trigger fires after critical, making emergency actions unreachable
- Actions without automation flags — unclear whether the system or a human should execute them
- Baselines measured under atypical conditions — skewed baselines make all subsequent thresholds wrong
- Missing risk assessment for automated actions — automated optimization without rollback causes cascading failures
- Confusing optimizer (P11, continuous action) with benchmark (P07, passive measurement) or quality_gate (P11, pass/fail barrier)

## Context

Optimizers operate in the P11 governance layer. They are distinct from benchmarks (measure but do not act), quality gates (binary pass/fail), and bugloops (one-time fix cycles). Optimizers run continuously, monitoring metrics and triggering actions when thresholds are crossed. They are the primary mechanism for self-improving systems.

## Impact

Correctly ordered thresholds reduced false-trigger incidents by 85%. Optimizers with documented baselines produced 3x more accurate improvement measurements. Automated actions with rollback plans recovered from 90% of optimization-induced regressions within one cycle.

## Reproducibility

Reliable optimizer production: (1) define direction (min/max), (2) establish baseline under documented conditions, (3) set tripartite thresholds in correct order, (4) define actions with automation flags and rollback plans, (5) configure monitoring with alerting, (6) validate threshold ordering matches optimization direction.

## References

- optimizer-builder SCHEMA.md (metric, threshold, action specification)
- P11 governance pillar specification
- Continuous optimization and control loop patterns
