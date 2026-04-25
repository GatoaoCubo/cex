---
id: p06_ed_build_actions
kind: enum_def
8f: F1_constrain
pillar: P06
title: "Enum Definitions -- Build Actions and CEX Constants"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [enum-def, build-actions, N03, constants, pillar, nucleus, verb]
tldr: "Canonical enumerations for all CEX build-time constants: BUILD_ACTION, PILLAR, NUCLEUS, MODEL_TIER, SIGNAL_EVENT, QUALITY_TIER, PIPELINE_FUNCTION. Machine-parseable source of truth for all 301 builders."
density_score: 0.93
updated: "2026-04-17"
related:
  - bld_knowledge_card_nucleus_def
  - p01_kc_cex_project_overview
  - spec_infinite_bootstrap_loop
  - p01_ctx_cex_project
  - p08_pat_nucleus_fractal
  - agent_card_engineering_nucleus
  - dispatch
  - p02_agent_admin_orchestrator
  - ctx_cex_new_dev_guide
  - p12_wf_create_orchestration_agent
---

# Enum Definitions: Build Actions and CEX Constants

## BUILD_ACTION

Controls how N03 treats the target artifact path during a build task.

| Value | Description | Behavior |
|-------|-------------|---------|
| CREATE | Produce new artifact from scratch | Fail if file exists unless `force=true` |
| REWRITE | Discard existing, build fresh | Overwrites unconditionally; preserves git history |
| MIGRATE | Update structure while preserving content | Loads existing, applies schema migration, saves |
| IMPROVE | Raise quality score of existing artifact | F7 GOVERN -> identify gaps -> targeted F6 patch |
| VALIDATE | Run quality gate only, no write | F7 only; outputs score without modifying file |

**Default:** CREATE  
**Closed set:** no new values expected without spec update.

## PILLAR

The 12 domain groups that organize all 300 kinds.

| Value | Name | Primary Domain |
|-------|------|----------------|
| P01 | Knowledge | Storage, retrieval, knowledge cards |
| P02 | Model | Agent definitions, providers, configs |
| P03 | Prompt | Templates, actions, chains, reasoning |
| P04 | Tools | External capabilities, APIs, executors |
| P05 | Output | Production artifacts, formatters |
| P06 | Schema | Data contracts, types, interfaces |
| P07 | Evaluation | Quality, scoring, testing, benchmarks |
| P08 | Architecture | System structure, diagrams, decisions |
| P09 | Config | Runtime settings, secrets, environments |
| P10 | Memory | State, context, indexing, summarization |
| P11 | Feedback | Learning, correction, loops, guardrails |
| P12 | Orchestration | Workflows, dispatch, scheduling |

**Closed set:** P01-P12 are fixed; new domains must extend existing pillars.

## NUCLEUS

The 8 operational agents of the CEX system.

| Value | Name | Sin Lens | Domain |
|-------|------|----------|--------|
| n00 | Genesis | (archetype) | template, pre-sin |
| n01 | Intelligence | analytical_envy | research, analysis |
| n02 | Marketing | creative_lust | copy, campaigns |
| n03 | Engineering | inventive_pride | build, schema, architecture |
| n04 | Knowledge | knowledge_gluttony | docs, RAG, indexing |
| n05 | Operations | gating_wrath | infra, testing, CI/CD |
| n06 | Commercial | strategic_greed | pricing, sales, revenue |
| n07 | Orchestrator | orchestrating_sloth | dispatch, coordination |

**Closed set:** N00-N07; new nuclei (N08+) require nucleus bootstrap protocol.

## MODEL_TIER

Model selection tiers used in BuildTask and nucleus routing.

| Value | Model | Context | Use Case |
|-------|-------|---------|---------|
| haiku | claude-haiku-4-5 | 200K | fast classification, preflight |
| sonnet | claude-sonnet-4-6 | 200K | N01, N02, N04, N05, N06 standard |
| opus | claude-opus-4-6 | 1M | N03, N07 high-effort builds |

**Open set:** new model tiers added when new models become available.

## SIGNAL_EVENT

Completion events sent by nuclei via signal_writer.

| Value | Meaning | Sent By |
|-------|---------|---------|
| complete | Wave task complete, artifacts produced | Any nucleus on success |
| error | Task failed, no usable artifacts | Any nucleus on unrecoverable failure |
| partial | Some artifacts complete, some failed | Nucleus when partial delivery |
| ready | Nucleus booted and awaiting task | Boot scripts |

**Closed set:** N07 lifecycle depends on these 4 values.

## QUALITY_TIER

Score-derived quality classification for artifacts.

| Value | Score Range | Meaning |
|-------|-------------|---------|
| exemplary | >= 9.5 | Best-in-class, can be used as builder example |
| excellent | >= 9.0 | Production-ready, CEX target |
| good | >= 8.0 | Acceptable for most uses |
| acceptable | >= 7.0 | Needs improvement but usable |
| below_floor | < 7.0 | Blocked from publication |
| unscored | null | Not yet peer-reviewed |

**Closed set:** tiers map to 8F quality floor (7.0 minimum for publication).

## PIPELINE_FUNCTION

The 8 (plus sub-steps) functions in the CEX reasoning pipeline.

| Value | Name | Mandatory | Description |
|-------|------|-----------|-------------|
| F1 | CONSTRAIN | yes | Resolve kind, pillar, schema |
| F2 | BECOME | yes | Load builder ISOs (13 per kind) |
| F2b | SPEAK | yes | Load controlled vocabulary KC |
| F3 | INJECT | yes | Assemble context: KCs, examples, brand, memory |
| F3b | PERSIST | no | Declare new knowledge for persistence |
| F3c | GROUND | no | Record provenance of injected sources |
| F4 | REASON | yes | Plan sections, approach, construction triad |
| F5 | CALL | yes | Use tools: compile, doctor, index, signal |
| F6 | PRODUCE | yes | Generate complete artifact with frontmatter + body |
| F7 | GOVERN | yes | Validate H01-H07 gates, run 12LP, score 5D |
| F7b | LEARN | no | Capture feedback signals after scoring |
| F8 | COLLABORATE | yes | Save, compile, commit, signal |

**Closed set:** F1-F8 are fixed; sub-steps (F2b, F3b, F3c, F7b) are optional extensions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.37 |
| [[p01_kc_cex_project_overview]] | upstream | 0.33 |
| [[spec_infinite_bootstrap_loop]] | related | 0.32 |
| [[p01_ctx_cex_project]] | upstream | 0.32 |
| [[p08_pat_nucleus_fractal]] | downstream | 0.31 |
| [[agent_card_engineering_nucleus]] | upstream | 0.31 |
| [[dispatch]] | downstream | 0.30 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.29 |
| [[ctx_cex_new_dev_guide]] | related | 0.29 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.28 |
