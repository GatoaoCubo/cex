---
id: p01_kc_regression_check
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P07
title: "Regression Check — Deep Knowledge for regression_check"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: regression_check
quality: 9.1
tags: [regression_check, P07, GOVERN, kind-kc]
tldr: "Automated comparison of current pipeline performance against a stored baseline to detect quality degradation."
when_to_use: "Building, reviewing, or reasoning about regression_check artifacts"
keywords: [regression, baseline, comparison, degradation, delta]
feeds_kinds: [regression_check]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_knowledge_card_regression_check
  - regression-check-builder
  - bld_collaboration_regression_check
  - p03_sp_regression_check_builder
  - p01_kc_benchmark
  - p07_regression_check
  - bld_architecture_regression_check
  - bld_config_regression_check
  - p11_qg_regression_check
  - bld_instruction_regression_check
---

# Regression Check

## Spec
```yaml
kind: regression_check
pillar: P07
llm_function: GOVERN
max_bytes: 2048
naming: p07_regcheck.md
core: false
```

## What It Is
A comparison protocol that runs the current pipeline against the same eval_dataset used in a previous run and checks whether scores or metrics have degraded beyond a defined threshold. NOT benchmark—benchmark measures performance in absolute terms; regression_check measures DELTA between two runs. Requires a stored baseline_ref to function.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | LangSmith comparison view | Compare eval runs side-by-side |
| LlamaIndex | Baseline comparison | Manual comparison of BatchEvalRunner outputs |
| CrewAI | Manual delta tracking | No native regression; compare log files |
| DSPy | compile() delta check | Compare compiled vs baseline metrics |
| Haystack | EvaluationRunOverview diff | Compare two pipeline run results |
| OpenAI | Evals baseline comparison | Compare eval run against reference run |
| Anthropic | Custom delta tracker | Compare eval JSONs against baseline |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| baseline_ref | str | required | Points to stored benchmark run |
| threshold | float | 0.05 | 5% degradation tolerance |
| metric | enum | quality_score | quality_score/latency_ms/cost_usd |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pre-merge gate | Run before merging prompt changes | CI checks delta < 5% |
| Model upgrade check | Validate new model doesn't degrade | Compare sonnet-4 vs sonnet-3.7 |
| Feature flag validation | Test new feature doesn't harm baseline | A/B delta on quality_score |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No baseline stored | Nothing to compare against | Always store baseline after first eval |
| Threshold too tight | False positives on LLM variance | Use >= 5% threshold for LLM quality |
| Confusing with benchmark | Benchmark is absolute; regression is delta | Store baseline from benchmark output |

## Integration Graph
```
[benchmark run N-1] --> [regression_check] --> [pass/fail delta]
[eval_dataset] -------> [regression_check]         |
[golden_test] --------> [regression_check] --> [quality_gate (P11)]
```

## Decision Tree
- IF measuring absolute performance THEN benchmark
- IF comparing current vs stored baseline THEN regression_check
- DEFAULT: regression_check as CI gate after any prompt or model change

## Quality Criteria
- GOOD: baseline_ref defined, threshold set, metric specified
- GREAT: CI-integrated, multiple metrics tracked, golden_test subset anchored
- FAIL: No baseline, threshold undefined, runs on different dataset than baseline

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_regression_check]] | sibling | 0.58 |
| [[regression-check-builder]] | related | 0.47 |
| [[bld_collaboration_regression_check]] | downstream | 0.45 |
| [[p03_sp_regression_check_builder]] | related | 0.41 |
| [[p01_kc_benchmark]] | sibling | 0.41 |
| [[p07_regression_check]] | related | 0.37 |
| [[bld_architecture_regression_check]] | downstream | 0.35 |
| [[bld_config_regression_check]] | downstream | 0.33 |
| [[p11_qg_regression_check]] | downstream | 0.33 |
| [[bld_instruction_regression_check]] | upstream | 0.31 |
