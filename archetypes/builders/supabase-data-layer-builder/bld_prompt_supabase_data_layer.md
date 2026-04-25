---
id: bld_instruction_supabase_data_layer
kind: instruction
pillar: P03
title: "Instructions — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, instruction, pipeline]
tldr: "Supabase Data Layer prompt: prompt template with variables, tone, and generation strategy"
density_score: 0.89
llm_function: REASON
related:
  - p12_wf_supabase_setup
  - bld_output_template_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - p04_tool_supabase_data_layer
  - bld_examples_supabase_data_layer
  - bld_memory_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - bld_quality_gate_supabase_data_layer
  - p04_tpl_supabase_data_layer
---
# Instructions: Supabase Data Layer Pipeline

## Phase 1: INTAKE — Read Config
1. Load company config YAML (identity, project, database, auth, rls, storage, realtime, vectors, edge_functions, integration_cex, budget)
2. Validate tier vs requested features (e.g., CDN requires Pro+, SSO requires Team+)
3. Identify vertical (ecommerce, saas, marketplace, content, costm)
4. Map nucleus consumers: which N01-N06 nuclei will use which modules

## Phase 2: SCHEMA — Design Database
1. Define schemas: `public` (app), `internal` (system), costm per config
2. Design tables per vertical (products, orders, users, orgs, memberships, etc.)
3. Add standard columns: `id UUID DEFAULT gen_random_uuid()`, `created_at`, `updated_at`, `org_id`
4. Enable extensions: pgvector (if vectors), pg_cron (if scheduled), pg_net (if webhooks)
5. Create indexes: every FK, every RLS column (org_id, user_id), sort columns
6. Generate migration SQL file: `supabase/migrations/YYYYMMDD_initial_schema.sql`

## Phase 3: RLS — Row Level Security
1. `ALTER TABLE t ENABLE ROW LEVEL SECURITY;` on EVERY table with user data
2. Apply patterns per table:
   - Owner: `auth.uid() = user_id`
   - Org member: `org_id = (auth.jwt()->'app_metadata'->>'org_id')::uuid`
   - Role-based: `(auth.jwt()->'app_metadata'->>'role') = 'admin'`
   - Public read: `true` FOR SELECT (catalogs, landing pages)
3. Index all columns used in policies
4. Test: login as user A → cannot see user B's data

## Phase 4: AUTH — Configure Authentication
1. Select providers from config (email, Google, Apple, GitHub, etc.)
2. Configure JWT expiry, costm claims (role, org_id, plan)
3. Set MFA if config requires (TOTP enrollment flow)
4. Configure redirect URLs for OAuth callbacks
5. Set costm SMTP if Pro+ (built-in limits 4 emails/hour)

## Phase 5: STORAGE — Configure Buckets
1. Create buckets per config (public vs private)
2. Set max_file_size and allowed_mime_types per bucket
3. Apply storage RLS policies (owner upload, org read, public read)
4. Configure image transforms if needed (resize, webp, quality)
5. Enable CDN if Pro+ and high-traffic assets

## Phase 6: REALTIME — Configure Channels
1. Add tables to publication: `ALTER PUBLICATION supabase_realtime ADD TABLE t;`
2. Configure Postgres Changes subscriptions (INSERT/UPDATE/DELETE per table)
3. Set up Broadcast channels (chat, notifications, live updates)
4. Configure Presence if needed (online users, collaboration)
5. Ensure RLS applies to Realtime (user receives only permitted changes)

## Phase 7: VECTORS — Configure pgvector (if enabled)
1. `CREATE EXTENSION IF NOT EXISTS vector;`
2. Create embedding tables with `VECTOR(N)` matching model dimensions
3. Create `match_documents()` function for semantic search
4. Create HNSW index for tables >1000 rows
5. Configure embedding model + distance function per config
6. Connect to N04's existing RAG infrastructure

## Phase 8: EDGE — Configure Edge Functions
1. Scaffold functions per config: `supabase functions new {name}`
2. Set secrets: `supabase secrets set KEY=value`
3. Configure triggers: HTTP, cron (pg_cron → pg_net), database webhook
4. Add CORS headers for browser clients
5. Configure deploy method (CLI, GitHub Actions, manual)

## Phase 9: DEPLOY — Push & Verify
1. `supabase db reset` — test all migrations locally
2. `supabase db push` — apply to remote
3. `supabase functions deploy` — deploy edge functions
4. Verify RLS: test isolation between tenants
5. Verify API: test REST + GraphQL endpoints
6. Configure MCP if enabled: `.mcp.json` with supabase + postgres servers

## Phase 10: DOCUMENT
1. Output migration SQL + config YAML + RLS summary
2. Signal complete to N07


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_supabase_setup]] | downstream | 0.48 |
| [[bld_output_template_supabase_data_layer]] | related | 0.44 |
| [[bld_manifest_supabase_data_layer]] | related | 0.43 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.42 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.41 |
| [[bld_examples_supabase_data_layer]] | upstream | 0.38 |
| [[bld_memory_supabase_data_layer]] | upstream | 0.36 |
| [[bld_system_prompt_supabase_data_layer]] | related | 0.35 |
| [[bld_quality_gate_supabase_data_layer]] | upstream | 0.33 |
| [[p04_tpl_supabase_data_layer]] | downstream | 0.33 |
