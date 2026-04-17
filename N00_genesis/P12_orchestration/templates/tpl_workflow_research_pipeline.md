---
id: tpl_workflow_research_pipeline
kind: template
pillar: P12
title: "Workflow — Multi-Source Research Pipeline"
version: 1.0.0
quality: 9.2
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/P12 workflow artifacts
variables: [PIPELINE_NAME, STAGES, QUALITY_GATE, INDUSTRY, REGION, TARGET_COUNT]
density_score: 0.95
tags: [template, workflow, research-pipeline, multi-source, crm, instance-extraction]
tldr: "End-to-end research pipeline workflow — from discovery through enrichment to validated CRM output."
updated: "2026-04-13"
---

# Workflow: {{PIPELINE_NAME | default: 'Research Pipeline'}}

## Pipeline Architecture (5 Phases)

```
Phase 1          Phase 2          Phase 3          Phase 4          Phase 5
DISCOVER    →    EXTRACT     →    VALIDATE    →    ENRICH      →    CONSOLIDATE
(find URLs)      (get data)       (anti-fake)      (fill gaps)      (merge + score)
   │                │                │                │                │
   SERPER           FIRECRAWL        Rules engine     Cross-ref        Dedup
   EXA              Manual parse     Phone check      Reputation       Quality score
   Maps API         PDF extract      Tax ID check     Coords lookup    Final JSON
```

---

## Phase 1: Discover

| Step | Action | Tool | Output |
|:----:|--------|------|--------|
| 1.1 | Broad search by vertical × city | SERPER | URL list |
| 1.2 | Semantic search for niche sources | EXA | URL list |
| 1.3 | Maps search for physical businesses | Maps API | POI list |
| 1.4 | Directory index crawl | FIRECRAWL | URL list |

**Input**: `{{INDUSTRY}}` × `{{REGION}}` × verticals
**Output**: `discover_urls.json` — deduplicated URL list

---

## Phase 2: Extract

| Step | Action | Tool | Output |
|:----:|--------|------|--------|
| 2.1 | Structured scrape of business pages | FIRECRAWL | Raw contacts |
| 2.2 | Maps data extraction (phone, coords) | Maps API | Enriched POIs |
| 2.3 | Social profile parsing (bio, links) | SERPER + parse | Social contacts |
| 2.4 | Registry lookup (tax ID, status) | Registry API | Legal data |

**Input**: URL list from Phase 1
**Output**: `raw_contacts.json` — all fields, unvalidated

---

## Phase 3: Validate

| Rule | Check | Action on Fail |
|------|-------|---------------|
| Anti-fake | Cross-reference 2+ data points | **Reject** |
| Phone format | Country-specific phone validation | Flag for manual review |
| Tax ID | Algorithmic validation (CNPJ/EIN/VAT) | Remove invalid |
| Address | Geocode → confirm city matches | Flag if mismatch |
| Duplicate | Name + city fuzzy match | Merge |

**Quality gate**: `{{QUALITY_GATE | default: 'min_2_datapoints'}}`
**Output**: `validated_contacts.json`

---

## Phase 4: Enrich

| Source | Data Added | Priority |
|--------|-----------|:--------:|
| Review platforms | Rating, complaints, reputation | High |
| Professional registries | License, credentials | High |
| Social media | Followers, activity, engagement | Medium |
| Business intelligence | Revenue range, employees | Medium |
| Geocoding | Lat/lng from address | Low |

**Input**: validated contacts
**Output**: `enriched_contacts.json`

---

## Phase 5: Consolidate

```
1. Merge all batches (A-F or equivalent)
2. Final dedup pass (tax ID → name+city)
3. Quality scoring (0-100 per contact)
4. Tier assignment (S+/S/A/B/C)
5. Generate pipeline evidence report
6. Export final CRM JSON + CSV + dashboard data
```

**Output**: `crm_final.json`, `crm_final.csv`, `pipeline_evidence.md`

---

## Execution Config

```yaml
pipeline:
  name: {{PIPELINE_NAME}}
  industry: {{INDUSTRY}}
  region: {{REGION}}
  target: {{TARGET_COUNT}}
  batches: [A, B, C, D, E, F]
  waves:
    wave_1: [A, B, F]     # parallel — high volume
    wave_2: [C, D]         # parallel — social + marketplace
    wave_3: [E]            # sequential — enrichment
  nucleus: n01
  timeout_per_batch: 3600  # seconds
  quality_gate: {{QUALITY_GATE | default: 'min_2_datapoints'}}
```

---

## Metrics to Track

| Metric | Target | Formula |
|--------|:------:|---------|
| Total contacts | {{TARGET_COUNT}} | Count of unique records |
| Phone coverage | 60% | contacts_with_phone / total |
| Address coverage | 85% | contacts_with_address / total |
| Web presence | 65% | contacts_with_web / total |
| Tax ID coverage | 40% | contacts_with_taxid / total |
| Fake rate | **0%** | fabricated / total |
| Source diversity | 3+ | avg sources per contact |
