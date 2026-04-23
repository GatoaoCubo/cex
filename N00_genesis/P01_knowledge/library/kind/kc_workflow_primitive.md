---
id: p01_kc_workflow_primitive
kind: knowledge_card
type: kind
pillar: P12
title: "Workflow Primitive -- Deep Knowledge for workflow_primitive"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: workflow_primitive
quality: 9.1
tags: [workflow_primitive, p12, PRODUCE, kind-kc, orchestration, dag]
tldr: "Atomic building blocks for agent workflows -- step, condition, loop, parallel, and router primitives that compose into DAGs"
when_to_use: "Designing agent workflows, building DAG-based orchestration, or extending the workflow engine"
keywords: [workflow, primitive, step, condition, loop, parallel, router, dag, orchestration]
feeds_kinds: [workflow_primitive]
density_score: null
related:
  - bld_memory_workflow_primitive
  - workflow-primitive-builder
  - bld_knowledge_card_workflow_primitive
  - p12_wp_map_reduce
  - p03_sp_workflow_primitive_builder
  - bld_collaboration_workflow_primitive
  - p03_ins_workflow_primitive_builder
  - bld_config_workflow_primitive
  - bld_examples_workflow_primitive
  - p01_kc_workflow
---

# Workflow Primitive

## Spec
```yaml
kind: workflow_primitive
pillar: P12
llm_function: PRODUCE
max_bytes: 4096
naming: p12_wp_{{type}}.yaml
core: false
```

## Purpose

Workflow primitives are the atomic units that compose into complex agent workflows (DAGs). Each primitive has a single responsibility: execute a step, branch on a condition, loop until done, fan-out in parallel, or route to a nucleus.

## Primitives

| Primitive | Purpose | Inputs | Outputs |
|-----------|---------|--------|---------|
| `step` | Execute one action | task, agent | result |
| `condition` | Branch on predicate | test, if_true, if_false | selected_branch |
| `loop` | Repeat until condition | body, max_iter, stop_when | final_result |
| `parallel` | Fan-out concurrent tasks | tasks[] | results[] |
| `router` | Pick nucleus by domain | intent | nucleus, model |
| `gate` | Block until quality met | artifact, threshold | pass/fail |
| `merge` | Combine parallel results | results[] | synthesized |

## Composition Rules

1. Primitives compose left-to-right: `step -> condition -> [step, step]`
2. Parallel branches must merge before continuing: `parallel -> merge -> step`
3. Gates are synchronization points: downstream waits for gate to pass
4. Loops must have explicit `max_iter` (no infinite loops in agent workflows)

## Key Patterns

1. **Research-then-build**: `step(research) -> gate(quality) -> parallel(build N03 + build N05) -> merge -> step(verify)`
2. **Retry with feedback**: `loop(step(build) -> gate(quality), stop_when=pass, max_iter=3)`
3. **Wave execution**: `parallel(wave_nuclei) -> gate(synthesis) -> parallel(next_wave)`

## CEX Integration

- `cex_sdk/workflow/` implements all 7 primitives as Python classes
- `cex_mission_runner.py` uses wave-based parallel + gate pattern
- `cex_coordinator.py` synthesis gates map to the `gate` primitive
- DAG definitions stored in `P12_orchestration/` as YAML

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_workflow_primitive]] | upstream | 0.54 |
| [[workflow-primitive-builder]] | related | 0.53 |
| [[bld_knowledge_card_workflow_primitive]] | sibling | 0.53 |
| [[p12_wp_map_reduce]] | related | 0.50 |
| [[p03_sp_workflow_primitive_builder]] | upstream | 0.49 |
| [[bld_collaboration_workflow_primitive]] | upstream | 0.44 |
| [[p03_ins_workflow_primitive_builder]] | upstream | 0.44 |
| [[bld_config_workflow_primitive]] | upstream | 0.41 |
| [[bld_examples_workflow_primitive]] | upstream | 0.40 |
| [[p01_kc_workflow]] | sibling | 0.40 |
