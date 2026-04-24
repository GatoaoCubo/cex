---
id: p01_ctx_cex_project
kind: context_doc
8f: F3_inject
pillar: P01
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: context-doc-builder
domain: cex_system
scope: "CEX typed knowledge system — architecture, nuclei, pipeline, and conventions for agent orientation"
quality: 9.0
tags: [context-doc, cex, architecture, orchestration]
tldr: "CEX: 123 kinds, 12 pillars, 8 nuclei (N01-N07), 8F pipeline. N07 orchestrates; N03 builds. GDP before dispatch."
keywords: [cex, nuclei, 8f, pipeline, kinds, pillars, dispatch]
density_score: 0.88
related:
  - p01_kc_cex_project_overview
  - ctx_cex_new_dev_guide
  - p03_sp_n03_creation_nucleus
  - p01_kg_cex_system_architecture
  - p03_sp_cex_core_identity
  - spec_cex_system_map
  - bld_collaboration_kind
  - n03_readme_technical
  - p03_sp_orchestration_nucleus
  - p12_wf_orchestration_pipeline
---

## Scope

In scope: CEX architecture, 12 pillars, 8 nuclei roles, 8F pipeline steps, core conventions, key file locations.
Out of scope: brand configuration, individual artifact schemas, nucleus-specific build rules, SDK runtime internals.

## Background

CEX is a typed knowledge system for LLM agents. It organizes 123 artifact kinds across 12 pillars (P01-P12), executed by 8 specialized nuclei (N01-N07) through a mandatory 8-step pipeline (8F). Every artifact has a kind, pillar, and quality target >= 9.0. N07 orchestrates; all others build. No nucleus self-scores quality.

## Nuclei

| Nucleus | Role | Domain |
|---------|------|--------|
| N01 | Intelligence | Research, analysis, market intel |
| N02 | Marketing | Copywriting, campaigns, brand voice |
| N03 | Builder | Artifact construction, builders, templates |
| N04 | Knowledge | RAG, KCs, embeddings, taxonomy |
| N05 | Operations | Code, testing, CI/CD, deploy |
| N06 | Commercial | Pricing, courses, funnels |
| N07 | Orchestrator | Dispatch, wave planning, consolidation |

## 8F Pipeline

F1 CONSTRAIN → F2 BECOME → F3 INJECT → F4 REASON → F5 CALL → F6 PRODUCE → F7 GOVERN → F8 COLLABORATE

## Constraints & Assumptions

- 8F is mandatory for every task — no exceptions, no shortcuts
- quality: null on all artifacts — peer review assigns scores
- GDP (Guided Decision Protocol) required before dispatch for subjective decisions
- N07 never builds artifacts directly — always dispatches to N03 or domain nucleus
- All executable code must be ASCII-only (no emoji, no accented chars in .py/.ps1)
- Assumed: brand_config.yaml is bootstrapped before nuclei run

## Dependencies

- `.cex/kinds_meta.json` — kind registry (123 kinds)
- `P{01-12}/_schema.yaml` — pillar schemas
- `archetypes/builders/{kind}-builder/` — 13 ISOs per kind
- `.cex/brand/brand_config.yaml` — brand context injected into all prompts
- `.claude/rules/` — per-nucleus operational rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_project_overview]] | related | 0.51 |
| [[ctx_cex_new_dev_guide]] | sibling | 0.49 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.45 |
| [[p01_kg_cex_system_architecture]] | related | 0.39 |
| [[p03_sp_cex_core_identity]] | downstream | 0.38 |
| [[spec_cex_system_map]] | sibling | 0.36 |
| [[bld_collaboration_kind]] | downstream | 0.35 |
| [[n03_readme_technical]] | downstream | 0.35 |
| [[p03_sp_orchestration_nucleus]] | downstream | 0.34 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.33 |
