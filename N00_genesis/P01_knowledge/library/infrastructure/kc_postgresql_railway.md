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
quality: 9.0
tags: [postgresql, railway, database, deploy, connection-pooling]
tldr: "Railway PostgreSQL: add plugin, get DATABASE_URL auto-injected. Use connection pooling (PgBouncer) for serverless. Backup via pg_dump cron."
when_to_use: "When deploying PostgreSQL on Railway platform"
keywords: [postgresql, railway, pgbouncer, database-url, backup]
density_score: 0.92
updated: "2026-04-07"
related:
  - KC_N05_POSTGRESQL_RAILWAY
  - p08_ac_railway_superintendent
  - p01_kc_railway_platform_deep
  - p02_agent_railway_superintendent
  - p12_dr_railway_superintendent
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p01_kc_deploy_paas
  - p03_sp_railway_superintendent
  - KC_N05_RAILWAY_CLI_PATTERNS
  - p05_output_deploy_checklist
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

## Key Principles

1. Domain-specific knowledge must be verifiable and traceable
2. Artifacts reference this card via `tags` matching
3. Updates trigger re-scoring of dependent artifacts
4. Card freshness tracked via `created`/`updated` timestamps
5. Cross-references validated by `cex_compile.py`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[KC_N05_POSTGRESQL_RAILWAY]] | sibling | 0.37 |
| [[p08_ac_railway_superintendent]] | downstream | 0.27 |
| [[p01_kc_railway_platform_deep]] | sibling | 0.27 |
| [[p02_agent_railway_superintendent]] | downstream | 0.25 |
| [[p12_dr_railway_superintendent]] | downstream | 0.24 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | sibling | 0.22 |
| [[p01_kc_deploy_paas]] | sibling | 0.22 |
| [[p03_sp_railway_superintendent]] | downstream | 0.22 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | sibling | 0.22 |
| [[p05_output_deploy_checklist]] | downstream | 0.20 |
