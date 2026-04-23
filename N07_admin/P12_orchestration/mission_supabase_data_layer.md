---
id: p12_mission_supabase_data_layer
kind: dag
pillar: P12
title: "Mission: Supabase Data Layer — Universal Data Platform Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_orchestrator
pipeline: domain_builder
domain: orchestration
quality: 9.1
tags: [mission, supabase, data-layer, database, auth, storage, realtime, vectors, edge-functions, N04, multi-tenant]
tldr: "36-artifact mission owned by N04: Supabase builder + 12 module KCs + template + 4 vertical examples + nucleus artifacts. Generic for any company."
node_count: 36
edge_count: 5
estimated_duration: "5-6h"
density_score: 0.95
related:
  - bld_collaboration_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - bld_architecture_supabase_data_layer
  - p12_dispatch_rule_supabase
  - agent_card_n04
  - bld_manifest_supabase_data_layer
  - p12_wf_supabase_setup
  - spec_n01_n04_verticalization
  - bld_system_prompt_supabase_data_layer
  - bld_tools_supabase_data_layer
---

# Mission: Supabase Data Layer

## Overview
Distill complete Supabase platform knowledge (12 modules) into typed CEX artifacts.
N04 (Knowledge) is the SUPERINTENDENT — defines schemas, RLS, policies, data flow.
All other nuclei (N01-N06) CONSUME the Supabase that N04 structures.
Builder is GENERIC — any company [x] fills a config YAML to get full data layer.

## Scope
| Dimension | Value |
|-----------|-------|
| Artifacts | 36 total |
| Phases | 5 (F0-F4) |
| Superintendent | N04 (knowledge) — owns data layer structure |
| Consumers | N01 (research), N02 (content), N03 (migrations), N05 (ops), N06 (CRM) |
| Builder ISOs | 13 |
| Platform KCs | 12 (1 per Supabase module) |
| Examples | 4 verticals (ecommerce, saas, marketplace, content) |
| N04 artifacts | 6 (KC, RAG, embedding, tool, dispatch, workflow) |
| Instance | 1 template (zero company data) |

## Phase DAG
```
F0 (N04: research 12 modules) ──► F1 (N04: 13 ISOs)
                                       │
                                       ▼
                                  F2 (N04: tpl + 4 examples)
                                       │
                                       ├──► F3 (N04: 6 nucleus artifacts)
                                       │
                                       └──► F4 (N04: instance template)
```

## Artifact Manifest
See: `.cex/runtime/handoffs/mission_supabase_data_layer.md` for full spec.

## Key Differentiators
- 12 platform KCs (not just DB — Auth, Storage, Realtime, Vectors, Edge, MCP)
- Multi-tenant patterns via RLS (org isolation without hardcode)
- pgvector integration connects with existing N04 RAG infrastructure
- Zero company data — instance template has only [PLACEHOLDERS]
- MCP config for @supabase/mcp-server-supabase

## Connections to Existing Builders
| Builder | Connection |
|---------|-----------|
| research-pipeline | pgvector as RAG retrieval backend |
| social-publisher | Storage for media, DB for scheduling |
| db-connector | Supabase as connector type (PostgREST + WS) |
| retriever | pgvector as retrieval backend |
| mcp-server | @supabase/mcp-server as reference |

## Status
- [ ] F0: Research (12 KCs)
- [ ] F1: Builder (13 ISOs)
- [ ] F2: Templates + Examples
- [ ] F3: N04 Artifacts
- [ ] F4: Instance Template

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_supabase_data_layer]] | related | 0.56 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.53 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.52 |
| [[p12_dispatch_rule_supabase]] | related | 0.50 |
| [[agent_card_n04]] | upstream | 0.44 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.39 |
| [[p12_wf_supabase_setup]] | related | 0.36 |
| [[spec_n01_n04_verticalization]] | upstream | 0.35 |
| [[bld_system_prompt_supabase_data_layer]] | upstream | 0.34 |
| [[bld_tools_supabase_data_layer]] | upstream | 0.34 |
