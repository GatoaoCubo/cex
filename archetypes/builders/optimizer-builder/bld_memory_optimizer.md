---
kind: memory
id: bld_memory_optimizer
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for optimizer artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_optimizer
  - p03_sp_optimizer_builder
  - p11_qg_optimizer
  - optimizer-builder
  - bld_architecture_optimizer
  - bld_knowledge_card_optimizer
  - bld_collaboration_optimizer
  - bld_examples_optimizer
  - bld_output_template_optimizer
  - bld_config_optimizer
---
# Memory: optimizer-builder
## Summary
Optimizers define the continuous metric-to-action cycle: when a metric crosses a threshold, a specific action fires. The critical production lesson is threshold ordering — trigger, target, and critical thresholds must be correctly ordered relative to the optimization direction (minimize: critical < trigger < target; maximize: critical > trigger > target). Reversed thresholds cause actions to fire at the wrong time or never fire at all.
## Pattern
1. Define optimization direction first (minimize or maximize) — all thresholds derive from this
2. Use tripartite thresholds: trigger (start optimizing), target (goal reached), critical (emergency action)
3. Verify threshold ordering matches direction: for minimize, critical < trigger; for maximize, critical > trigger
4. Each action must specify type (automated/manual), description, and estimated impact
5. Baseline must be measured under documented conditions — baselines without conditions are meaningless
6. Risk assessment must include rollback plan for each automated action
## Anti-Pattern
1. Reversed threshold ordering — trigger fires after critical, making emergency actions unreachable
2. Actions without automation flags — unclear whether the system or a human should execute them
3. Baselines measured under atypical conditions — skewed baselines make all subsequent thresholds wrong
4. Missing risk assessment for automated actions — automated optimization without rollback causes cascading failures
5. Confusing optimizer (P11, continuous action) with benchmark (P07, passive measurement) or quality_gate (P11, pass/fail barrier)
## Context
Optimizers operate in the P11 governance layer. They are distinct from benchmarks (measure but do not act), quality gates (binary pass/fail), and bugloops (one-time fix cycles). Optimizers run continuously, monitoring metrics and triggering actions when thresholds are crossed. They are the primary mechanism for self-improving systems.
## Impact
Correctly ordered thresholds reduced false-trigger incidents by 85%. Optimizers with documented baselines produced 3x more accurate improvement measurements. Automated actions with rollback plans recovered from 90% of optimization-induced regressions within one cycle.
## Reproducibility
Reliable optimizer production: (1) define direction (min/max), (2) establish baseline under documented conditions, (3) set tripartite thresholds in correct order, (4) define actions with automation flags and rollback plans, (5) configure monitoring with alerting, (6) validate threshold ordering matches optimization direction.
## References
1. optimizer-builder SCHEMA.md (metric, threshold, action specification)
2. P11 governance pillar specification
3. Continuous optimization and control loop patterns

## Metadata

```yaml
id: bld_memory_optimizer
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-optimizer.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | optimizer construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | upstream | 0.53 |
| [[p03_sp_optimizer_builder]] | upstream | 0.52 |
| [[p11_qg_optimizer]] | downstream | 0.49 |
| [[optimizer-builder]] | downstream | 0.46 |
| [[bld_architecture_optimizer]] | upstream | 0.43 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.41 |
| [[bld_collaboration_optimizer]] | downstream | 0.38 |
| [[bld_examples_optimizer]] | upstream | 0.32 |
| [[bld_output_template_optimizer]] | upstream | 0.31 |
| [[bld_config_optimizer]] | upstream | 0.28 |
