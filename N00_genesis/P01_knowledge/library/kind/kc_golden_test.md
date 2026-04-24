---
id: p01_kc_golden_test
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P07
title: "Golden Test — Deep Knowledge for golden_test"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: golden_test
quality: 9.1
tags: [golden_test, P07, GOVERN, kind-kc]
tldr: "Single human-verified reference test case at quality >= 9.5 used as regression anchor for pipeline evaluation."
when_to_use: "Building, reviewing, or reasoning about golden_test artifacts"
keywords: [golden, reference, quality-9.5, regression, anchor]
feeds_kinds: [golden_test]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["gold standard test", "reference test", "baseline case", "anchor test", "verified example"]
user_says: ["create a golden test", "criar teste de referencia", "set the quality baseline", "make a verified test case", "anchor this as the gold standard"]
long_tails: ["I need a human-verified reference case to detect quality regressions", "create a gold-standard test case at quality 9.5+ for calibration", "set up a regression anchor so I know when quality degrades", "build a verified input/output pair to calibrate my LLM judge"]
cross_provider:
  langchain: "LangSmith golden dataset entry"
  llamaindex: "BaseNode with quality annotation"
  crewai: "Reference task output (manually validated)"
  dspy: "devset gold example (score=1.0)"
  openai: "Eval ideal response ({input, ideal})"
  anthropic: "Human-verified eval case"
  haystack: "EvaluationExample (gold=True)"
related:
  - bld_architecture_golden_test
  - golden-test-builder
  - p01_kc_eval_dataset
  - bld_collaboration_golden_test
  - p01_kc_unit_eval
  - bld_architecture_unit_eval
  - p01_kc_few_shot_example
  - bld_knowledge_card_golden_test
  - few-shot-example-builder
  - p03_sp_golden_test_builder
---

# Golden Test

## Spec
```yaml
kind: golden_test
pillar: P07
llm_function: GOVERN
max_bytes: 4096
naming: p07_gt_{{case}}.md + .yaml
core: true
```

## What It Is
A single, human-verified test case that represents the ideal input/output pair at quality >= 9.5. Serves as a regression anchor—if the system changes and this case fails or degrades, a regression is detected. NOT few_shot_example (P01)—few-shot examples teach format; golden_tests evaluate quality. NOT unit_eval—unit_eval runs many cases; golden_test IS one specific case at maximum quality bar.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | LangSmith golden dataset entry | Manually annotated reference example |
| LlamaIndex | BaseNode with quality annotation | Hand-labeled high-quality node |
| CrewAI | Reference task output | Manually validated crew output |
| DSPy | devset gold example | dspy.Example with score=1.0 annotation |
| Haystack | EvaluationExample (gold) | example.gold=True annotation |
| OpenAI | Eval ideal response | {input, ideal} with human review |
| Anthropic | Human-verified eval case | Manually reviewed prompt+response pair |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| quality | float | >= 9.5 | Below 9.5 = not golden, use unit_eval |
| verified_by | str | human | human > LLM judge for golden cases |
| tolerance | float | 0.5 | Score must stay within +/- 0.5 of baseline |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Regression anchor | Detect quality degradation on change | p07_gt_research_output.yaml |
| Rubric calibration | Ground truth for scoring_rubric | p07_gt_scoring_calibration.yaml |
| LLM judge training | Train judge on known-good cases | p07_gt_judge_baseline.yaml |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Unverified golden_test | LLM hallucination as golden case | Always human-verify before promotion |
| Quality < 9.5 labeled golden | Lowers regression bar | Use unit_eval for quality < 9.5 |
| Treating as few_shot_example | Contaminates eval with training | Keep P01 few_shots and P07 golden separate |

## Integration Graph
```
[human review] --> [golden_test] --> [eval_dataset (subset)]
[scoring_rubric] -> [golden_test]         |
                        |-----------> [regression_check]
                        |-----------> [llm_judge calibration]
```

## Decision Tree
- IF quality >= 9.5 AND human-verified THEN golden_test
- IF quality < 9.5 OR not verified THEN unit_eval
- IF purpose is to teach format to LLM THEN few_shot_example (P01)
- DEFAULT: golden_test for highest-quality confirmed reference cases only

## Quality Criteria
- GOOD: Quality >= 9.5, input + expected output both present, human-verified
- GREAT: Linked to scoring_rubric, added to eval_dataset, tolerance defined
- FAIL: Quality < 9.5, LLM-only verification, input or expected output missing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_golden_test]] | downstream | 0.36 |
| [[golden-test-builder]] | related | 0.34 |
| [[p01_kc_eval_dataset]] | sibling | 0.31 |
| [[bld_collaboration_golden_test]] | downstream | 0.29 |
| [[p01_kc_unit_eval]] | sibling | 0.28 |
| [[bld_architecture_unit_eval]] | downstream | 0.27 |
| [[p01_kc_few_shot_example]] | sibling | 0.27 |
| [[bld_knowledge_card_golden_test]] | sibling | 0.25 |
| [[few-shot-example-builder]] | upstream | 0.25 |
| [[p03_sp_golden_test_builder]] | upstream | 0.24 |
