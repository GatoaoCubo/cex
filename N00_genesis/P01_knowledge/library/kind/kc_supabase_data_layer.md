---
id: p01_kc_supabase_data_layer
kind: knowledge_card
type: kind
pillar: P04
title: "Supabase Data Layer — Deep Knowledge for supabase_data_layer"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: supabase_data_layer
quality: 9.1
tags: [supabase_data_layer, P04, CALL, kind-kc, database, api, rls]
tldr: "Supabase-specific data layer config — tables, RLS policies, edge functions, storage buckets, and auth rules as a declarative artifact"
when_to_use: "Building, reviewing, or reasoning about supabase_data_layer artifacts"
keywords: [supabase, data_layer, rls, edge_function, storage, postgres, auth]
feeds_kinds: [supabase_data_layer]
density_score: 1.0
axioms:
  - "AVOID: Storing actual SUPABASE_KEY in the artifact (use env/secret_config)"
  - "AVOID: Defining application logic in RLS policies (keep them data-scoped)"
  - "AVOID: Missing RLS on public tables (security hole)"
linked_artifacts:
  primary: null
  related: []
related:
  - bld_manifest_supabase_data_layer
  - p04_tool_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_instruction_supabase_data_layer
  - bld_schema_supabase_data_layer
  - bld_tools_supabase_data_layer
  - bld_schema_sandbox_config
  - bld_system_prompt_supabase_data_layer
  - bld_memory_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
---

# Supabase Data Layer

## Spec
```yaml
kind: supabase_data_layer
pillar: P04
llm_function: CALL
max_bytes: 8192
naming: p04_supabase_data_layer_{{slug}}.md + .yaml
core: false
```

## Purpose
Defines a complete Supabase backend as a structured artifact — tables with types, Row Level Security policies, edge functions, storage buckets, auth providers, and realtime subscriptions. Captures the entire data-layer topology so it can be reviewed, replicated, or migrated without clicking through the Supabase dashboard.

## Boundary
| Pair | Boundary |
|------|----------|
| supabase_data_layer vs db_connector | supabase_data_layer = Supabase-specific full config; db_connector = generic connection string/driver |
| supabase_data_layer vs api_client | supabase_data_layer = backend definition; api_client = consumer-side SDK/REST config |
| supabase_data_layer vs secret_config | supabase_data_layer = schema/RLS; secret_config = actual keys/passwords |

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique identifier |
| kind | string | yes | Always "supabase_data_layer" |
| pillar | string | yes | P04 |
| tables | list[map] | yes | Table definitions with columns and types |
| rls_policies | list[map] | yes | Row Level Security rules per table |
| edge_functions | list | no | Deno edge function definitions |
| storage_buckets | list | no | Storage bucket configs with policies |
| auth_providers | list | no | Enabled auth providers (email, google, etc) |
| realtime | map | no | Realtime subscription config |

## Quality Gates
1. Every table has at least `id` column with proper type
2. RLS policies exist for every public table
3. No `anon` role has unrestricted write access
4. Edge functions specify runtime (deno) and entry point
5. Naming follows p04_supabase_data_layer_{slug}.md

## Anti-Patterns
- Storing actual SUPABASE_KEY in the artifact (use env/secret_config)
- Defining application logic in RLS policies (keep them data-scoped)
- Missing RLS on public tables (security hole)
- Mixing Supabase config with non-Supabase database configs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_supabase_data_layer]] | upstream | 0.39 |
| [[p04_tool_supabase_data_layer]] | related | 0.39 |
| [[p12_wf_supabase_setup]] | downstream | 0.36 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.33 |
| [[bld_schema_supabase_data_layer]] | upstream | 0.29 |
| [[bld_tools_supabase_data_layer]] | related | 0.29 |
| [[bld_schema_sandbox_config]] | downstream | 0.28 |
| [[bld_system_prompt_supabase_data_layer]] | upstream | 0.28 |
| [[bld_memory_supabase_data_layer]] | upstream | 0.28 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.28 |
