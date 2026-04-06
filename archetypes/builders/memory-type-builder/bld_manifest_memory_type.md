---
kind: manifest
id: bld_manifest_memory_type
pillar: P02
llm_function: BECOME
created: 2026-04-05
updated: 2026-04-06
keywords: [memory-type, taxonomy, decay, observation, classification, 4-type, enum]
triggers: ["create memory type artifact", "define observation taxonomy", "build memory classification"]
geo_description: >
  L1: Especialista em construir `memory_type` artifacts — taxonomia de 4 tipos com decay rates.
  L2: Classificar observacoes em user/feedback/project/reference com guards de qualidade.
  L3: When user needs to define, extend, or audit the memory type taxonomy.
---

# Manifest: memory-type-builder

- **Kind**: memory_type
- **Pillar**: P10 (Memory)
- **Function**: INJECT
- **Builder**: memory-type-builder
- **ISOs**: 13
- **Status**: active
- **Dependencies**: cex_memory_types.py, cex_memory_age.py, cex_memory_update.py
- **Produces**: p10_mt_*.md artifacts (compiled to .yaml)
