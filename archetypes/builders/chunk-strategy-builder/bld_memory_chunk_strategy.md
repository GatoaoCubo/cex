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
agent_group: edison
keywords: [chunk strategy, fixed-size, recursive character, semantic, document-structure]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Chunk Strategy"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_chunk_strategy
  - p10_lr_retriever_config_builder
  - p10_lr_output_validator_builder
  - p10_lr_handoff_protocol_builder
  - p03_sp_chunk_strategy_builder
  - p10_lr_memory_scope_builder
  - p10_lr_constraint_spec_builder
  - p10_lr_prompt_version_builder
  - chunk-strategy-builder
  - bld_instruction_chunk_strategy
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
1. Zero overlap: Cuts context at chunk boundaries, retriever misses split answers
2. Chunk too large: Exceeds embedding model context, wastes tokens on irrelevant content
3. Chunk too small: Loses context, increases retrieval noise
4. Ignoring document structure: Splits mid-table or mid-code-block
## Context
The 2048-byte body limit keeps chunk_strategy artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_chunk_strategy_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-chunk-strategy-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | chunk_strategy |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_chunk_strategy]] | upstream | 0.49 |
| [[p10_lr_retriever_config_builder]] | sibling | 0.49 |
| [[p10_lr_output_validator_builder]] | sibling | 0.43 |
| [[p10_lr_handoff_protocol_builder]] | sibling | 0.43 |
| [[p03_sp_chunk_strategy_builder]] | upstream | 0.40 |
| [[p10_lr_memory_scope_builder]] | sibling | 0.40 |
| [[p10_lr_constraint_spec_builder]] | sibling | 0.39 |
| [[p10_lr_prompt_version_builder]] | sibling | 0.39 |
| [[chunk-strategy-builder]] | upstream | 0.39 |
| [[bld_instruction_chunk_strategy]] | upstream | 0.38 |
