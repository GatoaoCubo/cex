---
kind: schema
id: bld_schema_enum_def
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for enum_def
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: enum_def
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_enum_{slug}) | YES | - | Namespace compliance |
| kind | literal "enum_def" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable enum name |
| values | list[string], len >= 2 | YES | - | Exact allowed values |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "enum_def" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the enum represents |
| default | string (must be in values) | REC | - | Default value if applicable |
| descriptions | map[string, string] | REC | - | Per-value descriptions |
| extensible | boolean | REC | false | Whether new values may be added |
| deprecated | list[string] | OPT | - | Values kept for compat, do not use |
| representations | map[string, string] | OPT | - | Framework-specific forms |
## ID Pattern
Regex: `^p06_enum_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the enum represents, domain context, who uses it
2. `## Values` — each value: name, description, when to use
3. `## Usage` — framework representations (JSON Schema, Pydantic, Zod, GraphQL, TypeScript)
4. `## Constraints` — default, extensibility, deprecation notes
## Constraints
- max_bytes: 1024 (body only — compact enum spec)
- naming: p06_enum_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- values list MUST match value names defined in ## Values section
- quality: null always
- NO implementation code in body — spec only
- All values in `deprecated` MUST also appear in `values`
