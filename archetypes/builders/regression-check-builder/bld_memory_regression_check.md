---
id: p10_lr_regression_check_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
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
satellite: edison
keywords: [regression check, baseline ref, threshold, metrics, comparison, Braintrust, Promptfoo, LangSmith, DeepEval, fail action]
---

## Summary
Regression checks are only as reliable as their baseline reference. A check that points to "the previous version" cannot be reproduced after a deployment rotates the codebase — the comparison becomes irreproducible and the check becomes untestable. Experiment IDs and version tags are stable references that survive deployment cycles.

The second critical failure mode is metric aggregation masking. A single composite score can improve while individual dimensions regress. A model change that increases fluency scores 8% while dropping factual accuracy 12% produces a net positive aggregate — but the regression is real and harmful. Per-metric thresholds with directional sensitivity catch what aggregation hides.

## Pattern
**Concrete baseline_ref + per-metric thresholds + explicit fail_action.**

Baseline reference rules:
- Always use a framework-native experiment ID: `experiment/prod-2026-03-22`, `run/abc123`, `v2.1.0`
- Never use relative descriptors: "previous", "last week", "before the change" — unresolvable after rotation
- Document when the baseline was captured and under what conditions
- Define a rotation policy: when does the baseline advance to the new production version?

Threshold rules:
- Document units in the artifact body: `5.0` means 5% relative deviation OR 0.05 absolute — never leave ambiguous
- Use relative thresholds (percentage) by default — they normalize across metric scales
- Use absolute thresholds only when the metric has a fixed known scale (0.0–1.0 scores)
- Tighten accuracy/faithfulness thresholds (2–3%) vs latency/cost (10–20%) — user-facing quality degrades faster than acceptable

Metric coverage minimum for production systems:
- Quality dimension: accuracy, faithfulness, or task-specific correctness score
- Safety dimension: hallucination_rate or groundedness score
- Performance dimension: latency_p95 or latency_p50
- Cost dimension: cost_per_call or tokens_per_request

fail_action rules:
- `block` for production deploy gates — never allow a confirmed regression to ship
- `warn` for staging or non-critical metrics — allows forward progress with visibility
- `log` only during baseline calibration phase — not acceptable for established checks

## Anti-Pattern
- Vague baseline_ref ("previous version", "last stable") — unresolvable, makes check useless after rotation.
- Single aggregated metric — masks per-dimension regressions that matter individually.
- threshold: 0 without justification — natural model variance causes false positives constantly.
- Missing fail_action — regression detected but no response configured; check produces noise only.
- No baseline rotation policy — baseline ages past 90 days and becomes an irrelevant historical artifact.
- Conflating regression_check with benchmark: regression_check requires baseline_ref; if there is no prior experiment to compare against, produce a benchmark instead.

## Context
The 2048-byte body limit for regression_check is generous relative to cli_tool (1024 bytes) because metric documentation requires per-metric threshold, direction, and method — each metric adds ~100 bytes. Budget: Overview (100) + Baseline (300) + Metrics (1200, ~300 per metric) + Failure Protocol (200) = ~1800 bytes for a 4-metric check. A check with more than 6 metrics should consider whether all dimensions are load-bearing or whether some belong in a separate specialized check.
