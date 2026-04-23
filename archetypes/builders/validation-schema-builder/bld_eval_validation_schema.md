---
kind: quality_gate
id: p11_qg_validation_schema
pillar: P06
llm_function: GOVERN
purpose: Golden and anti-examples of validation_schema artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Validation Schema'
version: 1.0.0
author: builder
tags:
- eval
- P06
- quality_gate
- examples
tldr: Validates post-generation contracts for field types, constraints, on_failure
  strategy, and system-only scope.
domain: validation_schema
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - bld_examples_validation_schema
  - bld_knowledge_card_validation_schema
  - p03_ins_validation_schema
  - bld_collaboration_validation_schema
  - p03_sp_validation-schema-builder
  - bld_schema_validation_schema
  - p11_qg_validator
  - bld_instruction_input_schema
  - p11_qg_input_schema
  - bld_memory_validation_schema
---

## Quality Gate

## Definition
A validation schema is a post-generation contract applied by the system after an artifact is produced. It defines fields, types, constraints, and violation behavior (reject, warn, auto-fix). The model never sees this schema; the pipeline enforces it. This gate ensures every validation schema is machine-enforceable, clearly bounded, and safe to apply automatically.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p06_vs_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `validation_schema` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `target_kind`, `fields`, `on_failure` all defined and non-empty |
| H07 | Fields list with types | `fields` contains at least one entry with `name`, `type`, and `required` |
| H08 | Constraint definitions per field | Each field in `fields` includes at least one named constraint |
| H09 | on_failure is valid enum | `on_failure` per field is one of: `reject`, `warn`, `auto_fix` |
| H10 | Field types are JSON Schema primitives | Types limited to: `string`, `integer`, `number`, `boolean`, `array`, `object` |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | No prose restating what the field table already shows |
| Constraints are machine-enforceable | 1.0 | Each constraint is checkable by a program without LLM interpretation |
| on_failure justified per field | 1.0 | Each `on_failure` choice has a brief reason |
| Tags include validation-schema | 0.5 | `tags` contains `"validation-schema"` |
| Scope boundary explicit | 1.0 | Body states model never sees this schema; pipeline-only |
| Coercion rules for auto_fix | 0.5 | `on_failure: auto_fix` fields document the exact coercion |
| Error messages are human-readable | 1.0 | Each failure produces a message a developer can act on |
| Backward compatibility noted | 0.5 | Body notes stable vs. change-prone fields across versions |
| No confusion with response_format | 0.5 | Body distinguishes this from P05 response format artifacts |
| Target kind is specific | 1.0 | `target_kind` names one artifact kind, not a generic scope |
Sum of weights: 8.0. `soft_score = sum(weight * gate_score) / 8.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as canonical validation contract |
| >= 8.0 | PUBLISH — safe to apply in production generation pipelines |
| >= 7.0 | REVIEW — applicable but coercion rules or boundary need clarification |
| < 7.0 | REJECT — do not apply; constraints are ambiguous or on_failure is inconsistent |
## Bypass
| Field | Value |
|-------|-------|
| condition | Target kind is new with no prior instances; schema is a best-effort draft |
| approver | Engineer responsible for the target kind's builder |
| audit_log | Entry in `.claude/bypasses/validation_schema_{date}.md` listing unvalidated fields |
| expiry | 30 days or until 10 instances of the target kind exist |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

## Examples

# Examples: validation-schema-builder
## Golden Example
INPUT: "Create validation_schema para knowledge_card output"
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
