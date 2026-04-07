---
kind: schema
id: bld_schema_hook_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for hook_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: hook_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_hookconf_{slug}) | YES | - | Namespace compliance |
| kind | literal "hook_config" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| target_builder | string | YES | - | Builder this config applies to |
| phases | list[string] | YES | - | 8F phases with bound hooks |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "hook_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| priority_mode | string | REC | - | How priority conflicts resolve (first-wins, last-wins, merge) |
| error_strategy | string | REC | - | What happens when a hook fails (halt, skip, retry) |
## ID Pattern
Regex: `^p04_hookconf_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview of hook lifecycle configuration
2. `## Hooks` — hook declaration table with phase, event, action, condition
3. `## Lifecycle` — execution order, error handling, retry behavior
4. `## Integration` — upstream/downstream pipeline connections
## Constraints
- max_bytes: 4096 (body only)
- naming: p04_hookconf_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8
