---
kind: schema
id: bld_schema_dispatch_rule
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for dispatch_rule - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
version: 2.0.0
quality: 9.1
title: "Schema Dispatch Rule"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_dispatch_rule
  - bld_schema_search_strategy
  - bld_schema_constraint_spec
  - bld_schema_reranker_config
  - bld_schema_retriever_config
  - bld_schema_golden_test
  - bld_schema_handoff_protocol
  - bld_schema_action_paradigm
  - bld_schema_voice_pipeline
  - bld_schema_unit_eval
---

# Schema: dispatch_rule
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `dispatch_rule` |
| Machine format | `yaml` (frontmatter yaml + md body) |
| Naming | `p12_dr_{scope}.yaml` |
| Max bytes | 4096 |
## Required Fields (13)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, matches `^p12_dr_[a-z][a-z0-9_]+$` | YES | — | Unique rule identifier |
| kind | literal `dispatch_rule` | YES | — | Type discriminator |
| pillar | literal `P12` | YES | — | Pillar anchor |
| version | semver string | YES | — | Rule version |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update date |
| author | string | YES | — | Rule author |
| domain | string | YES | — | Subject domain of this rule |
| quality | null | YES | null | Always null at authoring time |
| tags | list[string], len >= 1 | YES | — | Searchable labels |
| tldr | string <= 120ch | YES | — | One-line summary |
| keywords | list[string], len 5-12 | YES | — | Trigger words; all OR-matched; cover synonyms + bilingual variants |
| target | string, lowercase slug | YES | — | Routing target (agent, service, or team) |
## Recommended Fields (5)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| model | enum: sonnet, opus, haiku, flash | REC | Target model preference |
| priority | integer 1-10, unique per scope | REC | Dispatch priority (10=highest); no fractions |
| confidence_threshold | float 0.5-1.0, default 0.75 | REC | Min confidence to trigger; below threshold routes to fallback |
| fallback | string, lowercase slug | REC | Alternative target; MUST differ from target (no self-fallback) |
| strategy | enum: keyword_match, semantic, hybrid | REC | Matching algorithm; default keyword_match |
## ID Pattern
```
^p12_dr_[a-z][a-z0-9_]+$
```
## Keyword Design Rules
| Principle | Example | Why |
|-----------|---------|-----|
| Cover synonyms | [build, create, implement] | Same intent, different words |
| Include abbreviations | [docs, documentation] | Short forms common |
| Bilingual variants | [researchr, research] | Multi-language systems |
| Avoid ambiguous words | NOT [run, do] | Too generic, false matches |
| Use verb forms | [deploy, deploying] | Intent = actions |
| Keep focused | 5-12 per rule | Too few = missed, too many = noise |
## Priority Scale
| Priority | Meaning | Examples |
|----------|---------|---------|
| 9-10 | Critical | orchestration, deploy, security |
| 7-8 | High | build, research |
| 5-6 | Normal | docs, indexing |
| 1-4 | Low | logging, archival |
Overlap resolution: (1) highest priority, (2) most keyword matches, (3) first defined.
## Body Structure (5 sections)
1. `## Routing Triad` — trigger (keywords + threshold) -> target -> fallback; the core decision
2. `## Keywords` — full keyword list with rationale for inclusion; synonym groups
3. `## Priority` — priority value with justification; conflict analysis vs adjacent rules
4. `## Fallback` — fallback target with rationale; why it differs from primary
5. `## Cross-Reference` — bidirectional links: upstream (who sends) and downstream (who receives)
## Semantic Rules
1. One dispatch_rule routes one scope domain to one target
2. `keywords` are the primary match signal; all items OR-matched
3. `priority` resolves conflicts when multiple rules match same input
4. `confidence_threshold` gates whether match fires; below threshold -> fallback
5. `fallback` MUST differ from `target` (no self-fallback)
6. `strategy=hybrid` combines keyword and semantic scoring
7. `quality: null` mandatory at authoring; scored only after deployment
## Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes | 4096 (body only) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_dispatch_rule]] | upstream | 0.49 |
| [[bld_schema_search_strategy]] | sibling | 0.48 |
| [[bld_schema_constraint_spec]] | sibling | 0.47 |
| [[bld_schema_reranker_config]] | sibling | 0.47 |
| [[bld_schema_retriever_config]] | sibling | 0.47 |
| [[bld_schema_golden_test]] | sibling | 0.47 |
| [[bld_schema_handoff_protocol]] | sibling | 0.47 |
| [[bld_schema_action_paradigm]] | sibling | 0.47 |
| [[bld_schema_voice_pipeline]] | sibling | 0.46 |
| [[bld_schema_unit_eval]] | sibling | 0.46 |
