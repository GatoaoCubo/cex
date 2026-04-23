---
id: n00_input_schema_manifest
kind: knowledge_card
pillar: P06
nucleus: n00
title: "Input Schema -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, input_schema, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_input_schema
  - bld_schema_reranker_config
  - input-schema-builder
  - bld_schema_validation_schema
  - bld_schema_integration_guide
  - bld_schema_voice_pipeline
  - bld_schema_thinking_config
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Input schema defines the data contract for what an agent, tool, or pipeline step accepts as input. It specifies field names, types, required/optional status, validation constraints, and default values. Applied at F1 CONSTRAIN in the 8F pipeline, it ensures that callers provide well-formed input before any processing begins, preventing invalid data from propagating through the system.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `input_schema` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Target component + "Input Schema" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_component | string | yes | Agent, tool, or pipeline step this schema governs |
| fields | list | yes | Field definitions with name, type, required, constraints |
| schema_format | enum | yes | json_schema / pydantic / zod / typescript |
| strict_mode | bool | yes | Whether to reject unknown fields |
| example | object | no | Minimal valid input example |

## When to use
- Defining the accepted input for a new agent or tool before building it
- Enforcing input validation at the boundary of a microservice or pipeline stage
- Generating SDK method signatures from a canonical input contract

## Builder
`archetypes/builders/input_schema-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind input_schema --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering defines; N05 operations enforces
- `{{SIN_LENS}}` -- Inventive Pride: exact, minimal, no ambiguous fields
- `{{TARGET_AUDIENCE}}` -- callers of the agent or tool (humans, other agents, APIs)
- `{{DOMAIN_CONTEXT}}` -- component type, input complexity, validation strictness

## Example (minimal)
```yaml
---
id: input_schema_cex_8f_runner
kind: input_schema
pillar: P06
nucleus: n03
title: "cex_8f_runner Input Schema"
version: 1.0
quality: null
---
target_component: cex_8f_runner
schema_format: pydantic
strict_mode: true
fields:
  - {name: intent, type: str, required: true}
  - {name: kind, type: NucleusId, required: false}
  - {name: execute, type: bool, required: false, default: false}
```

## Related kinds
- `validation_schema` (P06) -- post-generation contract; input_schema is pre-processing
- `api_reference` (P06) -- references input schemas for request body definitions
- `enum_def` (P06) -- enum types referenced in input schema field definitions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | related | 0.45 |
| [[bld_schema_reranker_config]] | related | 0.41 |
| [[input-schema-builder]] | related | 0.39 |
| [[bld_schema_validation_schema]] | related | 0.39 |
| [[bld_schema_integration_guide]] | related | 0.38 |
| [[bld_schema_voice_pipeline]] | related | 0.38 |
| [[bld_schema_thinking_config]] | related | 0.38 |
| [[bld_schema_dataset_card]] | related | 0.38 |
| [[bld_schema_usage_report]] | related | 0.37 |
| [[bld_schema_multimodal_prompt]] | related | 0.37 |
