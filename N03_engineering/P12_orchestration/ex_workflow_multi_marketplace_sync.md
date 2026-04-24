---
id: ex_workflow_multi_marketplace_sync
kind: workflow
8f: F8_collaborate
pillar: P12
title: Multi-Marketplace Bidirectional Sync Workflow
version: 0.1.0
quality: 8.3
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, sync, workflow, marketplace]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p12_wf_supabase_setup
  - p12_mission_supabase_data_layer
  - p01_kc_supabase_edge_functions
  - p01_kc_supabase_self_hosting
  - kc_erp_integration
  - bld_instruction_supabase_data_layer
  - p12_dispatch_rule_supabase
  - bld_examples_app_directory_entry
---

## Purpose

Orchestrates bidirectional product synchronization across Shopify, Bling ERP, and Supabase — supports modes `pull`, `push`, `bidirectional`, and `single` for granular control over sync direction and scope.

## When to Use

- Bulk-pulling all Shopify products into Supabase on initial setup.
- Pushing approved Supabase products to Shopify and Bling simultaneously.
- Running a nightly full-sync cron to catch any missed webhook events.
- Syncing a single product by ID after a manual edit.

## Workflow Steps

```
INPUT: { mode, product_id?, shopify_api_version }
  |
  v
STEP 1: VALIDATE
  |-- Check mode is one of: pull | push | bidirectional | single
  |-- If mode == single: require product_id
  |-- Verify active tokens for Shopify + Bling + ML (if needed)
  |
  v
STEP 2: COLLECT
  |-- [pull / bidirectional] Fetch Shopify catalog (paginated)
  |-- [push / bidirectional] Fetch Supabase catalog (active products)
  |-- [single] Fetch one product from both sources
  |
  v
STEP 3: DIFF
  |-- Identify new items (in Shopify, not in Supabase)
  |-- Identify updated items (shopify_updated_at > supabase_updated_at)
  |-- Identify items to push (supabase_updated_at > shopify_synced_at)
  |-- Apply de-duplication by shopify_id
  |
  v
STEP 4: EXECUTE
  |-- [pull] Upsert Shopify items into Supabase products table
  |-- [push] PUT updated fields to Shopify Admin API
  |-- [bidirectional] Pull first, then push non-conflicting changes
  |-- [single] Sync one item both directions
  |
  v
STEP 5: REPORT
  |-- Update sync_log table with counts + errors
  |-- Emit result: { synced, errors, skipped }
```

## Sync Modes

| Mode | Direction | Use Case |
|------|-----------|---------|
| `pull` | Shopify -> Supabase | Initial seed, recovery after Supabase wipe |
| `push` | Supabase -> Shopify | Bulk title/SEO update from internal catalog |
| `bidirectional` | Both | Nightly cron; catch all drifts |
| `single` | Both (one product) | Debug or manual product sync |

## Configuration

```yaml
workflow:
  mode: bidirectional           # pull | push | bidirectional | single
  product_id: null              # required if mode == single
  shopify:
    store_domain: "{{BRAND_SHOPIFY_DOMAIN}}"
    api_version: "2024-01"
    page_size: 250
  bling:
    enabled: true
    batch_size: 10              # Bling rate limit: 3 req/s
  supabase:
    project_ref: "{{BRAND_SUPABASE_PROJECT_REF}}"
    products_table: "products"
    sync_log_table: "sync_log"
  conflict_resolution: shopify_wins  # shopify_wins | supabase_wins | newest_wins
  dry_run: false
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `mode` | enum | Sync direction |
| `product_id` | uuid? | Supabase product UUID (single mode) |
| `dry_run` | bool | Simulate without writing |

| Output | Type | Description |
|--------|------|-------------|
| `synced` | int | Products successfully synced |
| `errors` | int | Products that failed |
| `skipped` | int | Products already in sync |
| `sync_log` | DB row | Persisted sync result |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Shopify store to sync with |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference |

## Example Invocation

```bash
# Nightly full bidirectional sync
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/unified-sync \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -d '{"mode": "bidirectional"}'

# Sync one product
curl -X POST ... -d '{"mode": "single", "product_id": "uuid-here"}'
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | upstream | 0.31 |
| [[p01_kc_supabase_cli]] | upstream | 0.28 |
| [[p12_wf_supabase_setup]] | sibling | 0.21 |
| [[p12_mission_supabase_data_layer]] | related | 0.19 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.18 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.18 |
| [[kc_erp_integration]] | upstream | 0.17 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.16 |
| [[p12_dispatch_rule_supabase]] | related | 0.16 |
| [[bld_examples_app_directory_entry]] | upstream | 0.16 |
