---
id: p04_tpl_software_project
kind: template
8f: F6_produce
pillar: P04
title: "Template — Software Project"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [template, software-project, python, scaffold]
tldr: "Generic Python project template with [PLACEHOLDERS]. Produces: pyproject.toml, src layout, conftest.py, Dockerfile, CI workflow, deploy config. All fields configurable."
density_score: 0.88
related:
  - p04_tool_software_project
  - bld_sp_knowledge_card_software_project
  - bld_sp_schema_software_project
  - bld_sp_instruction_software_project
  - bld_sp_system_prompt_software_project
  - bld_sp_examples_software_project
  - p02_agent_software_project_manifest
  - p01_kc_python_project_structure
  - p04_ex_software_project_cli_tool
  - bld_sp_output_template_software_project
---

# Software Project Template

## Configuration

```yaml
project:
  name: [PROJECT_NAME]
  version: [VERSION]
  description: [DESCRIPTION]
  type: [cli_tool|api_service|pipeline_runner]
  python: [PYTHON_VERSION]

package:
  name: [PACKAGE_NAME]
  cli_name: [CLI_NAME]

dependencies:
  core: [CORE_DEPS]
  dev: [DEV_DEPS]
  optional: [OPTIONAL_DEPS]

deploy:
  target: [railway|render|docker]
  port: [PORT]
  workers: [WORKERS]
  health_path: [HEALTH_PATH]

config:
  env_prefix: [ENV_PREFIX]
  settings:
    - name: [SETTING_NAME]
      type: [str|int|bool]
      default: [DEFAULT_VALUE]
      required: [true|false]
```

## File Generation Map

| Config Field | Generated File | Section |
|--------------|---------------|---------|
| project.name | pyproject.toml | [project].name |
| project.type | src/ structure | cli.py vs api/main.py vs pipeline.py |
| dependencies.core | pyproject.toml | [project].dependencies |
| deploy.target | railway.toml or render.yaml | Deploy config |
| config.settings | src/{pkg}/config.py | BaseSettings fields |
| config.env_prefix | .env.example | Variable prefixes |

## How To Use

1. Copy this template
2. Fill all [PLACEHOLDERS]
3. Run software-project-builder with filled config
4. Builder generates complete project

## Vertical Examples

| Vertical | Type | Key Deps |
|----------|------|----------|
| Research Pipeline | pipeline_runner | httpx, beautifulsoup4, pydantic |
| Social Publisher | cli_tool | httpx, typer, rich, pydantic |
| Billing Connector | api_service | fastapi, stripe, pydantic |
| Data Migrator | cli_tool | asyncpg, typer, pydantic |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_software_project]] | related | 0.41 |
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.41 |
| [[bld_sp_schema_software_project]] | upstream | 0.38 |
| [[bld_sp_instruction_software_project]] | upstream | 0.37 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.36 |
| [[bld_sp_examples_software_project]] | related | 0.33 |
| [[p02_agent_software_project_manifest]] | upstream | 0.32 |
| [[p01_kc_python_project_structure]] | upstream | 0.31 |
| [[p04_ex_software_project_cli_tool]] | related | 0.29 |
| [[bld_sp_output_template_software_project]] | downstream | 0.26 |
