---
kind: config
id: bld_config_env_config
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
quality: 9.1
title: "Config Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: env_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_env_{scope_slug}.yaml` | `p09_env_api_service.yaml` |
| Builder directory | kebab-case | `env-config-builder/` |
| Frontmatter fields | snake_case | `sensitive_count`, `override` |
| Scope slug | snake_case, lowercase, no hyphens | `api_service`, `global`, `shaka` |
| Variable names | UPPER_SNAKE_CASE | `DATABASE_URL`, `API_PORT` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P09_config/examples/p09_env_{scope_slug}.yaml`
2. Compiled: `cex/P09_config/compiled/p09_env_{scope_slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5500 bytes
3. Density: >= 0.80 (no filler)
## Environment Enum
| Value | When to use |
|-------|-------------|
| development | Local dev only variables |
| staging | Pre-production environment |
| production | Production environment |
| all | Variables needed in all environments (default) |
## Scope Conventions
| Scope | Prefix | Example |
|-------|--------|---------|
| global | CEX_ | CEX_LOG_LEVEL, CEX_DEBUG |
| agent_group | {DOMAIN}_ | RESEARCHER_API_KEY, BUILDER_MODEL |
| service | {SERVICE}_ | API_PORT, API_CORS_ORIGINS |

## Metadata

```yaml
id: bld_config_env_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-env-config.md
```
