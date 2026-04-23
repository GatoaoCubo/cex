---
id: p08_cm_cex_bounded_contexts
kind: context_map
pillar: P08
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: n03_engineering
system_name: "CEXAI -- Cognitive Exchange AI"
contexts_count: 8
quality: 8.3
tags: [context_map, cex, ddd, bounded_context, nucleus, architecture]
tldr: "DDD context map of CEX: 8 nuclei as bounded contexts, 21 relationships, Shared Kernel from N00 Genesis."
related:
  - p01_ctx_cex_project
  - bld_sp_collaboration_software_project
  - p01_kc_cex_project_overview
  - p12_mission_bootstrap_2026q1
  - bld_collaboration_kind
  - p02_agent_creation_nucleus
  - p12_dr_content_factory
  - bld_knowledge_card_nucleus_def
  - mission_content_monetization
  - ctx_cex_new_dev_guide
density_score: 1.0
---

## Bounded Contexts

| Context | Team (Nucleus) | Core Domain? | Description |
|---------|----------------|-------------|-------------|
| N00_Genesis | Archetype (no runtime agent) | GENERIC | Template library: 12 pillar schemas, 300 kind definitions, builder archetypes, shared ISOs. Shared Kernel consumed by all other contexts. |
| N01_Intelligence | N01 (Analytical Envy) | SUPPORTING | Research, analysis, competitive intelligence. Produces knowledge_cards, research briefs, taxonomy audits. |
| N02_Marketing | N02 (Creative Lust) | SUPPORTING | Copy, campaigns, brand voice, content calendars. Produces prompt_templates, taglines, ad copy. |
| N03_Engineering | N03 (Inventive Pride) | CORE | Artifact construction, builder execution, 8F pipeline implementation. Produces agents, schemas, workflows, all typed artifacts. |
| N04_Knowledge | N04 (Knowledge Gluttony) | CORE | RAG, indexing, knowledge cards, documentation, curation. Owns the knowledge library and retrieval infrastructure. |
| N05_Operations | N05 (Gating Wrath) | SUPPORTING | Code, testing, deployment, CI/CD, MCP servers, runtime config. Executes and validates what N03 builds. |
| N06_Commercial | N06 (Strategic Greed) | SUPPORTING | Pricing, monetization, sales funnels, brand strategy. Produces content_monetization, course outlines, pricing models. |
| N07_Admin | N07 (Orchestrating Sloth) | CORE | Orchestration, dispatch, mission planning, GDP, wave management. Never builds -- routes, monitors, consolidates. |

## Relationships

| Upstream (U) | Downstream (D) | Pattern | Integration Type | Notes |
|-------------|----------------|---------|-----------------|-------|
| N00_Genesis | N01_Intelligence | Shared_Kernel | sync | N01 reads pillar schemas, kind defs, builder ISOs from N00 |
| N00_Genesis | N02_Marketing | Shared_Kernel | sync | N02 reads brand templates, prompt archetypes from N00 |
| N00_Genesis | N03_Engineering | Shared_Kernel | sync | N03 reads all 300 kind schemas, builder ISOs, archetype templates |
| N00_Genesis | N04_Knowledge | Shared_Kernel | sync | N04 reads KC templates, chunk strategies, embedding configs |
| N00_Genesis | N05_Operations | Shared_Kernel | sync | N05 reads tool schemas, config templates, test harnesses |
| N00_Genesis | N06_Commercial | Shared_Kernel | sync | N06 reads monetization templates, pricing archetypes |
| N00_Genesis | N07_Admin | Shared_Kernel | sync | N07 reads orchestration schemas, dispatch rules, crew templates |
| N07_Admin | N01_Intelligence | Customer_Supplier | async | N07 writes handoffs; N01 reads and executes autonomously |
| N07_Admin | N02_Marketing | Customer_Supplier | async | N07 dispatches marketing tasks via handoff files |
| N07_Admin | N03_Engineering | Customer_Supplier | async | N07 dispatches build tasks; N03 executes 8F pipeline |
| N07_Admin | N04_Knowledge | Customer_Supplier | async | N07 dispatches knowledge tasks; N04 curates and indexes |
| N07_Admin | N05_Operations | Customer_Supplier | async | N07 dispatches ops/deploy tasks; N05 executes |
| N07_Admin | N06_Commercial | Customer_Supplier | async | N07 dispatches commercial tasks; N06 prices and packages |
| N01_Intelligence | N03_Engineering | ACL | async | N03 consumes N01 research via knowledge_cards; translates to build specs |
| N01_Intelligence | N02_Marketing | ACL | async | N02 consumes competitor intel; translates to campaign positioning |
| N03_Engineering | N05_Operations | OHS | async | N03 publishes artifacts via 8F+signal protocol; N05 validates and deploys |
| N03_Engineering | N04_Knowledge | OHS | async | N03 produces artifacts; N04 indexes and retrieves them via cex_retriever |
| N04_Knowledge | N01_Intelligence | Conformist | sync | N01 adopts N04's KC schema and retrieval API directly |
| N04_Knowledge | N02_Marketing | Conformist | sync | N02 reads KCs as-is for content research |
| N06_Commercial | N02_Marketing | Partnership | async | Co-evolve pricing and campaign messaging; joint brand-price alignment |
| N05_Operations | N07_Admin | OHS | async | N05 exposes health checks, test results via signals; N07 consumes for consolidation |

## Integration Details

| Relationship | Translation Layer | Protocol | Sync/Async |
|-------------|-----------------|----------|-----------|
| N00 -> All (Shared_Kernel) | None (direct file read) | Filesystem (git) | sync |
| N07 -> N01..N06 (Customer_Supplier) | Handoff file (.cex/runtime/handoffs/) | File + dispatch.sh | async |
| N01 -> N03 (ACL) | N03 reads KC, extracts build-relevant facts | KC -> build spec translation | async |
| N01 -> N02 (ACL) | N02 reads intel KC, extracts positioning angles | KC -> campaign brief | async |
| N03 -> N05 (OHS) | signal_writer.py JSON signal | JSON signal protocol | async |
| N03 -> N04 (OHS) | cex_compile.py output + git commit | Compiled YAML + git | async |
| N04 -> N01 (Conformist) | None (N01 adopts KC schema) | Direct file read | sync |
| N04 -> N02 (Conformist) | None (N02 adopts KC schema) | Direct file read | sync |
| N06 <-> N02 (Partnership) | Shared decision_manifest.yaml | GDP protocol | async |
| N05 -> N07 (OHS) | signal_writer.py JSON signal | JSON signal protocol | async |

## Team Coupling

| Relationship | Coupling Level | Risk | Mitigation |
|-------------|----------------|------|-----------|
| N00 -> All (Shared_Kernel) | Very High | Schema change in N00 breaks all 7 nuclei | N00 changes require N07 approval; versioned schemas; backward-compatible evolution only |
| N07 -> N01..N06 (Customer_Supplier) | Low | Handoff format change breaks dispatch | Handoff schema is versioned; nuclei validate frontmatter on read |
| N01 -> N03 (ACL) | Low | N03 isolates from N01 model changes via translation | ACL owned by N03; N01 model changes do not propagate |
| N03 -> N05 (OHS) | Low | Signal format is versioned JSON; N05 validates on read | signal_writer.py enforces schema |
| N04 -> N01/N02 (Conformist) | Medium | N04 KC schema change forces N01/N02 to adapt | KC schema is stable (< 1 change/quarter); migration via cex_compile |
| N06 <-> N02 (Partnership) | High | Price-copy misalignment if teams diverge | Joint GDP session before any campaign; shared decision_manifest |
| N03 -> N04 (OHS) | Low | Compiled YAML format is stable; cex_compile validates | Compiler is the ACL boundary |
| N05 -> N07 (OHS) | Low | Signal format identical to N03->N05 | Same signal_writer.py; single protocol |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_ctx_cex_project]] | upstream | 0.32 |
| [[bld_sp_collaboration_software_project]] | downstream | 0.30 |
| [[p01_kc_cex_project_overview]] | upstream | 0.29 |
| [[p12_mission_bootstrap_2026q1]] | downstream | 0.28 |
| [[bld_collaboration_kind]] | downstream | 0.28 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[p12_dr_content_factory]] | downstream | 0.26 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.25 |
| [[mission_content_monetization]] | downstream | 0.25 |
| [[ctx_cex_new_dev_guide]] | related | 0.25 |
