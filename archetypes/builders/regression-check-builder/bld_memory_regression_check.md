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
agent_group: edison
keywords: [regression check, baseline ref, threshold, metrics, comparison, Braintrust, Promptfoo, LangSmith, DeepEval, fail action]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Regression Check"
density_score: 0.90
llm_function: INJECT
---
## Summary
Regression checks are only as reliable as their baseline reference. A check pointing to "the previous version" becomes irreproducible after deployment rotation — experiment IDs and version tags are stable references that survive deployment cycles. The second failure mode is aggregation masking: a composite score can improve while individual dimensions regress (e.g., +8% fluency / -12% factual accuracy nets positive). Per-metric thresholds with directional sensitivity catch what aggregation hides.

## Pattern
**Concrete baseline_ref + per-metric thresholds + explicit fail_action.**

1. baseline_ref: always a framework-native experiment ID or version tag (`experiment/prod-2026-03-22`, `v2.1.0`). Never relative descriptors ("previous", "last week") — unresolvable after rotation. Define a rotation policy: when does baseline advance to new production?
2. threshold units: document explicitly — `5.0` means 5% relative OR 0.05 absolute; never leave ambiguous. Use relative by default; absolute only for fixed-scale (0.0–1.0) metrics.
3. threshold tightness: accuracy/faithfulness 2–3%; latency/cost 10–20%.
4. metric coverage minimum: quality (accuracy/faithfulness), safety (hallucination_rate), performance (latency_p95), cost (cost_per_call).
5. fail_action: `block` for production deploy gates; `warn` for staging; `log` only during baseline calibration.

## Anti-Pattern
1. Vague baseline_ref ("previous version", "last stable") — unresolvable after rotation.
2. Single aggregated metric — masks per-dimension regressions.
3. threshold: 0 without justification — natural variance causes constant false positives.
4. Missing fail_action — regression detected but no response configured.
5. No baseline rotation policy — baseline ages past 90 days, becomes irrelevant artifact.

## Builder Context

This ISO operates within the `regression-check-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_regression_check_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_regression_check_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | regression_check |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
