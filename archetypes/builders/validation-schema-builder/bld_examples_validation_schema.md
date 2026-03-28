---
kind: examples
id: bld_examples_validation_schema
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of validation_schema artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: validation-schema-builder
## Golden Example
INPUT: "Cria validation_schema para knowledge_card output"
OUTPUT:
```yaml
id: p06_vs_knowledge_card
kind: validation_schema
pillar: P06
title: "Validation Schema: Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
format: "yaml"
fields_count: 8
on_failure: "reject"
strict: false
domain: "knowledge"
quality: null
tags: [validation-schema, knowledge-card, post-generation, P06]
tldr: "Post-generation schema for KCs: enforces id, kind, pillar, quality null, tags list, tldr length, density threshold"
coercion: false
error_template: "KC validation: {{field}} failed — {{reason}}"
density_score: 0.90
linked_artifacts:
  primary: "knowledge-card-builder"
  related: [p06_val_kc_quality_null, p11_qg_kc_publish]
## Schema Overview
Validates knowledge_card artifacts AFTER LLM generation, BEFORE pool acceptance.
Enforces structural correctness: required fields, types, format constraints.
The LLM does NOT see this schema — it is applied by the validation pipeline.
## Fields
| Field | Type | Required | Constraints | Error message |
|-------|------|----------|-------------|---------------|
| id | string | yes | pattern: ^p01_kc_[a-z][a-z0-9_]+$ | id must match p01_kc_ prefix pattern |
| kind | string | yes | enum: [knowledge_card] | kind must be "knowledge_card" |
| pillar | string | yes | enum: [P01] | pillar must be "P01" |
| quality | null | yes | eq: null | quality must be null — never self-score |
| tags | array | yes | min_length: 3 | tags must be list with >= 3 items |
| tldr | string | yes | max_length: 160 | tldr must be <= 160 characters |
| version | string | yes | pattern: ^\d+\.\d+\.\d+$ | version must be valid semver |
| author | string | yes | min_length: 1 | author must be non-empty |
## Failure Handling
- **on_failure**: reject — KCs with structural errors are not accepted
- **strict**: false — extra fields are allowed (extensible schema)
- **coercion**: false — types must match exactly (no string-to-int conversion)
- **error_template**: "KC validation: {{field}} failed — {{reason}}"
- **remediation**: Fix the failing field per error message, re-submit
## Integration
- **Pipeline position**: after LLM generation, before pool acceptance
- **Applied by**: validate_kc.py (HARD gates section)
- **Input**: raw KC output (yaml frontmatter + markdown body)
- **Output**: validated KC or rejection with field-level errors
## References
- P01_knowledge/_schema.yaml: field definitions for knowledge_card
- validate_kc.py v2.0: reference implementation of KC validation
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p06_vs_ pattern (H02 pass)
- kind: validation_schema (H04 pass)
- 17 required fields present (H07 pass)
- fields_count 8 >= 1 (H08 pass)
- on_failure "reject" in valid enum (H09 pass)
- format "yaml" in valid enum (H10 pass)
- target_kind non-empty (H11 pass)
- Fields table with all 8 fields, typed, constrained (S03 pass)
- Failure Handling section with remediation (S04 pass)
- Integration section with pipeline position (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
## Anti-Example
INPUT: "Schema para validar coisas"
BAD OUTPUT:
```yaml
id: output_schema
kind: schema
pillar: Schema
format: text
fields_count: 0
on_failure: maybe
quality: 9.0
tags: schema
## Validation
Check that the output looks correct.
If it doesn't look right, try again.
```
FAILURES:
1. id: no p06_vs_ prefix -> H02 FAIL
2. kind: "schema" not "validation_schema" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H05 FAIL
4. quality: 9.0 (not null) -> H06 FAIL
5. fields_count: 0 < 1 minimum -> H08 FAIL
6. on_failure: "maybe" not in enum -> H09 FAIL
7. format: "text" not in [json, yaml] -> H10 FAIL
8. target_kind: missing -> H11 FAIL
9. tags: string not list, len < 3 -> S02 FAIL
