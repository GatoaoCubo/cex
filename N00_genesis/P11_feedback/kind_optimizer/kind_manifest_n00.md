---
id: n00_optimizer_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Optimizer -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, optimizer, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An optimizer defines a process optimization specification that maps a measurable metric to a set of automated or semi-automated actions that improve it. It closes the measurement-action loop in the feedback flywheel, enabling continuous improvement of agent performance, cost efficiency, or quality without requiring manual tuning after initial configuration.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `optimizer` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_metric | string | yes | Metric being optimized (e.g. quality_score, latency_p95, token_cost) |
| optimization_direction | enum | yes | maximize \| minimize |
| baseline_value | float | yes | Current metric value before optimization |
| target_value | float | yes | Goal metric value |
| actions | array | yes | Ordered list of optimization actions with trigger thresholds |
| evaluation_window | string | yes | Time window for metric measurement (e.g. "7d", "30d") |
| max_action_frequency | string | no | Minimum interval between action applications |

## When to use
- When automating quality score improvement for a nucleus's artifact output
- When optimizing token costs through automatic compression or caching tuning
- When building latency optimization loops for production API endpoints

## Builder
`archetypes/builders/optimizer-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind optimizer --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: opt_n04_quality_score
kind: optimizer
pillar: P11
nucleus: n04
title: "Example Optimizer"
version: 1.0
quality: null
---
# Optimizer: N04 Knowledge Card Quality
target_metric: quality_score
optimization_direction: maximize
baseline_value: 7.8
target_value: 9.0
evaluation_window: "7d"
actions: [{threshold: 8.0, action: "trigger cex_evolve.py heuristic pass"}]
```

## Related kinds
- `reward_signal` (P11) -- signal that feeds optimizer metric updates
- `quality_gate` (P11) -- gate that optimizer targets to pass consistently
- `self_improvement_loop` (P11) -- higher-order loop that orchestrates optimizers
