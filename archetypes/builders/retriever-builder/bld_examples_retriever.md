---
kind: examples
id: bld_examples_retriever
pillar: P07
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [examples, retriever, P07, RAG, vector-search, hybrid-search]
density_score: 1.0
domain: "examples artifact construction"
title: "Examples Retriever"
---
# Examples: retriever-builder

## Golden Example

**INPUT**: "Create a hybrid retriever for a Qdrant store using Cohere embed-v3 embeddings
with reranking for a technical documentation RAG system."

**OUTPUT**:
```markdown
---
id: p04_retr_qdrant_hybrid_docs
kind: retriever
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: retriever-builder
name: "Qdrant Hybrid Retriever — Technical Docs"
store_type: qdrant
embedding_model: embed-english-v3.0
similarity_metric: dot_product
top_k: 50
search_type: hybrid
reranker: rerank-english-v3.0
metadata_filters: [source, version, category, language]
namespace: technical_docs
quality: null
tags: [retriever, qdrant, hybrid, cohere, reranking, technical-docs]
tldr: "Qdrant hybrid retriever using Cohere embed-v3 + BM25 with Cohere reranking for technical documentation RAG."
description: "Searches technical documentation collection using dense+sparse fusion, reranks top-50 to top-5 for precision."
---

## Overview
Qdrant vector store serving a technical documentation corpus. Uses Cohere embed-english-v3.0
(1024d, natively normalized) as the dense encoder. Designed for developer documentation RAG
where exact API names (keyword) and semantic intent (vector) both matter.

## Search Strategy
Hybrid search combining Qdrant's dense vectors with sparse BM25 index. Fusion via
Reciprocal Rank Fusion (RRF, k=60): balances semantic similarity and exact term matching
for technical queries like "list all methods of class X" or "explain async context manager."
dot_product metric used because Cohere embed-v3 vectors are natively normalized.
Cohere rerank-english-v3.0 applied after first-pass top_k=50 to return final top-5.

## Configuration
- top_k: 50 (first-pass); reranker returns top 5 for generation
- metadata_filters: source (file path), version (doc version string), category (api/guide/tutorial), language (en/pt)
- namespace: technical_docs
- score_threshold: 0.35 (discard low-confidence matches before reranking)
- chunk_size_assumption: 512 tokens from document_loader

## Integration
- SDK/library: qdrant-client + langchain QdrantVectorStore + cohere Python SDK
- auth: QDRANT_API_KEY env var (cloud) or none (local http://localhost:6333)
- connection: QDRANT_URL + QDRANT_API_KEY env vars; collection name = "technical_docs"
- embedding_call: CohereEmbeddings(model="embed-english-v3.0", input_type="search_query")
```

**WHY GOLDEN**: H01-H10 all pass. S01-S12 average ~9.4 — qdrant+Cohere+RRF+reranker+metadata+SDK all documented.

---

## Anti-Example

**INPUT**: "Create retriever"

**BAD OUTPUT**:
```markdown
---
id: retriever_1
kind: retriever
store_type: vector
embedding_model: embeddings
top_k: 100
quality: 8.5
tags: [search]
---
Searches documents using vectors.
```

**FAILURES**:
- H01: parses but H02 fails — id "retriever_1" does not match `^p04_retr_[a-z][a-z0-9_]+$`
- H03: kind == "retriever" passes but H04 fails — quality: 8.5 (must be null)
- H05: missing name, similarity_metric; pillar, version, created, updated, author, tldr all absent
- H06: store_type "vector" is not a valid enum value
- H07: embedding_model "embeddings" is too vague — no provider or model name
- H08: similarity_metric absent
- S01-S12: ~1.2/10 — no strategy, no config, no integration
- Body 1 line — missing Overview, Search Strategy, Configuration, Integration

## Cross-References

- **Pillar**: P07 (Evals)
- **Kind**: `examples`
- **Artifact ID**: `bld_examples_retriever`
- **Tags**: [examples, retriever, P07, RAG, vector-search, hybrid-search]

## Example Registry

| Aspect | Detail |
|--------|--------|
| Purpose | Few-shot exemplar for builder prompts |
| Injection | Loaded by `cex_skill_loader.py` at F3 |
| Quality | Must score 9.0+ to serve as exemplar |
