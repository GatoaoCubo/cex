---
id: ex-workflow-multi-marketplace-sync
kind: workflow
8f: F8_collaborate
pillar: P12
title: Multi-Marketplace Sync Workflow
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_BLING_API_URL
  - BRAND_MELI_USER_ID
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, orchestration, sync, multi_marketplace]
density_score: 0.99
related:
  - p01_kc_brand_voice_consistency_channels
  - p01_kc_supabase_realtime
  - bld_instruction_notifier
  - p01_kc_notifier
  - p03_pt_marketing_task_execution
  - n06_schema_brand_voice_contract
  - kc_erp_integration
  - p05_fmt_marketing_report
  - p04_notifier_NAME
  - p03_sp_notifier_builder
---

# Multi-Marketplace Sync Workflow

## Purpose
Orchestrates bidirectional state convergence across Shopify (storefront), Bling (ERP / fiscal truth), and Mercado Livre (marketplace) using Supabase as the hub-of-truth. Replaces ad-hoc cron jobs with a single, observable workflow with retry + backoff + circuit-breaker.

## When to use
- Brand operates on 2+ channels and SKUs must stay in sync.
- Stock discrepancy tolerance is <5 units and <15 minutes.
- Your ops team wants one place to look when "the systems disagree."

## When NOT to use
- Single-channel brand -- use the channel-specific api_client directly.
- Read-only mirror -- the downstream workflow is simpler than this full sync graph.

## Interface
- Trigger: cron every 15 min (default) OR on-demand `POST /unified-sync { mode: "pull"|"push"|"bidirectional"|"single", resource: "products"|"inventory"|"orders", dry_run?: bool }`.
- Output: structured report `{ started_at, ended_at, channels_touched, deltas, errors }`; persisted in `sync_runs` table.
- Side effects: writes to `products`, `inventory`, `orders`; emits metrics `sync.{channel}.{resource}.{op}.count`.

## Brand variables used
- `{{BRAND_NAME}}` -- report labeling.
- `{{BRAND_SHOPIFY_STORE_DOMAIN}}`, `{{BRAND_BLING_API_URL}}`, `{{BRAND_MELI_USER_ID}}` -- channel targeting.
- `{{BRAND_SUPABASE_PROJECT_REF}}` -- persistence layer.

## Workflow steps (see `ex_dag_multi_marketplace_sync.md` for the DAG)

1. **Acquire run lock** -- `pg_advisory_lock("sync")`; if busy, exit gracefully (cron will retry).
2. **Load channel health** -- check each channel's last ok heartbeat; skip unhealthy channels.
3. **Pull phase** (channels -> Supabase):
   - Shopify: diff by `updated_at` since last sync cursor.
   - Bling: relies on webhooks; sync only runs backfill if webhook gap detected.
   - ML: poll by seller + last_update_date.
4. **Reconcile phase**:
   - For each product present in >=2 channels, pick authority rule (see dispatch_rule).
   - Detect conflicts (same SKU, different titles). Log to `sync_conflicts`; do NOT auto-resolve on first encounter.
5. **Push phase** (Supabase -> channels):
   - Only push rows with `dirty=true` flag; clear flag on 2xx response.
   - Batch pushes per channel (Shopify 50, Bling 100, ML 20).
6. **Post-run audit** -- count `dirty` rows remaining; alert if > 5% of catalog (indicates repeated failures).
7. **Release lock**, write run report.

## Failure policy
- Per-channel circuit breaker: 5 consecutive failures -> mark channel unhealthy for 10 min.
- Partial success is SUCCESS: workflow reports per-channel outcome; exits 0 as long as no channel reports a hard auth error.
- Hard failure = OAuth invalidation or 5xx for >5 min on same endpoint; page ops.

## Idempotency
Every push carries a `request_id = hash(sku, channel, field, value, date)`. Channels that support idempotency keys (Shopify GraphQL mutations via `extensions.userErrors`) use it; others rely on natural key uniqueness.

## Related artifacts
- `ex_dag_multi_marketplace_sync.md` -- formal DAG.
- `ex_dispatch_rule_multi_marketplace.md` -- authority rules.
- `ex_workflow_inventory_reconcile.md` -- stock-only specialized version.
- `ex_api_client_shopify.md`, `ex_api_client_bling.md`, `ex_api_client_meli.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.26 |
| [[p01_kc_supabase_realtime]] | upstream | 0.26 |
| [[bld_instruction_notifier]] | upstream | 0.22 |
| [[p01_kc_notifier]] | upstream | 0.21 |
| [[p03_pt_marketing_task_execution]] | upstream | 0.21 |
| [[n06_schema_brand_voice_contract]] | upstream | 0.21 |
| [[kc_erp_integration]] | upstream | 0.20 |
| [[p05_fmt_marketing_report]] | upstream | 0.19 |
| [[p04_notifier_NAME]] | upstream | 0.19 |
| [[p03_sp_notifier_builder]] | upstream | 0.18 |
