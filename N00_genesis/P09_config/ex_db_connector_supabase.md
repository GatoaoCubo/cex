---
id: ex-db-connector-supabase
kind: db_connector
pillar: P09
title: Supabase DB Connector
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SUPABASE_URL
  - BRAND_SUPABASE_SERVICE_ROLE_KEY
  - BRAND_SUPABASE_ANON_KEY
tags: [commerce, template, distillation, supabase, db_connector]
---

# Supabase DB Connector

## Purpose
Edge-function and Node-runtime connector for Supabase Postgres. Wraps connection lifecycle, query helpers, and error normalization. Co-lives with `ex_supabase_data_layer.md` but is specifically about the *machinery* of reading/writing, not project identity.

## When to use
- Any edge function writing to tables (products, inventory, orders, etc.).
- Cron jobs and one-shot scripts that need service-role access.
- Typed CRUD needs in Node.js scripts (e.g. migration helpers).

## Interface
```ts
// db.ts
import { createClient, SupabaseClient } from "@supabase/supabase-js";
import type { Database } from "./types";

export function getDb(mode: "anon" | "service" = "service"): SupabaseClient<Database> {
  const key = mode === "service"
    ? Deno.env.get("{{BRAND_SUPABASE_SERVICE_ROLE_KEY}}")!
    : Deno.env.get("{{BRAND_SUPABASE_ANON_KEY}}")!;
  return createClient<Database>(Deno.env.get("{{BRAND_SUPABASE_URL}}")!, key, {
    auth: { persistSession: false },
    db: { schema: "public" },
  });
}
```

## Brand variables used
- `{{BRAND_SUPABASE_URL}}` -- project URL.
- `{{BRAND_SUPABASE_SERVICE_ROLE_KEY}}` -- server-only; never exposed.
- `{{BRAND_SUPABASE_ANON_KEY}}` -- used when the connector must NOT bypass RLS (rare on server; use for end-user-context queries).

## Helper patterns
```ts
// typed upsert with conflict target
await db.from("products")
  .upsert({ sku, title, updated_at: new Date().toISOString() }, { onConflict: "sku" })
  .throwOnError();

// paginated select
const { data, error } = await db.from("products")
  .select("id, sku, title")
  .range(offset, offset+limit-1)
  .order("updated_at", { ascending: false });

// raw RPC
const { data } = await db.rpc("reconcile_inventory", { sku_list: [...] });
```

## Error normalization
PostgREST surfaces errors as `{ message, details, hint, code }`. Normalize at the connector edge:
- `23505` (unique_violation) -> `DbError.UniqueViolation` with `constraint` field.
- `23503` (foreign_key_violation) -> `DbError.FkViolation`.
- `PGRST116` (not found on .single()) -> `null`, not throw.
- Anything else -> `DbError.Unknown` with original code preserved.

## Connection hygiene
Supabase's JS client is stateless -- no pool to manage. However:
- Do NOT create a new client on every request; reuse a module-level singleton per scope.
- For long-running scripts, unsubscribe realtime channels before exit to avoid dangling sockets.

## Row-level security notes
- Using `service` mode bypasses RLS; never pass user input to service-mode queries without sanitization.
- For per-user queries, use `anon` mode + pass the user's JWT via `global.headers.Authorization`.

## Related artifacts
- `ex_supabase_data_layer.md` -- project-level config.
- `ex_interface_supabase_tables.md` -- typed surface.
