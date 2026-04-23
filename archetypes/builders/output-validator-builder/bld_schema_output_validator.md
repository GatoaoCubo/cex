---
kind: schema
id: bld_schema_output_validator
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for output_validator
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_prompt_version
  - bld_schema_effort_profile
  - bld_schema_hook_config
  - bld_schema_smoke_eval
  - bld_schema_golden_test
---

# Schema: output_validator
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p05_oval_{slug}) | YES | - | Namespace compliance |
| kind | literal "output_validator" | YES | - | Type integrity |
| pillar | literal "P05" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| checks | string | YES | - | Checks |
| on_fail | string | YES | - | On fail |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "output_validator" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| retry_count | string | REC | - | Retry count |
| fix_prompt | string | REC | - | Fix prompt |
| severity | string | REC | - | Severity |
| applies_to | string | REC | - | Applies to |
## ID Pattern
Regex: `^p05_oval_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Checks` — checks specification
3. `## Failure Actions` — failure actions specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p05_oval_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.85

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.78 |
| [[bld_schema_handoff_protocol]] | sibling | 0.76 |
| [[bld_schema_memory_scope]] | sibling | 0.75 |
| [[bld_schema_constraint_spec]] | sibling | 0.75 |
| [[bld_schema_chunk_strategy]] | sibling | 0.74 |
| [[bld_schema_prompt_version]] | sibling | 0.74 |
| [[bld_schema_effort_profile]] | sibling | 0.72 |
| [[bld_schema_hook_config]] | sibling | 0.68 |
| [[bld_schema_smoke_eval]] | sibling | 0.68 |
| [[bld_schema_golden_test]] | sibling | 0.68 |
