---
kind: output_template
id: bld_output_template_memory_type
pillar: P05
llm_function: PRODUCE
quality: 9.0
title: "Output Template Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_memory_type
  - bld_instruction_memory_type
  - bld_system_prompt_memory_type
  - bld_config_memory_type
  - bld_collaboration_memory_type
  - bld_quality_gate_memory_type
  - bld_manifest_memory_type
  - bld_knowledge_card_memory_type
  - bld_architecture_memory_type
  - bld_examples_memory_type
---

# Output Template: memory_type

## Required Frontmatter

| Field | Format | Example |
|-------|--------|---------|
| id | p10_mt_{type} | p10_mt_correction |
| kind | literal | memory_type |
| pillar | literal | P10 |
| version | semver | 1.0.0 |
| created | YYYY-MM-DD | 2026-04-05 |
| updated | YYYY-MM-DD | 2026-04-05 |
| author | string | n07-orchestrator |
| type_name | enum | correction, preference, convention, context |
| decay_rate | float | 0.00, 0.01, 0.02, 0.05 |
| preserve_on_compact | bool | true, false |
| quality | null | null (never self-score) |
| tags | list | [memory_type, p10, {type}] |
| tldr | string<=160 | one-line description |

## Required Body Sections

| Section | Content | Min Length |
|---------|---------|-----------|
| Definition | What observations belong to this type, classification criteria | 2 sentences |
| Decay Policy | Formula, rationale, when pruned | 1 paragraph |
| Storage Rules | Location, naming, update-vs-append, compaction behavior | 3 bullet points |
| Examples | Concrete observations that ARE this type | 3 items |
| Anti-Examples | Observations that SEEM like this type but are NOT, with explanation | 2 items |

## Constraints

1. Total body <= 2048 bytes
2. One artifact per type (max 4 artifacts in entire system)
3. decay_rate must match type: correction=0.00, preference=0.01, convention=0.02, context=0.05

## Metadata

```yaml
id: bld_output_template_memory_type
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-output-template-memory-type.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_type]] | downstream | 0.39 |
| [[bld_instruction_memory_type]] | upstream | 0.34 |
| [[bld_system_prompt_memory_type]] | upstream | 0.33 |
| [[bld_config_memory_type]] | downstream | 0.32 |
| [[bld_collaboration_memory_type]] | downstream | 0.29 |
| [[bld_quality_gate_memory_type]] | downstream | 0.29 |
| [[bld_manifest_memory_type]] | upstream | 0.28 |
| [[bld_knowledge_card_memory_type]] | upstream | 0.28 |
| [[bld_architecture_memory_type]] | downstream | 0.27 |
| [[bld_examples_memory_type]] | downstream | 0.26 |
