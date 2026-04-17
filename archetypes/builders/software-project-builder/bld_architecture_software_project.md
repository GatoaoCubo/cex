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
quality: 9.1
tags: [builder, architecture, software-project, layers]
tldr: "4-layer architecture: Domain (business logic) → Infrastructure (DB, cache, external) → Interface (API/CLI) → Deploy (Docker, CI/CD). Clean deps: domain has zero external deps."
density_score: 1.0
llm_function: CONSTRAIN
---
# Architecture

This ISO describes a software project: its repository layout, modules, and build graph.

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

## DI + Config

```python
# deps.py — @lru_cache settings, Depends(get_db)
# config.py — BaseSettings(env_prefix="APP_", env_file=".env")
#   Required: database_url | Optional: redis_url, log_level, workers, debug
```

## Error Flow

Domain raises AppError → Infra wraps DB/HTTP errors → Interface returns HTTP → Middleware catches unhandled → 500.

## Testing

| Layer | Test Type | Speed | Deps |
|-------|-----------|-------|------|
| Domain | Unit | <1s | None |
| Infra | Integration | 1-10s | DB |
| Interface | API | 1-5s | TestClient |
| Deploy | E2E | 10-60s | Docker |
