---
kind: schema
id: bld_schema_validation_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for validation_schema
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: "2.0.0"
quality: 9.1
title: "Schema Validation Schema"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_input_schema
  - bld_schema_unit_eval
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_function_def
  - bld_schema_enum_def
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_retriever_config
  - bld_schema_memory_scope
---

# Schema: validation_schema
Derivation hierarchy: **SCHEMA (P06) > TEMPLATE (P03) > CONFIG (P04)**
Schema is upstream. Template/config must not define fields schema does not know.
## Frontmatter Fields
### Required (13)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_vs_{scope}) | YES | — | Namespace compliance |
| kind | literal "validation_schema" | YES | — | Type integrity |
| pillar | literal "P06" | YES | — | Pillar assignment |
| title | string "Validation Schema: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind this schema validates |
| on_failure | enum: reject, warn, auto_fix | YES | — | System behavior when validation fails |
| domain | string | YES | — | Domain this schema covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3, includes "validation-schema" | YES | — | Classification |
### Recommended (6)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| tldr | string <= 160ch | REC | — | Dense summary |
| format | enum: json, yaml | REC | — | Expected output format |
| fields_count | integer >= 1 | REC | — | Number of validated fields |
| strict | boolean | REC | false | If true, reject unknown fields |
| coercion | boolean | REC | false | Auto-coerce types before validation |
| density_score | float 0.80-1.00 | REC | — | Content density |
## Type Enum
Fields MUST use JSON-compatible types only:
| Type | Description |
|------|-------------|
| string | Text values |
| integer | Whole numbers |
| number | Decimal numbers |
| boolean | true/false |
| array | Ordered list |
| object | Key-value map |
## Fields Object
```yaml
fields:
  - name: "{{field_name}}"
    type: "{{string|integer|number|boolean|array|object}}"
    required: {{true|false}}
    constraints:
      min_length: {{integer}}
      max_length: {{integer}}
      pattern: "{{regex}}"
      enum: [{{value_1}}, {{value_2}}]
      min: {{number}}
      max: {{number}}
```
## Body Structure (3 required sections)
1. **Fields Table** — name, type, required, constraints per field
   - Split into Required (HARD gate) and Recommended (SOFT gate) tables
   - All 5 columns mandatory per row: Field, Type, Required, Default, Notes
   - Default = `--` for required fields
2. **Failure Handling** — on_failure behavior per field, error messages, remediation
   - `reject`: block artifact (critical fields: id, kind)
   - `warn`: log, allow through (recommended fields, style)
   - `auto_fix`: coerce value (safe conversions only, e.g. string "42" -> int 42)
3. **Constraints** — max_bytes, naming pattern, id rules, integration notes
## Constraints
- max_bytes: 4096 (body only) — builder files max 4428B, previous 3072 limit was insufficient
- naming: p06_vs_{scope}.yaml
- machine_format: json
- id == filename stem
- on_failure MUST be one of: reject, warn, auto_fix
- LLM NEVER sees this schema — system-side only
- quality: null always
- Type values MUST be JSON-compatible (string, integer, number, boolean, array, object)
## ID Pattern
Regex: `^p06_vs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | sibling | 0.60 |
| [[bld_schema_unit_eval]] | sibling | 0.53 |
| [[bld_schema_smoke_eval]] | sibling | 0.53 |
| [[bld_schema_golden_test]] | sibling | 0.52 |
| [[bld_schema_function_def]] | sibling | 0.52 |
| [[bld_schema_enum_def]] | sibling | 0.51 |
| [[bld_schema_reranker_config]] | sibling | 0.51 |
| [[bld_schema_dataset_card]] | sibling | 0.51 |
| [[bld_schema_retriever_config]] | sibling | 0.51 |
| [[bld_schema_memory_scope]] | sibling | 0.50 |
