---
id: p01_kc_deploy_paas
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Deploy PaaS — Railway, Render, Nixpacks"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [deploy, railway, render, paas, nixpacks, production]
tldr: "PaaS deploy patterns from codexa-core: Railway (primary), Render (secondary), nixpacks auto-detection, Procfile, health checks, rollback, env vars, scaling. Zero-Dockerfile deploys."
density_score: 1.0
when_to_use: "Apply when paas deploy patterns from codexa-core: railway (primary), render (secondary), nixpacks auto-detec..."
keywords: [knowledge-card, software-engineering, paas, railway, deploy]
axioms:
  - "AVOID: ❌ Secrets in railway.toml/render.yaml (use env vars)"
  - "AVOID: ❌ No health check (PaaS can't detect failures)"
  - "AVOID: ❌ Logging to files instead of stdout"
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_railway_platform_deep
  - KC_N05_RAILWAY_CLI_PATTERNS
  - p05_output_railway_toml
  - p01_kc_railway_cli_patterns
  - p02_agent_railway_superintendent
  - p08_ac_railway_superintendent
  - p03_sp_railway_superintendent
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - spec_n05_railway_superintendent
  - KC_N05_ZERO_DOWNTIME_DEPLOY
---

# Deploy PaaS Patterns

## Railway (Primary)

### railway.toml

```toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn api.main:app --host 0.0.0.0 --port $PORT --workers 4"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 3
```

### Deploy via CLI

```bash
# Install CLI
npm i -g @railway/cli

# Link project
railway login
railway link

# Deploy
railway up                         # Deploy current dir
railway up --service codexa-api    # Specific service
railway up --environment staging   # Specific env

# Rollback
railway rollback                   # Revert to previous deploy

# Logs
railway logs --tail 100
```

### Deploy via GitHub Actions

```yaml
- name: Install Railway CLI
  run: npm i -g @railway/cli

- name: Deploy to Railway
  run: railway up --service ${{ env.SERVICE }}
  env:
    RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}

- name: Health check
  run: |
    URL="${{ secrets.RAILWAY_URL }}"
    for i in $(seq 1 10); do
      curl -sf "$URL/health" && exit 0 || sleep 15
    done
    echo "Health check failed" && exit 1
```

### Environment Variables

```bash
railway variables set DATABASE_URL="postgresql://..."
railway variables set REDIS_URL="redis://..."
railway variables set API_KEYS="key1,key2"
```

## Render (Secondary)

### render.yaml (Blueprint)

```yaml
services:
  - type: web
    name: my-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn api.main:app --host 0.0.0.0 --port $PORT
    healthCheckPath: /health
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: my-db
          property: connectionString
      - key: PYTHON_VERSION
        value: "3.12"

databases:
  - name: my-db
    plan: starter
```

## Nixpacks (Auto-Detection)

Railway and Render use Nixpacks to auto-detect language and build.

### nixpacks.toml (Override defaults)

```toml
[phases.setup]
nixPkgs = ["python312", "ffmpeg"]

[phases.install]
cmds = ["pip install -r requirements.txt"]

[start]
cmd = "uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}"
```

### Detection Order

1. `Dockerfile` → Docker build (full control)
2. `nixpacks.toml` → Custom Nix config
3. `Procfile` → Process types
4. `pyproject.toml` → Python project
5. `requirements.txt` → Python fallback

## Procfile

```
web: uvicorn api.main:app --host 0.0.0.0 --port $PORT --workers 4
worker: celery -A tasks worker --loglevel=info
beat: celery -A tasks beat --loglevel=info
```

## Deploy Checklist

```
[ ] Health endpoint at /health (returns 200 + version + uptime)
[ ] Environment variables configured (no hardcoded secrets)
[ ] Database migrations run on startup (or separate migration job)
[ ] CORS configured for production origins
[ ] Rate limiting enabled
[ ] Logging to stdout (PaaS captures stdout)
[ ] Graceful shutdown (close DB pool, Redis, etc.)
[ ] Build tested locally: docker build . && docker run -p 8000:8000 ...
[ ] Rollback plan: railway rollback or redeploy previous tag
```

## Anti-Patterns

- ❌ Secrets in railway.toml/render.yaml (use env vars)
- ❌ No health check (PaaS can't detect failures)
- ❌ Logging to files instead of stdout
- ❌ Running migrations in web process startup (use separate job for large DBs)
- ❌ No graceful shutdown handlers

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_railway_platform_deep]] | sibling | 0.68 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | sibling | 0.62 |
| [[p05_output_railway_toml]] | downstream | 0.62 |
| [[p01_kc_railway_cli_patterns]] | sibling | 0.58 |
| [[p02_agent_railway_superintendent]] | downstream | 0.56 |
| [[p08_ac_railway_superintendent]] | downstream | 0.55 |
| [[p03_sp_railway_superintendent]] | downstream | 0.55 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | sibling | 0.55 |
| [[spec_n05_railway_superintendent]] | downstream | 0.51 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | sibling | 0.49 |
