---
id: p08_dir_rag_pipeline
kind: supervisor
pillar: P08
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
name: "RAG Pipeline Supervisor"
description: "Orchestrates the RAG pipeline: document ingestion, chunking, embedding, indexing, retrieval, and generation"
crew_size: 5
execution_mode: pipeline
domain: "rag"
quality: 9.1
tags: [supervisor, rag, pipeline, orchestration, P08]
tldr: "Crew supervisor for RAG pipeline: document-loader -> parser -> embedding-config -> retriever -> prompt-template in strict sequence."
density_score: 0.91
related:
  - bld_collaboration_retriever
  - p01_kc_document_loader
  - bld_collaboration_retriever_config
  - bld_architecture_embedding_config
  - bld_architecture_document_loader
  - bld_collaboration_document_loader
  - bld_collaboration_embedding_config
  - bld_collaboration_response_format
  - bld_collaboration_chunk_strategy
  - document_loader-builder
---
## Overview
Orchestrates a 5-builder crew for Retrieval-Augmented Generation pipelines. Each builder produces one artifact in strict pipeline order — output of each stage feeds as input to the next. No parallelism; each stage depends on the previous.
## Crew Roster
| Order | Builder | Produces | Depends On |
|-------|---------|----------|------------|
| 1 | document-loader-builder | document_loader spec (source, format, chunking) | none |
| 2 | parser-builder | parser spec (chunk boundaries, metadata extraction) | document_loader output format |
| 3 | embedding-config-builder | embedding_config (model, dimensions, batch size) | parser chunk schema |
| 4 | retriever-builder | retriever spec (index, similarity, top_k, filters) | embedding_config dimensions |
| 5 | prompt-template-builder | prompt_template (context injection, generation) | retriever output schema |
## Execution Flow
```
[Documents] -> document-loader -> [Raw chunks]
[Raw chunks] -> parser -> [Structured chunks + metadata]
[Structured chunks] -> embedding-config -> [Vectors]
[Vectors] -> retriever -> [Top-K relevant chunks]
[Top-K chunks] -> prompt-template -> [Augmented prompt -> LLM -> Response]
```
## Handoff Contracts
### document-loader -> parser
```yaml
provides: {format: "text|pdf|html", chunk_size: int, overlap: int}
```
### parser -> embedding-config
```yaml
provides: {chunk_schema: {text: string, metadata: object}, avg_tokens: int}
```
### embedding-config -> retriever
```yaml
provides: {model: string, dimensions: int, similarity_metric: "cosine|dot|euclidean"}
```
### retriever -> prompt-template
```yaml
provides: {results_schema: [{text: string, score: float, metadata: object}], top_k: int}
```
## Failure Handling
| Stage | Failure | Action |
|-------|---------|--------|
| document-loader | Unsupported format | HALT — cannot proceed without source |
| parser | Chunk too large for embedding model | Reduce chunk_size, retry once |
| embedding-config | Model unavailable | Fallback to text-embedding-3-small |
| retriever | Zero results | Expand query, lower similarity threshold |
| prompt-template | Context exceeds context window | Truncate lowest-score chunks |
## Constraints
1. Pipeline is strictly sequential — no stage may run before its predecessor completes
2. Total pipeline latency target: < 5s for retrieval path (stages 4-5)
3. Document ingestion (stages 1-3) may be async/batch — not latency-critical

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_retriever]] | downstream | 0.39 |
| [[p01_kc_document_loader]] | upstream | 0.37 |
| [[bld_collaboration_retriever_config]] | downstream | 0.37 |
| [[bld_architecture_embedding_config]] | related | 0.37 |
| [[bld_architecture_document_loader]] | upstream | 0.35 |
| [[bld_collaboration_document_loader]] | upstream | 0.34 |
| [[bld_collaboration_embedding_config]] | downstream | 0.34 |
| [[bld_collaboration_response_format]] | upstream | 0.31 |
| [[bld_collaboration_chunk_strategy]] | downstream | 0.31 |
| [[document_loader-builder]] | upstream | 0.30 |
