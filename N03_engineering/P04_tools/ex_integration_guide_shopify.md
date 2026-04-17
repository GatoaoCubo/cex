---
id: ex_integration_guide_shopify
kind: integration_guide
pillar: P04
title: Shopify Integration Guide
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
  - BRAND_SHOPIFY_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, shopify, integration]
---

## Purpose

Step-by-step integration guide for connecting a {{BRAND_SHOPIFY_DOMAIN}} Shopify store to a Supabase backend, enabling bidirectional product sync, webhook-driven inventory updates, and OAuth-authenticated admin operations.

## When to Use

- Setting up a new Shopify + Supabase commerce stack from scratch.
- Adding Shopify sync to an existing Supabase-backed product catalog.
- Migrating from a custom shop to Shopify while preserving internal product data.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| Shopify plan | Basic or above (Partner dev store OK) |
| Shopify Admin API version | `{{BRAND_SHOPIFY_API_VERSION}}` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |
| Edge runtime | Supabase Edge Functions (Deno) |
| Auth token scope | `read_products`, `write_products`, `read_inventory`, `write_inventory` |

## Architecture

```
Shopify Admin API
      |
      |-- REST / GraphQL ---------> edge function: fetch-from-shopify
      |                             edge function: push-titles-to-shopify
      |
      |-- Webhooks (HMAC-SHA256) -> edge function: shopify-webhook-handler
      |
Supabase DB (products table)
      |
      |-- DB Webhook ------------> edge function: product-sync-webhook
      |
Internal services
```

## Integration Steps

### Step 1 — Create a Custom App in Shopify

1. Navigate to `https://{{BRAND_SHOPIFY_DOMAIN}}/admin/apps/development`.
2. Click **Create an app** → name it (e.g., `{{BRAND_NAME}} Sync`).
3. Configure scopes: `read_products`, `write_products`, `read_inventory`, `write_inventory`.
4. Install the app. Copy the **Admin API access token**.
5. Store the token in Supabase secrets: `SHOPIFY_ADMIN_TOKEN`.

### Step 2 — Configure Webhook Subscriptions

```bash
# Register product update webhook
curl -X POST \
  https://{{BRAND_SHOPIFY_DOMAIN}}/admin/api/{{BRAND_SHOPIFY_API_VERSION}}/webhooks.json \
  -H "X-Shopify-Access-Token: $SHOPIFY_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "webhook": {
      "topic": "products/update",
      "address": "https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/shopify-webhook-handler",
      "format": "json"
    }
  }'
```

Repeat for: `products/create`, `products/delete`, `inventory_levels/update`.

Webhook secret is set in Supabase edge secrets as `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}`.

### Step 3 — Deploy Edge Functions

```bash
supabase functions deploy shopify-webhook-handler
supabase functions deploy fetch-from-shopify
supabase functions deploy push-titles-to-shopify
supabase functions deploy product-sync-webhook
```

Set secrets:

```bash
supabase secrets set SHOPIFY_STORE_DOMAIN={{BRAND_SHOPIFY_DOMAIN}}
supabase secrets set SHOPIFY_API_VERSION={{BRAND_SHOPIFY_API_VERSION}}
supabase secrets set SHOPIFY_WEBHOOK_SECRET={{BRAND_SHOPIFY_WEBHOOK_SECRET}}
```

### Step 4 — Initial Product Pull

Invoke `fetch-from-shopify` to seed the Supabase `products` table:

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/fetch-from-shopify \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY"
```

Expected: products upserted with `shopify_id`, `shopify_synced_at` populated.

### Step 5 — Enable DB Webhook (Supabase → Shopify push)

In Supabase Dashboard → Database → Webhooks, create a webhook on `products` table INSERT/UPDATE events pointing to `product-sync-webhook`.

### Step 6 — Verify Bidirectional Sync

1. Update a product title in Shopify Admin.
2. Confirm the Supabase `products` row reflects the change within 30 seconds.
3. Update a product title in Supabase.
4. Confirm the Shopify product is updated within 30 seconds.

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `SHOPIFY_STORE_DOMAIN` | env secret | e.g., `{{BRAND_SHOPIFY_DOMAIN}}` |
| `SHOPIFY_API_VERSION` | env secret | e.g., `2024-01` |
| `SHOPIFY_ADMIN_TOKEN` | env secret | Admin API access token |
| `SHOPIFY_WEBHOOK_SECRET` | env secret | HMAC signature secret |

| Output | Description |
|--------|-------------|
| Supabase `products` rows | Synced from Shopify |
| Shopify products | Updated from Supabase |
| Edge function logs | Visible in Supabase Dashboard |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Your store's myshopify.com domain |
| `{{BRAND_SHOPIFY_API_VERSION}}` | Admin API version (e.g., `2024-01`) |
| `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` | HMAC secret for webhook validation |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference ID |
| `{{BRAND_NAME}}` | Brand name for app display name |

## Example Usage

```typescript
// fetch-from-shopify edge function (excerpt)
const response = await fetch(
  `https://${Deno.env.get('SHOPIFY_STORE_DOMAIN')}/admin/api/${Deno.env.get('SHOPIFY_API_VERSION')}/products.json?limit=250`,
  { headers: { 'X-Shopify-Access-Token': Deno.env.get('SHOPIFY_ADMIN_TOKEN')! } }
);
const { products } = await response.json();
// upsert into Supabase products table...
```

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_api_client_shopify.md` | api_client | HTTP client spec for Shopify Admin API |
| `ex_webhook_shopify.md` | webhook | Webhook handler spec |
| `ex_oauth_app_config_shopify.md` | oauth_app_config | OAuth app configuration |
| `ex_supabase_data_layer.md` | supabase_data_layer | Supabase backend setup |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Bidirectional sync orchestration |
