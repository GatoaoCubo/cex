---
kind: schema
id: bld_schema_memory_scope
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for memory_scope
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: memory_scope
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_memscope_{slug}) | YES | - | Namespace compliance |
| kind | literal "memory_scope" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Created date |
| updated | date YYYY-MM-DD | YES | - | Updated date |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable name |
| memory_types | string | YES | - | Memory types |
| backend | string | YES | - | Backend |
| ttl | string | YES | - | Ttl |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "memory_scope" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string | REC | - | Description |
| scope | string | REC | - | Scope |
| max_entries | string | REC | - | Max entries |
| eviction_policy | string | REC | - | Eviction policy |
| encryption | string | REC | - | Encryption |
| shared_with | string | REC | - | Shared with |
## ID Pattern
Regex: `^p02_memscope_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — overview specification
2. `## Memory Types` — memory types specification
3. `## Backend Config` — backend config specification
4. `## Lifecycle` — lifecycle specification
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_memscope_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- density_min: 0.8
