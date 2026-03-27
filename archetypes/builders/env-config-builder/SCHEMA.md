---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for env_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: env_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_env_{scope_slug}) | YES | - | Namespace compliance |
| kind | literal "env_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Config scope: global, satellite name, or service name |
| variables | list[string], len >= 1 | YES | - | Variable names defined |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "env_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this config covers |
| environment | enum: development, staging, production, all | REC | all | Target environment |
| sensitive_count | integer | REC | - | Number of sensitive vars |
| override | string | REC | - | Override precedence summary |
| validation | string | REC | - | Validation strategy summary |

## ID Pattern
Regex: `^p09_env_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` — what scope, why these variables, who consumes them
2. `## Variable Catalog` — table: name, type, required, default, sensitive, validation
3. `## Override Precedence` — how values are resolved (env > file > default)
4. `## Sensitive Variables` — which vars are secrets, masking rules, storage guidance

## Constraints
- max_bytes: 4096 (body only — env configs can be larger)
- naming: p09_env_{scope_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- variables list MUST match variable names in ## Variable Catalog
- quality: null always
- NEVER include actual secret values — names and validation only
