---
id: ex-webhook-manager
kind: webhook
pillar: P04
title: Shopify Webhook Manager
version: 0.1.0
quality: 9.1
status: template
brand_placeholders:
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
  - BRAND_SUPABASE_PROJECT_REF
  - BRAND_SHOPIFY_WEBHOOK_SECRET
tags: [commerce, template, distillation, shopify, webhook, management]
density_score: 0.98
---

# Shopify Webhook Manager

## Purpose
CRUD operations for Shopify webhook subscriptions: list, setup (create the required topic set), delete, clear-all, test-fire, and rotate-secret. Ensures the brand's Shopify store always has exactly the webhook set the integration expects -- no gaps, no strays.

## When to use
- First-time setup (see `ex_integration_guide_shopify.md`).
- After rotating `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` -- must re-register all webhooks.
- Audit run to detect drift (manual admin UI changes created stray webhooks).

## Interface
```
POST /webhook-manager
  { op: "list" | "setup" | "delete" | "clear" | "test" | "rotate_secret",
    topic?: string,   // for delete
    webhook_id?: string, // for delete/test
  }
```
Returns `{ before: [...], after: [...], diff: {added, removed} }`.

## Brand variables used
- `{{BRAND_SHOPIFY_STORE_DOMAIN}}` -- target store.
- `{{BRAND_SHOPIFY_API_VERSION}}` -- pinned API version.
- `{{BRAND_SUPABASE_PROJECT_REF}}` -- callback address for all created webhooks.
- `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` -- HMAC shared secret; rotate via `op: "rotate_secret"`.

## Required topic set
| Topic | Purpose | Callback |
|-------|---------|----------|
| `products/update` | catalog mirror | `/shopify-webhook-handler` |
| `products/delete` | soft-delete mirror | `/shopify-webhook-handler` |
| `inventory_levels/update` | stock mirror | `/shopify-webhook-handler` |
| `orders/create` | order pipeline | `/shopify-webhook-handler` |
| `orders/paid` | fulfillment trigger | `/shopify-webhook-handler` |
| `app/uninstalled` | cleanup | `/shopify-webhook-handler` |

## Operations

### `op: "list"`
`GET https://{{BRAND_SHOPIFY_STORE_DOMAIN}}/admin/api/{{BRAND_SHOPIFY_API_VERSION}}/webhooks.json`; returns full subscription list with `id, topic, address, updated_at`.

### `op: "setup"` (idempotent)
For each topic in the required set:
- If present with correct address -> noop.
- If present with wrong address -> update.
- If absent -> create via `POST /webhooks.json { webhook: {topic, address, format: "json"} }`.

### `op: "delete"`
`DELETE /webhooks/{id}.json`; logs what was removed.

### `op: "clear"`
Deletes ALL webhooks on the store. Use only during decommission. Asks for `confirm: true` flag to avoid accidental triggering.

### `op: "test"`
Shopify doesn't offer a "test fire" endpoint; the manager instead POSTs a synthesized payload directly to the configured callback URL with the current HMAC secret -- verifies the handler is reachable and signature validation works.

### `op: "rotate_secret"`
1. Generate new random secret.
2. Delete all existing webhooks (they are bound to the old secret internally by Shopify).
3. Re-create the full set with the new secret.
4. Update `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` in the secret store.

## Drift detection
Nightly cron runs `op: "list"` and compares to required set; alerts if diff is non-empty. Catches rogue webhooks added via Shopify admin UI.

## Related artifacts
- `ex_webhook_shopify.md` -- handler registered by this manager.
- `ex_integration_guide_shopify.md` -- setup flow.
- `ex_notifier_webhook.md` -- outbound notification companion.
