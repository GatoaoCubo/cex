---
kind: examples
id: bld_examples_llm_judge
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of llm_judge artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: llm-judge-builder
## Golden Example
INPUT: "Create an LLM judge to evaluate RAG responses for faithfulness and answer relevance using DeepEval"
OUTPUT:
```yaml
id: p07_judge_rag_quality
kind: llm_judge
pillar: P07
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "RAG Response Quality Judge"
judge_model: "gpt-4o"
criteria:
  - faithfulness
  - answer_relevance
scale:
  type: likert
  min: 1
  max: 5
  anchors:
    1: "completely unfaithful or irrelevant"
    3: "partially faithful and relevant with notable gaps"
    5: "fully faithful to context and directly answers the question"
quality: null
tags: [llm_judge, rag, faithfulness, P07]
tldr: "RAG quality judge: gpt-4o evaluates faithfulness + relevance on 1-5 likert via DeepEval"
description: "Evaluates RAG pipeline outputs for factual faithfulness to retrieved context and relevance to user question"
few_shot:
  - input: "Q: What is the capital of France? Context: Paris is the capital and largest city of France."
    output: "The capital of France is Paris, a major European city known for the Eiffel Tower."
    score: 5
    rationale: "Answer is fully supported by context (faithfulness=5). Answer directly addresses the question (relevance=5). Eiffel Tower detail not in context but is accurate world knowledge — does not constitute hallucination."
  - input: "Q: What is the revenue of Acme Corp? Context: Acme Corp was founded in 1995 and employs 500 people."
    output: "Acme Corp revenue is approximately $50 million based on its employee count."
    score: 1
    rationale: "Answer introduces $50M figure not present in context (faithfulness=1). Hallucinated financial data from headcount is a critical faithfulness failure."
framework: deepeval
temperature: 0.0
chain_of_thought: true
aggregation: mean
pass_threshold: 3.5
```
## Overview
Evaluates RAG pipeline outputs on faithfulness (claims supported by retrieved context) and answer relevance (response addresses the user question). Reference-based judge — requires input question and retrieved context.
## Criteria
### faithfulness
Every factual claim must be traceable to context. High (5): all claims supported. Low (1): key claims hallucinated.
### answer_relevance
Output must directly address the question. High (5): fully addresses with no off-topic content. Low (1): fails to address or entirely off-topic.
## Scale
Type: likert | Range: 1-5 | 1=Failing, 3=Acceptable, 5=Excellent

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_judge_ pattern (H02 pass)
- kind: llm_judge (H04 pass)
- judge_model is concrete identifier "gpt-4o" (H07 pass)
- criteria list matches ## Criteria section names exactly (H08 pass)
- scale has min, max, 3 anchors (H09 pass)
- chain_of_thought: true, temperature: 0.0, framework declared, pass_threshold set

## Anti-Example
INPUT: "Create a judge to score responses"
BAD OUTPUT:
```yaml
id: response-scorer
kind: scorer
criteria: [quality]
scale: 1-10
judge_model: ""
quality: 8.5
tags: [eval]
```
Scores responses on quality.
## Criteria
quality: how good is it

FAILURES:
1. id: "response-scorer" has hyphens and no `p07_judge_` prefix -> H02 FAIL
2. kind: "scorer" not "llm_judge" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. judge_model: "" (empty, not a concrete identifier) -> H07 FAIL
5. Missing fields: pillar, version, created, updated, author, name, tldr -> H06 FAIL
6. scale: "1-10" is a string, not a structured map with anchors -> H09 FAIL
