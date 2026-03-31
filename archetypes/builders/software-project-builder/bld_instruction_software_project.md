---
id: bld_sp_instruction_software_project
kind: instruction
pillar: P03
title: "Instruction — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 8.8
tags: [builder, instruction, software-project, pipeline]
tldr: "9-step build pipeline: PARSE→SCAFFOLD→IMPLEMENT→TEST→LINT→DOCKER→CI→DEPLOY→REVIEW. Each step has inputs, outputs, and validation gates."
density_score: 0.92
---

# Software Project Builder — Instruction

## Build Pipeline (9 Steps)

### Step 1: PARSE (Intent → Project Spec)

**Input**: Natural language intent + builder ISOs + instance config
**Output**: Structured project specification

```yaml
project:
  name: my-pipeline
  type: cli_tool | api_service | pipeline_runner
  python: "3.12"
  dependencies: [pydantic, httpx, typer]
  features: [auth, cache, retry]
```

### Step 2: SCAFFOLD (Spec → Directory Structure)

**Input**: Project spec
**Output**: pyproject.toml + directory tree

```
Generate:
  pyproject.toml     # From kc_python_project_structure
  src/{name}/        # Source package
    __init__.py
    __version__.py
    config.py        # Pydantic BaseSettings
  tests/
    conftest.py      # From kc_pytest_patterns
  .env.example       # Template env vars
```

**Gate**: pyproject.toml must have [build-system], [project], [tool.ruff], [tool.pytest]

### Step 3: IMPLEMENT (Scaffold → Business Logic)

**Input**: Scaffolded project + builder ISOs (architecture, instruction)
**Output**: Core implementation files

```
If CLI tool:     src/{name}/cli.py (Typer)
If API service:  src/{name}/api/main.py (FastAPI) + routes/ + middleware/
If pipeline:     src/{name}/pipeline.py (stage executor)
```

Apply patterns from: kc_fastapi_patterns, kc_pydantic_patterns, kc_error_handling_python

**Gate**: All .py files must have valid syntax (`python -m py_compile`)

### Step 4: TEST (Implementation → Test Suite)

**Input**: Implementation files
**Output**: Test files with fixtures

```
tests/
  conftest.py          # Shared fixtures (TestClient, auth, sample data)
  test_{module}.py     # Per-module tests
  test_integration.py  # Cross-module tests
```

Apply patterns from: kc_pytest_patterns (markers, parametrize, coverage)

**Gate**: `pytest --collect-only` must find >0 tests

### Step 5: LINT (Code → Clean Code)

**Input**: All .py files
**Output**: Ruff + mypy config in pyproject.toml

```toml
[tool.ruff]           # From kc_ruff_uv
[tool.ruff.lint]
[tool.mypy]           # Type checking config
```

**Gate**: `ruff check .` returns 0 errors

### Step 6: DOCKER (Project → Container)

**Input**: Project with all code
**Output**: Dockerfile + docker-compose.yml + .dockerignore

Apply patterns from: kc_docker_patterns (multi-stage, non-root, healthcheck)

**Gate**: `docker build .` succeeds (if Docker available)

### Step 7: CI (Project → GitHub Actions)

**Input**: Project config (test framework, deploy target)
**Output**: .github/workflows/ci.yml

Apply patterns from: kc_github_actions (lint→test→build, cache, matrix)

**Gate**: YAML is valid, jobs reference correct commands

### Step 8: DEPLOY (Project → Deploy Config)

**Input**: Deploy target (Railway, Render, Docker)
**Output**: railway.toml | render.yaml | Procfile

Apply patterns from: kc_deploy_paas

**Gate**: Health check path configured, start command correct

### Step 9: REVIEW (Project → Quality Report)

**Input**: Complete project
**Output**: Quality report (7D rubric)

Apply patterns from: kc_code_review (7-dimension rubric)

```
## Project Quality Report
- Correctness:  ✅ All logic implements spec
- Security:     ✅ No hardcoded secrets, auth on all endpoints
- Performance:  ✅ No N+1, bounded operations
- Readability:  ✅ Clear naming, small functions
- Tests:        ✅ Coverage > 60%, markers set
- Documentation: ✅ README, docstrings, .env.example
- Architecture:  ✅ Follows src layout, clean deps
```

## Quick Reference

```
PARSE → SCAFFOLD → IMPLEMENT → TEST → LINT → DOCKER → CI → DEPLOY → REVIEW
  F1       F2         F3        F4     F5      F6     F7     F8       F8
```
