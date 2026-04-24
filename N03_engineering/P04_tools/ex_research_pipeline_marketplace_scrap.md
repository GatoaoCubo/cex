---
quality: 8.0
quality: 7.3
id: ex_research_pipeline_marketplace_scrap
kind: research_pipeline
8f: F5_call
pillar: P04
title: Marketplace Catalog Research Pipeline
version: 0.1.0
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, research, marketplace, scrap]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p12_mission_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - p01_kc_supabase_edge_functions
  - p12_wf_supabase_setup
  - p12_dispatch_rule_supabase
  - bld_examples_app_directory_entry
  - p01_kc_bling_erp_field_parametrization
  - instance_supabase_config_template
---

## Purpose

Automated research pipeline that cross-references the internal Supabase product catalog against Bling ERP and Mercado Livre — detects orphans, duplicates, and enrichment opportunities, then produces a structured audit report.

## When to Use

- Auditing catalog integrity across Supabase, Bling, and Mercado Livre.
- Finding products in Supabase that are missing from Bling (before mass creation).
- Discovering ML catalog items that match internal products for auto-enrichment.
- Generating a weekly discrepancy report for catalog management.

## Pipeline Stages

```
Stage 1: COLLECT
  |-- Fetch all Supabase product IDs + codes + titles
  |-- Fetch all Bling product codes via paginated API
  |-- Search ML catalog for each product (by EAN or title)

Stage 2: DIFF
  |-- In Supabase but NOT in Bling -> orphan_supabase_only[]
  |-- In Bling but NOT in Supabase -> orphan_bling_only[]
  |-- In both but stock mismatch  -> stock_discrepancy[]
  |-- In Supabase with ML match   -> enrichable[]

Stage 3: SCORE
  |-- Severity score per discrepancy (HIGH=stock differs >10%, MEDIUM=missing, LOW=metadata)
  |-- Estimated effort to fix (auto-fixable vs manual)

Stage 4: REPORT
  |-- Write structured JSON report to Supabase storage
  |-- Write summary markdown to research_reports/ table
  |-- Emit signal for N07 consolidation
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `supabase_products` | DB query | All active products from Supabase |
| `bling_products` | Bling API v3 | Paginated product list |
| `meli_search` | ML API | Catalog search per product |
| `dry_run` | bool | If true, report only; do not fix |
| `auto_fix` | bool | If true, trigger auto-creation for orphans |

| Output | Type | Description |
|--------|------|-------------|
| `audit_report.json` | Supabase storage | Full discrepancy dataset |
| `audit_summary.md` | Markdown | Human-readable summary |
| `enrichable_ids[]` | Array | Supabase product IDs with ML matches |
| `orphan_supabase_only[]` | Array | Products to create in Bling |

## Configuration

```json
{
  "batch_size": 50,
  "bling_rate_limit_ms": 400,
  "meli_rate_limit_ms": 200,
  "stock_discrepancy_threshold_pct": 10,
  "max_enrichment_candidates": 100,
  "report_storage_bucket": "audit-reports",
  "report_path_prefix": "catalog/{{BRAND_SUPABASE_PROJECT_REF}}"
}
```

## Example Invocation

```bash
# Dry run: report only
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-audit \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -d '{"dry_run": true}'

# With auto-fix: create missing Bling products
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-audit \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -d '{"dry_run": false, "auto_fix": true}'
```

## Sample Report Structure

```json
{
  "run_at": "2026-04-17T10:00:00Z",
  "supabase_total": 312,
  "bling_total": 289,
  "orphan_supabase_only": [{ "id": "uuid", "code": "CAT-001", "title": "..." }],
  "orphan_bling_only": [{ "bling_id": 12345, "code": "BL-900" }],
  "stock_discrepancy": [{ "code": "CAT-005", "supabase_stock": 10, "bling_stock": 3 }],
  "enrichable": [{ "supabase_id": "uuid", "meli_id": "MLB123456", "confidence": 0.92 }]
}
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_MELI_CLIENT_ID}}` | ML OAuth client ID for catalog search |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for DB + storage |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | related | 0.43 |
| [[p01_kc_supabase_cli]] | upstream | 0.34 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.26 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.26 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.24 |
| [[p12_wf_supabase_setup]] | downstream | 0.24 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.23 |
| [[bld_examples_app_directory_entry]] | downstream | 0.22 |
| [[p01_kc_bling_erp_field_parametrization]] | upstream | 0.21 |
| [[instance_supabase_config_template]] | upstream | 0.21 |
