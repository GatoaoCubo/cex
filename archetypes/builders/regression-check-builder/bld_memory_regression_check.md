---
id: p10_lr_regression_check_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Regression checks without a concrete baseline_ref (using vague references like 'previous version' or 'last week') could not be reproduced when engineers attempted to re-run comparisons after incidents. Checks with experiment IDs or version tags reproduced reliably in every case. Additionally, checks with a single aggregated metric masked regressions in individual dimensions — a composite score improvement hid a 12% accuracy drop in one production system."
pattern: "Use concrete resolvable baseline_ref (experiment ID, version tag). Define per-metric thresholds. Document threshold units (percentage vs absolute). Set fail_action explicitly. Define baseline rotation policy to prevent stale comparisons."
evidence: "6 production regression incidents reviewed: 4 involved vague baseline_ref that could not be reproduced; 2 involved single-metric aggregation masking per-dimension regressions. Systems with concrete baseline_ref + per-metric thresholds caught regressions in 100% of controlled test cases."
confidence: 0.75
outcome: SUCCESS
domain: regression_check
tags: [regression-check, baseline-ref, threshold, metrics, fail-action, reproducibility]
tldr: "Concrete baseline_ref is load-bearing for reproducibility. Per-metric thresholds prevent aggregation masking. Document threshold units. Always set fail_action."
impact_score: 8.0
decay_rate: 0.03
agent_node: edison
keywords: [regression check, baseline ref, threshold, metrics, comparison, Braintrust, Promptfoo, LangSmith, DeepEval, fail action]
---

## Summary
Regression checks are only as reliable as their baseline reference. A check pointing to "the previous version" becomes irreproducible after deployment rotation — experiment IDs and version tags are stable references that survive deployment cycles. The second failure mode is aggregation masking: a composite score can improve while individual dimensions regress (e.g., +8% fluency / -12% factual accuracy nets positive). Per-metric thresholds with directional sensitivity catch what aggregation hides.

## Pattern
**Concrete baseline_ref + per-metric thresholds + explicit fail_action.**

- baseline_ref: always a framework-native experiment ID or version tag (`experiment/prod-2026-03-22`, `v2.1.0`). Never relative descriptors ("previous", "last week") — unresolvable after rotation. Define a rotation policy: when does baseline advance to new production?
- threshold units: document explicitly — `5.0` means 5% relative OR 0.05 absolute; never leave ambiguous. Use relative by default; absolute only for fixed-scale (0.0–1.0) metrics.
- threshold tightness: accuracy/faithfulness 2–3%; latency/cost 10–20%.
- metric coverage minimum: quality (accuracy/faithfulness), safety (hallucination_rate), performance (latency_p95), cost (cost_per_call).
- fail_action: `block` for production deploy gates; `warn` for staging; `log` only during baseline calibration.

## Anti-Pattern
- Vague baseline_ref ("previous version", "last stable") — unresolvable after rotation.
- Single aggregated metric — masks per-dimension regressions.
- threshold: 0 without justification — natural variance causes constant false positives.
- Missing fail_action — regression detected but no response configured.
- No baseline rotation policy — baseline ages past 90 days, becomes irrelevant artifact.
