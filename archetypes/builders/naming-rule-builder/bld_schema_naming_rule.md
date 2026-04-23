---
id: bld_schema_naming_rule
pillar: P06
llm_function: CONSTRAIN
kind: schema
domain: naming_rule
version: 1.0.0
quality: 9.1
title: "Schema Naming Rule"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_integration_guide
  - bld_schema_customer_segment
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_spec
---

# Schema — Naming Rule (SOURCE OF TRUTH)
## ID Pattern
```
^p05_nr_[a-z][a-z0-9_]+$
```
Examples of valid IDs: `p05_nr_knowledge_card`, `p05_nr_signal`, `p05_nr_builder_dir`
Examples of invalid IDs: `p05_nr_KnowledgeCard` (uppercase), `p05_nr_-signal` (hyphen after prefix), `nr_knowledge_card` (missing pillar prefix)
## Field Definitions
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| id | string | yes | Must match `^p05_nr_[a-z][a-z0-9_]+$` |
| kind | string | yes | Fixed value: `naming_rule` |
| pillar | string | yes | Fixed value: `P05` |
| version | string | yes | Semver: `{major}.{minor}.{patch}` |
| created | string | yes | ISO date: `"YYYY-MM-DD"` |
| updated | string | yes | ISO date: `"YYYY-MM-DD"`, >= created |
| author | string | yes | Agent_group ID or human handle |
| scope | string | yes | One sentence, max 120 chars, describes what is named |
| pattern | string | yes | Valid regex, must match all valid examples |
| prefix | string | yes | Fixed prefix string; may be empty string `""` if none |
| suffix | string\|null | yes | Fixed suffix or `null` |
| separator | string | yes | Single char: `_` or `-` |
| case_style | enum | yes | One of: `snake_case`, `kebab-case`, `camelCase`, `PascalCase`, `UPPER_SNAKE` |
| versioning | string\|null | yes | Description of version embedding or `null` |
| collision_strategy | enum | yes | One of: `append_sequence`, `append_hash`, `append_date`, `reject`, `overwrite` |
| domain | string | yes | Domain slug, lowercase snake_case |
| quality | float\|null | yes | Null at creation; assigned post-review (0.0–10.0) |
| tags | list[string] | yes | Min 3 tags, lowercase kebab-case |
| tldr | string | yes | One sentence summary, max 160 chars |
| keywords | list[string] | yes | 5–8 terms, lowercase |
| density_score | string\|float | yes | `REC` at authoring time; float post-review |
## Body Structure (4 Required Sections)
```
## Scope
## Pattern Definition
## Examples
## Collision Resolution
```
All four sections MUST be present. No additional top-level sections required but permitted.
## Constraints
| Constraint | Value |
|------------|-------|
| Max file size | 4096 bytes |
| Min valid examples | 3 |
| Min invalid examples | 2 |
| Pattern type | Regex (not glob-only) |
| quality at creation | Must be `null` |
| density_score at creation | Must be `REC` |
| case_style | Must use exact enum values from allowed list |
| collision_strategy | Must use exact enum values from allowed list |
## Enum Values
**case_style**:
- `snake_case` — segments joined by `_`, all lowercase
- `kebab-case` — segments joined by `-`, all lowercase
- `camelCase` — first segment lowercase, subsequent capitalized, no separator
- `PascalCase` — all segments capitalized, no separator
- `UPPER_SNAKE` — segments joined by `_`, all uppercase
**collision_strategy**:
- `append_sequence` — append `_001`, `_002`, etc.
- `append_hash` — append `_{8hex}`
- `append_date` — append `_YYYYMMDD`
- `reject` — refuse to create; surface error to caller
- `overwrite` — replace existing artifact silently
## Drift Check
Every field in this schema MUST appear in `OUTPUT_TEMPLATE.md`. Run drift check before publishing:
```
Grep: pattern="{{" path=OUTPUT_TEMPLATE.md
```
Cross-reference each `{{var}}` against fields above. Zero drift permitted.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.62 |
| [[bld_schema_customer_segment]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.61 |
| [[bld_schema_pitch_deck]] | sibling | 0.61 |
| [[bld_schema_quickstart_guide]] | sibling | 0.61 |
| [[bld_schema_sandbox_spec]] | sibling | 0.61 |
