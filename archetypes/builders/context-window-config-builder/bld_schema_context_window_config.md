---
kind: schema
id: bld_schema_context_window_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for context_window_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: context_window_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_cwc_{slug}) | YES | — | Namespace compliance |
| kind | literal "context_window_config" | YES | — | Type integrity |
| pillar | literal "P03" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| title | string | YES | — | Human-readable config name |
| target_model | string | YES | — | Which model this config targets |
| total_tokens | int | YES | — | Hard ceiling from model |
| system_prompt_budget | int | YES | 2000 | Tokens for system prompt |
| few_shot_budget | int | REC | 3000 | Tokens for few-shot examples |
| retrieved_context_budget | int | YES | 8000 | Tokens for RAG context |
| user_query_budget | int | REC | 1000 | Tokens for user input |
| output_reserve | int | YES | 4000 | Must reserve for response |
| overflow_strategy | enum (truncate_lowest/compress/drop_section) | YES | truncate_lowest | What happens on overflow |
| priority_tiers | list[string] | YES | [system, query, context, examples] | Protection order |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "context_window_config" |
| tldr | string <= 160ch | YES | — | Dense summary |
## ID Pattern
Regex: `^p03_cwc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Budget Allocation` — table of section → tokens → percentage
2. `## Priority Tiers` — ordered list of protection priority
3. `## Overflow Rules` — what happens when budget exceeded
4. `## Model Profile` — target model specs and limits
5. `## Integration` — how this connects to prompt assembly pipeline
