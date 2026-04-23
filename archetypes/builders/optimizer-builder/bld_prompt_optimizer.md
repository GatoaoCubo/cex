---
id: p03_ins_optimizer
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Optimizer Builder Instructions
target: optimizer-builder agent
phases_count: 3
prerequisites:
  - The process or system to be optimized is named and described
  - At least one measurable metric is identified (latency, error rate, cost, throughput, etc.)
  - Optimization direction is known (minimize or maximize)
validation_method: checklist
domain: optimizer
quality: 9.2
tags:
  - instruction
  - optimizer
  - metric
  - P11
idempotent: true
atomic: false
rollback: "Delete the produced optimizer artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Research the target metric and baseline, compose tripartite thresholds and trigger-action pairs, validate ordering and risk, write optimizer artifact."
density_score: 0.87
llm_function: REASON
related:
  - p03_sp_optimizer_builder
  - bld_memory_optimizer
  - bld_knowledge_card_optimizer
  - p11_qg_optimizer
  - optimizer-builder
  - bld_collaboration_optimizer
  - bld_examples_optimizer
  - bld_architecture_optimizer
  - bld_output_template_optimizer
  - p01_kc_optimizer
---
## Context
The optimizer-builder receives a **process description** and produces an `optimizer` artifact encoding the metric-to-action cycle for continuous improvement of that process.
**Input variables**:
1. `{{process}}` — name and brief description of the process to optimize (e.g., "API response pipeline", "nightly batch job")
2. `{{metric}}` — the measurable quantity to optimize with unit (e.g., "p95 latency in ms", "error rate as %")
3. `{{direction}}` — `minimize` or `maximize`
4. `{{baseline}}` — optional current measured value under normal operating conditions; if absent, mark as `Configurable`
5. `{{constraints}}` — optional hard limits optimization must not violate (e.g., "cannot exceed $50/day")
**Output**: a single `optimizer` artifact at `p11_opt_{{process_slug}}.md` with tripartite thresholds, action catalog, baseline record, risk assessment, and monitoring config.
**Boundaries**: handles continuous optimization cycles only. Does NOT produce one-time bug fixes (bugloop), passive measurement records (benchmark), pass/fail barriers (quality_gate), or safety constraints (guardrail).
## Phases
### Phase 1: RESEARCH
**Goal**: Characterize the metric, establish baseline, and identify available actions.
1. Parse `{{metric}}`. Record: unit of measure, measurement point (where/when sampled), aggregation method (p50, p95, p99, average, rate).
2. Confirm `{{direction}}`. Apply the threshold ordering invariant:
   - **minimize**: trigger > target (worse than desired) > ... but critical is the worst. Order: `target < trigger < critical`.
   - **maximize**: target > trigger (below desired). Order: `target > trigger > critical`.
3. If `{{baseline}}` is provided, derive initial threshold estimates:
   - **minimize**: target = baseline, trigger = baseline × 1.10, critical = baseline × 1.50
   - **maximize**: target = baseline, trigger = baseline × 0.90, critical = baseline × 0.50
   If `{{baseline}}` is absent, set all three to `Configurable` and define the measurement procedure (tool, window duration, conditions to hold constant).
4. Document baseline conditions: date or measurement window, load level, environment, config version.
5. Identify 2–4 available actions: enumerate concrete operations that can move the metric toward `{{direction}}` (e.g., tune parameters, prune elements, scale capacity, replace component, restructure flow).
6. For each action, assess automation risk: can it fire without human approval? Set `automated: true` only if `risk.level = low` AND rollback is instant.
7. Search existing optimizers for this domain (brain_query [IF MCP]: `optimizer {{process}}`). Avoid duplicates; if found, determine whether an update is needed.
**Exit**: metric fully characterized, threshold values set (or Configurable with measurement procedure), at least 2 actions identified with automation flag.
### Phase 2: COMPOSE
**Goal**: Produce all artifact fields and body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.
8. Read SCHEMA.md — source of truth for all required fields.
9. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
10. Set `id = p11_opt_{{process_slug}}` where slug matches `^[a-z][a-z0-9_]+$`.
11. Set `kind = optimizer`, `pillar = P11`, `quality = null`.
12. Set `metric.name`, `metric.unit`, `metric.direction`.
13. Set thresholds using the ordering from Phase 1 step 2. All three values must be numeric (no subjective conditions).
14. Set `action.type` from enum: `[tune, prune, scale, replace, restructure]`.
15. Set `action.automated = true` only if `risk.level = low` AND rollback is instant (verified in step 6).
16. Set `frequency` based on how fast the metric changes: latency → continuous, cost → daily, batch throughput → per-run.
17. Write `## Target Process` section: scope, in-scope boundaries, out-of-scope boundaries.
18. Write `## Metrics` section: primary metric table + any secondary metrics.
19. Write `## Actions` section: trigger-condition rows with numeric thresholds + rollback procedure per action.
20. Write `## Risk Assessment` section: risk level (low/medium/high), failure mode, mitigation per action.
21. Write `## Monitoring` section: dashboard reference, alerts list (at least 2, specific threshold violations), reporting cadence.
22. Set `improvement.current = baseline.value`, `improvement.target = threshold.target`.
23. Set `cost.compute` and `cost.time` as floats representing overhead per optimization cycle.
**Exit**: all SCHEMA required fields populated, threshold ordering verified correct, every action has a numeric trigger, monitoring has at least 2 alerts.
### Phase 3: VALIDATE
**Goal**: Verify all quality gates before writing the final artifact.
24. Check QUALITY_GATES.md — verify each HARD gate manually (id format, kind, pillar, quality==null, all required fields).
25. Verify threshold ordering matches `metric.direction` (no inversion errors).
26. Verify every action trigger is numeric — no subjective conditions ("when it feels slow" fails).
27. Verify `automated: true` actions all have `risk.level = low`.
28. Verify `monitoring.alerts` reference specific threshold violations, not generic notifications.

## Template Loading

```yaml
# This instruction is ISO 3 of 13 in the builder stack
loader: cex_skill_loader.py
injection_point: F3_compose
priority: high
```

```bash
# Verify instruction loads correctly
python _tools/cex_skill_loader.py --verify optimizer
```

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | optimizer |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_optimizer_builder]] | related | 0.56 |
| [[bld_memory_optimizer]] | downstream | 0.45 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.43 |
| [[p11_qg_optimizer]] | downstream | 0.41 |
| [[optimizer-builder]] | downstream | 0.40 |
| [[bld_collaboration_optimizer]] | downstream | 0.38 |
| [[bld_examples_optimizer]] | downstream | 0.37 |
| [[bld_architecture_optimizer]] | downstream | 0.35 |
| [[bld_output_template_optimizer]] | downstream | 0.34 |
| [[p01_kc_optimizer]] | downstream | 0.30 |
