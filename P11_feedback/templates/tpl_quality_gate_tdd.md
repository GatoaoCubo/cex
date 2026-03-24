---
# TEMPLATE: TDD Compliance Quality Gate (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.quality_gate)
# Max 1024 bytes | density_min: 0.80 | quality_min: 8.0

id: p11_qg_tdd_compliance
type: quality_gate
lp: P11
title: "Gate: TDD Compliance"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
quality: 9.0
tags: [tdd, testing, quality-gate, feedback, build]
tldr: "Enforces test-first development: RED verified before code, YAGNI, no RED commits"
density_score: 0.88
---

# Gate: TDD Compliance

## Definition

| Property | Value |
|----------|-------|
| Metric | tdd_compliance_score |
| Threshold | 1.0 (all checks pass) |
| Operator | == |
| Scope | EDISON and ATLAS build satellites |

## Actions

| Result | Action | Escalation |
|--------|--------|------------|
| Pass | Approve commit, proceed to merge | None |
| Fail | Block commit, return to RED phase | Notify satellite owner |

## Checklist

- [ ] Test written BEFORE implementation code (test-first order verified via git diff timeline)
- [ ] RED phase verified: test runs and FAILS before implementation (proves test is meaningful)
- [ ] GREEN phase: minimal code written to pass test (no over-engineering)
- [ ] REFACTOR phase: cleanup without changing behavior (tests still pass)
- [ ] Commit state: GREEN only (no RED commits — every commit has all tests passing)
- [ ] YAGNI: only enough code to pass current test (no speculative features)
- [ ] Tests check behavior, not implementation (WHAT not HOW — no testing private methods)

## Scoring

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| Test-first order | 30% | Git diff shows test file changed before implementation file |
| RED phase evidence | 25% | Test failure output captured before fix |
| YAGNI compliance | 20% | No code exists without a corresponding test driving it |
| Behavior focus | 15% | Tests assert outputs/effects, not internal state |
| Commit hygiene | 10% | Every commit in branch has all tests passing |

## Anti-Patterns (Instant Fail)

- Writing code first, then backfilling tests ("test-after" = not TDD)
- RED phase skipped (test never seen failing = might be vacuously true)
- Testing implementation details (mocking internals, asserting call counts)
- Committing with failing tests ("I'll fix it in the next commit")
- Gold-plating in GREEN phase (adding features no test requires)

## Bypass

- Conditions: Hotfix patches with explicit time constraint (max 24h bypass)
- Approver: STELLA or project owner
- Audit: Bypass logged with reason + follow-up TDD ticket created
