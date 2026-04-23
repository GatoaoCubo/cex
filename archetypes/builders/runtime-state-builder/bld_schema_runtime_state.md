---
kind: schema
id: bld_schema_runtime_state
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for runtime_state
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_guardrail
  - bld_schema_usage_report
  - bld_schema_e2e_eval
  - bld_schema_smoke_eval
  - bld_schema_unit_eval
  - bld_schema_reranker_config
  - bld_schema_lifecycle_rule
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
---

# Schema: runtime_state
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_rs_{agent_slug}) | YES | — | Namespace compliance |
| kind | literal "runtime_state" | YES | — | Type integrity |
| pillar | literal "P10" | YES | — | Pillar assignment |
| title | string "Runtime State: {agent}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| agent | string | YES | — | Which agent this state belongs to |
| persistence | enum (session, cross_session) | YES | — | How long state lives |
| domain | string | YES | — | Domain this agent operates in |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
| routing_mode | enum (keyword, semantic, hybrid, rule_based) | YES | — | How routing decisions are made |
| priority_count | integer >= 1 | YES | — | Number of priorities defined |
| update_frequency | enum (per_task, per_session, on_trigger) | YES | — | When state updates |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| fallback_agent | string | REC | — | Who handles if this agent fails |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
| constraint_count | integer | REC | — | Number of constraints |
## ID Pattern
Regex: `^p10_rs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Agent Context` — which agent and its domain
2. `## Routing Rules` — how the agent routes tasks at runtime
3. `## Decision Tree` — branch conditions and outcomes
4. `## Priorities` — ordered list of optimization targets
5. `## Heuristics` — rules of thumb for ambiguous cases
6. `## Constraints` — limits on agent behavior
7. `## State Transitions` — what triggers state changes
## Constraints
- max_bytes: 3072 (body only)
- naming: p10_rs_{agent_slug}.md
- id == filename stem
- persistence MUST be valid enum
- routing_mode MUST be valid enum
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.62 |
| [[bld_schema_guardrail]] | sibling | 0.62 |
| [[bld_schema_usage_report]] | sibling | 0.61 |
| [[bld_schema_e2e_eval]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.61 |
| [[bld_schema_unit_eval]] | sibling | 0.61 |
| [[bld_schema_reranker_config]] | sibling | 0.61 |
| [[bld_schema_lifecycle_rule]] | sibling | 0.60 |
| [[bld_schema_search_strategy]] | sibling | 0.60 |
| [[bld_schema_quickstart_guide]] | sibling | 0.60 |
