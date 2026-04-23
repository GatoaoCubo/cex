---
id: n00_workflow_primitive_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Workflow Primitive -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, workflow_primitive, p12, n00, archetype, template]
density_score: 1.0
related:
  - workflow-primitive-builder
  - bld_schema_workflow_primitive
  - bld_architecture_workflow_primitive
  - bld_schema_workflow
  - bld_collaboration_workflow_primitive
  - p01_kc_workflow_primitive
  - p03_sp_workflow_primitive_builder
  - p01_kc_workflow
  - p03_ins_workflow_primitive_builder
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A workflow_primitive defines a low-level workflow execution primitive (Step, Parallel, Loop, Condition, Router) that serves as the atomic building block of complex orchestration logic. It is the instruction set of the CEX workflow engine -- each primitive has precise execution semantics that workflow compilers and runners can implement consistently across different execution environments.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `workflow_primitive` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| primitive_type | enum | yes | Step \| Parallel \| Loop \| Condition \| Router |
| semantics | string | yes | Prose description of execution behavior |
| parameters | array | yes | Named parameters with types and descriptions |
| preconditions | array | no | Conditions that must hold before execution |
| postconditions | array | no | Guarantees that hold after successful execution |
| error_behavior | enum | yes | fail_fast \| retry \| skip \| compensate |

## When to use
- When implementing a new workflow execution engine that must support CEX workflows
- When defining the execution semantics for a custom workflow step type
- When auditing whether a workflow implementation correctly handles all primitive types

## Builder
`archetypes/builders/workflow_primitive-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind workflow_primitive --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: wp_parallel_primitive
kind: workflow_primitive
pillar: P12
nucleus: n07
title: "Example Workflow Primitive"
version: 1.0
quality: null
---
# Workflow Primitive: Parallel
primitive_type: Parallel
semantics: "Execute all child steps concurrently. Collect all results before continuing."
parameters:
  - name: branches, type: array, description: "Steps to execute in parallel"
  - name: max_concurrency, type: integer, description: "Max simultaneous branches"
error_behavior: fail_fast
```

## Related kinds
- `workflow_node` (P12) -- node types that implement specific workflow primitives
- `workflow` (P12) -- workflow that composes these primitives into a complete program
- `dag` (P12) -- Parallel primitive maps to fan-out edges in the DAG

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-primitive-builder]] | related | 0.48 |
| [[bld_schema_workflow_primitive]] | upstream | 0.45 |
| [[bld_architecture_workflow_primitive]] | upstream | 0.43 |
| [[bld_schema_workflow]] | upstream | 0.41 |
| [[bld_collaboration_workflow_primitive]] | upstream | 0.41 |
| [[p01_kc_workflow_primitive]] | sibling | 0.39 |
| [[p03_sp_workflow_primitive_builder]] | upstream | 0.38 |
| [[p01_kc_workflow]] | sibling | 0.38 |
| [[p03_ins_workflow_primitive_builder]] | upstream | 0.37 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.37 |
