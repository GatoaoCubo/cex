---
id: p05_output_railway_toml
kind: output_validator
8f: F6_produce
pillar: P05
title: "Railway TOML Template — Service Variants"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.1
tags: [output, template, railway, toml, deploy]
tldr: "Standard railway.toml for 3 service types — python_api, node_spa, gateway."
density_score: 1.0
related:
  - p01_kc_deploy_paas
  - p01_kc_railway_platform_deep
  - p06_schema_railway_toml
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p03_sp_railway_superintendent
  - KC_N05_RAILWAY_CLI_PATTERNS
  - p02_agent_railway_superintendent
  - p01_kc_railway_cli_patterns
  - p08_ac_railway_superintendent
  - spec_n05_railway_superintendent
---

# Railway TOML Template

## Purpose
Standard `railway.toml` configuration for new Railway services.
Three variants covering the CODEXA topology.

---

## Variant 1: Python API (Primary)

```toml
# railway.toml — Python FastAPI Service
# Deploy: Railway auto-detect via nixpacks

[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn main:app --host 0.0.0.0 --port $PORT --workers 2 --log-level info --proxy-headers --forwarded-allow-ips '*'"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 3
numReplicas = 1

[env]
PYTHONUNBUFFERED = "1"
# ENV is set per environment (staging/production) via Railway dashboard
```

### Field Reference

| Field | Value | Why |
|-------|-------|-----|
| `builder` | nixpacks | Auto-detects Python, installs deps |
| `startCommand` | uvicorn with --host 0.0.0.0 | Required for Railway port binding |
| `--port $PORT` | Railway injects PORT env | Never hardcode port |
| `--workers 2` | 2 workers for 0.5-1 vCPU | Scale via numReplicas, not workers |
| `--proxy-headers` | Trust Railway's reverse proxy | X-Forwarded-For, X-Real-IP |
| `healthcheckPath` | /health | Must return 200 within timeout |
| `healthcheckTimeout` | 300 | 5min for cold start (14-check startup) |
| `restartPolicyType` | ON_FAILURE | Auto-restart on crash, not on deploy |
| `numReplicas` | 1 | Scale up manually when needed |

## Variant 2: Node SPA (Frontend)

```toml
# railway.toml — Node.js Static SPA
[build]
builder = "nixpacks"
buildCommand = "npm ci && npm run build"

[deploy]
startCommand = "npx serve dist -l $PORT"
healthcheckPath = "/"
healthcheckTimeout = 30
restartPolicyType = "ON_FAILURE"
numReplicas = 1

[env]
NODE_ENV = "production"
```

## Variant 3: Gateway (Python Proxy)

```toml
# railway.toml — API Gateway / Reverse Proxy
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "python -m gateway --host 0.0.0.0 --port $PORT"
healthcheckPath = "/health"
healthcheckTimeout = 60
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 5
numReplicas = 1

[env]
PYTHONUNBUFFERED = "1"
```

## Validation Checklist

```yaml
validation:
  - "[deploy].startCommand contains --host 0.0.0.0"
  - "[deploy].startCommand contains $PORT (not hardcoded)"
  - "[deploy].healthcheckPath is set"
  - "[deploy].healthcheckTimeout >= 30"
  - "[deploy].restartPolicyType is ON_FAILURE"
  - "[env].PYTHONUNBUFFERED = 1 (for Python services)"
  - "No secrets in [env] section (use Railway variables)"
```

## Deploy Flow
```
1. railway link --project <id> --service <name>
2. Validate railway.toml (schema 3.1)
3. railway up
4. Wait for /health 200 (< healthcheckTimeout)
5. Verify in Railway dashboard
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_deploy_paas]] | upstream | 0.69 |
| [[p01_kc_railway_platform_deep]] | upstream | 0.63 |
| [[p06_schema_railway_toml]] | downstream | 0.62 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | upstream | 0.57 |
| [[p03_sp_railway_superintendent]] | upstream | 0.51 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | upstream | 0.50 |
| [[p02_agent_railway_superintendent]] | upstream | 0.47 |
| [[p01_kc_railway_cli_patterns]] | upstream | 0.46 |
| [[p08_ac_railway_superintendent]] | downstream | 0.46 |
| [[spec_n05_railway_superintendent]] | downstream | 0.45 |
