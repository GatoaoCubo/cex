---
id: bld_sp_architecture_software_project
kind: architecture
pillar: P08
title: "Architecture — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 8.9
tags: [builder, architecture, software-project, layers]
tldr: "4-layer architecture: Domain (business logic) → Infrastructure (DB, cache, external) → Interface (API/CLI) → Deploy (Docker, CI/CD). Clean deps: domain has zero external deps."
density_score: 0.90
---

# Architecture

## 4-Layer Model

```
┌─────────────────────────────────┐
│  Layer 4: DEPLOY                │  Docker, CI/CD, Railway, monitoring
│  (How it runs in production)    │
├─────────────────────────────────┤
│  Layer 3: INTERFACE             │  FastAPI routes, Typer CLI, WebSocket
│  (How users interact)           │
├─────────────────────────────────┤
│  Layer 2: INFRASTRUCTURE        │  DB, cache, HTTP clients, file I/O
│  (How it connects to world)     │
├─────────────────────────────────┤
│  Layer 1: DOMAIN                │  Pure business logic, Pydantic models
│  (What it does)                 │  Zero external dependencies
└─────────────────────────────────┘
```

### Dependency Rule

```
Deploy → Interface → Infrastructure → Domain
         ↓            ↓                ↓
         imports       imports          imports NOTHING external
```

Domain layer has ZERO external deps (only stdlib + pydantic).
Infrastructure adapts external services to domain interfaces.
Interface exposes domain operations via API/CLI.
Deploy packages everything for production.

## Directory Mapping

```
src/{package}/
├── domain/              # Layer 1: Pure logic
│   ├── models.py        # Pydantic data models
│   ├── services.py      # Business rules
│   └── errors.py        # Custom exceptions
├── infra/               # Layer 2: External world
│   ├── db.py            # Database client
│   ├── cache.py         # Redis/in-memory
│   ├── http_client.py   # External API calls
│   └── config.py        # BaseSettings (env vars)
├── api/                 # Layer 3: HTTP interface
│   ├── main.py          # FastAPI app
│   ├── routes/          # Route handlers
│   ├── middleware/       # Auth, CORS, rate-limit
│   └── deps.py          # Dependency injection
├── cli.py               # Layer 3: CLI interface
└── __init__.py
```

## Dependency Injection (FastAPI)

```python
# src/{package}/api/deps.py
from functools import lru_cache
from ..infra.db import Database
from ..infra.config import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

async def get_db(settings: Settings = Depends(get_settings)) -> Database:
    return Database(settings.database_url)
```

## Config Pattern

```python
# src/{package}/infra/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {"env_prefix": "APP_", "env_file": ".env"}

    # Required
    database_url: str

    # Optional with defaults
    redis_url: str = "redis://localhost:6379/0"
    log_level: str = "info"
    workers: int = 4
    debug: bool = False

    # Feature flags
    enable_cache: bool = True
    enable_rate_limit: bool = True
```

## Error Flow

```
Domain raises AppError (business logic failure)
  → Infrastructure catches DB/HTTP errors → wraps in AppError
    → Interface catches AppError → returns HTTP response
      → Middleware catches unhandled → returns 500
```

## Testing Strategy

```
tests/
├── test_domain/        # Unit tests (fast, no I/O)
│   └── test_services.py
├── test_infra/         # Integration tests (needs DB/cache)
│   └── test_db.py
├── test_api/           # API tests (TestClient)
│   └── test_routes.py
└── conftest.py         # Shared fixtures
```

| Layer | Test Type | Speed | External Deps |
|-------|-----------|-------|---------------|
| Domain | Unit | <1s | None |
| Infra | Integration | 1-10s | DB, Redis |
| Interface | API | 1-5s | TestClient (in-process) |
| Deploy | E2E | 10-60s | Docker, HTTP |
