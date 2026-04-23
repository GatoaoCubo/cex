---
kind: schema
id: bld_schema_chunk_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for chunk_strategy
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Chunk Strategy"
version: "1.0.0"
author: n03_builder
tags: [chunk_strategy, builder, examples]
tldr: "Golden and anti-examples for chunk strategy construction, demonstrating ideal structure and common pitfalls."
domain: "chunk strategy construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_prompt_version
  - bld_schema_effort_profile
  - bld_schema_usage_report
  - bld_schema_hook_config
  - bld_schema_golden_test
---

# Schema: chunk_strategy
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_chunk_{slug}) | YES | - | Namespace compliance |
| kind | literal "chunk_strategy" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| method | string | YES | - | Method |
| chunk_size | string | YES | - | Chunk size |
| chunk_overlap | string | YES | - | Chunk overlap |
| separators | string | YES | - | Separators |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "chunk_strategy" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| tokenizer | string | REC | - | Tokenizer |
| min_chunk_size | string | REC | - | Min chunk size |
| strip_whitespace | string | REC | - | Strip whitespace |
| keep_separator | string | REC | - | Keep separator |
## ID Pattern
Regex: `^p01_chunk_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Method` — method specification
3. `## Parameters` — parameters specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p01_chunk_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.78 |
| [[bld_schema_output_validator]] | sibling | 0.76 |
| [[bld_schema_handoff_protocol]] | sibling | 0.75 |
| [[bld_schema_memory_scope]] | sibling | 0.75 |
| [[bld_schema_constraint_spec]] | sibling | 0.75 |
| [[bld_schema_prompt_version]] | sibling | 0.73 |
| [[bld_schema_effort_profile]] | sibling | 0.71 |
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_hook_config]] | sibling | 0.68 |
| [[bld_schema_golden_test]] | sibling | 0.67 |
