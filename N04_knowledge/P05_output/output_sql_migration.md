---
id: p10_out_sql_migration
kind: output
pillar: P10
title: "Output: SQL Migration"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [output, n04, sql, migration, supabase, database]
tldr: "Supabase migration SQL: CREATE tables + INSERT KCs + CREATE indexes."
density_score: 0.92
related:
  - p06_schema_database
  - output_kc_quality_audit_20260408
  - p10_out_taxonomy_map
  - p06_schema_export_format
  - p03_sp_knowledge_nucleus
  - p01_kc_knowledge_card
  - n04_agent_knowledge
  - bld_output_template_kind
  - p10_out_knowledge_graph
  - self_review_2026-04-02
---

# Output: SQL Migration

## Template
```sql
-- Migration: {{NAME}}
-- Generated: {{DATE}}
-- KCs: {{COUNT}}

-- 1. Create tables (if not exist)
CREATE TABLE IF NOT EXISTS kcs (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  pillar TEXT NOT NULL,
  domain TEXT,
  title TEXT NOT NULL,
  tldr TEXT,
  body TEXT NOT NULL,
  tags TEXT[],
  density_score FLOAT,
  quality FLOAT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Insert KCs
INSERT INTO kcs (id, kind, pillar, domain, title, tldr, body, tags, density_score, quality)
VALUES
  ('{{ID}}', '{{KIND}}', '{{PILLAR}}', '{{DOMAIN}}', '{{TITLE}}', '{{TLDR}}', '{{BODY}}', ARRAY[{{TAGS}}], {{DENSITY}}, {{QUALITY}})
ON CONFLICT (id) DO UPDATE SET
  body = EXCLUDED.body,
  updated_at = now();

-- 3. Create indexes
CREATE INDEX IF NOT EXISTS idx_kcs_kind ON kcs(kind);
CREATE INDEX IF NOT EXISTS idx_kcs_pillar ON kcs(pillar);
CREATE INDEX IF NOT EXISTS idx_kcs_domain ON kcs(domain);
```

## Usage

| Variable | Source | Example |
|----------|--------|---------|
| `{{NAME}}` | Migration purpose | `"kc_batch_2026_04_01"` |
| `{{DATE}}` | Current timestamp | `"2026-04-01T14:30:00Z"` |
| `{{COUNT}}` | Number of KCs | `"15"` |
| `{{ID}}` | KC filename | `"kc_react_patterns"` |
| `{{KIND}}` | KC frontmatter | `"knowledge_card"` |
| `{{PILLAR}}` | KC directory | `"P01"` |
| `{{BODY}}` | Escaped KC content | `'## Pattern\nHook pattern...'` |
| `{{TAGS}}` | Comma-separated | `'react','patterns','hooks'` |

**Generate from compiled KCs:**
```bash
python _tools/cex_compile.py --all
python _tools/sql_export.py > migration.sql
```

### Example Output
```sql
-- Migration: kc_batch_2026_04_01
-- Generated: 2026-04-01T14:30:00Z
-- KCs: 2

INSERT INTO kcs (id, kind, pillar, domain, title, tldr, body, tags, density_score, quality)
VALUES
  ('kc_react_patterns', 'knowledge_card', 'P01', 'frontend', 'React Patterns', 'Common React patterns for components', '## Hook Pattern\nUseState for local state...', ARRAY['react','patterns','hooks'], 0.89, 8.5),
  ('kc_sql_indexing', 'knowledge_card', 'P04', 'database', 'SQL Indexing', 'Database index optimization strategies', '## Index Types\nB-tree for equality...', ARRAY['sql','indexing','performance'], 0.91, 8.7)
ON CONFLICT (id) DO UPDATE SET
  body = EXCLUDED.body,
  updated_at = now();
```

## Validation

| Check | SQL Query | Expected |
|-------|-----------|----------|
| Table exists | `SELECT to_regclass('kcs');` | `'kcs'` |
| Row count | `SELECT COUNT(*) FROM kcs;` | `{{COUNT}}` |
| Index coverage | `SELECT indexname FROM pg_indexes WHERE tablename='kcs';` | 4 indexes |
| Recent data | `SELECT MAX(updated_at) FROM kcs;` | Today's timestamp |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_database]] | upstream | 0.47 |
| [[output_kc_quality_audit_20260408]] | upstream | 0.36 |
| [[p10_out_taxonomy_map]] | sibling | 0.28 |
| [[p06_schema_export_format]] | upstream | 0.25 |
| [[p03_sp_knowledge_nucleus]] | upstream | 0.24 |
| [[p01_kc_knowledge_card]] | upstream | 0.21 |
| [[n04_agent_knowledge]] | upstream | 0.21 |
| [[bld_output_template_kind]] | upstream | 0.20 |
| [[p10_out_knowledge_graph]] | sibling | 0.19 |
| [[self_review_2026-04-02]] | upstream | 0.19 |
