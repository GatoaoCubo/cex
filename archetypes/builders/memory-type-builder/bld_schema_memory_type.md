---
kind: schema
id: bld_schema_memory_type
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema for memory_type artifacts
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_bugloop
  - bld_schema_context_window_config
  - bld_schema_sandbox_spec
---

# Schema: memory_type
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_mt_{slug}) | YES | - | Namespace |
| kind | literal "memory_type" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver | YES | "1.0.0" | Versioning |
| created | date | YES | - | Creation date |
| updated | date | YES | - | Last update |
| author | string | YES | - | Producer |
| type_name | enum: correction, preference, convention, context | YES | - | Memory category |
| decay_rate | float 0.0-1.0 | YES | - | Confidence decay per cycle |
| preserve_on_compact | boolean | YES | - | Survive context compression |
| quality | null | YES | null | Never self-score |
| tags | list[string] | YES | - | Must include "memory_type" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p10_mt_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Definition` -- what this memory type captures
2. `## Decay Policy` -- how confidence decays over time
3. `## Storage Rules` -- where and how stored
4. `## Examples` -- concrete examples of this type
## Constraints
- max_bytes: 2048
- naming: p10_mt_{type}.md
- machine_format: yaml
- type_name MUST be one of 4 enum values
- decay_rate 0.0 = permanent, 0.05 = fast decay

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_reranker_config]] | sibling | 0.62 |
| [[bld_schema_usage_report]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.61 |
| [[bld_schema_dataset_card]] | sibling | 0.60 |
| [[bld_schema_integration_guide]] | sibling | 0.59 |
| [[bld_schema_sandbox_config]] | sibling | 0.59 |
| [[bld_schema_bugloop]] | sibling | 0.58 |
| [[bld_schema_context_window_config]] | sibling | 0.58 |
| [[bld_schema_sandbox_spec]] | sibling | 0.58 |
