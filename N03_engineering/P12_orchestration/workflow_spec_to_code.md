---
id: p12_wf_spec_to_code
kind: workflow
pillar: P12
title: "Workflow — Spec to Code"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [workflow, spec-to-code, n03, implementation]
tldr: "7-step workflow transforming CEX builder specs into executable Python projects: load spec → resolve deps → scaffold → implement → test → validate → package."
density_score: 0.90
related:
  - bld_sp_instruction_software_project
  - bld_sp_schema_software_project
  - p12_wf_builder_8f_pipeline
  - p01_kc_n03_software_engineering
  - bld_architecture_kind
  - bld_sp_system_prompt_software_project
  - bld_instruction_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_output_template_builder
---

# Workflow: Spec to Code

## Trigger

```yaml
trigger: "implement [X] in Python" | handoff from N01/N02/N04/N06
input:
  builder_dir: archetypes/builders/{kind}-builder/
  instance_config: _instances/{name}/N0X_*/{kind}_config.md
  output_dir: projects/{kind}/
```

## Steps

### Step 1: Load Spec (2min)

```yaml
action: Read builder ISOs + instance config
reads:
  - bld_instruction_{kind}.md    # Pipeline steps
  - bld_architecture_{kind}.md   # Layer structure
  - bld_config_{kind}.md         # Default settings
  - bld_schema_{kind}.md         # Data models
  - bld_error_handling_{kind}.md # Error patterns
  - instance_config.md           # Company-specific settings
output: structured_spec
```

### Step 2: Resolve Dependencies (1min)

```yaml
action: Map spec requirements to Python packages
reads:
  - bld_tools_{kind}.md          # Tool requirements
  - kc_python_project_structure  # Packaging patterns
output:
  python_version: "3.12"
  dependencies: [pydantic, httpx, ...]
  dev_deps: [pytest, ruff, mypy]
  project_type: cli_tool | api_service | pipeline_runner
```

### Step 3: Scaffold (3min)

```yaml
action: Generate project skeleton
reads:
  - bld_output_template_software_project.md
  - kc_python_project_structure
produces:
  - pyproject.toml
  - src/{package}/__init__.py
  - src/{package}/config.py
  - tests/conftest.py
  - .env.example
  - README.md
```

### Step 4: Implement (15min)

```yaml
action: Generate business logic from spec
reads:
  - bld_instruction_{kind}.md    # Stage order
  - bld_architecture_{kind}.md   # Layer structure
  - kc_fastapi_patterns          # If API mode
  - kc_pydantic_patterns         # Data models
  - kc_error_handling_python     # Error patterns
produces:
  - src/{package}/pipeline.py    # Or api/main.py, cli.py
  - src/{package}/models.py
  - src/{package}/errors.py
  - src/{package}/core/*.py
```

### Step 5: Test (5min)

```yaml
action: Generate test suite
reads:
  - bld_examples_{kind}.md       # Test scenarios
  - kc_pytest_patterns           # Fixtures, parametrize
produces:
  - tests/test_core.py
  - tests/test_pipeline.py       # Or test_api.py, test_cli.py
  - tests/test_integration.py
gate: pytest --collect-only finds ≥3 tests
```

### Step 6: Validate (3min)

```yaml
action: Run quality gates
checks:
  - python -m py_compile (all .py)
  - ruff check . (lint)
  - pytest --collect-only (tests exist)
  - secret scan (no hardcoded keys)
gate: All 4 checks pass
retry: max 2 if any fail
```

### Step 7: Package (3min)

```yaml
action: Add deploy infrastructure
reads:
  - kc_docker_patterns
  - kc_github_actions
  - kc_deploy_paas
produces:
  - Dockerfile
  - docker-compose.yml
  - .github/workflows/ci.yml
  - railway.toml | render.yaml
signal: completion to N07
```

## Total Time: ~30min per project

## Failure Escalation

```
Step fail → retry (max 2)
  → still fail → simplify (reduce scope)
    → still fail → DRAFT + signal N07
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_instruction_software_project]] | upstream | 0.35 |
| [[bld_sp_schema_software_project]] | upstream | 0.29 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.28 |
| [[p01_kc_n03_software_engineering]] | upstream | 0.28 |
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.27 |
| [[bld_instruction_kind]] | upstream | 0.26 |
| [[kind-builder]] | upstream | 0.26 |
| [[bld_collaboration_kind]] | related | 0.25 |
| [[bld_output_template_builder]] | upstream | 0.24 |
