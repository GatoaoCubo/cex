---
id: bld_sp_error_handling_software_project
kind: error_handling
pillar: P10
title: "Error Handling — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 8.8
tags: [builder, error-handling, software-project, recovery]
tldr: "Error handling for project builds: syntax errors (fix+retry), test failures (adjust fixtures), lint failures (auto-fix), Docker failures (simplify), deploy failures (rollback)."
density_score: 0.88
---

# Error Handling

## Build Failures

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Syntax error in .py | `py_compile` fails | Fix syntax, retry (max 2) |
| Missing import | ImportError in tests | Add to dependencies, retry |
| Test collection fails | `pytest --collect-only` returns 0 | Check conftest, fix fixtures |
| Lint errors | `ruff check` non-zero | Run `ruff check --fix`, retry |
| Type errors | `mypy` failures | Add type hints or `# type: ignore` |
| Docker build fails | `docker build` non-zero | Simplify Dockerfile, check deps |
| CI YAML invalid | YAML parse error | Validate with `python -c "import yaml; yaml.safe_load(...)"` |

## Recovery Strategy

```
Attempt 1: Build normally
  If FAIL → identify failing gate
  
Attempt 2: Fix specific failure
  Syntax: regenerate the failing file
  Tests: adjust conftest fixtures
  Lint: apply auto-fix (ruff --fix)
  Docker: fall back to single-stage
  
Attempt 3: Simplify
  Reduce scope (fewer files, simpler structure)
  Mark as DRAFT if still failing
  
After 3 attempts: STOP
  Save what works, flag failures
  Signal N07 for human review
```

## Deploy Failures

| Failure | Recovery |
|---------|----------|
| Railway deploy fails | Check logs, fix config, redeploy |
| Health check timeout | Increase start_period, check startup code |
| Database migration fails | Rollback migration, fix SQL |
| Out of memory | Reduce workers, optimize imports |
| Port conflict | Check PORT env var, use dynamic port |

## Rollback Protocol

```bash
# Railway
railway rollback

# Docker
docker-compose down
docker-compose up -d --build  # Rebuild from last working state

# Database
# Apply down migration
psql -f migrations/XXX_down.sql
```

## Signals

```yaml
# On failure
signal:
  type: build_failed
  nucleus: N03
  task: implement_pipeline
  gate_failed: G2_tests
  attempts: 2
  needs: human_review
```
