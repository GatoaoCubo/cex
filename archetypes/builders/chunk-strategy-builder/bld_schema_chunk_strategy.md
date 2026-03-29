---
kind: schema
id: bld_schema_chunk_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for chunk_strategy
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: chunk_strategy
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_chunk_{slug}) | YES | - | Namespace compliance |
| kind | literal "chunk_strategy" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| method | string | YES | - | Method |
| chunk_size | string | YES | - | Chunk size |
| chunk_overlap | string | YES | - | Chunk overlap |
| separators | string | YES | - | Separators |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "chunk_strategy" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| tokenizer | string | REC | - | Tokenizer |
| min_chunk_size | string | REC | - | Min chunk size |
| strip_whitespace | string | REC | - | Strip whitespace |
| keep_separator | string | REC | - | Keep separator |
## ID Pattern
Regex: `^p01_chunk_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Method` — method specification
3. `## Parameters` — parameters specification
4. `## Integration` — integration specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p01_chunk_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8
