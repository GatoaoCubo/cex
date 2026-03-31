---
id: n01_emb_intelligence_config
kind: embedding_config
pillar: P01
title: "Embedding Config for N01 Intelligence RAG"
version: "2.0.0"
created: "2026-03-30"
updated: "2026-03-31"
author: "N07_peer_review"
model_name: "text-embedding-004"
provider: "Google"
dimensions: 768
chunk_size: 512
chunk_overlap: 64
quality: 8.9
tags: [embedding, config, n01, rag, intelligence, vector, google]
tldr: "text-embedding-004 at 768 dimensions for N01 Intelligence RAG — optimized for research papers, market reports, and technical documentation."
density_score: 0.88
---

## Purpose

Defines the vector embedding model and chunking strategy for all documents ingested into the **N01 Intelligence Nucleus** knowledge base. This configuration drives the accuracy and relevance of N01's Retrieval-Augmented Generation (RAG) capabilities across research papers, competitor analyses, and market reports.

## Model Selection

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | `text-embedding-004` | Top-tier MTEB performance, native Gemini integration |
| Provider | Google | Same ecosystem as N01's LLM (gemini-2.5-pro) |
| Dimensions | 768 | Rich semantic representation, efficient for large-scale search |
| Distance Metric | cosine | Standard for normalized embeddings |
| Max Tokens | 8192 | Handles long academic abstracts without truncation |
| Batch Size | 32 | Optimal throughput for bulk ingestion |
| Normalize | true | Required for cosine similarity |

## Chunking Strategy

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Chunk Size | 512 tokens | Balance between contextual richness and vector specificity |
| Overlap | 64 tokens | Preserves semantic continuity at chunk boundaries |
| Tokenizer | nomic-bert | Consistent token counting across ingestion pipeline |

**Design rationale**: Research papers contain dense, interconnected concepts. A 512-token chunk captures full paragraphs while remaining specific enough for precise retrieval. The 64-token overlap (12.5%) prevents information loss at boundaries — critical when a key finding spans two chunks.

## Domain-Specific Tuning

N01 ingests three primary document types with different characteristics:

1. **Research Papers** (arXiv, JSTOR): Dense academic prose, formulas, citations. Chunk at paragraph boundaries when possible.
2. **Market Reports** (industry analysts): Structured sections with tables and charts. Chunk at section headers.
3. **Competitor Docs** (product pages, press releases): Marketing-heavy, shorter. Smaller effective chunks (256-384 tokens).

## Performance Expectations

| Metric | Target |
|--------|--------|
| Latency per batch | < 100ms (Google API) |
| Throughput | ~2000 chunks/min |
| Recall@10 | > 0.85 for research queries |
| Cost | ~$0.00013 per 1K tokens |

## Integration

Deployed via Google's Vertex AI or direct API. Vectors stored in local FAISS index for development, with Pinecone/Weaviate as production targets. Compatible with N04 Knowledge Nucleus retrieval pipeline.
