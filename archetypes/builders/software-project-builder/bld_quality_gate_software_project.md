---
id: bld_sp_quality_gate_software_project
kind: quality_gate
pillar: P07
title: "Quality Gate — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, quality-gate, software-project, validation]
tldr: "8 hard gates for software projects: syntax valid, tests pass, lint clean, no secrets, Docker builds, CI valid, health endpoint exists, deps audited. Must pass all 8 for ≥8.0."
density_score: 1.0
llm_function: GOVERN
---
# Quality Gates

This ISO describes a software project: its repository layout, modules, and build graph.

## 8 Hard Gates

| Gate | Check | Pass Criteria | Weight |
|------|-------|---------------|--------|
| **G1: Syntax** | `python -m py_compile` on all .py | 0 errors | BLOCK |
| **G2: Tests** | `pytest --collect-only` | ≥3 tests found | BLOCK |
| **G3: Lint** | `ruff check .` | 0 errors | BLOCK |
| **G4: Secrets** | Scan for API keys, passwords | 0 matches in non-test files | BLOCK |
| **G5: Docker** | Dockerfile has multi-stage + non-root | Both present | WARN |
| **G6: CI** | .github/workflows/ci.yml valid YAML | Parses without error | WARN |
| **G7: Health** | `/health` endpoint exists (API mode) | Returns 200 | WARN |
| **G8: Deps** | `pip-audit` on dependencies | 0 critical CVEs | WARN |

**BLOCK** = fails build, **WARN** = allows but flags

## Scoring Rubric

```
9.0-9.3: All 8 gates pass + rich tests + full CI/CD + security scanning
8.5-8.9: G1-G4 pass + Docker + CI present
8.0-8.4: G1-G4 pass (syntax, tests, lint, no secrets)
7.0-7.9: G1-G2 pass only (syntax valid, some tests)
<7.0:    Syntax errors or no tests → REJECT
```

## Gate Details

### G1: Syntax Validation

```bash
find src/ -name "*.py" -exec python -m py_compile {} \;
# Must return 0 for all files
```

### G2: Test Collection

```bash
pytest --collect-only tests/
# Must find ≥3 test items
# Must have conftest.py with ≥1 fixture
```

### G3: Lint

```bash
ruff check . --output-format=json
# Must return [] (empty issues list)
```

### G4: Secret Scanning

```python
PATTERNS = [
    r'password\s*=\s*["\'][^"\']+["\']',
    r'api_key\s*=\s*["\'][^"\']+["\']',
    r'sk-[a-zA-Z0-9]{20,}',
    r'ghp_[a-zA-Z0-9]{36}',
    r'-----BEGIN (RSA |EC )?PRIVATE KEY-----',
]
# Scan all files except tests/ and .env.example
```

### G5: Docker Validation

```python
def validate_dockerfile(content):
    checks = {
        "multi_stage": "AS builder" in content or "AS build" in content,
        "non_root": "USER " in content and "USER root" not in content,
        "healthcheck": "HEALTHCHECK" in content,
        "no_install_recommends": "--no-install-recommends" in content,
    }
    return all(checks.values())
```

### G6: CI Validation

```python
import yaml
with open(".github/workflows/ci.yml") as f:
    ci = yaml.safe_load(f)
assert "jobs" in ci
assert any(j for j in ci["jobs"] if "test" in j.lower() or "lint" in j.lower())
```

## Retry Policy

- If G1-G3 fail: retry implementation (max 2 attempts)
- If G4 fails: remove secrets, replace with env vars, retry
- If G5-G8 fail: flag as warnings, allow build to proceed
- After 2 retries: save as DRAFT with quality < 8.0

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental software-engineering artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
