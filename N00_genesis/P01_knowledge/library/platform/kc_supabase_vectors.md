---
id: p01_kc_supabase_vectors
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Vectors — pgvector, Embeddings, Semantic Search, RAG"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, pgvector, vectors, embeddings, rag, semantic-search, platform]
tldr: "Native pgvector in PostgreSQL: vector(1536), HNSW/IVFFlat indexes, match_documents() for semantic search, integrates with OpenAI/Cohere/local embeddings"
when_to_use: "When configuring embeddings, semantic search, or RAG pipeline with Supabase"
keywords: [pgvector, embeddings, semantic-search, rag, supabase-vectors]
long_tails:
  - How to create a table with vector column in Supabase
  - HNSW vs IVFFlat for embedding indexes in pgvector
  - match_documents function for semantic search in Supabase
axioms:
  - ALWAYS create HNSW index for tables with >1000 vectors
  - NEVER store embeddings without metadata (content, source, created_at)
  - ALWAYS use RLS on embedding tables for multi-tenant isolation
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_auth]
density_score: 0.91
data_source: "https://supabase.com/docs/guides/ai"
related:
  - p01_kc_supabase_pgvector_rag_setup
  - p01_embedding_config_supabase
  - p01_rag_source_supabase
  - bld_collaboration_embedding_config
  - p01_gl_embedding
  - p01_emb_openai_text_embedding_3_small
  - p03_sp_vector_store_builder
  - bld_examples_embedder_provider
  - p01_kc_vector_embedding_model_selection
  - p06_schema_database
---

# Supabase Vectors — pgvector + RAG

## Quick Reference
```yaml
topic: supabase_vectors
scope: pgvector, embeddings, HNSW, IVFFlat, semantic search, RAG
owner: n04_knowledge
criticality: high
extension: pgvector (enable: create extension vector)
n04_connection: concrete backend for N04 RAG/embeddings
```

## Initial Setup
```sql
-- 1. Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Create table with embedding column
CREATE TABLE documents (
  id BIGSERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),  -- OpenAI ada-002 / text-embedding-3-small
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. RLS mandatory
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "owner_read" ON documents
  FOR SELECT USING (metadata->>'org_id' = (auth.jwt()->'app_metadata'->>'org_id'));

-- 4. HNSW index (recommended for >1000 rows)
CREATE INDEX ON documents
  USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);
```

## Modelos de Embedding
| Model | Dim | Cost/1M tok |
|--------|-----|-------------|
| text-embedding-3-small (OpenAI) | 1536 | USD 0.02 |
| text-embedding-3-large (OpenAI) | 3072 | USD 0.13 |
| nomic-embed-text (local) | 768 | Free |
| Cohere embed-v3 | 1024 | USD 0.10 |

## Index Types
| Index | When to Use | Build Time | Query Speed | Recall |
|-------|-------------|------------|-------------|--------|
| None | <1000 rows | 0 | Slow (exact) | 100% |
| IVFFlat | 1K-100K rows, fast build | Fast | Medium | ~95% |
| HNSW | >1K rows, frequent queries | Slow | Fast | ~98% |

```sql
-- IVFFlat (faster to build)
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- HNSW (faster for queries)
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);
```

## Distance Functions
| Operator | Function | When to Use |
|----------|----------|-------------|
| `<=>` | vector_cosine_ops | Default: normalized embeddings (OpenAI, Cohere) |
| `<#>` | vector_ip_ops | Inner product (MRL, matryoshka) |
| `<->` | vector_l2_ops | L2/Euclidean (images, spatial) |

## Match Function (Semantic Search)
```sql
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding VECTOR(1536),
  match_threshold FLOAT DEFAULT 0.78,
  match_count INT DEFAULT 10
)
RETURNS TABLE (id BIGINT, content TEXT, metadata JSONB, similarity FLOAT)
LANGUAGE sql STABLE
AS $$
  SELECT id, content, metadata,
    1 - (embedding <=> query_embedding) AS similarity
  FROM documents
  WHERE 1 - (embedding <=> query_embedding) > match_threshold
  ORDER BY embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Hybrid Search (BM25 + Vector)
```sql
-- Combine full-text with vector: weights 0.3 BM25 + 0.7 vector
SELECT id, content,
  (0.3 * ts_rank(fts, q) + 0.7 * (1 - (embedding <=> vec))) AS score
FROM documents, plainto_tsquery('portuguese','termo') q
WHERE fts @@ q ORDER BY score DESC LIMIT 10;
```

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| No index on >1K rows | Sequential query scan, timeout | HNSW or IVFFlat |
| Wrong dimensions | Insert fails silently | Match exact model dimensions |
| No metadata | Impossible to filter by source/date | JSONB metadata mandatory |
| Embedding without RLS | Tenant A sees tenant B data | RLS by org_id/user_id |

## Golden Rules
- MATCH VECTOR(N) column dimensions with the exact model
- INDEX with HNSW for any production table
- COMBINE vector search with BM25 for hybrid retrieval
- STORE source/chunk_index in metadata for traceability

## References
- Docs: https://supabase.com/docs/guides/ai
- pgvector: https://github.com/pgvector/pgvector
- Embeddings: https://supabase.com/docs/guides/ai/vector-columns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_pgvector_rag_setup]] | sibling | 0.69 |
| [[p01_embedding_config_supabase]] | related | 0.68 |
| [[p01_rag_source_supabase]] | related | 0.53 |
| [[bld_collaboration_embedding_config]] | downstream | 0.43 |
| [[p01_gl_embedding]] | related | 0.37 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.36 |
| [[p03_sp_vector_store_builder]] | downstream | 0.35 |
| [[bld_examples_embedder_provider]] | downstream | 0.34 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.34 |
| [[p06_schema_database]] | downstream | 0.33 |
