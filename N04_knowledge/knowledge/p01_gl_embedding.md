---
id: p01_gl_embedding
kind: glossary_entry
pillar: P01
title: "Embedding"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: null
tags: [glossary, embedding, vector, similarity]
tldr: "A fixed-length float vector representing text semantics, enabling similarity search via cosine distance in vector stores."
density_score: 0.96
---

# Embedding

**Term**: Embedding
**Abbreviation**: emb
**Synonyms**: vector representation, text embedding, dense vector

**Definition**: A fixed-length array of floating-point numbers (typically 384–3072 dimensions) that represents the semantic meaning of a text passage. Produced by embedding models (OpenAI `text-embedding-3-*`, Voyage `voyage-3`, local SBERT). Stored in vector databases (pgvector, FAISS). Retrieved via cosine similarity, dot product, or L2 distance. The numeric substrate of RAG pipelines.

**See**: `embedding_config`, `embedder_provider`, `vector_store`
