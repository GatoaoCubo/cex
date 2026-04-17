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
quality: 9.1
tags: [builder, instruction, software-project, pipeline]
tldr: "9-step build pipeline: PARSE→SCAFFOLD→IMPLEMENT→TEST→LINT→DOCKER→CI→DEPLOY→REVIEW. Each step has inputs, outputs, and validation gates."
density_score: 0.92
llm_function: REASON
---
# Software Project Builder — Instruction

This ISO describes a software project: its repository layout, modules, and build graph.

## Build Pipeline (9 Steps)

### Step 1: PARSE (F1) — Intent → Project Spec
**Input**: Intent + ISOs + config → **Output**: `{name, type, python, deps, features}` YAML
**Gate**: type ∈ {cli_tool, api_service, pipeline_runner}
### Step 2: SCAFFOLD (F2) — Spec → Directory
**Output**: pyproject.toml + `src/{name}/` + `tests/conftest.py` + `.env.example`
**Gate**: pyproject.toml has [build-system], [project], [tool.ruff], [tool.pytest]
### Step 3: IMPLEMENT (F3) — Scaffold → Business Logic
**Output per archetype**:
- CLI tool: `cli.py` (Typer+Rich) — apply kc_pydantic_patterns
- API service: `api/main.py` (FastAPI) + routes/ + middleware/ — apply kc_fastapi_patterns
- Pipeline: `pipeline.py` (stage executor) — apply kc_error_handling_python
**Gate**: `python -m py_compile` on all .py
### Step 4: TEST (F4) — Implementation → Test Suite
**Output**: `conftest.py` (fixtures) + `test_{module}.py` + `test_integration.py`
Apply kc_pytest_patterns: markers, parametrize, coverage ≥60%.
**Gate**: `pytest --collect-only` finds >0 tests
### Step 5: LINT (F5) — Code → Clean Code
**Output**: Ruff + mypy config in pyproject.toml (from kc_ruff_uv)
**Gate**: `ruff check .` returns 0 errors
### Step 6: DOCKER (F6) — Project → Container
**Output**: Dockerfile (multi-stage, non-root, healthcheck) + compose + .dockerignore
Apply kc_docker_patterns. **Gate**: valid Dockerfile syntax
### Step 7: CI (F7) — Project → GitHub Actions
**Output**: `.github/workflows/ci.yml` (lint→test→build, cache, matrix)
Apply kc_github_actions. **Gate**: valid YAML, correct job refs
### Step 8: DEPLOY (F8) — Project → Deploy Config
**Output**: railway.toml | render.yaml | Procfile — apply kc_deploy_paas
**Gate**: Health check + start command configured
### Step 9: REVIEW (F8b) — Quality Report (7D rubric)
Correctness · Security · Performance · Readability · Tests · Docs · Architecture
Apply kc_code_review. Each dimension: ✅/⚠️/❌ with 1-line rationale.
## Pipeline Map
```
PARSE→SCAFFOLD→IMPLEMENT→TEST→LINT→DOCKER→CI→DEPLOY→REVIEW
 F1      F2       F3       F4   F5    F6    F7   F8    F8b
```

## Cross-References

- **Pillar**: P03 (Prompt)
- **Kind**: `instruction`
- **Artifact ID**: `bld_sp_instruction_software_project`
- **Tags**: [builder, instruction, software-project, pipeline]

## Builder Integration

| Aspect | Detail |
|--------|--------|
| ISO | 1 of 13 builder ISOs |
| Loader | `cex_skill_loader.py` |
| Pipeline | Injected at F3 (Compose) |
