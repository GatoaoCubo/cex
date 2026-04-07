---
id: p04_retr_pinecone
kind: retriever
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Pinecone Vector Retriever"
store_type: pinecone
embedding_model: text-embedding-3-small
similarity_metric: cosine
top_k: 10
search_type: vector
reranker: null
metadata_filters: [source, pillar, kind]
namespace: "default"
quality: 9.0
tags: [retriever, pinecone, vector, RAG]
tldr: "Pinecone vector retriever using text-embedding-3-small with cosine similarity, top-k=10"
description: "Searches Pinecone serverless index for semantically similar document chunks"
domain: "tool integration"
title: "Retriever Pinecone"
density_score: 0.95
---

# Pinecone Vector Retriever

## Overview
Searches a Pinecone serverless vector index using OpenAI text-embedding-3-small embeddings (1536 dimensions). Primary use case: RAG retrieval over ingested knowledge base documents.

## Search Strategy
Pure vector search using cosine similarity. Cosine chosen because text-embedding-3-small produces normalized vectors where cosine and dot product are equivalent. No reranker configured — top_k results returned directly.

## Configuration
- top_k: 10
- metadata_filters: source (string), pillar (string), kind (string)
- namespace: "default" (single-tenant)
- score_threshold: 0.7 (results below this are discarded)
- chunk_size_assumption: 512 tokens (from document_loader stage)

## Integration
- SDK: pinecone-client (Python), @pinecone-database/pinecone (Node)
- auth: env var `PINECONE_API_KEY`
- connection: env var `PINECONE_INDEX_NAME` for index host
- embedding_call: OpenAIEmbeddings(model="text-embedding-3-small")

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `retriever`
- **Artifact ID**: `p04_retr_pinecone`
- **Tags**: [retriever, pinecone, vector, RAG]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `retriever` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: retriever
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```
