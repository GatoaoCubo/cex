---
id: bld_sp_config_software_project
kind: config
pillar: P09
title: "Config — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [builder, config, software-project, defaults]
tldr: "Default configuration: Python 3.12, hatchling, ruff, pytest, Docker multi-stage, Railway deploy, GitHub Actions CI. All overridable via instance config."
density_score: 0.88
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
llm_function: CONSTRAIN
related:
  - bld_tools_prompt_cache
  - KC_N05_POSTGRESQL_RAILWAY
  - bld_collaboration_prompt_cache
  - bld_sp_instruction_software_project
  - bld_sp_system_prompt_software_project
  - skill
  - p01_kc_deploy_paas
  - research_then_build
  - bld_knowledge_card_feature_flag
  - p10_lr_env_config_builder
---
# Config

This ISO describes a software project: its repository layout, modules, and build graph.

## Defaults

```yaml
python_version: "3.12"
build_backend: hatchling
line_length: 100
test_framework: pytest
test_coverage_minimum: 60
lint_tool: ruff
type_checker: mypy
formatter: ruff
container: docker-multi-stage
deploy_target: railway
ci_provider: github-actions
package_manager: uv
```

## Override via Instance Config

```yaml
# _instances/{name}/N03_engineering/software_project_config.md
project_name: my-app
project_type: api_service  # cli_tool | api_service | pipeline_runner
python_version: "3.11"     # Override default
deploy_target: render      # Override railway
extra_deps:
  - celery>=5.3
  - asyncpg>=0.29
features:
  - auth
  - cache
  - rate_limit
  - webhooks
```

## Environment Variables Pattern

```
# .env.example (template)
APP_DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
APP_REDIS_URL=redis://localhost:6379/0
APP_API_KEYS=dev-key-123
APP_DEBUG=false
APP_LOG_LEVEL=info
APP_WORKERS=4
```

## Feature Flags

| Feature | Default | Adds |
|---------|---------|------|
| auth | off | APIKeyMiddleware, JWT handler |
| cache | off | Redis client, cache middleware |
| rate_limit | off | TenantRateLimitMiddleware |
| webhooks | off | Webhook routes, signature verification |
| celery | off | Worker, beat, Redis broker |
| monitoring | off | Prometheus metrics, health detail |

## Lifecycle

- Created via 8F pipeline (F1-Focus through F8-Furnish)
- Scored by `cex_score.py` (3-layer: structural + rubric + semantic)
- Compiled by `cex_compile.py` for validation
- Retrieved by `cex_retriever.py` for context injection
- Evolved by `cex_evolve.py` when quality drops below threshold

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_prompt_cache]] | upstream | 0.25 |
| [[KC_N05_POSTGRESQL_RAILWAY]] | upstream | 0.21 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.21 |
| [[bld_sp_instruction_software_project]] | upstream | 0.21 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.20 |
| [[skill]] | upstream | 0.19 |
| [[p01_kc_deploy_paas]] | upstream | 0.19 |
| [[research_then_build]] | upstream | 0.19 |
| [[bld_knowledge_card_feature_flag]] | upstream | 0.19 |
| [[p10_lr_env_config_builder]] | downstream | 0.19 |
