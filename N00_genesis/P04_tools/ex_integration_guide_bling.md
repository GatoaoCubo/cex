---
id: ex-integration-guide-bling
kind: integration_guide
8f: F6_produce
pillar: P04
title: Bling ERP Integration Guide
version: 0.1.0
quality: 9.0
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_BLING_ACCESS_TOKEN
  - BRAND_BLING_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, bling, integration_guide]
density_score: 1.0
related:
  - p01_kc_bling_erp_automation_boundary
  - p01_kc_bling_erp_field_parametrization
  - kc_erp_integration
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p01_kc_supabase_edge_functions
  - p12_wf_supabase_setup
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - bld_manifest_supabase_data_layer
---

# Bling ERP Integration Guide

## Purpose
Bind {{BRAND_NAME}} to Bling ERP for fiscal product registration, warehouse stock truth, order mirroring, and (optionally) NF-e emission. This is the Brazilian fiscal backbone layer.

## When to use
- Brand sells in Brazil and needs fiscal compliance beyond the storefront.
- Inventory-of-truth moves from Shopify to the ERP layer.
- NF-e emission is required per sale (B2B default, B2C depending on regime).

## Prerequisites
- Bling Plus or higher subscription (API access is not on free tier).
- Bling dev app created at `https://developer.bling.com.br`: client_id, client_secret, redirect_uri whitelisted.
- Supabase tables: `products`, `inventory`, `orders_bling`, `invoices`, `webhook_inbox_bling`, `bling_tokens`.

## Architecture

```
Bling ERP
  |-- webhooks --> [bling-webhook]        --> Supabase.products/inventory/orders_bling/invoices
  |-- REST <-- [sync-bling-product]      <-- DB trigger
  |-- REST <-- [sync-all-products-bling] <-- manual batch
  |-- REST <-- [bling-audit]             <-- daily cron
  |-- REST <-- [bling-create-missing]    <-- reconciler
  |
  +-- OAuth <-- [bling-oauth-callback]   <-- admin UI link
  +-- OAuth refresh <-- [token-auto-refresh] <-- 5h55m cron
```

## Brand variables used
All listed in frontmatter; treat client secret and webhook secret as P0 secrets (Supabase vault, not repo).

## Setup steps
1. **Create Bling dev app** -- grant scopes listed in `ex_oauth_app_config_bling.md`.
2. **Connect account** -- user clicks "Connect Bling" in admin; browser -> authorize URL -> callback -> token stored.
3. **Deploy edge functions**:
   ```bash
   supabase functions deploy bling-webhook
   supabase functions deploy bling-oauth-callback
   supabase functions deploy token-auto-refresh
   supabase functions deploy sync-bling-product
   supabase functions deploy sync-all-products-bling
   supabase functions deploy bling-audit
   supabase functions deploy bling-create-missing
   ```
4. **Schedule refresher** -- `token-auto-refresh` cron every 5h55m; never let a token lapse silently.
5. **Register webhook URL** in Bling dashboard: `https://{{BRAND_SUPABASE_PROJECT_REF}}.functions.supabase.co/bling-webhook`. Save HMAC key into `{{BRAND_BLING_WEBHOOK_SECRET}}`.
6. **Initial reconcile** -- run `bling-audit` in `dry_run=true`; expect full diff report. Feed `bling-create-missing` with the diff once reviewed.
7. **Schedule nightly audit** -- `bling-audit` cron 03:00 local; alert if diff > 1% of catalog.

## Verification checklist
- [ ] `GET /Api/v3/situacoes/Produto` returns 200 with bearer token.
- [ ] Test produto create via UI -> webhook lands within 20s -> Supabase `products` row has `source=bling`.
- [ ] Token refresh: force-expire token (set `expires_at` to past) -> next API call refreshes silently.
- [ ] Rate limit: trigger 10 concurrent `sync-bling-product` calls -> no 429 (client holds requests in bucket).

## Quirks + gotchas
- NCM code is required for every produto -- set default in `BRAND_DEFAULT_NCM` to avoid fiscal block.
- Bling SKU (`codigo`) is the CROSS-SYSTEM key. Keep Shopify SKU == Bling codigo identical; mismatches cause duplicates.
- `estoque` is per-warehouse. `inventory-reconcile` MUST sum across the warehouses listed in `BRAND_BLING_DEPOSITS`.
- Deletion: prefer `situacao=I` (soft-delete) over hard delete; Bling retains fiscal history.

## Related artifacts
- `ex_api_client_bling.md`
- `ex_webhook_bling.md`
- `ex_oauth_app_config_bling.md`
- `ex_workflow_inventory_reconcile.md`
- `ex_workflow_multi_marketplace_sync.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bling_erp_automation_boundary]] | upstream | 0.36 |
| [[p01_kc_bling_erp_field_parametrization]] | upstream | 0.35 |
| [[kc_erp_integration]] | upstream | 0.33 |
| [[bld_tools_supabase_data_layer]] | related | 0.32 |
| [[p01_kc_supabase_cli]] | upstream | 0.26 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.24 |
| [[p12_wf_supabase_setup]] | downstream | 0.21 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.20 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.18 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.17 |
