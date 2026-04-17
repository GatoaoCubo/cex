---
id: n00_workflow_node_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Workflow Node -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, workflow_node, p12, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A workflow_node is a typed node in a visual or programmatic workflow, representing a single unit of computation with defined input schema, output schema, execution semantics, and visual representation. It is the building block from which workflows and DAGs are assembled, providing a reusable, typed contract for each step that tooling can validate and execute.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `workflow_node` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| node_type | enum | yes | task \| decision \| parallel \| join \| start \| end \| subworkflow |
| input_schema | object | yes | JSON Schema of node inputs |
| output_schema | object | yes | JSON Schema of node outputs |
| executor | enum | yes | nucleus \| tool \| script \| webhook \| human |
| executor_ref | string | yes | Reference to executor (nucleus ID, tool name, script path) |
| idempotent | boolean | yes | Whether re-running produces the same result |

## When to use
- When defining reusable node types for a visual workflow editor
- When building a workflow library of typed, validated step definitions
- When generating workflow schemas for static analysis or validation

## Builder
`archetypes/builders/workflow_node-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind workflow_node --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: wn_nucleus_task_node
kind: workflow_node
pillar: P12
nucleus: n07
title: "Example Workflow Node"
version: 1.0
quality: null
---
# Workflow Node: Nucleus Task
node_type: task
executor: nucleus
executor_ref: n03
idempotent: false
input_schema: {type: object, properties: {handoff_path: {type: string}}}
output_schema: {type: object, properties: {signal: {type: string}, artifacts: {type: array}}}
```

## Related kinds
- `workflow` (P12) -- workflow composed of these nodes
- `workflow_primitive` (P12) -- execution primitives that implement node behavior
- `dag` (P12) -- dependency graph connecting workflow nodes
