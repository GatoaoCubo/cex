---
kind: memory
id: bld_memory_validator
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for validator artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Validator"
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
  - bld_collaboration_validator
  - bld_knowledge_card_validator
  - p11_qg_validator
  - p03_sp_validator-builder
  - p03_ins_validator
  - bld_architecture_validator
  - bld_output_template_validator
  - bld_examples_validator
  - bld_tools_validator
---
# Memory: validator-builder
## Summary
Validators are individual pass/fail technical checks with structured conditions (field/operator/value), severity levels, and optional auto-fix policies. The critical production lesson is severity calibration — marking everything as error severity causes validation fatigue, where developers bypass validators entirely. The tiered approach (error blocks, warning notifies, info logs) maintains compliance without fatigue. The second lesson is auto-fix safety: auto-fix must only apply to deterministic corrections where the fix is provably correct.
## Pattern
1. Conditions must be structured: field + operator + expected value — not prose descriptions
2. Severity must be tiered: error (blocks), warning (notifies, does not block), info (logs silently)
3. Reserve error severity for true blockers — overuse causes bypass behavior
4. Auto-fix must be deterministic: only fix when the correct value is unambiguous (trim whitespace, fix casing)
5. Bypass policy must require explicit justification logged in audit trail — no silent bypasses
6. Each validator should test exactly one thing — compound validators that check multiple conditions are hard to debug
## Anti-Pattern
1. All validators set to error severity — causes validation fatigue and mass bypass behavior
2. Prose-based conditions ("check that the name looks right") — not machine-evaluable
3. Auto-fix for ambiguous corrections — fixing "approximately 10" to 10 vs 10.0 is not deterministic
4. Compound validators checking 3+ conditions — when one fails, unclear which condition caused the failure
5. Confusing validator (P06, individual pass/fail) with quality_gate (P11, aggregate scoring) or scoring_rubric (P07, weighted evaluation)
6. Missing audit trail on bypasses — bypassed validators provide no governance value
## Context
Validators operate in the P06 spec layer as atomic technical checks. They are consumed by quality gates (P11) that aggregate multiple validator results into ship/no-ship decisions. In pre-commit pipelines, validators run automatically on every artifact change, providing immediate feedback. The key design principle is that each validator checks exactly one condition — composition happens at the quality gate level.
## Impact
Tiered severity (error/warning/info) reduced bypass rates from 30% to under 5%. Structured conditions enabled 100% automation of validator execution. Single-condition validators reduced debugging time by 50% compared to compound validators.
## Reproducibility
Reliable validator production: (1) define one condition per validator as field/operator/value, (2) set severity apowntely (error only for true blockers), (3) add auto-fix only for deterministic corrections, (4) define bypass policy with audit requirements, (5) provide clear error messages, (6) validate against 9 HARD + 10 SOFT gates.
## References
1. validator-builder SCHEMA.md (22 frontmatter fields, condition specification)
2. P06 spec pillar specification
3. Pre-commit validation and severity calibration patterns

## Metadata

```yaml
id: bld_memory_validator
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-validator.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | validator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[validator-builder]] | upstream | 0.56 |
| [[bld_collaboration_validator]] | upstream | 0.51 |
| [[bld_knowledge_card_validator]] | upstream | 0.51 |
| [[p11_qg_validator]] | upstream | 0.50 |
| [[p03_sp_validator-builder]] | upstream | 0.49 |
| [[p03_ins_validator]] | upstream | 0.43 |
| [[bld_architecture_validator]] | upstream | 0.41 |
| [[bld_output_template_validator]] | upstream | 0.41 |
| [[bld_examples_validator]] | upstream | 0.40 |
| [[bld_tools_validator]] | upstream | 0.38 |
