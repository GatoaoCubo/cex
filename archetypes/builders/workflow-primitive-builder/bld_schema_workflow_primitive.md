---
kind: schema
id: bld_schema_workflow_primitive
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for workflow_primitive - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - p03_ins_workflow_primitive_builder
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_input_schema
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_agent_profile
---

# Schema: workflow_primitive
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `workflow_primitive` |
| Machine format | `yaml` |
| Naming | `p12_wp_{type}.yaml` |
| Max bytes | 4096 |
## Required Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| type | enum (step, condition, loop, parallel, router, gate, merge) | YES | - | primitive category |
| description | string, non-empty | YES | - | one-line purpose of this primitive |
| inputs | list[io_object], non-empty | YES | - | typed input fields consumed |
| outputs | list[io_object], non-empty | YES | - | typed output fields produced |
## I/O Object Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| name | string, non-empty, snake_case | YES | - | field identifier |
| type | enum (string, integer, float, boolean, list, object, artifact_ref) | YES | - | data type |
| required | boolean | YES | true | whether this field must be present |
| description | string | NO | omitted | one-line purpose |
## Type-Specific Required Fields
### step
No additional required fields. Simplest primitive.
### condition
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| condition_expr | string, non-empty | YES | boolean expression to evaluate |
| true_branch | string (primitive ref) | YES | next primitive when condition is true |
| false_branch | string (primitive ref) | YES | next primitive when condition is false |
### loop
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| max_iter | integer, 1-100 | YES | maximum iterations before forced exit |
| break_condition | string | NO | optional early exit expression |
| feedback_input | string | NO | input field that receives iteration feedback |
### parallel
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| branches | list[string], non-empty | YES | primitive refs to execute concurrently |
| merge_ref | string (primitive ref) | YES | reference to corresponding merge primitive |
| timeout_s | integer, > 0 | NO | max seconds before killing stalled branches |
### router
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| routes | list[route_object] | YES | list of match-target pairs |
| default_route | string (primitive ref) | YES | fallback when no match |
### gate
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| threshold | number (0.0-1.0 ratio or integer count) | YES | required to pass |
| wait_for | list[string] | YES | upstream primitive refs to collect from |
| timeout_s | integer, > 0 | NO | max seconds to wait before failing |
### merge
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| strategy | enum (all, any, first, majority) | YES | how to combine branch results |
| source_refs | list[string], non-empty | YES | upstream parallel/gate refs |
## Route Object Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| match | string, non-empty | YES | pattern to match against router input |
| target | string (primitive ref) | YES | primitive to route to on match |
## Optional Fields (all types)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| name | string | NO | omitted | instance name for this primitive |
| tags | list[string] | NO | omitted | classification tags |
| retry_count | integer, >= 0 | NO | 0 | retries on failure |
| on_error | string (primitive ref) | NO | omitted | error handler primitive |
| composable_after | list[string] | NO | omitted | primitive types that can precede |
| composable_before | list[string] | NO | omitted | primitive types that can follow |
## Semantic Rules
1. One primitive = one type = one atomic operation = one file
2. Primitives are stateless definitions — reusable across multiple workflows
3. Left-to-right composition: outputs of primitive A must type-match inputs of primitive B
4. Every parallel MUST reference a merge via `merge_ref` — fan-out without fan-in is forbidden
5. Every loop MUST have `max_iter` (1-100) — unbounded loops kill systems
6. Every gate MUST have numeric `threshold` — thresholdless gates always pass
7. Every router MUST have `default_route` — unmatched inputs must go somewhere
8. Merge `strategy` determines result assembly: all (wait for everything), any (first success), first (fastest), majority (>50%)
## Boundary Rules
`workflow_primitive` IS:
- atomic orchestration building block
- typed I/O contract for composition
- self-contained with guard clauses
`workflow_primitive` IS NOT:
- `workflow`: no multi-step graph, no edge definitions, no execution plan
- `dag`: no dependency graph, no topological sort
- `signal`: no atomic event notification, no fire-and-forget status
- `handoff`: no task instructions, no scope fences, no execution context
## Canonical Minimal Example
```yaml
type: step
description: Execute research query and return findings
inputs:
  - name: query
    type: string
    required: true
  - name: max_results
    type: integer
    required: false
outputs:
  - name: findings
    type: list
    required: true
  - name: confidence
    type: float
    required: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.51 |
| [[bld_schema_reranker_config]] | sibling | 0.50 |
| [[p03_ins_workflow_primitive_builder]] | upstream | 0.50 |
| [[bld_schema_quickstart_guide]] | sibling | 0.50 |
| [[bld_schema_dataset_card]] | sibling | 0.49 |
| [[bld_schema_pitch_deck]] | sibling | 0.49 |
| [[bld_schema_input_schema]] | sibling | 0.49 |
| [[bld_schema_sandbox_config]] | sibling | 0.49 |
| [[bld_schema_benchmark_suite]] | sibling | 0.48 |
| [[bld_schema_agent_profile]] | sibling | 0.47 |
