---
kind: schema
id: bld_schema_pattern
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for pattern — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P08_architecture/_schema.yaml v4.0 + SEED_BANK.yaml + TAXONOMY_LAYERS.yaml
quality: 9.1
title: "Schema Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
  - bld_schema_action_prompt
  - bld_schema_prompt_version
  - bld_schema_pitch_deck
---

# Schema: pattern
## Frontmatter Fields (Required — 14)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_pat_{slug}) | YES | — | H02, H03 |
| kind | literal "pattern" | YES | — | H04 |
| pillar | literal "P08" | YES | — | H06 |
| version | semver X.Y.Z | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | H06 |
| updated | date YYYY-MM-DD | YES | — | H06 |
| author | string | YES | — | H06 |
| domain | string | YES | — | Architecture domain |
| quality | null | YES | null | H05 — never self-score |
| tags | list[string], len >= 3 | YES | — | H07 |
| tldr | string <= 160ch | YES | — | S01 |
| name | string | YES | — | Pattern name (H08) |
| problem | string | YES | — | What recurring problem (H09) |
| solution | string | YES | — | Core solution approach |
## Frontmatter Fields (Extended — 7)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| context | string | REC | When/where this pattern applies |
| forces | list[string] | REC | Tensions making the problem hard |
| consequences | list[string] | REC | Trade-offs of applying the pattern |
| related_patterns | list[string] | REC | Complementary or alternative patterns |
| anti_patterns | list[string] | REC | What NOT to do |
| applicability | string | REC | When to use / when not to use |
| keywords | list[string] | REC | Brain search terms |
## ID Pattern
Regex: `^p08_pat_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem (H02). Underscores only.
## Body Structure (required sections)
1. `## Problem` — the recurring problem in concrete terms
2. `## Context` — conditions and environment where problem occurs
3. `## Forces` — tensions that make the problem hard to solve
4. `## Solution` — the reusable approach (concrete, not abstract)
5. `## Consequences` — trade-offs (benefits AND costs)
6. `## Examples` — 2+ concrete applications of the pattern
7. `## Anti-Patterns` — common wrong approaches to the same problem
8. `## Related Patterns` — complementary, alternative, or prerequisite patterns
9. `## References` — sources, GoF/POSA/CEX refs
## Constraints
- max_bytes: 4096 (body)
- density_min: 0.80
- naming: p08_pat_{slug}.md
- id == filename stem
- name: clear, concise (2-5 words, e.g., "Continuous Batching")
- problem: must describe RECURRING situation, not one-off
- forces: list of at least 2 competing tensions
- consequences: must include at least 1 cost/drawback (not benefits-only)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_output_validator]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.60 |
| [[bld_schema_constraint_spec]] | sibling | 0.59 |
| [[bld_schema_chunk_strategy]] | sibling | 0.58 |
| [[bld_schema_smoke_eval]] | sibling | 0.58 |
| [[bld_schema_action_prompt]] | sibling | 0.58 |
| [[bld_schema_prompt_version]] | sibling | 0.58 |
| [[bld_schema_pitch_deck]] | sibling | 0.57 |
