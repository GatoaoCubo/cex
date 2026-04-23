---
id: tpl_validation_schema
kind: validation_schema
pillar: P06
quality: 9.0
title: "Tpl Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for schema, demonstrating ideal structure and common pitfalls."
domain: "schema"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill
  - research_then_build
  - bld_config_tagline
  - bld_tools_prompt_cache
  - bld_tools_multi_modal_config
  - p04_ct_fix_frontmatter
  - bld_tools_memory_type
  - bld_tools_context_window_config
  - p06_td_quality_score
  - bld_tools_retriever_config
---
# {{title}}

## Rules
- {{rule}}

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: tpl_validation_schema
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply tpl-validation-schema.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `validation_schema` |
| Pillar | P06 |
| Domain | schema |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | downstream | 0.52 |
| [[research_then_build]] | downstream | 0.51 |
| [[bld_config_tagline]] | related | 0.37 |
| [[bld_tools_prompt_cache]] | upstream | 0.36 |
| [[bld_tools_multi_modal_config]] | upstream | 0.35 |
| [[p04_ct_fix_frontmatter]] | upstream | 0.34 |
| [[bld_tools_memory_type]] | upstream | 0.34 |
| [[bld_tools_context_window_config]] | upstream | 0.33 |
| [[p06_td_quality_score]] | related | 0.33 |
| [[bld_tools_retriever_config]] | upstream | 0.32 |
