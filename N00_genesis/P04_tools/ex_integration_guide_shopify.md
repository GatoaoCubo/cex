---
id: ex-integration-guide-shopify
kind: integration_guide
pillar: P04
title: Shopify Integration Guide
version: 0.1.0
quality: 9.0
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
  - BRAND_SHOPIFY_ADMIN_TOKEN
  - BRAND_SHOPIFY_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, shopify, integration_guide]
density_score: 1.0
related:
  - bld_tools_supabase_data_layer
  - bld_tools_social_publisher
  - p01_kc_supabase_cli
  - bld_instruction_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_collaboration_webhook
  - p01_kc_supabase_edge_functions
  - bld_architecture_social_publisher
  - webhook-builder
  - kc_app_directory_entry
---

# Shopify Integration Guide

## Purpose
Wire {{BRAND_NAME}} to Shopify for bidirectional catalog + inventory + order sync. This guide glues together the api_client, webhook handler, OAuth config, and Supabase mirror into one reproducible setup.

## When to use
- New brand onboarding that uses Shopify as the storefront of record.
- Migration from a private Shopify app token to a public/custom app with OAuth.
- Recovery procedure after rotating webhook secrets or admin tokens.

## Prerequisites
- Supabase project provisioned (`{{BRAND_SUPABASE_PROJECT_REF}}`) with tables: `products`, `inventory`, `orders`, `shopify_installations`, `webhook_inbox`, `shopify_sync_log`.
- Shopify store admin access: `{{BRAND_SHOPIFY_STORE_DOMAIN}}`.
- Env vars set: `{{BRAND_SHOPIFY_ADMIN_TOKEN}}`, `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}`.
- API version pinned: `{{BRAND_SHOPIFY_API_VERSION}}` (rotate every 6 months).

## Architecture (read top to bottom)

```
Shopify store
  |-- webhooks --> [shopify-webhook-handler]  --> Supabase.products/inventory/orders
  |                                               |
  |                                               +-- db trigger --> [product-sync-webhook] --> Shopify Admin API
  |
  +-- Admin API <-- [unified-sync]             <-- cron
  +-- Admin API <-- [fetch-from-shopify]       <-- manual
  +-- Admin API <-- [push-titles-to-shopify]   <-- admin UI
```

## Brand variables used
All listed in frontmatter; every one must be an env var in the edge function runtime, NEVER a literal.

## Setup steps
1. **Create Shopify app** -- Admin > Apps > Develop apps > Create app. Add scopes: `read_products, write_products, read_inventory, write_inventory, read_orders`.
2. **Install OAuth flow** (if multi-tenant) -- see `ex_oauth_app_config_shopify.md`. Skip if single-store custom app.
3. **Provision admin token** -- copy from app install page into `{{BRAND_SHOPIFY_ADMIN_TOKEN}}`.
4. **Deploy edge functions**:
   ```bash
   supabase functions deploy shopify-webhook-handler
   supabase functions deploy fetch-from-shopify
   supabase functions deploy push-titles-to-shopify
   supabase functions deploy unified-sync
   ```
5. **Register webhooks** -- run `webhook-manager` once: `POST /webhook-manager {op:"setup"}`. It creates `products/update`, `inventory_levels/update`, `orders/create`, `orders/paid`, `app/uninstalled`.
6. **Initial catalog backfill** -- `POST /fetch-from-shopify {full: true}`; expect ~2 min per 1000 products.
7. **Verify inventory reconcile** -- run `inventory-reconcile` in `dry_run=true`; expect 0 discrepancies on a clean install.
8. **Enable DB trigger** -- Supabase dashboard > Database > Triggers > enable `product_sync_outbound` on `products` table.

## Verification checklist
- [ ] `GET /shopify/admin/api/{{BRAND_SHOPIFY_API_VERSION}}/shop.json` returns 200 with the token.
- [ ] Inbound webhook delivery log shows ingress within 10s of a test product update.
- [ ] Double-UTF-8 repair regression: create a product named `Portão` in Shopify, verify `Portão` (not `PortÃ£o`) lands in Supabase.
- [ ] Uninstall test: remove app -> `app/uninstalled` fires -> installation row soft-deleted.

## Troubleshooting
| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| 401 from Admin API | Token revoked or wrong scope | Reinstall app, refresh scopes |
| 429 loops | Missing bucket backoff | See rate-limit contract in `ex_api_client_shopify.md` |
| Webhook not received | HMAC secret mismatch after rotation | Re-run webhook-manager `rotate_secret` op |
| `PortÃ£o` in DB | UTF-8 repair skipped | Enable on read path in api_client |

## Related artifacts
- `ex_api_client_shopify.md`
- `ex_webhook_shopify.md`
- `ex_oauth_app_config_shopify.md`
- `ex_webhook_manager_shopify.md`
- `ex_workflow_multi_marketplace_sync.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | related | 0.29 |
| [[bld_tools_social_publisher]] | related | 0.25 |
| [[p01_kc_supabase_cli]] | upstream | 0.25 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.24 |
| [[p12_wf_supabase_setup]] | downstream | 0.23 |
| [[bld_collaboration_webhook]] | related | 0.22 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.22 |
| [[bld_architecture_social_publisher]] | downstream | 0.22 |
| [[webhook-builder]] | related | 0.22 |
| [[kc_app_directory_entry]] | upstream | 0.21 |
