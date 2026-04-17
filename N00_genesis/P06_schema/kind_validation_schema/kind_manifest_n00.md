---
id: n00_validation_schema_manifest
kind: knowledge_card
pillar: P06
nucleus: n00
title: "Validation Schema -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, validation_schema, p06, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Validation schema defines the post-generation contract that LLM output or pipeline data must satisfy before it is accepted. It specifies the full structural, semantic, and business-rule constraints as a declarative schema (JSON Schema, Pydantic model, or Zod definition). Unlike input_schema (which validates what goes IN), validation_schema governs what comes OUT of a generation or transformation step.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `validation_schema` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Target artifact type + "Validation Schema" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_kind | string | yes | The CEX kind this schema validates |
| schema_format | enum | yes | json_schema / pydantic / zod / cerberus |
| required_fields | list | yes | Fields that must be present and non-null |
| field_constraints | list | yes | Per-field constraints (type, pattern, range) |
| custom_validators | list | no | Named custom validation functions |

## When to use
- Defining the acceptance criteria for LLM-generated artifact output
- Building a quality gate that rejects structurally incomplete or semantically wrong output
- Providing the declarative schema that an output_validator enforces at runtime

## Builder
`archetypes/builders/validation_schema-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind validation_schema --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering + N05 operations co-define validation schemas
- `{{SIN_LENS}}` -- Gating Wrath: strict, explicit, no ambiguous acceptance criteria
- `{{TARGET_AUDIENCE}}` -- output_validator at F7 GOVERN consuming this schema
- `{{DOMAIN_CONTEXT}}` -- artifact type, quality requirements, regulatory constraints

## Example (minimal)
```yaml
---
id: validation_schema_knowledge_card
kind: validation_schema
pillar: P06
nucleus: n03
title: "Knowledge Card Validation Schema"
version: 1.0
quality: null
---
target_kind: knowledge_card
schema_format: pydantic
required_fields: [id, kind, pillar, nucleus, title, version, quality]
field_constraints:
  - {field: quality, type: float_or_null, min: 0.0, max: 10.0}
  - {field: version, pattern: "^\\d+\\.\\d+$"}
```

## Related kinds
- `input_schema` (P06) -- pre-processing contract; validation_schema is post-generation
- `output_validator` (P05) -- runtime enforcer that consumes this schema
- `validator` (P06) -- reusable validation rule referenced by this schema
