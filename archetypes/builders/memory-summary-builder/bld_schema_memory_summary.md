---
kind: schema
id: bld_schema_memory_summary
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for memory_summary
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_constraint_spec
  - bld_schema_action_prompt
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_chunk_strategy
  - bld_schema_unit_eval
---

# Schema: memory_summary
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_ms_{slug}) | YES | - | Namespace compliance |
| kind | literal "memory_summary" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable summary name |
| source_type | enum: conversation, session, multi_session, document | YES | - | What was compressed |
| compression_method | enum: abstractive, extractive, hybrid, sliding_window | YES | - | Compression strategy |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "memory_summary" |
| tldr | string <= 160ch | YES | - | Dense summary of the summary |
| max_tokens | integer | REC | - | Max output tokens for summary |
| trigger | enum: token_threshold, turn_count, explicit, time_based | REC | - | When summarization fires |
| source_window | integer | REC | - | Messages/turns to summarize |
| retain_entities | boolean | REC | true | Keep entity mentions |
| retain_timestamps | boolean | REC | false | Keep temporal markers |
| freshness_decay | float 0-1 | REC | 0.1 | Weight reduction over time |
| description | string <= 200ch | REC | - | What this summary captures |
## ID Pattern
Regex: `^p10_ms_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this summary does, when triggered, scope
2. `## Compression` — method, ratio, what is preserved vs dropped
3. `## Trigger` — when summarization fires, thresholds
4. `## Retention` — what is kept (entities, decisions, action items)
## Constraints
- max_bytes: 2048 (body only — memory artifacts are moderately compact)
- naming: p10_summary_{scope}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- source_type MUST match the actual input being compressed
- compression_method MUST be one of the four defined enums
- quality: null always
- NO raw conversation text in body — spec and metadata only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_handoff_protocol]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.62 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.62 |
| [[bld_schema_chunk_strategy]] | sibling | 0.62 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
