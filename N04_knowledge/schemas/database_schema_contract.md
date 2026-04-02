---
id: p06_schema_database
kind: schema
pillar: P06
title: "Database Schema Contract — Supabase"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [schema, n04, database, supabase, sql, tables, embedding]
tldr: "Supabase table schemas: kcs (metadata), embeddings (vectors), search_index (FTS), audit_log (changes)."
density_score: 0.93
---

# Database Schema — Supabase

## Tables

### kcs
```sql
CREATE TABLE kcs (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  pillar TEXT NOT NULL,
  domain TEXT,
  title TEXT NOT NULL,
  tldr TEXT,
  body TEXT NOT NULL,
  tags TEXT[],
  keywords TEXT[],
  density_score FLOAT,
  quality FLOAT,
  version TEXT DEFAULT '1.0.0',
  author TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### embeddings
```sql
CREATE TABLE embeddings (
  id SERIAL PRIMARY KEY,
  kc_id TEXT REFERENCES kcs(id),
  chunk_index INT,
  chunk_text TEXT,
  embedding vector(1536),
  model TEXT DEFAULT 'text-embedding-3-small',
  created_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_embeddings_vec ON embeddings USING ivfflat (embedding vector_cosine_ops);
```

### search_index (Full-Text Search)
```sql
CREATE INDEX idx_kcs_fts ON kcs USING gin(to_tsvector('english', title || ' ' || body));
```

### audit_log
```sql
CREATE TABLE kc_audit_log (
  id SERIAL PRIMARY KEY,
  kc_id TEXT,
  action TEXT, -- create, update, archive, delete
  diff JSONB,
  actor TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

## Constraints & Validation

| Table | Field | Constraint | Reason |
|-------|-------|-----------|--------|
| `kcs` | `id` | `LIKE 'kc_%'` | Enforce KC naming convention |
| `kcs` | `pillar` | `CHECK (pillar ~ '^P[0-9]{2}$')` | Validate P01-P12 format |
| `kcs` | `density_score` | `CHECK (density_score >= 0 AND density_score <= 1)` | Score must be 0-1 range |
| `kcs` | `quality` | `CHECK (quality >= 0 AND quality <= 10)` | Quality must be 0-10 range |
| `kcs` | `body` | `CHECK (length(body) >= 100)` | Minimum content requirement |
| `embeddings` | `chunk_index` | `CHECK (chunk_index >= 0)` | No negative chunk indices |
| `embeddings` | `chunk_text` | `CHECK (length(chunk_text) <= 8000)` | Max token limit for embedding |
| `audit_log` | `action` | `CHECK (action IN ('create', 'update', 'archive', 'delete'))` | Valid action types only |

## Table Relationships

| Query Pattern | Tables | SQL Example |
|---------------|--------|-------------|
| Semantic search | `kcs` + `embeddings` | `SELECT k.* FROM kcs k JOIN embeddings e ON k.id = e.kc_id ORDER BY e.embedding <=> $vector LIMIT 10` |
| Full-text search | `kcs` | `SELECT * FROM kcs WHERE to_tsvector('english', title || ' ' || body) @@ plainto_tsquery('search term')` |
| Change tracking | `kcs` + `audit_log` | `SELECT a.* FROM kc_audit_log a WHERE a.kc_id = $kc_id ORDER BY created_at DESC` |
| Chunk retrieval | `embeddings` | `SELECT chunk_text, chunk_index FROM embeddings WHERE kc_id = $kc_id ORDER BY chunk_index` |