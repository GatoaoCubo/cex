---
id: p01_kc_ruff_uv
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Ruff + UV — Modern Python Tooling"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [ruff, uv, linting, formatting, python-tooling]
tldr: "Modern Python tooling: Ruff (linter+formatter, 100x faster than flake8+isort+black), UV (pip replacement, 10-100x faster installs). Config in pyproject.toml. Real config from codexa-core."
density_score: 0.91
related:
  - bld_sp_tools_software_project
  - bld_sp_output_template_software_project
  - bld_sp_schema_software_project
  - bld_sp_instruction_software_project
  - bld_sp_system_prompt_software_project
  - KC_N05_NIXPACKS_BUILDPACKS
  - p01_kc_python_project_structure
  - bld_sp_quality_gate_software_project
  - p01_kc_github_actions
  - spec_zero_install
---

# Ruff + UV

## Ruff (Linter + Formatter)

Replaces: flake8, isort, black, pylint, pycodestyle, pyflakes, bugbear.
Speed: 100x faster (Rust-based). Single tool for lint + format.

### pyproject.toml Config (from codexa-core)

```toml
[tool.ruff]
line-length = 100
target-version = "py310"
exclude = [".git", ".mypy_cache", "__pycache__", "build", "dist", "venv"]

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # unused arguments
    "SIM",    # simplify
    "TCH",    # type-checking imports
    "PTH",    # use pathlib
    "RUF",    # ruff-specific
]
ignore = [
    "E501",   # line too long (formatter handles)
    "B008",   # function calls in defaults (FastAPI pattern)
    "ARG001", # unused args (common in callbacks)
]

[tool.ruff.lint.isort]
known-first-party = ["mypackage"]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["ARG001", "ARG002", "S101"]
"**/__init__.py" = ["F401"]  # unused imports OK in __init__
```

### CLI Usage

```bash
# Lint (check)
ruff check .
ruff check src/ --output-format=github    # CI-friendly output

# Lint (fix)
ruff check --fix .

# Format (check only)
ruff format --check .

# Format (apply)
ruff format .
```

### CI Integration

```yaml
- name: Lint
  run: ruff check . --output-format=github
- name: Format check
  run: ruff format --check .
```

## UV (Fast Python Package Manager)

Replaces: pip, pip-tools, virtualenv.
Speed: 10-100x faster than pip (Rust-based, parallel downloads).

### Usage

```bash
# Create virtual environment
uv venv

# Install from pyproject.toml
uv pip install -e ".[dev]"

# Install from requirements
uv pip install -r requirements.txt

# Generate lockfile
uv pip compile pyproject.toml -o requirements.txt

# Sync (install exact versions from lockfile)
uv pip sync requirements.txt
```

### CI Integration

```yaml
- name: Install UV
  run: pip install uv
- name: Create venv
  run: uv venv
- name: Install deps
  run: uv pip install -e ".[ci]"
```

## mypy (Type Checking)

```toml
[tool.mypy]
python_version = "3.10"
strict = true
warn_return_any = true
ignore_missing_imports = true
disallow_untyped_defs = true
show_error_codes = true

[[tool.mypy.overrides]]
module = ["tests.*"]
disallow_untyped_defs = false
strict = false
```

### CLI

```bash
mypy src/mypackage/ --ignore-missing-imports
```

## Complete Toolchain

```
pyproject.toml          # ALL config (deps, lint, test, build)
├── uv venv             # Create env (100ms)
├── uv pip install      # Install deps (seconds, not minutes)
├── ruff check .        # Lint (milliseconds)
├── ruff format .       # Format (milliseconds)
├── mypy src/           # Type check (seconds)
├── pytest tests/       # Test (varies)
└── hatch build         # Package (seconds)
```

## Anti-Patterns

- ❌ Using flake8 + isort + black separately (Ruff does all 3)
- ❌ `pip install` in CI (UV is 10-100x faster)
- ❌ No `per-file-ignores` for tests (tests need different rules)
- ❌ `line-length = 79` (modern standard is 100-120)
- ❌ Running mypy with `strict = true` on tests (too noisy)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_tools_software_project]] | downstream | 0.48 |
| [[bld_sp_output_template_software_project]] | downstream | 0.39 |
| [[bld_sp_schema_software_project]] | downstream | 0.35 |
| [[bld_sp_instruction_software_project]] | downstream | 0.30 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.28 |
| [[KC_N05_NIXPACKS_BUILDPACKS]] | sibling | 0.28 |
| [[p01_kc_python_project_structure]] | sibling | 0.27 |
| [[bld_sp_quality_gate_software_project]] | downstream | 0.27 |
| [[p01_kc_github_actions]] | sibling | 0.25 |
| [[spec_zero_install]] | related | 0.24 |
