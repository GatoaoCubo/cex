---
id: bld_knowledge_card_supabase_data_layer
kind: knowledge_card
pillar: P01
title: "Builder KC — Supabase Data Layer Architecture & Tradeoffs"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [builder, supabase, data-layer, architecture, tradeoffs]
tldr: "Supabase Data Layer knowledge: domain knowledge, terminology, and contextual background"
density_score: 1.0
when_to_use: "Use when building knowledge card artifacts for data_platform"
keywords: [layer, knowledge-card, matrix, summary, data_platform]
linked_artifacts:
  primary: null
  related: []
llm_function: INJECT
related:
  - bld_manifest_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_memory_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - bld_architecture_supabase_data_layer
  - bld_schema_supabase_data_layer
  - p04_tool_supabase_data_layer
  - bld_examples_supabase_data_layer
---
# Supabase Data Layer — Builder Knowledge

## Executive Summary
Supabase is a full data platform (not just a database): PostgreSQL 15+ with 12 integrated modules. The builder designs config-driven data layers where a single YAML file determines the entire infrastructure. N04 (Knowledge) superintends — defines schemas, RLS, policies. All other nuclei consume.

## Module Decision Matrix
| Module | Always Enable | If Config Says | Never on Free |
|--------|-------------|----------------|---------------|
| Database | ✅ | — | — |
| Auth | ✅ | — | — |
| RLS | ✅ | — | — |
| Storage | If media/files needed | `storage.buckets` defined | — |
| Realtime | If live updates needed | `realtime.habilitado: true` | — |
| pgvector | If RAG/embeddings | `vectors.habilitado: true` | — |
| Edge Functions | If serverless compute | `edge_functions.functions` defined | — |
| CDN | If high-traffic assets | tier >= Pro | ✅ |
| PITR | If data-critical | tier >= Pro + addon | ✅ |
| SSO SAML | If enterprise auth | tier >= Team | ✅ |
| Branching | If team dev workflow | tier >= Pro | ✅ |

## Multi-Tenant Architecture
```text
[Company X Config YAML]
    → [N04 reads config]
    → [Schema: public + org isolation via org_id]
    → [RLS: every table filtered by org_id from JWT]
    → [Storage: buckets per org/{org_id}/]
    → [Realtime: changes filtered by RLS]
    → [Vectors: embeddings scoped by org_id metadata]
    → [Edge: functions check JWT org claim]
```

## Tier-Feature Mapping
| Feature | Free | Pro | Team |
|---------|------|-----|------|
| Max DB | 500 MB | 8 GB+ | 8 GB+ |
| Max Storage | 1 GB | 100 GB+ | 100 GB+ |
| Edge CPU | 2s | 10s | 150s |
| CDN | ❌ | ✅ | ✅ |
| Daily backups | ❌ | 7d | 14d |
| SSO | ❌ | Addon | ✅ |
| SOC2 | ❌ | ❌ | ✅ |

## Nucleus Data Flow
| Nucleus | Writes To | Reads From | Module |
|---------|-----------|------------|--------|
| N01 (Intelligence) | research_results, embeddings | sources, vectors | DB + pgvector |
| N02 (Marketing) | posts, products, media | content, schedules | DB + Storage |
| N03 (Engineering) | migrations, functions | schemas, deploys | CLI + Edge |
| N04 (Knowledge) | ALL schemas, policies | ALL config | ALL modules |
| N05 (Operations) | backups, monitoring | alerts, metrics | pg_cron + Realtime |
| N06 (Commercial) | leads, transactions | CRM data, reports | DB + RLS |

## Critical Anti-Patterns
| Anti-Pattern | Consequence |
|-------------|-------------|
| RLS disabled on user tables | Data leak across tenants |
| service_role_key in client | Complete RLS bypass |
| No index on org_id | Full table scan on every query |
| Hardcoded project_ref | Config breaks on project change |
| Features above tier | Runtime errors, silent failures |
| Manual schema changes | Migration drift, unreproducible |

## Extension Checklist
| Extension | Enable When | Impact |
|-----------|------------|--------|
| pgvector | Any RAG/embeddings/search | Core for N04 |
| pg_cron | Scheduled jobs (cleanup, sync) | Core for N05 |
| pg_net | HTTP from SQL (webhooks) | Edge triggers |
| pg_graphql | GraphQL needed alongside REST | Auto-enabled |
| postgis | Geospatial queries | Location-based apps |
| wrappers | External data (Stripe, S3) | Integrations |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_supabase_data_layer]] | downstream | 0.47 |
| [[p12_wf_supabase_setup]] | downstream | 0.46 |
| [[bld_memory_supabase_data_layer]] | related | 0.46 |
| [[bld_system_prompt_supabase_data_layer]] | downstream | 0.45 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.44 |
| [[p01_kc_supabase_data_layer_n04]] | sibling | 0.43 |
| [[bld_architecture_supabase_data_layer]] | downstream | 0.43 |
| [[bld_schema_supabase_data_layer]] | downstream | 0.40 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.39 |
| [[bld_examples_supabase_data_layer]] | related | 0.38 |
