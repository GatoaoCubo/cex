---
id: bld_sp_manifest_software_project
kind: manifest
pillar: P03
title: "Manifest — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [builder, manifest, software-project, capabilities]
tldr: "Capability manifest: 8 verticals (scaffold, implement, test, lint, docker, ci, deploy, review), 12 platform KCs consumed, 23 CEX tools available, 3 output modes (CLI, API, pipeline)."
density_score: 0.89
keywords: [software-engineering, manifest, software-project, builder, capabilities]
triggers: ["create software-engineering", "build software-engineering artifact"]
capabilities: >
  L1: | Vertical | What It Does | Depends On |. L2: Max project complexity: 20 files. L3: When user needs to create, build, or scaffold software engineering.
llm_function: BECOME
---
# Software Project Builder — Manifest

This ISO describes a software project: its repository layout, modules, and build graph.

## Capabilities

| Vertical | What It Does | Depends On |
|----------|-------------|------------|
| **Scaffold** | pyproject.toml, src layout, CLI entry points | kc_python_project_structure |
| **Implement** | FastAPI routes, Pydantic models, business logic | kc_fastapi_patterns, kc_pydantic_patterns |
| **Test** | pytest fixtures, conftest, parametrize, coverage | kc_pytest_patterns |
| **Lint** | Ruff config, mypy, pre-commit hooks | kc_ruff_uv, kc_git_hooks_ci |
| **Docker** | Multi-stage Dockerfile, compose, .dockerignore | kc_docker_patterns |
| **CI/CD** | GitHub Actions workflows (lint→test→build→deploy) | kc_github_actions |
| **Deploy** | Railway, Render, nixpacks, Procfile | kc_deploy_paas |
| **Review** | PR review rubric, GitHub MCP, code review | kc_code_review |

## Knowledge Sources

| KC | Pillar | Status |
|----|--------|--------|
| kc_python_project_structure | P01/platform | ✅ |
| kc_pytest_patterns | P01/platform | ✅ |
| kc_github_actions | P01/platform | ✅ |
| kc_docker_patterns | P01/platform | ✅ |
| kc_fastapi_patterns | P01/platform | ✅ |
| kc_pydantic_patterns | P01/platform | ✅ |
| kc_deploy_paas | P01/platform | ✅ |
| kc_ruff_uv | P01/platform | ✅ |
| kc_git_hooks_ci | P01/platform | ✅ |
| kc_code_review | P01/platform | ✅ |
| kc_error_handling_python | P01/platform | ✅ |
| kc_security_forctices | P01/platform | ✅ |

## Output Modes

| Mode | When | Output |
|------|------|--------|
| **CLI tool** | `build cli-tool for X` | typer CLI + src/ + tests/ |
| **API service** | `build api for X` | FastAPI + middleware + routes |
| **Pipeline runner** | `build pipeline for X` | Stage-based executor (like 8F) |

## Boundary

- Max project complexity: 20 files
- Does NOT implement domain logic (that's the domain builder's job)
- Does NOT manage infrastructure (that's N05 Ops)
- Does NOT write marketing copy (that's N02)
- DOES create the skeleton, tests, CI/CD, Docker that domain builders fill
