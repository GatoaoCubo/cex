---
id: spec_n05_railway_superintendent
kind: constraint_spec
pillar: P06
title: Spec N05 Railway Backend Superintendent
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: operations-engineering
quality_target: 9.0
status: EXECUTED
scope: N05_operations
tags: [spec, n05, railway, backend, fastapi, postgresql, deploy]
tldr: N05 evolves from generic DevOps to Railway Backend Superintendent with real production data.
density_score: 0.96
quality: 9.2
updated: "2026-04-07"
---

# Spec N05 -- Railway Backend Superintendent

## 1. VISION

N05 transitions from a generic DevOps nucleus into the **Railway/Backend Superintendent**
with absolute ownership of the production API lifecycle.

> Guiding question: Is this deployment safe, observable, and reversible?

### Current State vs Target

| Dimension | CURRENT | TARGET |
|-----------|---------|--------|
| Identity | Generic DevOps | Railway Superintendent |
| Model | GPT via Codex CLI | Claude Opus via claude CLI |
| Runtime | codex | claude |
| MCPs | none | railway + postgresql |
| Focus | code review, pytest, debug | deploy, API lifecycle, Railway infra |
| KCs | 1 generic | 12 railway-native |
| Output | logs, patches | railway.toml, migrations, health endpoints |

---

## 2. HYDRATION -- REAL PRODUCTION SYSTEM

Data extracted from the real backend (codexa-core/api/).

### 2.1 Railway Topology (4 services)

| Service | Config | Stack |
|---------|--------|-------|
| codexa-api | api/railway.toml | FastAPI+uvicorn+nixpacks |
| codexa-frontend | nixpacks.toml | React+Vite+serve |
| mc-dashboard | railway.toml | Node |
| gateway | gateway/railway.toml | Python+uvicorn |

### 2.2 Real Backend Numbers

198 Python files, ~51K LOC core, 141 endpoints, 31 routers, 105 core modules, 63 env vars, 25+ deps

### 2.3 Real Middleware Stack (8 layers)

1. CORS (outermost)
2. TenantRateLimit (free=60/pro=120/business=300)
3. APIKeyMiddleware (JWT+APIKey hybrid)
4. RLSMiddleware (Row-Level Security)
5. EndpointRateLimit (per-endpoint LLM)
6. body_size_limit (5MB/10MB)
7. catch_all_exceptions (JSON)
8. request_id_and_timing (X-Request-Id)

### 2.4 Real Infrastructure

DB: PostgreSQL Railway (asyncpg pool 3-20, SSL negotiation)
Cache: Redis Railway (hiredis, TTL=60s, in-memory fallback)
Auth: JWT+APIKey hybrid (PyJWT, bcrypt)
LLM: Multi-Router (Groq/Cerebras/Gemini/Claude/OpenAI/Ollama)
Sandbox: E2B (code+browser)
Payments: Stripe + MercadoPago PIX (BRL centavos wallet)
ERP: Bling OAuth2 (background token refresh)
Marketplace: MercadoLivre OAuth2
Email: Resend+Jinja2, WhatsApp: pywa, Execution: 3-tier local/cloud/e2b

### 2.5 Real Health Endpoint

HealthResponse: status, version, timestamp, uptime_seconds, environment, database{}, cache{}
/health (full) + /pipeline/health (tiers)

### 2.6 Startup Sequence (14 checks)

asyncpg pool > auto-migrations > Redis > rate limiter > E2B > Stripe > MercadoPago >
MercadoLivre OAuth > Bling OAuth+background refresh > ExecutionPipeline > LLM tracking >
Credit tables > Mentor tables > Referral tables

### 2.7 Environment Variables (63 total)

Required: DATABASE_URL, ANTHROPIC_API_KEY, OPENAI_API_KEY, PORT, ENV
Mock-mode: STRIPE_SECRET_KEY, MERCADOPAGO_ACCESS_TOKEN, E2B_API_KEY
Pool: DB_POOL_MIN=3, DB_POOL_MAX=20, DB_COMMAND_TIMEOUT=60

### 2.8 Credits (BRL)

research=75c, ad=50c, photo=100c, full=200c, scrape=FREE

---

## 3. 8F DECOMPOSITION

### F1 CONSTRAIN
6 schemas: railway_toml, api_response, env_var, health_check, middleware_stack, startup_sequence

### F2 BECOME
role: Railway/Backend Superintendent, model: opus, mcps: [railway,postgresql]
12 capabilities hydrated with the real system (see section 2)

### F3 INJECT (12 KCs)

| # | KC | Action | Hydration |
|---|-----|--------|-----------|
| 1 | kc_railway_platform_deep | CREATE | 4 real services |
| 2 | kc_railway_cli_patterns | CREATE | up/link/rollback |
| 3 | kc_postgresql_railway | CREATE | asyncpg SSL migrations |
| 4 | kc_nixpacks_buildpacks | CREATE | real nixpacks.toml |
| 5 | kc_zero_downtime_deploy | CREATE | 14-step startup |
| 6 | kc_api_health_monitoring | CREATE | real HealthResponse |
| 7 | kc_uvicorn_production | CREATE | startCommand workers |
| 8 | kc_railway_networking | CREATE | CORS regex origins |
| 9 | kc_middleware_stack | CREATE | 8-layer stack |
| 10 | kc_credit_system_railway | CREATE | BRL wallet |
| 11 | kc_fastapi_patterns | REUSE | existing P01 |
| 12 | kc_deploy_paas | REUSE | existing P01 |

### F4 REASON
Deploy: verify toml - verify env - check migrations - railway link - railway up - await health 30s - verify /health - verify /pipeline/health - monitor logs - confirm rate-limit
Rollback: identify service - logs - blast radius - railway rollback - verify - check CORS

### F5 CALL
.mcp-n05.json: railway+postgres MCP. Fallback: CLI

### F6 PRODUCE
6 templates: railway.toml, deploy checklist, rollback plan, health endpoint, middleware stack, env contract

### F7 GOVERN
6 gates: deploy smoke 30s, rollback plan 4 services, migration safe, env 63 vars, health full, middleware intact

### F8 COLLABORATE
dispatch receives_from N03/N07, handoff_to N03, boot/n05.ps1

---

## 4. ARTIFACTS (30: 16 CREATE + 14 REWRITE)

W1 Identity+Boot: agent, prompt, card, boot, mcp, seed (6)
W2 Knowledge: 10 new KCs + 1 rewrite (11)
W3 Schemas+Output: 6 schemas + 4 outputs (10)
W4 Quality+Orchestration: gate, dispatch, workflow, checkpoint (4)

---

## 5. SEED WORDS

railway-native, api-lifecycle, zero-downtime, rollback-first, infrastructure-as-evidence, deploy-superintendent, health-obsessed, nixpacks, postgresql-managed, uvicorn-production, smoke-test-always, env-contract-enforced, migration-safe, observability-driven, middleware-stack-ordered, asyncpg-pool, redis-fallback, multi-service-topology, cors-regex, rate-limit-tiered, credit-system-aware, json-structured-logging, request-id-correlation, graceful-shutdown, ssl-negotiation, mock-mode-fallback
