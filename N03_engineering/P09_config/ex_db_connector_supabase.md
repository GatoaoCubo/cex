---
id: ex_db_connector_supabase
kind: db_connector
8f: F5_call
pillar: P09
title: Supabase Database Connector
version: 0.1.0
quality: 8.3
status: template
brand_placeholders:
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, supabase, db_connector, config]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p01_kc_supabase_edge_functions
  - p12_wf_supabase_setup
  - p01_kc_supabase_self_hosting
  - p12_mission_supabase_data_layer
  - p01_kc_supabase_database
  - p01_kc_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - p12_dispatch_rule_supabase
---

## Purpose

Connection configuration spec for Supabase PostgreSQL backend — defines connection parameters, pooling settings, auth modes, and environment variable schema for edge functions and frontend clients.

## When to Use

- Setting up a new environment (staging, production) with Supabase credentials.
- Documenting the connection architecture for security reviews.
- Configuring connection pooling for high-concurrency edge functions.
- Onboarding a developer who needs to run local Supabase.

## Connection Parameters

### Frontend (Browser / React)

| Parameter | Env Var | Example Value |
|-----------|---------|---------------|
| Supabase URL | `VITE_SUPABASE_URL` | `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co` |
| Anon key | `VITE_SUPABASE_ANON_KEY` | `eyJ...` (public, safe in frontend) |
| Auth mode | — | `anon` (RLS enforced) |

### Edge Functions (Deno)

| Parameter | Env Var | Access Level |
|-----------|---------|-------------|
| Supabase URL | `SUPABASE_URL` | Auto-injected by Supabase runtime |
| Service role key | `SUPABASE_SERVICE_ROLE_KEY` | Auto-injected; full bypass RLS |
| Anon key | `SUPABASE_ANON_KEY` | Auto-injected |

### Direct PostgreSQL (Admin / Migrations)

| Parameter | Value |
|-----------|-------|
| Host | `db.{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co` |
| Port | `5432` |
| Database | `postgres` |
| User | `postgres` |
| Password | Supabase Dashboard → Settings → Database |
| SSL | Required (`?sslmode=require`) |

Connection string:
```
postgresql://postgres:{PASSWORD}@db.{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co:5432/postgres?sslmode=require
```

### Pooled Connection (Supavisor — for high concurrency)

| Mode | Port | Use Case |
|------|------|---------|
| Transaction pooling | `6543` | Edge functions, serverless (recommended) |
| Session pooling | `5432` | Long-running connections, migrations |

```
# Transaction pool (for edge functions)
postgresql://postgres.{{BRAND_SUPABASE_PROJECT_REF}}:{PASSWORD}@aws-0-sa-east-1.pooler.supabase.com:6543/postgres
```

## Environment Variables

### Local Development (`.env.local`)

```env
VITE_SUPABASE_URL=https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co
VITE_SUPABASE_ANON_KEY=eyJ...

# For local Supabase (supabase start)
VITE_SUPABASE_URL=http://localhost:54321
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Production (Supabase Edge Secrets)

```bash
# Set via CLI
supabase secrets set SHOPIFY_ADMIN_TOKEN=shpat_...
supabase secrets set BLING_CLIENT_ID={{BRAND_BLING_CLIENT_ID}}
supabase secrets set BLING_CLIENT_SECRET={{BRAND_BLING_CLIENT_SECRET}}
supabase secrets set MELI_CLIENT_ID={{BRAND_MELI_CLIENT_ID}}
supabase secrets set MELI_CLIENT_SECRET={{BRAND_MELI_CLIENT_SECRET}}
supabase secrets set SUPPORT_EMAIL={{BRAND_SUPPORT_EMAIL}}

# List all secrets (values hidden)
supabase secrets list
```

## Connection Health Check

```typescript
// Quick connectivity test
const { data, error } = await supabase.from('products').select('count').limit(1);
if (error) throw new Error(`Supabase connection failed: ${error.message}`);
console.log('Supabase connected. Product count:', data[0].count);
```

## Local Development Setup

```bash
# Install Supabase CLI
npm install -g supabase

# Start local Supabase stack (PostgreSQL + Studio + Auth + Storage)
supabase start

# Apply migrations
supabase db push

# Generate TypeScript types from schema
supabase gen types typescript --local > src/integrations/supabase/types.ts

# Link to production project
supabase link --project-ref {{BRAND_SUPABASE_PROJECT_REF}}
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference ID |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | upstream | 0.78 |
| [[p01_kc_supabase_cli]] | upstream | 0.64 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.50 |
| [[p12_wf_supabase_setup]] | downstream | 0.44 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.44 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.44 |
| [[p01_kc_supabase_database]] | upstream | 0.43 |
| [[p01_kc_supabase_data_layer]] | upstream | 0.39 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.39 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.38 |
