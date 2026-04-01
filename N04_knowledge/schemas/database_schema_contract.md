---
id: p06_schema_database
kind: schema
pillar: P06
title: "Database Schema Contract — Supabase"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: null
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
