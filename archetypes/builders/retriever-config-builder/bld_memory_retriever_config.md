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
agent_node: edison
keywords: [retriever config, dense-only, sparse-only, hybrid, reranked]
memory_scope: project
observation_types: [user, feedback, project, reference]
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
- top_k too low: Misses relevant chunks, especially with imprecise queries
- No score threshold: Returns irrelevant results when no good match exists
- Dense-only for keyword queries: Semantic search fails on exact terms, codes, IDs
- No reranker on large top_k: Returns many results but wrong order
## Context
The 2048-byte body limit keeps retriever_config artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
