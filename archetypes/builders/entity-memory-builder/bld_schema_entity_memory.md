---
kind: schema
id: bld_schema_entity_memory
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for entity_memory
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Entity Memory"
version: "1.0.0"
author: n03_builder
tags: [entity_memory, builder, examples]
tldr: "Golden and anti-examples for entity memory construction, demonstrating ideal structure and common pitfalls."
domain: "entity memory construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_memory_scope
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_constraint_spec
  - bld_schema_prompt_version
  - bld_schema_golden_test
  - bld_schema_chunk_strategy
  - bld_schema_enum_def
  - bld_schema_smoke_eval
---

# Schema: entity_memory
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_em_{slug}) | YES | - | Namespace compliance |
| kind | literal "entity_memory" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable entity name |
| entity_type | enum: person, tool, concept, organization, project, service | YES | - | Entity classification |
| attributes | map[string, string] | YES | - | Key-value facts about the entity |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "entity_memory" |
| tldr | string <= 160ch | YES | - | Dense summary |
| update_policy | enum: append, overwrite, merge, versioned | REC | merge | How facts are updated |
| source | string | REC | - | Where entity info originated |
| relationships | list[{entity, relation}] | REC | - | Links to other entities |
| confidence | float 0.0-1.0 | REC | - | Reliability of stored facts |
| last_referenced | date YYYY-MM-DD | REC | - | Last mention timestamp |
| expiry | date YYYY-MM-DD or null | REC | null | When to consider stale |
| description | string <= 200ch | REC | - | What entity this memory tracks |
## ID Pattern
Regex: `^p10_em_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what entity this memory tracks, purpose, scope
2. `## Attributes` — key-value facts table, types, sources
3. `## Relationships` — connections to other entities with relation types
4. `## Update Policy` — how facts are added, modified, or conflict-resolved
## Constraints
- max_bytes: 2048 (entity memory is richer than tools but still compact)
- naming: p10_entity_{scope}.md (single file per entity)
- machine_format: yaml (compiled artifact)
- id == filename stem
- attributes map MUST be non-empty (at least 1 key-value fact)
- entity_type MUST be one of the declared enum values
- quality: null always
- NO derived inferences in attributes — observed facts only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_retriever_config]] | sibling | 0.62 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.61 |
| [[bld_schema_constraint_spec]] | sibling | 0.60 |
| [[bld_schema_prompt_version]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
| [[bld_schema_chunk_strategy]] | sibling | 0.59 |
| [[bld_schema_enum_def]] | sibling | 0.58 |
| [[bld_schema_smoke_eval]] | sibling | 0.58 |
