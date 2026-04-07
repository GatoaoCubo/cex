---
kind: schema
id: bld_schema_constraint_spec
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for constraint_spec
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: constraint_spec
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_constraint_{slug}) | YES | - | Namespace compliance |
| kind | literal "constraint_spec" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| constraint_type | string | YES | - | Constraint type |
| pattern | string | YES | - | Pattern |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "constraint_spec" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| provider_compat | string | REC | - | Provider compat |
| fallback | string | REC | - | Fallback |
| temperature_override | string | REC | - | Temperature override |
| max_tokens | string | REC | - | Max tokens |
## ID Pattern
Regex: `^p03_constraint_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Constraint Definition` — constraint definition specification
3. `## Provider Compatibility` — provider compatibility specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p03_constraint_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.85
