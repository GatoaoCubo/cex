---
id: bld_memory_supabase_data_layer
kind: memory
pillar: P01
title: "Memory — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, memory, learnings]
tldr: "Supabase Data Layer knowledge: context persistence, recall triggers, and state management"
density_score: 0.85
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
related:
  - bld_knowledge_card_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_manifest_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - bld_quality_gate_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_multi_tenant
  - bld_examples_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
---
# Builder Memory

## Summary
The Supabase Data Layer builder produces configuration artifacts (YAML + SQL) that define a complete data platform for any company. The most critical lesson: RLS is not optional — every table with user data MUST have row-level security. Multi-tenant isolation via org_id in JWT claims is the default pattern.

## Patterns That Work
1. **Config-first**: Single YAML file drives all infrastructure decisions
2. **RLS-by-default**: Enable RLS on table creation, not as afterthought
3. **Org isolation**: org_id column + JWT app_metadata claim = simple multi-tenant
4. **Migration discipline**: All DDL via `supabase migration new`, never manual
5. **Tier awareness**: Design features within tier limits, document overage risks
6. **Index everything RLS touches**: org_id, user_id, any column in policies
7. **12-module thinking**: Supabase is a platform, not just a database

## Anti-Patterns Learned
- Hardcoded project_ref breaks when migrating between environments
- service_role_key in client-side code = complete security bypass
- RLS with unindexed subqueries kills performance at scale
- Wildcard mime types in storage buckets = security vulnerability
- Ignoring tier limits leads to silent failures or surprise billing
- Manual Dashboard changes create unreproducible schema drift
- Subscribing to all Realtime tables overloads WAL processing

## Key Decisions
| Decision | Rationale |
|----------|-----------|
| org_id over user_id for isolation | Supports teams/orgs, not just individuals |
| JWT claims over membership table lookup | Faster RLS policy evaluation |
| HNSW over IVFFlat for vectors | Better recall + query speed for production |
| Supavisor over direct connections | Required for serverless/edge workloads |
| pg_cron + pg_net for async | Avoid Edge Function CPU limits for background jobs |

## Context
This builder was created for CEX (Codexa) to enable any company to get a complete data layer via config. N04 superintends — no nucleus writes to Supabase without N04's schema definition. Learning records are appended as companies onboard and edge cases surface.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_supabase_data_layer]] | related | 0.48 |
| [[p12_wf_supabase_setup]] | downstream | 0.46 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.45 |
| [[bld_system_prompt_supabase_data_layer]] | downstream | 0.41 |
| [[bld_quality_gate_supabase_data_layer]] | downstream | 0.41 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.40 |
| [[p01_kc_supabase_multi_tenant]] | related | 0.39 |
| [[bld_examples_supabase_data_layer]] | related | 0.37 |
| [[bld_output_template_supabase_data_layer]] | downstream | 0.36 |
| [[p01_kc_supabase_data_layer_n04]] | related | 0.33 |
