---
id: p12_wf_supabase_setup
kind: workflow
pillar: P12
title: "Workflow — Supabase New Project Setup"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [workflow, supabase, setup, data-layer, N04]
tldr: "7-step workflow: config intake → schema design → RLS → modules → edge functions → deploy → verify. N04 superintends, N03 deploys."
steps_count: 7
execution: sequential
depends_on: []
signals: [schema_ready, rls_applied, deployed, verified]
density_score: 0.90
related:
  - bld_manifest_supabase_data_layer
  - p04_tool_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - bld_collaboration_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_memory_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - p12_dispatch_rule_supabase
  - bld_architecture_supabase_data_layer
---

# Workflow: Supabase New Project Setup

## Purpose
End-to-end workflow for N04 to set up a complete Supabase data layer from a company config YAML. Produces migration SQL, RLS policies, and module configs.

## Anti-patterns (When NOT to Use)
| Scenario | Why Not | Use Instead |
|----------|---------|-------------|
| Existing Supabase project with data | Risk data loss from schema conflicts | Manual migration workflow |
| Single-tenant app (no org_id) | RLS adds unnecessary complexity | Simple schema without RLS |
| Prototype/MVP with <10 tables | Overhead exceeds benefit | Direct Supabase dashboard setup |
| Non-standard auth (not JWT) | RLS policies assume JWT claims | Custom auth + manual policies |
| Serverless-only (no edge functions) | Scaffolds unused functions | Skip steps 5-6, use API only |

## Steps

### Step 1: Config Intake [N04]
- **Action**: Load and validate company config YAML
- **Input**: Config file path
- **Output**: Validated config object
- **Checks**: All required sections present, tier matches features, no hardcoded data
- **Signal**: config_validated

### Step 2: Schema Design [N04]
- **Action**: Generate CREATE TABLE + indexes for all tables
- **Input**: Validated config (database section)
- **Output**: `migrations/001_schema.sql`
- **Checks**: org_id column on shared tables, indexes on FKs + sort columns
- **Signal**: schema_ready

### Step 3: RLS Policies [N04]
- **Action**: Generate ENABLE RLS + CREATE POLICY for every table
- **Input**: Config (rls section + table definitions)
- **Output**: `migrations/002_rls.sql`
- **Checks**: Every user-data table has RLS, patterns match JWT claims
- **Signal**: rls_applied

### Step 4: Module Configuration [N04]
- **Action**: Configure Storage, Realtime, Vectors, Auth per config
- **Input**: Config (storage, realtime, vectors, auth sections)
- **Output**: `migrations/003_modules.sql` + bucket configs
- **Checks**: Tier-appropriate features only, pgvector index if >1K rows
- **Signal**: modules_configured

### Step 5: Edge Functions [N04 → N03]
- **Action**: Scaffold edge functions, set secrets
- **Input**: Config (edge_functions section)
- **Output**: `functions/{name}/index.ts` + secrets list
- **Checks**: CORS headers present, secrets not hardcoded
- **Signal**: functions_ready

### Step 6: Deploy [N03]
- **Action**: Apply migrations and deploy functions
- **Input**: All migration files + function scaffolds
- **Output**: Applied schema on Supabase project
- **Commands**: `supabase db push` + `supabase functions deploy`
- **Signal**: deployed

### Step 7: Verify [N04 + N05]
- **Action**: Test RLS isolation, API endpoints, realtime channels
- **Input**: Deployed project
- **Output**: Verification report
- **Checks**: Tenant A cannot see tenant B data, API returns correct data
- **Signal**: verified

## Dependencies
- Supabase CLI installed and linked to project
- Company config YAML filled with real values
- Access token for Supabase project (service_role for migrations)

## Error Recovery
| Step | Error | Recovery |
|------|-------|----------|
| 1 | Invalid config | Return validation errors, fix config |
| 2 | Schema conflict | `supabase db diff` to find conflicts |
| 3 | RLS recursion | Simplify policy, use JWT claims instead |
| 6 | Migration fails | Fix SQL, `db reset` local, retry push |
| 7 | RLS leak | Add missing policy, re-deploy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_supabase_data_layer]] | upstream | 0.57 |
| [[p04_tool_supabase_data_layer]] | upstream | 0.53 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.46 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.44 |
| [[bld_collaboration_supabase_data_layer]] | related | 0.44 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.41 |
| [[bld_memory_supabase_data_layer]] | upstream | 0.40 |
| [[bld_system_prompt_supabase_data_layer]] | upstream | 0.40 |
| [[p12_dispatch_rule_supabase]] | related | 0.39 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.37 |
