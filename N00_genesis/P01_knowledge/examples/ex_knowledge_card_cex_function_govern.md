---
id: p01_kc_cex_function_govern
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function GOVERN — Quality Inspection and System Governance"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [cex, llm-function, govern, quality-gate, shokunin, evals, benchmark]
tldr: "GOVERN evaluates and controls quality via 22 types (28% of CEX) — the largest function, pipeline Shokunin"
when_to_use: "Understand how LLMs ensure quality and CEX's most original contribution (governance as first-class citizen)"
keywords: [govern, quality_gate, validator, benchmark, golden_test, evals, shokunin]
long_tails:
  - "Why GOVERN is the largest CEX function with 22 types"
  - "What is the difference between quality_gate and validator in CEX"
axioms:
  - "ALWAYS implement GOVERN on every output consumed by another system"
  - "NEVER treat governance as an optional step at the end of the pipeline"
linked_artifacts:
  primary: p01_kc_cex_function_constrain
  related: [p01_kc_cex_function_produce, p01_kc_cex_function_collaborate]
density_score: null
data_source: "https://arxiv.org/abs/2303.11366"
related:
  - p01_kc_lp07_evals
  - p01_kc_cex_lp07_evals
  - p01_kc_lp11_feedback
  - p01_kc_cex_taxonomy
  - p01_kc_cex_lp11_feedback
  - p01_kc_validator
  - bld_architecture_quality_gate
  - bld_architecture_golden_test
  - p01_kc_cex_function_produce
  - p01_kc_cex_function_inject
---

## Summary

GOVERN evaluates, controls, and improves output quality via quality gates, benchmarks, validators, and lifecycle rules. With 22 types (28% of CEX), it is the largest function — reflecting a critical industry gap where no framework treats governance as a first-class citizen. LangChain has Callback (rudimentary), DSPy has Metric (partial), CrewAI has nothing. CEX treats quality as an architectural function as important as generation. Analogy: Japanese Shokunin — the artisan who refuses to deliver work below standard. REFLECT (self-critique) is a sub-function of GOVERN applied internally.

## Spec

| Sub-function | Types | LPs | Function |
|--------------|-------|-----|----------|
| Evaluation | 6 types | P07 | Measure quality objectively |
| Validation | 6 types | P05-P06 | Verify formal conformance |
| Config | 8 types | P02+P09 | Control system behavior |
| Feedback | 6 types | P04+P11 | Correct and improve iteratively |

Evaluation types: unit_eval, smoke_eval, e2e_eval, benchmark,
golden_test, scoring_rubric. From unit test to multi-dimensional rubric.
quality_gate (holistic numeric score) vs validator (binary pass/fail).
benchmark (comparative between versions) vs eval (absolute by criterion).
confidence_threshold operates PRE-generation; quality_gate operates POST-generation.
law (constitutional, inviolable) vs runtime_rule (adjustable at execution).
guardrail (proactive, prevents) vs validator (reactive, detects).
bugloop (test->fail->fix->verify->commit) vs simple retry (repeats).
Reflexion (Shinn 2023) and Self-Refine (Madaan 2023) confirm:
self-critique is GOVERN applied to own output, not a separate function.
22 formal types vs LangChain Callback (1) vs DSPy Metric (2).
No framework treats governance with this granularity.

## Patterns

| Trigger | Action |
|---------|--------|
| Output consumed by another system | quality_gate with threshold |
| Conformance with specific rules | validator (pass/fail) |
| Comparison between versions or models | standardized benchmark |
| Detect quality regression | golden_test as reference |
| Reproducible and explainable evaluation | scoring_rubric with criteria |
| Quick test after change | smoke_eval before full suite |
| Automatic defect correction | bugloop (test->fix->verify) |
| Gradual feature rollout | feature_flag without deploy |
| Inviolable system principle | law (constitutional) |

## Code

<!-- lang: python | purpose: quality gate and eval patterns -->
```python
# quality_gate: score numerico com threshold
score = scoring_rubric.evaluate(output, criteria=["density", "accuracy"])
if score < 7.0:
    output = refine(output)  # GOVERN triggers re-PRODUCE
elif score >= 9.5:
    pool.promote(output, tier="golden")  # Shokunin standard

# golden_test: regressao contra referencia conhecida
expected = load_golden("kc_function_call_v1.md")
similarity = compare(output, expected)
assert similarity > 0.85, "Regression detected"

# bugloop: test -> fail -> fix -> verify -> commit
while not tests_pass(module) and attempts < 3:
    diagnosis = analyze_failure(test_output)
    apply_fix(diagnosis)
    attempts += 1
```

## Anti-Patterns

- Production without governance (factory without quality control)
- quality_gate only at the end (error propagates through entire pipeline)
- Self-scoring quality (quality: null until external validation)
- Confusing validator (format) with quality_gate (quality)
- Outdated golden_test (obsolete reference generates false negatives)
- Guardrail without log (silent blocking prevents debugging)

## References

- source: https://arxiv.org/abs/2303.11366
- source: https://arxiv.org/abs/2303.17651
- related: p01_kc_cex_function_constrain
- related: p01_kc_cex_function_produce
- related: p01_kc_cex_function_collaborate

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp07_evals]] | sibling | 0.36 |
| [[p01_kc_cex_lp07_evals]] | sibling | 0.31 |
| [[p01_kc_lp11_feedback]] | sibling | 0.27 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.27 |
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.25 |
| [[p01_kc_validator]] | sibling | 0.25 |
| [[bld_architecture_quality_gate]] | downstream | 0.23 |
| [[bld_architecture_golden_test]] | downstream | 0.22 |
| [[p01_kc_cex_function_produce]] | sibling | 0.21 |
| [[p01_kc_cex_function_inject]] | sibling | 0.21 |
