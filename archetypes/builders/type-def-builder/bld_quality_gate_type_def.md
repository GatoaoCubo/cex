---
id: p11_qg_type_def
kind: quality_gate
pillar: P06
title: "Gate: Type Def"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: type_def
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - type-def
  - schema
  - P06
tldr: "Validates reusable type declarations for base type, constraints, serialization, and composition rules."
llm_function: GOVERN
---
## Definition
A type definition ofclares a named, reusable data structure: its base type, constraints, nullable semantics, serialization format, and composition rules. Type defs are consumed by validation schemas, validators, and code generators. This gate ensures every type def is machine-usable, unambiguous, and backward compatible.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p06_td_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `type_def` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `type_name`, `base_type`, `nullable` all defined and non-empty |
| H07 | Base type specified | `base_type` is present and comes from the controlled vocabulary in CONFIG.md |
| H08 | Constraints section present | Body contains a `## Constraints` section with at least one named constraint |
| H09 | Serialization format present | Body contains a `## Serialization` section specifying wire format (JSON, YAML, Protobuf, etc.) |
| H10 | Type name is PascalCase | `type_name` matches `^[A-Z][A-Za-z0-9]*$` |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Definition is tight; no tautological descriptions or repeated field names |
| Constraints are machine-validatable | 1.0 | Each constraint is expressed as a checkable rule (min, max, pattern, enum) |
| Composition rules documented | 1.0 | Union, intersection, or tuple composition is explicit when base_type is composite |
| Nullable semantics explicit | 0.5 | `nullable: true` or `nullable: false` is set; absence is not acceptable |
| Generics parameters documented | 0.5 | If the type is generic, type parameters are named and constrained |
| Tags include type-def | 0.5 | `tags` list contains `"type-def"` |
| Inheritance chain documented | 0.5 | If the type extends another, the parent type is named with a reference |
| Valid and invalid examples | 1.0 | Body contains at least one valid instance and one invalid instance |
| Backward compatibility notes | 0.5 | If version > 1.0.0, breaking changes are listed in body |
| Consumers cross-referenced | 0.5 | Body or frontmatter lists at least one artifact that consumes this type |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as canonical type definition |
| >= 8.0 | PUBLISH — safe to reference in schemas and validators |
| >= 7.0 | REVIEW — usable but constraints or examples need work |
| < 7.0 | REJECT — do not reference; ambiguous or incomplete definition |
## Bypass
| Field | Value |
|-------|-------|
| condition | Bootstrapping a new domain where no controlled vocabulary exists yet and the type is needed to unblock other artifacts |
| approver | Architect responsible for the P06 pillar |
| audit_log | Entry required in `.claude/bypasses/type_def_{date}.md` noting which HARD gates are waived and why |
| expiry | 14 days; type must reach PUBLISH score before any dependent artifact is published |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
