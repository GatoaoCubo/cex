---
id: n00_type_def_manifest
kind: knowledge_card
8f: F3_inject
pillar: P06
nucleus: n00
title: "Type Def -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, type_def, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_architecture_type_def
  - bld_schema_reranker_config
  - bld_schema_input_schema
  - bld_schema_integration_guide
  - bld_collaboration_type_def
  - bld_schema_multimodal_prompt
  - type-def-builder
  - bld_schema_dataset_card
  - bld_schema_thinking_config
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Type def produces a custom type definition that extends the base type system with domain-specific composite types, aliases, or branded primitives. Type defs are referenced by input schemas, validation schemas, and interfaces to enforce semantic correctness beyond simple primitive types. They serve as the vocabulary of the CEX domain type system.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `type_def` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Type name in PascalCase |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| type_name | string | yes | Canonical type name used in schema references |
| base_type | string | yes | Primitive or composed type being extended |
| fields | list | no | For composite types: field definitions |
| constraints | list | no | Validation constraints (min, max, pattern, etc.) |
| serialization | string | no | How to serialize/deserialize this type |

## When to use
- Defining a domain-specific type that appears across multiple schemas (e.g., KindId, SemVer, NucleusId)
- Creating a branded primitive that prevents accidental assignment of wrong-domain values
- Establishing a composite record type shared across input and validation schemas

## Builder
`archetypes/builders/type_def-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind type_def --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering defines type vocabulary
- `{{SIN_LENS}}` -- Inventive Pride: expressive, minimal, no redundant types
- `{{TARGET_AUDIENCE}}` -- schemas, validators, and SDK generators consuming the type
- `{{DOMAIN_CONTEXT}}` -- domain, type stability, serialization requirements

## Example (minimal)
```yaml
---
id: type_def_quality_score
kind: type_def
pillar: P06
nucleus: n03
title: "QualityScore"
version: 1.0
quality: null
---
type_name: QualityScore
base_type: float
constraints:
  - {min: 0.0, max: 10.0}
  - {nullable: true, meaning: "not yet peer-reviewed"}
```

## Related kinds
- `enum_def` (P06) -- constrained string/int type; type_def is for composite or branded types
- `input_schema` (P06) -- schema that uses type_def in field definitions
- `validation_schema` (P06) -- enforces type_def constraints at runtime

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_type_def]] | downstream | 0.40 |
| [[bld_schema_reranker_config]] | related | 0.38 |
| [[bld_schema_input_schema]] | related | 0.38 |
| [[bld_schema_integration_guide]] | related | 0.38 |
| [[bld_collaboration_type_def]] | related | 0.38 |
| [[bld_schema_multimodal_prompt]] | related | 0.38 |
| [[type-def-builder]] | related | 0.38 |
| [[bld_schema_dataset_card]] | related | 0.37 |
| [[bld_schema_thinking_config]] | related | 0.37 |
| [[bld_schema_search_strategy]] | related | 0.37 |
