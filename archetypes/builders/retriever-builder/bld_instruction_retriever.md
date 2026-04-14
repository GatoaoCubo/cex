---
kind: instruction
id: bld_instruction_retriever
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for retriever artifacts
pattern: 3-phase pipeline (Research -> Compose -> Validate)
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [instruction, retriever, P03, RAG, vector-search]
density_score: 0.86
domain: "instruction artifact construction"
title: "Instruction Retriever"
---
# Instructions: How to Produce a retriever

## Phase 1: RESEARCH

1. Identify the vector store backend — ask if not specified (Chroma, Pinecone, FAISS, Qdrant, Weaviate, Milvus, Elasticsearch, costm)
2. Determine the embedding model: name, provider, dimension size (e.g. text-embedding-3-small = 1536d)
3. Choose similarity metric based on embedding model recommendations:
   - OpenAI models: cosine (normalized) or dot_product
   - Cohere embed-v3: dot_product (natively normalized)
   - Sentence-transformers: cosine
   - Custom/unknown: cosine (safe default)
4. Decide search strategy:
   - vector: dense embeddings only — best for semantic similarity
   - keyword: BM25/TF-IDF — best for exact term matching
   - hybrid: RRF or weighted fusion — best for most production RAG
5. Define top_k: typical range 5-20; for reranking pipelines use top_k=50 then rerank to top 5
6. Decide reranker: Cohere rerank-v3, ColBERT, cross-encoder/ms-marco — only if top_k > 20 or precision critical
7. Map metadata_filters: which document fields can be filtered pre-search (e.g. source, date, category, language)
8. Confirm namespace/collection scoping — multi-tenant or single collection
9. Check for existing retriever artifacts to avoid duplicates (glob p04_retr_*.md)
10. Confirm store slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE

1. Read bld_schema_retriever.md — source of truth for all fields
2. Read bld_output_template_retriever.md — fill `{{vars}}` following schema constraints
3. Fill frontmatter: all required fields present, quality: null
4. Write `## Overview`: store backend, embedding model, use case context
5. Write `## Search Strategy`: vector/keyword/hybrid rationale, similarity metric justification, reranking if applicable
6. Write `## Configuration`: top_k value, metadata_filters list, namespace, score threshold if applicable
7. Write `## Integration`: SDK/library reference, auth pattern, connection string format (no secrets)
8. Measure body byte count — must be <= 2048 bytes
9. Verify id matches `^p04_retr_[a-z][a-z0-9_]+$` and equals filename stem

## Phase 3: VALIDATE

1. Open bld_quality_gate_retriever.md — verify each HARD gate in order
2. H01: YAML frontmatter parses without errors
3. H02: id matches `^p04_retr_[a-z][a-z0-9_]+$` and equals filename stem
4. H03: kind == "retriever"
5. H04: quality == null
6. H05: all required fields present (id, name, store_type, embedding_model, similarity_metric, top_k)
7. H06: store_type is valid enum value
8. H07: embedding_model is a non-empty string
9. H08: similarity_metric is valid enum value
10. H09: top_k >= 1
11. H10: body <= 2048 bytes
12. Score SOFT gates (target >= 7.0)
13. Boundary check: is this local store search? Not web? Not file ingestion? Not SQL?
14. If any HARD gate fails — fix before delivering artifact
