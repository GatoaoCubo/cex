---
id: kc_template_catalog
kind: knowledge-card
domain: meta
pillar: P01
version: "1.0"
created: "2026-04-07"
updated: "2026-04-07"
quality: 9.1
tags: [templates, catalog, registry, mustache, pillars, instance-extraction, N04]
tldr: "Master catalog of all 123 CEX templates across 12 pillars + 3 non-pillar. 105 core kind templates + 15 instance-extraction templates (from gato-ao-cubo) + 3 non-pillar. Documents variable dependencies, resolution chains, and /init flow."
density_score: 1.0
---

# Template Catalog — Complete CEX Template Inventory

> Compiled by N04 from N01's variable registry + N03's 15 new templates + full pillar scan.
> Source: `spec_instance_extraction.md`, `kc_instance_variable_registry.md`, `tpl_template_registry.md`

## Executive Summary

| Metric | Count |
|--------|------:|
| **Total templates** | **123** |
| Pillar templates (core kinds) | 105 |
| Instance-extraction templates (new) | 15 |
| Non-pillar templates | 3 |
| Pillars covered | 12/12 |
| Unique instance variables (new) | 25 |
| Unique BRAND_* variables (existing) | 44 |

---

## 1. Template Inventory — Core Kind Templates (105)

These are the structural templates — one per kind — used to scaffold any CEX artifact.

### P01 Knowledge (9 templates)

| Template | Kind | Variables |
|----------|------|-----------|
| `tpl_chunk_strategy.md` | chunk-strategy | Structural (frontmatter-only) |
| `tpl_context_doc.md` | context-doc | Structural |
| `tpl_embedding_config.md` | embedding-config | Structural |
| `tpl_few_shot_example.md` | few-shot-example | Structural |
| `tpl_glossary_entry.md` | glossary-entry | Structural |
| `tpl_knowledge_card.md` | knowledge-card | Structural |
| `tpl_knowledge_card_kind.md` | knowledge-card (kind) | Structural |
| `tpl_rag_source.md` | rag-source | Structural |
| `tpl_retriever_config.md` | retriever-config | Structural |

### P02 Model (11 templates)

| Template | Kind |
|----------|------|
| `tpl_agent.md` | agent |
| `tpl_agent_package.md` | agent-package |
| `tpl_axiom.md` | axiom |
| `tpl_boot_config.md` | boot-config |
| `tpl_fallback_chain.md` | fallback-chain |
| `tpl_handoff_protocol.md` | handoff-protocol |
| `tpl_lens.md` | lens |
| `tpl_memory_scope.md` | memory-scope |
| `tpl_mental_model.md` | mental-model |
| `tpl_model_card.md` | model-card |
| `tpl_router.md` | router |

### P03 Prompt (7 templates)

| Template | Kind |
|----------|------|
| `tpl_action_prompt.md` | action-prompt |
| `tpl_chain.md` | chain |
| `tpl_constraint_spec.md` | constraint-spec |
| `tpl_instruction.md` | instruction |
| `tpl_prompt_template.md` | prompt-template |
| `tpl_prompt_version.md` | prompt-version |
| `tpl_system_prompt.md` | system-prompt |

### P04 Tools (22 core templates)

| Template | Kind |
|----------|------|
| `tpl_api_client.md` | api-client |
| `tpl_audio_tool.md` | audio-tool |
| `tpl_browser_tool.md` | browser-tool |
| `tpl_cli_tool.md` | cli-tool |
| `tpl_code_executor.md` | code-executor |
| `tpl_computer_use.md` | computer-use |
| `tpl_daemon.md` | daemon |
| `tpl_db_connector.md` | db-connector |
| `tpl_document_loader.md` | document-loader |
| `tpl_function_def.md` | function-def |
| `tpl_hook.md` | hook |
| `tpl_mcp_server.md` | mcp-server |
| `tpl_notifier.md` | notifier |
| `tpl_plugin.md` | plugin |
| `tpl_research_pipeline.md` | research-pipeline |
| `tpl_retriever.md` | retriever |
| `tpl_search_tool.md` | search-tool |
| `tpl_social_publisher.md` | social-publisher |
| `tpl_software_project.md` | software-project |
| `tpl_supabase_data_layer.md` | supabase-data-layer |
| `tpl_vision_tool.md` | vision-tool |
| `tpl_webhook.md` | webhook |

### P05 Output (4 core templates)

| Template | Kind |
|----------|------|
| `tpl_formatter.md` | formatter |
| `tpl_output_validator.md` | output-validator |
| `tpl_parser.md` | parser |
| `tpl_response_format.md` | response-format |

### P06 Schema (6 templates)

| Template | Kind |
|----------|------|
| `tpl_enum_def.md` | enum-def |
| `tpl_input_schema.md` | input-schema |
| `tpl_interface.md` | interface |
| `tpl_type_def.md` | type-def |
| `tpl_validation_schema.md` | validation-schema |
| `tpl_validator.md` | validator |

### P07 Evals (10 templates)

| Template | Kind |
|----------|------|
| `tpl_benchmark.md` | benchmark |
| `tpl_e2e_eval.md` | e2e-eval |
| `tpl_eval_dataset.md` | eval-dataset |
| `tpl_golden_test.md` | golden-test |
| `tpl_llm_judge.md` | llm-judge |
| `tpl_red_team_eval.md` | red-team-eval |
| `tpl_regression_check.md` | regression-check |
| `tpl_scoring_rubric.md` | scoring-rubric |
| `tpl_smoke_eval.md` | smoke-eval |
| `tpl_unit_eval.md` | unit-eval |

### P08 Architecture (8 templates)

| Template | Kind |
|----------|------|
| `tpl_agent_card.md` | agent-card |
| `tpl_component_map.md` | component-map |
| `tpl_decision_record.md` | decision-record |
| `tpl_diagram.md` | diagram |
| `tpl_invariant.md` | invariant |
| `tpl_naming_rule.md` | naming-rule |
| `tpl_pattern.md` | pattern |
| `tpl_supervisor.md` | supervisor |

### P09 Config (7 templates)

| Template | Kind |
|----------|------|
| `tpl_env_config.md` | env-config |
| `tpl_feature_flag.md` | feature-flag |
| `tpl_path_config.md` | path-config |
| `tpl_permission.md` | permission |
| `tpl_rate_limit_config.md` | rate-limit-config |
| `tpl_runtime_rule.md` | runtime-rule |
| `tpl_secret_config.md` | secret-config |

### P10 Memory (6 templates)

| Template | Kind |
|----------|------|
| `tpl_brain_index.md` | brain-index |
| `tpl_entity_memory.md` | entity-memory |
| `tpl_learning_record.md` | learning-record |
| `tpl_memory_summary.md` | memory-summary |
| `tpl_runtime_state.md` | runtime-state |
| `tpl_session_state.md` | session-state |

### P11 Feedback (7 core templates)

| Template | Kind |
|----------|------|
| `tpl_bugloop.md` | bugloop |
| `tpl_content_monetization.md` | content-monetization |
| `tpl_guardrail.md` | guardrail |
| `tpl_lifecycle_rule.md` | lifecycle-rule |
| `tpl_optimizer.md` | optimizer |
| `tpl_quality_gate.md` | quality-gate |
| `tpl_reward_signal.md` | reward-signal |

### P12 Orchestration (8 core templates)

| Template | Kind |
|----------|------|
| `tpl_checkpoint.md` | checkpoint |
| `tpl_dag.md` | dag |
| `tpl_dispatch_rule.md` | dispatch-rule |
| `tpl_handoff.md` | handoff |
| `tpl_schedule.md` | schedule |
| `tpl_signal.md` | signal |
| `tpl_spawn_config.md` | spawn-config |
| `tpl_workflow.md` | workflow |

---

## 2. Instance-Extraction Templates (15 new — from gato-ao-cubo)

Created by N03 (commit `74bb7481`). These are **brand-parametric** — filled by `brand_inject.py` during `/init`.

### Category A: CRM Mission Pipeline (7 templates) — P12

| Template | Path | Variables | Origin (gato) |
|----------|------|-----------|----------------|
| `tpl_crm_mission_plan.md` | `P12_orchestration/templates/` | BRAND_NAME, INDUSTRY, REGION, TARGET_COUNT, BATCH_SOURCES, CITIES, PIPELINE_NAME | `crm_mission/MISSION_PLAN.md` |
| `tpl_research_batch_directories.md` | `P12_orchestration/templates/` | INDUSTRY, REGION, DIRECTORY_SOURCES, SEARCH_QUERIES, CITIES, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_a_diretorios_pet.md` |
| `tpl_research_batch_maps.md` | `P12_orchestration/templates/` | REGION, CATEGORIES, CITIES, RADIUS_KM, MAPS_PROVIDER, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_b_google_maps.md` |
| `tpl_research_batch_social.md` | `P12_orchestration/templates/` | INDUSTRY, PLATFORMS, HASHTAGS, REGION, CITIES, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_c_social_discovery.md` |
| `tpl_research_batch_marketplaces.md` | `P12_orchestration/templates/` | INDUSTRY, MARKETPLACES, SEARCH_TERMS, CITIES, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_d_marketplaces.md` |
| `tpl_research_batch_reputation.md` | `P12_orchestration/templates/` | PLATFORMS, REVIEW_SOURCES, MIN_RATING, PROFESSIONAL_REGISTRY, INDUSTRY, CITIES, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_e_reputation.md` |
| `tpl_research_batch_cnae.md` | `P12_orchestration/templates/` | CNAE_CODES, REGION, LEGAL_SOURCES, CITIES, SIC_CODES, NAICS_CODES, OUTPUT_FILE, SIGNAL_TAG | `crm_mission/batch_f_cnae_deep.md` |

### Category B: Dashboard (1 template) — P05

| Template | Path | Variables | Origin (gato) |
|----------|------|-----------|----------------|
| `tpl_crm_dashboard.html` | `P05_output/templates/` | BRAND_NAME, BRAND_COLORS.*, MAP_CENTER_LAT, MAP_CENTER_LNG, MAP_ZOOM, CRM_DATA_SOURCE | `N06_commercial/P05_output/dashboard.html` |

### Category C: Research Pipeline (2 templates) — P04

| Template | Path | Variables | Origin (gato) |
|----------|------|-----------|----------------|
| `tpl_search_tool_business_discovery.md` | `P04_tools/templates/` | INDUSTRY, REGION, SEARCH_PROVIDERS, VERTICALS, CITIES | `p04_search_pet_business_discovery` |
| `tpl_retriever_business_intel.md` | `P04_tools/templates/` | SOURCES, MERGE_STRATEGY, DEDUP_FIELDS, INDUSTRY, REGION | `p04_retr_multi_source_business_intel` |

### Category D: Workflows (3 templates) — P12

| Template | Path | Variables | Origin (gato) |
|----------|------|-----------|----------------|
| `tpl_workflow_research_pipeline.md` | `P12_orchestration/templates/` | PIPELINE_NAME, STAGES, QUALITY_GATE, INDUSTRY, REGION, TARGET_COUNT | `p12_wf_crm_research_pipeline` |
| `tpl_workflow_strategic_outreach.md` | `P12_orchestration/templates/` | BRAND_NAME, CHANNELS, OUTREACH_STAGES, SEGMENTS, TARGET_COUNT, REGION | `p12_wf_gato_strategic_outreach` |
| `tpl_crm_pipeline_evidence.md` | `P12_orchestration/templates/` | BRAND_NAME, PIPELINE_NAME, BATCHES, FINAL_STATS, CITIES, TARGET_COUNT | (pipeline evidence pattern) |

### Category E: Learning + Config (2 templates) — P11, P12

| Template | Path | Variables | Origin (gato) |
|----------|------|-----------|----------------|
| `tpl_learning_record_autonomy.md` | `P11_feedback/templates/` | MISSION, NUCLEUS, PHASE, FINDINGS, METRICS, RECOMMENDATIONS | `emergent_autonomy_20260403/*.md` |
| `tpl_brand_context_nucleus.md` | `P12_orchestration/templates/` | NUCLEUS_ID, NUCLEUS_NAME, BRAND_* | `N01_research/P09_config/brand_context.md` |

---

## 3. Non-Pillar Templates (3)

| Template | Path | Variables | Purpose |
|----------|------|-----------|---------|
| `tpl_decision_manifest_brand.yaml` | `.cex/runtime/decisions/` | BRAND_NAME, DECISIONS.*, CONSTRAINTS.* | GDP decision manifest per brand |
| `tpl_crm_admin_spec.md` | `_docs/specs/` | BRAND_NAME, DB_PROVIDER, TABLES, MAP_PROVIDER, AUTH_METHOD, FRAMEWORK | CRM admin panel specification |
| `tpl_template_registry.md` | `_docs/specs/` | (meta — no injection) | N03's template index (this catalog supersedes it) |

---

## 4. Variable Dependency Graph

### Resolution Chain

```
Template file (tpl_*.md)
  └─ {{VARIABLE}} in body text
       └─ brand_inject.py reads config
            ├─ .cex/brand/brand_config.yaml    → BRAND_* (44 vars)
            ├─ .cex/instance/instance_config.yaml → CRM/pipeline/infra (23 vars)  [proposed]
            └─ fallback → {{VARIABLE}} stays as placeholder (unfilled)
```

### Layer 1: BRAND_* Variables → `brand_config.yaml` (44 existing)

These are identity variables. Already fully documented in `kc_brand_variable_audit.md`.

| Group | Examples | Config Path |
|-------|----------|-------------|
| Identity | BRAND_NAME, BRAND_TAGLINE, BRAND_MISSION | `brand_config.yaml → identity.*` |
| Audience | BRAND_ICP, BRAND_ICP_LOCATION, BRAND_ICP_VALUES | `brand_config.yaml → audience.*` |
| Voice | BRAND_PERSONALITY, BRAND_TONE | `brand_config.yaml → voice.*` |
| Visual | BRAND_COLORS.*, BRAND_LOGO_URL | `brand_config.yaml → visual.*` |
| Operations | BRAND_REGION, BRAND_CHANNELS, BRAND_COMPETITORS | `brand_config.yaml → operations.*` |

### Layer 2: Instance Variables → `instance_config.yaml` (23 new + 2 discovered)

These are operational variables, specific to CRM/research workflows.

| Section | Variables | Config Path | Depends On |
|---------|-----------|-------------|------------|
| **crm_pipeline** | INDUSTRY, TARGET_COUNT, BATCH_SOURCES, DIRECTORY_SOURCES, SEARCH_QUERIES, CATEGORIES, CITIES, RADIUS_KM, HASHTAGS, MARKETPLACES, CNAE_CODES, LEGAL_SOURCES | `instance_config.yaml → crm_pipeline.*` | BRAND_REGION (derives CITIES), BRAND_CHANNELS (derives PLATFORMS) |
| **dashboard** | MAP_CENTER_LAT, MAP_CENTER_LNG, MAP_ZOOM, CRM_DATA_SOURCE | `instance_config.yaml → dashboard.*` | BRAND_HQ (derives lat/lng via geocoding) |
| **infrastructure** | DB_PROVIDER, TABLES, MAP_PROVIDER, AUTH_METHOD | `instance_config.yaml → infrastructure.*` | Independent |
| **research** | SEARCH_PROVIDERS, MERGE_STRATEGY, DEDUP_FIELDS | `instance_config.yaml → research.*` | Independent |
| **discovered** | BRAND_EMAIL, BRAND_DOMAIN | `brand_config.yaml` (proposed extension) | Derivable from existing LOGO_URL |

### Layer 3: Structural Variables (no injection — pattern only)

| Variable Pattern | Used In | Resolution |
|------------------|---------|------------|
| PIPELINE_NAME | CRM templates | User chooses at mission time |
| OUTPUT_FILE | Batch templates | Auto-generated: `crm_batch_{letter}_{type}.json` |
| SIGNAL_TAG | Batch templates | Auto-generated: `batch_{letter}_complete` |
| MISSION, NUCLEUS, PHASE | Learning records | Runtime context (filled by `cex_mission_runner.py`) |
| STAGES, BATCHES, FINAL_STATS | Workflow templates | Composite — built from pipeline results |

### Variable Cross-Dependency Map

```
BRAND_REGION ──→ REGION ──→ CITIES (expansion rings)
BRAND_CHANNELS ──→ PLATFORMS (social subset)
BRAND_HQ ──→ MAP_CENTER_LAT, MAP_CENTER_LNG (geocoding)
INDUSTRY ──→ CATEGORIES, SEARCH_QUERIES, HASHTAGS (domain-specific)
TARGET_COUNT ──→ BATCH_SOURCES (determines which batches to run)
```

---

## 5. Usage Flow — How `/init` Triggers Template Resolution

```
User runs /init
│
├── Step 1: Answer ~6 questions
│   ├── Brand name, domain, audience, tone, language, tagline
│   └── (Optional) CRM pipeline params: industry, target count, region
│
├── Step 2: Config files created
│   ├── .cex/brand/brand_config.yaml  ← BRAND_* filled
│   └── .cex/instance/instance_config.yaml  ← CRM/pipeline vars filled (if applicable)
│
├── Step 3: brand_inject.py resolves templates
│   ├── Scans all tpl_*.md files in P*/templates/
│   ├── Replaces {{VARIABLE}} with config values
│   └── Writes resolved artifacts to output paths
│
├── Step 4: git checkout -b <brand-slug>
│   ├── Branch created from main
│   └── Templates remain in main (never touched)
│
├── Step 5: Resolved artifacts created in branch
│   ├── tpl_crm_mission_plan.md → crm_mission/MISSION_PLAN.md
│   ├── tpl_crm_dashboard.html  → N06_commercial/P05_output/dashboard.html
│   └── (each template → concrete artifact with brand data)
│
└── Step 6: N07 dispatches first mission
    ├── Research pipeline runs with brand context
    ├── CRM populates with real contacts
    └── Dashboard shows real data
```

### Template Lifecycle

```
ARCHETYPE (main)          INSTANCE (brand branch)         PRIVATE (never in main)
────────────────          ─────────────────────           ──────────────────────
tpl_crm_mission_plan.md → MISSION_PLAN.md                crm_batch_*.json
tpl_crm_dashboard.html  → dashboard.html                 .env, API keys
tpl_research_batch_*.md → batch_a.md, batch_b.md...      crm_enrich_*.json
brand_config_template   → brand_config.yaml (filled)     canva_token.json
```

---

## 6. Cross-Reference Matrix

### New Templates ↔ Existing Core Templates

| New (instance extraction) | Related Core Template | Relationship |
|---------------------------|----------------------|--------------|
| `tpl_crm_mission_plan.md` | `tpl_workflow.md` (P12) | Specialized CRM workflow |
| `tpl_research_batch_*.md` (6) | `tpl_research_pipeline.md` (P04) | Concrete batch implementations |
| `tpl_crm_dashboard.html` | `tpl_response_format.md` (P05) | HTML output format |
| `tpl_search_tool_business_discovery.md` | `tpl_search_tool.md` (P04) | Business-specific search |
| `tpl_retriever_business_intel.md` | `tpl_retriever.md` (P04) | Multi-source business retriever |
| `tpl_workflow_research_pipeline.md` | `tpl_workflow.md` (P12) | Research-specific workflow |
| `tpl_workflow_strategic_outreach.md` | `tpl_workflow.md` (P12) | Outreach-specific workflow |
| `tpl_crm_pipeline_evidence.md` | `tpl_checkpoint.md` (P12) | Pipeline completion evidence |
| `tpl_learning_record_autonomy.md` | `tpl_learning_record.md` (P10) | Autonomy-specific learning |
| `tpl_brand_context_nucleus.md` | `tpl_boot_config.md` (P02) | Per-nucleus brand injection |
| `tpl_decision_manifest_brand.yaml` | `tpl_runtime_rule.md` (P09) | Brand-specific GDP decisions |
| `tpl_crm_admin_spec.md` | `tpl_software_project.md` (P04) | CRM infrastructure spec |

### Template → Tool Dependencies

| Template | Resolved By | Post-Processing |
|----------|------------|-----------------|
| All `tpl_*.md` | `brand_inject.py` | `cex_compile.py` (→ .yaml) |
| BRAND_* templates | `brand_propagate.py` | Push to all nuclei |
| Instance templates | `brand_inject.py` (proposed: extend to read `instance_config.yaml`) | N/A |
| Learning records | Runtime (not injected) | `cex_memory_update.py` |

### Related Knowledge Cards

| KC | Relationship |
|----|-------------|
| `kc_instance_variable_registry.md` | Sister — 67 variables mapped by N01 |
| `kc_brand_variable_audit.md` | Parent — 44 BRAND_* vars documented |
| `kc_rosetta_stone.md` | Terminology reference |
| `spec_instance_extraction.md` | Parent spec — defines extraction framework |
| `tpl_template_registry.md` | Predecessor — N03's 17-template index (this KC supersedes) |

---

## 7. Template Distribution Summary

| Pillar | Core | Instance-Extraction | Total |
|--------|:----:|:-------------------:|:-----:|
| P01 Knowledge | 9 | 0 | 9 |
| P02 Model | 11 | 0 | 11 |
| P03 Prompt | 7 | 0 | 7 |
| P04 Tools | 22 | 2 | 24 |
| P05 Output | 4 | 1 | 5 |
| P06 Schema | 6 | 0 | 6 |
| P07 Evals | 10 | 0 | 10 |
| P08 Architecture | 8 | 0 | 8 |
| P09 Config | 7 | 0 | 7 |
| P10 Memory | 6 | 0 | 6 |
| P11 Feedback | 7 | 1 | 8 |
| P12 Orchestration | 8 | 11 | 19 |
| **Non-pillar** | 0 | 3 | 3 |
| **TOTAL** | **105** | **18** | **123** |

> P12 Orchestration is the heaviest pillar (19 templates) due to CRM pipeline batches.
> P04 Tools is second (24 templates) due to the broad tool taxonomy.

---

## 8. Open Items

| Item | Status | Owner |
|------|--------|-------|
| Extend `brand_inject.py` to read `instance_config.yaml` | Pending | N05 |
| Create `_instances/_template/.cex/instance/instance_config.yaml` | Pending | N03 |
| Geocoding derivation for MAP_CENTER_LAT/LNG from BRAND_HQ | Proposed | N05 |
| Add BRAND_EMAIL, BRAND_DOMAIN to `brand_config_template.yaml` | Proposed | N03 |
| Template validation: ensure all {{vars}} have config mapping | Pending | N05 |

---

## Verification

- [x] All 123 templates inventoried with pillar assignment
- [x] 15 instance-extraction templates documented with variables and origin
- [x] 3 non-pillar templates documented
- [x] Variable dependency graph with resolution chains
- [x] /init usage flow documented
- [x] Cross-references to existing core templates
- [x] Related KCs and specs linked
- [x] Distribution summary by pillar
