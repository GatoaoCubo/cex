---
id: KC_N05_RAILWAY_PLATFORM_DEEP
kind: knowledge_card
pillar: P01
title: Railway Platform - Architecture, Deploy & Operations
domain: N05_operations
tags: [railway, deploy, infra, cloud, platform]
quality: 9.0
sources:
  - https://docs.railway.com/overview/about-railway
  - https://docs.railway.com/guides/deployments
  - https://docs.railway.com/guides/healthchecks
  - https://docs.railway.com/reference/scaling
  - https://docs.railway.com/guides/variables
  - https://docs.railway.com/guides/private-networking
  - https://docs.railway.com/reference/config-as-code
created: 2026-04-01
---

# Railway Platform — Architecture, Deploy & Operations

## 1. Platform Overview

Railway is an all-in-one intelligent cloud provider that handles infrastructure provisioning, local development, and cloud deployment.

**Core capabilities:**
- OCI-compliant image building from code repos (with or without Dockerfile)
- Docker images from Docker Hub, GHCR, GitLab, Microsoft, Quay.io
- Variable/secret management per service and project level
- Static and ephemeral environments
- Built-in observability (logs, metrics)
- CLI + API + Web UI

## 2. Environments

| Type | Use Case |
|------|----------|
| Static | `production`, `staging` — persistent, named environments |
| Ephemeral | Auto-created per PR, destroyed on PR close |
| PR environment | Special `"pr"` key in railway.toml overrides |

Each environment has its own **isolated private network** — cross-environment traffic is prevented.

## 3. Deploy Triggers

| Trigger | Mechanism |
|---------|-----------|
| Git push | GitHub Autodeploys — auto-deploy on push to linked branch |
| Docker image | Image Auto Updates — watches for new tags |
| CLI | `railway up` from local directory |
| API | REST API deploy hook (webhook URL per service) |
| Staged changes | Review before applying, then promote |

**Pre-deploy command:** runs before container start (e.g., DB migrations):
```toml
[deploy]
preDeployCommand = ["npm run db:migrate"]
```

## 4. Health Checks

- Configure via `healthcheckPath` in railway.toml or service settings
- Railway hits `GET {healthcheckPath}` and waits for HTTP 200
- Default timeout: **300 seconds** (configurable via `healthcheckTimeout` or `RAILWAY_HEALTHCHECK_TIMEOUT_SEC` env var)
- Only after 200 does Railway switch traffic to new deployment (zero-downtime)
- Failure = deployment fails, previous version stays live
- **Caveat:** services with attached volumes still have downtime during redeploy

```toml
[deploy]
healthcheckPath = "/health"
healthcheckTimeout = 300
```

**Important:** App must listen on `$PORT` (injected by Railway). Health check hostname is `healthcheck.railway.app`.

## 5. Restart Policy

```toml
[deploy]
restartPolicyType = "ON_FAILURE"   # ON_FAILURE | ALWAYS | NEVER
restartPolicyMaxRetries = 5
```

## 6. Cron Jobs

```toml
[deploy]
cronSchedule = "*/15 * * * *"   # cron syntax, UTC
```

Service runs on schedule instead of continuously. Previous deployment overlaps controlled by `overlapSeconds`.

## 7. Domains & SSL

- `railway domain` → auto-generate `*.up.railway.app` subdomain
- `railway domain example.com` → assign custom domain
- SSL automatically provisioned for all Railway-managed domains
- Public domain available as `$RAILWAY_PUBLIC_DOMAIN` env var

## 8. Volumes (Persistent Storage)

- Attached to a service, mounted at a specified path
- Survive redeployments
- **Downtime caveat:** volume-attached services incur brief downtime on redeploy (volume can only attach to one replica at a time)

## 9. TCP Proxy

- Enables external TCP connections to services (e.g., PostgreSQL from local machine)
- Incurs **Network Egress billing**
- Available via `$RAILWAY_TCP_PROXY_PORT` env var
- Used by default on database plugins for external access

## 10. Scaling

### Vertical Scaling
Auto-scales up to plan limits. No config required.

### Horizontal Scaling (Replicas)
Manual replica count via service settings. Each replica gets full plan resource allocation:

| Plan | Max vCPU/replica | Max RAM/replica |
|------|-----------------|----------------|
| Pro  | 24 vCPU         | 24 GB          |

**Traffic distribution:** random round-robin across replicas. Multi-region: nearest region first, then round-robin within region.

**Sticky sessions:** NOT supported.

Scaling operations are staged changes — no full redeployment. New replicas use existing image. Removed replicas drain gracefully.

## 11. Private Networking

- Internal DNS: `SERVICE_NAME.railway.internal`
- Example: `http://api.railway.internal:8000`
- Encryption: WireGuard (all inter-service traffic)
- Zero config needed — auto-discovery within same environment
- IPv6 addressing used internally
- No public ports needed for internal communication

```python
# Internal DB connection from API service
DATABASE_URL = "postgresql://user:pass@postgres.railway.internal:5432/railway"
```

## 12. Variables System

### Types

| Type | Scope | Syntax |
|------|-------|--------|
| Service variable | Single service | Set in Variables tab |
| Shared variable | All services in project | `${{ shared.KEY }}` |
| Reference variable | Cross-service pull | `${{ SERVICE_NAME.VAR }}` |
| Sealed variable | Build+deploy only, never visible in UI | Set as "sealed" |

### Reference Syntax Examples
```
API_URL=https://${{ backend.RAILWAY_PUBLIC_DOMAIN }}
DB_URL=${{ postgres.DATABASE_URL }}
INTERNAL_API=${{ api.RAILWAY_PRIVATE_DOMAIN }}
```

### Railway-Injected Variables
```
RAILWAY_PUBLIC_DOMAIN       # public domain for this service
RAILWAY_PRIVATE_DOMAIN      # internal .railway.internal hostname
RAILWAY_TCP_PROXY_PORT      # TCP proxy port if enabled
PORT                        # port to listen on (required)
RAILWAY_ENVIRONMENT         # environment name
RAILWAY_SERVICE_NAME        # service name
```

### Import from .env
Supported file patterns: `.env`, `.env.example`, `.env.local`, `.env.production`, `.env.<suffix>`

### Third-party Integrations
- **Doppler Sync** — push secrets from Doppler to Railway automatically
- **Heroku Import** — migrate config vars from Heroku

## 13. Config as Code (railway.toml)

Full reference:

```toml
[build]
builder = "RAILPACK"           # RAILPACK (default) or DOCKERFILE
buildCommand = "npm run build"
watchPatterns = ["src/**"]     # only redeploy when these change
dockerfilePath = "Dockerfile"  # if DOCKERFILE builder
railpackVersion = "0.7.0"      # pin Railpack version

[deploy]
startCommand = "node index.js"
preDeployCommand = ["npm run db:migrate"]
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 5
cronSchedule = "*/15 * * * *"
overlapSeconds = "60"
drainingSeconds = "10"         # SIGTERM to SIGKILL gap

# Environment-specific overrides
[environments.staging]
[deploy]
startCommand = "node index.staging.js"

# PR environment override
[environments.pr]
[deploy]
startCommand = "node index.pr.js"
```

## 14. Deployment Lifecycle (Zero-Downtime)

```
Push to GitHub
    ↓
Build (Railpack/Dockerfile)
    ↓
preDeployCommand runs
    ↓
New container starts
    ↓
Health check polling (/health → 200)
    ↓
Traffic switched to new container
    ↓
Old container drained (drainingSeconds) → stopped
```

## Anti-Patterns

- Do NOT use `railway up` without first running `railway service` to confirm target service
- Do NOT attach volumes to services requiring zero-downtime (volume lock = brief downtime)
- Do NOT hardcode ports — always use `$PORT`
- Do NOT use external TCP connections unnecessarily (incurs egress cost — use `.railway.internal` instead)
