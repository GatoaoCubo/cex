---
id: KC_N05_POSTGRESQL_RAILWAY
kind: knowledge_card
pillar: P01
title: PostgreSQL & Redis on Railway — Setup, Connection, Performance
domain: N05_operations
tags: [postgresql, redis, database, railway, plugin, connection]
quality: 9.0
sources:
  - https://docs.railway.com/guides/postgresql
  - https://docs.railway.com/guides/redis
created: 2026-04-01
---

# PostgreSQL & Redis on Railway

## 1. PostgreSQL — Setup

### Add Plugin
```bash
# Via CLI
railway add --database postgres

# Via web UI
Ctrl/Cmd + K → "PostgreSQL" → Add
```

Railway provisions a PostgreSQL service with SSL enabled. Uses official Docker Hub image.

### Available Environment Variables

```bash
PGHOST        # hostname
PGPORT        # port (usually 5432)
PGUSER        # username
PGPASSWORD    # password
PGDATABASE    # database name
DATABASE_URL  # full connection string (most libraries auto-detect this)
```

### DATABASE_URL Format
```
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=require
```

Most Python/Node/Go libraries auto-detect `DATABASE_URL` — no extra config needed.

## 2. Connecting from Services

### Internal (Preferred — No Egress Cost)

```python
# Python / psycopg2 / asyncpg
import os
DATABASE_URL = os.environ["DATABASE_URL"]

# asyncpg note: Railway internal may need ssl=False for .railway.internal hosts
import asyncpg
conn = await asyncpg.connect(DATABASE_URL, ssl=False)  # for internal networking
```

```javascript
// Node.js / pg
const { Pool } = require('pg')
const pool = new Pool({ connectionString: process.env.DATABASE_URL })
```

```python
# SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine(os.environ["DATABASE_URL"])
```

### External (TCP Proxy — Incurs Egress Cost)

TCP Proxy is enabled by default on database plugins for external access (e.g., local development, DBeaver, TablePlus).

```bash
# Connect from local machine
psql $DATABASE_URL

# Or via Railway CLI
railway connect postgres
```

**Cost note:** External TCP connections bill for Network Egress. Use `.railway.internal` for service-to-service to avoid charges.

## 3. Extensions

Default template does NOT include extensions. Available as separate templates:

| Extension | Use Case | Template |
|-----------|----------|---------|
| `pgvector` | Vector embeddings, semantic search | pgvector template |
| `PostGIS` | Geographic/spatial data | PostGIS template |
| `TimescaleDB` | Time-series data | TimescaleDB template |

### Adding Extensions Manually

After connecting:
```sql
-- Check available extensions
SELECT * FROM pg_available_extensions ORDER BY name;

-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Enable UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable pg_trgm (fuzzy search)
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

## 4. Performance Configuration

Modify PostgreSQL settings via `ALTER SYSTEM` and restart:

```sql
-- Connect via railway connect or DATABASE_URL
ALTER SYSTEM SET shared_buffers = '256MB';
ALTER SYSTEM SET effective_cache_size = '1GB';
ALTER SYSTEM SET work_mem = '16MB';
ALTER SYSTEM SET maintenance_work_mem = '128MB';
ALTER SYSTEM SET max_connections = '100';
ALTER SYSTEM SET wal_level = 'replica';
ALTER SYSTEM SET max_wal_senders = '3';
```

Then restart the PostgreSQL service from Railway dashboard (not `railway restart` — use web UI for DB plugins).

### pg_stat Monitoring

```sql
-- Active queries
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';

-- Table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- Index usage
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- Cache hit rate (should be > 99%)
SELECT sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) AS ratio
FROM pg_statio_user_tables;
```

## 5. Connection Pooling

Railway's managed PostgreSQL does not include PgBouncer by default. Options:

### Option A: SQLAlchemy Pool (App-Level)
```python
from sqlalchemy import create_engine
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,       # check connection health
    pool_recycle=3600,        # recycle connections after 1h
)
```

### Option B: asyncpg Pool
```python
import asyncpg

pool = await asyncpg.create_pool(
    DATABASE_URL,
    min_size=5,
    max_size=20,
    ssl=False  # for .railway.internal connections
)
```

### Option C: PgBouncer as Separate Service
Add PgBouncer as a separate Railway service, point it at `postgres.railway.internal:5432`, then point app at PgBouncer internally.

## 6. Migrations

Best practice: run migrations as `preDeployCommand` in railway.toml:

```toml
# railway.toml
[deploy]
preDeployCommand = ["python -m alembic upgrade head"]
# or
preDeployCommand = ["python manage.py migrate"]
# or
preDeployCommand = ["node_modules/.bin/prisma migrate deploy"]
```

This ensures migrations run before new app version starts, preventing schema mismatches.

**Alembic pattern:**
```bash
# Local: generate migration
alembic revision --autogenerate -m "add users table"

# Railway: auto-runs on deploy via preDeployCommand
# alembic upgrade head
```

## 7. Backup & Recovery

```bash
# Manual backup via pg_dump
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql

# Restore
psql $DATABASE_URL < backup_20260401.sql
```

Railway provides **native Backups feature** (configurable in service settings) for automated point-in-time snapshots.

## 8. Monitoring

Recommended stack:
- **PostgreSQL Exporter** → Prometheus → Grafana
- Deploy as additional Railway service pointing at `postgres.railway.internal`

```yaml
# Example docker-compose / Railway template
postgres-exporter:
  image: prometheuscommunity/postgres-exporter
  environment:
    DATA_SOURCE_NAME: $DATABASE_URL
```

---

## 9. Redis — Setup

### Add Plugin
```bash
railway add --database redis
```

### Available Environment Variables

```bash
REDISHOST     # hostname
REDISUSER     # username (usually "default")
REDISPORT     # port (usually 6379)
REDISPASSWORD # password
REDIS_URL     # full connection string
```

### REDIS_URL Format
```
redis://:PASSWORD@HOST:PORT
```

## 10. Connecting to Redis

### Internal (Preferred)
```python
import redis
import os

r = redis.from_url(os.environ["REDIS_URL"])
# or with internal DNS:
r = redis.Redis(host="redis.railway.internal", port=6379, password=os.environ["REDISPASSWORD"])
```

```javascript
// Node.js / ioredis
const Redis = require('ioredis')
const redis = new Redis(process.env.REDIS_URL)
```

### External (TCP Proxy)
```bash
redis-cli -u $REDIS_URL
# or
railway connect redis
```

## 11. Redis Operational Notes

- Templates are **unmanaged** — full control over configuration
- For persistence, eviction policies, replication: refer to official Redis docs
- Railway provides native **Backups feature** for Redis data snapshots
- Monitoring: deploy `redis_exporter` as Railway service → Prometheus

### Common Redis Config Patterns
```bash
# Set via railway variables (passed to Redis on startup)
# Or ALTER via redis-cli CONFIG SET

CONFIG SET maxmemory 256mb
CONFIG SET maxmemory-policy allkeys-lru  # LRU eviction when full
CONFIG SET appendonly yes                 # AOF persistence
CONFIG SET save "900 1 300 10 60 10000"  # RDB snapshots
```

## 12. Multi-Service Architecture Pattern

```
┌──────────────────────────────────────────────┐
│              Railway Project                  │
│                                              │
│  ┌─────────┐    .railway.internal    ┌──────┐│
│  │   API   │◄──────────────────────►│  PG  ││
│  │ service │◄──────────────────────►│      ││
│  └─────────┘                        └──────┘│
│       │         .railway.internal    ┌──────┐│
│       └────────────────────────────►│Redis ││
│                                     └──────┘│
│                                              │
│  External TCP Proxy (egress cost):           │
│  PG: *.proxy.rlwy.net:PORT                  │
│  Redis: *.proxy.rlwy.net:PORT               │
└──────────────────────────────────────────────┘
```

## Anti-Patterns

- Do NOT use external TCP connection from within Railway services (use `.railway.internal` — free)
- Do NOT forget `sslmode=require` when connecting externally (Railway PG requires SSL)
- Do NOT skip `preDeployCommand` for migrations — race condition on startup
- Do NOT use asyncpg with ssl=True on `.railway.internal` connections (causes SSL handshake errors)
- Do NOT modify `max_connections` above plan limits (causes OOM)
- Do NOT store large blobs in Redis without `maxmemory` + eviction policy (OOM eviction)
