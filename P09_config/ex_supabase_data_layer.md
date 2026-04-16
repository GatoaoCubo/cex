---
id: ex-supabase-data-layer
kind: supabase_data_layer
pillar: P09
title: Supabase Data Layer
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_SUPABASE_PROJECT_REF
  - BRAND_SUPABASE_URL
  - BRAND_SUPABASE_ANON_KEY
  - BRAND_SUPABASE_SERVICE_ROLE_KEY
tags: [commerce, template, distillation, supabase, data_layer]
---

# Supabase Data Layer

## Purpose
Single source of truth for how {{BRAND_NAME}} reads from and writes to Supabase: project identity, client bootstrapping, row-level security posture, storage buckets, and edge-function env contracts. Every other commerce artifact assumes this layer is wired.

## When to use
- Onboarding a new developer / nucleus -- they should read this before touching any DB call.
- Setting up a non-prod (staging / preview) project that mirrors prod.
- Troubleshooting auth errors, RLS denials, or env mismatches.

## Interface
Clients:
- Browser / React app: `@supabase/supabase-js` with anon key.
- Edge functions: `@supabase/supabase-js` with service role key (bypasses RLS).
- Admin scripts: service role key, never committed.

Storage buckets (expected):
- `products/` -- product images, public-read.
- `media-kits/` -- generated kit assets, public-read.
- `uploads/` -- admin uploads before processing, private.

## Brand variables used
- `{{BRAND_SUPABASE_PROJECT_REF}}` -- short project id (e.g. `abcd1234`).
- `{{BRAND_SUPABASE_URL}}` -- full URL `https://{ref}.supabase.co`.
- `{{BRAND_SUPABASE_ANON_KEY}}` -- public JWT, RLS-gated; safe for browser.
- `{{BRAND_SUPABASE_SERVICE_ROLE_KEY}}` -- SECRET; server + edge only; bypasses RLS.

## Client bootstrap
```ts
// src/integrations/supabase/client.ts
import { createClient } from "@supabase/supabase-js";
export const supabase = createClient(
  "{{BRAND_SUPABASE_URL}}",
  "{{BRAND_SUPABASE_ANON_KEY}}",
  { auth: { persistSession: true, detectSessionInUrl: true } },
);
```
No direct fetches, no alternate clients, no service role in the browser -- ever.

## RLS posture
Every user-facing table has RLS enabled. Default policy patterns:
- `products`, `blog_posts` -- `SELECT` public, `INSERT/UPDATE/DELETE` admin-only (via role JWT claim).
- `orders` -- `SELECT` owning user, `INSERT` anon + service role, `UPDATE` service role only.
- `partners` (B2B) -- `SELECT` owning user, `UPDATE` owning user (whitelisted fields), admin can `SELECT` all.
- `sync_runs`, `shopify_sync_log` -- NO public policy; service role only.

## Env contract per runtime
| Runtime | Required | Notes |
|---------|----------|-------|
| Browser (`import.meta.env`) | `VITE_SUPABASE_URL={{BRAND_SUPABASE_URL}}`, `VITE_SUPABASE_ANON_KEY={{BRAND_SUPABASE_ANON_KEY}}` | never include service role |
| Edge functions | `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_ANON_KEY` | auto-injected by Supabase runtime |
| Admin scripts | `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` | pass via `.env.local`, never check in |

## Migrations
- Source: `supabase/migrations/` (SQL files, one timestamped per change).
- Generate types after schema change: `supabase gen types typescript --project-id {{BRAND_SUPABASE_PROJECT_REF}} > src/integrations/supabase/types.ts`.
- Never edit `types.ts` manually -- it's generated.

## Related artifacts
- `ex_db_connector_supabase.md`
- `ex_interface_supabase_tables.md`
