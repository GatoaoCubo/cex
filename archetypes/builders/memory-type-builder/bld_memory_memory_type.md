---
kind: memory
id: bld_memory_memory_type
pillar: P10
llm_function: INJECT
observation_count: 3
confidence: 0.85
observation: "memory_type builder patterns: 4-type taxonomy, enum-driven classification, decay-rate alignment"
pattern: "New kind creation follows: KC first, then builder ISOs, then doctor validation"
evidence: "kc_memory_type.md created before builder; density gates caught low-density ISOs"
outcome: "successful"
memory_scope: "project"
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_system_prompt_memory_type
  - bld_manifest_memory_type
  - bld_collaboration_memory_type
  - bld_tools_memory_type
  - bld_knowledge_card_memory_type
  - bld_architecture_memory_type
  - p01_kc_memory_type
  - bld_instruction_memory_type
  - bld_config_memory_type
  - bld_output_template_memory_type
---

# Memory: memory-type-builder

## Observations

| # | Date | Type | Confidence | Observation |
|---|------|------|------------|-------------|
| 1 | 2026-04-05 | convention | 0.80 | memory_type builder created during OpenClaude assimilation (Wave 4, T11) |
| 2 | 2026-04-05 | correction | 0.85 | First-pass ISOs had low density (0.67-0.70); tables beat prose for density |
| 3 | 2026-04-05 | pattern | 0.90 | 4-type taxonomy (correction/preference/convention/context) is stable across production systems |

## Patterns

| Pattern | Evidence | Reuse |
|---------|----------|-------|
| New kind sequence: meta -> KC -> ISOs -> doctor | All 115 kinds followed this | Always |
| Tables raise density above 0.78 threshold | Doctor density gate pass rate 100% with tables | When ISO density < 0.78 |
| Enum-driven classification reduces LLM ambiguity | MemoryType enum in cex_memory_types.py | For any categorical kind |
| Decay rates must align between memory_age and memory_update | Linear decay 1yr floor 50% in both modules | When touching memory pipeline |

## Build Context

| Field | Value |
|-------|-------|
| Origin | OpenClaude assimilation, pattern harvest from memory system |
| SDK module | `cex_memory_types.py` (MemoryType enum + should_save classifier) |
| Wired at | `cex_memory_update.py` append_observation() |
| Quality gate | Dedup check: reject if cosine similarity > 0.85 with existing observation |
| Failure mode | Missing type = defaults to `context` (safest fallback) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_memory_type]] | upstream | 0.39 |
| [[bld_manifest_memory_type]] | upstream | 0.33 |
| [[bld_collaboration_memory_type]] | downstream | 0.31 |
| [[bld_tools_memory_type]] | upstream | 0.31 |
| [[bld_knowledge_card_memory_type]] | upstream | 0.30 |
| [[bld_architecture_memory_type]] | upstream | 0.28 |
| [[p01_kc_memory_type]] | related | 0.27 |
| [[bld_instruction_memory_type]] | upstream | 0.25 |
| [[bld_config_memory_type]] | upstream | 0.24 |
| [[bld_output_template_memory_type]] | upstream | 0.24 |
