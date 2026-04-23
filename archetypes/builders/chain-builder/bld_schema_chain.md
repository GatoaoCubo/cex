---
kind: schema
id: bld_schema_chain
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for chain
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_action_prompt
  - bld_schema_workflow
  - bld_schema_quickstart_guide
  - bld_schema_search_strategy
  - bld_schema_golden_test
  - bld_schema_reranker_config
  - bld_schema_fallback_chain
  - bld_schema_usage_report
  - bld_schema_output_validator
  - bld_schema_unit_eval
---

# Schema: chain
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ch_{pipeline_slug}) | YES | - | Namespace compliance |
| kind | literal "chain" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable chain name |
| steps_count | integer | YES | - | Number of steps in body (must match) |
| flow | enum: sequential, branching, parallel, mixed | YES | "sequential" | Step arrangement |
| input_format | string | YES | - | What the first step receives |
| output_format | string | YES | - | What the last step produces |
| context_passing | enum: full, filtered, summary | REC | "full" | Inter-step context strategy |
| error_strategy | enum: fail_fast, skip, retry, fallback | REC | "fail_fast" | Chain-level error handling |
| domain | string | YES | - | Domain this chain belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "chain" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |
## ID Pattern
Regex: `^p03_ch_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Purpose` — why this chain exists, what transformation it performs
2. `## Steps` — numbered steps, each with Input/Prompt/Output subsections
3. `## Data Flow` — ASCII diagram showing step connections + context strategy
4. `## Error Handling` — strategy, failure behavior, retry policy
## Constraints
- max_bytes: 6144 (body only)
- naming: p03_ch_{pipeline_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- steps_count MUST match actual count of numbered steps in body
- Each step MUST define Input, Prompt, and Output
- Steps are TEXT transformations only — no agent spawns or tool calls
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_action_prompt]] | sibling | 0.65 |
| [[bld_schema_workflow]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.60 |
| [[bld_schema_reranker_config]] | sibling | 0.60 |
| [[bld_schema_fallback_chain]] | sibling | 0.59 |
| [[bld_schema_usage_report]] | sibling | 0.59 |
| [[bld_schema_output_validator]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
