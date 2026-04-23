---
id: p01_embedding_config_supabase
kind: embedding_config
pillar: P01
title: "Embedding Config — pgvector in Supabase"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [embedding-config, supabase, pgvector, dimensions, hnsw, N04]
tldr: "pgvector embedding config: VECTOR(1536) default, HNSW index, cosine distance, match_documents() function, multi-tenant via RLS"
density_score: 0.91
related:
  - p01_kc_supabase_vectors
  - p01_kc_supabase_pgvector_rag_setup
  - p01_rag_source_supabase
  - bld_collaboration_embedding_config
  - p01_gl_embedding
  - p01_kc_embedding_config
  - p03_sp_vector_store_builder
  - p01_kc_vector_embedding_model_selection
  - vector-store-builder
  - p06_schema_database
---

# Embedding Config: pgvector

## Default Configuration
```yaml
extension: pgvector
version: "0.7+"
column_type: "VECTOR(1536)"
index_type: hnsw
index_params:
  m: 16
  ef_construction: 64
distance_function: cosine
operator: "<=> (vector_cosine_ops)"
```

## Model → Dimension Mapping
| Model | Dimensions | Column | Index Ops |
|-------|-----------|--------|-----------|
| text-embedding-3-small | 1536 | VECTOR(1536) | vector_cosine_ops |
| text-embedding-3-large | 3072 | VECTOR(3072) | vector_cosine_ops |
| nomic-embed-text | 768 | VECTOR(768) | vector_cosine_ops |
| Cohere embed-v3 | 1024 | VECTOR(1024) | vector_cosine_ops |

## Index Selection
| Rows | Index | Build | Query | Recall |
|------|-------|-------|-------|--------|
| <1K | None (brute force) | 0 | Slow | 100% |
| 1K-100K | IVFFlat | Fast | Medium | ~95% |
| >1K | HNSW | Slow | Fast | ~98% |

## Setup SQL
```sql
-- Enable
CREATE EXTENSION IF NOT EXISTS vector;

-- Table
CREATE TABLE documents (
  id BIGSERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index
CREATE INDEX idx_documents_embedding
  ON documents USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);

-- RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "org_scoped" ON documents
  FOR ALL USING (
    (metadata->>'org_id') = (auth.jwt()->'app_metadata'->>'org_id')
  );

-- Search function
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding VECTOR(1536),
  match_threshold FLOAT DEFAULT 0.78,
  match_count INT DEFAULT 10
) RETURNS TABLE (id BIGINT, content TEXT, metadata JSONB, similarity FLOAT)
LANGUAGE sql STABLE AS $$
  SELECT id, content, metadata,
    1 - (embedding <=> query_embedding) AS similarity
  FROM documents
  WHERE 1 - (embedding <=> query_embedding) > match_threshold
  ORDER BY embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Tuning Parameters
| Parameter | Default | Tradeoff |
|-----------|---------|----------|
| m (HNSW) | 16 | Higher = better recall, more memory |
| ef_construction | 64 | Higher = better index, slower build |
| ef_search | 40 | Higher = better recall, slower query |
| match_threshold | 0.78 | Higher = more precise, fewer results |
| match_count | 10 | Higher = more context, more tokens |
| chunk_size | 500 tokens | Larger = more context, less precise |
| chunk_overlap | 50 tokens | More = smoother boundaries, redundancy |

## Distance Functions
| Function | Operator | When |
|----------|----------|------|
| Cosine | `<=>` | Default for text embeddings |
| Inner product | `<#>` | MRL/matryoshka embeddings |
| L2 (Euclidean) | `<->` | Image embeddings, spatial |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_vectors]] | related | 0.61 |
| [[p01_kc_supabase_pgvector_rag_setup]] | related | 0.60 |
| [[p01_rag_source_supabase]] | related | 0.40 |
| [[bld_collaboration_embedding_config]] | downstream | 0.38 |
| [[p01_gl_embedding]] | related | 0.34 |
| [[p01_kc_embedding_config]] | related | 0.34 |
| [[p03_sp_vector_store_builder]] | downstream | 0.31 |
| [[p01_kc_vector_embedding_model_selection]] | related | 0.31 |
| [[vector-store-builder]] | downstream | 0.31 |
| [[p06_schema_database]] | downstream | 0.31 |
