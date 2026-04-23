---
kind: schema
id: bld_schema_search_tool
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for search_tool
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_constraint_spec
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_cli_tool
  - bld_schema_golden_test
  - bld_schema_chunk_strategy
  - bld_schema_prompt_version
  - bld_schema_smoke_eval
---

# Schema: search_tool
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_search_{provider_slug}) | YES | - | Namespace compliance |
| kind | literal "search_tool" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable tool name |
| provider | string | YES | - | Search provider (tavily, serper, perplexity, brave, exa, google) |
| search_type | enum: web, semantic, hybrid, news, images | YES | web | Primary search type |
| max_results | integer, >= 1 | YES | 10 | Maximum results per query |
| result_fields | list[string] | REC | [title, url, snippet] | Fields in each result |
| date_range | boolean | REC | false | Supports date filtering |
| domain_filter | boolean | REC | false | Supports domain whitelist/blacklist |
| language | list[string] | REC | ["en"] | Supported languages |
| cost_per_query | string | REC | - | Approximate cost per query |
| rate_limit | string | REC | - | Requests per minute/second |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "search_tool" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the tool does |
## ID Pattern
Regex: `^p04_search_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this search tool does, provider, use case
2. `## Query` — query parameters, syntax, filtering options
3. `## Results` — result structure, fields, ranking, pagetion
4. `## Provider` — provider-specific details, API key, rate limits, cost
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_search_{provider_slug}.md + .yaml (compiled)
- machine_format: yaml (compiled artifact)
- id == filename stem
- max_results MUST be >= 1
- quality: null always
- NO API keys or secrets in artifact — reference env vars only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.69 |
| [[bld_schema_constraint_spec]] | sibling | 0.67 |
| [[bld_schema_output_validator]] | sibling | 0.66 |
| [[bld_schema_handoff_protocol]] | sibling | 0.66 |
| [[bld_schema_memory_scope]] | sibling | 0.66 |
| [[bld_schema_cli_tool]] | sibling | 0.64 |
| [[bld_schema_golden_test]] | sibling | 0.64 |
| [[bld_schema_chunk_strategy]] | sibling | 0.64 |
| [[bld_schema_prompt_version]] | sibling | 0.64 |
| [[bld_schema_smoke_eval]] | sibling | 0.64 |
