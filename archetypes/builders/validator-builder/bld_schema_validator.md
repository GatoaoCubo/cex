---
kind: schema
id: bld_schema_validator
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for validator
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_output_validator
  - bld_schema_input_schema
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_smoke_eval
  - bld_schema_guardrail
  - bld_schema_action_prompt
  - bld_schema_runtime_rule
  - bld_schema_retriever_config
  - bld_schema_reranker_config
---

# Schema: validator
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_val_{rule}) | YES | - | Namespace compliance |
| kind | literal "validator" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| rule | string | YES | - | Human-readable rule name |
| conditions | list[object] | YES | - | When this validator fires |
| error_message | string | YES | - | Message on failure |
| severity | enum: error, warning, info | YES | "error" | Failure severity |
| auto_fix | boolean | YES | false | Can system auto-remediate? |
| pre_commit | boolean | YES | false | Runs before commit? |
| threshold | number or null | REC | null | Numeric threshold if applicable |
| bypass | object {conditions, approver} | REC | null | Bypass policy |
| logging | boolean | REC | true | Log validation results? |
| domain | string | YES | - | What artifact kind this validates |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "validator" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |
## Conditions Object
```yaml
conditions:
  - field: "{{field_name}}"
    operator: "{{eq|ne|gt|lt|gte|lte|regex|in|not_in|exists|type_check}}"
    value: "{{expected_value}}"
    target: "{{frontmatter|body|filename}}"
```
Operators: eq, ne, gt, lt, gte, lte, regex, in, not_in, exists, type_check.
Target: frontmatter (default), body, filename.
## Bypass Object
```yaml
bypass:
  conditions: ["{{when_bypass_allowed}}"]
  approver: "{{role_or_name}}"
  audit: true
```
## ID Pattern
Regex: `^p06_val_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Rule Definition` — what is checked, in plain language
2. `## Conditions` — structured conditions table (field, operator, value)
3. `## Error Handling` — error_message, severity, remediation steps
4. `## Bypass Policy` — when bypass is allowed, who approves
## Constraints
- max_bytes: 3072 (body only)
- naming: p06_val_{rule}.yaml
- machine_format: yaml
- id == filename stem
- severity MUST be one of: error, warning, info
- conditions MUST have at least 1 entry
- quality: null always
- validator is pass/fail — no weighted scoring (that is quality_gate P11)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_output_validator]] | sibling | 0.60 |
| [[bld_schema_input_schema]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.58 |
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_smoke_eval]] | sibling | 0.58 |
| [[bld_schema_guardrail]] | sibling | 0.58 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
| [[bld_schema_runtime_rule]] | sibling | 0.57 |
| [[bld_schema_retriever_config]] | sibling | 0.56 |
| [[bld_schema_reranker_config]] | sibling | 0.56 |
