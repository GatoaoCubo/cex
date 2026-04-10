---
id: sync_health_gato3
kind: e2e_eval
title: "GATO3 Sync Health Report"
version: 1.0.0
quality: null
pillar: P07
tags: [sync, health, audit, shopify, bling, mercado-livre, race-condition]
nucleus: N05
created: 2026-04-10
---

# GATO3 Sync Health Report

## Executive Summary

The GATO3 product sync ecosystem has **13 edge functions** totaling ~3,200 lines of TypeScript. Shopify integration is **mature and bidirectional** with webhook support. Bling ERP integration is **functional but fragile** (token expiry is the main risk). Mercado Livre integration is **OAuth-only** -- zero product sync exists.

**Critical finding**: There is no cross-channel inventory reconciliation. A Shopify sale decrements Supabase stock but does NOT update Bling or ML. This creates an overselling risk on multi-channel orders.

---

## Per-Function Analysis

### 1. unified-sync (960 lines) -- HEALTHY

**What it does**: Full bidirectional sync engine with 4 modes (pull/push/bidirectional/single) and 4 scopes (all/inventory/content/price). Timestamp-based conflict resolution with 60-second tolerance.

**Dependencies**: SHOPIFY_ACCESS_TOKEN, Supabase service client.

**Strengths**:
- Most complete sync function in the codebase
- DryRun mode for safe testing
- Force mode to override timestamps
- Proper pagination via Shopify `Link` header
- Double-encoding fix (`fixDoubleEncoding`)
- Rate limiting (500ms between API calls)
- Detailed per-product sync results with change tracking

**Failure modes**:
- No retry logic on Shopify API 429 (rate limit) responses
- Pagination uses `page_info` parameter (correct for cursor-based, but raw `Response` type handling is fragile)
- No timeout on individual product sync operations
- Bidirectional mode fetches ALL Shopify products even if only 1 changed

**Risk**: LOW -- well-structured, comprehensive

### 2. sync-shopify-product (268 lines) -- HEALTHY

**What it does**: Single-product push from Supabase to Shopify. Creates new or updates existing. Updates inventory if `inventory_sync_enabled`.

**Dependencies**: SHOPIFY_ACCESS_TOKEN, product.shopify_product_id.

**Failure modes**:
- No idempotency guard -- calling twice creates duplicate Shopify products if first call succeeded but Supabase update failed
- Images are sent on every sync (Shopify may re-download them each time)
- Hardcoded vendor: 'GATO3' and product_type: 'Acessorios para Gatos'

**Risk**: LOW

### 3. fetch-from-shopify (233 lines) -- HEALTHY

**What it does**: Pull single product from Shopify, update Supabase with name/price/quantity. Fixes double UTF-8 encoding.

**Dependencies**: SHOPIFY_ACCESS_TOKEN, product.shopify_product_id.

**Failure modes**:
- Does not update images (pull only pulls name, price, quantity, description)
- `stripHtml` regex (`/<[^>]*>/g`) is naive -- may break on malformed HTML

**Risk**: LOW

### 4. push-titles-to-shopify (166 lines) -- HEALTHY

**What it does**: Batch push all linked product titles and descriptions to Shopify.

**Failure modes**:
- No pagination on Supabase query (if >1000 products, may miss some)
- Sequential processing with no parallelism

**Risk**: LOW

### 5. create-shopify-checkout (134 lines) -- HEALTHY

**What it does**: Creates Shopify cart via Storefront GraphQL API. Returns checkout URL with `?channel=online_store` parameter.

**Dependencies**: SHOPIFY_STOREFRONT_TOKEN.

**Failure modes**:
- No stock validation before cart creation -- user can add items that are out of stock
- No cart expiry handling

**Risk**: LOW (Shopify handles checkout-side stock validation)

### 6. shopify-webhook-handler (215 lines) -- HEALTHY with CAVEAT

**What it does**: Processes 3 Shopify webhook topics:
- `products/update`: Updates name, description, price, variant IDs
- `inventory_levels/update`: Updates quantity
- `orders/create`: Decrements Supabase stock per line item

**Dependencies**: SHOPIFY_WEBHOOK_SECRET (fail-closed -- rejects if not configured).

**Security**: STRONG
- HMAC-SHA256 validation via `_shared/validation.ts`
- Shop domain validation against expected domain
- Fail-closed: rejects if secret is not configured

**Failure modes**:
- `orders/create` decrements Supabase stock but does NOT update Bling stock -- **OVERSELLING RISK**
- No deduplication -- if Shopify retries a webhook, stock gets decremented twice
- Looks up by `shopify_variant_id` with GID format, but stored format may differ

**Risk**: MEDIUM -- order handler has cross-channel propagation gap

### 7. sync-bling-product (324 lines) -- CONDITIONAL

**What it does**: Full product push to Bling. Maps all fields: name, code, brand, price, cost, stock, NCM, dimensions, weight, GTIN, images, warranty. Supports create/update/delete.

**Dependencies**: BLING_API_TOKEN (env) OR bling_credentials (DB). Requires valid OAuth token.

**Strengths**:
- Comprehensive field mapping (18+ fields)
- Explicit exclusion: does NOT sync `preco_b2c` (site-only margin price)
- Full audit logging to `bling_sync_log`
- Dimension parsing from string format ("10.0cm x 5.0cm x 15.0cm")
- Weight parsing with unit detection (g/kg)

**Failure modes**:
- Token expiry: Bling tokens last 6h. If expired, all syncs fail silently until manual refresh
- No automatic token refresh logic in the function itself
- Bling API v3 rate limits not documented in code

**Risk**: MEDIUM -- works perfectly when token is valid, fails completely when expired

### 8. sync-all-products-bling (184 lines) -- CONDITIONAL

**What it does**: Batch sync by calling `sync-bling-product` for each product. Filters: pending/error/all.

**Dependencies**: Service-role only. Calls sync-bling-product internally.

**Failure modes**:
- Cascading failure: if Bling token is expired, every single product call fails
- Max 100 products per batch (hardcoded limit)

**Risk**: MEDIUM -- same token dependency

### 9. bling-oauth-callback (192 lines) -- HEALTHY

**What it does**: GET: exchanges authorization code for tokens. POST: refreshes tokens. Stores in `bling_credentials`.

**Critical design**: Bling refresh tokens are SINGLE-USE. Code handles this correctly -- stores new refresh token immediately after refresh.

**Failure modes**:
- DELETE-then-INSERT instead of UPSERT -- brief window where no credentials exist
- No error recovery if insert fails after delete (tokens lost)

**Risk**: LOW (but see token cron gap below)

### 10. bling-webhook (155 lines) -- PARTIALLY HEALTHY

**What it does**: Handles 4 Bling event types:
- `estoques.alteracao`: Stock update -> Supabase quantity
- `produtos.alteracao`: Product update -> Supabase quantity + status
- `produtos.excluidos`: Product delete -> archive in Supabase
- `produtos.incluidos`: Log only (no auto-create)

**Security**: WEAK
- Webhook secret validation is OPTIONAL and soft: warns but does NOT reject
- Any HTTP POST to the endpoint will be accepted

**Failure modes**:
- Stock update updates both `quantity` AND `stock` columns (redundant? legacy?)
- Does NOT propagate Bling stock changes to Shopify -- **DESYNC RISK**
- Product update maps Bling status ("Ativo"/"Inativo"/"Excluido") to Supabase status but Supabase uses different values ("published"/"draft"/"archived")

**Risk**: MEDIUM -- weak auth + no cross-channel propagation

### 11. meli-oauth-callback (190 lines) -- HEALTHY but LONELY

**What it does**: GET: OAuth code exchange. POST: token refresh. Stores in `meli_credentials`. Fetches seller nickname.

**Current state**: OAuth flow works. Tokens are stored. But ZERO functions consume them. No product listing, no order sync, no stock sync.

**Risk**: LOW (it works) but HIGH (it does nothing useful beyond auth)

### 12. product-sync-webhook (167 lines) -- HEALTHY with SCOPE LIMITATION

**What it does**: Supabase DB webhook trigger on products table INSERT/UPDATE. Auto-calls `sync-shopify-product` when relevant fields change and `shopify_sync_enabled=true`.

**Scope limitation**: Only triggers Shopify sync. Does NOT trigger Bling sync or ML sync.

**Failure modes**:
- No debouncing -- rapid edits trigger multiple sync calls
- Only checks 7 field changes (name, price, description, long_description, quantity, status, images)

**Risk**: LOW

### 13. webhook-manager (352 lines) -- HEALTHY

**What it does**: CRUD management for Shopify webhooks. 6 actions: list/setup/delete/clear/test/status. Auto-creates 3 required webhooks pointing to `shopify-webhook-handler`.

**Risk**: LOW -- well-structured management utility

---

## Credential Health Assessment

### SHOPIFY

| Credential | Type | Expiry | Auto-refresh | Risk |
|-----------|------|--------|-------------|------|
| SHOPIFY_ACCESS_TOKEN | Custom App token | Never (permanent) | N/A | LOW |
| SHOPIFY_STOREFRONT_TOKEN | Public token | Never (permanent) | N/A | LOW |
| SHOPIFY_WEBHOOK_SECRET | App secret | Never | N/A | LOW |

Shopify uses permanent custom app tokens. No rotation needed.

### BLING

| Credential | Type | Expiry | Auto-refresh | Risk |
|-----------|------|--------|-------------|------|
| access_token | OAuth2 Bearer | **6 hours** | **NONE -- manual only** | **HIGH** |
| refresh_token | OAuth2 | Single-use | Via POST to bling-oauth-callback | **HIGH** |

**Critical**: Bling tokens expire every 6 hours. There is NO automated cron to refresh them. The only refresh path is:
1. Manual POST to `bling-oauth-callback` from `Integracoes.tsx` UI
2. After 6h, all Bling sync fails silently until admin manually refreshes

### MERCADO LIVRE

| Credential | Type | Expiry | Auto-refresh | Risk |
|-----------|------|--------|-------------|------|
| access_token | OAuth2 Bearer | **6 hours** | **NONE -- manual only** | **MEDIUM** |
| refresh_token | OAuth2 | 6 months | Via POST to meli-oauth-callback | LOW |

ML refresh tokens last 6 months (much better than Bling). But access tokens still expire every 6h with no cron.

---

## Webhook Coverage Analysis

### Shopify Webhooks (via webhook-manager)

| Topic | Handled | Handler behavior |
|-------|---------|-----------------|
| `products/update` | YES | Updates name, description, price, variant IDs in Supabase |
| `inventory_levels/update` | YES | Updates quantity in Supabase |
| `orders/create` | YES | Decrements Supabase stock per line item |
| `orders/fulfilled` | NO | Not handled -- no fulfillment tracking |
| `orders/cancelled` | NO | Not handled -- stock NOT restored on cancellation |
| `refunds/create` | NO | Not handled -- stock NOT restored on refund |
| `products/create` | NO | Not handled -- new Shopify products not imported |
| `products/delete` | NO | Not handled -- deleted products remain in Supabase |

### Bling Webhooks

| Event | Handled | Handler behavior |
|-------|---------|-----------------|
| `estoques.alteracao` | YES | Updates quantity + stock in Supabase |
| `produtos.alteracao` | YES | Updates quantity + status in Supabase |
| `produtos.excluidos` | YES | Archives product in Supabase |
| `produtos.incluidos` | LOGGED | Logs only, no auto-import |
| `vendas.*` | NO | No order events handled |
| `nfe.*` | NO | No fiscal note events handled |

### Mercado Livre Webhooks

| Event | Handled | Handler behavior |
|-------|---------|-----------------|
| ALL | **NO** | No ML webhook handler exists |

---

## Race Condition Analysis: Where Can Overselling Happen?

### Scenario 1: Simultaneous Shopify + ML Sale (CRITICAL)

```
T0: Supabase stock = 1
T1: Customer A buys on Shopify (stock -> 0 in Supabase via webhook)
T2: Customer B buys on Mercado Livre (ML doesn't know stock is 0)
T3: Both orders confirmed -- 1 item, 2 buyers
```

**Why it happens**: ML has no stock sync. ML listings show stale stock.
**Fix needed**: Cross-channel inventory reconciliation.

### Scenario 2: Simultaneous Shopify + Bling Stock Update

```
T0: Supabase stock = 10
T1: Bling receives physical stock adjustment (stock -> 15 via webhook)
T2: Shopify sale happens (stock -> 9 via webhook, based on stale T0 value)
T3: Supabase stock = 9 (lost the Bling update)
```

**Why it happens**: Both webhooks update `quantity` with absolute values, not deltas. Last-write-wins.
**Fix needed**: Delta-based stock adjustments or optimistic locking with version column.

### Scenario 3: Duplicate Webhook Processing

```
T0: Shopify sends orders/create webhook
T1: Handler decrements stock (quantity 10 -> 9)
T2: Shopify retries (network timeout on T0 response)
T3: Handler decrements again (quantity 9 -> 8) -- WRONG
```

**Why it happens**: No idempotency key (e.g., order ID deduplication).
**Fix needed**: Check if order was already processed before decrementing.

### Scenario 4: Token Expiry During Batch Sync

```
T0: sync-all-products-bling starts (50 products)
T1: Products 1-30 sync successfully
T2: Bling token expires mid-batch
T3: Products 31-50 all fail -- marked as "error" but token issue, not product issue
```

**Why it happens**: No token validation before batch, no mid-batch refresh.
**Fix needed**: Token health check before batch, or catch 401 and auto-refresh.

---

## Cross-Channel Propagation Matrix

| Event | Supabase | Shopify | Bling | ML |
|-------|----------|---------|-------|----|
| Product created in Supabase | -- | Auto (if sync_enabled) | Manual (batch or per-product) | NOT SYNCED |
| Product edited in Supabase | -- | Auto (if sync_enabled) | NOT auto | NOT SYNCED |
| Stock changed in Supabase | -- | Auto (if sync_enabled) | NOT auto | NOT SYNCED |
| Shopify product updated | webhook -> DB | -- | NOT propagated | NOT SYNCED |
| Shopify stock changed | webhook -> DB | -- | NOT propagated | NOT SYNCED |
| Shopify order placed | webhook -> DB decrement | -- | NOT propagated | NOT SYNCED |
| Bling stock changed | webhook -> DB | NOT propagated | -- | NOT SYNCED |
| Bling product updated | webhook -> DB | NOT propagated | -- | NOT SYNCED |
| ML order placed | NOT HANDLED | NOT HANDLED | NOT HANDLED | -- |

**Key insight**: Changes propagate INTO Supabase but NOT OUT to other channels. The only automatic outbound sync is Supabase -> Shopify via the DB webhook trigger (`product-sync-webhook`).

---

## Shared Code Analysis

### `_shared/cors.ts`
- CORS helper for edge function responses
- Used by all Shopify and Bling functions

### `_shared/validation.ts`
- `validateShopifyHmac(rawBody, hmac, secret)`: HMAC-SHA256 validation
- `isValidShopDomain(domain)`: Validates against expected `gatoaocubo.myshopify.com`
- `EXPECTED_SHOP_DOMAIN`: Constant for domain validation
- Used only by `shopify-webhook-handler`

---

## Health Score

| Component | Score | Notes |
|-----------|-------|-------|
| Shopify Admin API sync | 9/10 | Complete bidirectional, good error handling |
| Shopify Storefront checkout | 8/10 | Works well, minor stock validation gap |
| Shopify webhooks | 7/10 | 3 topics handled but no order cancel/refund |
| Bling product sync | 7/10 | Comprehensive fields but token fragility |
| Bling webhooks | 5/10 | Soft auth, no cross-channel propagation |
| Bling token management | 3/10 | Manual refresh only, 6h expiry |
| ML integration | 1/10 | OAuth only, zero product sync |
| Cross-channel inventory | 0/10 | Does not exist |
| Overselling prevention | 0/10 | No atomic cross-channel locks |

**Overall ecosystem health: 4.4/10** -- Shopify is solid, everything else needs work.
