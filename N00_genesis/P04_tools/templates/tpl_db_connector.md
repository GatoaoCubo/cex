---
id: "p04_conn_{{SERVICE_SLUG}}"
kind: db_connector
8f: F5_call
pillar: P04
version: 1.0.0
title: Template - Db Connector
tags: [template, database, connector, sql, pool]
tldr: "Database connection config: URL, pool size, timeouts, query patterns. Supports PostgreSQL, SQLite, Supabase."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - p01_kc_db_connector
  - p04_db_postgres
  - p04_webhook_NAME
  - p11_qg_shokunin_pool
  - p04_search_tool_NAME
  - p06_schema_startup_sequence
  - bld_examples_runtime_state
  - p10_ax_shokunin_quality
  - p03_ap_{{ACTION_SLUG}}
  - bld_examples_input_schema
---

# Db Connector: [NAME]

## Purpose
[WHAT this db_connector does]
## Configuration
```yaml
driver: [asyncpg | psycopg2 | aiosqlite | supabase]
url: "${DATABASE_URL}"
pool_size: [5 | 10 | 20]
timeout_s: [30]

ssl: [require | prefer | disable]
```
## Pool Settings
| Env | pool_size | overflow | timeout |
|-----|-----------|----------|---------|
| Dev | 2 | 5 | 60s |
| Staging | 5 | 10 | 30s |
| Production | 20 | 30 | 10s |
## Query Patterns
```python
async with db.acquire() as conn:
    result = await conn.fetch("SELECT * FROM t WHERE id = $1", id)
async with db.transaction() as tx:
    await tx.execute("INSERT ...", ...)
```
## Error Handling
1. **Connection failed**: Retry 3x with backoff
2. **Query timeout**: Log slow query + error
3. **Pool exhausted**: Queue + warn at 80%
## Quality Gate
1. [ ] URL from environment (never hardcoded)
2. [ ] Pool size per environment
3. [ ] SSL in production
4. [ ] Slow query logging

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `db_connector` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_db_connector]] | upstream | 0.26 |
| [[p04_db_postgres]] | sibling | 0.21 |
| [[p04_webhook_NAME]] | related | 0.21 |
| [[p11_qg_shokunin_pool]] | downstream | 0.18 |
| [[p04_search_tool_NAME]] | related | 0.17 |
| [[p06_schema_startup_sequence]] | downstream | 0.17 |
| [[bld_examples_runtime_state]] | downstream | 0.17 |
| [[p10_ax_shokunin_quality]] | downstream | 0.16 |
| [[p03_ap_{{ACTION_SLUG}}]] | upstream | 0.16 |
| [[bld_examples_input_schema]] | downstream | 0.16 |
