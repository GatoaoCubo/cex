---
id: bld_memory_document_loader
kind: learning_record
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: INJECT
observation: "Chunking strategy and metadata preservation are the two highest-leverage decisions in document_loader design — they determine retrieval quality for every downstream query."
pattern: "semantic chunking + 12.5% overlap + source/page/section metadata = best RAG baseline"
evidence: "LangChain benchmarks show semantic chunking outperforms fixed by 15-23% on multi-hop QA; overlap prevents answer-spanning-chunk misses"
confidence: 0.85
quality: 9.0
tags: [learning_record, document_loader, chunking, metadata, RAG, P04]
tldr: "Key lessons from document_loader builds: overlap is mandatory, metadata is non-negotiable, parser choice drives quality."
memory_scope: project
observation_types: [user, feedback, project, reference]
density_score: 0.99
title: Memory ISO - document_loader
related:
  - bld_knowledge_card_document_loader
  - p03_sp_document_loader_builder
  - p01_kc_chunk_strategy
  - bld_instruction_document_loader
  - p11_qg_document_loader
  - p08_dir_rag_pipeline
  - p01_kc_rag_chunking_strategies
  - bld_output_template_document_loader
  - p01_kc_document_loader
  - bld_knowledge_card_embedding_config
---
## Summary
Chunk strategy and metadata preservation are the two highest-leverage decisions in
document_loader design. A loader with wrong chunk_strategy or missing source metadata
degrades every downstream retrieval query — the damage is invisible at ingestion time
but catastrophic at query time.

## Pattern
**Semantic chunking + overlap + full metadata = RAG baseline**
- semantic > recursive > sentence > fixed for retrieval recall on open-domain QA
- recursive is safe default when semantic chunking infeasible (no embedding budget)
- overlap of 12.5% of chunk_size is minimum; 20% for highly dense technical text
- metadata must include: source, chunk_index, total_chunks, format, page (if paged format)

## Anti-Pattern
| Mistake | Symptom | Fix |
|---|---|---|
| overlap: 0 | Answers that span chunk boundaries never retrieved | Set overlap >= chunk_size * 0.125 |
| Missing source metadata | Citation impossible; retrieval results unverifiable | Always include source field |
| Ignoring encoding | Silent UnicodeDecodeError on ~8% of real-world corpora | Use chardet before open() |
| Single parser for all formats | HTML chunks contain nav/footer boilerplate; CSV as raw text | Per-format parser + post-processing step |
| chunk_size > 1024 tokens | Exceeds context window of smaller LLMs; dilutes retrieval score | Default 512; max 1024 for GPT-4 class |
| No corrupt file handling | Silent data loss — documents missing from index with no log | Try/except per file, emit partial doc + error_metadata |

## Context
- 2048 byte body budget: forces concise spec — use tables, not prose
- Retriever downstream: chunk quality directly determines retriever precision@k
- Embedding cost: smaller chunks = more embeddings = higher cost; balance with recall
- Unstructured.io auto-detects format for mixed-format corpora; single-format loaders
  should use format-specific parsers for higher fidelity
- Apache Tika covers 1000+ formats via JVM; use for rare formats before building costm parser

## Versioning Signals
- Bump minor version when adding new formats_supported
- Bump patch version when updating chunk_size or overlap defaults
- Bump major version when changing chunk_strategy or output_format (breaking change for downstream)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_document_loader]] | related | 0.46 |
| [[p03_sp_document_loader_builder]] | related | 0.36 |
| [[p01_kc_chunk_strategy]] | upstream | 0.35 |
| [[bld_instruction_document_loader]] | related | 0.32 |
| [[p11_qg_document_loader]] | downstream | 0.31 |
| [[p08_dir_rag_pipeline]] | downstream | 0.31 |
| [[p01_kc_rag_chunking_strategies]] | upstream | 0.29 |
| [[bld_output_template_document_loader]] | related | 0.29 |
| [[p01_kc_document_loader]] | upstream | 0.29 |
| [[bld_knowledge_card_embedding_config]] | upstream | 0.28 |
