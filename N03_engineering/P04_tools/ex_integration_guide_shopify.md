---
quality: 9.1
id: ex_integration_guide_shopify
kind: integration_guide
pillar: P04
title: Shopify Integration Guide
version: 0.2.0
quality: 6.8
status: example
author: n03_engineering
created: "2026-04-17"
updated: "2026-04-22"
domain: ecommerce_integration
integration_type: API_Webhook
tldr: "Connects a Shopify store to a Supabase backend for bidirectional product sync, HMAC-verified webhook events, and OAuth-authenticated admin operations."
api_endpoints:
  - GET /admin/api/{version}/products.json
  - PUT /admin/api/{version}/products/{id}.json
  - POST /admin/api/{version}/webhooks.json
  - GET /admin/api/{version}/inventory_levels.json
dependencies:
  - supabase-cli >= 1.0
  - shopify-admin-api
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
  - BRAND_SHOPIFY_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, example, shopify, integration, webhook, supabase]
density_score: 0.88
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p01_kc_supabase_edge_functions
  - p12_wf_supabase_setup
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - bld_manifest_supabase_data_layer
  - p12_mission_supabase_data_layer
  - p12_dispatch_rule_supabase
  - bld_tools_social_publisher
---

## Overview

Connects a Shopify store (`{{BRAND_SHOPIFY_DOMAIN}}`) to a Supabase backend for bidirectional product sync using Shopify Admin REST API, HMAC-SHA256-verified webhooks, and Supabase edge functions.

## When to Use

- Setting up a new Shopify + Supabase commerce stack from scratch.
- Adding Shopify sync to an existing Supabase-backed product catalog.
- Migrating from a custom shop to Shopify while preserving internal product data.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| Shopify plan | Basic or above (Partner dev store OK) |
| Admin API version | `{{BRAND_SHOPIFY_API_VERSION}}` (e.g., `2024-01`) |
| API scopes | `read_products`, `write_products`, `read_inventory`, `write_inventory` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |
| Edge runtime | Supabase Edge Functions (Deno) |

## Architecture

```
Shopify Admin API
  |-- REST / GraphQL -> edge fn: fetch-from-shopify, push-titles-to-shopify
  |-- Webhooks (HMAC-SHA256) -> edge fn: shopify-webhook-handler
Supabase DB: products
  |-- DB Webhook -> edge fn: product-sync-webhook
```

## API Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| `GET` | `/admin/api/{ver}/products.json?limit=250` | List all products (paginated) | X-Shopify-Access-Token |
| `PUT` | `/admin/api/{ver}/products/{id}.json` | Update product fields | X-Shopify-Access-Token |
| `POST` | `/admin/api/{ver}/webhooks.json` | Register webhook subscription | X-Shopify-Access-Token |
| `GET` | `/admin/api/{ver}/inventory_levels.json` | Get inventory levels | X-Shopify-Access-Token |
| `DELETE` | `/admin/api/{ver}/webhooks/{id}.json` | Remove webhook subscription | X-Shopify-Access-Token |

## Integration Steps

### Step 1 -- Create Custom App

1. Go to `https://{{BRAND_SHOPIFY_DOMAIN}}/admin/apps/development`.
2. Click **Create an app** -> name it (e.g., `{{BRAND_NAME}} Sync`).
3. Configure scopes: `read_products`, `write_products`, `read_inventory`, `write_inventory`.
4. Install the app and copy the **Admin API access token**.
5. Store: `supabase secrets set SHOPIFY_ADMIN_TOKEN=<token>`.

### Step 2 -- Register Webhook Subscriptions

```bash
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

Register for: `products/create`, `products/update`, `products/delete`, `inventory_levels/update`.

### Step 3 -- Deploy Edge Functions

```bash
supabase functions deploy shopify-webhook-handler
supabase functions deploy fetch-from-shopify
supabase functions deploy push-titles-to-shopify
supabase functions deploy product-sync-webhook

supabase secrets set SHOPIFY_STORE_DOMAIN={{BRAND_SHOPIFY_DOMAIN}}
supabase secrets set SHOPIFY_API_VERSION={{BRAND_SHOPIFY_API_VERSION}}
supabase secrets set SHOPIFY_WEBHOOK_SECRET={{BRAND_SHOPIFY_WEBHOOK_SECRET}}
```

### Step 4 -- Initial Product Pull

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/fetch-from-shopify \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY"
```

Expected: products upserted with `shopify_id` and `shopify_synced_at` populated.

### Step 5 -- Enable DB Webhook (Supabase -> Shopify push)

In Supabase Dashboard -> Database -> Webhooks: create webhook on `products` table `INSERT/UPDATE` events targeting `product-sync-webhook`.

### Step 6 -- Verify Bidirectional Sync

1. Update a product title in Shopify Admin; confirm Supabase row reflects change within 30s.
2. Update a product title in Supabase; confirm Shopify product updated within 30s.

## Error Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 401 | Invalid or missing access token | Re-generate token in Shopify admin; update secret |
| 403 | Missing required API scope | Re-install app with correct scopes |
| 422 | Unprocessable entity (bad payload) | Inspect `errors` field in response JSON |
| 429 | API rate limit hit | Shopify REST: 2 req/s; add `Retry-After` header backoff |
| 400 (webhook) | HMAC signature mismatch | Verify `SHOPIFY_WEBHOOK_SECRET` matches Shopify setting |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `SHOPIFY_STORE_DOMAIN` | env secret | e.g., `{{BRAND_SHOPIFY_DOMAIN}}` |
| `SHOPIFY_API_VERSION` | env secret | e.g., `2024-01` |
| `SHOPIFY_ADMIN_TOKEN` | env secret | Admin API access token |
| `SHOPIFY_WEBHOOK_SECRET` | env secret | HMAC signature verification secret |

| Output | Description |
|--------|-------------|
| Supabase `products` rows | Synced from Shopify with `shopify_id`, `shopify_synced_at` |
| Shopify products | Updated from Supabase via push edge function |
| Edge function logs | Visible in Supabase Dashboard -> Edge Functions |

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Products not syncing from Shopify | fetch-from-shopify not called | Invoke manually; check service key auth |
| Webhook HMAC validation failing | Wrong secret or encoding | Re-set `SHOPIFY_WEBHOOK_SECRET`; use raw body for HMAC |
| 429 on bulk product pull | >250 products; loop hitting rate limit | Add `page_info` cursor pagination + 500ms delay |
| Supabase change not pushing to Shopify | DB webhook not configured | Recreate DB webhook in Supabase Dashboard |

## Brand Variables

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Your store's myshopify.com domain |
| `{{BRAND_SHOPIFY_API_VERSION}}` | Admin API version (e.g., `2024-01`) |
| `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` | HMAC secret for webhook validation |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference ID |
| `{{BRAND_NAME}}` | Brand name for app display name |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | related | 0.50 |
| [[p01_kc_supabase_cli]] | upstream | 0.41 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.38 |
| [[p12_wf_supabase_setup]] | downstream | 0.32 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.30 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.29 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.26 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.26 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.25 |
| [[bld_tools_social_publisher]] | related | 0.24 |
