---
kind: schema
id: bld_schema_knowledge_card
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema for knowledge_card — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P01_knowledge/_schema.yaml v4.0 + validate_kc.py v2.0 + 721 real KCs
quality: 9.1
title: "Schema Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_axiom
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_input_schema
  - bld_schema_action_prompt
  - bld_schema_smoke_eval
  - bld_schema_unit_eval
---

# Schema: knowledge_card
## Frontmatter Fields (Required — 14)
| Field | Type | Required | Default | Validator |
|-------|------|----------|---------|-----------|
| id | string (p01_kc_{slug}) | YES | — | H02, H03 |
| kind | literal "knowledge_card" | YES | — | H04 |
| pillar | literal "P01" | YES | — | H06 |
| title | string 5-100 chars | YES | — | H06, S03 |
| version | semver X.Y.Z | YES | "1.0.0" | H06, S04 |
| created | date YYYY-MM-DD | YES | — | H06, S05 |
| updated | date YYYY-MM-DD | YES | — | H06, S05 |
| author | string (not orchestrator) | YES | — | H06, H10 |
| domain | string | YES | — | H06 |
| quality | null | YES | null | H05 |
| tags | list[string], len 3-7 | YES | — | H07 |
| tldr | string <= 160 chars, must contain concrete data | YES | — | S01, S02 |
| when_to_use | string (specific context, not "when needed") | YES | — | H06 |
| axioms | list[string], len >= 1, ALWAYS/NEVER/IF-THEN form | YES | — | S18 |
## Frontmatter Fields (CEX Extended — 5)
| Field | Type | Required | Validator |
|-------|------|----------|-----------|
| keywords | list[string], len 2-5 (terms user would literally type) | REC | S16 |
| long_tails | list[string], len 2-3 (full natural-language phrases) | REC | S17 |
| linked_artifacts | object {primary, related} | REC | S14, S20 |
| density_score | float 0.80-1.00 | REC | — |
| data_source | URL or artifact ref | REC | S15 |
## ID Pattern
Regex: `^p01_kc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem (H02). Underscores only.
## Linked Artifacts Object
```yaml
linked_artifacts:
  primary: null            # or artifact_id
  related: [p01_kc_xxx]   # list of related ids
```
Both `primary` and `related` keys required (S20).
## Body Structure: domain_kc
1. `## Quick Reference` — yaml: topic, scope, owner, criticality
2. `## Key Concepts` — bullets >= 3, concrete examples
3. `## Strategy Phases` — numbered steps with outcomes
4. `## Golden Rules` — actionable rules >= 3
5. `## Flow` — text/ascii diagram
6. `## Comparativo` — comparison table
7. `## References` — artifact refs + URLs
## Body Structure: meta_kc
1. `## Executive Summary` — dense overview (2-3 sentences)
2. `## Spec Table` — key-value specs
3. `## Patterns` — what works
4. `## Anti-Patterns` — what fails
5. `## Application` — how to apply
6. `## References` — artifact refs + URLs
Density hierarchy (most to least info/token): tables > code blocks > bullet lists > ASCII diagrams > short paragraphs.
## Constraints
- max_bytes: 5120 (body) — H08. Covers 97%+ of 721 real KCs (p95=4274B)
- min_bytes: 200 — KCs below 200B are empty/stub
- min_bullets: 3
- density_min: 0.80
- bullet_max_chars: 80 — S10
- naming: p01_kc_{topic_slug}.md
- no internal paths (records/, .claude/, /home/) — H09
- no filler phrases — S09
- no self-references in tldr — S02

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.59 |
| [[bld_schema_axiom]] | sibling | 0.58 |
| [[bld_schema_retriever_config]] | sibling | 0.58 |
| [[bld_schema_output_validator]] | sibling | 0.57 |
| [[bld_schema_handoff_protocol]] | sibling | 0.57 |
| [[bld_schema_memory_scope]] | sibling | 0.57 |
| [[bld_schema_input_schema]] | sibling | 0.57 |
| [[bld_schema_action_prompt]] | sibling | 0.56 |
| [[bld_schema_smoke_eval]] | sibling | 0.56 |
| [[bld_schema_unit_eval]] | sibling | 0.56 |
