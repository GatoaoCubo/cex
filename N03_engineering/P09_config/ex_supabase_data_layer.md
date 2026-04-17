---
id: ex_supabase_data_layer
kind: supabase_data_layer
pillar: P09
title: Commerce Supabase Data Layer
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_SUPABASE_PROJECT_REF
  - BRAND_NAME
tags: [commerce, template, distillation, supabase, database, backend]
density_score: 1.0
updated: "2026-04-17"
---

## Purpose

Supabase backend specification for a multi-marketplace commerce platform — defines the core tables, RLS policies, storage buckets, edge function auth, and client singleton pattern for `{{BRAND_NAME}}` backend services.

## When to Use

- Bootstrapping a new Supabase project for commerce operations.
- Documenting the data layer for onboarding new developers.
- Reviewing RLS policies during security audits.
- Referencing table schemas when writing edge functions or migrations.

## Project Configuration

| Field | Value |
|-------|-------|
| Project ref | `{{BRAND_SUPABASE_PROJECT_REF}}` |
| Region | `sa-east-1` (São Paulo, Brazil) |
| Database version | PostgreSQL 15+ |
| Auth | Email + magic link + Google OAuth |
| Storage | Supabase Storage (S3-compatible) |
| Edge Functions | Deno runtime |
| Realtime | Enabled on `products` table |

## Core Tables

### `products`

Primary catalog table. Source of truth for all product data.

```sql
create table products (
  id              uuid primary key default gen_random_uuid(),
  sku             text not null unique,
  title           text not null check (char_length(title) between 3 and 255),
  description     text,
  price           numeric(10,2) not null check (price > 0),
  stock           integer not null default 0 check (stock >= 0),
  status          text not null default 'draft' check (status in ('active','draft','archived')),
  category        text,
  images          jsonb default '[]',
  shopify_id      bigint unique,
  bling_id        bigint unique,
  meli_id         text,
  shopify_synced_at timestamptz,
  bling_synced_at   timestamptz,
  created_at      timestamptz default now(),
  updated_at      timestamptz default now()
);
create index idx_products_sku on products(sku);
create index idx_products_status on products(status);
```

### `bling_tokens`

OAuth token storage for Bling ERP.

```sql
create table bling_tokens (
  id            uuid primary key default gen_random_uuid(),
  access_token  text not null,
  refresh_token text not null,
  expires_at    timestamptz not null,
  updated_at    timestamptz default now()
);
```

### `meli_tokens`

OAuth token storage for Mercado Livre.

```sql
create table meli_tokens (
  id            uuid primary key default gen_random_uuid(),
  access_token  text not null,
  refresh_token text not null,
  expires_at    timestamptz not null,
  user_id       bigint,
  updated_at    timestamptz default now()
);
```

### `sync_log`

Audit trail for all sync operations.

```sql
create table sync_log (
  id          uuid primary key default gen_random_uuid(),
  source      text not null,    -- shopify | bling | meli
  mode        text not null,    -- pull | push | bidirectional | single
  synced      integer default 0,
  errors      integer default 0,
  skipped     integer default 0,
  run_at      timestamptz default now()
);
```

### `webhook_errors`

Persistent log of failed webhook deliveries.

```sql
create table webhook_errors (
  id          uuid primary key default gen_random_uuid(),
  source      text,
  topic       text,
  delivery_id text,
  error       text,
  occurred_at timestamptz default now()
);
```

## RLS Policies

```sql
-- Products: service role full access, anon read-only for active
alter table products enable row level security;
create policy "public_read_active" on products for select using (status = 'active');
create policy "service_full_access" on products using (auth.role() = 'service_role');

-- Tokens: service role only (no public access)
alter table bling_tokens enable row level security;
create policy "service_only" on bling_tokens using (auth.role() = 'service_role');
alter table meli_tokens enable row level security;
create policy "service_only" on meli_tokens using (auth.role() = 'service_role');
```

## Storage Buckets

| Bucket | Access | Purpose |
|--------|--------|---------|
| `product-images` | Public read, service write | Product image CDN |
| `audit-reports` | Service only | Reconciliation JSON reports |
| `media-kits` | Public read | Downloadable product media kits |

## Client Singleton Pattern

```typescript
// src/integrations/supabase/client.ts
import { createClient } from '@supabase/supabase-js';
import type { Database } from './types';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const supabase = createClient<Database>(supabaseUrl, supabaseAnonKey);
```

For edge functions, use the service role client:

```typescript
const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!,
);
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference ID |
| `{{BRAND_NAME}}` | Brand name for project naming |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_db_connector_supabase.md` | db_connector | Connection configuration |
| `ex_interface_supabase_tables.md` | interface | Table contracts and type definitions |
| `ex_validator_inventory_invariants.md` | validator | Business rule enforcement |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Primary consumer of this data layer |
