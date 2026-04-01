---
id: "p04_conn_{{SERVICE_SLUG}}"
kind: db_connector
pillar: P04
version: 1.0.0
title: Template - Db Connector
tags: [template, database, connector, sql, pool]
tldr: "Database connection config: URL, pool size, timeouts, query patterns. Supports PostgreSQL, SQLite, Supabase."
quality: 8.6
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
- **Connection failed**: Retry 3x with backoff
- **Query timeout**: Log slow query + error
- **Pool exhausted**: Queue + warn at 80%
## Quality Gate
- [ ] URL from environment (never hardcoded)
- [ ] Pool size per environment
- [ ] SSL in production
- [ ] Slow query logging
