---
id: bld_context_sources_canary_config
kind: knowledge_card
pillar: P01
title: "Context Sources: canary_config Builder"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: 5.4
tags: [context_sources, canary_config, P09]
llm_function: CONSTRAIN
tldr: "Ordered context sources for F3 INJECT in canary_config builds."
density_score: null
---

# Context Sources: canary_config Builder

## Injection Order (F3 INJECT)
| Priority | Source | Path | Why |
|----------|--------|------|-----|
| 1 | Schema | archetypes/builders/canary-config-builder/bld_schema_canary_config.md | Field constraints |
| 2 | Knowledge Card | N00_genesis/P01_knowledge/library/kind/kc_canary_config.md | Traffic stages + rollback triggers |
| 3 | Examples | archetypes/builders/canary-config-builder/bld_examples_canary_config.md | Golden reference |
| 4 | Quality Gate | archetypes/builders/canary-config-builder/bld_quality_gate_canary_config.md | Validation rules |
| 5 | slo_definition KC | N00_genesis/P01_knowledge/library/kind/kc_slo_definition.md | Rollback trigger signals |
| 6 | deployment_manifest KC | N00_genesis/P01_knowledge/library/kind/kc_deployment_manifest.md | Boundary context |
| 7 | Memory | archetypes/builders/canary-config-builder/bld_memory_canary_config.md | Recalled corrections |
