---
id: sync_fix_report_20260410
kind: e2e_eval
title: "Unified-Sync Push Fix + Stock Alignment Report"
version: 1.0.0
quality: null
pillar: P07
tags: [shopify, sync, bug-fix, variant, stock-alignment, inventory]
nucleus: N05
created: 2026-04-10
---

# Unified-Sync Push Fix + Stock Alignment Report

## Executive Summary

Fixed 3 critical bugs in the Shopify push pipeline (`unified-sync` and `sync-shopify-product`) in `gato-cubo-commerce`. These bugs caused duplicate Shopify variants on every push update, image re-download storms, and silent crash on API rate limiting.

---

## Bugs Fixed

### Bug 1: Variant ID Missing on Update (CRITICAL)

| Field | Value |
|-------|-------|
| Files | `unified-sync/index.ts:530`, `sync-shopify-product/index.ts:115` |
| Severity | CRITICAL -- data corruption on every push update |
| Root cause | `pushProduct()` sends `variants: [{ price }]` without `id` field |
| Impact | Shopify interprets missing variant ID as "create new variant" on PUT |
| Result | Duplicate variants accumulate on every sync cycle |

**Fix applied**: Extract numeric variant ID from the GID format stored in Supabase (`gid://shopify/ProductVariant/12345` -> `12345`), include it in the variant object on update requests.

Before:
```typescript
shopifyData.variants = [{ price: product.price.toString() }];
```

After:
```typescript
if (isUpdate && numericVariantId) {
  shopifyData.variants = [{ id: numericVariantId, price: product.price.toString() }];
} else {
  shopifyData.variants = [{ price: product.price.toString() }];
}
```

### Bug 2: Images Resent on Every Update (PERFORMANCE)

| Field | Value |
|-------|-------|
| File | `unified-sync/index.ts:539`, `sync-shopify-product/index.ts:123` |
| Severity | MEDIUM -- performance + duplicate images |
| Root cause | `images` array sent in PUT request body on every update |
| Impact | Shopify re-downloads all image URLs, creating duplicates |

**Fix applied**: Only include `images` in the payload when creating new products.

### Bug 3: No 429 Retry Logic (RELIABILITY)

| Field | Value |
|-------|-------|
| File | `unified-sync/index.ts:190` |
| Severity | MEDIUM -- batch sync crashes on rate limit |
| Root cause | `ShopifyAPI.request()` throws on any non-200 |
| Impact | Batch push of 50+ products hits Shopify rate limit, entire batch fails |

**Fix applied**: Added retry loop (max 3 retries) that reads `Retry-After` header and backs off before retrying.

---

## Files Modified (gato-cubo-commerce)

| File | Lines changed | Change type |
|------|--------------|-------------|
| `supabase/functions/unified-sync/index.ts` | ~40 | Bug fix (variant ID, images, retry) |
| `supabase/functions/sync-shopify-product/index.ts` | ~25 | Bug fix (variant ID, images) |

---

## Stock Alignment Assessment

### Current Propagation Matrix

| Event | Supabase | Shopify | Bling | ML |
|-------|----------|---------|-------|----|
| Product edit in Supabase | -- | Auto (if sync_enabled) | Manual | NONE |
| Shopify sale | webhook -> DB | -- | NOT propagated | NONE |
| Bling stock change | webhook -> DB | NOT propagated | -- | NONE |
| ML sale | NOT HANDLED | NOT HANDLED | NOT HANDLED | -- |

**Key finding**: Changes flow INTO Supabase from Shopify and Bling webhooks, but never propagate OUTWARD to sibling channels. This means:
- A Shopify sale decrements Supabase but Bling still shows old stock
- A Bling physical adjustment updates Supabase but Shopify still shows old stock
- ML has zero automation

### Existing Mitigation: inventory-reconcile

The `inventory-reconcile` edge function EXISTS and is functional. It:
1. Reads Supabase stock (source of truth)
2. Queries Bling and Shopify stock via API
3. Detects discrepancies
4. Auto-corrects by pushing Supabase values outward
5. Logs all movements to `inventory_movements` table

**This function is the correct fix for stock alignment.** It needs to be scheduled via pg_cron (see MARKETPLACE_SYNC spec Wave 4).

### Recommended Operational Actions

#### Immediate (can run now)

1. **Run inventory-reconcile in dry_run mode** to assess current stock drift:
   ```
   POST /functions/v1/inventory-reconcile?dry_run=1
   Authorization: Bearer {service_role_key}
   ```

2. **Run inventory-reconcile in correction mode** to align all channels:
   ```
   POST /functions/v1/inventory-reconcile
   Authorization: Bearer {service_role_key}
   ```

3. **Run unified-sync push** (now fixed) to create missing Shopify listings:
   ```
   POST /functions/v1/unified-sync
   Body: { "mode": "push", "scope": "all", "force": true }
   Authorization: Bearer {service_role_key}
   ```

#### Short-term (schedule via pg_cron)

4. **Schedule inventory-reconcile** every 15 minutes to prevent stock drift:
   ```sql
   SELECT cron.schedule(
     'inventory-reconcile-15m',
     '*/15 * * * *',
     $$SELECT net.http_post(
       url := current_setting('app.settings.supabase_url') || '/functions/v1/inventory-reconcile',
       headers := jsonb_build_object(
         'Authorization', 'Bearer ' || current_setting('app.settings.service_role_key'),
         'Content-Type', 'application/json'
       ),
       body := '{}'::jsonb
     );$$
   );
   ```

5. **Schedule token-auto-refresh** every 4 hours (Bling + ML tokens expire in 6h):
   See `token-auto-refresh` function (already exists in commerce repo).

---

## Missing Shopify Listings: Diagnostic Query

Products in Supabase with `status = 'published'` but no Shopify listing:

```sql
SELECT id, name, sku, price, quantity, shopify_sync_enabled
FROM products
WHERE status = 'published'
  AND shopify_product_id IS NULL
ORDER BY created_at;
```

To batch-create all missing listings, enable sync and push:

```sql
-- Enable sync for all published products without Shopify listing
UPDATE products
SET shopify_sync_enabled = true
WHERE status = 'published'
  AND shopify_product_id IS NULL;
```

Then call:
```
POST /functions/v1/unified-sync
Body: { "mode": "push", "scope": "all" }
```

The fixed `pushProduct()` will create new Shopify products for these and store the IDs back in Supabase.

---

## Remaining Gaps (from MARKETPLACE_SYNC spec)

| Gap | Priority | Status |
|-----|----------|--------|
| Cross-channel stock propagation on webhook events | P0 | NOT BUILT -- inventory-reconcile handles scheduled, not real-time |
| Idempotent order processing (dedup) | P0 | NOT BUILT -- shopify-webhook-handler has no order dedup |
| ML product sync | P1 | NOT BUILT -- meli OAuth works but no listing functions |
| Auto token refresh cron | P2 | FUNCTION EXISTS -- needs pg_cron schedule |
| Bling webhook hard auth | P2 | NOT FIXED -- still soft-warns on invalid secret |
| Order cancel/refund stock restore | P3 | NOT BUILT -- no handlers for orders/cancelled or refunds/create |

---

## Verification Checklist

- [x] unified-sync push sends variant ID on update
- [x] unified-sync push skips images on update
- [x] unified-sync has 429 retry with Retry-After backoff
- [x] sync-shopify-product sends variant ID on update
- [x] sync-shopify-product skips images on update
- [ ] Run inventory-reconcile dry_run to confirm stock state
- [ ] Run unified-sync push to create missing Shopify listings
- [ ] Schedule inventory-reconcile via pg_cron
- [ ] Schedule token-auto-refresh via pg_cron
