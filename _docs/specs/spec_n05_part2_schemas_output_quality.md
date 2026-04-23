---
id: spec_n05_part2
kind: constraint_spec
pillar: P06
title: Spec N05 Part 2 -- Schemas Output Quality Orchestration
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: operations-engineering
quality_target: 9.0
status: EXECUTED
scope: N05_operations
depends_on: spec_n05_railway_superintendent
tags: [spec, n05, schemas, output, quality-gates, orchestration]
tldr: Waves 3-4 of N05 -- schemas, output templates, quality gates, orchestration.
density_score: 0.95
quality: 9.2
updated: "2026-04-07"
---

# Spec N05 Part 2 -- Schemas, Output, Quality, Orchestration

## COMPLETED PRE-REQUISITES

- [x] Part 1 identity (agent, system_prompt, agent_card)
- [x] Wave 2 KCs (7 new via SHAKA, 58KB)
- [x] Boot/config (n05.cmd, .mcp-n05.json, seed)

---

## WAVE 3A: SCHEMAS (P06) -- 6 CREATE in N05/P06_schema/

### 3.1 railway_toml_schema.yaml
Validates railway.toml before deploy. Based on actual api/railway.toml.
Required sections: [build] (builder, buildCommand), [deploy] (startCommand with --host 0.0.0.0 --port, healthcheckPath, healthcheckTimeout 10-300, restartPolicyType, numReplicas), [env] (PYTHONUNBUFFERED=1, ENV).

### 3.2 api_response_contract.yaml
Standard response format. Success: {status, data, timestamp, request_id}. Error: {detail, status_code, docs(/docs on 404), support(on 500)}. Required headers: X-Request-Id, X-Process-Time, X-RateLimit-Limit/Remaining/Reset.

### 3.3 env_var_contract.yaml
63 vars mapped from actual codebase. Categories: required (DATABASE_URL, PORT, ENV), cloud_tier (ANTHROPIC_API_KEY, OPENAI_API_KEY), mock_mode (STRIPE_SECRET_KEY, MERCADOPAGO_ACCESS_TOKEN, E2B_API_KEY, REDIS_URL->in_memory), pool_tuning (DB_POOL_MIN=3, DB_POOL_MAX=20, DB_COMMAND_TIMEOUT=60), railway_auto (RAILWAY_ENVIRONMENT, PORT), oauth (ML_APP_ID, BLING_CLIENT_ID, WA_TOKEN), cost_control (LLM_BUDGET_DAILY, FIRECRAWL_MONTHLY_BUDGET).

### 3.4 health_check_contract.yaml
Based on the actual HealthResponse Pydantic model. /health GET (no auth): {status: healthy|degraded|unhealthy, version: semver, timestamp: iso8601z, uptime_seconds: float, environment: prod|staging|dev, database: {status, pool_size}, cache: {status, connected}}. degraded_when: database.status==unhealthy. /pipeline/health: {pipeline, available_tiers: [local, cloud, e2b]}.

### 3.5 middleware_stack_contract.yaml
8 layers in fixed order: 1.CORS (outermost), 2.TenantRateLimit (free=60/pro=120/business=300), 3.APIKeyAuth (JWT+APIKey), 4.RLS (X-User-ID), 5.EndpointRateLimit (LLM ops), 6.BodySizeLimit (5MB/10MB), 7.CatchAll (exceptions->JSON), 8.RequestIdTiming (X-Request-Id, X-Process-Time). Rules: CORS outermost, Auth before RLS, CatchAll before CORS.

### 3.6 startup_sequence_contract.yaml
14 ordered checks: 1.database(init_pool,required), 2.migrations(auto_run,depends:db), 3.redis(fallback:in_memory), 4.rate_limiter(depends:redis), 5.e2b(mock), 6.stripe(mock), 7.mercadopago(mock), 8.mercadolivre(oauth+sync), 9.bling(oauth+bg_refresh), 10.execution_pipeline(health), 11.llm_tracking(table+callback), 12.credits(tables), 13.mentor(tables), 14.referral(tables). Shutdown: close_pool, close_redis.

---

## WAVE 3B: OUTPUT TEMPLATES (P05) -- 6 CREATE in N05/P05_output/

### 3.7 output_railway_toml.md
Standard railway.toml template for new services. Includes: [build] nixpacks + buildCommand, [deploy] startCommand + healthcheckPath + restart + replicas, [env] PYTHONUNBUFFERED + ENV. Variants: python_api (uvicorn), node_spa (serve dist), gateway (python -m). Each variant with explanatory comments.

### 3.8 output_deploy_checklist.md
12-item pre-deploy checklist based on the actual flow:
1. railway.toml valido (schema 3.1)
2. .env vars completas (schema 3.3)
3. migrations testadas (UP+DOWN)
4. health endpoint respondendo local
5. CORS origins updated
6. rate limit config reviewed
7. middleware stack intact (schema 3.5)
8. railway link --service correto
9. railway up executado
10. /health returns healthy < 30s
11. /pipeline/health tiers operational
12. logs monitored 60s without errors

### 3.9 output_rollback_plan.md
Template for 4-service topology:
- Affected service: [api|frontend|gateway|dashboard]
- Blast radius: [which services depend on it, CORS impact, auth impact]
- Data at risk: [irreversible migrations? data created?]
- Command: railway rollback --service [name]
- Post-rollback verification: /health + CORS + auth flow
- Communication: [who to notify, estimated downtime]

### 3.10 output_health_endpoint.md
FastAPI /health + /ready template based on the actual model:
- HealthResponse Pydantic model
- db_health() via asyncpg pool check
- cache_health() via Redis ping
- Degraded logic (db unhealthy = degraded)
- Pipeline health (tiers check)
- Complete copy-paste Python code

### 3.11 output_middleware_stack.md
8-layer middleware stack template with Python code:
- add_middleware order (last=outermost)
- CORSMiddleware config (origins, regex, headers, max_age)
- Custom middleware patterns (@app.middleware)
- Rate limit tiers config
- Body size limit patterns
- Exception->JSON converter
- Request ID + timing middleware

### 3.12 output_env_contract.md
.env.example template with all 63 vars categorized:
- Sections: required, cloud_tier, payments, oauth, pool, rate_limit, cost_control
- Each var with: description, default, mock behavior
- Validation on boot (which vars to log warning if absent)

---

## WAVE 4A: QUALITY GATES (P07) -- 1 REWRITE

### 4.1 quality_gate_operations.md (REWRITE)

| Gate | Threshold | Required |
|------|-----------|----------|
| deploy_smoke | /health healthy < 30s | yes |
| rollback_plan | covers 4 services | yes |
| migration_safe | UP+DOWN tested | yes |
| env_complete | 63 vars, 5 required | yes |
| health_full | db+cache+pipeline OK | yes |
| middleware_intact | 8 layers correct order | yes |
| startup_clean | 14 checks pass/fallback | yes |
| api_latency | p95 < 500ms | no |
| cors_valid | 4 origins whitelisted | yes |
| rate_limit_active | X-RateLimit headers | yes |

---

## WAVE 4B: ORCHESTRATION (P12) -- 3 REWRITE

### 4.2 dispatch_rule_operations.md
keywords: deploy, railway, backend, api, production, staging, database, migration, rollback, health, uvicorn, nixpacks, infra, scale, postgres, middleware, cors, rate-limit
receives_from: [N03, N07, N02(html assets)], handoff_to: [N03]
model: opus, mcps: [railway, postgresql]

### 4.3 workflow_operations.md
Deploy pipeline: validate_toml > validate_env > validate_migrations > validate_health_local > create_rollback_plan > railway up > verify_health_prod < 30s > verify_pipeline > monitor_logs 60s > signal_complete. On failure: execute rollback plan.

### 4.4 checkpoint_operations.md
Resume protocol: save step+service+sha+rollback, resume from step N, cleanup after confirm.

---

## ARTEFATOS PART 2 (16 total: 12 CREATE + 4 REWRITE)

W3A Schemas: 6 CREATE (railway_toml, api_response, env_var, health_check, middleware_stack, startup_sequence)
W3B Output: 6 CREATE (railway_toml, deploy_checklist, rollback_plan, health_endpoint, middleware_stack, env_contract)
W4A Quality: 1 REWRITE (quality_gate with 10 gates)
W4B Orch: 3 REWRITE (dispatch_rule, workflow, checkpoint)
