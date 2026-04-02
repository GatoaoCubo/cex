---
id: p10_out_embedding_batch
kind: output
pillar: P10
title: "Output: Embedding Batch"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 8.5
tags: [output, n04, embedding, vector, batch, supabase]
tldr: "Batch embedding export: chunked KC text + vectors for Supabase/vector DB ingestion."
density_score: 0.91
---

# Output: Embedding Batch

## Format
```json
{"kc_id": "p01_kc_chain_of_thought", "chunk_index": 0, "chunk_text": "CoT elicits intermediate reasoning...", "model": "text-embedding-3-small"}
{"kc_id": "p01_kc_chain_of_thought", "chunk_index": 1, "chunk_text": "Variants: zero-shot, few-shot...", "model": "text-embedding-3-small"}
```

## Pipeline
```
KCs → chunk (per embedding_contract) → embed (API call) → insert (Supabase)
```

## Usage

| Scenario | Implementation |
|----------|---------------|
| **Supabase vector search** | `INSERT INTO embeddings (kc_id, chunk_index, text, embedding) VALUES ...` |
| **Semantic similarity** | Query: `SELECT * FROM embeddings ORDER BY embedding <-> query_vector LIMIT 10` |
| **RAG pipeline** | Retrieve chunks → rank by cosine similarity → inject into LLM context |
| **Bulk index rebuild** | Process all KCs in batches of 50 → rate-limit API calls → upsert vectors |

## Batch Metadata
```json
{"_meta": {"total_kcs": 243, "total_chunks": 890, "model": "text-embedding-3-small", "dimensions": 1536, "generated": "2026-03-31"}}
```