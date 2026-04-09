---
id: p01_kc_scoring_rubric
kind: knowledge_card
type: kind
pillar: P07
title: "Scoring Rubric — Deep Knowledge for scoring_rubric"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: scoring_rubric
quality: 9.1
tags: [scoring_rubric, P07, GOVERN, kind-kc]
tldr: "Multi-dimensional evaluation framework defining quality criteria with explicit anchors per dimension and score scale."
when_to_use: "Building, reviewing, or reasoning about scoring_rubric artifacts"
keywords: [rubric, criteria, evaluation, 5D, 12LP, quality-framework]
feeds_kinds: [scoring_rubric]
density_score: null
aliases: ["evaluation rubric", "grading criteria", "quality framework", "scoring guide", "assessment matrix"]
user_says: ["define scoring criteria", "criterios de avaliacao", "how do I measure quality", "create a rubric", "set up evaluation dimensions"]
long_tails: ["I need to define what good output looks like across multiple dimensions", "create a scoring framework to calibrate my LLM judge", "build an evaluation rubric with anchor descriptions for each score level", "set up quality criteria with weighted dimensions for automated scoring"]
cross_provider:
  langchain: "CriteriaEvalChain with rubric prompt"
  llamaindex: "RelevancyEvaluator with scoring guide"
  crewai: "Custom scoring agent with rubric"
  dspy: "Custom metric function with rubric logic"
  openai: "model-graded rubric (grader_model_graded)"
  anthropic: "Claude judge with dimension anchors"
  haystack: "Custom LLMEvaluator with rubric"
---

# Scoring Rubric

## Spec
```yaml
kind: scoring_rubric
pillar: P07
llm_function: GOVERN
max_bytes: 5120
naming: p07_sr_{{framework}}.md + .yaml
core: true
```

## What It Is
A structured evaluation framework that defines what "good output" means across N dimensions, each with explicit anchor descriptions for each score point. Used to calibrate llm_judge evaluators, train human reviewers, and define quality thresholds for quality_gate (P11). NOT benchmark—rubric defines criteria; benchmark runs measurements. NOT quality_gate—quality_gate blocks on threshold; rubric defines the score itself.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Custom eval criteria | CriteriaEvalChain with rubric prompt |
| LlamaIndex | EvaluationResult criteria | RelevancyEvaluator with scoring guide |
| CrewAI | Custom scoring agent | Dedicated rubric-applying crew agent |
| DSPy | Custom metric function | Lambda metric with rubric logic |
| Haystack | Custom LLMEvaluator | Evaluator with rubric in judge prompt |
| OpenAI | Model-graded rubric | grader_model_graded with rubric criteria |
| Anthropic | Claude judge rubric | Scoring prompt with dimension anchors |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| framework | str | custom | 5D, 12LP, RAGAS, G-Eval, custom |
| dimensions | list[Dimension] | required | More = granular, harder to calibrate |
| scale | int | 10 | 0-5 coarse/fast, 0-10 balanced, 0-100 precise |
| aggregation | enum | weighted_avg | weighted_avg/min/geometric |
| weights | dict[str, float] | equal | Sum must = 1.0 |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| 5D rubric | General LLM output quality | accuracy, completeness, clarity, density, format |
| 12LP rubric | Long-form professional content | 12 language quality dimensions |
| RAGAS rubric | RAG pipeline evaluation | faithfulness, relevancy, context_precision |
| G-Eval rubric | NLG tasks (summarization, MT) | coherence, consistency, fluency, relevance |
| Domain rubric | Specialized agent output | Custom dimensions for marketing copy |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| >8 dimensions | Evaluators disagree, calibration fails | Keep <= 6 core dimensions |
| No anchor descriptions | Score 7 means different things | Define 3/5/7/9/10 anchors per dimension |
| Rubric without calibration | Judges drift over time | Validate against golden_tests monthly |
| Conflating with quality_gate | Rubric scores; gate blocks | quality_gate uses rubric output as input |

## Integration Graph
```
[domain knowledge] --> [scoring_rubric] --> [llm_judge config]
[golden_test] -------> [scoring_rubric calibration]
                            |-----------> [quality_gate (P11)]
                            |-----------> [benchmark quality metric]
                            |-----------> [unit_eval / e2e_eval]
```

## Decision Tree
- IF defining WHAT quality means with dimensions + anchors THEN scoring_rubric
- IF applying rubric automatically with LLM THEN llm_judge (references rubric)
- IF blocking pipeline on quality threshold THEN quality_gate (P11)
- IF measuring aggregate performance THEN benchmark (uses rubric as metric)
- DEFAULT: scoring_rubric before building any evaluator or quality gate

## Quality Criteria
- GOOD: >= 3 dimensions, scale defined, aggregation set, weights sum to 1.0
- GREAT: Each dimension has anchor descriptions (3/7/10), calibrated on golden_tests
- FAIL: Single-dimension, no anchors, weights != 1.0, used as quality_gate directly

## Built-in Frameworks Reference
| Framework | Dims | Scale | Best For |
|---|---|---|---|
| 5D | 5 | 0-10 | General agent output quality |
| 12LP | 12 | 0-10 | Long-form professional writing |
| RAGAS | 4 | 0-1 | RAG pipeline faithfulness/relevancy |
| G-Eval | 4 | 0-5 | NLG tasks (summarization, MT) |
| Custom | N | any | Domain-specific agent evaluation |
