---
id: p06_schema_startup_sequence
kind: input_schema
pillar: P06
title: "Startup Sequence Contract — 14 Checks"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.1
tags: [schema, startup, health, deploy, railway, lifespan]
tldr: "14-check ordered startup sequence with fallbacks. Shutdown cleanup. Lifespan protocol."
density_score: 1.0
---

# Startup Sequence Contract — 14 Checks

## Schema Purpose
Defines the exact order of service initialization at boot (FastAPI lifespan).
Each check has a dependency, fallback behavior, and failure mode.

---

## Startup Sequence

| # | Service | Depends On | Required | Fallback | Timeout |
|---|---------|-----------|----------|----------|---------|
| 1 | **Database Pool** | — | yes | FATAL exit | 30s |
| 2 | **Auto Migrations** | #1 db | yes | FATAL exit | 60s |
| 3 | **Redis** | — | no | in-memory dict | 10s |
| 4 | **Rate Limiter** | #3 redis | yes | in-memory fallback | 5s |
| 5 | **E2B Sandbox** | — | no | mock (returns sample) | 10s |
| 6 | **Stripe** | — | no | mock (test keys) | 10s |
| 7 | **MercadoPago** | — | no | mock (test access_token) | 10s |
| 8 | **MercadoLivre** | — | no | mock (oauth skip) | 15s |
| 9 | **Bling ERP** | — | no | mock (oauth skip, bg_refresh off) | 15s |
| 10 | **Execution Pipeline** | #1 db | yes | degraded (local tier only) | 10s |
| 11 | **LLM Tracking** | #1 db | yes | log-only fallback | 5s |
| 12 | **Credits System** | #1 db | yes | free-mode (no deductions) | 5s |
| 13 | **Mentor System** | #1 db | no | disabled | 5s |
| 14 | **Referral System** | #1 db | no | disabled | 5s |

## Startup Rules

```yaml
rules:
  order: "strictly sequential (1 → 14)"
  required_failure: "log.critical() + sys.exit(1)"
  optional_failure: "log.warning() + set mock/disabled + continue"
  total_budget: "< 45 seconds for all 14 checks"
  health_after: "/health returns 200 only after all 14 complete"
```

## Detailed Check Specs

### #1 Database Pool (REQUIRED)
```yaml
database:
  driver: asyncpg
  pool_min: 3
  pool_max: 20
  command_timeout: 60
  ssl: "prefer"
  url_env: "DATABASE_URL"
  validation: "SELECT 1"
  on_fail: "sys.exit(1) — cannot operate without DB"
```

### #2 Auto Migrations (REQUIRED)
```yaml
migrations:
  strategy: "run on startup"
  direction: "UP only (never auto-DOWN)"
  lock: "advisory lock to prevent parallel migration"
  depends: "#1 database pool must be ready"
  on_fail: "sys.exit(1) — schema mismatch is fatal"
```

### #3 Redis (OPTIONAL)
```yaml
redis:
  url_env: "REDIS_URL"
  fallback: "in-memory dict (TTL via asyncio)"
  use_cases: ["rate-limit counters", "session cache", "pub/sub"]
  on_fail: "log.warning('Redis unavailable, using in-memory')"
```

### #5-#9 External Services (OPTIONAL)
```yaml
external_services:
  pattern: "try connect → on fail → set MOCK_MODE=true → log warning"
  mock_behavior:
    e2b: "return sample code execution result"
    stripe: "accept all payments, return test charge_id"
    mercadopago: "accept PIX, return test payment_id"
    mercadolivre: "skip OAuth, return empty listings"
    bling: "skip OAuth, disable background refresh"
  env_detection: "if *_API_KEY missing or empty → auto-mock"
```

### #10 Execution Pipeline (REQUIRED)
```yaml
pipeline:
  tiers: ["local", "cloud", "e2b"]
  health_check: "pipeline.health() returns available tiers"
  degraded: "if only local tier → status: degraded (not unhealthy)"
  depends: "#1 database"
```

## Shutdown Sequence

```yaml
shutdown:
  order:
    1: "Stop accepting new requests (graceful)"
    2: "Wait for in-flight requests (timeout: 30s)"
    3: "Close Redis connection"
    4: "Close database pool (await pool.close())"
    5: "Log shutdown complete"
  signal: "SIGTERM from Railway"
  grace_period: "30 seconds before SIGKILL"
```

## Lifespan Implementation

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: 14 checks in order
    await init_database_pool()      # 1
    await run_migrations()          # 2
    await init_redis()              # 3
    await init_rate_limiter()       # 4
    await init_e2b()                # 5
    await init_stripe()             # 6
    await init_mercadopago()        # 7
    await init_mercadolivre()       # 8
    await init_bling()              # 9
    await init_pipeline()           # 10
    await init_llm_tracking()       # 11
    await init_credits()            # 12
    await init_mentor()             # 13
    await init_referral()           # 14
    logger.info("All 14 startup checks complete")
    
    yield  # App runs here
    
    # SHUTDOWN
    await close_redis()
    await close_database_pool()
    logger.info("Shutdown complete")
```
