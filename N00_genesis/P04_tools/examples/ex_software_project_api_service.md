---
id: p04_ex_software_project_api_service
kind: example
8f: F3_inject
pillar: P04
title: "Example — API Service (Product API)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [example, software-project, api-service, fastapi, supabase]
tldr: "Complete API service: Product management with FastAPI+Pydantic+Supabase. Middleware stack (CORS→RateLimit→Auth→RLS), multi-stage Docker, Railway deploy, GitHub Actions CI."
density_score: 0.90
related:
  - bld_sp_architecture_software_project
  - bld_sp_knowledge_card_software_project
  - bld_sp_system_prompt_software_project
  - bld_sp_schema_software_project
  - p04_tpl_software_project
  - bld_sp_examples_software_project
  - n06_api_access_pricing
  - p04_ex_software_project_cli_tool
  - p01_kc_fastapi_patterns
  - bld_sp_instruction_software_project
---

# Example: API Service — Product API

## Config

```yaml
project: { name: product-api, version: 1.0.0, type: api_service, python: "3.12" }
package: { name: product_api, cli_name: product-api }
dependencies:
  core: [fastapi>=0.100, uvicorn[standard]>=0.23, pydantic>=2.0, httpx>=0.24, asyncpg>=0.29]
  dev: [pytest>=7.0, pytest-asyncio>=0.21, ruff>=0.1.0]
deploy: { target: railway, port: 8000, workers: 4, health_path: /health }
config: { env_prefix: APP, settings: [database_url, redis_url, api_keys, debug] }
```

## Key Files

**src/product_api/api/main.py**: FastAPI app with middleware stack (CORS outermost).
**src/product_api/api/routes/products.py**: CRUD routes with Pydantic models.
**src/product_api/api/middleware/auth.py**: API key + JWT hybrid auth.
**src/product_api/domain/models.py**: Product, CreateProduct, UpdateProduct models.
**src/product_api/infra/db.py**: asyncpg pool, health check, graceful shutdown.
**src/product_api/infra/config.py**: BaseSettings with APP_ prefix.
**Dockerfile**: Multi-stage, non-root user, healthcheck.
**docker-compose.yml**: API + Postgres + Redis + pgAdmin (dev-tools profile).
**.github/workflows/ci.yml**: lint → test → docker-build.

## Architecture

```
src/product_api/
├── domain/           # Layer 1: Pure logic
│   ├── models.py     # Pydantic: Product, CreateProduct
│   ├── services.py   # CRUD logic (no DB imports)
│   └── errors.py     # ProductNotFound, ValidationError
├── infra/            # Layer 2: External
│   ├── db.py         # asyncpg pool
│   ├── cache.py      # Redis client
│   └── config.py     # BaseSettings
├── api/              # Layer 3: Interface
│   ├── main.py       # FastAPI + middleware
│   ├── routes/       # Route handlers
│   ├── middleware/    # Auth, rate-limit, RLS
│   └── deps.py       # Dependency injection
└── __init__.py
```

## What Makes It Good

- Middleware order correct (CORS outermost)
- Domain layer has zero infrastructure imports
- Health check returns DB + cache status
- Async all the way (asyncpg, not psycopg2)
- Docker compose with healthcheck deps
- Rate limiting per tenant tier (free/pro/business)

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `example`
- **Artifact ID**: `p04_ex_software_project_api_service`
- **Tags**: [example, software-project, api-service, fastapi, supabase]

## Example Registry

| Aspect | Detail |
|--------|--------|
| Purpose | Few-shot exemplar for builder prompts |
| Injection | Loaded by `cex_skill_loader.py` at F3 |
| Quality | Must score 9.0+ to serve as exemplar |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_architecture_software_project]] | downstream | 0.44 |
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.35 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.30 |
| [[bld_sp_schema_software_project]] | upstream | 0.28 |
| [[p04_tpl_software_project]] | related | 0.28 |
| [[bld_sp_examples_software_project]] | sibling | 0.27 |
| [[n06_api_access_pricing]] | downstream | 0.26 |
| [[p04_ex_software_project_cli_tool]] | sibling | 0.26 |
| [[p01_kc_fastapi_patterns]] | upstream | 0.24 |
| [[bld_sp_instruction_software_project]] | upstream | 0.24 |
