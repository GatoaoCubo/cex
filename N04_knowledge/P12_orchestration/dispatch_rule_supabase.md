---
id: p12_dispatch_rule_supabase
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule — Supabase Data Layer (N04)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [dispatch-rule, supabase, data-layer, N04, routing]
tldr: "Route supabase/database/schema/auth/storage/vector/rls queries to N04 — N04 superintends all data layer decisions"
density_score: 0.88
related:
  - bld_collaboration_supabase_data_layer
  - p12_mission_supabase_data_layer
  - bld_architecture_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - p12_wf_supabase_setup
  - p03_pc_cex_universal
  - bld_sp_collaboration_software_project
  - bld_manifest_supabase_data_layer
  - p04_tool_supabase_data_layer
  - p12_dr_software_project
---

# Dispatch Rule: Supabase → N04

## Trigger Keywords
| Keyword | Confidence | Example Intent |
|---------|-----------|----------------|
| supabase | 0.95 | "configure supabase for..." |
| database schema | 0.85 | "design database schema..." |
| rls policy | 0.90 | "create RLS policies for..." |
| row level security | 0.90 | "setup row level security..." |
| pgvector | 0.90 | "setup vector search in..." |
| storage bucket | 0.85 | "create storage buckets..." |
| realtime channel | 0.85 | "configure realtime for..." |
| edge function | 0.80 | "create edge function..." |
| migration sql | 0.85 | "generate migration for..." |
| multi-tenant | 0.80 | "implement multi-tenant..." |
| data layer | 0.90 | "setup data layer for..." |
| supabase mcp | 0.95 | "configure supabase mcp..." |

## Routing Rules
```yaml
primary_nucleus: N04
confidence_threshold: 0.80
fallback_nucleus: N03  # if purely engineering/deploy task

cross_nucleus_handoffs:
  - condition: "intent contains 'deploy' or 'push'"
    handoff_to: N03
    reason: "N03 handles migration deployment"
  - condition: "intent contains 'research' or 'benchmark'"
    handoff_to: N01
    reason: "N01 handles research using Supabase data"
  - condition: "intent contains 'publish' or 'social' or 'content'"
    handoff_to: N02
    reason: "N02 handles content stored in Supabase"
  - condition: "intent contains 'monitor' or 'backup' or 'alert'"
    handoff_to: N05
    reason: "N05 handles operational monitoring"
  - condition: "intent contains 'crm' or 'lead' or 'sales'"
    handoff_to: N06
    reason: "N06 handles commercial data"
```

## N04 Always Owns
- Schema design (CREATE TABLE, ALTER TABLE)
- RLS policy creation/modification
- Extension management (CREATE EXTENSION)
- pgvector configuration (embeddings, indexes)
- Config YAML structure and validation
- Cross-nucleus data access rules

## Anti-patterns (DON'T route to N04)
| Intent | Route Instead | Why |
|--------|--------------|-----|
| "debug connection timeout" | N05 | Operational issue, not data design |
| "write marketing copy about our DB" | N02 | Copy writing, not data layer |
| "analyze user behavior from DB" | N01 | Research analysis, not schema |
| "price our SaaS based on DB usage" | N06 | Commercial strategy, not data |
| "deploy to production environment" | N03 | Infrastructure deployment |

## Examples
| Intent | Routes To | Why |
|--------|----------|-----|
| "cria schema supabase para e-commerce" | N04 | Schema design |
| "deploy migrations no staging" | N04 → N03 | N04 generates, N03 deploys |
| "pesquisa benchmarks de pgvector" | N04 → N01 | N01 researches, N04 uses |
| "publica posts salvos no supabase" | N04 → N02 | N02 publishes content |
| "monitora quota de storage" | N04 → N05 | N05 monitors ops |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_supabase_data_layer]] | related | 0.52 |
| [[p12_mission_supabase_data_layer]] | related | 0.48 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.46 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.46 |
| [[p12_wf_supabase_setup]] | related | 0.40 |
| [[p03_pc_cex_universal]] | upstream | 0.36 |
| [[bld_sp_collaboration_software_project]] | upstream | 0.36 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.34 |
| [[p04_tool_supabase_data_layer]] | upstream | 0.34 |
| [[p12_dr_software_project]] | sibling | 0.33 |
