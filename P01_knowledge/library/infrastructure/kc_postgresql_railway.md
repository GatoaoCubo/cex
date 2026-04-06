---
id: p01_kc_postgresql_railway
kind: knowledge_card
type: infrastructure
pillar: P01
title: "PostgreSQL on Railway"
version: 1.0.0
created: 2026-03-30
author: n05_operations
domain: infrastructure
quality: 8.9
tags: [postgresql, railway, database, deploy, connection-pooling]
tldr: "Railway PostgreSQL: add plugin, get DATABASE_URL auto-injected. Use connection pooling (PgBouncer) for serverless. Backup via pg_dump cron."
when_to_use: "When deploying PostgreSQL on Railway platform"
keywords: [postgresql, railway, pgbouncer, database-url, backup]
density_score: 0.92
---

# PostgreSQL on Railway

## Setup

| Step | Command/Action | Result |
|------|---------------|--------|
| 1 | Add PostgreSQL plugin in Railway dashboard | DATABASE_URL auto-injected |
| 2 | Enable connection pooling | PgBouncer proxy on port 6543 |
| 3 | Set `PGBOUNCER_URL` as primary | Handles serverless connection spikes |

## Connection String Format
```
postgresql://user:pass@host:port/dbname?sslmode=require
```

## Key Config

| Variable | Purpose | Default |
|----------|---------|---------|
| `DATABASE_URL` | Direct connection | Auto-set by Railway |
| `DATABASE_POOL_URL` | Pooled connection (PgBouncer) | Port 6543 |
| `PGDATA` | Data directory | `/var/lib/postgresql/data` |

## Backup Strategy
```bash
# Cron: daily pg_dump to S3/R2
pg_dump $DATABASE_URL | gzip > backup_$(date +%Y%m%d).sql.gz
```

## Anti-Pattern
Direct connections without pooling in serverless = connection exhaustion. Always use PgBouncer URL for application code.
