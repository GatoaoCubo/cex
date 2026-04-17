---
id: p01_kc_llm_judge
kind: knowledge_card
type: kind
pillar: P07
title: "LLM Judge — Deep Knowledge for llm_judge"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: llm_judge
quality: 9.1
tags: [llm_judge, P07, GOVERN, kind-kc]
tldr: "Configuration for using an LLM as automated evaluator scoring outputs against defined criteria."
when_to_use: "Building, reviewing, or reasoning about llm_judge artifacts"
keywords: [llm-judge, evaluator, automated-eval, scoring]
feeds_kinds: [llm_judge]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# LLM Judge

## Spec
```yaml
kind: llm_judge
pillar: P07
llm_function: GOVERN
max_bytes: 2048
naming: p07_judge.md
core: true
```

## What It Is
Configuration for an LLM-as-Judge evaluator: which model to use, what criteria to score, the scale, and the judge system prompt. The judge reads a response and outputs a numeric or categorical score. NOT scoring_rubric—rubric defines WHAT to evaluate; llm_judge defines HOW to evaluate (model, scale, prompt implementation).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | LLMChain as judge | Custom eval chain scoring responses |
| LlamaIndex | LLMRelevancyEvaluator | Built-in LLM-based evaluators |
| CrewAI | Custom judge agent | Dedicated crew agent as evaluator |
| DSPy | LM-based metric | Lambda metric using LM for scoring |
| Haystack | LLMEvaluator | Built-in LLM judge component |
| OpenAI | GPT-4o as judge | Model-graded eval via Evals API |
| Anthropic | Claude as judge | Haiku/Sonnet judge with scoring prompt |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| judge_model | str | claude-haiku-4-5 | Stronger = accurate, expensive; weaker = fast |
| scale | int | 10 | 0-5 coarse, 0-100 over-precise |
| chain_of_thought | bool | true | true = interpretable, false = faster |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pairwise judge | Compare A vs B output quality | "Which is better?" + reason |
| Rubric grader | Score against scoring_rubric criteria | Apply 5D rubric per dimension |
| Calibrated judge | Validate against golden_tests | Tune judge prompt to match human scores |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Using judge as scoring_rubric | Confuses config with criteria | Rubric defines WHAT, judge applies HOW |
| Same model judges own outputs | Self-serving bias | Use different model family for judging |
| No calibration against golden_tests | Unchecked judge drift | Validate judge on >= 10 golden_tests |

## Integration Graph
```
[scoring_rubric] --> [llm_judge] --> [unit_eval score]
[golden_test] -----> [llm_judge calibration]
                          |-------> [benchmark quality metric]
                          |-------> [e2e_eval scoring]
```

## Decision Tree
- IF defining WHAT to evaluate (dimensions, criteria) THEN scoring_rubric
- IF defining HOW to evaluate (model, scale, prompt) THEN llm_judge
- DEFAULT: llm_judge for any automated quality scoring pipeline

## Quality Criteria
- GOOD: judge_model specified, criteria linked to scoring_rubric, scale defined
- GREAT: Calibrated against golden_tests, chain_of_thought enabled, bias mitigation
- FAIL: No rubric link, self-evaluating (same model as target), uncalibrated
