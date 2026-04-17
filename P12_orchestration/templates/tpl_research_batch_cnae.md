---
id: tpl_research_batch_cnae
kind: template
pillar: P12
title: "Research Batch — Tax Registry / Business Classification Deep Harvest"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_f_cnae_deep.md
variables: [CNAE_CODES, REGION, LEGAL_SOURCES, CITIES, SIC_CODES, NAICS_CODES, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, tax-registry, cnae, cnpj, crm, instance-extraction]
tldr: "Tax registry business discovery — systematic code × city sweep via government/open data sources."
updated: "2026-04-13"
---

# BATCH F — Tax Registry / Business Classification Deep Harvest

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_f_registry.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_F_REGISTRY'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (for dedup)

---

## Objective

Systematic sweep of **business classification code × city** combinations via government and open-data registries. This catches formally registered businesses that may not have online presence.

---

## Business Classification Codes

### Brazil (CNAE)

{{#CNAE_CODES}}
| CNAE | Description | Segment |
|------|-------------|---------|
{{#each}}
| {{code}} | {{description}} | `{{segment}}` |
{{/each}}
{{/CNAE_CODES}}

### USA (NAICS) — if applicable

{{#NAICS_CODES}}
| NAICS | Description | Segment |
|-------|-------------|---------|
{{#each}}
| {{code}} | {{description}} | `{{segment}}` |
{{/each}}
{{/NAICS_CODES}}

### EU (NACE) / UK (SIC) — if applicable

{{#SIC_CODES}}
| Code | Description | Segment |
|------|-------------|---------|
{{#each}}
| {{code}} | {{description}} | `{{segment}}` |
{{/each}}
{{/SIC_CODES}}

---

## Cities to Sweep

{{#CITIES}}
| City | Priority | Current Contacts |
|------|:--------:|:----------------:|
{{#each}}
| {{name}} | {{priority}} | {{current_count}} |
{{/each}}
{{/CITIES}}

---

## Systematic Method (per code × city)

```
Step 1: Open Data Registry
  {{LEGAL_SOURCES.primary}} → search by code + city + status=ACTIVE

Step 2: Backup Registry
  {{LEGAL_SOURCES.secondary}} → cross-reference

Step 3: Validate
  {{LEGAL_SOURCES.validation}} → confirm active status

For each result:
  Extract:
    - Legal name (razão social)
    - Trade name (nome fantasia)
    - Tax ID (CNPJ / EIN / VAT)
    - Classification code
    - Status (active/inactive)
    - Address
    - Start date
    - Legal form (MEI, LLC, Corp, etc.)
```

---

## Data Schema

```json
{
  "razao_social": "string",
  "nome_fantasia": "string",
  "cnpj": "string (or tax_id)",
  "cnae_principal": "string (or classification_code)",
  "situacao": "ATIVA",
  "endereco": "string",
  "cidade": "string (required)",
  "uf": "string",
  "data_abertura": "string (YYYY-MM-DD)",
  "natureza_juridica": "string",
  "porte": "MEI | ME | EPP | medium | large",
  "segmento": "string (derived from code)",
  "fonte": "{{registry_name}}"
}
```

---

## Quality Rules

1. **Active only** — skip dissolved/suspended businesses
2. **Dedup on tax ID** — unique identifier prevents duplicates
3. **Cross-reference** — merge with existing contacts by name+city
4. **Recency** — flag businesses opened < 1 year (may not be operational yet)
