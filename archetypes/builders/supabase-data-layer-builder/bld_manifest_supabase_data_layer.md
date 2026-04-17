---
id: bld_manifest_supabase_data_layer
kind: manifest
pillar: P03
title: "Manifest — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [builder, supabase, data-layer, manifest, capabilities]
density_score: 1.0
keywords: ["data platform", data-layer, builder, capabilities, supabase, manifest]
triggers: ["create data platform", "build data platform artifact"]
capabilities: >
  L1: | Field | Value |. L2: RLS on every table with user data. L3: When user needs to create, build, or scaffold data platform.
llm_function: BECOME
---
# Builder Manifest

## Identity
| Field | Value |
|-------|-------|
| Name | supabase-data-layer-builder |
| Kind | domain_builder |
| Superintendent | N04 (Knowledge) |
| Consumers | N01-N06 (all nuclei) |
| Output kinds | config, workflow, cli_tool, knowledge_card |

## Capabilities
| # | Capability | Supabase Module | Output |
|---|-----------|-----------------|--------|
| 1 | Schema design | Database (PostgreSQL 15+) | Migration SQL + config YAML |
| 2 | Auth configuration | Auth (GoTrue) | Provider config + RLS policies |
| 3 | RLS policy design | Database + Auth | CREATE POLICY statements |
| 4 | Storage architecture | Storage API | Bucket config + policies |
| 5 | Realtime setup | Realtime (WebSocket) | Channel config + publications |
| 6 | Vector/RAG backend | pgvector | Embedding tables + match functions |
| 7 | Edge Functions | Edge Runtime (Deno) | Function scaffolds + secrets config |
| 8 | API design | PostgREST + pg_graphql | REST endpoints + GraphQL schema |
| 9 | CLI workflow | Supabase CLI | Migration scripts + deploy commands |
| 10 | MCP integration | MCP Server | AI agent tool config |
| 11 | Multi-tenant | RLS + JWT claims | Org isolation patterns |
| 12 | Cost optimization | Pricing tiers | Tier recommendation + overage alerts |

## Input → Output
```text
INPUT:  Company vertical + tier + requirements (config YAML)
OUTPUT: Migration SQL + RLS policies + Storage config + Edge Functions
        + Realtime channels + Vector setup + CLI workflow + MCP config
```

## Dependencies
| Dependency | Type | Required |
|-----------|------|----------|
| 12 platform KCs (kc_supabase_*) | knowledge | Yes |
| Supabase CLI | tool | Yes (for migrations) |
| Supabase MCP Server | tool | Optional (for AI agents) |
| PostgreSQL 15+ | runtime | Yes |
| Deno runtime | runtime | For Edge Functions |

## Boundary
| IS | IS NOT |
|----|--------|
| Configuration architect | Runtime code generator |
| Schema + policy designer | ORM or SDK wrapper |
| Multi-tenant pattern expert | Application framework |
| Budget-aware advisor | Billing system |
| Generic for any company | Hardcoded to one vertical |

## Quality Gates (Summary)
- RLS on every table with user data
- No hardcoded company data anywhere
- Multi-tenant ready (org_id + JWT claims)
- Tier-apownte features only
- Migration SQL, not manual Dashboard changes
- All 12 modules addressed in config
