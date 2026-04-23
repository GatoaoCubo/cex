---
id: bld_sp_output_template_software_project
kind: output_template
pillar: P06
title: "Output Template — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, output-template, software-project]
tldr: "Standard output structure: pyproject.toml skeleton, src layout, conftest.py, Dockerfile, CI workflow. All [PLACEHOLDERS] for costmization."
density_score: 0.88
llm_function: PRODUCE
related:
  - bld_sp_schema_software_project
  - bld_sp_examples_software_project
  - p01_kc_docker_patterns
  - bld_sp_system_prompt_software_project
  - p01_kc_ruff_uv
  - p04_output_github_actions
  - p01_kc_python_project_structure
  - p01_kc_pytest_patterns
  - p01_kc_github_actions
  - bld_sp_instruction_software_project
---
# Output Template

This ISO describes a software project: its repository layout, modules, and build graph.

## pyproject.toml

```toml
[build-system]
requires = ["hatchling>=1.21.0"]
build-backend = "hatchling.build"

[project]
name = "[PROJECT_NAME]"
version = "[VERSION]"
description = "[DESCRIPTION]"
requires-python = ">=3.10"
dependencies = [
    [DEPENDENCIES]
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "pytest-cov>=4.0", "ruff>=0.1.0"]

[project.scripts]
[CLI_NAME] = "[PACKAGE].cli:app"

[tool.ruff]
line-length = 100
[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "UP", "SIM"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["-v", "--tb=short", "--strict-markers"]
markers = ["slow: slow tests", "integration: external deps"]
```

## src/[PACKAGE]/__init__.py

```python
"""[DESCRIPTION]"""
__version__ = "[VERSION]"
```

## src/[PACKAGE]/config.py

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {"env_prefix": "[PREFIX]_", "env_file": ".env"}
    [CONFIG_FIELDS]

settings = Settings()
```

## tests/conftest.py

```python
import os
import pytest
os.environ["ENV"] = "test"
[TEST_ENV_VARS]

@pytest.fixture
def [MAIN_FIXTURE]():
    [FIXTURE_BODY]
```

## Dockerfile

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /build
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM python:3.12-slim
RUN groupadd --gid 1000 app && useradd --uid 1000 --gid app app
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" PYTHONUNBUFFERED=1
COPY --chown=app:app src/ ./src/
EXPOSE [PORT]
HEALTHCHECK CMD curl -f http://localhost:[PORT]/health || exit 1
USER app
CMD [START_COMMAND]
```

## .github/workflows/ci.yml

```yaml
name: CI
on: [push, pull_request]
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12', cache: 'pip' }
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest --cov -m "not slow"
```

## Cross-References

- **Pillar**: P06 (Schema)
- **Kind**: `output template`
- **Artifact ID**: `bld_sp_output_template_software_project`
- **Tags**: [builder, output-template, software-project]

## Output Pipeline

| Aspect | Detail |
|--------|--------|
| Template | Defines structure for output template outputs |
| Validation | Checked against `validation_schema` |
| Post-hook | Scored by `cex_score.py` after creation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_schema_software_project]] | upstream | 0.45 |
| [[bld_sp_examples_software_project]] | upstream | 0.38 |
| [[p01_kc_docker_patterns]] | upstream | 0.36 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.36 |
| [[p01_kc_ruff_uv]] | upstream | 0.35 |
| [[p04_output_github_actions]] | upstream | 0.34 |
| [[p01_kc_python_project_structure]] | upstream | 0.34 |
| [[p01_kc_pytest_patterns]] | upstream | 0.33 |
| [[p01_kc_github_actions]] | upstream | 0.33 |
| [[bld_sp_instruction_software_project]] | upstream | 0.32 |
