---
id: p01_kc_docker_patterns
kind: knowledge_card
pillar: P01
title: "Docker Patterns — Multi-Stage, Compose, Production"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [docker, container, multi-stage, compose, production]
tldr: "Production Docker patterns from codexa-core: multi-stage builds (builder→runtime), non-root user, health checks, compose services (API+Postgres+Redis+Worker), profiles for dev tools."
density_score: 1.0
when_to_use: "Apply when production docker patterns from codexa-core: multi-stage builds (builder→runtime), non-root user,..."
keywords: [multi-stage, knowledge-card, layer, profiles, docker]
axioms:
  - "AVOID: ❌ Single-stage build (huge image with build tools)"
  - "AVOID: ❌ Running as root (security vulnerability)"
  - "AVOID: ❌ No HEALTHCHECK (orchestrator can't detect failures)"
linked_artifacts:
  primary: null
  related: []
related:
  - bld_sp_output_template_software_project
  - p01_kc_docker_ai_containerization
  - bld_sp_schema_software_project
  - KC_N05_NIXPACKS_BUILDPACKS
  - bld_sp_tools_software_project
  - bld_sp_examples_software_project
  - spec_zero_install
  - KC_N05_UVICORN_PRODUCTION
  - p01_kc_deploy_paas
  - bld_sp_system_prompt_software_project
---

# Docker Patterns

## Multi-Stage Dockerfile

```dockerfile
# Stage 1: Builder — install deps in isolated layer
FROM python:3.12-slim AS builder
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --upgrade pip wheel && pip install -r requirements.txt

# Stage 2: Runtime — minimal image with only runtime deps
FROM python:3.12-slim AS api
ARG BUILD_DATE
ARG VERSION=1.0.0
LABEL org.opencontainers.image.title="My API" \
      org.opencontainers.image.version="${VERSION}"

# Security: non-root user
RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser
WORKDIR /app

# Copy venv from builder (no build tools in runtime)
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Runtime-only system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY --chown=appuser:appuser src/ ./src/
COPY --chown=appuser:appuser api/ ./api/

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PORT=8000
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

USER appuser
CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT} --workers 4"]
```

### Key Decisions

| Decision | Why |
|----------|-----|
| Multi-stage | Builder image has gcc/build tools (~800MB), runtime is slim (~200MB) |
| Non-root user | Security — container runs as uid 1000, not root |
| Venv copy | Clean dependency isolation, no system-wide installs |
| HEALTHCHECK | Orchestrator (Docker/K8s) knows when app is ready |
| `--no-install-recommends` | Minimal attack surface |
| `rm -rf /var/lib/apt/lists/*` | Smaller layer, no cached package lists |

## docker-compose.yml (Full Stack)

```yaml
services:
  api:
    build: { context: ., dockerfile: Dockerfile }
    ports: ["8000:8000"]
    environment:
      - DATABASE_URL=postgresql://app:pass@postgres:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      postgres: { condition: service_healthy }
      redis: { condition: service_healthy }
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes: [postgres_data:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d mydb"]
      interval: 10s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes --maxmemory 256mb
    volumes: [redis_data:/data]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]

  worker:
    build: { context: ., dockerfile: Dockerfile }
    command: celery -A tasks worker --loglevel=info
    depends_on: [postgres, redis, api]
    profiles: [workers]  # Only with --profile workers

  pgadmin:
    image: dpage/pgadmin4:latest
    ports: ["5050:5050"]
    profiles: [dev-tools]  # Only with --profile dev-tools

volumes:
  postgres_data:
  redis_data:

networks:
  default:
    driver: bridge
```

### Compose Patterns

| Pattern | Usage |
|---------|-------|
| `depends_on.condition` | Wait for health before starting dependent |
| `profiles` | Optional services: `docker-compose --profile workers up` |
| Named volumes | Persistent data across restarts |
| `restart: unless-stopped` | Auto-recover from crashes |
| `${VAR:-default}` | Environment variable with fallback |

## .dockerignore

```
.git
.github
.venv
__pycache__
*.pyc
node_modules
.env
.env.*
tests/
docs/
*.md
!README.md
```

## Anti-Patterns

- ❌ Single-stage build (huge image with build tools)
- ❌ Running as root (security vulnerability)
- ❌ No HEALTHCHECK (orchestrator can't detect failures)
- ❌ `COPY . .` without .dockerignore (leaks .env, .git)
- ❌ `pip install` in runtime stage (use multi-stage venv copy)
- ❌ `latest` tag in production (use pinned versions)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_output_template_software_project]] | downstream | 0.43 |
| [[p01_kc_docker_ai_containerization]] | sibling | 0.33 |
| [[bld_sp_schema_software_project]] | downstream | 0.27 |
| [[KC_N05_NIXPACKS_BUILDPACKS]] | sibling | 0.26 |
| [[bld_sp_tools_software_project]] | downstream | 0.24 |
| [[bld_sp_examples_software_project]] | downstream | 0.23 |
| [[spec_zero_install]] | related | 0.23 |
| [[KC_N05_UVICORN_PRODUCTION]] | sibling | 0.22 |
| [[p01_kc_deploy_paas]] | sibling | 0.22 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.20 |
