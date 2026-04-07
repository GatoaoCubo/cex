---
id: KC_N05_ZERO_DOWNTIME_DEPLOY
title: Zero-Downtime Deploy Patterns
domain: N05_operations
kind: knowledge_card
pillar: P05
tags: [deploy, zero-downtime, blue-green, railway, sigterm, migrations, rollback, 12-factor]
quality: 9.1
sources:
  - https://docs.railway.com/guides/healthchecks
  - https://12factor.net/
  - https://fastapi.tiangolo.com/deployment/concepts/
created: 2026-04-01
---

# KC: Zero-Downtime Deploy Patterns

**Domain**: Operations / Deploy  
**Sources**: Railway docs, 12-Factor App, FastAPI deployment  
**Quality**: 9.0

---

## 1. Core Concept

Zero-downtime deploy = new version receives traffic ONLY after it passes a health gate. Old version continues serving until the new one is ready. Requires: health checks, graceful shutdown, and migration sequencing.

---

## 2. Railway Health Gate

Railway blocks traffic routing until the health endpoint returns HTTP 200:

```
Deploy triggered
  → new container starts
  → Railway polls GET /health every ~5s
  → if 200 within timeout: swap traffic to new container
  → if timeout exceeded: deploy fails, old container stays live
```

**Config:**
- Health endpoint path: set in service settings (e.g., `/health`)
- Timeout: default 300s — override with `RAILWAY_HEALTHCHECK_TIMEOUT_SEC`
- PORT: Railway injects `PORT` env var — app MUST listen on it
- Allow requests from: `healthcheck.railway.app`

**Critical**: Railway does NOT monitor health after deploy. Only gates the initial traffic swap.

---

## 3. Blue-Green on Railway

Railway supports blue-green via **environments** (not built-in blue-green toggle):

```
Pattern:
  production env  = "blue"  (live traffic)
  staging env     = "green" (new version deploys here first)

Flow:
  1. Deploy to staging/green
  2. Run smoke tests against staging URL
  3. If pass → promote to production (redeploy or env variable update)
  4. If fail → staging stays broken, production untouched
```

For true blue-green within one environment, use Railway's **deploy pipeline** + health checks to gate traffic.

---

## 4. SIGTERM Handling (Graceful Shutdown)

When Railway terminates a container, it sends SIGTERM. The app has a window to finish in-flight requests before SIGKILL.

**FastAPI + Uvicorn pattern:**

```python
import signal
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown — cleanup connections, flush queues
    await db_pool.close()
    await redis.close()

app = FastAPI(lifespan=lifespan)
```

**Uvicorn graceful shutdown config:**
```bash
uvicorn main:app \
  --timeout-graceful-shutdown 30  # wait up to 30s for in-flight requests
```

**What happens on SIGTERM:**
1. Uvicorn stops accepting new connections
2. Waits for in-flight requests up to `timeout-graceful-shutdown`
3. Runs lifespan shutdown block
4. Exits cleanly

---

## 5. Connection Draining

Before shutdown, drain active connections:

```python
# In lifespan shutdown:
# 1. Stop accepting new DB connections
await db_pool.close()

# 2. Wait for active queries to complete (with timeout)
await asyncio.wait_for(db_pool.wait_closed(), timeout=25.0)

# 3. Close message queue consumers
await consumer.stop()
```

**Rule**: Always set `timeout-graceful-shutdown` > your longest expected request duration. For Railway, 30s is a safe default for CRUD APIs.

---

## 6. Migration Sequencing

DB migrations must run ONCE before new app code starts serving traffic. Running migrations inside the app startup causes race conditions with multiple workers.

**Railway pattern — separate migration service or start command:**

```dockerfile
# Dockerfile CMD for production
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port $PORT --workers 2"]
```

**Problem**: If you have multiple replicas, all run `alembic upgrade head` simultaneously.

**Fix — use a Railway custom start command with a lock or run-once job:**
```bash
# Option 1: single replica runs migrations first (set replica=1 during deploy)
# Option 2: Alembic with advisory lock (pg_try_advisory_lock)
# Option 3: separate Railway job service that runs migrations, then scales up app
```

**Backward-compatible migration rule** (12-Factor):
- New column: add nullable first, deploy app, then add NOT NULL constraint
- Rename column: add new column, dual-write, migrate data, remove old
- Never DROP a column in the same deploy that removes code using it

---

## 7. Rollback Automation

Railway rollback = redeploy a previous deployment from the UI or CLI:

```bash
# Via Railway CLI
railway rollback [deployment-id]
```

**Automated rollback trigger:**
```bash
# Post-deploy health check script
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" https://your-app.railway.app/health)
if [ "$HEALTH" != "200" ]; then
  echo "Health check failed: $HEALTH — triggering rollback"
  railway rollback
fi
```

**Migration rollback**: Always write `downgrade()` in Alembic migrations. Before a risky deploy:
```bash
# Save current revision
alembic current  # e.g., abc123

# If rollback needed:
alembic downgrade abc123
```

---

## 8. 12-Factor Patterns (Deploy-Relevant)

| Factor | Rule | Impact on Zero-Downtime |
|--------|------|------------------------|
| **Config** (III) | Store config in env vars, never code | Swap config without rebuild |
| **Processes** (VI) | Stateless processes, no sticky sessions | Any instance can be killed |
| **Disposability** (IX) | Fast startup, graceful shutdown | Minimize traffic gap during swap |
| **Dev/Prod Parity** (X) | Same stack dev and prod | Catch issues before deploy |
| **Build/Release/Run** (V) | Separate stages strictly | Rollback = switch release, not rebuild |

**Stateless process rule**: Never store session state in local memory. Use Redis or DB. This enables killing any worker at any time without losing user state.

---

## 9. Health Endpoint Implementation

```python
from fastapi import FastAPI, status
from sqlalchemy import text

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    """Railway health gate — must return 200 for deploy to proceed."""
    return {"status": "ok"}

@app.get("/ready", status_code=status.HTTP_200_OK)
async def ready():
    """Deep readiness check — DB connectivity."""
    try:
        async with db.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "ready", "db": "ok"}
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not_ready", "db": str(e)}
        )
```

Use `/health` (shallow) for Railway health gate. Use `/ready` (deep) for internal orchestration checks.

---

## 10. Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|-------------|---------|-----|
| Running migrations inside each worker | Race condition, lock contention | Run once before workers start |
| No SIGTERM handler | Requests dropped mid-flight | Implement lifespan shutdown |
| Health endpoint hits external DB | Deploy fails if DB is slow | Use shallow `/health`, deep `/ready` |
| Storing session in local memory | Rolling restart loses sessions | Use Redis for session state |
| DROP column same deploy as code removal | Old instances fail on new schema | Two-phase migration |
| No rollback plan | Stuck on broken deploy | Always have `alembic downgrade` ready |
