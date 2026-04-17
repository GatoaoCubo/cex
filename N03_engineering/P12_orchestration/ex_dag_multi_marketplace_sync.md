---
id: ex_dag_multi_marketplace_sync
kind: dag
pillar: P12
title: Multi-Marketplace Sync DAG
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, dag, sync, marketplace]
density_score: 1.0
updated: "2026-04-17"
---

## Purpose

Directed Acyclic Graph (DAG) definition for multi-marketplace product sync — maps the dependency order of sync stages to enable parallel execution where possible and guarantee correct sequencing for dependent steps.

## When to Use

- Implementing the unified-sync function as a structured pipeline with explicit stage dependencies.
- Visualizing the sync execution plan for debugging or monitoring.
- Extending the sync with new stages (e.g., Mercado Livre push) without breaking existing order.

## DAG Definition

```yaml
dag:
  id: multi_marketplace_sync
  description: Bidirectional product sync across Shopify, Bling, Supabase
  schedule: "0 3 * * *"   # nightly at 03:00 local
  concurrency: 3

nodes:
  - id: validate_tokens
    type: task
    fn: checkActiveTokens
    inputs: [shopify, bling, meli]
    outputs: [token_status]

  - id: fetch_shopify
    type: task
    fn: fetchShopifyProducts
    depends_on: [validate_tokens]
    inputs: [shopify_config]
    outputs: [shopify_products]

  - id: fetch_supabase
    type: task
    fn: fetchSupabaseProducts
    depends_on: [validate_tokens]
    inputs: [supabase_config]
    outputs: [supabase_products]

  - id: diff_shopify_supabase
    type: task
    fn: computeDiff
    depends_on: [fetch_shopify, fetch_supabase]
    inputs: [shopify_products, supabase_products]
    outputs: [to_pull, to_push, in_sync]

  - id: pull_to_supabase
    type: task
    fn: upsertToSupabase
    depends_on: [diff_shopify_supabase]
    condition: "to_pull.length > 0"
    inputs: [to_pull]
    outputs: [pull_result]

  - id: push_to_shopify
    type: task
    fn: pushToShopify
    depends_on: [diff_shopify_supabase]
    condition: "to_push.length > 0"
    inputs: [to_push]
    outputs: [push_result]

  - id: push_to_bling
    type: task
    fn: pushToBling
    depends_on: [pull_to_supabase]   # Bling gets fresh Supabase data
    condition: "bling.enabled"
    inputs: [supabase_products_updated]
    outputs: [bling_result]

  - id: write_sync_log
    type: task
    fn: writeSyncLog
    depends_on: [pull_to_supabase, push_to_shopify, push_to_bling]
    inputs: [pull_result, push_result, bling_result]
    outputs: [sync_log_id]

  - id: notify_on_error
    type: task
    fn: sendErrorNotification
    depends_on: [write_sync_log]
    condition: "sync_log.errors > 0"
    inputs: [sync_log_id]
    outputs: []
```

## Execution Graph (ASCII)

```
validate_tokens
  |
  +-- fetch_shopify ---+
  |                    |
  +-- fetch_supabase --+-- diff_shopify_supabase
                              |
                  +-----------+-----------+
                  |                       |
           pull_to_supabase       push_to_shopify
                  |
           push_to_bling
                  |
           write_sync_log
                  |
           notify_on_error (conditional)
```

## Stage Timings (Expected)

| Stage | Expected Duration | Parallel |
|-------|-----------------|---------|
| `validate_tokens` | < 1s | No |
| `fetch_shopify` | 5-60s (250 products/page) | Yes (with fetch_supabase) |
| `fetch_supabase` | 1-5s | Yes (with fetch_shopify) |
| `diff_shopify_supabase` | < 1s | No |
| `pull_to_supabase` | 2-10s | No |
| `push_to_shopify` | 5-30s (rate-limited) | No |
| `push_to_bling` | 10-60s (3 req/s limit) | No |
| `write_sync_log` | < 1s | No |

Total: 30-180s depending on catalog size.

## Error Handling

| Stage Failure | Behavior |
|--------------|---------|
| `validate_tokens` | Abort all; no sync runs without valid tokens |
| `fetch_shopify` | Abort pull stages; push stages can still run |
| `pull_to_supabase` | Log errors per item; continue with next |
| `push_to_shopify` | Log errors per item; Bling push still runs |
| `push_to_bling` | Log errors; sync_log marks Bling as partial |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Shopify store domain |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_workflow_multi_marketplace_sync.md` | workflow | High-level workflow spec |
| `ex_dispatch_rule_multi_marketplace.md` | dispatch_rule | Marketplace routing logic |
| `ex_api_client_shopify.md` | api_client | Shopify fetch/push |
| `ex_api_client_bling.md` | api_client | Bling push |
