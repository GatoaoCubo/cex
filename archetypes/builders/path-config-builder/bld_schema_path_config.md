---
kind: schema
id: bld_schema_path_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for path_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_env_config
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_smoke_eval
  - bld_schema_handoff_protocol
  - bld_schema_golden_test
  - bld_schema_constraint_spec
  - bld_schema_usage_report
  - bld_schema_action_prompt
---

# Schema: path_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_path_{scope_slug}) | YES | - | Namespace compliance |
| kind | literal "path_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Config scope: global, agent_group, service |
| paths | list[string], len >= 1 | YES | - | Path names defined |
| platform | enum: windows, unix, all | YES | all | Target platform |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "path_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What these paths cover |
| base_dir | string | REC | - | Root directory for relative paths |
| dir_count | integer | REC | - | Number of directory paths |
| file_count | integer | REC | - | Number of file paths |
## ID Pattern
Regex: `^p09_path_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — scope, purpose, platform, base directory, consumers
2. `## Path Catalog` — table: name, type (dir/file), platform, default, required, notes
3. `## Directory Hierarchy` — ASCII tree showing parent-child path relationships
4. `## Platform Notes` — platform-specific path differences, resolution rules
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_path_{scope_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- paths list MUST match path names in ## Path Catalog
- quality: null always
- NEVER include user-specific absolute paths (use expandable vars)
- Forward slashes in templates (normalize at runtime)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.60 |
| [[bld_schema_env_config]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.59 |
| [[bld_schema_output_validator]] | sibling | 0.59 |
| [[bld_schema_smoke_eval]] | sibling | 0.59 |
| [[bld_schema_handoff_protocol]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_constraint_spec]] | sibling | 0.58 |
| [[bld_schema_usage_report]] | sibling | 0.58 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
