---
id: p01_kc_supabase_pgvector_rag_setup
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Supabase pgvector Setup for RAG Pipelines"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: data_platform
quality: 9.2
tags: [supabase, pgvector, rag, embeddings, postgresql, vector-search, knowledge]
tldr: "Enable pgvector in Supabase, create VECTOR(1536) table, HNSW index, match_documents() RPC — full RAG backend in 5 SQL statements"
when_to_use: "When building RAG pipelines that need vector search co-located with PostgreSQL data, avoiding a separate vector DB"
keywords: [pgvector, supabase, rag, hnsw, embeddings, match_documents, semantic-search]
long_tails:
  - How to set up pgvector in Supabase for semantic search
  - Supabase HNSW index vs IVFFlat for RAG
  - How to implement match_documents RPC in Supabase pgvector
  - Supabase pgvector RLS multi-tenant vector setup
axioms:
  - ALWAYS enable RLS on vector tables before production deployment
  - NEVER skip HNSW index on tables exceeding 10k rows
  - ALWAYS use VECTOR(1536) for OpenAI ada-002 / text-embedding-3-small
  - IF multi-tenant THEN add user_id to metadata + RLS policy scoped to auth.uid()
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_vectors, p01_kc_rag_fundamentals]
density_score: 0.91
data_source: "https://supabase.com/docs/guides/ai/vector-columns"
related:
  - p01_embedding_config_supabase
  - p01_kc_supabase_vectors
  - p01_rag_source_supabase
  - p01_emb_openai_text_embedding_3_small
  - bld_collaboration_embedding_config
  - p01_gl_embedding
  - p06_schema_database
  - p03_sp_vector_store_builder
  - p01_kc_embedding_config
  - p01_kc_vector_embedding_model_selection
---
# Supabase pgvector Setup for RAG Pipelines

## Quick Reference
```yaml
topic: supabase_pgvector_rag_setup
scope: pgvector extension, HNSW index, match_documents RPC, RLS
owner: builder_agent
criticality: high
min_tier: Free (500MB DB included)
embedding_dim: 1536 (OpenAI) | 1024 (Cohere) | 768 (local)
```

## Key Concepts
- **pgvector**: PostgreSQL extension; `VECTOR(N)` column type; operators `<=>`, `<->`, `<#>`
- **HNSW**: Graph-based ANN index; no training needed; `m` controls graph degree, `ef_construction` recall
- **IVFFlat**: Centroid-based; requires `ANALYZE` post-insert; optimal for >500k rows with `lists` tuning
- **match_documents()**: PostgreSQL RPC returning top-k rows by cosine similarity score
- **RLS**: Row Level Security enforced at DB layer — same table, per-tenant isolation
- **Cosine distance `<=>`**: Standard for normalized text embeddings (OpenAI, Cohere, Voyage)

## Setup Phases

**1. Enable extension**
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

**2. Create table**
```sql
CREATE TABLE documents (
  id         BIGSERIAL PRIMARY KEY,
  content    TEXT NOT NULL,
  metadata   JSONB DEFAULT '{}',
  embedding  VECTOR(1536),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
```

**3. HNSW index** (recommended: < 1M rows)
```sql
CREATE INDEX ON documents
  USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);
-- High recall variant: m=32, ef_construction=128
```

**4. match_documents RPC**
```sql
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding VECTOR(1536),
  match_count     INT     DEFAULT 5,
  match_threshold FLOAT   DEFAULT 0.7
) RETURNS TABLE (id BIGINT, content TEXT, metadata JSONB, similarity FLOAT)
LANGUAGE SQL STABLE AS $$
  SELECT id, content, metadata,
         1 - (embedding <=> query_embedding) AS similarity
  FROM   documents
  WHERE  1 - (embedding <=> query_embedding) > match_threshold
  ORDER  BY embedding <=> query_embedding
  LIMIT  match_count;
$$;
GRANT EXECUTE ON FUNCTION match_documents TO anon, authenticated;
```

**5. RLS policy**
```sql
-- Public read
CREATE POLICY "public_read" ON documents FOR SELECT USING (true);
-- Multi-tenant
CREATE POLICY "tenant_read" ON documents FOR SELECT
  USING ((metadata->>'user_id')::text = auth.uid()::text);
```

## Index Comparison

| Index | Rows sweet spot | Build cost | p95 latency | Recall |
|-------|----------------|-----------|-------------|--------|
| None (exact) | < 10k | Zero | 1–5ms | 100% |
| HNSW | 10k – 1M | Medium | 5–20ms | 98%+ |
| IVFFlat | 500k – 5M | Low+ANALYZE | 10–30ms | 95%+ |

IVFFlat `lists` rule: `sqrt(row_count)` for balanced; e.g., 1M rows → `lists=1000`

## Distance Operators

| Operator | Metric | Best for |
|----------|--------|----------|
| `<=>` | Cosine | Normalized text embeddings (OpenAI, Cohere) |
| `<->` | L2 Euclidean | Image, vision, unnormalized embeddings |
| `<#>` | Inner product | Pre-normalized vectors (fastest) |

## Python Integration
```python
from supabase import create_client
import openai

sb = create_client(SUPABASE_URL, SUPABASE_KEY)
oa = openai.OpenAI()

def embed(text: str) -> list[float]:
    return oa.embeddings.create(
        input=text, model="text-embedding-3-small"
    ).data[0].embedding

def upsert(content: str, metadata: dict = {}):
    sb.table("documents").insert(
        {"content": content, "metadata": metadata, "embedding": embed(content)}
    ).execute()

def search(query: str, k: int = 5, threshold: float = 0.7):
    return sb.rpc("match_documents", {
        "query_embedding": embed(query),
        "match_count": k,
        "match_threshold": threshold
    }).execute().data
```

## Golden Rules
- SET `hnsw.ef_search = 100` at query time for high-recall use cases
- VACUUM ANALYZE documents after bulk inserts (IVFFlat rebuilds centroids)
- MONITOR index health: `SELECT * FROM pg_stat_user_indexes WHERE relname = 'documents'`
- CHUNK content to 512–1024 tokens before embedding; store chunk_index in metadata
- NEVER store raw full documents — split, embed, and link to parent via metadata

## References
- Supabase AI docs: https://supabase.com/docs/guides/ai/vector-columns
- pgvector GitHub: https://github.com/pgvector/pgvector
- OpenAI embeddings: https://platform.openai.com/docs/guides/embeddings
- Related: p01_kc_supabase_vectors (base SQL patterns), p01_kc_rag_fundamentals (retrieval patterns)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_embedding_config_supabase]] | related | 0.63 |
| [[p01_kc_supabase_vectors]] | sibling | 0.62 |
| [[p01_rag_source_supabase]] | related | 0.47 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.35 |
| [[bld_collaboration_embedding_config]] | downstream | 0.33 |
| [[p01_gl_embedding]] | related | 0.33 |
| [[p06_schema_database]] | downstream | 0.32 |
| [[p03_sp_vector_store_builder]] | downstream | 0.29 |
| [[p01_kc_embedding_config]] | sibling | 0.28 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.28 |
