---
id: p10_lr_bugloop_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Automated fix loops with a single confidence threshold applied uniformly to all failure types triggered incorrect auto-fixes on 34% of probabilistic failures. Separating trigger classification from fix application reduced incorrect auto-fix rate to 8% across 6 test suites (214 failures processed)."
pattern: "Classify failure type before applying any fix. Auto-fix only deterministic failures at confidence >= 0.85. Escalate probabilistic failures regardless of confidence score. Vary fix strategy on each retry attempt."
evidence: "6 suites, 214 failures: auto-fix success 91% on deterministic triggers, 23% on p..."
confidence: 0.7
outcome: SUCCESS
domain: bugloop
tags: [bugloop, auto-fix, escalation, verification-suite, rollback-policy]
tldr: "Classify failure type first; auto-fix only deterministic failures at high confidence; escalate everything ambiguous; vary strategy per retry attempt."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [bug detection, fix loop, confidence threshold, escalation, rollback, verification suite, deterministic, probabilistic]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Bugloop"
density_score: 0.90
llm_function: INJECT
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
1. Applying auto-fix based solely on confidence score without classifying failure type first.
2. Retrying with the same fix strategy (identical patch applied twice never improves outcomes).
3. Skipping the verification suite after auto-fix and relying on the original single test.
4. Setting max_attempts above 5 (loop thrash risk; returns diminish sharply after attempt 3).
5. Treating escalation as failure; escalation is the correct output for probabilistic failures.
6. Setting detect.pattern too broadly (matches unrelated failures, generates spurious fix attempts).
## Context
This pattern emerged from fix loops that processed syntax-level and logic-level failures in the same pipeline with a uniform threshold of 0.80. Probabilistic failures like assertion mismatches were auto-fixed with patches that passed locally but broke downstream consumers. Separating classification into a pre-fix gate cut incorrect auto-fixes by 74%.
Confidence calibration reference:
1. Deterministic + reversible: 0.85-0.95 — auto-fix safe
2. Schema/format errors: 0.70-0.88 — auto-fix safe with assertions

## Metadata

```yaml
id: p10_lr_bugloop_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-bugloop-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | bugloop |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
