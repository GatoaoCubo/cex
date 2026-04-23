---
id: p10_lr_retriever_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "retriever_config artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from LangChain BaseRetriever, LlamaIndex BaseRetriever, Haystack Retriever, ChromaDB, Pinecone, Weaviate, FAISS documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: retriever_config
tags: [retriever-config, P01, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [retriever config, dense-only, sparse-only, hybrid, reranked]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Retriever Config"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_retriever_config
  - p10_lr_chunk_strategy_builder
  - p10_lr_handoff_protocol_builder
  - p10_lr_output_validator_builder
  - p03_sp_retriever_config_builder
  - p10_lr_memory_scope_builder
  - p10_lr_prompt_version_builder
  - p10_lr_constraint_spec_builder
  - bld_instruction_retriever_config
  - bld_examples_retriever_config
---
## Summary
Retrieval parameters — how to search and rank chunks from a vector/hybrid store. The difference between a useful retriever_config and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Search Strategy, Parameters, Integration.
Body budget: 2048 bytes max.
## Anti-Pattern
1. top_k too low: Misses relevant chunks, especially with imprecise queries
2. No score threshold: Returns irrelevant results when no good match exists
3. Dense-only for keyword queries: Semantic search fails on exact terms, codes, IDs
4. No reranker on large top_k: Returns many results but wrong order
## Context
The 2048-byte body limit keeps retriever_config artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_retriever_config_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-retriever-config-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | retriever_config |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_retriever_config]] | upstream | 0.46 |
| [[p10_lr_chunk_strategy_builder]] | sibling | 0.46 |
| [[p10_lr_handoff_protocol_builder]] | sibling | 0.42 |
| [[p10_lr_output_validator_builder]] | sibling | 0.42 |
| [[p03_sp_retriever_config_builder]] | upstream | 0.41 |
| [[p10_lr_memory_scope_builder]] | sibling | 0.41 |
| [[p10_lr_prompt_version_builder]] | sibling | 0.40 |
| [[p10_lr_constraint_spec_builder]] | sibling | 0.40 |
| [[bld_instruction_retriever_config]] | upstream | 0.37 |
| [[bld_examples_retriever_config]] | upstream | 0.36 |
