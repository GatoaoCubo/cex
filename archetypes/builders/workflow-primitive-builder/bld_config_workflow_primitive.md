---
kind: config
id: bld_config_workflow_primitive
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: workflow_primitive Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_wp_{type}.yaml` | `p12_wp_step.yaml`, `p12_wp_parallel.yaml` |
| Named instance | `p12_wp_{type}_{name}.yaml` | `p12_wp_gate_quality_check.yaml` |
| Builder directory | kebab-case | `workflow-primitive-builder/` |
| Field names | snake_case | `max_iter`, `merge_ref`, `condition_expr` |
| Type values | lowercase enum | `step`, `condition`, `loop`, `parallel`, `router`, `gate`, `merge` |
| Branch references | dot notation | `p12_wp_step.research`, `p12_wp_merge.collect` |
Rule: use `.yaml` only for this builder — primitives are human-readable composition blocks.
## File Paths
- Output: `cex/P12_orchestration/compiled/p12_wp_{type}.yaml`
- Human reference: `cex/P12_orchestration/examples/p12_wp_{type}.md`
## Size Limits
- Preferred primitive size: <= 2048 bytes
- Absolute max: 4096 bytes
- Primitives should be compact: one type, one operation, clear I/O
- Descriptions are one-liners, not paragraphs
## Primitive Restrictions
- Required fields must appear exactly as defined in schema
- Omit optional null/unknown fields instead of writing placeholders
- `max_iter` required only for loop type (must be 1-100)
- `threshold` required only for gate type (numeric)
- `merge_ref` required only for parallel type (must reference a merge primitive)
- Inputs and outputs must be typed (name + type + required flag)
## Boundary Restrictions
- No full workflow graphs — a primitive is ONE atomic block
- No DAG edge definitions — those compose primitives, not define them
- No signal payloads or handoff instructions
- No agent identity or system prompt content
- No routing policy tables (use router primitive type instead)
## Composition Rules
- Primitives compose left-to-right: output of one feeds input of the next
- Every parallel MUST have a corresponding merge — fan-out without fan-in is forbidden
- Every gate MUST have a threshold — gates without thresholds always pass (useless)
- Every loop MUST have max_iter — unbounded loops are system killers
- Router default_route is mandatory — unmatched routes must go somewhere
- Type compatibility: outputs of primitive A must type-match inputs of primitive B
