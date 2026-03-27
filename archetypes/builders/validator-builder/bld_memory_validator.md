---
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for validator artifact generation
---

# Memory: validator-builder

## Summary

Validators are individual pass/fail technical checks with structured conditions (field/operator/value), severity levels, and optional auto-fix policies. The critical production lesson is severity calibration — marking everything as error severity causes validation fatigue, where developers bypass validators entirely. The tiered approach (error blocks, warning notifies, info logs) maintains compliance without fatigue. The second lesson is auto-fix safety: auto-fix must only apply to deterministic corrections where the fix is provably correct.

## Pattern

- Conditions must be structured: field + operator + expected value — not prose descriptions
- Severity must be tiered: error (blocks), warning (notifies, does not block), info (logs silently)
- Reserve error severity for true blockers — overuse causes bypass behavior
- Auto-fix must be deterministic: only fix when the correct value is unambiguous (trim whitespace, fix casing)
- Bypass policy must require explicit justification logged in audit trail — no silent bypasses
- Each validator should test exactly one thing — compound validators that check multiple conditions are hard to debug

## Anti-Pattern

- All validators set to error severity — causes validation fatigue and mass bypass behavior
- Prose-based conditions ("check that the name looks right") — not machine-evaluable
- Auto-fix for ambiguous corrections — fixing "approximately 10" to 10 vs 10.0 is not deterministic
- Compound validators checking 3+ conditions — when one fails, unclear which condition caused the failure
- Confusing validator (P06, individual pass/fail) with quality_gate (P11, aggregate scoring) or scoring_rubric (P07, weighted evaluation)
- Missing audit trail on bypasses — bypassed validators provide no governance value

## Context

Validators operate in the P06 spec layer as atomic technical checks. They are consumed by quality gates (P11) that aggregate multiple validator results into ship/no-ship decisions. In pre-commit pipelines, validators run automatically on every artifact change, providing immediate feedback. The key design principle is that each validator checks exactly one condition — composition happens at the quality gate level.

## Impact

Tiered severity (error/warning/info) reduced bypass rates from 30% to under 5%. Structured conditions enabled 100% automation of validator execution. Single-condition validators reduced debugging time by 50% compared to compound validators.

## Reproducibility

Reliable validator production: (1) define one condition per validator as field/operator/value, (2) set severity appropriately (error only for true blockers), (3) add auto-fix only for deterministic corrections, (4) define bypass policy with audit requirements, (5) provide clear error messages, (6) validate against 9 HARD + 10 SOFT gates.

## References

- validator-builder SCHEMA.md (22 frontmatter fields, condition specification)
- P06 spec pillar specification
- Pre-commit validation and severity calibration patterns
