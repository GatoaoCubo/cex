---
id: KC_N05_NIXPACKS_BUILDPACKS
kind: knowledge_card
pillar: P01
title: Nixpacks & Railpack — Auto-detection, Build Config, Python
domain: N05_operations
tags: [nixpacks, railpack, buildpack, python, build, deploy]
quality: 9.1
sources:
  - https://nixpacks.com/docs
  - https://nixpacks.com/docs/providers/python
created: 2026-04-01
related:
  - p01_kc_nixpacks_buildpacks
  - p01_kc_deploy_paas
  - p06_schema_railway_toml
  - bld_sp_tools_software_project
  - p02_agent_software_project_manifest
  - spec_zero_install
  - p05_output_railway_toml
  - p01_kc_ruff_uv
  - bld_sp_output_template_software_project
  - n05_readme_install
---

# Nixpacks & Railpack — Build Configuration

## 1. Status & Migration Note

> **Nixpacks is in maintenance mode** — not under active development.
> Railway's current default builder is **Railpack** (successor to Nixpacks).
> Configure builder in railway.toml:

```toml
[build]
builder = "RAILPACK"   # default, recommended
# builder = "NIXPACKS"  # legacy, still supported
```

Both share similar configuration philosophy. Patterns below apply to both unless noted.

## 2. Core Principles

- **Zero config by default** — auto-detects language and sets up build/start without any config file
- **Fully customizable** — every phase (install/build/start) can be overridden
- **Easily extensible** — new providers (languages) can be added with minimal Nix knowledge
- **20+ languages supported** — Python, Node, Go, Ruby, Java, PHP, Rust, Clojure, Zig, etc.

## 3. Auto-Detection Logic

Nixpacks/Railpack scans the repo root for indicator files:

| Language | Detection Files |
|----------|----------------|
| Python | `main.py`, `requirements.txt`, `pyproject.toml`, `Pipfile` |
| Node.js | `package.json` |
| Go | `go.mod` |
| Ruby | `Gemfile` |
| Java | `pom.xml`, `build.gradle` |
| PHP | `composer.json` |
| Rust | `Cargo.toml` |

Multiple providers detected → priority order applies (check Railpack docs for specifics).

## 4. Build Phases

```
┌─────────────────────────────────────┐
│  SETUP PHASE                        │
│  Install system packages (Nix/apt)  │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  INSTALL PHASE                      │
│  Install language dependencies      │
│  (pip install, npm install, etc.)   │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  BUILD PHASE                        │
│  Compile/bundle (npm run build, etc)│
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  START COMMAND                      │
│  Runtime entrypoint                 │
│  (gunicorn, node, etc.)             │
└─────────────────────────────────────┘
```

Each phase can be overridden via `nixpacks.toml`, env vars, or `Procfile`.

## 5. nixpacks.toml Configuration

```toml
# nixpacks.toml — place in repo root

[phases.setup]
nixPkgs = ["...", "ffmpeg"]          # Nix packages to install
aptPkgs = ["git", "curl"]            # apt packages (Ubuntu-based)

[phases.install]
cmds = ["pip install -r requirements.txt", "pip install gunicorn"]

[phases.build]
cmds = ["npm run build"]
cacheDirectories = [".cache", "node_modules"]

[start]
cmd = "gunicorn app:app --bind 0.0.0.0:$PORT"
```

### Environment Variable Overrides

```bash
# Override start command
NIXPACKS_START_CMD="python app.py"

# Override Python version
NIXPACKS_PYTHON_VERSION="3.11"

# Override package manager
NIXPACKS_PYTHON_PACKAGE_MANAGER="poetry"
```

### Procfile Support

```
# Procfile (alternative to nixpacks.toml start)
web: gunicorn app:app --bind 0.0.0.0:$PORT
worker: celery -A tasks worker
```

## 6. Python Provider (Detailed)

### Detection
Any of: `main.py`, `requirements.txt`, `pyproject.toml`, `Pipfile`

### Python Version Selection (Priority Order)
1. `NIXPACKS_PYTHON_VERSION` env var
2. `.python-version` file (e.g., `3.11.4`)
3. `runtime.txt` file (e.g., `python-3.11`)
4. `.tool-versions` file (asdf format: `python 3.11.4`)
5. Default: **Python 3.11**

Available versions: 2.7 through 3.13

### Package Manager Auto-Detection

| Lockfile Present | Manager Used |
|-----------------|--------------|
| `uv.lock` | uv |
| `poetry.lock` | poetry |
| `pdm.lock` | pdm |
| `Pipfile.lock` | pipenv |
| `requirements.txt` | pip |
| `pyproject.toml` (no lock) | setuptools |
| none | pip (empty) |

Override: `NIXPACKS_PYTHON_PACKAGE_MANAGER=poetry`

Options: `auto`, `requirements`, `setuptools`, `poetry`, `pdm`, `uv`, `pipenv`, `skip`

### Install Commands by Manager

```bash
# pip
pip install -r requirements.txt

# poetry
poetry install --no-dev --no-interactive --no-ansi

# uv
uv sync --frozen

# pdm
pdm install --prod

# pipenv
pipenv install --deploy
```

### Start Command Auto-Detection

| Condition | Start Command |
|-----------|---------------|
| Django detected | `python manage.py migrate && gunicorn project.wsgi` |
| `pyproject.toml` with module | `python -m {module_name}` |
| `main.py` exists | `python main.py` |

**Best practice:** Always specify explicitly via railway.toml or `Procfile`:
```toml
# railway.toml
[deploy]
startCommand = "gunicorn app:app --bind 0.0.0.0:$PORT --workers 2"
```

### Virtual Environment

- Created at `/opt/venv`
- PATH modified to use venv Python binary
- Persists between build phases

### Cache Directories (Persist Between Builds)

```
~/.cache/pip/
~/.cache/uv/
~/.cache/pdm/
```

### Default Environment Variables Set by Provider

```bash
PYTHONUNBUFFERED=1              # No output buffering (essential for logs)
PYTHONDONTWRITEBYTECODE=1       # Don't write .pyc files
PIP_NO_CACHE_DIR=false          # Cache enabled
PIP_DISABLE_PIP_VERSION_CHECK=1 # Suppress version warnings
```

## 7. Debugging Build Issues

```bash
# See what Nixpacks detects (run locally)
nixpacks plan .

# Force specific provider
NIXPACKS_PYTHON_VERSION=3.11 nixpacks build . --name myapp

# Check build logs in Railway
railway logs --build
```

**Common issues:**

| Problem | Cause | Fix |
|---------|-------|-----|
| Wrong Python version | No version pin | Add `.python-version` file |
| Wrong package manager | Multiple lockfiles | Set `NIXPACKS_PYTHON_PACKAGE_MANAGER` |
| Start command wrong | Django auto-detection | Explicit `startCommand` in railway.toml |
| Missing system lib | Nix/apt not configured | Add to `nixpacks.toml` phases.setup |
| Build succeeds, runtime fails | Missing env var | Check `$PORT` is used |

## 8. Node.js Provider (Reference)

```toml
[phases.install]
cmds = ["npm ci"]

[phases.build]
cmds = ["npm run build"]
cacheDirectories = ["node_modules", ".next/cache"]

[start]
cmd = "npm start"
```

Node version: pin via `.nvmrc`, `.node-version`, or `engines.node` in `package.json`.

## 9. Apt Packages (System Dependencies)

For packages not in Nix (Ubuntu-based builds):

```toml
[phases.setup]
aptPkgs = ["libpq-dev", "ffmpeg", "libmagic1", "wkhtmltopdf"]
```

Common needs:
- `libpq-dev` — psycopg2 compilation
- `libmagic1` — python-magic
- `ffmpeg` — audio/video processing
- `libssl-dev` — cryptography packages

## Anti-Patterns

- Do NOT rely on auto-detected start command for production — always be explicit
- Do NOT have multiple lockfiles (poetry.lock AND requirements.txt) — causes ambiguous detection
- Do NOT skip `.python-version` — default 3.11 may not match your dev environment
- Do NOT forget `$PORT` — Railway injects it; hardcoding port causes health check failures

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_nixpacks_buildpacks]] | sibling | 0.66 |
| [[p01_kc_deploy_paas]] | sibling | 0.38 |
| [[p06_schema_railway_toml]] | downstream | 0.38 |
| [[bld_sp_tools_software_project]] | downstream | 0.36 |
| [[p02_agent_software_project_manifest]] | downstream | 0.30 |
| [[spec_zero_install]] | related | 0.29 |
| [[p05_output_railway_toml]] | downstream | 0.29 |
| [[p01_kc_ruff_uv]] | sibling | 0.28 |
| [[bld_sp_output_template_software_project]] | downstream | 0.28 |
| [[n05_readme_install]] | downstream | 0.27 |
