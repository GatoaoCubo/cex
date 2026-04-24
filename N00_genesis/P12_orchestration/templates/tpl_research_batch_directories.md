---
id: tpl_research_batch_directories
kind: template
8f: F6_produce
pillar: P12
title: "Research Batch — Industry Directory Scraping"
version: 1.0.0
quality: 9.0
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_a_diretorios_pet.md
variables: [INDUSTRY, REGION, DIRECTORY_SOURCES, SEARCH_QUERIES, CITIES, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, directories, crm, instance-extraction]
tldr: "Directory-based business discovery batch — scrape industry-specific portals and local listings for contact data."
updated: "2026-04-13"
related:
  - tpl_research_batch_maps
  - bld_schema_model_registry
  - n06_schema_brand_config
  - bld_schema_experiment_tracker
  - tpl_research_batch_cnae
  - tpl_research_batch_marketplaces
  - tpl_research_batch_social
  - bld_schema_training_method
  - tpl_search_tool_business_discovery
  - bld_schema_tagline
---

# BATCH A — {{INDUSTRY}} Directory Discovery

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_a_directories.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_A_DIRECTORIES'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (for dedup)

---

## Directory Sources

{{#DIRECTORY_SOURCES}}
### {{position}}. {{name}} ({{roi_tier}})

```
URL: {{url}}
Method: {{method}}

{{#cities}}
Scrape for: {{city_name}}, {{state}}
{{/cities}}

Extract:
  - Business name
  - Full address
  - Phone number
  - Specialties / categories
  - Rating (if available)
  - Credentials (if available)
```

**Why this source matters**: {{rationale}}

{{/DIRECTORY_SOURCES}}

---

## Fallback: Generic Local Directories

If industry-specific directories don't exist for your market:

| Directory | Type | Coverage |
|-----------|------|----------|
| Google Business / Maps | Universal | Global |
| TeleListas / Yellow Pages | Local listings | National |
| City business registry | Municipal | Local |
| Chamber of Commerce | Associations | Regional |

---

## Data Extraction Schema

For each contact found:

```json
{
  "nome_fantasia": "string (required)",
  "endereco": "string",
  "cidade": "string (required)",
  "uf": "string",
  "telefone": "string (BR format: +55 XX XXXXX-XXXX)",
  "email": "string",
  "website": "string",
  "segmento": "string (required)",
  "sub_segmento": "string",
  "fonte": "{{source_name}}",
  "credenciais": "string",
  "notas": "string"
}
```

---

## Quality Rules

1. **Never fabricate** — if a directory has no results, report zero (not invented data)
2. **Dedup before save** — check name + city against existing CRM
3. **Phone format** — validate Brazilian phone format (8 or 9 digits after DDD)
4. **At least 2 data points** — name + city minimum; name + phone preferred

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_research_batch_maps]] | sibling | 0.43 |
| [[bld_schema_model_registry]] | upstream | 0.40 |
| [[n06_schema_brand_config]] | upstream | 0.35 |
| [[bld_schema_experiment_tracker]] | upstream | 0.34 |
| [[tpl_research_batch_cnae]] | sibling | 0.32 |
| [[tpl_research_batch_marketplaces]] | sibling | 0.32 |
| [[tpl_research_batch_social]] | sibling | 0.32 |
| [[bld_schema_training_method]] | upstream | 0.32 |
| [[tpl_search_tool_business_discovery]] | sibling | 0.32 |
| [[bld_schema_tagline]] | upstream | 0.31 |
