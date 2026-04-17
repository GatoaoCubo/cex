---
id: p01_kc_supabase_data_layer_n04
kind: knowledge_card
pillar: P01
title: "N04 Master KC — Supabase Data Layer Superintendence"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [knowledge-card, supabase, data-layer, N04, superintendent, master]
tldr: "N04 superintends the entire Supabase data layer: defines schemas, RLS, policies for all nuclei. Single config YAML drives 12 modules."
when_to_use: "When N04 needs to design, review, or modify any Supabase data layer configuration"
density_score: 0.90
---

# N04 Supabase Data Layer — Master KC

## N04's Role
N04 (Knowledge) is the SUPERINTENDENT of the Supabase data layer. No nucleus writes schemas or modifies policies without N04's definition. N04:
- Reads company config YAML
- Designs schemas for all nuclei
- Defines RLS policies (who sees what)
- Manages pgvector integration (N04's RAG backend)
- Produces migration SQL for N03 to deploy

## 12 Modules Under N04
| Module | N04 Defines | KCs |
|--------|------------|-----|
| Database | Tables, indexes, extensions | kc_supabase_database |
| Auth | Providers, JWT claims, MFA | kc_supabase_auth |
| RLS | Policies per table per nucleus | kc_supabase_multi_tenant |
| Storage | Buckets, mime types, policies | kc_supabase_storage |
| Realtime | Publications, channels, filters | kc_supabase_realtime |
| Vectors | pgvector config, HNSW indexes | kc_supabase_vectors |
| Edge Functions | Scaffolds, secrets, triggers | kc_supabase_edge_functions |
| REST API | Endpoint design, filtering | kc_supabase_api |
| CLI | Migration workflow | kc_supabase_cli |
| MCP | AI agent tool config | kc_supabase_mcp |
| Self-Hosting | Docker stack if needed | kc_supabase_self_hosting |
| Pricing | Tier selection, cost alerts | kc_supabase_pricing |

## Nucleus Data Contracts
| Nucleus | Tables Owned | Access Level | RLS Pattern |
|---------|-------------|-------------|-------------|
| N01 | research_*, embeddings | read/write own data | org_member |
| N02 | content_*, posts, media | read/write own data | org_member |
| N03 | migrations (no tables) | deploy only | admin |
| N05 | monitoring_*, cron_log | read all, write monitoring | admin |
| N06 | commercial_*, leads | read/write own org | org_member |

## Decision Flow
```text
New company → config YAML → N04 validates
  → N04 generates migrations → N03 deploys
  → N04 notifies each nucleus of their tables/access
  → Nuclei connect via their RLS-scoped credentials
```

## pgvector — N04's RAG Backend
N04 uses pgvector as the concrete backend for embeddings:
- Replaces external vector DBs (Pinecone, Weaviate)
- Same PostgreSQL instance = no extra infra
- RLS on embedding tables = multi-tenant RAG
- HNSW indexes for fast semantic search
- match_documents() function for N04's RAG pipeline

## Escalation Rules
- Schema change request → N04 reviews → migration
- RLS policy conflict → N04 resolves → new policy
- Performance issue → N04 + N05 investigate → index/optimize
- Unresolvable conflict → escalate to N07
