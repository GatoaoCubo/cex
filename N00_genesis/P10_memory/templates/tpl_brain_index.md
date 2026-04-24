---
# TEMPLATE: Brain Index (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.knowledge_index)
# Max 3072 bytes

id: p10_bi_{{INDEX_SLUG}}
kind: knowledge_index
8f: F3_inject
pillar: P10
title: "Brain Index: {{INDEX_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Brain Index: {{INDEX_NAME}}

## Semantic Index
```yaml
engine: {{bm25|faiss|hybrid}}
namespace: {{NAMESPACE}}
refresh: {{REFRESH_POLICY}}
```

## Structured Store (SQLite)
```yaml
engine: sqlite
tables:
  sessions:
    columns: [id, content_session_id, memory_session_id, started_at, ended_at, summary]
    index: [content_session_id, started_at]
  observations:
    columns: [id, session_id, content, source_hook, created_at]
    index: [session_id, created_at]
    fk: sessions.id
  summaries:
    columns: [id, session_id, summary_text, token_count, created_at]
    index: [session_id]
    fk: sessions.id
fts: FTS5 on observations.content + summaries.summary_text
```

## 3-Layer Progressive Disclosure
<!-- MCP exposes 3 layers to minimize token usage -->

| Layer | Tool | Returns | Token Cost |
|-------|------|---------|------------|
| 1. Search | `search_memory` | Entity names + brief matches | 50-100 tokens |
| 2. Timeline | `get_timeline` | Session list with timestamps + summaries | 200-500 tokens |
| 3. Detail | `get_observations` | Full observation text for a session | 500-1000 tokens |

<!-- Pattern: always start at Layer 1, drill down only when needed = 10x token savings -->

## Retrieval Policy
- Query shape: {{EXPECTED_QUERY_PATTERN}}
- Ranking signal: {{PRIMARY_RANKING_SIGNAL}}
- Reindex when: {{REINDEX_TRIGGER}}
