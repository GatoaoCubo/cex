---
id: bld_config_naming_rule
pillar: P09
llm_function: CONSTRAIN
kind: config
domain: naming_rule
version: 1.0.0
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Naming Rule"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_naming_rule
  - p03_ins_naming_rule
  - bld_memory_naming_rule
  - bld_schema_naming_rule
  - bld_knowledge_card_naming_rule
  - bld_tools_naming_rule
  - bld_examples_naming_rule
  - naming-rule-builder
  - p03_sp_naming_rule_builder
  - bld_config_kind
---
# Config — Naming Rule Builder
## Artifact Naming
| Config | Value |
|--------|-------|
| Builder directory | `naming-rule-builder/` (kebab-case) |
| Output artifact naming | `p05_nr_{scope_slug}.md` |
| ID pattern | `^p05_nr_[a-z][a-z0-9_]+$` |
| Scope slug format | snake_case, lowercase, no hyphens |
| Scope slug max length | 40 characters |
## File Paths
| Artifact Location | Path Pattern |
|------------------|--------------|
| Pool output | `records/pool/p05/{id}.md` |
| Builder files | `archetypes/builders/naming-rule-builder/*.md` |
| Schema reference | `archetypes/builders/naming-rule-builder/SCHEMA.md` |
| Template reference | `archetypes/builders/naming-rule-builder/OUTPUT_TEMPLATE.md` |
## Size Limits
| Limit | Value |
|-------|-------|
| Max artifact bytes | 4096 |
| Max scope field length | 120 characters |
| Max tldr field length | 160 characters |
| Min keywords | 5 |
| Max keywords | 8 |
| Min tags | 3 |
| Min valid examples | 3 |
| Min invalid examples | 2 |
## Case Style Enum
| Value | Description | Separator |
|-------|-------------|-----------|
| `snake_case` | all lowercase, `_` separator | `_` |
| `kebab-case` | all lowercase, `-` separator | `-` |
| `camelCase` | no separator, first lower | none |
| `PascalCase` | no separator, all caps | none |
| `UPPER_SNAKE` | all uppercase, `_` separator | `_` |
## Collision Strategy Enum
| Value | Behavior |
|-------|----------|
| `append_sequence` | Append `_001`, `_002`, increment on collision |
| `append_hash` | Append `_{8hex}` content hash |
| `append_date` | Append `_YYYYMMDD` |
| `reject` | Raise error, do not create duplicate |
| `overwrite` | Replace existing artifact silently |
## Version Format
```
{major}.{minor}.{patch}
```
Initial version at creation: `1.0.0`
Breaking schema change: increment major
Additive field change: increment minor
Fix/clarification: increment patch
## Quality Field Rules
| Stage | Value |
|-------|-------|
| At creation | `null` — mandatory |
| Post-review (>= 7.0) | Float assigned by reviewer |
| Rejected (< 7.0) | Float assigned, artifact flagged for rework |
## Density Score Rules
| Stage | Value |
|-------|-------|
| At authoring | `REC` — recommended, not computed |
| Post-indexing | Float (0.0–1.0) computed by pool indexer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_naming_rule]] | upstream | 0.41 |
| [[p03_ins_naming_rule]] | upstream | 0.35 |
| [[bld_memory_naming_rule]] | downstream | 0.33 |
| [[bld_schema_naming_rule]] | upstream | 0.33 |
| [[bld_knowledge_card_naming_rule]] | upstream | 0.33 |
| [[bld_tools_naming_rule]] | upstream | 0.33 |
| [[bld_examples_naming_rule]] | upstream | 0.29 |
| [[naming-rule-builder]] | upstream | 0.27 |
| [[p03_sp_naming_rule_builder]] | upstream | 0.27 |
| [[bld_config_kind]] | sibling | 0.26 |
