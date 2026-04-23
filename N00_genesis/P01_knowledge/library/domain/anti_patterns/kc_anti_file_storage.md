---
id: p01_kc_anti_file_storage
kind: knowledge_card
type: domain
pillar: P01
title: "Anti-Pattern: LLM as File Storage"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: 9.1
tags: [anti-pattern, file-storage, context-window, cost]
tldr: "Don't dump entire files into LLM context. Use retrieval + relevant excerpts. Full-file injection wastes tokens, increases cost, decreases accuracy."
when_to_use: "Reviewing prompt design for token efficiency"
keywords: [anti-pattern, file-storage, token-waste, context-pollution]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_anti_full_context
  - p01_kc_anti_isolated_sessions
  - p01_kc_operational_laws
  - p01_kc_distillation_pipeline
  - p01_kc_pattern_extraction
  - p01_gl_rag
  - p01_kc_knowledge_card
  - p01_kc_qa_validation
  - p01_kc_knowledge_distillation
  - p01_kc_refinement
---

# Anti-Pattern: LLM as File Storage

## The Problem
Dumping entire files (10K+ tokens) into context when the LLM only needs 200 tokens of relevant info.

## Symptoms
1. Prompts >50K tokens for simple tasks
2. High API costs with no quality improvement
3. LLM "forgets" instructions buried under file dumps
4. Slow response times

## Fix
1. Retrieve relevant chunks (RAG), not whole files
2. Summarize large files before injection
3. Use `cex_token_budget.py` to enforce limits
4. Place critical instructions at start AND end of prompt (primacy + recency)

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Anti-Pattern: LLM as File Storage"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Anti-Pattern: LLM as File Storage" --top 5
```

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_card` |
| Pillar | P01 |
| Domain | anti_patterns |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_anti_full_context]] | sibling | 0.40 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.32 |
| [[p01_kc_operational_laws]] | sibling | 0.29 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.25 |
| [[p01_kc_pattern_extraction]] | sibling | 0.23 |
| [[p01_gl_rag]] | related | 0.22 |
| [[p01_kc_knowledge_card]] | sibling | 0.21 |
| [[p01_kc_qa_validation]] | sibling | 0.20 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.20 |
| [[p01_kc_refinement]] | sibling | 0.20 |
