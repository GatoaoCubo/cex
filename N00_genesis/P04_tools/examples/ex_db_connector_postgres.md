---
id: p04_db_postgres
kind: db_connector
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "PostgreSQL Connector"
service: "PostgreSQL"
protocol: rest
auth: api_key
endpoints:
  - query
  - execute
quality: 9.0
tags: [db_connector, postgres, sql, data]
tldr: "PostgreSQL connector for structured data queries via asyncpg with connection pooling"
description: "Read/write access to PostgreSQL databases for agent data retrieval and storage"
health_check: "SELECT 1"
mapping: "SQL result rows mapped to list of dicts"
transform: "datetime to ISO 8601, Decimal to float"
retry: "3 retries with exponential backoff"
rate_limit: "100 queries/minute"
logging: structured
versioning: "Schema migrations via Alembic"
domain: "tool integration"
title: "Db Connector Postgres"
density_score: 0.91
---

# PostgreSQL Connector

## Overview
Provides agents with structured data access to PostgreSQL databases via asyncpg. Used for reading business data, writing agent outputs, and querying metadata stores.

## Endpoints
### query (inbound)
SELECT queries — returns result rows as list of dicts.
Data shape:
- `sql` (string): Parameterized SQL query
- `params` (array): Bind parameters

### execute (outbound)
INSERT/UPDATE/DELETE — returns affected row count.
Data shape:
- `sql` (string): Parameterized DML statement
- `params` (array): Bind parameters

## Health & Errors
Health: `SELECT 1` on connection pool checkout
- ConnectionError: retry with backoff, max 3 attempts
- QueryTimeout: log and return error after 30s
Circuit breaker: open after 5 consecutive failures, half-open after 60s

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `db connector`
- **Artifact ID**: `p04_db_postgres`
- **Tags**: [db_connector, postgres, sql, data]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `db connector` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `db connector`
- **Artifact ID**: `p04_db_postgres`
- **Tags**: [db_connector, postgres, sql, data]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `db connector` | Artifact type |
| Pipeline | 8F (F1→F8) |
