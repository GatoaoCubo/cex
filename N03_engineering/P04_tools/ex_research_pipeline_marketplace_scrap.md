---
id: ex_research_pipeline_marketplace_scrap
kind: research_pipeline
pillar: P04
title: Marketplace Catalog Research Pipeline
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, research, marketplace, scrap]
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

| Artifact | Kind | Role |
|----------|------|------|
| `ex_browser_tool_marketplace_scrap.md` | browser_tool | Web scraping fallback |
| `ex_api_client_bling.md` | api_client | Bling data source |
| `ex_api_client_meli.md` | api_client | ML data source |
| `ex_workflow_inventory_reconcile.md` | workflow | Post-audit reconciliation |
