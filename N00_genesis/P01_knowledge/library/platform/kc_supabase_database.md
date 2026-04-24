---
id: p01_kc_supabase_database
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Database — PostgreSQL 15+ com 50+ Extensions"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [supabase, postgresql, database, extensions, migrations, platform]
tldr: "PostgreSQL 15+ gerenciado com 50+ extensions (pgvector, pg_cron, pg_net, pgjwt), migrations versionadas, e REST/GraphQL auto-gerados"
when_to_use: "Quando configurar banco de dados Supabase para qualquer empresa"
keywords: [supabase-database, postgresql, extensions, migrations]
long_tails:
  - Como habilitar extensions no Supabase PostgreSQL
  - Limites de conexao e storage por tier Supabase
  - Migrations versionadas com Supabase CLI
axioms:
  - SEMPRE habilite pgvector se o projeto usa embeddings ou RAG
  - NUNCA exponha a connection string diretamente ao client-side
  - SEMPRE use migrations versionadas, nunca ALTER TABLE manual em producao
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
service: postgres (porta 5432)
```

## Core Specs
| Spec | Free | Pro (USD 25/mo) | Team (USD 599/mo) |
|------|------|-----------------|---------------------|
| Storage | 500 MB | 8 GB (then USD 0.125/GB) | 8 GB+ |
| Connections | 60 direct | 200 direct | 200+ |
| Pooler (Supavisor) | 200 pooled | 1500 pooled | 3000 pooled |
| Projetos | 2 ativos | Ilimitado | Ilimitado |
| Daily backups | 0 | 7 dias | 14 dias |
| PITR | Não | Addon USD 100/mo | Addon |
| Branching | Não | Sim | Sim |

## Extensions Criticas
| Extension | Funcao | Habilitar |
|-----------|--------|-----------|
| pgvector | Vector similarity search (embeddings, RAG) | `create extension vector;` |
| pg_graphql | GraphQL endpoint nativo sobre schema | Habilitado por default |
| pg_cron | Jobs agendados (cleanup, sync, reports) | `create extension pg_cron;` |
| pg_net | HTTP requests de dentro do SQL | `create extension pg_net;` |
| pgjwt | JWT gen/validation inside SQL | `create extension pgjwt;` |
| pgcrypto | Encryption functions | Habilitado por default |
| pg_stat_statements | Query performance monitoring | Habilitado por default |
| plv8 | JavaScript runtime inside SQL | `create extension plv8;` |
| postgis | Geospatial queries | `create extension postgis;` |
| pg_trgm | Fuzzy text search (trigrams) | `create extension pg_trgm;` |
| wrappers | FDW: Stripe, Firebase, S3, BigQuery | `create extension wrappers;` |

## Migration Workflow
```text
[supabase migration new] → [edit SQL] → [supabase db push] → [supabase db diff]
     cria arquivo             schema         aplica local      compara remote
     timestamped              changes        ou remote         vs local
```

## Connection Patterns
| Metodo | Quando Usar | URL |
|--------|-------------|-----|
| Direct (port 5432) | Migrations, admin, long queries | `postgresql://postgres:[pw]@db.[ref].supabase.co:5432/postgres` |
| Pooler Transaction (6543) | App server, serverless, edge | `postgresql://postgres.[ref]:[pw]@aws-0-[region].pooler.supabase.com:6543/postgres` |
| Pooler Session (5432) | Prepared statements, LISTEN/NOTIFY | Pooler URL com `?pgbouncer=true` |
| PostgREST (API) | Client-side, CRUD, filtering | `https://[ref].supabase.co/rest/v1/` |

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Direct connection de serverless | Pool exhaustion, max_connections | Usar Supavisor pooler |
| ALTER TABLE em produção sem migration | Schema drift, rollback impossivel | `supabase migration new` sempre |
| Extension não usada habilitada | Overhead memória, startup lento | Habilitar só o necessário |
| Sem index em colunas de WHERE/JOIN | Full table scan, query lenta | `CREATE INDEX CONCURRENTLY` |

## Golden Rules
- INDEXE toda coluna usada em RLS policies (auth.uid() = user_id)
- USE Supavisor para qualquer app com >10 conexões simultâneas
- VERSIONNE todo DDL via `supabase migration new`
- MONITORE via `pg_stat_statements` — queries >100ms = otimizar

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
