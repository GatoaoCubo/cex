---
id: integration_map_gato3
kind: e2e_eval
title: "GATO3 Marketplace Integration Map"
version: 1.0.0
quality: null
pillar: P07
tags: [shopify, bling, mercado-livre, integration, sync, audit]
nucleus: N05
created: 2026-04-10
---

# GATO3 Marketplace Integration Map

## Architecture Overview

```
                        +-----------------+
                        |   SUPABASE DB   |
                        |   (products)    |
                        | Source of Truth  |
                        +---------+-------+
                                  |
              +-------------------+-------------------+
              |                   |                   |
    +---------v--------+ +-------v--------+ +--------v--------+
    |    SHOPIFY       | |   BLING ERP    | | MERCADO LIVRE   |
    | (storefront +    | | (fiscal/tax +  | | (marketplace)   |
    |  checkout)       | |  inventory)    | |                 |
    +------------------+ +----------------+ +-----------------+
    | Admin API 2025-07| | REST API v3    | | REST API        |
    | Storefront API   | | OAuth2         | | OAuth2          |
    | Webhooks (3)     | | Webhooks (3)   | | OAuth only      |
    +------------------+ +----------------+ +-----------------+
```

## Data Flow Per Edge Function

### SHOPIFY SYNC PATH (6 functions -- WORKING)

| # | Function | Direction | What it does | Status |
|---|----------|-----------|--------------|--------|
| 1 | `unified-sync` (960L) | Bi-directional | Full sync engine: pull/push/bidirectional/single modes. Timestamp-based conflict resolution (newer wins). Scopes: all/inventory/content/price. Rate limited 500ms. | **WORKING** -- most complete function |
| 2 | `sync-shopify-product` (268L) | Supabase -> Shopify | Push single product by ID. Creates if no shopify_product_id, updates if exists. Syncs inventory if enabled. Logs to `shopify_sync_logs`. | **WORKING** |
| 3 | `fetch-from-shopify` (233L) | Shopify -> Supabase | Pull single product from Shopify Admin API. Fixes double UTF-8 encoding ("PortAo" -> "Portao"). Updates name, price, quantity. | **WORKING** |
| 4 | `push-titles-to-shopify` (166L) | Supabase -> Shopify | Batch push all linked product titles/descriptions to Shopify. Rate limited 500ms. | **WORKING** |
| 5 | `create-shopify-checkout` (134L) | Cart -> Shopify Storefront | Creates Shopify cart via Storefront GraphQL API. Adds `?channel=online_store` param. Returns checkoutUrl. | **WORKING** |
| 6 | `shopify-webhook-handler` (215L) | Shopify -> Supabase | Handles 3 webhook topics: products/update, inventory_levels/update, orders/create. HMAC validation via _shared/validation.ts. | **WORKING** |

### BLING ERP SYNC PATH (4 functions -- WORKING but token-dependent)

| # | Function | Direction | What it does | Status |
|---|----------|-----------|--------------|--------|
| 7 | `sync-bling-product` (324L) | Supabase -> Bling | Push single product. Full payload: nome, codigo, marca, preco, estoque, NCM, dimensions, weight, GTIN, images. Logs to `bling_sync_log`. | **WORKING** -- needs valid token |
| 8 | `sync-all-products-bling` (184L) | Supabase -> Bling | Batch sync via calling sync-bling-product for each product. Filters: pending/error/all. Rate limited 500ms. Service-role only. | **WORKING** -- needs valid token |
| 9 | `bling-oauth-callback` (192L) | OAuth flow | GET: exchange authorization code for tokens. POST: refresh tokens. Stores in `bling_credentials`. Tokens expire in 6h. Single-use refresh tokens. | **WORKING** |
| 10 | `bling-webhook` (155L) | Bling -> Supabase | Handles: estoques.alteracao, produtos.alteracao, produtos.excluidos, produtos.incluidos. Updates quantity/status. | **PARTIALLY WORKING** -- webhook secret validation is soft (warn, not reject) |

### MERCADO LIVRE PATH (1 function -- OAUTH ONLY)

| # | Function | Direction | What it does | Status |
|---|----------|-----------|--------------|--------|
| 11 | `meli-oauth-callback` (190L) | OAuth flow | GET: exchange code for tokens. POST: refresh tokens. Stores in `meli_credentials`. Fetches seller info. Tokens expire 6h, refresh lasts 6 months. | **WORKING** -- OAuth only, NO product sync |

### ORCHESTRATION (2 functions -- WORKING)

| # | Function | Direction | What it does | Status |
|---|----------|-----------|--------------|--------|
| 12 | `product-sync-webhook` (167L) | Supabase -> Shopify (trigger) | DB webhook trigger on products INSERT/UPDATE. Auto-calls sync-shopify-product when relevant fields change and shopify_sync_enabled=true. | **WORKING** |
| 13 | `webhook-manager` (352L) | N/A (management) | CRUD for Shopify webhooks. Actions: list/setup/delete/clear/test/status. Creates 3 required webhooks (products/update, inventory_levels/update, orders/create). | **WORKING** |

## Frontend Sync UI

| Component | File | What it does |
|-----------|------|-------------|
| `ShopifySync.tsx` (413L) | Admin page | Per-product push/pull buttons. "Enviar Todos" / "Buscar Todos" batch actions. Shows sync status badges. |
| `Integracoes.tsx` (274L) | Admin page | OAuth status for Bling + ML. Token expiry display. Connect/Reconnect/Refresh buttons. |
| `shopify.ts` (153L) | Library | Storefront API client. Cart creation GraphQL. Public token `ba00cdeffdbdd19b`. |
| `cartStore.ts` (98L) | Zustand store | Cart state with `shopifyVariantId`. Persisted to localStorage as `gato3-shopify-cart`. |

## Database Schema (products table -- integration columns)

| Column | Type | Source | Description |
|--------|------|--------|-------------|
| `shopify_product_id` | VARCHAR | Shopify Admin API | Numeric product ID |
| `shopify_variant_id` | VARCHAR | Shopify Admin API | GraphQL GID format: `gid://shopify/ProductVariant/{id}` |
| `shopify_inventory_item_id` | VARCHAR | Shopify Admin API | For inventory level API calls |
| `shopify_sync_enabled` | BOOLEAN | Manual toggle | Enables auto-sync via product-sync-webhook |
| `shopify_last_sync` | TIMESTAMPTZ | Auto-set | Last successful Shopify sync |
| `inventory_sync_enabled` | BOOLEAN | Manual toggle | Enables inventory push to Shopify |
| `bling_product_id` | BIGINT | Bling API | Bling internal product ID |
| `bling_codigo` | VARCHAR(50) | Bling API | SKU/code in Bling |
| `bling_situacao` | VARCHAR(20) | Bling API | Ativo/Inativo/Excluido |
| `bling_ncm` | VARCHAR(10) | Manual/Bling | Tax classification |
| `bling_last_sync` | TIMESTAMPTZ | Auto-set | Last successful Bling sync |
| `bling_sync_error` | TEXT | Auto-set | Last error message |
| `bling_sync_status` | VARCHAR(20) | Auto-set | pending/synced/error/skipped |
| `meli_item_id` | VARCHAR(20) | ML API | MLB listing ID (e.g. MLB1234567890) |
| `meli_last_sync` | TIMESTAMPTZ | Auto-set | Last ML sync timestamp |
| `sku` | VARCHAR | Manual | Universal SKU |
| `cost_price` | DECIMAL(10,2) | Manual | Unit cost for margin calc |
| `quantity` | INTEGER | Source of truth | Physical stock count |

## Credential Tables

| Table | Columns | Token TTL | Refresh TTL |
|-------|---------|-----------|-------------|
| `bling_credentials` | access_token_encrypted, refresh_token_encrypted, expires_at, scope | 6h | Single-use |
| `meli_credentials` | access_token, refresh_token, expires_at, meli_user_id, scope | 6h | 6 months |

## Sync Log Tables

| Table | Purpose | Key columns |
|-------|---------|-------------|
| `shopify_sync_logs` | Shopify push/pull audit | product_id, action, status, shopify_response |
| `bling_sync_log` | Bling create/update/webhook audit | product_id, bling_product_id, operation, direction, status |

## What EXISTS (Working Sync Paths)

```
[OK] Supabase -> Shopify (Admin API): product CRUD + inventory + images
[OK] Shopify -> Supabase (Admin API): product pull + inventory pull + encoding fix
[OK] Shopify -> Supabase (Webhooks): products/update, inventory_levels/update, orders/create
[OK] Supabase -> Shopify (Storefront): cart creation + checkout URL
[OK] Supabase DB -> Shopify (Trigger): auto-sync on product change
[OK] Supabase -> Bling (REST v3): full product push (name, price, stock, NCM, dims, weight, images)
[OK] Bling -> Supabase (Webhooks): stock change, product update, product delete
[OK] Bling OAuth: authorize + refresh token flow
[OK] ML OAuth: authorize + refresh token flow + seller info fetch
```

## What's MISSING (Gaps)

```
[MISSING] ML product listing sync (create/update items via ML Items API)
[MISSING] ML -> Supabase webhook handler (orders, questions, item updates)
[MISSING] Cross-channel inventory reconciliation (Shopify sale -> Bling + ML update)
[MISSING] Automated token refresh cron (Bling 6h, ML 6h -- both expire silently)
[MISSING] Automated bidirectional sync cron (no scheduled sync exists)
[MISSING] ML order webhook -> Supabase -> update all channels
[MISSING] Shopify order -> Bling fiscal note (NF-e) generation
[MISSING] Overselling prevention (no atomic inventory lock across channels)
[MISSING] Bling -> Shopify sync (Bling stock change does NOT propagate to Shopify)
[MISSING] ML listing status monitoring (active/paused/closed)
```

## What's BROKEN (Code exists but can't work)

```
[BROKEN] Bling webhook secret validation is soft -- warns but does NOT reject invalid secrets
[BROKEN] Bling token refresh requires manual POST -- no cron, tokens expire silently in 6h
[BROKEN] ML credentials stored but unused -- no sync functions consume them
[BROKEN] product-sync-webhook only triggers Shopify sync, ignores Bling and ML
[BROKEN] inventory_sync_enabled flag only affects Shopify push, not Bling or ML
[BROKEN] Bling webhook updates quantity but does NOT propagate to Shopify
[BROKEN] Shopify order webhook decrements Supabase stock but does NOT update Bling stock
```

## Secrets / Environment Variables Required

| Secret | Used by | Status |
|--------|---------|--------|
| `SHOPIFY_ACCESS_TOKEN` | unified-sync, sync-shopify-product, fetch-from-shopify, push-titles, shopify-webhook-handler, webhook-manager | Required -- Admin API |
| `SHOPIFY_STOREFRONT_TOKEN` | create-shopify-checkout | Required -- public token in client code too |
| `SHOPIFY_WEBHOOK_SECRET` | shopify-webhook-handler | Required -- HMAC validation (fail-closed) |
| `BLING_CLIENT_ID` | bling-oauth-callback | Required -- OAuth |
| `BLING_CLIENT_SECRET` | bling-oauth-callback | Required -- OAuth |
| `BLING_API_TOKEN` | sync-bling-product (env fallback) | Optional -- prefers DB credentials |
| `BLING_WEBHOOK_SECRET` | bling-webhook | Optional -- soft validation only |
| `MELI_APP_ID` | meli-oauth-callback | Required -- OAuth |
| `MELI_CLIENT_SECRET` | meli-oauth-callback | Required -- OAuth |
| `WEBHOOK_SECRET` | product-sync-webhook | Optional -- DB webhook auth |
| `SUPABASE_URL` | All functions | Required -- auto-injected |
| `SUPABASE_SERVICE_ROLE_KEY` | All functions | Required -- auto-injected |
