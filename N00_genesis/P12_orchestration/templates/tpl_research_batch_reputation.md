---
id: tpl_research_batch_reputation
kind: template
pillar: P12
title: "Research Batch — Reputation + Professional Registry Enrichment"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_e_reputation.md
variables: [PLATFORMS, REVIEW_SOURCES, MIN_RATING, PROFESSIONAL_REGISTRY, INDUSTRY, CITIES, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, reputation, enrichment, professional-registry, crm, instance-extraction]
tldr: "Reputation enrichment + professional registry discovery — add quality signals and discover regulated businesses."
updated: "2026-04-13"
related:
  - tpl_workflow_research_pipeline
  - tpl_research_batch_directories
  - tpl_research_batch_marketplaces
  - tpl_research_batch_cnae
  - tpl_research_batch_maps
  - tpl_research_batch_social
  - tpl_crm_mission_plan
  - tpl_search_tool_business_discovery
  - bld_schema_model_registry
  - tpl_retriever_business_intel
---

# BATCH E — Reputation + Professional Registry

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_e_reputation.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_E_REPUTATION'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (enrichment target + dedup)

---

## Objective

Two functions:
1. **Discovery**: Find new businesses via professional registries and regulatory databases
2. **Enrichment**: Add reputation data to existing contacts (reviews, ratings, complaints)

---

## Source 1: Review Platforms (Enrichment)

{{#REVIEW_SOURCES}}
### {{name}}

```
For top {{batch_size | default: '50'}} existing contacts (with business name):
  SERPER: site:{{domain}} "{{business_name}}"

If page found:
  FIRECRAWL: {{result_url}}

  Extract:
    - Overall score ({{score_range}})
    - Response rate (%)
    - Return rate (% would do business again)
    - Complaint count (last 12 months)
    - Status: {{status_labels}}
```

**No listing = positive signal for small businesses** — means they're small/local without complaint volume. Mark as: `review_status: "no_listing"`.

{{/REVIEW_SOURCES}}

---

## Source 2: Professional Registries (Discovery)

{{#PROFESSIONAL_REGISTRY}}
### {{name}} ({{acronym}})

```
{{#queries}}
SERPER: site:{{domain}} "{{search_term}}" "{{city}}"
EXA: "{{registry_name}} {{INDUSTRY}} {{city}}"
{{/queries}}

FIRECRAWL: {{public_lookup_url}} (public consultation section)

Extract:
  - Business name
  - Registration number
  - Address
  - Specialty / license type
  - Active status
```

{{/PROFESSIONAL_REGISTRY}}

---

## Source 3: Business Intelligence Platforms

| Platform | Type | Data Available |
|----------|------|----------------|
| {{PLATFORMS.business_intel_1 | default: 'Econodata'}} | B2B intelligence | Company size, revenue range, employees |
| {{PLATFORMS.business_intel_2 | default: 'LinkedIn Sales Navigator'}} | Professional network | Decision makers, company info |

---

## Data Schema (Enrichment Fields)

```json
{
  "review_source": "string",
  "review_score": "float",
  "review_response_rate": "float (0-1)",
  "review_complaint_count": "integer",
  "review_status": "string (excellent|good|regular|poor|no_listing)",
  "professional_registry": "string (registry name)",
  "registry_number": "string",
  "registry_active": "boolean",
  "registry_specialty": "string"
}
```

---

## Quality Rules

1. **Match by normalized name** — fuzzy match OK (Levenshtein < 3)
2. **Enrichment only** — don't overwrite existing verified data
3. **Min rating filter**: only flag contacts with score < {{MIN_RATING | default: '3.0'}} for review
4. **Registry = high trust** — contacts found via professional registry get trust boost

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_workflow_research_pipeline]] | sibling | 0.32 |
| [[tpl_research_batch_directories]] | sibling | 0.31 |
| [[tpl_research_batch_marketplaces]] | sibling | 0.29 |
| [[tpl_research_batch_cnae]] | sibling | 0.28 |
| [[tpl_research_batch_maps]] | sibling | 0.28 |
| [[tpl_research_batch_social]] | sibling | 0.26 |
| [[tpl_crm_mission_plan]] | sibling | 0.24 |
| [[tpl_search_tool_business_discovery]] | sibling | 0.23 |
| [[bld_schema_model_registry]] | upstream | 0.22 |
| [[tpl_retriever_business_intel]] | sibling | 0.21 |
