---
id: p04_tool_embedding_batch
kind: cli_tool
pillar: P04
title: "Embedding Batch Processor — Bulk Vector Generation"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 9.0
tags: [tool, n04, embedding, batch, vector, pgvector]
tldr: "CLI tool for bulk embedding generation: chunk corpus, embed via API, upsert to pgvector, with rate limiting, resume, and progress tracking."
density_score: 0.92
related:
  - p10_out_embedding_batch
  - p01_emb_openai_text_embedding_3_small
  - p01_emb_nomic_embed_text
  - bld_knowledge_card_embedding_config
  - n01_emb_text_embedding_4
  - embedding-config-builder
  - bld_instruction_embedding_config
  - p06_schema_database
  - p01_kc_vector_embedding_model_selection
  - p06_arch_rag_pipeline
---

# Embedding Batch Processor

## Purpose

Processes the full CEX artifact corpus (2,184+ documents) into vector embeddings and upserts them to Supabase pgvector. Handles rate limits, failures, and incremental updates.

## Usage

```bash
# Full corpus embedding (first run)
python _tools/embedding_batch.py run --source P01_knowledge/ --model text-embedding-3-small --target supabase

# Incremental update (only new/modified artifacts)
python _tools/embedding_batch.py update --since 2026-04-07

# Dry run (estimate tokens + cost)
python _tools/embedding_batch.py estimate --source P01_knowledge/

# Resume interrupted batch
python _tools/embedding_batch.py resume --batch-id batch_20260407_001

# Verify embeddings match source
python _tools/embedding_batch.py verify --source P01_knowledge/ --target supabase
```

## Pipeline

```
Source files → Read + Parse frontmatter → Chunk (per chunk_strategy) → Embed (API) → Upsert (pgvector)
     │                                       │                            │              │
     │                                       ▼                            ▼              ▼
     │                              chunk_strategy config       Rate limiter        Batch ID
     │                              (256-2048 tokens)           (60 RPM / 1M TPM)   + progress
     ▼
  Skip compiled/*.yaml
  Skip binary files
  Skip files < 100 bytes
```

## Configuration

| Parameter | Default | Override |
|-----------|---------|---------|
| Model | `text-embedding-3-small` | `--model text-embedding-3-large` |
| Chunk size | 512 tokens | `--chunk-size 1024` |
| Overlap | 64 tokens | `--overlap 128` |
| Batch size | 100 chunks per API call | `--batch-size 50` |
| Rate limit | 60 requests/min | `--rpm 30` |
| Retry | 3 attempts, exponential backoff | `--retries 5` |
| Target | Supabase pgvector | `--target local` (FAISS) |

## Cost Estimation

| Corpus | Chunks (est.) | Tokens (est.) | Cost (3-small) | Cost (3-large) |
|--------|--------:|----------:|-------:|-------:|
| P01 Knowledge (197) | ~800 | ~400K | $0.008 | $0.052 |
| All N04 artifacts (43) | ~200 | ~100K | $0.002 | $0.013 |
| Full CEX corpus (2,184) | ~9,000 | ~4.5M | $0.090 | $0.585 |

## Supabase Table Schema

```sql
CREATE TABLE IF NOT EXISTS cex_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    artifact_path TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding VECTOR(1536),  -- or 3072 for large model
    kind TEXT,
    pillar TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(artifact_path, chunk_index)
);

CREATE INDEX ON cex_embeddings USING hnsw (embedding vector_cosine_ops);
```

## Error Handling

| Error | Action | Resume |
|-------|--------|--------|
| Rate limit (429) | Exponential backoff (1s → 2s → 4s → 8s) | Automatic |
| API timeout | Retry up to 3x, then skip + log | Skip logged in batch manifest |
| Duplicate chunk | Upsert (ON CONFLICT UPDATE) | Idempotent |
| Invalid UTF-8 | Skip + log warning | Continue batch |
| Supabase connection lost | Retry 3x, then pause batch | Resume from last successful chunk |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_embedding_batch]] | downstream | 0.43 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.36 |
| [[p01_emb_nomic_embed_text]] | upstream | 0.34 |
| [[bld_knowledge_card_embedding_config]] | upstream | 0.29 |
| [[n01_emb_text_embedding_4]] | upstream | 0.29 |
| [[embedding-config-builder]] | upstream | 0.28 |
| [[bld_instruction_embedding_config]] | upstream | 0.28 |
| [[p06_schema_database]] | downstream | 0.27 |
| [[p01_kc_vector_embedding_model_selection]] | upstream | 0.27 |
| [[p06_arch_rag_pipeline]] | downstream | 0.27 |
