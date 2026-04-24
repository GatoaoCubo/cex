---
id: p02_mm_codebase_mapper
kind: mental_model
8f: F4_reason
pillar: P02
title: "Mental Model: Codebase Mapper"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
domain: knowledge
quality: 9.1
tags: [codebase, mapping, stack-detection, mental-model]
tldr: "Stack detection via config files, imports, entry points"
density_score: 0.92
related:
  - bld_sp_knowledge_card_software_project
  - KC_N05_ZERO_DOWNTIME_DEPLOY
  - bld_sp_system_prompt_software_project
  - p04_ex_software_project_api_service
  - p08_ac_explore
  - bld_sp_architecture_software_project
  - bld_config_app_directory_entry
  - p02_agent_railway_superintendent
  - p01_kc_deploy_paas
  - kc_app_directory_entry
---

# Mental Model: Codebase Mapper

## Purpose
Detect project stack and architecture by reading deterministic signals. Every conclusion traces to a concrete file.

## Signals

| Signal | Files | Reveals |
|--------|-------|---------|
| Package mgr | `package.json`, `requirements.txt`, `go.mod` | Runtime + deps |
| Config | `tsconfig.json`, `.eslintrc`, `webpack.*` | Language version + tooling |
| Imports | `grep -r "import" src/` | Auth, payments, ORM |
| Entry point | `main.py`, `index.ts`, `app.py` | App type (API/CLI/worker) |
| Infra | `Dockerfile`, `railway.json`, `vercel.json` | Deploy target + CI |
| Schema | `*.prisma`, `alembic/`, `migrations/` | DB type + ORM |

## Decision Logic

```
1. READ dep files -> runtime (Python/Node/Go/Rust)
2. READ configs -> framework (FastAPI/Next.js/Gin)
3. GREP imports -> auth, payments, database
4. FIND entry points -> app type
5. CHECK infra -> deploy target
6. OUTPUT -> stack_profile with confidence per item
```

## Output

```yaml
stack_profile:
  runtime: python
  framework: fastapi
  auth: jwt
  database: postgres
  deploy: railway
  confidence: 0.95
  evidence:
    runtime: "pyproject.toml:3 python='^3.11'"
    framework: "app.py:1 from fastapi import FastAPI"
```

## Failure Modes

| Failure | Recovery |
|---------|----------|
| No entry point | Scan for `if __name__` or `export default` recursively |
| Multi-runtime | Report both; score each independently |
| No dep file | File extension census (`*.py` vs `*.ts` count) |
| Monorepo | Map each workspace separately |

## Quality Gates
- Every conclusion links to file path + line
- Confidence < 0.7 flagged as uncertain
- Multi-stack reported honestly, never forced to single

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.24 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | downstream | 0.23 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.20 |
| [[p04_ex_software_project_api_service]] | downstream | 0.19 |
| [[p08_ac_explore]] | downstream | 0.19 |
| [[bld_sp_architecture_software_project]] | downstream | 0.19 |
| [[bld_config_app_directory_entry]] | downstream | 0.18 |
| [[p02_agent_railway_superintendent]] | related | 0.18 |
| [[p01_kc_deploy_paas]] | upstream | 0.18 |
| [[kc_app_directory_entry]] | upstream | 0.17 |
