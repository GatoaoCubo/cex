---
id: p10_out_embedding_batch
kind: output
8f: F6_produce
pillar: P10
title: "Output: Embedding Batch"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [output, n04, embedding, vector, batch, supabase]
tldr: "Batch embedding export: chunked KC text + vectors for Supabase/vector DB ingestion."
density_score: 0.91
related:
  - p04_tool_embedding_batch
  - p06_schema_database
  - p01_emb_openai_text_embedding_3_small
  - bld_collaboration_embedding_config
  - p01_kc_embedder_provider
  - p06_schema_embedding
  - p01_gl_embedding
  - embedding-config-builder
  - bld_architecture_embedding_config
  - p08_dir_rag_pipeline
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

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|---------|--------------|
| **Single large batch** (500+ chunks) | Batch in groups of 50-100 to avoid timeouts |
| **No duplicate detection** | Check existing chunks before embedding to avoid waste |
| **Blocking API calls** | Use async/await for parallel embedding requests |
| **Missing error recovery** | Retry failed embeddings with exponential backoff |

## Batch Metadata
```json
{"_meta": {"total_kcs": 243, "total_chunks": 890, "model": "text-embedding-3-small", "dimensions": 1536, "generated": "2026-03-31"}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_embedding_batch]] | upstream | 0.46 |
| [[p06_schema_database]] | upstream | 0.44 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.42 |
| [[bld_collaboration_embedding_config]] | downstream | 0.40 |
| [[p01_kc_embedder_provider]] | upstream | 0.39 |
| [[p06_schema_embedding]] | upstream | 0.37 |
| [[p01_gl_embedding]] | upstream | 0.37 |
| [[embedding-config-builder]] | upstream | 0.36 |
| [[bld_architecture_embedding_config]] | upstream | 0.34 |
| [[p08_dir_rag_pipeline]] | upstream | 0.34 |
