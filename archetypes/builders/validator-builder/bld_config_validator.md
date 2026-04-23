---
kind: config
id: bld_config_validator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
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
title: "Config Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_validator
  - bld_knowledge_card_validator
  - bld_examples_validator
  - bld_output_template_validator
  - p03_ins_validator
  - p11_qg_validator
  - bld_collaboration_validator
  - p03_sp_validator-builder
  - bld_config_input_schema
  - bld_config_output_validator
---
# Config: validator Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_val_{rule_slug}.yaml` | `p06_val_kc_quality_null.yaml` |
| Builder directory | kebab-case | `validator-builder/` |
| Frontmatter fields | snake_case | `error_message`, `auto_fix` |
| Rule slugs | snake_case, lowercase | `kc_quality_null`, `id_prefix_check` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_val_{rule_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_val_{rule_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80
## Severity Enum
| Value | Meaning | Effect |
|-------|---------|--------|
| error | Blocks acceptance | Artifact cannot be committed/published |
| warning | Flags issue | Artifact accepted but flagged for review |
| info | Informational | Logged only, no blocking |
## Operator Enum
| Operator | Meaning | Example |
|----------|---------|---------|
| eq | Equals | `quality eq null` |
| ne | Not equals | `kind ne ""` |
| gt / lt | Greater/less than | `density_score gt 0.80` |
| gte / lte | Greater/less or equal | `version gte "1.0.0"` |
| regex | Regex match | `id regex "^p06_val_"` |
| in | Value in list | `severity in [error, warning, info]` |
| not_in | Value not in list | `author not_in [orchestrator]` |
| exists | Field exists | `tldr exists true` |
| type_check | Type assertion | `conditions type_check list` |
## Auto-Fix Policy
- auto_fix: true ONLY for deterministic, safe repairs (formatting, casing, null insertion)
- auto_fix: false for anything requiring semantic judgment
- When auto_fix: true, the fix MUST be documented in Error Handling section

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_validator]] | upstream | 0.40 |
| [[bld_knowledge_card_validator]] | upstream | 0.38 |
| [[bld_examples_validator]] | upstream | 0.36 |
| [[bld_output_template_validator]] | upstream | 0.36 |
| [[p03_ins_validator]] | upstream | 0.33 |
| [[p11_qg_validator]] | upstream | 0.32 |
| [[bld_collaboration_validator]] | upstream | 0.31 |
| [[p03_sp_validator-builder]] | upstream | 0.29 |
| [[bld_config_input_schema]] | sibling | 0.28 |
| [[bld_config_output_validator]] | sibling | 0.26 |
