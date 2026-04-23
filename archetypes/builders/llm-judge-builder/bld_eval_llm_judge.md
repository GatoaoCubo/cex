---
kind: quality_gate
id: p11_qg_llm_judge
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of llm_judge artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: llm_judge"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, llm-judge, P07, evals, criteria, scale, few-shot]
tldr: "Pass/fail gate for llm_judge artifacts: judge_model presence, criteria completeness, scale anchors, few-shot calibration, and boundary compliance."
domain: "LLM-as-Judge configuration — automated quality evaluators with declared model, criteria, scale, and calibration examples"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - p03_sp_llm_judge_builder
  - bld_instruction_llm_judge
  - bld_knowledge_card_llm_judge
  - llm-judge-builder
  - bld_collaboration_llm_judge
  - p10_lr_llm_judge_builder
  - p01_kc_llm_judge
  - bld_output_template_llm_judge
  - bld_architecture_llm_judge
  - bld_schema_llm_judge
---

## Quality Gate

# Gate: llm_judge
## Definition
| Field | Value |
|---|---|
| metric | llm_judge artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: llm_judge` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p07_judge_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or wrong prefix |
| H03 | ID equals filename stem | `id: p07_judge_foo` but file is `p07_judge_bar.md` |
| H04 | Kind equals literal `llm_judge` | `kind: scorer` or `kind: rubric` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `judge_model`, `criteria`, or `scale` |
| H07 | judge_model is a concrete model identifier | `judge_model: "a good model"` or empty string |
| H08 | criteria list has at least one item | `criteria: []` or criteria field absent |
| H09 | scale has min, max, and at least 2 anchors | Scale defined without anchor labels |
| H10 | Artifact is a judge config, not a pipeline blocker | Artifact conditionally halts execution flow (that is quality_gate P11) |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Criteria independence | 1.0 | Each criterion measures exactly one quality aspect; no overlap between criteria |
| Scale anchor quality | 1.0 | Anchors define concrete observable behaviors, not vague labels like "good" or "bad" |
| Few-shot coverage | 1.0 | At least 2 examples present; covers both high and low score ends of scale |
| Few-shot rationale quality | 1.0 | Each example has chain-of-thought rationale explaining score assignment |
| Judge model apownteness | 0.5 | Model is from different family than likely evaluated model (reduces self-enhancement bias) |
| Framework mapping | 0.5 | Framework field set and integration pattern documented |
| Chain-of-thought declaration | 0.5 | chain_of_thought field explicitly set; rationale provided if false |
| Temperature setting | 0.5 | temperature <= 0.2 for reproducibility; reason documented if higher |
| Aggregation method | 0.5 | aggregation declared for multi-criteria judges |
| Boundary clarity | 1.0 | Explicitly not a scoring_rubric (no model), not a quality_gate (no block), not a benchmark |
| Domain specificity | 1.0 | Criteria and few-shot examples specific to the declared evaluation domain |
| pass_threshold declaration | 0.5 | pass_threshold set when judge feeds a binary decision downstream |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Experimental judge under active calibration — few-shot examples not yet finalized |
| approver | Author self-certification with calibration plan and deadline |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — experimental judges must reach >= 7.0 or be removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H07 (missing judge_model means the artifact is a scoring_rubric, not a judge) |

## Examples

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
author: "builder_agent"
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
quality: 8.9
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
