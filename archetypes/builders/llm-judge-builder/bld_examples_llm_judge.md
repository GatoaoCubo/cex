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
    rationale: "Answer introduces $50M figure not present in context (faithfulness=1). Answer attempts relevance but fabricates the key fact. Hallucinated financial data from headcount is a critical faithfulness failure."
framework: deepeval
temperature: 0.0
chain_of_thought: true
aggregation: mean
pass_threshold: 3.5
```
## Overview
Evaluates RAG pipeline outputs on two independent quality dimensions: faithfulness (claims supported by retrieved context) and answer relevance (response addresses the user question). Reference-based judge — requires input question and retrieved context.
## Criteria
### faithfulness
Every factual claim in the output must be traceable to the provided context. Penalizes hallucination, inference beyond context, and unsupported assertions.
High score (5): all claims directly supported by context; no fabricated facts.
Low score (1): key claims contradict or are absent from context; hallucination present.
### answer_relevance
The output must directly address the user's question. Penalizes off-topic responses, partial answers, and excessive irrelevant elaboration.
High score (5): response fully addresses the question with no off-topic content.
Low score (1): response fails to address the question or is entirely off-topic.
## Scale
Type: likert | Range: 1-5
| Score | Label | Meaning |
|-------|-------|---------|
| 1 | Failing | Critical failure — hallucination or complete irrelevance |
| 3 | Acceptable | Partial compliance with notable gaps |
| 5 | Excellent | Full compliance, no gaps detected |
## Few-Shot Examples
### Example 1 (high score)
Input: "Q: What is the capital of France? Context: Paris is the capital and largest city of France."
Output: "The capital of France is Paris."
Score: 5 / 5
Rationale: Claim directly supported by context. Answer precisely addresses question. No extraneous claims.
### Example 2 (low score)
Input: "Q: What is Acme Corp revenue? Context: Acme Corp was founded in 1995."
Output: "Acme Corp revenue is $50M."
Score: 1 / 5
Rationale: Revenue figure absent from context. Hallucinated critical fact. Faithfulness failure dominates.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_judge_ pattern (H02 pass)
- kind: llm_judge (H04 pass)
- judge_model is concrete identifier "gpt-4o" (H07 pass)
- criteria list matches ## Criteria section names exactly (H08 pass)
- scale has min, max, 3 anchors (H09 pass)
- 2 few_shot examples with scores within 1-5 range and rationale (soft pass)
- chain_of_thought: true (reduces hallucinated scores)
- temperature: 0.0 (reproducibility)
- framework: deepeval declared (integration ready)
- pass_threshold: 3.5 (downstream decision documented)
- criteria are non-overlapping (faithfulness != relevance)

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
7. tags: only 1 item, missing "llm_judge" -> soft FAIL
8. criteria: ["quality"] is a single vague dimension with no definition -> soft FAIL
9. No few_shot examples — judge will drift on edge cases -> soft FAIL
10. No scale anchors — "1-10" without labels is unactionable -> H09 FAIL
11. Body missing ## Scale, ## Few-Shot Examples sections -> soft FAIL
12. criterion "quality" is not a measurable dimension — what does "quality" mean? -> soft FAIL
