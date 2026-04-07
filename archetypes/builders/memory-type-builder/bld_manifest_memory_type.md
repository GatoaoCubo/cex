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
  L1: Specialist in building `memory_type` artifacts — taxonomia de 4 types with decay rates.
  L2: Classify observactions em user/feedback/project/reference with guards de quality.
  L3: When user needs to define, extend, or audit the memory type taxonomy.
quality: 9.1
title: "Manifest Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
density_score: 0.90
---

# Manifest: memory-type-builder

1. **Kind**: memory_type
2. **Pillar**: P10 (Memory)
3. **Function**: INJECT
4. **Builder**: memory-type-builder
5. **ISOs**: 13
6. **Status**: active
7. **Dependencies**: cex_memory_types.py, cex_memory_age.py, cex_memory_update.py
8. **Produces**: p10_mt_*.md artifacts (compiled to .yaml)

## Metadata

```yaml
id: bld_manifest_memory_type
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-manifest-memory-type.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `manifest` |
| Pillar | P02 |
| Domain | memory type construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Builder Context

This ISO operates within the `memory-type-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |
