---
id: p01_rag_source_supabase
kind: rag_source
pillar: P01
title: "RAG Source — Supabase pgvector as Embedding Backend"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [rag-source, supabase, pgvector, embeddings, semantic-search, N04]
tldr: "pgvector in Supabase replaces external vector DBs — same PostgreSQL, RLS-scoped, HNSW indexed, multi-tenant RAG ready"
density_score: 0.89
---

# RAG Source: Supabase pgvector

## Why pgvector Over External Vector DBs
| Aspect | pgvector (Supabase) | Pinecone | Weaviate |
|--------|-------------------|----------|----------|
| Extra infra | None (same PG) | Separate service | Separate service |
| Cost | Included in Supabase | USD 70+/mo | USD 25+/mo |
| RLS/multi-tenant | Native (same RLS) | Application-level | Namespace-based |
| SQL joins | Direct (same DB) | Impossible | Impossible |
| Hybrid search | BM25 + vector in 1 query | Vector only | Vector + BM25 separate |

## Limitations & Anti-Patterns
| Limitation | Threshold | Alternative |
|------------|-----------|-------------|
| Vector count | >1M vectors | Pinecone/Weaviate |
| Query latency | >200ms p95 | Dedicated vector DB |
| Memory usage | >50% of PG RAM | External vector store |
| Complex filters | >5 metadata filters | Application-level filtering |

**Anti-patterns:**
- Storing high-dimensional vectors (>2048D) — kills performance
- No connection pooling — exhausts PG connections
- Embedding updates without VACUUM — index bloat

## Connection Config
```yaml
rag_backend: supabase_pgvector
connection:
  host: "db.[PROJECT_REF].supabase.co"
  port: 5432
  database: postgres
  pooler: "aws-0-[REGION].pooler.supabase.com:6543"
embedding:
  model: text-embedding-3-small
  dimensions: 1536
  distance: cosine
index:
  type: hnsw
  params: {m: 16, ef_construction: 64}
tables:
  - name: documents
    content_column: content
    embedding_column: embedding
    metadata_column: metadata
    rls: org_member
search:
  function: match_documents
  threshold: 0.78
  max_results: 10
```

## Ingestion Pipeline
```text
[Source Document] → chunk (500 tokens, 50 overlap)
    → embed (text-embedding-3-small)
    → INSERT INTO documents (content, metadata, embedding)
    → HNSW index auto-updates
```

## Retrieval Pipeline
```text
[User Query] → embed query
    → SELECT * FROM match_documents(query_embedding, 0.78, 10)
    → RLS filters by org_id automatically
    → Return top-k chunks with similarity scores
    → Inject into LLM context
```

## Multi-Tenant RAG
```sql
-- Embeddings are org-scoped via RLS
CREATE POLICY "org_rag" ON documents
  FOR SELECT USING (
    (metadata->>'org_id') = (auth.jwt()->'app_metadata'->>'org_id')
  );
-- Company A's RAG never sees Company B's documents
```

## Monitoring
| Metric | Query | Target |
|--------|-------|--------|
| Index size | `SELECT pg_relation_size('documents_embedding_idx')` | <1GB |
| Query latency | `EXPLAIN ANALYZE SELECT * FROM match_documents(...)` | <100ms |
| Recall | Test with known-answer queries | >95% |
| Table size | `SELECT pg_total_relation_size('documents')` | Within tier |