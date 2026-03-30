---
id: n01_emb_text_embedding_4
kind: embedding_config
pillar: P01
title: "Embedding Config for N01 RAG"
version: "1.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
model_name: "text-embedding-004"
provider: "Google"
dimensions: 768
chunk_size: 512
chunk_overlap: 64
quality: null
tags: [embedding, config, n01, rag, memory, vector]
tldr: "Specifies the text-embedding-004 model with 768 dimensions for N01's RAG knowledge base."
---

## Purpose
This document defines the standard vector embedding model and chunking strategy for all documents ingested into the **N01 Intelligence Nucleus** knowledge base. This configuration is critical for the performance and accuracy of its Retrieval-Augmented Generation (RAG) capabilities.

## Model Rationale
- **Model**: `text-embedding-004`
- **Provider**: Google
- **Reasoning**: As of its release, `text-embedding-004` is a state-of-the-art model offering top-tier performance on the MTEB (Massive Text Embedding Benchmark). Its 768 dimensions provide a rich semantic representation while remaining efficient for large-scale vector search operations. Native integration with the `gemini-2.5-pro` model ensures optimal compatibility and performance.

## Chunking Strategy
- **Chunk Size**: `512 tokens`
- **Overlap**: `64 tokens`
- **Reasoning**: A chunk size of 512 tokens is chosen as an optimal balance between two competing needs:
    1.  **Contextual Richness**: Chunks must be large enough to contain complete semantic units (paragraphs, concepts).
    2.  **Vector Specificity**: Chunks must be small enough so that the resulting vector accurately represents a specific piece of information.
- The 64-token overlap ensures that semantic context is not lost at the boundaries between chunks, improving the retriever's ability to find relevant passages that span across chunk divisions.
