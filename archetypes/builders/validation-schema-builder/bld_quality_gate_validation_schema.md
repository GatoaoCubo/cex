---
id: p11_qg_validation_schema
kind: quality_gate
pillar: P06
title: "Gate: Validation Schema"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: validation_schema
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - validation-schema
  - contract
  - P06
tldr: "Validates post-generation contracts for field types, constraints, on_failure strategy, and system-only scope."
llm_function: GOVERN
---
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
