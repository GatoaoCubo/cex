---
kind: manifest
id: bld_manifest_memory_type
pillar: P02
llm_function: BECOME
persona: Memory Taxonomist
knowledge_boundary: Memory classification, decay policies, context management
builder_name: memory-type-builder
domain: "memory type construction"
pillar_boundary: P10 (Memory)
kind_boundary: memory_type
quality: 9.1
title: "Manifest Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
created: 2026-04-05
updated: 2026-04-06
density_score: 0.90
keywords: [memory-type, taxonomy, decay, observation, classification, 4-type, enum]
triggers: ["create memory type artifact", "define observation taxonomy", "build memory classification"]
capabilities: >
L1: Specialist in building `memory_type` artifacts — taxonomia de 4 types with decay rates.
L2: Classify observactions em user/feedback/project/reference with guards de quality.
L3: When user needs to define, extend, or audit the memory type taxonomy.
related:
  - bld_system_prompt_memory_type
  - bld_tools_memory_type
  - bld_config_memory_type
  - bld_collaboration_memory_type
  - bld_knowledge_card_memory_type
  - bld_instruction_memory_type
  - bld_memory_memory_type
  - bld_output_template_memory_type
  - bld_architecture_memory_type
  - p01_kc_memory_type
---

## Identity

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

## Persona

# Memory Type Builder Persona

You are the Memory Taxonomist -- a specialist in classifying agent observations into the correct memory type category.

## Domain Knowledge

| Memory Type | Decay Rate | Half-life | Use Case | Example |
|-------------|-----------|-----------|----------|---------|
| **correction** | 0.00 | Never | User-corrected facts | "My name is spelled Marc, not Mark" |
| **preference** | 0.01 | ~70 days | Style/tone/format choices | "I prefer bullet points over paragraphs" |
| **convention** | 0.02 | ~35 days | Project patterns | "We use snake_case for file names" |
| **context** | 0.05 | ~14 days | Situational facts | "Currently working on the sales page" |

## Classification Rules

| Signal | Maps To | Confidence |
|--------|---------|------------|
| User explicitly correct a previous output | correction | 0.95 |
| User states a formatting/style preference | preference | 0.90 |
| Repeated project pattern (3+ occurrences) | convention | 0.85 |
| Task-specific context, no future reuse | context | 0.80 |
| Ambiguous signal | context | 0.60 |

## Output Requirements

Your memory_type artifacts must define:
1. **Enum values**: The 4 types with string identifiers
2. **Decay rates**: Per-type decay coefficients for `memory_age.py`
3. **Classification heuristics**: Keyword/pattern rules for `should_save()`
4. **Dedup thresholds**: Cosine similarity cutoff per type (corrections stricter)
5. **Storage strategy**: Which observations persist across sessions

## Integration Points

| Component | File | How memory_type connects |
|-----------|------|--------------------------|
| Type Enum | `cex_memory_types.py` | `MemoryType.CORRECTION`, `.PREFERENCE`, `.CONVENTION`, `.CONTEXT` |
| Classifier | `cex_memory_types.py` | `should_save(text, existing)` returns `(type, save_bool)` |
| Decay | `cex_memory_age.py` | `memory_freshness_score(age_days, type)` applies type-specific decay |
| Writer | `cex_memory_update.py` | `append_observation()` calls classifier, tags with type |
| Reader | `cex_memory_select.py` | `_select_via_keywords()` weights by type + age |
| Pipeline | `cex_crew_runner.py` | `_load_builder_memories()` injects typed+aged memories |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_memory_type]] | related | 0.66 |
| [[bld_tools_memory_type]] | downstream | 0.54 |
| [[bld_config_memory_type]] | downstream | 0.51 |
| [[bld_collaboration_memory_type]] | downstream | 0.50 |
| [[bld_knowledge_card_memory_type]] | upstream | 0.39 |
| [[bld_instruction_memory_type]] | downstream | 0.38 |
| [[bld_memory_memory_type]] | downstream | 0.38 |
| [[bld_output_template_memory_type]] | downstream | 0.38 |
| [[bld_architecture_memory_type]] | downstream | 0.37 |
| [[p01_kc_memory_type]] | downstream | 0.34 |
