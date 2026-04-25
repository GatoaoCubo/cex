---
id: p01_kc_supabase_database
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Database — PostgreSQL 15+ with 50+ Extensions"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [supabase, postgresql, database, extensions, migrations, platform]
tldr: "Managed PostgreSQL 15+ with 50+ extensions (pgvector, pg_cron, pg_net, pgjwt), versioned migrations, and auto-generated REST/GraphQL"
when_to_use: "When configuring Supabase database for any company"
keywords: [supabase-database, postgresql, extensions, migrations]
long_tails:
  - How to enable extensions in Supabase PostgreSQL
  - Connection and storage limits per Supabase tier
  - Versioned migrations with Supabase CLI
axioms:
  - ALWAYS enable pgvector if the project uses embeddings or RAG
  - NEVER expose the connection string directly to client-side
  - ALWAYS use versioned migrations, never manual ALTER TABLE in production
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_auth, p01_kc_supabase_vectors]
density_score: 0.88
data_source: "https://supabase.com/docs/guides/database"
related:
  - p01_kc_supabase_cli
  - bld_tools_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - p01_rag_source_supabase
  - p12_wf_supabase_setup
  - p12_dispatch_rule_supabase
  - bld_config_supabase_data_layer
---

# Supabase Database — PostgreSQL 15+

## Quick Reference
```yaml
topic: supabase_database
scope: PostgreSQL 15+, extensions, migrations, connection pooling
owner: n04_knowledge
criticality: high
service: postgres (port 5432)
```

## Core Specs
| Spec | Free | Pro (USD 25/mo) | Team (USD 599/mo) |
|------|------|-----------------|---------------------|
| Storage | 500 MB | 8 GB (then USD 0.125/GB) | 8 GB+ |
| Connections | 60 direct | 200 direct | 200+ |
| Pooler (Supavisor) | 200 pooled | 1500 pooled | 3000 pooled |
| Projects | 2 active | Unlimited | Unlimited |
| Daily backups | 0 | 7 days | 14 days |
| PITR | No | Addon USD 100/mo | Addon |
| Branching | No | Yes | Yes |

## Critical Extensions
| Extension | Function | Enable |
|-----------|--------|-----------|
| pgvector | Vector similarity search (embeddings, RAG) | `create extension vector;` |
| pg_graphql | Native GraphQL endpoint over schema | Enabled by default |
| pg_cron | Scheduled jobs (cleanup, sync, reports) | `create extension pg_cron;` |
| pg_net | HTTP requests from within SQL | `create extension pg_net;` |
| pgjwt | JWT gen/validation inside SQL | `create extension pgjwt;` |
| pgcrypto | Encryption functions | Enabled by default |
| pg_stat_statements | Query performance monitoring | Enabled by default |
| plv8 | JavaScript runtime inside SQL | `create extension plv8;` |
| postgis | Geospatial queries | `create extension postgis;` |
| pg_trgm | Fuzzy text search (trigrams) | `create extension pg_trgm;` |
| wrappers | FDW: Stripe, Firebase, S3, BigQuery | `create extension wrappers;` |

## Migration Workflow
```text
[supabase migration new] → [edit SQL] → [supabase db push] → [supabase db diff]
     creates file              schema         applies local     compares remote
     timestamped              changes        or remote         vs local
```

## Connection Patterns
| Method | When to Use | URL |
|--------|-------------|-----|
| Direct (port 5432) | Migrations, admin, long queries | `postgresql://postgres:[pw]@db.[ref].supabase.co:5432/postgres` |
| Pooler Transaction (6543) | App server, serverless, edge | `postgresql://postgres.[ref]:[pw]@aws-0-[region].pooler.supabase.com:6543/postgres` |
| Pooler Session (5432) | Prepared statements, LISTEN/NOTIFY | Pooler URL with `?pgbouncer=true` |
| PostgREST (API) | Client-side, CRUD, filtering | `https://[ref].supabase.co/rest/v1/` |

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Direct connection from serverless | Pool exhaustion, max_connections | Use Supavisor pooler |
| ALTER TABLE in production without migration | Schema drift, impossible rollback | Always `supabase migration new` |
| Unused extension enabled | Memory overhead, slow startup | Enable only what is needed |
| No index on WHERE/JOIN columns | Full table scan, slow query | `CREATE INDEX CONCURRENTLY` |

## Golden Rules
- INDEX every column used in RLS policies (auth.uid() = user_id)
- USE Supavisor for any app with >10 simultaneous connections
- VERSION all DDL via `supabase migration new`
- MONITOR via `pg_stat_statements` — queries >100ms = optimize

## References
- Docs: https://supabase.com/docs/guides/database
- Extensions: https://supabase.com/docs/guides/database/extensions
- CLI migrations: https://supabase.com/docs/guides/cli/managing-environments

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_cli]] | sibling | 0.47 |
| [[bld_tools_supabase_data_layer]] | downstream | 0.47 |
| [[bld_output_template_supabase_data_layer]] | downstream | 0.32 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.32 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.32 |
| [[p01_kc_supabase_self_hosting]] | sibling | 0.31 |
| [[p01_rag_source_supabase]] | related | 0.31 |
| [[p12_wf_supabase_setup]] | downstream | 0.30 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.30 |
| [[bld_config_supabase_data_layer]] | downstream | 0.30 |
