---
id: n00_dual_loop_architecture_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Dual Loop Architecture -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, dual_loop_architecture, p08, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A dual_loop_architecture defines the outer/inner loop control structure for agent execution: the outer loop handles goal decomposition, planning, and wave orchestration (N07 domain), while the inner loop handles single-task execution, quality gating, and retry logic (nucleus domain). It formalizes the separation of orchestration from production that makes CEX scalable.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `dual_loop_architecture` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable architecture name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| outer_loop | object | yes | Orchestration layer definition |
| outer_loop.owner | string | yes | Nucleus responsible (typically n07) |
| outer_loop.responsibilities | list | yes | Planning, dispatch, consolidation duties |
| inner_loop | object | yes | Execution layer definition |
| inner_loop.owner | string | yes | Nucleus responsible (n01-n06) |
| inner_loop.responsibilities | list | yes | 8F run, quality gate, signal |
| gate | object | no | Quality threshold between loops |
| gate.min_score | float | no | Minimum score to exit inner loop (default 8.0) |
| gate.max_retries | integer | no | Inner loop retry limit before escalation |

## When to use
- Designing a new multi-agent system where orchestration and production must be separated
- Documenting how N07 and a nucleus collaborate on a complex mission
- Establishing retry and escalation rules for autonomous workflows

## Builder
`archetypes/builders/dual_loop_architecture-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind dual_loop_architecture --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dla_cex_standard
kind: dual_loop_architecture
pillar: P08
nucleus: n07
title: "CEX Standard Dual Loop"
version: 1.0
quality: null
---
outer_loop:
  owner: n07
  responsibilities: [plan_waves, write_handoffs, dispatch_grid, consolidate]
inner_loop:
  owner: n03
  responsibilities: [run_8f, quality_gate, signal_complete]
gate:
  min_score: 8.0
  max_retries: 2
```

## Related kinds
- `workflow` (P12) -- sequences that implement the outer loop plan
- `supervisor` (P08) -- crew orchestrator that implements inner loop coordination
- `quality_gate` (P07) -- the gate artifact between inner loop retries
