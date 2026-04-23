---
kind: schema
id: bld_schema_lens
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for lens
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Lens"
version: "1.0.0"
author: n03_builder
tags: [lens, builder, examples]
tldr: "Golden and anti-examples for lens construction, demonstrating ideal structure and common pitfalls."
domain: "lens construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_action_prompt
  - bld_schema_constraint_spec
  - bld_schema_smoke_eval
  - bld_schema_chunk_strategy
  - bld_schema_unit_eval
  - bld_schema_golden_test
---

# Schema: lens
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_lens_{slug}) | YES | - | Namespace compliance |
| kind | literal "lens" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| perspective | string | YES | - | Name of the viewpoint |
| applies_to | list[string], len >= 1 | YES | - | Artifact kinds this lens filters |
| focus | string | YES | - | What this lens emphasizes |
| filters | list[string] | REC | [] | Attributes the lens highlights |
| bias | string or null | REC | null | Declared directional bias |
| interpretation | string | REC | - | How this lens reads artifacts |
| weight | float 0.0-1.0 | REC | 1.0 | Relative importance in multi-lens |
| priority | integer | REC | 0 | Ordering when multiple lenses apply |
| scope | string | REC | - | Boundaries of the perspective |
| domain | string | YES | - | Domain this lens belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "lens" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p02_lens_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Perspective` — what this lens sees and emphasizes
2. `## Filters` — specific attributes this lens highlights or suppresses
3. `## Application` — how to apply this lens to artifacts
4. `## Limitations` — what this lens misses or de-emphasizes
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_lens_{perspective_slug}.yaml
- machine_format: yaml
- id == filename stem
- perspective MUST be non-empty string
- applies_to MUST list at least 1 artifact kind
- quality: null always
- lens is a FILTER — no execution logic (that is agent)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.61 |
| [[bld_schema_memory_scope]] | sibling | 0.61 |
| [[bld_schema_action_prompt]] | sibling | 0.60 |
| [[bld_schema_constraint_spec]] | sibling | 0.59 |
| [[bld_schema_smoke_eval]] | sibling | 0.59 |
| [[bld_schema_chunk_strategy]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.59 |
