---
kind: knowledge_card
id: bld_knowledge_card_workflow_primitive
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for workflow_primitive production — atomic searchable facts
sources: workflow-primitive-builder schema + cex_mission_runner.py + cex_coordinator.py
quality: 9.1
title: "Knowledge Card Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_workflow_primitive_builder
  - bld_memory_workflow_primitive
  - p11_qg_workflow_primitive
  - p03_sp_workflow_primitive_builder
  - bld_examples_workflow_primitive
  - bld_output_template_workflow_primitive
  - p01_kc_workflow_primitive
  - bld_config_workflow_primitive
  - workflow-primitive-builder
  - bld_schema_workflow_primitive
---

# Domain Knowledge: workflow_primitive
## Executive Summary
Workflow primitives are YAML atomic building blocks — the seven composable types that form the basis of orchestration workflows. Each primitive defines one operation with typed inputs and outputs: step (single action), condition (if/else branch), loop (guarded repeat), parallel (concurrent fan-out), router (dynamic dispatch), gate (synchronization barrier), and merge (fan-in collection). Unlike full workflows (multi-step graphs), DAGs (dependency edges), or signals (status events), primitives carry only one atomic operation with typed I/O contracts for safe composition.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| Format | YAML |
| Naming | `p12_wp_{type}.yaml` |
| Max bytes | 4096 |
| Required fields | 4: type, description, inputs, outputs |
| Type enum | step, condition, loop, parallel, router, gate, merge (7 values) |
| I/O object fields | 3 required: name, type, required + 1 optional: description |
| Data types | string, integer, float, boolean, list, object, artifact_ref |
| Composition | left-to-right: outputs type-match inputs of successor |
| Scope | one primitive = one type = one operation = one file |
## Patterns
| Pattern | Rule |
|---------|------|
| Research-then-build | step (research) -> gate (quality >= 8.0) -> step (build) |
| Retry with feedback | loop (max_iter=3, break_condition="score >= 8.0", feedback_input=feedback) |
| Wave execution | parallel (fan-out to nuclei) -> merge (strategy=all) -> gate (threshold=0.8) |
| Conditional routing | condition (if research_needed) -> true: step (research) / false: step (build) |
| Dynamic dispatch | router (routes by domain) -> default: step (generic_handler) |
| Quality synchronization | gate (threshold=0.8, wait_for=[build_1, build_2, build_3]) |
| Parallel must merge | every parallel has merge_ref; every merge has source_refs |
| Loop guard | every loop has max_iter (1-100) — no unbounded loops |
| Gate threshold | every gate has numeric threshold — no always-pass gates |
| Router fallback | every router has default_route — no dropped inputs |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Full workflow graph in one primitive | Primitives are atomic — one type, one operation |
| Loop without max_iter | Unbounded loop runs forever — system killer |
| Parallel without merge_ref | Fan-out results are silently lost |
| Gate without threshold | Always passes — provides zero quality control |
| Router without default_route | Unmatched inputs silently disappear |
| Untyped I/O (all "string") | Composition validation impossible |
| Compound primitive (step + condition + loop) | Defeats the composition model |
| More than 15 inputs/outputs | Primitive is too complex — decompose |
## Application
1. Identify the primitive type from the 7-value enum
2. Define typed inputs: name, type, required flag, description
3. Define typed outputs: name, type, required flag, description
4. Add type-specific guards:
   - loop: max_iter (1-100), break_condition, feedback_input
   - parallel: branches, merge_ref, timeout_s
   - gate: threshold, wait_for, timeout_s
   - condition: condition_expr, true_branch, false_branch
   - router: routes [{match, target}], default_route
   - merge: strategy (all/any/first/majority), source_refs
   - step: (no additional guards)
5. Add composition metadata: composable_after, composable_before
6. Add error handling: retry_count, on_error
7. Validate atomicity: one type, one operation
8. Name file `p12_wp_{type}.yaml`, keep under 4096 bytes
## References
- Schema: workflow_primitive schema (P06)
- Runtime: cex_mission_runner.py, cex_coordinator.py, cex_sdk/workflow/
- Pillar: P12 (orchestration)
- Boundary: workflow (graph), dag (edges), signal (event), handoff (instruction) — all distinct from workflow_primitive

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_workflow_primitive_builder]] | downstream | 0.62 |
| [[bld_memory_workflow_primitive]] | downstream | 0.59 |
| [[p11_qg_workflow_primitive]] | downstream | 0.56 |
| [[p03_sp_workflow_primitive_builder]] | downstream | 0.56 |
| [[bld_examples_workflow_primitive]] | downstream | 0.55 |
| [[bld_output_template_workflow_primitive]] | downstream | 0.55 |
| [[p01_kc_workflow_primitive]] | sibling | 0.54 |
| [[bld_config_workflow_primitive]] | downstream | 0.51 |
| [[workflow-primitive-builder]] | downstream | 0.50 |
| [[bld_schema_workflow_primitive]] | downstream | 0.46 |
