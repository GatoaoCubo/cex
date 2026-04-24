---
id: p10_entity_cex_system
kind: entity_memory
8f: F3_inject
pillar: P10
title: "Entity Memory — CEX System"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: system-knowledge
quality: 9.1
tags: [entity-memory, cex, system, architecture, metadata]
tldr: "Persistent entity memory tracking CEX system facts: 123 kinds, 12 pillars, 8 nuclei, 125 builders, 59 tools, 2184 artifacts."
density_score: 0.95
related:
  - p01_kc_cex_project_overview
  - p01_kg_cex_system_architecture
  - p06_arch_knowledge_graph
  - bld_knowledge_card_nucleus_def
  - p01_ctx_cex_project
  - bld_collaboration_kind
  - spec_cex_system_map
  - ctx_cex_new_dev_guide
  - bld_architecture_kind
  - agent_card_n04
---

# Entity Memory — CEX System

## Entity Profile

| Attribute | Value | Last Verified |
|-----------|-------|---------------|
| Entity name | CEX (Typed Knowledge System for LLM Agents) | 2026-04-07 |
| Entity type | Software system / AI agent framework | 2026-04-07 |
| Kind count | 123 | 2026-04-07 |
| Pillar count | 12 (P01–P12) | 2026-04-07 |
| Nucleus count | 8 (N00–N07) | 2026-04-07 |
| Builder count | 125 (13 ISOs each) | 2026-04-07 |
| Tool count | 59 (_tools/*.py) | 2026-04-07 |
| Artifact count | 2,184+ | 2026-04-07 |
| SDK | `cex_sdk/` — 78 .py, 4,504 lines | 2026-04-07 |
| Pipeline | 8F (F1 Focus → F8 File) | 2026-04-07 |
| Decision protocol | GDP (Guided Decision Protocol) | 2026-04-07 |

## Nucleus Registry

| ID | Name | Sin | Domain |
|----|------|-----|--------|
| N00 | Genesis | — | Archetype / bootstrap |
| N01 | Intelligence | Envy | Research / analysis |
| N02 | voice | Lust | Marketing / copy |
| N03 | Creation | Pride | Build / create |
| N04 | Knowledge | Gluttony | RAG / docs / memory |
| N05 | Operations | Wrath | Code / test / deploy |
| N06 | Commercial | Greed | Brand / monetization |
| N07 | Admin | Sloth (delegation) | Orchestration |

## Pillar Registry

| ID | Name | Kind Count |
|----|------|--------:|
| P01 | Knowledge | 10 |
| P02 | Orchestration | 11 |
| P03 | Agents | 8 |
| P04 | Ingestion | 7 |
| P05 | Prompts | 9 |
| P06 | Schema | 8 |
| P07 | Quality | 9 |
| P08 | Output | 11 |
| P09 | Feedback | 8 |
| P10 | Memory | 8 |
| P11 | Commercialization | 18 |
| P12 | Deploy | 16 |

## Key Relationships

| From | Relationship | To |
|------|-------------|-----|
| Kind | BELONGS_TO | Pillar |
| Kind | BUILT_BY | Builder (13 ISOs) |
| Kind | OWNED_BY | Nucleus |
| Artifact | INSTANCE_OF | Kind |
| Nucleus | DISPATCHED_BY | N07 (orchestrator) |
| Builder | INHERITS | N00 Genesis |

## Change Log

| Date | Event | Impact |
|------|-------|--------|
| 2026-04-06 | All nuclei upgraded to Opus 4.6 (1M context) | Uniform model layer |
| 2026-04-07 | FULLGRID mission dispatched | 6 nuclei in parallel |
| 2026-04-07 | N04 AutoResearch bootstrap | 12 gaps identified, closure in progress |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_project_overview]] | upstream | 0.40 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.36 |
| [[p06_arch_knowledge_graph]] | upstream | 0.34 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.34 |
| [[p01_ctx_cex_project]] | upstream | 0.33 |
| [[bld_collaboration_kind]] | downstream | 0.31 |
| [[spec_cex_system_map]] | upstream | 0.30 |
| [[ctx_cex_new_dev_guide]] | related | 0.30 |
| [[bld_architecture_kind]] | upstream | 0.29 |
| [[agent_card_n04]] | upstream | 0.28 |
