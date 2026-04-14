---
id: bld_collaboration_supabase_data_layer
kind: collaboration
pillar: P12
title: "Collaboration — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [builder, supabase, data-layer, collaboration, multi-nucleus]
density_score: 1.0
llm_function: COLLABORATE
---
# Collaboration Map

## N04 as Superintendent
N04 (Knowledge) owns the Supabase data layer. No nucleus writes schemas or policies without N04's definition. N04 reads the config YAML, produces migration SQL + RLS policies + module configs, and each nucleus receives its specific access scope.

## Handoff Matrix
| From | To | Trigger | Payload | Signal |
|------|-----|---------|---------|--------|
| N07 | N04 | New company config YAML | Config file path | mission_start |
| N04 | N01 | Schema ready for research | Tables: research_*, pgvector config | schema_ready_n01 |
| N04 | N02 | Schema ready for content | Tables: content_*, storage buckets | schema_ready_n02 |
| N04 | N03 | Migrations ready for deploy | supabase/migrations/ dir | migrations_ready |
| N04 | N05 | Monitoring config ready | pg_cron jobs, Realtime alerts | monitoring_ready |
| N04 | N06 | CRM schema ready | Tables: commercial_*, RLS policies | schema_ready_n06 |
| N01 | N04 | Research needs new table/index | Schema change request | schema_request |
| N02 | N04 | Content needs new bucket/table | Storage + schema request | storage_request |
| N03 | N04 | Migration applied | Deploy confirmation | deploy_complete |
| N05 | N04 | Alert triggered | Monitoring event | alert_fired |

## Cross-Builder Dependencies
| Builder | Connection | Data Exchange |
|---------|-----------|---------------|
| research-pipeline-builder | pgvector as retrieval backend | Embedding tables, match_documents() |
| social-publisher-builder | Storage for media, DB for scheduling | content_* tables, media buckets |
| db-connector-builder | Supabase as connector type | PostgREST + WebSocket configs |
| retriever-builder | pgvector as search backend | Vector indexes, distance functions |
| embedding-config-builder | pgvector dimensions + model | VECTOR(N) column spec |
| mcp-server-builder | @supabase/mcp-server reference | MCP tools config |
| webhook-builder | Edge Functions as receivers | Function scaffolds + secrets |
| env-config-builder | Supabase env vars | SUPABASE_URL, keys, DB URL |

## Conflict Resolution
| Conflict | Resolution |
|----------|-----------|
| N01 wants new table | N04 reviews, creates migration, applies RLS |
| N02 wants public bucket | N04 validates mime types + size limits first |
| N03 deploys breaking migration | N04 reviews diff, requires branch test first |
| N05 pg_cron overloads DB | N04 adjusts schedule, adds connection limits |
| N06 needs cross-org query | N04 creates admin RLS policy with role check |

## Escalation Path
```text
Nucleus request → N04 reviews → schema change? → migration + RLS → deploy via N03
                                → config change? → update YAML → notify consumers
                                → conflict? → escalate to N07
```
