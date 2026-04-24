---
id: n00_workflow_manifest
kind: knowledge_card
8f: F3_inject
pillar: P12
nucleus: n00
title: "Workflow -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, workflow, p12, n00, archetype, template]
density_score: 1.0
related:
  - p01_kc_workflow
  - bld_schema_workflow
  - workflow-builder
  - bld_architecture_workflow
  - bld_schema_quickstart_guide
  - bld_schema_contributor_guide
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_kind
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A workflow defines a sequential or parallel sequence of steps that accomplish a multi-stage task, specifying the order of operations, conditional branching, input/output contracts between steps, and error handling. It is the fundamental orchestration artifact that CEX uses to codify repeatable multi-step processes as versioned, runnable specifications.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `workflow` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| execution_mode | enum | yes | sequential \| parallel \| hybrid |
| steps | array | yes | Ordered step definitions with ID, kind, inputs, outputs, and on_error |
| inputs | object | yes | Workflow-level input parameters |
| outputs | object | yes | Workflow-level output artifacts |
| timeout_minutes | integer | yes | Maximum total workflow execution time |
| retry_policy | object | no | Step-level retry configuration |

## When to use
- When codifying a repeatable multi-step process that nuclei execute
- When building the execution plan for a CEX mission wave
- When defining the process that a crew_template or dag references

## Builder
`archetypes/builders/workflow-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind workflow --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: wf_8f_pipeline_execution
kind: workflow
pillar: P12
nucleus: n07
title: "Example Workflow"
version: 1.0
quality: null
---
# Workflow: 8F Pipeline Execution
execution_mode: sequential
timeout_minutes: 30
steps:
  - id: F1_constrain, inputs: [user_intent], outputs: [kind, pillar]
  - id: F2_become, inputs: [kind], outputs: [builder_context]
  - id: F6_produce, inputs: [builder_context], outputs: [artifact]
  - id: F8_collaborate, inputs: [artifact], outputs: [signal]
```

## Related kinds
- `dag` (P12) -- dependency graph encoding workflow execution topology
- `workflow_node` (P12) -- typed node that workflow steps reference
- `schedule` (P12) -- temporal trigger that initiates this workflow

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_workflow]] | sibling | 0.46 |
| [[bld_schema_workflow]] | upstream | 0.45 |
| [[workflow-builder]] | related | 0.40 |
| [[bld_architecture_workflow]] | upstream | 0.39 |
| [[bld_schema_quickstart_guide]] | upstream | 0.37 |
| [[bld_schema_contributor_guide]] | upstream | 0.36 |
| [[bld_schema_reranker_config]] | upstream | 0.36 |
| [[bld_schema_integration_guide]] | upstream | 0.35 |
| [[bld_schema_benchmark_suite]] | upstream | 0.35 |
| [[bld_schema_kind]] | upstream | 0.35 |
