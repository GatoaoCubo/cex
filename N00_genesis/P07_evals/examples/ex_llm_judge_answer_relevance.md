---
id: p07_judge_answer_relevance
kind: llm_judge
pillar: P07
name: "Answer Relevance Judge"
description: "LLM-as-judge evaluator for RAG answer relevance, completeness, and citation accuracy"
judge_model: claude-sonnet-4-6
criteria: [relevance, completeness, citation_accuracy]
scale: "1-5"
few_shot: 3
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.0
tags: [llm-judge, answer-relevance, rag, evaluation, citation]
related:
  - bld_examples_llm_judge
  - p07_dataset_rag_qa_v1
  - bld_collaboration_citation
  - p07_llm_judge
  - p10_lr_llm_judge_builder
  - p01_qg_faq_entry
  - p03_cs_json_output
  - bld_examples_prompt_technique
  - brand_decisions_memory
  - bld_knowledge_card_llm_judge
---

# LLM Judge: Answer Relevance

## Purpose

Evaluates RAG-generated answers using Claude Sonnet as judge. Scores three orthogonal criteria on a 1-5 scale with calibrated few-shot examples to reduce variance.

## Judge Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | claude-sonnet-4-6 | Cost-effective, consistent scoring |
| Temperature | 0.0 | Deterministic judgments |
| Max tokens | 512 | Structured output only |
| Criteria | 3 (relevance, completeness, citation) | Orthogonal dimensions |
| Scale | 1-5 integer | Granular enough, not noisy |
| Few-shot | 3 per criterion | Calibration anchors |

## Criteria Definitions

### Relevance (1-5)
Does the answer directly address the question asked?
- **5**: Precisely answers the question, no tangential content
- **3**: Partially relevant, includes some off-topic material
- **1**: Answer is about a different topic entirely

### Completeness (1-5)
Does the answer cover all aspects of the question?
- **5**: All sub-questions answered, no gaps
- **3**: Main point covered, secondary aspects missing
- **1**: Only superficially touches the topic

### Citation Accuracy (1-5)
Are claims properly attributed to retrieved sources?
- **5**: Every factual claim has a correct source citation
- **3**: Some citations present but gaps or misattributions exist
- **1**: No citations or all citations are incorrect

## Few-Shot Calibration Examples

### Example 1 — High Score (5/5/5)
```yaml
question: "What is the default rotation policy for API keys in organization?"
context: "KC_CONFIG_003: API keys rotate every 90 days via Vault. AES-256 encryption at rest. Audit log enabled."
answer: "The default rotation policy for API keys in organization is 90 days, managed through Vault with AES-256 encryption at rest and audit logging enabled [KC_CONFIG_003]."
scores:
  relevance: 5       # Directly answers the question
  completeness: 5    # Covers rotation, encryption, audit
  citation_accuracy: 5  # Correct source attribution
```

### Example 2 — Medium Score (3/2/3)
```yaml
question: "How does BM25 handle synonym matching?"
context: "KC_BM25_001: BM25 is keyword-based, operates on exact token matches. Does not understand synonyms."
answer: "BM25 is a search algorithm that ranks documents by relevance. It uses TF-IDF scoring and works well for keyword searches."
scores:
  relevance: 3       # Related to BM25 but doesn't answer synonym question
  completeness: 2    # Missing the key point: BM25 does NOT handle synonyms
  citation_accuracy: 3  # No citation but no false attribution either
```

### Example 3 — Low Score (1/1/1)
```yaml
question: "What are the rate limits for Anthropic Tier 2?"
context: "KC_RATELIMIT_002: Tier 2 allows 1000 RPM, 80K TPM, $50/day budget."
answer: "To deploy on Railway, use `railway up` after configuring your service. Make sure to set environment variables first."
scores:
  relevance: 1       # Completely off-topic (deployment vs rate limits)
  completeness: 1    # Answers a different question entirely
  citation_accuracy: 1  # No relevant citations
```

## Judge Prompt Template

```
You are an evaluation judge. Score the following answer on three criteria.

Question: {{question}}
Retrieved Context: {{context}}
Generated Answer: {{answer}}

Score each criterion 1-5:
- relevance: Does the answer address the question?
- completeness: Are all aspects covered?
- citation_accuracy: Are sources correctly cited?

Respond in YAML only:
```yaml
relevance: <1-5>
completeness: <1-5>
citation_accuracy: <1-5>
reasoning: "<1 sentence>"
```

## Execution

```python
import anthropic

client = anthropic.Anthropic()

def judge_answer(question: str, context: str, answer: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        temperature=0.0,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT.format(
                question=question, context=context, answer=answer
            )
        }]
    )
    return yaml.safe_load(response.content[0].text)
```

## Pass/Fail Thresholds

| Criterion | Pass | Warn | Fail |
|-----------|------|------|------|
| Relevance | >= 4 | 3 | <= 2 |
| Completeness | >= 4 | 3 | <= 2 |
| Citation | >= 3 | 2 | <= 1 |
| **Composite** | **>= 3.7 avg** | **3.0-3.6** | **< 3.0** |

## Anti-Patterns
- Using opus as judge (expensive, no accuracy gain for scoring)
- Temperature > 0 (introduces scoring variance)
- Judging without few-shot calibration (scores drift across runs)
- Single composite score instead of per-criterion (hides weaknesses)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_llm_judge]] | related | 0.31 |
| [[p07_dataset_rag_qa_v1]] | related | 0.27 |
| [[bld_collaboration_citation]] | downstream | 0.23 |
| [[p07_llm_judge]] | sibling | 0.22 |
| [[p10_lr_llm_judge_builder]] | downstream | 0.21 |
| [[p01_qg_faq_entry]] | downstream | 0.21 |
| [[p03_cs_json_output]] | upstream | 0.21 |
| [[bld_examples_prompt_technique]] | related | 0.21 |
| [[brand_decisions_memory]] | downstream | 0.20 |
| [[bld_knowledge_card_llm_judge]] | upstream | 0.20 |
