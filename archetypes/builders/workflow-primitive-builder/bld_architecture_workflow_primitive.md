---
kind: architecture
id: bld_architecture_workflow_primitive
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of workflow_primitive — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - workflow-primitive-builder
  - bld_collaboration_workflow_primitive
  - p03_ins_workflow_primitive_builder
  - p03_sp_workflow_primitive_builder
  - bld_tools_workflow_primitive
  - bld_knowledge_card_workflow_primitive
  - bld_config_workflow_primitive
  - bld_schema_workflow_primitive
  - bld_memory_workflow_primitive
  - p11_qg_workflow_primitive
---

# Architecture: workflow_primitive in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata (id, kind, pillar, type, quality) | workflow-primitive-builder | active |
| type_field | Primitive type: step, condition, loop, parallel, router, gate, merge | workflow-primitive-builder | active |
| inputs | Typed input fields consumed by the primitive | workflow-primitive-builder | active |
| outputs | Typed output fields produced by the primitive | workflow-primitive-builder | active |
| guards | Type-specific constraints: max_iter, threshold, timeout_s, condition_expr | workflow-primitive-builder | active |
| composition_metadata | Composability rules: what can precede/follow this primitive | workflow-primitive-builder | active |
| branch_config | Type-specific branch references (parallel branches, router routes) | workflow-primitive-builder | active |
## Dependency Graph
```
workflow_primitive  --composes_into-->  workflow       --executes_via-->  mission_runner
workflow_primitive  --consumed_by-->    coordinator    --orchestrates-->  wave_execution
workflow_primitive  --validated_by-->   quality_gate   --checks-->       composition_rules
parallel_primitive  --requires-->       merge_primitive --collects-->     fan_in_results
```
| From | To | Type | Data |
|------|----|------|------|
| workflow_primitive (P12) | workflow (P12) | composes_into | primitives combine into full workflow graphs |
| workflow_primitive | cex_mission_runner.py | consumed_by | mission runner executes primitives in wave order |
| workflow_primitive | cex_coordinator.py | consumed_by | coordinator manages synthesis gates between waves |
| workflow_primitive | cex_sdk/workflow/ | runtime | SDK workflow module instantiates primitives at runtime |
| parallel primitive | merge primitive | requires | parallel fan-out MUST have a corresponding merge fan-in |
| gate primitive | upstream primitives | wait_for | gates block until upstream threshold is met |
| loop primitive | feedback input | receives | loops consume iteration feedback to decide continue/break |
| signal (P12) | gate primitive | triggers | signals from completed work feed into gate threshold checks |
## Boundary Table
| workflow_primitive IS | workflow_primitive IS NOT |
|-----------------------|--------------------------|
| An atomic orchestration building block (one type, one operation) | A full multi-step workflow graph (workflow P12) |
| Typed I/O contract for composition (inputs/outputs) | A DAG edge definition (dag P12) |
| Self-contained with guard clauses (max_iter, threshold) | An inter-agent signal (signal P12) |
| Composable left-to-right into workflows | Task instructions or handoff content (handoff P12) |
| YAML for human readability | JSON wire format (that belongs to signal) |
| Stateless definition (reusable across workflows) | Mutable state that changes during execution |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | type, description | Define what kind of primitive this is |
| Contract | inputs, outputs | Specify typed I/O for composition |
| Control | guards (max_iter, threshold, timeout_s) | Constrain execution behavior |
| Composition | composable_after, composable_before, branch_config | Enable assembly into workflows |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-primitive-builder]] | downstream | 0.75 |
| [[bld_collaboration_workflow_primitive]] | upstream | 0.70 |
| [[p03_ins_workflow_primitive_builder]] | upstream | 0.68 |
| [[p03_sp_workflow_primitive_builder]] | upstream | 0.66 |
| [[bld_tools_workflow_primitive]] | upstream | 0.61 |
| [[bld_knowledge_card_workflow_primitive]] | upstream | 0.56 |
| [[bld_config_workflow_primitive]] | downstream | 0.55 |
| [[bld_schema_workflow_primitive]] | upstream | 0.54 |
| [[bld_memory_workflow_primitive]] | downstream | 0.53 |
| [[p11_qg_workflow_primitive]] | downstream | 0.53 |
