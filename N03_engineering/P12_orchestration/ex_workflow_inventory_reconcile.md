---
id: ex_workflow_inventory_reconcile
kind: workflow
pillar: P12
title: Inventory Reconciliation Workflow
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, inventory, reconcile, workflow]
density_score: 1.0
updated: "2026-04-17"
---

## Purpose

Compares stock quantities across Supabase, Bling ERP, and Shopify — detects discrepancies, generates a reconciliation report, and optionally auto-corrects to a designated source of truth.

## When to Use

- Running a daily or weekly stock audit to catch sync drift.
- Resolving inventory discrepancies after a webhook outage.
- Before major sales events (Black Friday, etc.) to ensure stock accuracy.
- Post-migration validation after importing a new catalog.

## Workflow Steps

```
INPUT: { source_of_truth, auto_correct, threshold_pct }
  |
  v
STEP 1: FETCH
  |-- Fetch Supabase products with stock > 0
  |-- Fetch Bling stock levels (via /estoques)
  |-- Fetch Shopify inventory levels (via /inventory_levels.json)
  |
  v
STEP 2: JOIN
  |-- Match by code/SKU across all three sources
  |-- Unmatched products -> unmapped_items[]
  |
  v
STEP 3: DIFF
  |-- For each matched product:
  |     |-- Compare quantities (supabase vs bling vs shopify)
  |     |-- Flag if max-min deviation > threshold_pct
  |     |-- Classify: OK | MISMATCH | MISSING_IN_SOURCE
  |
  v
STEP 4: REPORT
  |-- Write reconciliation_report.json to Supabase storage
  |-- Insert summary row into inventory_audits table
  |
  v
STEP 5: CORRECT (conditional: auto_correct == true)
  |-- For each MISMATCH:
  |     |-- Apply source_of_truth stock to all other platforms
  |     |-- Log correction applied
  |-- For MISSING_IN_SOURCE:
  |     |-- Skip (requires human review)
  |
  v
STEP 6: NOTIFY
  |-- If corrections > 0: send summary email
  |-- If unmapped_items > 5: alert for catalog cleanup
```

## Configuration

```yaml
workflow:
  source_of_truth: supabase       # supabase | bling | shopify
  auto_correct: false             # true enables write corrections
  threshold_pct: 10               # flag if stock differs by > 10%
  notify_email: "{{BRAND_SUPPORT_EMAIL}}"
  supabase:
    project_ref: "{{BRAND_SUPABASE_PROJECT_REF}}"
  shopify:
    store_domain: "{{BRAND_SHOPIFY_DOMAIN}}"
  report:
    storage_bucket: "audit-reports"
    retention_days: 90
```

## Report Schema

```json
{
  "run_at": "2026-04-17T03:00:00Z",
  "source_of_truth": "supabase",
  "threshold_pct": 10,
  "summary": {
    "total_products": 312,
    "ok": 289,
    "mismatch": 15,
    "missing_in_bling": 4,
    "missing_in_shopify": 2,
    "unmapped": 2
  },
  "mismatches": [
    {
      "sku": "CAT-005",
      "supabase_stock": 10,
      "bling_stock": 3,
      "shopify_stock": 10,
      "deviation_pct": 70,
      "auto_corrected": false
    }
  ]
}
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `source_of_truth` | enum | Which platform's stock is authoritative |
| `auto_correct` | bool | Whether to apply corrections automatically |
| `threshold_pct` | int | Minimum deviation % to flag as mismatch |

| Output | Type | Description |
|--------|------|-------------|
| `reconciliation_report` | JSON (storage) | Full discrepancy dataset |
| `inventory_audits` row | DB | Summary metrics |
| `corrections_applied` | int | Number of auto-corrections made |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Shopify store for inventory levels |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for DB + storage |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_validator_inventory_invariants.md` | validator | Business rule validation |
| `ex_research_pipeline_marketplace_scrap.md` | research_pipeline | Broader catalog audit |
| `ex_api_client_shopify.md` | api_client | Shopify inventory source |
| `ex_api_client_bling.md` | api_client | Bling stock source |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Sync that feeds this reconciliation |
