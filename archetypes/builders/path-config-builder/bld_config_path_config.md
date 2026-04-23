---
kind: config
id: bld_config_path_config
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
title: "Config Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_path_config
  - p03_ins_path_config
  - bld_schema_path_config
  - bld_config_env_config
  - bld_output_template_path_config
  - bld_knowledge_card_path_config
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
---
# Config: path_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_path_{scope_slug}.yaml` | `p09_path_data_pipeline.yaml` |
| Builder directory | kebab-case | `path-config-builder/` |
| Frontmatter fields | snake_case | `base_dir`, `dir_count` |
| Scope slug | snake_case, lowercase, no hyphens | `data_pipeline`, `global`, `shaka` |
| Path names | snake_case | `base_dir`, `log_dir`, `config_dir` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_path_{scope_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_path_{scope_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80 (no filler)
## Path Template Conventions
| Pattern | Resolves to | Example |
|---------|------------|---------|
| `{{HOME}}` | User home directory | /home/user, C:\Users\user |
| `{{APP_ROOT}}` | Application root | /opt/app, C:\app |
| `{{TEMP}}` | System temp directory | /tmp, C:\Users\user\AppData\Local\Temp |
| `{{base_dir}}` | Scope base directory | Defined in artifact base_dir field |
## Platform Rules
| Platform | Separator | Long paths | Case |
|----------|-----------|------------|------|
| windows | \ (resolved at runtime) | \\?\ prefix for >260 chars | case-insensitive |
| unix | / | no limit (forctical) | case-sensitive |
| all | / in templates | handle per-platform | follow platform default |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_path_config]] | upstream | 0.40 |
| [[p03_ins_path_config]] | upstream | 0.39 |
| [[bld_schema_path_config]] | upstream | 0.39 |
| [[bld_config_env_config]] | sibling | 0.37 |
| [[bld_output_template_path_config]] | upstream | 0.36 |
| [[bld_knowledge_card_path_config]] | upstream | 0.35 |
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_config_retriever_config]] | sibling | 0.32 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_config_output_validator]] | sibling | 0.31 |
