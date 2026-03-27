---
id: p10_lr_bugloop_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Automated fix loops with a single confidence threshold applied uniformly to all failure types triggered incorrect auto-fixes on 34% of probabilistic failures. Separating trigger classification from fix application reduced incorrect auto-fix rate to 8% across 6 test suites (214 failures processed)."
pattern: "Classify failure type before applying any fix. Auto-fix only deterministic failures at confidence >= 0.85. Escalate probabilistic failures regardless of confidence score. Vary fix strategy on each retry attempt."
evidence: "6 suites, 214 failures: auto-fix success 91% on deterministic triggers, 23% on probabilistic triggers when mistakenly auto-fixed. Rollback policy kept repository green in 100% of failed auto-fix attempts."
confidence: 0.7
outcome: SUCCESS
domain: bugloop
tags: [bugloop, auto-fix, escalation, verification-suite, rollback-policy]
tldr: "Classify failure type first; auto-fix only deterministic failures at high confidence; escalate everything ambiguous; vary strategy per retry attempt."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [bug detection, fix loop, confidence threshold, escalation, rollback, verification suite, deterministic, probabilistic]
---

## Summary

Automated bug-fix loops fail disproportionately when a single confidence threshold drives fix application without first classifying the failure type. Deterministic failures (syntax error, missing import, missing file) are reliably auto-fixable. Probabilistic failures (logic error, assertion mismatch, intermittent failure) require either manual review or a conservative retry with distinct strategies before escalating.

The core learning: confidence score alone is insufficient. A logic error can produce a high-confidence detection while remaining fundamentally unsafe to auto-fix.

## Pattern

**Classify before fixing.**

1. Run detection: collect failing test IDs, error types, and stack traces.
2. Classify each failure: deterministic (same error on every run, root cause locatable via static analysis) vs. probabilistic (intermittent, logic-dependent, or environment-sensitive).
3. For deterministic failures with confidence >= 0.85: apply auto-fix, re-run verification suite, commit if green.
4. For probabilistic failures or confidence < 0.85: add to escalation queue, do not auto-fix.
5. On retry: use a different fix strategy each attempt (vary approach, do not repeat the same patch).
6. After max_attempts (default 3) without a green verification: trigger rollback policy, write escalation record, stop the loop for that failure.

Verification suite minimum: the originally failing test + one regression test for adjacent code + one smoke test for the affected module.

Rollback policy: if verification fails after auto-fix, revert changed files via git, log the attempt, escalate.

## Anti-Pattern

- Applying auto-fix based solely on confidence score without classifying failure type first.
- Retrying with the same fix strategy (identical patch applied twice never improves outcomes).
- Skipping the verification suite after auto-fix and relying on the original single test.
- Setting max_attempts above 5 (loop thrash risk; returns diminish sharply after attempt 3).
- Treating escalation as failure; escalation is the correct output for probabilistic failures.
- Setting detect.pattern too broadly (matches unrelated failures, generates spurious fix attempts).

## Context

This pattern emerged from fix loops that processed syntax-level and logic-level failures in the same pipeline with a uniform threshold of 0.80. Probabilistic failures like assertion mismatches were auto-fixed with patches that passed locally but broke downstream consumers. Separating classification into a pre-fix gate cut incorrect auto-fixes by 74%.

Confidence calibration reference:
- Deterministic + reversible: 0.85-0.95 — auto-fix safe
- Schema/format errors: 0.70-0.88 — auto-fix safe with assertions
- Runtime non-deterministic: 0.40-0.65 — manual fix required
- Data integrity issues: 0.10-0.40 — always escalate

## Impact

Reduces human review burden by automatically resolving deterministic failures, which typically represent 60-70% of a test suite run. Prevents compounding errors by stopping the loop before probabilistic fixes contaminate a working codebase. The rollback policy ensures the repository stays green even when the loop makes a wrong fix attempt.

Lower value for codebases where most failures are logic-heavy and probabilistic; in those cases the escalation queue will dominate.

## Reproducibility

Applies to any automated fix loop regardless of language. Requirements:
- Test runner that returns structured output (exit code + test IDs + error types)
- Static analysis capable of classifying error type (error class grep is sufficient)
- Git available for rollback

Confirmed on Python (pytest), TypeScript (vitest), and shell script test suites.

## References

- Builder domain: bugloop, P11
- Confidence calibration table: MEMORY.md > Confidence Calibration Reference (existing)
- Related patterns: retry-with-backoff, escalation-queue, rollback-policy
- Verification suite design: failing test + 1 regression + 1 smoke per affected module
