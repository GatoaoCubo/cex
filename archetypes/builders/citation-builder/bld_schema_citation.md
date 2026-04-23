---
kind: schema
id: bld_schema_citation
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for citation
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_rl_algorithm
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
---

# Schema: citation
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_cit_{slug}) | YES | — | Namespace compliance |
| kind | literal "citation" | YES | — | Type integrity |
| pillar | literal "P01" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| title | string | YES | — | Source title |
| source_type | enum (web/paper/book/internal/api) | YES | web | Source classification |
| reliability_tier | enum (tier_1/tier_2/tier_3) | YES | tier_2 | Primary/secondary/tertiary |
| url | string (URL) | YES | — | Direct link for verification |
| date_accessed | date YYYY-MM-DD | YES | today | When source was accessed |
| excerpt | string | YES | — | Relevant 1-3 sentence quote |
| relevance_scope | list[string] | REC | [] | Domains/kinds this citation supports |
| domain | string | YES | — | Domain this citation belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "citation" |
| tldr | string <= 160ch | YES | — | Dense summary of source |
## ID Pattern
Regex: `^p01_cit_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Source` — full bibliographic info (author, title, publisher, date)
2. `## Excerpt` — key passage(s) from source
3. `## Relevance` — why this source matters, what claims it supports
4. `## Verification` — how to verify (DOI, URL, ISBN), freshness policy
5. `## Related` — linked citations, knowledge_cards, context_docs
## Constraints
- max_bytes: 2048
- naming: p01_cit_{topic_slug}.md
- source_type must be one of: web, paper, book, internal, api
- reliability_tier must be one of: tier_1, tier_2, tier_3
- excerpt must be 1-3 sentences (not the entire source)
- url must be a valid URL or artifact reference

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.63 |
| [[bld_schema_search_strategy]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_reranker_config]] | sibling | 0.61 |
| [[bld_schema_benchmark_suite]] | sibling | 0.61 |
| [[bld_schema_pitch_deck]] | sibling | 0.60 |
| [[bld_schema_rl_algorithm]] | sibling | 0.60 |
| [[bld_schema_integration_guide]] | sibling | 0.60 |
| [[bld_schema_sandbox_config]] | sibling | 0.59 |
