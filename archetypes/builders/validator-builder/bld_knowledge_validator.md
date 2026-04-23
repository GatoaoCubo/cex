---
kind: knowledge_card
id: bld_knowledge_card_validator
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for validator production — atomic searchable facts
sources: validator-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_validator-builder
  - bld_memory_validator
  - p11_qg_validator
  - bld_collaboration_validator
  - bld_examples_validator
  - p03_ins_validator
  - validator-builder
  - bld_schema_validator
  - bld_output_template_validator
  - p01_kc_validator
---

# Domain Knowledge: validator
## Executive Summary
A `validator` (P06) is a deterministic, binary (pass/fail) technical check applied to an artifact before acceptance. It differs from `quality_gate` (weighted scoring 0–10), `scoring_rubric` (subjective evaluation), and `validation_schema` (silent post-generation contract) by being an explicit named rule with structured conditions, severity, and optional bypass policy. Validators enforce contracts; they do not measure quality.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 |
| Kind | `validator` |
| ID pattern | `^p06_val_[a-z][a-z0-9_]+$` |
| Naming | `p06_val_{rule}.yaml` |
| Max body | 3072 bytes |
| Machine format | yaml |
| Required frontmatter fields | 14 |
| Recommended fields | 4 |
| `severity` values | `error`, `warning`, `info` |
| `quality` field | always `null` |
| Result | pass/fail — no weighted scoring |
## Patterns
| Pattern | Rule |
|---------|------|
| Deterministic | Same input always produces same result — no randomness |
| Binary result | Pass or fail only — never a score, never a percentage |
| Composable | Multiple validators chain; all must pass for acceptance |
| Actionable error messages | Tell what to fix, not just what failed |
| Conditions as triples | Each condition: `(field, operator, value)` + optional `target` |
| `pre_commit: true` | Validator fires before git commit for that artifact kind |
| `auto_fix: true` | Only for safe, lossless repairs (casing, formatting, whitespace) |
| Bypass requires audit | `bypass.audit: true` always; `approver` names the authorizing role |
**Condition operators**:
| Operator | Use case |
|----------|----------|
| `eq` / `ne` | Exact match / mismatch |
| `gt` / `lt` / `gte` / `lte` | Numeric thresholds |
| `regex` | Pattern matching (IDs, naming) |
| `in` / `not_in` | Enum membership |
| `exists` | Field presence check |
| `type_check` | Type conformance |
**Condition targets**: `frontmatter` (default), `body`, `filename`
**Boundary — what validator is NOT**:
| kind | Why NOT validator |
|------|-----------------|
| `quality_gate` | Weighted scoring 0–10; validators are binary |
| `scoring_rubric` | Subjective criteria; validators are objective |
| `validation_schema` | Silent system contract; validators are explicit named rules |
| `input_schema` | Defines input shape; validators check rule conformance |
| `guardrail` | Behavioral safety limits; validators check data fields |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Numeric score in result | Validators are binary — scoring belongs in `quality_gate` |
| Empty `conditions` list | Schema HARD gate: at least 1 condition required |
| Vague `error_message` ("invalid") | Not actionable; user cannot fix without knowing what failed |
| `auto_fix: true` on lossy changes | Data loss is unsafe; auto-fix only for lossless repairs |
| `bypass` without `audit: true` | No governance trail; exception is untracked |
| `quality` set to a score | Never self-score; governance assigns |
| `id` not matching filename stem | Schema constraint violated; indexing breaks |
## Application
1. Name the rule in `rule` field (human-readable, e.g. `"id_namespace_compliance"`)
2. Set `id` = `p06_val_{rule_snake}`, must equal filename stem
3. Set `domain` to the artifact kind this validator governs
4. Set `severity`: `error` blocks, `warning` flags, `info` logs only
5. Set `pre_commit: true` if this fires before commit; `false` if post-acceptance
6. Write `conditions` list: at least 1 triple of `(field, operator, value)` with optional `target`
7. Write `error_message`: actionable — what to fix, not just what failed
8. Decide `auto_fix`: only `true` if repair is lossless and safe
9. If bypass is needed: define `bypass.conditions`, `bypass.approver`, `bypass.audit: true`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_validator-builder]] | downstream | 0.50 |
| [[bld_memory_validator]] | downstream | 0.48 |
| [[p11_qg_validator]] | downstream | 0.46 |
| [[bld_collaboration_validator]] | downstream | 0.46 |
| [[bld_examples_validator]] | downstream | 0.45 |
| [[p03_ins_validator]] | downstream | 0.44 |
| [[validator-builder]] | downstream | 0.43 |
| [[bld_schema_validator]] | downstream | 0.41 |
| [[bld_output_template_validator]] | downstream | 0.41 |
| [[p01_kc_validator]] | sibling | 0.39 |
