---
id: tpl_crm_mission_plan
kind: template
pillar: P12
title: "CRM Full Harvest — Mission Plan Template"
version: 1.0.0
quality: 9.2
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/MISSION_PLAN.md
variables: [BRAND_NAME, INDUSTRY, REGION, TARGET_COUNT, BATCH_SOURCES, CITIES, PIPELINE_NAME]
density_score: 0.95
tags: [template, crm, mission-plan, research, instance-extraction]
tldr: "Universal CRM research mission plan — any brand fills {{mustache}} slots to orchestrate multi-batch contact discovery."
updated: "2026-04-13"
---

# Mission: {{PIPELINE_NAME}} — CRM Research Plan

## Objective

Build a CRM of **{{TARGET_COUNT}}+ real contacts** in the **{{INDUSTRY}}** sector across **{{REGION}}** using multi-source research batches. Zero fabricated data.

---

## Status Tracker

| Metric | Current | Target |
|--------|:-------:|:------:|
| Total contacts | 0 | {{TARGET_COUNT}}+ |
| With phone | 0% | 60% |
| With address | 0% | 85% |
| With email/web | 0% | 65% |
| With tax ID | 0% | 40% |
| Fakes | 0 | **0** |

---

## Batch Architecture

| Slot | Batch | Sources | Output | ROI Estimate |
|:----:|-------|---------|--------|:------------:|
| A | Directories | {{BATCH_SOURCES.directories}} | `crm_batch_a_directories.json` | +40-80 |
| B | Maps | Google Maps / {{BATCH_SOURCES.maps_provider}} | `crm_batch_b_maps.json` | +60-120 |
| C | Social | {{BATCH_SOURCES.social_platforms}} | `crm_batch_c_social.json` | +30-60 |
| D | Marketplaces | {{BATCH_SOURCES.marketplaces}} | `crm_batch_d_marketplaces.json` | +10-30 |
| E | Reputation | {{BATCH_SOURCES.reputation_sources}} | `crm_batch_e_reputation.json` | +10-20 |
| F | Tax Registry | {{BATCH_SOURCES.tax_registry}} | `crm_batch_f_registry.json` | +30-50 |

---

## Wave Execution Plan

### Wave 1 — High-Volume Discovery (Parallel: A + B + F)

These are the bulk-discovery batches that yield the most contacts per hour of research. Run in parallel via N01 slots.

```bash
bash _spawn/dispatch.sh solo n01 "BATCH_A_DIRECTORIES"
bash _spawn/dispatch.sh solo n01 "BATCH_B_MAPS"
bash _spawn/dispatch.sh solo n01 "BATCH_F_REGISTRY"
```

### Wave 2 — Social + Marketplace Discovery (Parallel: C + D)

Informal businesses and digitally active sellers. Lower volume but higher digital maturity signals.

```bash
bash _spawn/dispatch.sh solo n01 "BATCH_C_SOCIAL"
bash _spawn/dispatch.sh solo n01 "BATCH_D_MARKETPLACES"
```

### Wave 3 — Enrichment + Reputation (Sequential: E)

Enrichment of existing contacts with reputation data, professional registrations, and quality signals.

```bash
bash _spawn/dispatch.sh solo n01 "BATCH_E_REPUTATION"
```

---

## Post-Grid: Merge + Consolidate

```bash
# 1. Dry-run check
python N01_research/P05_output/data/merge_batches.py --all --dry-run

# 2. Merge
python N01_research/P05_output/data/merge_batches.py --all

# 3. Commit
git add N01_research/P05_output/data/ && git commit -m "[N07] merge batches → {N} contacts"
```

---

## Cities ({{REGION}})

{{#CITIES}}
| City | Priority | Current Contacts |
|------|:--------:|:----------------:|
{{#each}}
| {{name}} | {{priority}} | {{current_count}} |
{{/each}}
{{/CITIES}}

---

## Quality Gates

1. **Anti-fake**: Every contact must have at least 2 verifiable data points
2. **Dedup**: Match on normalized name + city before merge
3. **Format**: All outputs as JSON following `P05_output/p05_rf_crm_output_standard.md`
4. **Validation**: Phone format, tax ID algorithm, email domain check

---

## Brand Context

- **Brand**: {{BRAND_NAME}}
- **Industry**: {{INDUSTRY}}
- **Region**: {{REGION}}
- **Target**: {{TARGET_COUNT}}+ contacts
- **Use case**: B2B prospecting, partnership development, local market intelligence
