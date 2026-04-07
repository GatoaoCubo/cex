---
kind: schema
id: bld_schema_prompt_version
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for prompt_version
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: prompt_version
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_pv_{slug}) | YES | - | Namespace compliance |
| kind | literal "prompt_version" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| prompt_ref | string | YES | - | Prompt ref |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "prompt_version" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| metrics | string | REC | - | Metrics |
| ab_group | string | REC | - | Ab group |
| parent_version | string | REC | - | Parent version |
| status | string | REC | - | Status |
| model_tested | string | REC | - | Model tested |
## ID Pattern
Regex: `^p03_pv_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Prompt Snapshot` — prompt snapshot specification
3. `## Metrics` — metrics specification
4. `## Lineage` — lineage specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p03_pv_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8
