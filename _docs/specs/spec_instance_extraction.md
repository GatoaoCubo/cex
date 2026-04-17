---
id: spec_instance_extraction
kind: context_doc
title: "Instance Extraction: gato-ao-cubo → universal templates in main"
version: 1.0.0
quality: 9.0
created: 2026-04-07
purpose: Extract reusable patterns from gato-ao-cubo branch into main as {{mustache}} templates
density_score: 1.0
---

# Instance Extraction: Prototype → Archetype

## Principle

Gato³ was the first CEX instance. Every pattern built for it must become
a universal template in main. The instance fills the template. The template
lives in main. Private data stays in the branch.

## Three-Layer Separation

| Layer | Branch | Contains | Variables |
|-------|--------|----------|-----------|
| **Archetype** | main | Templates with {{mustache}} slots | Open — any brand fills them |
| **Instance** | gato-ao-cubo (or any brand branch) | Filled templates with real data | Closed — brand-specific |
| **Private** | gato-ao-cubo only (never in main) | Contacts, API keys, financial data | Never templated |

## Extraction Map: gato-ao-cubo → main templates

### 1. CRM Mission Pipeline

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `crm_mission/MISSION_PLAN.md` | `P12_orchestration/templates/tpl_crm_mission_plan.md` | {{BRAND_NAME}}, {{INDUSTRY}}, {{REGION}}, {{TARGET_COUNT}}, {{BATCH_SOURCES}} |
| `crm_mission/batch_a_diretorios_pet.md` | `P12_orchestration/templates/tpl_research_batch_directories.md` | {{INDUSTRY}}, {{REGION}}, {{DIRECTORY_SOURCES}}, {{SEARCH_QUERIES}} |
| `crm_mission/batch_b_google_maps.md` | `P12_orchestration/templates/tpl_research_batch_maps.md` | {{REGION}}, {{CATEGORIES}}, {{CITIES}}, {{RADIUS_KM}} |
| `crm_mission/batch_c_social_discovery.md` | `P12_orchestration/templates/tpl_research_batch_social.md` | {{INDUSTRY}}, {{PLATFORMS}}, {{HASHTAGS}}, {{REGION}} |
| `crm_mission/batch_d_marketplaces.md` | `P12_orchestration/templates/tpl_research_batch_marketplaces.md` | {{INDUSTRY}}, {{MARKETPLACES}}, {{SEARCH_TERMS}} |
| `crm_mission/batch_e_reputation.md` | `P12_orchestration/templates/tpl_research_batch_reputation.md` | {{PLATFORMS}}, {{REVIEW_SOURCES}}, {{MIN_RATING}} |
| `crm_mission/batch_f_cnae_deep.md` | `P12_orchestration/templates/tpl_research_batch_cnae.md` | {{CNAE_CODES}}, {{REGION}}, {{LEGAL_SOURCES}} |

### 2. Brand Config

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `.cex/brand/brand_config.yaml` | `_instances/_template/.cex/brand/brand_config.yaml` | ALL {{BRAND_*}} — already mostly exists |

### 3. Dashboard

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `N06_commercial/P05_output/dashboard.html` | `P05_output/templates/tpl_crm_dashboard.html` | {{BRAND_NAME}}, {{BRAND_COLORS.*}}, {{MAP_CENTER_LAT}}, {{MAP_CENTER_LNG}}, {{MAP_ZOOM}}, {{CRM_DATA_SOURCE}} |

### 4. CRM Admin Spec

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| CRM admin spec (commit 1744e921) | `_docs/specs/tpl_crm_admin_spec.md` | {{BRAND_NAME}}, {{DB_PROVIDER}}, {{TABLES}}, {{MAP_PROVIDER}}, {{AUTH_METHOD}} |

### 5. Research Pipeline Artifacts

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `p04_search_pet_business_discovery` | `P04_tools/templates/tpl_search_tool_business_discovery.md` | {{INDUSTRY}}, {{REGION}}, {{SEARCH_PROVIDERS}} |
| `p04_retr_multi_source_business_intel` | `P04_tools/templates/tpl_retriever_business_intel.md` | {{SOURCES}}, {{MERGE_STRATEGY}}, {{DEDUP_FIELDS}} |
| `p12_wf_crm_research_pipeline` | `P12_orchestration/templates/tpl_workflow_research_pipeline.md` | {{PIPELINE_NAME}}, {{STAGES}}, {{QUALITY_GATE}} |
| `p12_wf_gato_strategic_outreach` | `P12_orchestration/templates/tpl_workflow_strategic_outreach.md` | {{BRAND_NAME}}, {{CHANNELS}}, {{OUTREACH_STAGES}} |

### 6. Decision Manifest

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `decision_manifest_brand_{{BRAND_NAME}}.yaml` | `.cex/runtime/decisions/tpl_decision_manifest_brand.yaml` | {{BRAND_NAME}}, {{DECISIONS.*}} |

### 7. Learning Records Pattern

| Source (gato) | Template (main) | Variables |
|---------------|----------------|-----------|
| `emergent_autonomy_20260403/*.md` | `P11_feedback/templates/tpl_learning_record_autonomy.md` | {{MISSION}}, {{NUCLEUS}}, {{PHASE}}, {{FINDINGS}} |

## What NEVER goes to main

| Category | Files | Reason |
|----------|-------|--------|
| Contact data | `crm_batch_*.json`, `crm_enrich_*.json` | Private customer data |
| Brand config values | `brand_config.yaml` (filled) | Brand-specific identity |
| GDP decisions (filled) | `decision_manifest_brand_{{BRAND_NAME}}.yaml` | Brand-specific choices |
| API keys / secrets | Any `.env`, auth tokens | Security |

## The /init Flow (how a new brand uses templates)

```
User runs /init
  │
  ├── 1. Answers ~6 questions (name, domain, audience, tone, language, tagline)
  │
  ├── 2. brand_inject.py fills {{BRAND_*}} in all templates
  │     brand_config.yaml created with real values
  │
  ├── 3. git checkout -b <brand-slug>
  │     Branch created from main
  │
  ├── 4. Templates resolved → artifacts created
  │     tpl_crm_mission_plan.md → crm_mission/MISSION_PLAN.md
  │     tpl_crm_dashboard.html → dashboard.html
  │
  └── 5. N07 dispatches first mission
        Research pipeline runs with brand context
        CRM populates with real contacts
        Dashboard shows real data
```

## Implementation

| Step | Nucleus | What |
|------|---------|------|
| 1 | N01 | Read gato-ao-cubo artifacts, extract patterns, identify {{variables}} |
| 2 | N03 | Create templates in main with mustache variables |
| 3 | N05 | Update brand_inject.py to resolve new template variables |
| 4 | N04 | Document all new variables in template registry |
| 5 | N07 | Test: create mock brand, verify templates fill correctly |
