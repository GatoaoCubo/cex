---
id: p01_chunk_strategy
kind: chunk_strategy
8f: F3_inject
pillar: P01
version: 1.0.0
title: "Template — Chunk Strategy"
tags: [template, chunk, rag, splitting]
tldr: "Defines how documents are split into retrievable chunks for RAG pipelines. Controls size, overlap, boundary detection, and metadata propagation."
quality: 9.0
related:
  - p01_kc_chunk_strategy
  - p01_kc_rag_chunking_strategies
  - bld_knowledge_card_chunk_strategy
  - p06_schema_embedding
  - p10_lr_chunk_strategy_builder
  - bld_collaboration_chunk_strategy
  - chunk-strategy-builder
  - bld_knowledge_card_embedding_config
  - bld_examples_chunk_strategy
  - p06_arch_rag_pipeline
---

# Chunk Strategy Template

## Purpose
Configure how source documents are split into chunks for embedding and retrieval. A chunk strategy balances granularity (small = precise) vs context (large = coherent).

## Configuration
```yaml
id: p01_cs_[STRATEGY_NAME]
kind: chunk_strategy
method: [heading_based | fixed_tokens | semantic | sentence]
max_tokens: [256 | 512 | 1024]
overlap_tokens: [0 | 32 | 64 | 128]
boundary: [heading | paragraph | sentence | none]
metadata_propagate: [title, source_url, section_path]
```

## Methods

| Method | Best For | Chunk Size | Boundary |
|--------|----------|------------|----------|
| heading_based | Docs with ## structure | Variable | `## ` markers |
| fixed_tokens | Uniform corpora | Fixed 512 | Token count |
| semantic | Dense prose | Variable | Topic shift |
| sentence | Short texts, Q&A | 1-3 sentences | `.` `?` `!` |

## Overlap Strategy
- `0`: No overlap — fastest, may lose context at boundaries
- `32-64`: Light overlap — good for structured docs
- `128`: Heavy overlap — best for dense prose, 2x storage cost

## Boundary Rules
- **heading_based**: Split at `## ` lines, keep heading as chunk prefix
- **fixed_tokens**: Split at nearest sentence boundary within ±10% of target
- **semantic**: Use embedding similarity; split when cosine drops below 0.7
- **sentence**: Split at sentence boundaries using spaCy/nltk

## Metadata Propagation
Each chunk inherits metadata from its source document:
- `source_url` — origin document URL
- `section_path` — hierarchical path (e.g., `docs > api > auth`)
- `chunk_index` — position within document (0-based)
- `total_chunks` — total chunks from this document

## Quality Gate
- [ ] `max_tokens` ≤ embedding model's context window
- [ ] `overlap_tokens` < `max_tokens / 2`
- [ ] At least 1 metadata field propagated
- [ ] Method matches document structure

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_chunk_strategy]] | related | 0.41 |
| [[p01_kc_rag_chunking_strategies]] | related | 0.39 |
| [[bld_knowledge_card_chunk_strategy]] | related | 0.38 |
| [[p06_schema_embedding]] | downstream | 0.33 |
| [[p10_lr_chunk_strategy_builder]] | downstream | 0.31 |
| [[bld_collaboration_chunk_strategy]] | downstream | 0.30 |
| [[chunk-strategy-builder]] | related | 0.28 |
| [[bld_knowledge_card_embedding_config]] | related | 0.27 |
| [[bld_examples_chunk_strategy]] | downstream | 0.27 |
| [[p06_arch_rag_pipeline]] | downstream | 0.26 |
