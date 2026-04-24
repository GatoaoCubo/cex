---
id: ex-workflow-inventory-reconcile
kind: workflow
8f: F8_collaborate
pillar: P12
title: Inventory Reconcile Workflow
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_BLING_API_URL
  - BRAND_BLING_DEPOSITS
  - BRAND_RECONCILE_TOLERANCE
tags: [commerce, template, distillation, orchestration, inventory, reconcile]
density_score: 0.95
related:
  - kc_erp_integration
  - p01_kc_bling_erp_automation_boundary
  - p01_kc_bling_erp_field_parametrization
  - p03_sp_brand_nucleus
  - p03_sp_workflow-builder
---

# Inventory Reconcile Workflow

## Purpose
Specialized workflow focused solely on stock convergence across Supabase (cache), Bling (ERP truth), and Shopify (storefront display). Catches drift, reports it, and -- on operator consent -- auto-corrects by writing Bling's number back into the other channels.

## When to use
- Stock discrepancies cause canceled orders or oversells and you need them fixed daily.
- Bling ERP is the accounting truth and you can't let Shopify drift.
- You want a dry-run diff view before any write.

## When NOT to use
- Single-channel brand -- trivially consistent.
- Brands that don't use Bling -- build a simplified 2-channel version.

## Brand variables used
- `{{BRAND_NAME}}` -- report labeling.
- `{{BRAND_SHOPIFY_STORE_DOMAIN}}`, `{{BRAND_BLING_API_URL}}` -- channel endpoints.
- `{{BRAND_BLING_DEPOSITS}}` -- JSON array of Bling deposito ids counted as "available stock".
- `{{BRAND_RECONCILE_TOLERANCE}}` -- integer; deltas smaller than this are logged but not acted on (default `2`).

## Workflow

1. **Snapshot**
   - Pull current Supabase `inventory` rows into memory.
   - Pull current Bling `estoques` for `{{BRAND_BLING_DEPOSITS}}` (one call per deposito, parallel).
   - Pull current Shopify `inventoryLevels` via bulk GraphQL query.
2. **Normalize** -- every row keyed by `(sku, warehouse_or_location)`; align to the Bling taxonomy (Bling is truth).
3. **Compute deltas**
   - For each SKU: Bling_total = sum over deposits; Supabase_total = aggregate row; Shopify_total = sum over locations.
   - `delta_shopify = shopify_total - bling_total`; `delta_supabase = supabase_total - bling_total`.
4. **Tolerance filter** -- drop any SKU whose |delta| <= `{{BRAND_RECONCILE_TOLERANCE}}`.
5. **Validate** -- run `ex_validator_inventory_invariants.md` checks (see there for rules). Hard failures abort the workflow; warnings continue.
6. **Report** -- write to `inventory_reconcile_runs` table: `{run_id, started_at, discrepancies_count, auto_corrected_count, report_path}`.
7. **Act**
   - Mode `dry_run` -> return report, no writes.
   - Mode `auto_correct` -> for each SKU, write Bling total to Supabase + Shopify.
   - Mode `propose` -> attach proposals to a ticket in the ops queue; human approves before write.
8. **Notify** -- `ex_notifier_webhook.md` emits `stock_low` for SKUs below `brand.reorder_threshold`.

## Safety rails
- If discrepancy set > 25% of catalog AND mode is `auto_correct` -> refuse and downgrade to `propose`; assumes a systemic bug, not real drift.
- If Bling is unreachable -> refuse to touch Shopify; stale Bling data would cause wrong writes.
- Always record `before/after` per SKU for 90 days so an operator can revert a bad correction.

## Scheduling
- Default cron: every 2h during business hours, every 6h off-hours.
- On-demand trigger from admin dashboard "Reconcile now" button.

## Related artifacts
- `ex_validator_inventory_invariants.md` -- rule set used in validate step.
- `ex_workflow_multi_marketplace_sync.md` -- the broader sync; this is a specialization.
- `ex_api_client_bling.md`, `ex_api_client_shopify.md`
- `ex_notifier_webhook.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_erp_integration]] | upstream | 0.26 |
| [[p01_kc_bling_erp_automation_boundary]] | upstream | 0.22 |
| [[p01_kc_bling_erp_field_parametrization]] | upstream | 0.21 |
| [[p03_sp_brand_nucleus]] | upstream | 0.17 |
| [[p03_sp_workflow-builder]] | upstream | 0.16 |
