---
# TEMPLATE: Mental Model — Codebase Mapper (P02 Model)
# Valide contra P02_model/_schema.yaml (types.mental_model)
# Max 2048 bytes | quality_min: 7.0

id: p02_mm_codebase_mapper
kind: mental_model
pillar: P02
title: "Mental Model: Codebase Mapper"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: knowledge
quality: 8.5
tags: [codebase, mapping, stack-detection, mental-model]
tldr: "Deterministic stack detection via config files, imports, and entry points"
---

# Mental Model: Codebase Mapper

## Purpose

Detect project stack, architecture, and key integration points by reading deterministic signals in the codebase. No guessing — every conclusion must trace to a concrete file or pattern.

## Signals (Input Layer)

| Signal Type | Files to Check | What It Reveals |
|-------------|----------------|-----------------|
| Package manager | `package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml` | Runtime + dependencies |
| Config files | `tsconfig.json`, `pyproject.toml`, `.eslintrc`, `webpack.config.*` | Language version + build tooling |
| SDK imports | `grep -r "import\|require\|from" src/` | Auth (jose/JWT), payments (Stripe), ORM (Prisma/SQLAlchemy) |
| Entry points | `main.py`, `index.ts`, `app.py`, `server.ts` | Application type (API/CLI/worker) |
| Infra configs | `Dockerfile`, `railway.json`, `vercel.json`, `.github/workflows/` | Deploy target + CI/CD |
| Schema files | `*.prisma`, `alembic/`, `migrations/` | Database type + ORM |

## Decision Logic

```
1. READ dependency files -> identify runtime (Python/Node/Go/Rust)
2. READ config files -> identify language version + framework
3. GREP imports -> identify auth method, payment provider, database
4. FIND entry points -> classify app type (API/CLI/worker/frontend)
5. CHECK infra -> identify deploy target and CI pipeline
6. OUTPUT: stack_profile.yaml with all findings + confidence per item
```

## Output Schema

```yaml
stack_profile:
  runtime: [python|node|go|rust|multi]
  framework: [fastapi|express|nextjs|gin|none]
  language_version: [version_string]
  auth: [jwt|oauth|session|none]
  payments: [stripe|mercadopago|none]
  database: [postgres|mysql|sqlite|mongo|none]
  orm: [sqlalchemy|prisma|sequelize|none]
  deploy: [railway|vercel|docker|aws|none]
  ci: [github_actions|gitlab_ci|none]
  confidence: [0.0_to_1.0]
```

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| No entry point found | No `main.*`, `index.*`, `app.*`, `server.*` in root or `src/` | Scan all directories for `if __name__` or `export default` patterns |
| Ambiguous stack (multi-runtime) | Both `package.json` and `requirements.txt` exist | Check both — report as multi-stack with per-runtime confidence |
| Missing dependency file | No package manager file found | Fall back to file extension census (`*.py` count vs `*.ts` count) |
| Monorepo structure | Multiple `package.json` at different depths | Map each workspace separately, report as monorepo |

## Quality Gates

- Every conclusion links to a specific file path
- Confidence < 0.7 must be flagged as uncertain
- Multi-stack projects reported as such (never forced into single stack)
