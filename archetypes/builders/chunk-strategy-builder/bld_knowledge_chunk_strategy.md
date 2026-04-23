---
kind: knowledge_card
id: bld_knowledge_card_chunk_strategy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for chunk_strategy production
sources: LangChain text_splitter module, LlamaIndex node_parser, Unstructured chunking, semantic chunking research (Anthropic, Greg Kamradt)
quality: 9.0
title: "Knowledge Card Chunk Strategy"
version: "1.0.0"
author: n03_builder
tags: [chunk_strategy, builder, examples]
tldr: "Golden and anti-examples for chunk strategy construction, demonstrating ideal structure and common pitfalls."
domain: "chunk strategy construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_chunk_strategy_builder
  - p01_kc_chunk_strategy
  - p01_kc_rag_chunking_strategies
  - p01_chunk_strategy
  - p03_sp_chunk_strategy_builder
  - bld_knowledge_card_document_loader
  - bld_knowledge_card_retriever_config
  - n01_emb_text_embedding_4
  - bld_instruction_chunk_strategy
  - chunk-strategy-builder
---

# Domain Knowledge: chunk_strategy
## Executive Summary
Chunking method configuration — how to split documents into retrievable segments. Produced as P01 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 |
| llm_function | CONSTRAIN |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Fixed-size | Split by token/char count with overlap | Uniform corpus, known embedding window |
| Recursive character | Try separators in priority order (\n\n, \n, ., ' ') | Mixed-format documents, general-purpose |
| Semantic | Split on embedding similarity boundaries | Preserving topic coherence, variable-length chunks |
| Document-structure | Split on headings, sections, pages | Structured documents (HTML, Markdown, PDF) |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Zero overlap | Cuts context at chunk boundaries, retriever misses split answers |
| Chunk too large | Exceeds embedding model context, wastes tokens on irrelevant content |
| Chunk too small | Loses context, increases retrieval noise |
| Ignoring document structure | Splits mid-table or mid-code-block |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p01_chunk_[a-z][a-z0-9_]+$`
## References
- LangChain TextSplitter, LlamaIndex NodeParser, Unstructured ChunkingStrategy, Haystack DocumentSplitter
- LangChain text_splitter module, LlamaIndex node_parser, Unstructured chunking, semantic chunking research (Anthropic, Greg Kamradt)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_chunk_strategy_builder]] | downstream | 0.53 |
| [[p01_kc_chunk_strategy]] | sibling | 0.43 |
| [[p01_kc_rag_chunking_strategies]] | sibling | 0.34 |
| [[p01_chunk_strategy]] | related | 0.32 |
| [[p03_sp_chunk_strategy_builder]] | related | 0.32 |
| [[bld_knowledge_card_document_loader]] | sibling | 0.30 |
| [[bld_knowledge_card_retriever_config]] | sibling | 0.29 |
| [[n01_emb_text_embedding_4]] | related | 0.29 |
| [[bld_instruction_chunk_strategy]] | downstream | 0.28 |
| [[chunk-strategy-builder]] | related | 0.26 |
