---
kind: knowledge_card
id: bld_knowledge_card_regression_check
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for regression_check production — baseline comparison configuration
sources: Braintrust experiment comparison, Promptfoo --compare, LangSmith A/B experiments, DeepEval regression tests
quality: 9.0
title: "Knowledge Card Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_regression_check
  - p03_sp_regression_check_builder
  - regression-check-builder
  - bld_collaboration_regression_check
  - bld_config_regression_check
  - bld_architecture_regression_check
  - bld_instruction_regression_check
  - bld_tools_regression_check
  - p11_qg_regression_check
  - bld_examples_regression_check
---

# Domain Knowledge: regression_check
## Executive Summary
Regression checks compare a current LLM system against a known-good baseline to detect quality degradation. They define what to compare (metrics), against what (baseline_ref), and how much deviation is acceptable (threshold). A regression_check does NOT measure absolute performance — it only answers: "is this version worse than the reference?"
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
| Tool | Baseline | Invocation | Output |
|------|----------|-----------|--------|
| Braintrust | Named experiment (e.g., `experiment/prod-v1.2`) | `braintrust eval --compare <baseline>` | Diff table with per-metric delta |
| Promptfoo | Previous run file or named config version | `promptfoo eval --compare baseline.json` | Diff report, regressions in red |
| LangSmith | Dataset + evaluator run tagged as reference | Compare experiment in UI | Side-by-side score comparison |
| DeepEval | Stored metrics from prior run (`--save`) | `deepeval test run --compare-to <file>` | pass/fail per metric with delta |
## Patterns
| Pattern | When to use |
|---------|-------------|
| relative threshold | Percentage deviation from baseline (most common) |
| absolute threshold | Fixed score floor (e.g., accuracy must stay >= 0.85) |
| composite threshold | Weighted combination of multiple metrics |
| per-metric threshold | Different tolerance per dimension |
- **Baseline capture**: tag baselines at release or deploy — never compare against a moving target
- **Threshold calibration**: start at 5% relative deviation; tighten to 2% for production-critical pipelines
- **Statistical significance**: for stochastic models, require minimum sample size before declaring regression
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
- Braintrust: braintrustdata.com/docs/guides/evals | Promptfoo: promptfoo.dev/docs | LangSmith: docs.smith.langchain.com/evaluation | DeepEval: docs.confident-ai.com

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_regression_check]] | sibling | 0.60 |
| [[p03_sp_regression_check_builder]] | downstream | 0.53 |
| [[regression-check-builder]] | downstream | 0.53 |
| [[bld_collaboration_regression_check]] | downstream | 0.49 |
| [[bld_config_regression_check]] | downstream | 0.45 |
| [[bld_architecture_regression_check]] | downstream | 0.41 |
| [[bld_instruction_regression_check]] | downstream | 0.41 |
| [[bld_tools_regression_check]] | downstream | 0.39 |
| [[p11_qg_regression_check]] | downstream | 0.39 |
| [[bld_examples_regression_check]] | downstream | 0.39 |
