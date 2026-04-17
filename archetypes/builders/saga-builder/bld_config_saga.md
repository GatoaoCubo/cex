---
id: bld_context_sources_saga
kind: knowledge_card
pillar: P01
title: "Context Sources: saga Builder"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: 5.4
tags: [context_sources, saga, P12]
llm_function: CONSTRAIN
tldr: "Ordered context sources for F3 INJECT in saga builds."
density_score: null
---

# Context Sources: saga Builder

## Injection Order (F3 INJECT)
| Priority | Source | Path | Why |
|----------|--------|------|-----|
| 1 | Schema | archetypes/builders/saga-builder/bld_schema_saga.md | Field constraints |
| 2 | Knowledge Card | N00_genesis/P01_knowledge/library/kind/kc_saga.md | Garcia-Molina + compensation model |
| 3 | Examples | archetypes/builders/saga-builder/bld_examples_saga.md | Golden reference |
| 4 | Quality Gate | archetypes/builders/saga-builder/bld_quality_gate_saga.md | Compensation completeness gate |
| 5 | workflow KC | N00_genesis/P01_knowledge/library/kind/kc_workflow.md | Boundary clarification |
| 6 | Memory | archetypes/builders/saga-builder/bld_memory_saga.md | Recalled corrections |
