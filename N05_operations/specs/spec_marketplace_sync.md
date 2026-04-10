---
id: spec_marketplace_sync
kind: e2e_eval
title: "MARKETPLACE_SYNC Spec -- Cross-Channel Inventory & ML Integration"
version: 1.0.0
quality: null
pillar: P07
tags: [spec, marketplace, sync, mercado-livre, inventory, overselling, cron, webhook]
nucleus: N05
created: 2026-04-10
---

# MARKETPLACE_SYNC Spec

## Mission Purpose

Build the missing pieces to make GATO3 a true multi-channel commerce operation:
1. Mercado Livre product listing sync
2. Cross-channel inventory reconciliation
3. Automated token refresh
4. Order webhook chain across all channels

## Current State (from audit)

| Channel | Product Sync | Stock Sync | Order Sync | Token Refresh |
|---------|-------------|------------|------------|---------------|
| Shopify | Bidirectional | Bidirectional | Webhook (partial) | N/A (permanent token) |
| Bling | Supabase->Bling | Bling->Supabase (webhook) | None | Manual (6h TTL) |
| ML | **None** | **None** | **None** | Manual (6h TTL) |

## Target State

| Channel | Product Sync | Stock Sync | Order Sync | Token Refresh |
|---------|-------------|------------|------------|---------------|
| Shopify | Bidirectional | Bidirectional | Full (incl. cancel/refund) | N/A |
| Bling | Bidirectional | Bidirectional + propagate | Order->NF-e trigger | Auto cron (4h) |
| ML | Supabase->ML | Supabase->ML + ML->Supabase | ML order->Supabase | Auto cron (4h) |

---

## Wave 1: Overselling Prevention (P0 -- Revenue Risk)

### 1.1 Inventory Reconciliation Function

**New edge function**: `inventory-reconcile`

```
Purpose: After any stock change event, propagate the new quantity to ALL channels
Trigger: Called by shopify-webhook-handler, bling-webhook, and future meli-webhook

Flow:
1. Receive { productId, newQuantity, source: "shopify" | "bling" | "supabase" }
2. Update Supabase products.quantity = newQuantity
3. For each OTHER channel (not the source):
   a. If shopify_product_id exists -> update Shopify inventory via Admin API
   b. If bling_product_id exists -> update Bling stock via API v3
   c. If meli_item_id exists -> update ML stock via Items API
4. Log reconciliation to new reconciliation_log table
```

**Key design decisions**:
- Source channel is excluded from propagation (avoid echo loops)
- Uses Supabase as single source of truth
- Rate limited per channel (Shopify 500ms, Bling 500ms, ML 1s)

### 1.2 Idempotent Order Processing

**Modify**: `shopify-webhook-handler` orders/create handler

```
Before decrementing stock:
1. Check shopify_order_log for order_id (new table)
2. If exists -> skip (already processed)
3. If not -> process + insert order_id
4. After decrementing Supabase -> call inventory-reconcile
```

**New table**: `order_processing_log`
```sql
CREATE TABLE order_processing_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id VARCHAR(100) NOT NULL,
  channel VARCHAR(20) NOT NULL, -- shopify, bling, meli
  event_type VARCHAR(50) NOT NULL, -- orders/create, orders/cancel
  processed_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(order_id, channel, event_type)
);
```

### 1.3 Order Cancellation/Refund Handlers

**Modify**: `shopify-webhook-handler` to handle:
- `orders/cancelled`: Restore stock in Supabase + propagate via inventory-reconcile
- `refunds/create`: Restore stock for refunded line items

**Add to webhook-manager REQUIRED_WEBHOOKS**:
```typescript
{ topic: 'orders/cancelled', format: 'json' },
{ topic: 'refunds/create', format: 'json' },
```

---

## Wave 2: Token Auto-Refresh (P2 -- Operational Risk)

### 2.1 Token Refresh Cron Function

**New edge function**: `token-refresh-cron`

```
Purpose: Auto-refresh Bling and ML tokens before they expire
Schedule: Every 4 hours via pg_cron or Supabase scheduled function
Method: Supabase pg_cron -> HTTP POST to edge functions

Flow:
1. Query bling_credentials.expires_at
   - If expires in < 2 hours -> POST to bling-oauth-callback (refresh)
   - If refresh fails -> log error, send alert via Supabase webhook
2. Query meli_credentials.expires_at
   - If expires in < 2 hours -> POST to meli-oauth-callback (refresh)
   - If refresh fails -> log error

Alert mechanism: Insert into new token_alerts table, read from Integracoes.tsx
```

### 2.2 pg_cron Setup

```sql
-- Enable pg_cron extension (Supabase Pro plan required)
CREATE EXTENSION IF NOT EXISTS pg_cron;

-- Schedule token refresh every 4 hours
SELECT cron.schedule(
  'refresh-marketplace-tokens',
  '0 */4 * * *',
  $$
  SELECT net.http_post(
    url := current_setting('app.settings.supabase_url') || '/functions/v1/token-refresh-cron',
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || current_setting('app.settings.service_role_key'),
      'Content-Type', 'application/json'
    ),
    body := '{}'::jsonb
  );
  $$
);
```

### 2.3 Token Health Check in Integracoes.tsx

**Modify**: `Integracoes.tsx` to show:
- Last auto-refresh timestamp
- Next scheduled refresh
- Alert banner if refresh has been failing

---

## Wave 3: Mercado Livre Product Sync (P1 -- Revenue Opportunity)

### 3.1 ML Product Listing Function

**New edge function**: `sync-meli-product`

```
Purpose: Create or update ML listing from Supabase product
API: ML Items API (POST /items, PUT /items/{id})

Flow:
1. Receive { productId }
2. Load product from Supabase
3. Load ML credentials from meli_credentials
4. If meli_item_id is null -> CREATE listing
   - Map Supabase fields to ML Item schema
   - POST https://api.mercadolibre.com/items
   - Store returned item_id in products.meli_item_id
5. If meli_item_id exists -> UPDATE listing
   - PUT https://api.mercadolibre.com/items/{meli_item_id}
   - Update title, price, available_quantity, description

Field mapping:
| Supabase | ML Items API |
|----------|-------------|
| name | title (max 60 chars) |
| price | price (or preco_b2c if set) |
| quantity | available_quantity |
| description | plain text description |
| images[0..9] | pictures[].source |
| "MLB" | site_id |
| category_id | listing_type_id = "gold_special" |
```

### 3.2 ML Batch Sync Function

**New edge function**: `sync-all-products-meli`

```
Purpose: Batch sync all published products to ML
Similar to sync-all-products-bling pattern
Filters: pending, error, all
Service-role only
```

### 3.3 ML Webhook Handler

**New edge function**: `meli-webhook-handler`

```
Purpose: Handle ML notifications
ML notification types:
- orders_v2: New order -> decrement stock + call inventory-reconcile
- items: Item status change -> update Supabase
- questions: New question -> insert into meli_questions table (future CRM)

Webhook setup:
POST https://api.mercadolibre.com/applications/{APP_ID}/webhooks
{
  "callback_url": "https://fuuguegkqnpzrrhwymgw.supabase.co/functions/v1/meli-webhook-handler",
  "topic": "orders_v2"
}
```

### 3.4 ML Webhook Manager

**New edge function**: `meli-webhook-manager`

```
Same pattern as webhook-manager but for ML:
- list: GET notification topics
- setup: register order + item webhooks
- status: verify configuration
```

---

## Wave 4: Bidirectional Sync Cron (P3 -- Consistency)

### 4.1 Scheduled Bidirectional Sync

**New edge function**: `scheduled-sync`

```
Purpose: Periodic full reconciliation across all channels
Schedule: Every 15 minutes via pg_cron

Flow:
1. Run unified-sync bidirectional (Shopify <-> Supabase)
2. Run sync-all-products-bling filter=all (Supabase -> Bling)
3. Run sync-all-products-meli filter=all (Supabase -> ML)
4. Compare quantities across channels
5. If mismatch detected -> use Supabase as truth, propagate
6. Log sync summary to sync_reconciliation_log
```

### 4.2 pg_cron for Bidirectional Sync

```sql
SELECT cron.schedule(
  'bidirectional-product-sync',
  '*/15 * * * *',
  $$
  SELECT net.http_post(
    url := current_setting('app.settings.supabase_url') || '/functions/v1/scheduled-sync',
    headers := jsonb_build_object(
      'Authorization', 'Bearer ' || current_setting('app.settings.service_role_key'),
      'Content-Type', 'application/json'
    ),
    body := '{"scope": "inventory"}'::jsonb
  );
  $$
);
```

---

## New Database Tables Required

```sql
-- 1. Order processing idempotency
CREATE TABLE order_processing_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id VARCHAR(100) NOT NULL,
  channel VARCHAR(20) NOT NULL,
  event_type VARCHAR(50) NOT NULL,
  line_items JSONB,
  processed_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(order_id, channel, event_type)
);

-- 2. Inventory reconciliation audit
CREATE TABLE inventory_reconciliation_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id UUID REFERENCES products(id),
  source_channel VARCHAR(20) NOT NULL,
  old_quantity INTEGER,
  new_quantity INTEGER,
  channels_updated JSONB, -- {"shopify": true, "bling": true, "meli": false}
  errors JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Token health alerts
CREATE TABLE token_alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  provider VARCHAR(20) NOT NULL, -- bling, meli
  alert_type VARCHAR(50) NOT NULL, -- refresh_failed, expired, refresh_success
  message TEXT,
  resolved BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. ML sync log (mirror bling_sync_log)
CREATE TABLE meli_sync_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id UUID REFERENCES products(id),
  meli_item_id VARCHAR(20),
  operation VARCHAR(50) NOT NULL,
  direction VARCHAR(30) NOT NULL,
  request_payload JSONB,
  response_payload JSONB,
  status VARCHAR(20) NOT NULL,
  error_message TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## New Edge Functions Summary

| Function | Wave | Lines (est.) | Purpose |
|----------|------|-------------|---------|
| `inventory-reconcile` | 1 | ~200 | Cross-channel stock propagation |
| `token-refresh-cron` | 2 | ~150 | Auto-refresh Bling + ML tokens |
| `sync-meli-product` | 3 | ~300 | ML product listing create/update |
| `sync-all-products-meli` | 3 | ~180 | ML batch sync |
| `meli-webhook-handler` | 3 | ~200 | ML order/item notifications |
| `meli-webhook-manager` | 3 | ~250 | ML webhook CRUD |
| `scheduled-sync` | 4 | ~150 | Periodic full reconciliation |

**Total new code**: ~1,430 lines across 7 functions + 4 new DB tables + 2 cron jobs.

---

## Modified Existing Functions

| Function | Change | Wave |
|----------|--------|------|
| `shopify-webhook-handler` | Add idempotency, order cancel/refund, call inventory-reconcile | 1 |
| `bling-webhook` | Harden auth (reject invalid secret), call inventory-reconcile | 1 |
| `product-sync-webhook` | Add Bling + ML trigger alongside Shopify | 3 |
| `webhook-manager` | Add orders/cancelled + refunds/create to REQUIRED_WEBHOOKS | 1 |

---

## Priority Fix List (ordered by revenue risk)

### P0: Overselling Prevention (Wave 1)
- **Risk**: Customer buys last item on Shopify + ML simultaneously = 2 orders, 1 item
- **Fix**: `inventory-reconcile` function + idempotent order processing
- **Effort**: 2-3 days
- **Revenue impact**: Direct loss on every oversold order (refund + reputation)

### P1: ML Product Sync (Wave 3)
- **Risk**: ML is a revenue channel with zero product automation
- **Fix**: `sync-meli-product` + `meli-webhook-handler`
- **Effort**: 3-4 days
- **Revenue impact**: Currently manual listing management = missed sales + stale prices

### P2: Auto Token Refresh (Wave 2)
- **Risk**: Bling + ML tokens expire every 6h with no cron
- **Fix**: `token-refresh-cron` + pg_cron schedule
- **Effort**: 1 day
- **Revenue impact**: Silent sync failure = stale stock = overselling OR lost sales

### P3: Order Webhook Chain (Waves 1+3)
- **Risk**: Shopify orders don't update Bling stock. ML orders don't exist.
- **Fix**: Modify shopify-webhook-handler + new meli-webhook-handler
- **Effort**: 2-3 days
- **Revenue impact**: Stock desync across channels compounds over time

### P4: Scheduled Reconciliation (Wave 4)
- **Risk**: Webhook failures or missed events cause gradual stock drift
- **Fix**: `scheduled-sync` + pg_cron every 15 minutes
- **Effort**: 1-2 days
- **Revenue impact**: Safety net -- catches what webhooks miss

---

## Implementation Order

```
Week 1: Wave 1 (P0) -- Overselling prevention
  Day 1-2: inventory-reconcile function
  Day 2-3: Modify shopify-webhook-handler (idempotency + cancel/refund)
  Day 3:   Modify bling-webhook (hard auth + propagation)
  Day 3:   DB migrations (order_processing_log, inventory_reconciliation_log)

Week 1: Wave 2 (P2) -- Token refresh
  Day 4:   token-refresh-cron function
  Day 4:   pg_cron setup + token_alerts table
  Day 4:   Integracoes.tsx health display update

Week 2: Wave 3 (P1) -- ML integration
  Day 5-6: sync-meli-product + sync-all-products-meli
  Day 7-8: meli-webhook-handler + meli-webhook-manager
  Day 8:   DB migrations (meli_sync_log)
  Day 8:   Modify product-sync-webhook (add ML trigger)

Week 2: Wave 4 (P3) -- Scheduled sync
  Day 9:   scheduled-sync function
  Day 9:   pg_cron setup (15min interval)
  Day 10:  Integration testing across all channels
```

---

## Success Criteria

| Metric | Current | Target |
|--------|---------|--------|
| Channels with product sync | 2 (Shopify, Bling) | 3 (+ML) |
| Channels with stock propagation | 0 | 3 |
| Token refresh automation | Manual | Auto (4h cron) |
| Overselling protection | None | Idempotent + cross-channel |
| Stock reconciliation frequency | Never | Every 15 min |
| Order -> stock update channels | 1 (Shopify->Supabase) | 3 (all channels) |
