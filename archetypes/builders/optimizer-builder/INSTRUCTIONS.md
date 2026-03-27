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
quality: null
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
---

## Context

The optimizer-builder receives a **process description** and produces an `optimizer` artifact encoding the metric-to-action cycle for continuous improvement of that process.

**Input variables**:
- `{{process}}` — name and brief description of the process to optimize (e.g., "API response pipeline", "nightly batch job")
- `{{metric}}` — the measurable quantity to optimize with unit (e.g., "p95 latency in ms", "error rate as %")
- `{{direction}}` — `minimize` or `maximize`
- `{{baseline}}` — optional current measured value under normal operating conditions; if absent, mark as `TBD`
- `{{constraints}}` — optional hard limits optimization must not violate (e.g., "cannot exceed $50/day")

**Output**: a single `optimizer` artifact at `p11_opt_{{process_slug}}.md` with tripartite thresholds, action catalog, baseline record, risk assessment, and monitoring config.

**Boundaries**: handles continuous optimization cycles only. Does NOT produce one-time bug fixes (bugloop), passive measurement records (benchmark), pass/fail barriers (quality_gate), or safety constraints (guardrail).

---

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
   If `{{baseline}}` is absent, set all three to `TBD` and define the measurement procedure (tool, window duration, conditions to hold constant).
4. Document baseline conditions: date or measurement window, load level, environment, config version.
5. Identify 2–4 available actions: enumerate concrete operations that can move the metric toward `{{direction}}` (e.g., tune parameters, prune elements, scale capacity, replace component, restructure flow).
6. For each action, assess automation risk: can it fire without human approval? Set `automated: true` only if `risk.level = low` AND rollback is instant.
7. Search existing optimizers for this domain (brain_query [IF MCP]: `optimizer {{process}}`). Avoid duplicates; if found, determine whether an update is needed.

**Exit**: metric fully characterized, threshold values set (or TBD with measurement procedure), at least 2 actions identified with automation flag.

---

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

---

### Phase 3: VALIDATE

**Goal**: Verify all quality gates before writing the final artifact.

24. Check QUALITY_GATES.md — verify each HARD gate manually (id format, kind, pillar, quality==null, all required fields).
25. Verify threshold ordering matches `metric.direction` (no inversion errors).
26. Verify every action trigger is numeric — no subjective conditions ("when it feels slow" fails).
27. Verify `automated: true` actions all have `risk.level = low`.
28. Verify `monitoring.alerts` reference specific threshold violations, not generic notifications.
29. Check SOFT gates (rollback defined, secondary metrics present, >= 2 alerts).
30. If score < 8.0: revise in same pass before outputting. Do not output a failing artifact.
31. Write the final artifact using the Output Contract template below.

---

## Output Contract

```
---
id: p11_opt_{{process_slug}}
kind: optimizer
pillar: P11
domain: {{process}}
version: 1.0.0
created: {{date}}
author: optimizer-builder
metric: {{metric_name}}
unit: {{unit}}
direction: {{minimize|maximize}}
trigger: {{trigger_value}}
target: {{target_value}}
critical: {{critical_value}}
baseline: {{baseline_value}}
quality: null
tags: [optimizer, {{process_slug}}, {{metric_name}}]
---

## Target Process

**Process**: {{process}}
**In scope**: {{in_scope_boundaries}}
**Out of scope**: {{out_of_scope_boundaries}}

## Metrics

| Metric | Unit | Direction | Trigger | Target | Critical |
|--------|------|-----------|---------|--------|----------|
| {{metric_name}} | {{unit}} | {{direction}} | {{trigger}} | {{target}} | {{critical}} |

## Actions

| Threshold | Type | Description | Automated | Rollback |
|-----------|------|-------------|-----------|---------|
| trigger | {{action_type}} | {{action_desc}} | {{true|false}} | {{rollback_desc}} |
| critical | manual_review | escalate to on-call | false | n/a |

## Risk Assessment

| Action | Risk | Failure Mode | Mitigation |
|--------|------|-------------|------------|
| {{action_desc}} | {{low|medium|high}} | {{failure_mode}} | {{mitigation}} |

## Monitoring

- **Dashboard**: {{dashboard_name_or_url}}
- **Alerts**: {{alert_1_desc}} (trigger breach), {{alert_2_desc}} (critical breach)
- **Reporting**: {{reporting_cadence}}
- **Check interval**: {{check_interval}}

## Baseline Record

- **Value**: {{baseline_value}} {{unit}}
- **Measured at**: {{timestamp_or_window}}
- **Conditions**: {{load_level}}, {{environment}}, {{config_version}}
```

---

## Validation

| # | Gate | Type |
|---|------|------|
| 1 | `metric` field present and includes unit | HARD |
| 2 | `direction` is exactly `minimize` or `maximize` | HARD |
| 3 | Threshold ordering is correct for direction (no inversion) | HARD |
| 4 | Each threshold level (trigger, target, critical) has at least one action | HARD |
| 5 | `critical` level has at least one `automated: false` action | HARD |
| 6 | Every action trigger is a numeric value, not a subjective condition | HARD |
| 7 | Baseline is documented (value or TBD with measurement procedure) | HARD |
| 8 | `quality: null` is set | HARD |
| 9 | `automated: true` actions all have `risk.level = low` | HARD |
| 10 | Monitoring has at least 2 alerts referencing specific thresholds | SOFT |
| 11 | Rollback procedure defined for each action | SOFT |
| 12 | Secondary metrics table present | SOFT |

---

## Metacognition

**Does**:
- Encodes continuous metric-to-action optimization cycles with tripartite thresholds
- Produces correct threshold ordering based on direction (minimize vs maximize)
- Documents risk, failure mode, and mitigation for each action
- Configures monitoring so the cycle can run autonomously

**Does NOT**:
- Produce one-time bug fix procedures (use bugloop)
- Record passive measurements without actions (use benchmark)
- Define pass/fail quality barriers (use quality_gate)
- Enforce safety constraints (use guardrail)

**Chaining**: output feeds monitoring systems (thresholds + check_interval), alert routers (alert channels), dashboard builders (metric + target). Input from benchmark results (baseline), process owner requirements, constraint catalog.
