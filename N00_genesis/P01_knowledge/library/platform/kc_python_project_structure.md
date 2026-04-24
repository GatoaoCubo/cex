---
id: p01_kc_python_project_structure
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Python Project Structure — pyproject.toml + Hatchling"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [python, pyproject, hatchling, packaging, project-structure]
tldr: "Modern Python project anatomy: pyproject.toml as single source of truth, hatchling build backend, src layout, extras, CLI entry points, and dev environments."
density_score: 0.91
related:
  - bld_sp_schema_software_project
  - bld_sp_knowledge_card_software_project
  - bld_sp_system_prompt_software_project
  - p04_tpl_software_project
  - bld_sp_output_template_software_project
  - bld_sp_instruction_software_project
  - p04_ex_software_project_cli_tool
  - bld_sp_examples_software_project
  - p04_tool_software_project
  - p02_agent_software_project_manifest
---

# Python Project Structure

## pyproject.toml — Single Source of Truth

Modern Python projects use `pyproject.toml` (PEP 621) for ALL config.
No more `setup.py`, `setup.cfg`, `MANIFEST.in`, or `requirements.txt` for deps.

### Build System

```toml
[build-system]
requires = ["hatchling>=1.21.0"]
build-backend = "hatchling.build"
```

**Why Hatchling**: Fastest build backend. No C compilation needed.
Alternatives: setuptools (legacy), flit (simple), maturin (Rust).

### Project Metadata

```toml
[project]
name = "my-package"
version = "2.0.0"
description = "Short description"
readme = "README.md"
license = "MIT"
requires-python = ">=3.10"
authors = [{ name = "Team", email = "dev@example.com" }]
keywords = ["ai", "agents", "framework"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Framework :: FastAPI",
    "Programming Language :: Python :: 3.12",
    "Typing :: Typed",
]
```

### Dependencies (Tiered)

```toml
# Core — always installed
dependencies = [
    "pydantic>=2.0.0",
    "httpx>=0.24.0",
    "typer>=0.9.0",
    "rich>=13.0.0",
    "pyyaml>=6.0",
]

# Optional groups — pip install package[api]
[project.optional-dependencies]
api = ["fastapi>=0.100.0", "uvicorn[standard]>=0.23.0"]
brain = ["sentence-transformers>=2.2.0", "faiss-cpu>=1.7.4"]
dev = ["pytest>=7.0", "pytest-cov>=4.0", "ruff>=0.1.0", "mypy>=1.5"]
ci = ["pytest>=7.0", "ruff>=0.1.0"]
all = ["fastapi>=0.100.0", "uvicorn>=0.23.0", "httpx>=0.24.0"]
```

**Pattern**: `core` (minimal) → `extras` (feature flags) → `all` (everything) → `dev` (testing/lint).

### CLI Entry Points

```toml
[project.scripts]
myapp = "mypackage.cli:main"
myapp-local = "mypackage.local.cli:main"
```

### Plugin System

```toml
[project.entry-points."myapp.plugins"]
local_llm = "mypackage.plugins.local_llm:LocalLLM"
dashboard = "mypackage.plugins.dashboard:Dashboard"
```

## Directory Layout (src layout)

```
project/
├── pyproject.toml          # ALL config
├── README.md
├── LICENSE
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/      # CI/CD
├── src/mypackage/          # Source code (src layout)
│   ├── __init__.py
│   ├── __version__.py      # Single version source
│   ├── cli.py              # Typer CLI
│   ├── core/               # Business logic
│   ├── api/                # FastAPI routes
│   └── plugins/            # Plugin system
├── tests/                  # Tests (outside src)
│   ├── conftest.py
│   ├── test_core/
│   └── test_api/
└── docs/
```

**Key**: Source in `src/` prevents accidental imports from project root.

## Hatchling Build Config

```toml
[tool.hatch.version]
path = "src/mypackage/__version__.py"
pattern = "__version__ = ['\"](?P<version>[^'\"]+)['\"]"

[tool.hatch.build.targets.sdist]
include = ["/src", "/pyproject.toml", "/README.md"]

[tool.hatch.build.targets.wheel]
packages = ["src/mypackage"]

[tool.hatch.envs.default.scripts]
test = "pytest {args:tests}"
test-cov = "pytest --cov=src/mypackage --cov-report=term-missing"
```

## Anti-Patterns

- ❌ `setup.py` without `pyproject.toml` (legacy)
- ❌ `requirements.txt` as dependency source (use `dependencies = [...]`)
- ❌ Version scattered across multiple files
- ❌ Source code at project root (no `src/` layout)
- ❌ Dev dependencies in core deps

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_schema_software_project]] | downstream | 0.53 |
| [[bld_sp_knowledge_card_software_project]] | sibling | 0.46 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.42 |
| [[p04_tpl_software_project]] | downstream | 0.42 |
| [[bld_sp_output_template_software_project]] | downstream | 0.41 |
| [[bld_sp_instruction_software_project]] | downstream | 0.39 |
| [[p04_ex_software_project_cli_tool]] | downstream | 0.37 |
| [[bld_sp_examples_software_project]] | downstream | 0.36 |
| [[p04_tool_software_project]] | downstream | 0.34 |
| [[p02_agent_software_project_manifest]] | downstream | 0.32 |
