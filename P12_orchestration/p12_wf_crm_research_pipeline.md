---
id: p12_wf_crm_research_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-03"
updated: "2026-04-03"
author: "workflow-builder"
title: "CRM Research Pipeline Automation"
steps_count: 5
execution: mixed
agent_nodes: [n01, n04, n05, n06, n07]
timeout: 5400
retry_policy: per_step
depends_on: []
signals: [n01_web_research_complete, n05_validation_complete, n06_scoring_complete, n04_crm_structured, workflow_complete, workflow_error]
spawn_configs: [p12_spawn_n01_solo_research, p12_spawn_n05_solo_ops, p12_spawn_n06_solo_commercial, p12_spawn_n04_solo_knowledge]
domain: "crm-research"
quality: null
tags: [workflow, crm, research, pipeline, pet, B2B, mixed, P12]
tldr: "5-step mixed pipeline: N01 collects pet business leads, N05 validates CNPJs, N06 scores B2B potential (parallel), N04 structures CRM + KCs"
density_score: null
---
## Purpose
Automates GATO³ B2B CRM prospecting for pet industry. Replaces manual research (112+ contacts, ABC Paulista) with a repeatable workflow. New rings/segments reuse the same pipeline.

## Steps

### Step 1: Web Research [n01] — Wave 0
- **Agent**: n01 (gemini-2.5-pro)
- **Action**: Search target geography + segments; collect CNPJ, name, address, segment, contacts, ratings
- **Input**: Handoff with `geography`, `segments` (clinica_vet, pet_shop, banho_tosa, hospital_24h, ong), `depth`
- **Output**: `N01_research/output/output_crm_{scope}.md`
- **Signal**: `n01_web_research_complete` (`contacts_count`, `segments_covered`)
- **Depends on**: none
- **On failure**: retry(1) → `n01_error` → N07

### Step 2: CNPJ + Contact Validation [n05] — Wave 1
- **Agent**: n05 (codex/o3)
- **Action**: Validate CNPJs, verify phone formats, flag `a_validar` fields, deduplicate
- **Input**: Raw CRM from Step 1
- **Output**: `N05_operations/output/crm_validated_{scope}.md`
- **Signal**: `n05_validation_complete` (`valid_count`, `invalid_count`, `dedup_removed`)
- **Depends on**: Step 1
- **On failure**: retry(1) → skip (pass raw with `validation: skipped`)

### Step 3: B2B Lead Scoring [n06] — Wave 1 (parallel)
- **Agent**: n06 (claude/sonnet)
- **Action**: Score B2B potential (alto/medio/baixo) by porte, foco_felino, segment_fit, rating, density
- **Input**: Raw CRM from Step 1
- **Output**: `N06_commercial/output/crm_scored_{scope}.md`
- **Signal**: `n06_scoring_complete` (`alto_count`, `medio_count`, `baixo_count`)
- **Depends on**: Step 1
- **On failure**: retry(1) → skip (default `medio`)

### Step 4: CRM Structuring [n04] — Wave 2
- **Agent**: n04 (gemini-2.5-pro)
- **Action**: Merge validated + scored data; generate segment KCs; create Supabase-ready chunks
- **Input**: Steps 2 + 3 outputs
- **Output**: `N04_knowledge/output/crm_structured_{scope}.md` + segment KCs
- **Signal**: `n04_crm_structured` (`total_contacts`, `kc_count`)
- **Depends on**: Steps 2, 3
- **On failure**: retry(1) → `n04_error` → N07

### Step 5: Consolidation [n07] — Wave 3
- **Agent**: n07 (claude/opus)
- **Action**: Commit Gemini work (N01, N04); compose CRM brief; archive handoffs
- **Input**: All signals + git log + output dirs
- **Output**: `N07_orchestration/briefs/crm_{scope}_brief.md`
- **Signal**: `workflow_complete` (`total_contacts`, `validated_pct`, `alto_leads`)
- **Depends on**: Step 4
- **On failure**: abort → `workflow_error`

## Wave Plan
| Wave | Steps | Mode | Gate |
|------|-------|------|------|
| 0 | Step 1 (N01) | solo | n01_web_research_complete |
| 1 | Step 2 (N05) + Step 3 (N06) | parallel | both signals |
| 2 | Step 4 (N04) | solo | n04_crm_structured |
| 3 | Step 5 (N07) | solo | workflow_complete |

## Dependencies
- Handoff must specify `geography`, `segments`, `depth`
- N01/N04 cannot git commit — N07 consolidates
- spawn_delay_ms=5000 between waves
- `.cex/runtime/signals/` must be writable
