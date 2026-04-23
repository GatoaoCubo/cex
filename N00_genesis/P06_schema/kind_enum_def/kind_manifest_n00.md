---
id: n00_enum_def_manifest
kind: knowledge_card
pillar: P06
nucleus: n00
title: "Enum Def -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, enum_def, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_enum_def
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_eval_metric
  - bld_schema_action_paradigm
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_voice_pipeline
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Enum def produces a reusable enumeration type definition that constrains a field to a fixed set of valid string or integer values. Enum defs are referenced across multiple schemas to ensure consistent value vocabularies (e.g., nucleus names, pillar codes, quality grades). They serve as the single source of truth for constrained field values across the CEX typed knowledge system.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `enum_def` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Enum name in PascalCase |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| enum_name | string | yes | Canonical name used in schema references |
| value_type | enum | yes | string / integer / boolean |
| values | list | yes | All valid values with optional description |
| extensible | bool | yes | Whether new values can be added without breaking change |
| deprecated_values | list | no | Values no longer in use with migration path |

## When to use
- Defining a constrained set of values that multiple schemas share
- Replacing ad-hoc string fields with a validated vocabulary
- Providing the canonical value list for dropdown UI components

## Builder
`archetypes/builders/enum_def-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind enum_def --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering defines; N04 knowledge documents
- `{{SIN_LENS}}` -- Inventive Pride: precise, minimal, no redundancy
- `{{TARGET_AUDIENCE}}` -- schemas, validators, and UI components referencing the enum
- `{{DOMAIN_CONTEXT}}` -- domain where the enum is used, stability expectations

## Example (minimal)
```yaml
---
id: enum_def_nucleus_id
kind: enum_def
pillar: P06
nucleus: n03
title: "NucleusId"
version: 1.0
quality: null
---
enum_name: NucleusId
value_type: string
extensible: false
values:
  - {value: n00, description: Genesis archetype}
  - {value: n01, description: Intelligence}
  - {value: n07, description: Orchestrator}
```

## Related kinds
- `input_schema` (P06) -- references enum defs for constrained fields
- `validation_schema` (P06) -- enforces enum constraints on artifact values
- `type_def` (P06) -- composite type definitions that may include enum fields

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_enum_def]] | related | 0.56 |
| [[bld_schema_reranker_config]] | related | 0.44 |
| [[bld_schema_usage_report]] | related | 0.44 |
| [[bld_schema_eval_metric]] | related | 0.43 |
| [[bld_schema_action_paradigm]] | related | 0.43 |
| [[bld_schema_benchmark_suite]] | related | 0.43 |
| [[bld_schema_dataset_card]] | related | 0.42 |
| [[bld_schema_integration_guide]] | related | 0.42 |
| [[bld_schema_multimodal_prompt]] | related | 0.42 |
| [[bld_schema_voice_pipeline]] | related | 0.42 |
