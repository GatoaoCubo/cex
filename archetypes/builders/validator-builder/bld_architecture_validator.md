---
kind: architecture
id: bld_architecture_validator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of validator — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - validator-builder
  - bld_architecture_quality_gate
  - p01_kc_validator
  - output-validator-builder
  - bld_collaboration_validator
  - p11_qg_validator
  - bld_examples_validator
  - bld_memory_validator
  - p03_sp_validator-builder
  - bld_collaboration_output_validator
---

# Architecture: validator in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22-field metadata header (id, kind, pillar, domain, target_kind, severity, etc.) | validator-builder | active |
| conditions | Structured check rules (field, operator, value) that define pass/fail | author | active |
| severity_level | Classification of violation impact: error, warning, or info | author | active |
| auto_fix_policy | Whether violations can be automatically repaired and how | author | active |
| bypass_policy | Conditions under which the validator can be skipped with audit | author | active |
| audit_trail | Logging requirements for validation runs and bypass events | author | active |
## Dependency Graph
```
artifact (any)  --checked_by-->  validator  --produces-->    pass_fail_result
quality_gate    --depends-->     validator  --signals-->     validation_event
validator       --depends-->     type_def
```
| From | To | Type | Data |
|------|----|------|------|
| artifact (any) | validator | data_flow | artifact submitted for validation check |
| validator | pass_fail_result | produces | boolean pass/fail with severity and message |
| quality_gate (P11) | validator | dependency | gates compose validators as hard check components |
| type_def (P06) | validator | dependency | type definitions inform field and constraint checks |
| validator | validation_event (P12) | signals | emitted on pass, fail, or bypass |
| law (P08) | validator | dependency | laws may mandate specific validation rules |
## Boundary Table
| validator IS | validator IS NOT |
|--------------|-----------------|
| A technical pass/fail check with structured conditions | A multi-dimensional scoring framework (scoring_rubric P07) |
| Classified by severity (error/warning/info) | A quality barrier with scoring formula (quality_gate P11) |
| Supports auto_fix for recoverable violations | A post-generation schema contract (validation_schema P06) |
| Includes bypass policy with audit trail | An input contract for operations (input_schema P06) |
| Applied to individual rules — atomic checks | A reusable type declaration (type_def P06) |
| Runs at pre-commit or pre-promotion checkpoints | A response format instruction for the LLM (response_format P05) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | artifact, type_def | Artifact under check and type constraints |
| Rules | frontmatter, conditions, severity_level | Define what is checked and how severe violations are |
| Remediation | auto_fix_policy, bypass_policy | Handle violations via fix or approved skip |
| Audit | audit_trail | Log validation runs and bypass events |
| Output | pass_fail_result, validation_event, quality_gate | Deliver result and feed into quality gates |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[validator-builder]] | upstream | 0.54 |
| [[bld_architecture_quality_gate]] | sibling | 0.47 |
| [[p01_kc_validator]] | upstream | 0.45 |
| [[output-validator-builder]] | upstream | 0.42 |
| [[bld_collaboration_validator]] | upstream | 0.41 |
| [[p11_qg_validator]] | upstream | 0.41 |
| [[bld_examples_validator]] | upstream | 0.40 |
| [[bld_memory_validator]] | downstream | 0.40 |
| [[p03_sp_validator-builder]] | upstream | 0.39 |
| [[bld_collaboration_output_validator]] | downstream | 0.37 |
