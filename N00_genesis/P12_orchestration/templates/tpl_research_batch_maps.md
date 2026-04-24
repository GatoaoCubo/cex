---
id: tpl_research_batch_maps
kind: template
8f: F6_produce
pillar: P12
title: "Research Batch — Maps / Business Profile Deep Harvest"
version: 1.0.0
quality: 9.0
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_b_google_maps.md
variables: [REGION, CATEGORIES, CITIES, RADIUS_KM, MAPS_PROVIDER, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, maps, google-maps, crm, instance-extraction]
tldr: "Maps-based business discovery — systematic category × city matrix via Google Maps or equivalent provider."
updated: "2026-04-13"
related:
  - tpl_research_batch_directories
  - tpl_research_batch_cnae
  - tpl_search_tool_business_discovery
  - tpl_research_batch_social
  - tpl_research_batch_marketplaces
  - tpl_retriever_business_intel
  - tpl_workflow_research_pipeline
  - bld_schema_model_registry
  - n06_schema_brand_config
  - tpl_research_batch_reputation
---

# BATCH B — Maps / Business Profile Deep Harvest

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_b_maps.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_B_MAPS'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (for dedup)

---

## Objective

Sweep {{MAPS_PROVIDER | default: 'Google Maps/Business Profile'}} by **CATEGORY × CITY** matrix to discover businesses not found in other sources. Maps data is often the most complete for phone, rating, reviews, hours, and exact coordinates.

---

## Category × City Matrix

### Categories to Search

{{#CATEGORIES}}
| # | Category | Aliases |
|---|----------|---------|
{{#each}}
| {{position}} | "{{primary}}" | {{aliases}} |
{{/each}}
{{/CATEGORIES}}

### Cities (sweep ALL)

{{#CITIES}}
| City | State | Priority |
|------|-------|:--------:|
{{#each}}
| {{name}} | {{state}} | {{priority}} |
{{/each}}
{{/CITIES}}

### Query Format

```
SERPER: "{{category}}" near "{{city}}" {{state}}
SERPER: "{{category}}" "{{city}}" phone hours
```

Or with radius:

```
SERPER: "{{category}}" within {{RADIUS_KM | default: '15'}}km of "{{center_city}}"
```

---

## Data Extraction (per result)

```json
{
  "nome_fantasia": "string (required)",
  "endereco": "string (full address from Maps)",
  "cidade": "string (required)",
  "uf": "string",
  "telefone": "string",
  "google_rating": "float (1.0-5.0)",
  "google_reviews": "integer",
  "horario": "string (business hours)",
  "google_maps_url": "string",
  "lat": "float",
  "lng": "float",
  "segmento": "string (required)",
  "fonte": "google_maps"
}
```

---

## Priority Rules

1. **High-value signals**: phone, coordinates, rating > 4.0, reviews > 10
2. **Skip chains**: if a national chain has 100+ locations, mark as `chain: true`
3. **Dedup**: match on normalized name + city before merge
4. **Coordinates**: always capture lat/lng for dashboard mapping

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_research_batch_directories]] | sibling | 0.47 |
| [[tpl_research_batch_cnae]] | sibling | 0.38 |
| [[tpl_search_tool_business_discovery]] | sibling | 0.37 |
| [[tpl_research_batch_social]] | sibling | 0.32 |
| [[tpl_research_batch_marketplaces]] | sibling | 0.29 |
| [[tpl_retriever_business_intel]] | sibling | 0.28 |
| [[tpl_workflow_research_pipeline]] | sibling | 0.28 |
| [[bld_schema_model_registry]] | upstream | 0.28 |
| [[n06_schema_brand_config]] | upstream | 0.26 |
| [[tpl_research_batch_reputation]] | sibling | 0.25 |
