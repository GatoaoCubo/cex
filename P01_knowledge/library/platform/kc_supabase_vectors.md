---
id: p01_kc_supabase_vectors
kind: knowledge_card
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
tldr: "pgvector nativo no PostgreSQL: vector(1536), indexes HNSW/IVFFlat, match_documents() para semantic search, integra com OpenAI/Cohere/local embeddings"
when_to_use: "Quando configurar embeddings, semantic search, ou RAG pipeline com Supabase"
keywords: [pgvector, embeddings, semantic-search, rag, supabase-vectors]
long_tails:
  - Como criar tabela com coluna vector no Supabase
  - HNSW vs IVFFlat para index de embeddings no pgvector
  - Function match_documents para semantic search no Supabase
axioms:
  - SEMPRE crie index HNSW para tabelas com >1000 vetores
  - NUNCA armazene embeddings sem metadata (content, source, created_at)
  - SEMPRE use RLS em tabelas de embeddings para multi-tenant isolation
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_auth]
density_score: 0.91
data_source: "https://supabase.com/docs/guides/ai"
---

# Supabase Vectors — pgvector + RAG

## Quick Reference
```yaml
topic: supabase_vectors
scope: pgvector, embeddings, HNSW, IVFFlat, semantic search, RAG
owner: n04_knowledge
criticality: high
extension: pgvector (habilitar: create extension vector)
conexao_n04: backend concreto para RAG/embeddings do N04
```

## Setup Inicial
```sql
-- 1. Habilitar pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Criar tabela com coluna embedding
CREATE TABLE documents (
  id BIGSERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),  -- OpenAI ada-002 / text-embedding-3-small
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. RLS obrigatório
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "owner_read" ON documents
  FOR SELECT USING (metadata->>'org_id' = (auth.jwt()->'app_metadata'->>'org_id'));

-- 4. Index HNSW (recomendado para >1000 rows)
CREATE INDEX ON documents
  USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);
```

## Modelos de Embedding
| Modelo | Dim | Custo/1M tok |
|--------|-----|-------------|
| text-embedding-3-small (OpenAI) | 1536 | USD 0.02 |
| text-embedding-3-large (OpenAI) | 3072 | USD 0.13 |
| nomic-embed-text (local) | 768 | Grátis |
| Cohere embed-v3 | 1024 | USD 0.10 |

## Index Types
| Index | Quando Usar | Build Time | Query Speed | Recall |
|-------|-------------|------------|-------------|--------|
| Nenhum | <1000 rows | 0 | Lento (exact) | 100% |
| IVFFlat | 1K-100K rows, build rápido | Rápido | Médio | ~95% |
| HNSW | >1K rows, queries frequentes | Lento | Rápido | ~98% |

```sql
-- IVFFlat (mais rápido para construir)
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- HNSW (mais rápido para queries)
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);
```

## Distance Functions
| Operador | Function | Quando Usar |
|----------|----------|-------------|
| `<=>` | vector_cosine_ops | Default: normalized embeddings (OpenAI, Cohere) |
| `<#>` | vector_ip_ops | Inner product (MRL, matryoshka) |
| `<->` | vector_l2_ops | L2/Euclidean (imagens, spatial) |

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
-- Combinar full-text com vector: pesos 0.3 BM25 + 0.7 vector
SELECT id, content,
  (0.3 * ts_rank(fts, q) + 0.7 * (1 - (embedding <=> vec))) AS score
FROM documents, plainto_tsquery('portuguese','termo') q
WHERE fts @@ q ORDER BY score DESC LIMIT 10;
```

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Sem index em >1K rows | Query scan sequencial, timeout | HNSW ou IVFFlat |
| Dimensões erradas | Insert falha silenciosamente | Match model dimensions exato |
| Sem metadata | Impossível filtrar por fonte/data | JSONB metadata obrigatório |
| Embedding sem RLS | Tenant A vê dados do tenant B | RLS por org_id/user_id |

## Golden Rules
- MATCH dimensões da coluna VECTOR(N) com o modelo exato
- INDEXE com HNSW para qualquer tabela de produção
- COMBINE vector search com BM25 para hybrid retrieval
- GUARDE source/chunk_index no metadata para rastreabilidade

## References
- Docs: https://supabase.com/docs/guides/ai
- pgvector: https://github.com/pgvector/pgvector
- Embeddings: https://supabase.com/docs/guides/ai/vector-columns
