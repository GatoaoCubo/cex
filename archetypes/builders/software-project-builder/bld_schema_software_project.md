---
id: bld_sp_schema_software_project
kind: schema
pillar: P02
title: "Schema — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, schema, software-project, validation]
tldr: "Validation schema for software projects: required files, pyproject.toml fields, directory structure, test requirements, Docker constraints."
density_score: 0.88
llm_function: CONSTRAIN
related:
  - bld_sp_system_prompt_software_project
  - bld_sp_instruction_software_project
  - bld_sp_output_template_software_project
  - p04_tool_software_project
  - p01_kc_python_project_structure
  - bld_sp_quality_gate_software_project
  - bld_sp_knowledge_card_software_project
  - p04_tpl_software_project
  - bld_sp_examples_software_project
  - p12_wf_spec_to_code
---
# Software Project Schema

This ISO describes a software project: its repository layout, modules, and build graph.

## Required Files

| File | Required | Validation |
|------|----------|------------|
| pyproject.toml | ✅ | Must have [build-system], [project], [tool.ruff] |
| README.md | ✅ | Must have install + usage sections |
| src/{pkg}/__init__.py | ✅ | Must exist |
| tests/conftest.py | ✅ | Must have ≥1 fixture |
| .env.example | ✅ | Must list all env vars |
| Dockerfile | ⚠️ | Required for API/pipeline, optional for CLI |
| .github/workflows/ci.yml | ⚠️ | Required if GitHub repo |

## pyproject.toml Validation

```yaml
required_sections:
  - build-system.requires
  - build-system.build-backend
  - project.name
  - project.version
  - project.dependencies
  - tool.ruff
  - tool.pytest.ini_options

required_deps:
  dev: [pytest, ruff]
  api: [fastapi, uvicorn, pydantic]
  cli: [typer]

constraints:
  project.name: "^[a-z][a-z0-9-]{2,40}$"
  project.version: "^\\d+\\.\\d+\\.\\d+$"
  tool.ruff.line-length: ">=80, <=120"
```

## Directory Structure

```yaml
required_dirs:
  - src/{package}/
  - tests/

optional_dirs:
  - src/{package}/api/       # If API mode
  - src/{package}/core/      # Business logic
  - .github/workflows/       # If GitHub
  - docs/                    # Documentation

forbidden_patterns:
  - "*.pyc"
  - "__pycache__/"
  - ".env"          # Must be in .gitignore
  - "node_modules/"
```

## Test Requirements

```yaml
minimum_tests: 3
required_markers: [unit, integration]
fixture_requirements:
  - conftest.py must set ENV=test before app import
  - At least 1 shared fixture
coverage:
  minimum: 60
  branch: true
```

## Docker Validation

```yaml
dockerfile:
  must_have:
    - multi-stage (FROM ... AS builder, FROM ... AS runtime)
    - non-root USER
    - HEALTHCHECK
  must_not_have:
    - "COPY . ."  (without .dockerignore)
    - hardcoded secrets
    - apt-get without --no-install-recommends
```

## Security Checks

```yaml
no_secrets:
  patterns:
    - "password\\s*=\\s*['\"][^'\"]+['\"]"
    - "api_key\\s*=\\s*['\"][^'\"]+['\"]"
    - "sk-[a-zA-Z0-9]{20,}"
    - "ghp_[a-zA-Z0-9]{36}"
  allowed_in:
    - ".env.example"  # Only as placeholders
    - "tests/"        # Test-only keys
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_system_prompt_software_project]] | downstream | 0.45 |
| [[bld_sp_instruction_software_project]] | downstream | 0.45 |
| [[bld_sp_output_template_software_project]] | downstream | 0.41 |
| [[p04_tool_software_project]] | downstream | 0.38 |
| [[p01_kc_python_project_structure]] | upstream | 0.38 |
| [[bld_sp_quality_gate_software_project]] | downstream | 0.37 |
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.36 |
| [[p04_tpl_software_project]] | downstream | 0.35 |
| [[bld_sp_examples_software_project]] | downstream | 0.31 |
| [[p12_wf_spec_to_code]] | downstream | 0.31 |
