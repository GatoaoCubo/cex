---
id: bld_architecture_supabase_data_layer
kind: architecture
pillar: P02
title: "Architecture — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [builder, supabase, data-layer, architecture, multi-nucleus]
density_score: 0.90
llm_function: CONSTRAIN
related:
  - p01_kc_supabase_data_layer_n04
  - bld_collaboration_supabase_data_layer
  - p12_mission_supabase_data_layer
  - p12_dispatch_rule_supabase
  - spec_n01_n04_verticalization
  - bld_knowledge_card_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_manifest_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - p04_tool_supabase_data_layer
---
# Architecture

## Component Inventory
| Component | Role | Module | Owner |
|-----------|------|--------|-------|
| PostgreSQL 15+ | Core database, SQL, extensions | Database | N04 |
| GoTrue | Auth server, JWT, OAuth | Auth | N04 |
| PostgREST | Auto-generated REST API | API | N04 |
| pg_graphql | Auto-generated GraphQL | API | N04 |
| Realtime | WebSocket server | Realtime | N04 |
| Storage API | File management, buckets | Storage | N04 |
| imgproxy | Image transforms | Storage | N04 |
| Edge Runtime | Deno serverless functions | Edge | N04 |
| Kong | API gateway, routing | Infrastructure | N04 |
| Studio | Dashboard web UI | Management | N04 |
| Supabase CLI | Migrations, deploy | Tooling | N04 |
| MCP Server | AI agent tools | Integration | N04 |

## Multi-Nucleus Data Flow
```text
              ┌─────────────────────────────────────────┐
              │         N04 (Superintendent)             │
              │  Schemas, RLS, Policies, Config, Flow    │
              └─────────────┬───────────────────────────┘
                            │ defines
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  ┌──────────┐      ┌──────────┐        ┌──────────┐
  │ Database │      │ Storage  │        │ Realtime │
  │ +pgvector│      │ +CDN     │        │ +Presence│
  └────┬─────┘      └────┬─────┘        └────┬─────┘
       │                  │                   │
  ┌────┴──────────────────┴───────────────────┴────┐
  │                    Kong (Gateway)               │
  └─┬──────┬──────┬──────┬──────┬──────┬──────────┘
    │      │      │      │      │      │
   N01    N02    N03    N04    N05    N06
 research content migrations knowledge ops  commercial
```

## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| Config YAML | N04 | input | Company requirements |
| N04 | Database | defines | Schema, tables, indexes |
| N04 | Auth | defines | Providers, claims, MFA |
| N04 | RLS | defines | Policies per table |
| N04 | Storage | defines | Buckets, policies, transforms |
| N04 | Realtime | defines | Publications, channels |
| N04 | pgvector | defines | Embedding tables, indexes |
| N04 | Edge | defines | Functions, secrets, triggers |
| N01 | Database+pgvector | reads/writes | Research data, embeddings |
| N02 | Database+Storage | reads/writes | Content, media files |
| N03 | CLI+Edge | executes | Migrations, deploys |
| N05 | pg_cron+Realtime | monitors | Scheduled jobs, alerts |
| N06 | Database | reads/writes | CRM, transactions |

## Boundary
| IS | IS NOT |
|----|--------|
| Config-driven infrastructure | Runtime application code |
| Multi-tenant by default | Single-tenant assumption |
| All 12 modules, one config | Database-only setup |
| Generic for any vertical | Hardcoded to one company |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.64 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.62 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.52 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.50 |
| [[spec_n01_n04_verticalization]] | downstream | 0.43 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.40 |
| [[p12_wf_supabase_setup]] | downstream | 0.39 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.38 |
| [[bld_system_prompt_supabase_data_layer]] | downstream | 0.37 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.34 |
