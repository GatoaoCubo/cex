---
id: tpl_template_registry
kind: context_doc
title: "Template Registry — Instance Extraction Templates"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
purpose: Index of all universal templates extracted from gato-ao-cubo patterns
density_score: 0.95
tags: [registry, templates, instance-extraction, mustache]
tldr: "Master registry of 17 templates extracted from gato-ao-cubo → main. All use {{mustache}} variables filled by brand_inject.py or /init."
updated: "2026-04-13"
---

# Template Registry

## Extraction Summary

| Metric | Value |
|--------|:-----:|
| Templates created | 17 |
| Categories | 7 |
| Source branch | gato-ao-cubo |
| Variable system | {{mustache}} (compatible with brand_inject.py) |
| Fill mechanism | `/init` → `brand_inject.py` → `brand_propagate.py` |

---

## Category 1: CRM Mission Pipeline (7 templates)

| Template | Path | Variables |
|----------|------|-----------|
| Mission Plan | `P12_orchestration/templates/tpl_crm_mission_plan.md` | BRAND_NAME, INDUSTRY, REGION, TARGET_COUNT, BATCH_SOURCES, CITIES, PIPELINE_NAME |
| Batch: Directories | `P12_orchestration/templates/tpl_research_batch_directories.md` | INDUSTRY, REGION, DIRECTORY_SOURCES, SEARCH_QUERIES, CITIES |
| Batch: Maps | `P12_orchestration/templates/tpl_research_batch_maps.md` | REGION, CATEGORIES, CITIES, RADIUS_KM, MAPS_PROVIDER |
| Batch: Social | `P12_orchestration/templates/tpl_research_batch_social.md` | INDUSTRY, PLATFORMS, HASHTAGS, REGION, CITIES |
| Batch: Marketplaces | `P12_orchestration/templates/tpl_research_batch_marketplaces.md` | INDUSTRY, MARKETPLACES, SEARCH_TERMS, CITIES |
| Batch: Reputation | `P12_orchestration/templates/tpl_research_batch_reputation.md` | PLATFORMS, REVIEW_SOURCES, MIN_RATING, PROFESSIONAL_REGISTRY |
| Batch: Tax Registry | `P12_orchestration/templates/tpl_research_batch_cnae.md` | CNAE_CODES, REGION, LEGAL_SOURCES, CITIES |

## Category 2: Dashboard (1 template)

| Template | Path | Variables |
|----------|------|-----------|
| CRM Dashboard | `P05_output/templates/tpl_crm_dashboard.html` | BRAND_NAME, BRAND_COLORS.*, MAP_CENTER_LAT, MAP_CENTER_LNG, MAP_ZOOM, CRM_DATA_SOURCE |

## Category 3: CRM Admin Spec (1 template)

| Template | Path | Variables |
|----------|------|-----------|
| Admin Panel Spec | `_docs/specs/tpl_crm_admin_spec.md` | BRAND_NAME, DB_PROVIDER, TABLES, MAP_PROVIDER, AUTH_METHOD, FRAMEWORK |

## Category 4: Research Pipeline (2 templates)

| Template | Path | Variables |
|----------|------|-----------|
| Business Discovery Search | `P04_tools/templates/tpl_search_tool_business_discovery.md` | INDUSTRY, REGION, SEARCH_PROVIDERS, VERTICALS, CITIES |
| Business Intel Retriever | `P04_tools/templates/tpl_retriever_business_intel.md` | SOURCES, MERGE_STRATEGY, DEDUP_FIELDS |

## Category 5: Workflows (3 templates)

| Template | Path | Variables |
|----------|------|-----------|
| Research Pipeline | `P12_orchestration/templates/tpl_workflow_research_pipeline.md` | PIPELINE_NAME, STAGES, QUALITY_GATE, INDUSTRY, REGION, TARGET_COUNT |
| Strategic Outreach | `P12_orchestration/templates/tpl_workflow_strategic_outreach.md` | BRAND_NAME, CHANNELS, OUTREACH_STAGES, SEGMENTS, TARGET_COUNT |
| Pipeline Evidence | `P12_orchestration/templates/tpl_crm_pipeline_evidence.md` | BRAND_NAME, PIPELINE_NAME, BATCHES, FINAL_STATS, CITIES |

## Category 6: Decision Manifest (1 template)

| Template | Path | Variables |
|----------|------|-----------|
| Brand Decision Manifest | `.cex/runtime/decisions/tpl_decision_manifest_brand.yaml` | BRAND_NAME, DECISIONS.*, CONSTRAINTS.* |

## Category 7: Learning Records + Config (2 templates)

| Template | Path | Variables |
|----------|------|-----------|
| Autonomy Learning Record | `P11_feedback/templates/tpl_learning_record_autonomy.md` | MISSION, NUCLEUS, PHASE, FINDINGS, METRICS, RECOMMENDATIONS |
| Nucleus Brand Context | `P12_orchestration/templates/tpl_brand_context_nucleus.md` | NUCLEUS_ID, NUCLEUS_NAME, BRAND_* |

---

## Brand Config Template

| Template | Path | Variables |
|----------|------|-----------|
| brand_config.yaml | `_instances/_template/.cex/brand/brand_config.yaml` | ALL BRAND_* (identity, archetype, voice, audience, visual, content, operations) |

---

## How Templates Get Filled

```
1. User runs /init
2. Answers ~6 questions (name, domain, audience, tone, language, tagline)
3. brand_config.yaml created with real values
4. brand_inject.py resolves {{BRAND_*}} in templates
5. git checkout -b <brand-slug> (new branch)
6. Templates → real artifacts with brand data
7. N07 dispatches first mission using filled templates
```

## Variable Naming Convention

| Prefix | Scope | Example |
|--------|-------|---------|
| `BRAND_*` | Brand identity | `{{BRAND_NAME}}`, `{{BRAND_TAGLINE}}` |
| `INDUSTRY` | Market context | `{{INDUSTRY}}` |
| `REGION` | Geographic scope | `{{REGION}}` |
| `CITIES.*` | City list | `{{#CITIES}}...{{/CITIES}}` |
| `DECISIONS.*` | GDP decisions | `{{DECISIONS.scope.choice}}` |
| `CONSTRAINTS.*` | Execution limits | `{{CONSTRAINTS.language}}` |
| `*_SOURCES` | Data sources | `{{BATCH_SOURCES.directories}}` |
| `FINAL_STATS.*` | Metrics | `{{FINAL_STATS.total}}` |
