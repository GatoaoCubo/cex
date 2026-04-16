---
id: kc_instance_variable_registry
kind: knowledge-card
domain: meta
pillar: P01
version: "1.0"
created: "2026-04-07"
updated: "2026-04-07"
quality: 9.1
tags: [instance, variables, templates, mustache, extraction, registry, N01]
tldr: "Registry of 67 {{mustache}} variables extracted from gato-ao-cubo branch. 7 categories, 44 BRAND_* (existing) + 23 new CRM/pipeline/dashboard vars. Maps instance → archetype separation."
density_score: 1.0
---

# Instance Variable Registry

> Extracted by N01 from `gato-ao-cubo` branch analysis (2026-04-07).
> Source spec: `_docs/specs/spec_instance_extraction.md`

## Executive Summary

| Metric | Count |
|--------|-------|
| Total unique variables | 67 |
| Existing `BRAND_*` (already in `brand_config_template.yaml`) | 44 |
| **New instance variables** (need templates) | **23** |
| Categories | 7 |
| Branch-only files (private, never templated) | ~30 |
| Compiled artifacts unique to gato-ao-cubo | 21 |
| Hardcoded instance references found | 60+ occurrences |

## Methodology

Two approaches compared:

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **A. Grep-based extraction** (diff + pattern match) | Fast, exhaustive, catches all hardcoded strings | False positives, misses semantic variables | Used for discovery |
| **B. Spec-guided mapping** (spec_instance_extraction.md) | Structured, 7 categories pre-defined, N07-validated | May miss emergent patterns not in spec | Used for classification |

**Hybrid used**: Grep found candidates → Spec validated categories → Manual analysis resolved ambiguities.

## Category 1: BRAND_* Variables (44 — already registered)

These exist in `brand_config_template.yaml` and are documented in `kc_brand_variable_audit.md`.
No duplication here — see that KC for the full list.

**Key insight**: The gato-ao-cubo branch fills ALL 44 with real data. The template in main has `{{BRAND_*}}` placeholders. This layer is **solved**.

## Category 2: CRM Mission Pipeline (12 new variables)

Extracted from: `crm_mission/MISSION_PLAN.md`, `batch_a` through `batch_f`

| Variable | Type | Example (gato) | Template Target |
|----------|------|-----------------|-----------------|
| `{{INDUSTRY}}` | string | `"pet"` | `tpl_crm_mission_plan.md` |
| `{{TARGET_COUNT}}` | int | `500` | `tpl_crm_mission_plan.md` |
| `{{BATCH_SOURCES}}` | list | `["directories", "google_maps", "social", "marketplaces", "reputation", "cnae"]` | `tpl_crm_mission_plan.md` |
| `{{DIRECTORY_SOURCES}}` | list | `["guialocal", "telelistas", "ifood"]` | `tpl_research_batch_directories.md` |
| `{{SEARCH_QUERIES}}` | list | `["pet shop {cidade}", "loja pet {cidade}"]` | `tpl_research_batch_directories.md` |
| `{{CATEGORIES}}` | list | `["pet_shop", "clinica_vet", "banho_tosa", "hotel_pet"]` | `tpl_research_batch_maps.md` |
| `{{CITIES}}` | list | `["São Caetano do Sul", "Santo André", "São Bernardo"]` | `tpl_research_batch_maps.md` |
| `{{RADIUS_KM}}` | int | `50` | `tpl_research_batch_maps.md` |
| `{{HASHTAGS}}` | list | `["#petshop", "#gatosdobrasil", "#bemestarfelino"]` | `tpl_research_batch_social.md` |
| `{{MARKETPLACES}}` | list | `["iFood", "Rappi", "Mercado Livre", "Shopee"]` | `tpl_research_batch_marketplaces.md` |
| `{{CNAE_CODES}}` | list | `["4789-0/04", "7500-1/00", "9609-2/08"]` | `tpl_research_batch_cnae.md` |
| `{{LEGAL_SOURCES}}` | list | `["Casa dos Dados", "CNPJ.biz", "ReceitaWS"]` | `tpl_research_batch_cnae.md` |

### Inheritance Note

`{{REGION}}` and `{{PLATFORMS}}` overlap with `BRAND_REGION` and `BRAND_CHANNELS`. Resolution:
- `{{REGION}}` → derives from `BRAND_REGION` + `BRAND_EXPANSION_RINGS`
- `{{PLATFORMS}}` → derives from `BRAND_CHANNELS` (subset: social only)

## Category 3: Dashboard Rendering (4 new variables)

Extracted from: `N02_marketing/output/{{BRAND_NAME}}_crm_dashboard.html`, `N06_commercial/output/`

| Variable | Type | Example (gato) | Template Target |
|----------|------|-----------------|-----------------|
| `{{MAP_CENTER_LAT}}` | float | `-23.6235` | `tpl_crm_dashboard.html` |
| `{{MAP_CENTER_LNG}}` | float | `-46.5519` | `tpl_crm_dashboard.html` |
| `{{MAP_ZOOM}}` | int | `12` | `tpl_crm_dashboard.html` |
| `{{CRM_DATA_SOURCE}}` | enum | `"inline"` / `"api_endpoint"` | `tpl_crm_dashboard.html` |

### Derivation Candidates

`MAP_CENTER_LAT/LNG` could auto-derive from `BRAND_HQ` via geocoding. Worth implementing in `brand_inject.py`.

## Category 4: CRM Admin Infrastructure (4 new variables)

Extracted from: commit `1744e921` (CRM Admin spec)

| Variable | Type | Example (gato) | Template Target |
|----------|------|-----------------|-----------------|
| `{{DB_PROVIDER}}` | string | `"supabase"` | `tpl_crm_admin_spec.md` |
| `{{TABLES}}` | list | `["contatos", "interacoes", "segmentos"]` | `tpl_crm_admin_spec.md` |
| `{{MAP_PROVIDER}}` | string | `"leaflet_osm"` | `tpl_crm_admin_spec.md` |
| `{{AUTH_METHOD}}` | string | `"supabase_auth"` | `tpl_crm_admin_spec.md` |

## Category 5: Research Pipeline (3 new variables)

Extracted from: `p04_search_pet_business_discovery`, `p12_wf_crm_research_pipeline`

| Variable | Type | Example (gato) | Template Target |
|----------|------|-----------------|-----------------|
| `{{SEARCH_PROVIDERS}}` | list | `["SERPER", "FIRECRAWL", "EXA"]` | `tpl_search_tool_business_discovery.md` |
| `{{MERGE_STRATEGY}}` | string | `"dedup_by_cnpj"` | `tpl_retriever_business_intel.md` |
| `{{DEDUP_FIELDS}}` | list | `["cnpj", "phone", "name"]` | `tpl_retriever_business_intel.md` |

## Category 6: Outreach / Commercial (not new — composites)

Extracted from: `p12_wf_gato_strategic_outreach`, `p04_cm_{{BRAND_NAME}}_revenue_strategy`

These are **composite** — they combine existing BRAND_* vars:

| Pattern | Composes From | Template Target |
|---------|---------------|-----------------|
| Outreach segments | `{{CATEGORIES}}` + `{{INDUSTRY}}` | `tpl_workflow_strategic_outreach.md` |
| Channel strategy | `{{BRAND_CHANNELS}}` | `tpl_workflow_strategic_outreach.md` |
| Revenue model | `{{BRAND_TIERS}}` + `{{BRAND_PRICING_MODEL}}` | `tpl_decision_manifest_brand.yaml` |

**No new atomic variables needed** — the 7 category in the spec resolves to composites of Cat. 1 + Cat. 2.

## Category 7: Learning Records (not variables — structural pattern)

Extracted from: `.cex/learning_records/emergent_autonomy_20260403/`

These are **not mustache-templated**. They are runtime artifacts that follow a structural pattern:

```
.cex/learning_records/{{MISSION_SLUG}}/
  ├── {{PHASE}}_{{DOMAIN}}_{{NUCLEUS}}.md
  └── signal_{{NUCLEUS}}_{{TIMESTAMP}}.json
```

Template already implicit in the file-naming convention. **No variable injection needed** — just document the convention.

## Private Data (NEVER templated, NEVER in main)

| Category | Files (gato-ao-cubo) | Reason |
|----------|----------------------|--------|
| Contact JSONs | `crm_batch_*.json`, `crm_enrich_*.json` | Private customer data |
| Filled brand_config | `.cex/brand/brand_config.yaml` (with real values) | Brand-specific identity |
| Canva tokens | `.cex/brand/canva_token.json` | API secret |
| GDP decisions (filled) | `decision_manifest_brand_{{BRAND_NAME}}.yaml` | Brand-specific choices |
| Overnight logs | `.cex/overnight/*.log` | Session-specific runtime |
| Quality audits | `.cex/quality/audit_*.json` | Instance-specific scores |
| Signal archives | `.cex/archive/signals_*/*.json` | Runtime state |

## Consolidated New Variable Map (23 vars)

```yaml
# instance_config.yaml — new section proposed for brand_config_template.yaml
# Section: crm_pipeline
crm_pipeline:
  INDUSTRY: "{{INDUSTRY}}"                     # e.g., "pet", "food", "beauty"
  TARGET_COUNT: "{{TARGET_COUNT}}"             # e.g., 500
  BATCH_SOURCES: "{{BATCH_SOURCES}}"           # ["directories", "google_maps", ...]
  DIRECTORY_SOURCES: "{{DIRECTORY_SOURCES}}"   # ["guialocal", "ifood", ...]
  SEARCH_QUERIES: "{{SEARCH_QUERIES}}"         # ["pet shop {cidade}", ...]
  CATEGORIES: "{{CATEGORIES}}"                 # ["pet_shop", "clinica_vet", ...]
  CITIES: "{{CITIES}}"                         # ["São Caetano", "Santo André", ...]
  RADIUS_KM: "{{RADIUS_KM}}"                  # 50
  HASHTAGS: "{{HASHTAGS}}"                     # ["#petshop", ...]
  MARKETPLACES: "{{MARKETPLACES}}"             # ["iFood", "Mercado Livre", ...]
  CNAE_CODES: "{{CNAE_CODES}}"                 # ["4789-0/04", ...]
  LEGAL_SOURCES: "{{LEGAL_SOURCES}}"           # ["Casa dos Dados", ...]

# Section: dashboard
dashboard:
  MAP_CENTER_LAT: "{{MAP_CENTER_LAT}}"         # -23.6235
  MAP_CENTER_LNG: "{{MAP_CENTER_LNG}}"         # -46.5519
  MAP_ZOOM: "{{MAP_ZOOM}}"                     # 12
  CRM_DATA_SOURCE: "{{CRM_DATA_SOURCE}}"       # "inline" | "api_endpoint"

# Section: infrastructure
infrastructure:
  DB_PROVIDER: "{{DB_PROVIDER}}"               # "supabase"
  TABLES: "{{TABLES}}"                         # ["contatos", "interacoes", ...]
  MAP_PROVIDER: "{{MAP_PROVIDER}}"             # "leaflet_osm"
  AUTH_METHOD: "{{AUTH_METHOD}}"               # "supabase_auth"

# Section: research
research:
  SEARCH_PROVIDERS: "{{SEARCH_PROVIDERS}}"     # ["SERPER", "FIRECRAWL", "EXA"]
  MERGE_STRATEGY: "{{MERGE_STRATEGY}}"         # "dedup_by_cnpj"
  DEDUP_FIELDS: "{{DEDUP_FIELDS}}"             # ["cnpj", "phone", "name"]
```

## Hardcoded Patterns Found (must be eliminated)

| Pattern | Occurrences | Replace With |
|---------|-------------|-------------|
| `GATO³` / `{{BRAND_NAME}}` / `{{BRAND_NAME}}` | 40+ | `{{BRAND_NAME}}` |
| `ABC Paulista` | 15+ | `{{BRAND_REGION}}` |
| `pet` (as industry literal) | 30+ | `{{INDUSTRY}}` |
| `{{BRAND_EMAIL}}` | 2 | `{{BRAND_EMAIL}}` (new) |
| `{{BRAND_DOMAIN}}` | 4 | `{{BRAND_DOMAIN}}` (new) |
| `-23.62` / `-46.55` (coords) | 2 | `{{MAP_CENTER_LAT/LNG}}` |
| `São Caetano do Sul` (as HQ) | 5 | `{{BRAND_HQ}}` |
| `B-C+` (income class) | 3 | `{{BRAND_ICP_INCOME}}` |

### 2 Additional Variables Discovered (not in spec)

| Variable | Discovered In | Reason |
|----------|---------------|--------|
| `{{BRAND_EMAIL}}` | decision_manifest, canva_token | Contact email used in pipelines |
| `{{BRAND_DOMAIN}}` | brand_config (logo_url, favicon_url) | Web domain (derivable from LOGO_URL) |

**Total**: 23 new + 2 discovered = **25 new variables** beyond the 44 BRAND_*.

## Implementation Priority

| Priority | Variables | Nucleus | Effort |
|----------|-----------|---------|--------|
| P0 — immediate | `INDUSTRY`, `CATEGORIES`, `CITIES`, `TARGET_COUNT` | N03 | Low — used in every CRM template |
| P1 — high | `MAP_CENTER_*`, `MAP_ZOOM`, `CRM_DATA_SOURCE` | N03 | Medium — dashboard template |
| P1 — high | `CNAE_CODES`, `LEGAL_SOURCES`, `SEARCH_PROVIDERS` | N03 | Medium — research templates |
| P2 — medium | `DB_PROVIDER`, `TABLES`, `MAP_PROVIDER`, `AUTH_METHOD` | N05 | Medium — infra templates |
| P3 — low | `BRAND_EMAIL`, `BRAND_DOMAIN` | N03 | Low — derivable from existing config |

## Alternatives Considered

### Alt 1: Flat BRAND_* namespace (extend existing)
Add all 25 vars as `BRAND_INDUSTRY`, `BRAND_TARGET_COUNT`, etc. within `brand_config.yaml`.

**Pros**: Single config file, existing injection pipeline works.
**Cons**: Bloats brand config with CRM-specific fields irrelevant to non-CRM brands. Mixes identity with operational config.

### Alt 2: Separate `instance_config.yaml` (recommended)
New file `.cex/instance/instance_config.yaml` with 4 sections (crm_pipeline, dashboard, infrastructure, research).

**Pros**: Clean separation — brand identity ≠ operational config. New brands only fill what they need. `brand_inject.py` loads both files.
**Cons**: Two config files to maintain. Requires extending `brand_inject.py`.

### Alt 3: Per-template frontmatter defaults
Each template file carries `defaults:` in its frontmatter. Unfilled vars use the default.

**Pros**: Self-documenting templates. No central config bloat.
**Cons**: Defaults scattered across 20+ files. Hard to audit. Breaks the "single source of truth" principle.

**Recommendation**: **Alt 2** — `instance_config.yaml` separates identity from operations. The `| default:` syntax (already in `brand_inject.py`) handles missing values for brands that don't use CRM.

## Cross-References

| Document | Relationship |
|----------|-------------|
| `kc_brand_variable_audit.md` | Sister KC — covers the 44 BRAND_* vars |
| `spec_instance_extraction.md` | Parent spec — defines the 7-category framework |
| `brand_config_template.yaml` | Identity variables (existing) |
| `brand_inject.py` | Injection engine (needs extension for instance_config) |
| `brand_propagate.py` | Propagation engine (needs instance_config routing) |

## Verification Checklist

- [ ] All 23+2 new vars documented with types and examples
- [ ] No BRAND_* duplication (checked against kc_brand_variable_audit)
- [ ] Private data categories listed with rationale
- [ ] Implementation priority assigned
- [ ] 3 alternatives compared with recommendation
- [ ] Cross-references to related KCs and specs
