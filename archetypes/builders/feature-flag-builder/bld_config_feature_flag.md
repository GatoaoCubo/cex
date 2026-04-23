---
kind: config
id: bld_config_feature_flag
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
title: "Config Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_feature_flag
  - bld_output_template_feature_flag
  - bld_examples_feature_flag
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - feature-flag-builder
  - bld_knowledge_card_feature_flag
  - bld_config_output_validator
  - p03_sp_feature_flag_builder
---
# Config: feature_flag Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_ff_{feature_slug}.yaml` | `p09_ff_enable_vector_search.yaml` |
| Builder directory | kebab-case | `feature-flag-builder/` |
| Frontmatter fields | snake_case | `flag_name`, `default_state` |
| Feature slug | snake_case, lowercase, no hyphens | `enable_dark_mode`, `use_new_api` |
| Flag names | snake_case, verb prefix | `enable_*`, `use_*`, `show_*`, `allow_*` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_ff_{feature_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_ff_{feature_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 1536 bytes (tightest P09 kind)
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80 (no filler — every word counts at 1536)
## Category Reference
| Category | Default State | Lifecycle | Example |
|----------|--------------|-----------|---------|
| release | off | deploy -> ramp -> full -> retire | enable_vector_search |
| experiment | off | deploy -> measure -> decide -> retire | use_new_checkout_flow |
| ops | on | always on, OFF = emergency kill | enable_rate_limiting |
| permission | off | on for entitled users only | allow_premium_export |
## Flag Naming Conventions
| Prefix | Meaning | Example |
|--------|---------|---------|
| enable_ | Activate a feature | enable_dark_mode |
| use_ | Switch implementation | use_new_search |
| show_ | UI visibility toggle | show_beta_banner |
| allow_ | Permission-like toggle | allow_bulk_export |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_feature_flag]] | upstream | 0.36 |
| [[bld_output_template_feature_flag]] | upstream | 0.36 |
| [[bld_examples_feature_flag]] | upstream | 0.34 |
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_config_retriever_config]] | sibling | 0.33 |
| [[bld_config_prompt_version]] | sibling | 0.33 |
| [[feature-flag-builder]] | related | 0.32 |
| [[bld_knowledge_card_feature_flag]] | upstream | 0.32 |
| [[bld_config_output_validator]] | sibling | 0.32 |
| [[p03_sp_feature_flag_builder]] | upstream | 0.31 |
