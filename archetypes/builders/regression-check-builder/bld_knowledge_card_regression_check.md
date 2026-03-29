---
kind: knowledge_card
id: bld_knowledge_card_regression_check
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for regression_check production — baseline comparison configuration
sources: Braintrust experiment comparison, Promptfoo --compare, LangSmith A/B experiments, DeepEval regression tests
---

# Domain Knowledge: regression_check
## Executive Summary
Regression checks are comparison configurations that measure a current LLM system against a known-good baseline to detect quality degradation. They define what to compare (metrics), against what (baseline_ref), and how much deviation is acceptable (threshold). A regression_check does NOT measure absolute performance — it only answers: "is this version worse than the reference?"
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (Evals) |
| llm_function | GOVERN (controls deployment gates) |
| Layer | runtime |
| machine_format | yaml |
| naming | p07_rc_{slug}.md |
| max_bytes | 2048 |
| Required fields | id, name, baseline_ref, threshold, metrics |
## Tool Integrations
### Braintrust
- Baseline = named experiment (e.g., `experiment/prod-v1.2`)
- Comparison via experiment diff UI or `braintrust eval --compare <baseline>`
- Metrics: scores defined in eval functions (accuracy, hallucination, coherence)
- Threshold: percentage drop in aggregate score triggers alert
- Output: diff table with per-metric delta and statistical significance
### Promptfoo --compare
- Baseline = previous run results file or named config version
- Invocation: `promptfoo eval --compare baseline.json`
- Metrics: pass rate, assertion scores, latency percentiles
- Threshold: configurable per assertion in `promptfooconfig.yaml`
- Output: diff report showing regressions highlighted in red
### LangSmith A/B Experiments
- Baseline = dataset + evaluator run tagged as reference
- Comparison: create experiment, compare against reference run in UI
- Metrics: evaluator scores (correctness, helpfulness, groundedness)
- Threshold: manual review or automated via feedback tags
- Output: side-by-side score comparison with statistical summary
### DeepEval Regression Tests
- Baseline = stored metrics from previous test run (`deepeval test run --save`)
- Comparison: `deepeval test run --compare-to <baseline_file>`
- Metrics: GEval, Faithfulness, AnswerRelevancy, Hallucination
- Threshold: `min_score` per metric in test config
- Output: pass/fail per metric with delta from baseline
## Patterns
- **Baseline capture**: always tag baselines at release or deploy — never compare against a moving target
- **Threshold calibration**: start at 5% relative deviation; tighten to 2% for production-critical pipelines
- **Multi-metric comparison**: compare all relevant dimensions simultaneously — a latency win masking accuracy regression is a false positive
- **Statistical significance**: for stochastic models, require minimum sample size before declaring regression
| Pattern | When to use |
|---------|-------------|
| relative threshold | Percentage deviation from baseline (most common) |
| absolute threshold | Fixed score floor (e.g., accuracy must stay >= 0.85) |
| composite threshold | Weighted combination of multiple metrics |
| per-metric threshold | Different tolerance per dimension |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague baseline_ref ("previous version") | Unresolvable — cannot reproduce comparison |
| threshold: 0 without justification | Zero tolerance fails on natural model variance |
| Single metric comparison | A model can win on accuracy and lose on latency/cost |
| No fail_action defined | Regression detected but nothing happens |
| Comparing against stale baseline (>90 days) | Baseline no longer reflects production reality |
| Conflating with benchmark | Benchmark = absolute; regression_check = relative to baseline |
## Boundary
| IS regression_check | IS NOT regression_check |
|--------------------|------------------------|
| Compares current vs baseline_ref | Measures absolute performance (benchmark) |
| Detects relative degradation | Tests isolated correctness (unit_eval) |
| Config for framework execution | Validates single reference case (golden_test) |
| Runtime gate for deploy/PR | Fast sanity check (smoke_eval) |
## References
- Braintrust: braintrustdata.com/docs/guides/evals
- Promptfoo: promptfoo.dev/docs/configuration/guide
- LangSmith: docs.smith.langchain.com/evaluation
- DeepEval: docs.confident-ai.com/docs/regression-testing
