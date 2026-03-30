---
id: p10_lr_chunk_strategy_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "chunk_strategy artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from LangChain TextSplitter, LlamaIndex NodeParser, Unstructured ChunkingStrategy, Haystack DocumentSplitter documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: chunk_strategy
tags: [chunk-strategy, P01, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_node: edison
keywords: [chunk strategy, fixed-size, recursive character, semantic, document-structure]
---

## Summary
Chunking method configuration — how to split documents into retrievable segments. The difference between a useful chunk_strategy and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Method, Parameters, Integration.
Body budget: 2048 bytes max.
## Anti-Pattern
- Zero overlap: Cuts context at chunk boundaries, retriever misses split answers
- Chunk too large: Exceeds embedding model context, wastes tokens on irrelevant content
- Chunk too small: Loses context, increases retrieval noise
- Ignoring document structure: Splits mid-table or mid-code-block
## Context
The 2048-byte body limit keeps chunk_strategy artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
