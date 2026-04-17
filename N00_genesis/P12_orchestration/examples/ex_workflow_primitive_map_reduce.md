---
id: p12_wp_map_reduce
kind: workflow_primitive
pillar: P12
title: "Example — Map-Reduce Workflow Primitive"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
primitive_type: composite
primitives_used: [parallel, merge, gate]
domain: workflow_primitive
quality: 9.1
tags: [workflow-primitive, map-reduce, parallel, merge, orchestration, dag]
tldr: "Map-reduce pattern: fan-out tasks to parallel nuclei (map), collect and synthesize results (reduce), quality gate before output."
when_to_use: "Distributing independent subtasks across nuclei and combining results into a single output"
keywords: [workflow, primitive, map, reduce, parallel, merge, fan-out, synthesis]
density_score: null
---

# Workflow Primitive: Map-Reduce

## Pattern
```
         ┌─→ step(N01: research)  ─┐
intent ──┼─→ step(N02: marketing) ─┼──→ merge ──→ gate(quality >= 8.0) ──→ output
         └─→ step(N03: build)     ─┘
```

## Primitives Used
| Primitive | Role | Config |
|-----------|------|--------|
| parallel | Fan-out intent to 3 nuclei | tasks: [n01_task, n02_task, n03_task] |
| step (×3) | Execute one task per nucleus | agent: n01/n02/n03, timeout: 600s |
| merge | Combine 3 results into one | strategy: concatenate_by_section |
| gate | Quality check on merged output | threshold: 8.0, retry_on_fail: true |

## Configuration
```yaml
type: composite
name: map_reduce
steps:
  - id: fan_out
    primitive: parallel
    tasks:
      - {agent: n01, task: "$intent.research_component"}
      - {agent: n02, task: "$intent.marketing_component"}
      - {agent: n03, task: "$intent.build_component"}
    timeout_per_task: 600

  - id: collect
    primitive: merge
    inputs: ["fan_out.results"]
    strategy: concatenate_by_section
    conflict_resolution: latest_wins

  - id: quality_check
    primitive: gate
    input: "collect.output"
    threshold: 8.0
    on_fail: retry_lowest_scoring
    max_retries: 2

  - id: output
    primitive: step
    action: save_and_signal
    input: "quality_check.output"
```

## Execution Timeline
| Time | Primitive | Status |
|------|-----------|--------|
| T+0s | parallel (fan-out) | 3 tasks dispatched |
| T+0-600s | step × 3 | Running concurrently |
| T+600s | merge | Collecting results |
| T+601s | gate | Quality check |
| T+602s | output | Save + signal |

## Composition Rules
1. `parallel` MUST be followed by `merge` before any sequential step
2. `gate` blocks downstream — if fail, retry or abort
3. Each `step` must have explicit `timeout` (no infinite waits)
4. `merge` must define `conflict_resolution` for overlapping sections

## Boundary
workflow_primitive IS: an atomic or composite building block for agent workflow DAGs with typed inputs/outputs.
workflow_primitive IS NOT: a director (orchestrates people), a workflow definition (full DAG), or a signal (inter-nucleus message).
