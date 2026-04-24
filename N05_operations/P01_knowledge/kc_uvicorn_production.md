---
id: KC_N05_UVICORN_PRODUCTION
title: Uvicorn Production Configuration — Workers, uvloop, Gunicorn, FastAPI Practices
domain: N05_operations
kind: knowledge_card
8f: F3_inject
pillar: P05
tags: [uvicorn, gunicorn, workers, uvloop, httptools, fastapi, production, graceful-reload, memory]
quality: 9.1
sources:
  - https://www.uvicorn.org/deployment/
  - https://www.uvicorn.org/settings/
  - https://fastapi.tiangolo.com/deployment/server-workers/
  - https://github.com/zhanymkanov/fastapi-best-practices
created: 2026-04-01
related:
  - KC_N05_ZERO_DOWNTIME_DEPLOY
  - p01_kc_deploy_paas
  - p01_kc_context_parallelization
  - p05_output_railway_toml
  - p02_agent_railway_superintendent
  - KC_N05_NIXPACKS_BUILDPACKS
  - p03_sp_railway_superintendent
  - p10_lr_daemon_builder
  - p06_schema_railway_toml
  - p01_kc_docker_patterns
---

# KC: Uvicorn Production Configuration

**Domain**: Operations / Runtime  
**Sources**: Uvicorn docs (deployment + settings), FastAPI server workers, Gunicorn docs  
**Quality**: 9.0

---

## 1. Worker Count Formula

```
workers = (2 * CPU_cores) + 1
```

| CPUs | Workers |
|------|---------|
| 1 | 3 |
| 2 | 5 |
| 4 | 9 |
| 8 | 17 |

**Railway note**: Railway Hobby plan = 8 vCPU shared. In practice, for API services start with `workers=2` and scale based on observed CPU usage. More workers = more RAM consumed.

**Memory estimate**: Each Uvicorn worker uses ~50-100MB base + your model size. For a typical FastAPI CRUD API: ~80MB/worker. With 4 workers: ~320MB.

**Set via env var** (12-Factor compatible):
```bash
WEB_CONCURRENCY=5  # uvicorn reads this automatically if --workers not set
```

---

## 2. Gunicorn + Uvicorn (Recommended for Production)

Gunicorn acts as the process manager; Uvicorn workers handle async I/O:

```bash
gunicorn main:app \
  -k uvicorn.workers.UvicornWorker \
  --workers 4 \
  --bind 0.0.0.0:$PORT \
  --timeout 120 \
  --keepalive 5 \
  --graceful-timeout 30 \
  --access-logfile - \
  --error-logfile -
```

**Note**: `uvicorn.workers` module is deprecated in newer versions. Migrate to `uvicorn-worker` package:

```bash
pip install uvicorn-worker
```

```bash
gunicorn main:app \
  -k uvicorn_worker.UvicornWorker \
  --workers 4 \
  --bind 0.0.0.0:$PORT
```

**Why Gunicorn + Uvicorn over plain Uvicorn?**
- Gunicorn manages worker restarts automatically (dead worker → respawn)
- Supports zero-downtime reload via SIGHUP
- Battle-tested process supervision
- `UvicornH11Worker` available for PyPy environments

---

## 3. Plain Uvicorn (Single Process / Containers)

For Docker/Railway single containers, plain Uvicorn with multiple workers:

```bash
uvicorn main:app \
  --host 0.0.0.0 \
  --port $PORT \
  --workers 4 \
  --loop uvloop \
  --http httptools \
  --timeout-keep-alive 5 \
  --timeout-graceful-shutdown 30 \
  --access-log \
  --log-level info
```

**FastAPI CLI wrapper** (equivalent):
```bash
fastapi run --workers 4 main.py
```

---

## 4. uvloop (Event Loop Optimization)

```bash
pip install uvloop
```

```bash
uvicorn main:app --loop uvloop
```

**Performance gain**: uvloop is a Cython reimplementation of asyncio's event loop. Typically 2-4x faster than the default asyncio loop for I/O-heavy workloads.

**Default**: `--loop auto` uses uvloop if installed, falls back to asyncio.

**httptools** (HTTP parser):
```bash
pip install httptools
```
```bash
uvicorn main:app --http httptools  # faster HTTP parsing vs h11
```

---

## 5. Key Settings Reference

| Setting | Default | Production Value | Notes |
|---------|---------|-----------------|-------|
| `--workers` | 1 | `2*CPU+1` | Or via `WEB_CONCURRENCY` |
| `--loop` | auto | `uvloop` | Install uvloop first |
| `--http` | auto | `httptools` | Install httptools first |
| `--timeout-keep-alive` | 5 | 5 | Close idle connections after 5s |
| `--timeout-graceful-shutdown` | None | 30 | Wait 30s before SIGKILL |
| `--backlog` | 2048 | 2048 | Max pending connections queue |
| `--limit-concurrency` | None | 1000 | Return 503 above this limit |
| `--log-level` | info | info | Use `warning` in high-traffic |
| `--access-log` | enabled | enabled (pipe to aggregator) | Disable with `--no-access-log` |

---

## 6. Graceful Reload (Zero-Downtime Code Update)

**With Gunicorn** — send SIGHUP for rolling worker restart:

```bash
# Find gunicorn master PID
cat /tmp/gunicorn.pid  # or: pgrep -f gunicorn

# Rolling restart (zero-downtime)
kill -HUP <master_pid>
```

What happens:
1. Master receives SIGHUP
2. Spawns new workers with new code
3. Old workers finish in-flight requests
4. Old workers killed after `graceful-timeout`

**With plain Uvicorn** — no built-in rolling restart. Use SIGTERM + container restart (Railway handles this):
```bash
# Railway redeploy triggers SIGTERM → uvicorn drains → new container starts
# Health check gate ensures no traffic until new instance is ready
```

---

## 7. Dockerfile for Production

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Run migrations then start (single-replica pattern)
CMD ["sh", "-c", "alembic upgrade head && gunicorn main:app -k uvicorn_worker.UvicornWorker --workers ${WEB_CONCURRENCY:-3} --bind 0.0.0.0:${PORT:-8000} --timeout 120 --graceful-timeout 30 --access-logfile - --error-logfile -"]
```

**requirements.txt (production deps):**
```
fastapi
uvicorn[standard]      # includes uvloop + httptools
uvicorn-worker
gunicorn
```

---

## 8. FastAPI-Specific Production Practices

### Async vs Sync decisions

```python
# CORRECT: async for I/O (DB, HTTP calls)
@app.get("/users/{id}")
async def get_user(id: int):
    return await db.fetch_user(id)  # non-blocking

# CORRECT: sync for CPU-bound (FastAPI runs in threadpool)
@app.post("/process")
def cpu_heavy(data: bytes):
    return process_image(data)  # GIL released in threadpool

# WRONG: blocking I/O in async — blocks entire event loop
@app.get("/bad")
async def bad():
    time.sleep(5)  # blocks ALL requests!
    return {}
```

### Lifespan for startup/shutdown

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create connection pool once (not per request)
    app.state.db = await create_db_pool(settings.DATABASE_URL)
    app.state.redis = await create_redis(settings.REDIS_URL)
    yield
    # Shutdown: drain connections gracefully
    await app.state.db.close()
    await app.state.redis.close()

app = FastAPI(lifespan=lifespan)
```

### Dependencies (cached per request)

```python
from functools import lru_cache

@lru_cache
def get_settings() -> Settings:
    return Settings()  # loaded once, cached forever

async def get_db(request: Request) -> AsyncSession:
    async with AsyncSession(request.app.state.db) as session:
        yield session
        # auto-commits or rolls back on exception
```

### Pydantic settings (12-Factor config)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str = "redis://localhost:6379"
    environment: str = "production"
    workers: int = 3

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

---

## 9. Memory Per Worker Optimization

```python
# Avoid loading large objects per-request — load once at startup

# BAD: reloads model every request
@app.post("/predict")
async def predict(data: Input):
    model = load_model("model.pkl")  # 500MB each call!
    return model.predict(data)

# GOOD: load once in lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = load_model("model.pkl")  # once
    yield

@app.post("/predict")
async def predict(data: Input, request: Request):
    return request.app.state.model.predict(data)
```

**Memory calculation before scaling workers:**
```
total_ram = base_worker_ram * workers + (shared_objects_if_any)
# base_worker_ram: measure with `psutil.Process().memory_info().rss`
```

---

## 10. Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|-------------|---------|-----|
| `workers=1` in production | No parallelism, single point of failure | Use `2*CPU+1` |
| No `--timeout-graceful-shutdown` | Requests dropped on restart | Set 30s |
| Blocking I/O in `async` function | Blocks entire event loop | Use sync route or `asyncio.to_thread()` |
| Not using uvloop | 2-4x slower event loop | `pip install uvloop`, `--loop uvloop` |
| Loading models per-request | Memory explosion | Load in lifespan, store in `app.state` |
| `--reload` in production | Performance hit, no multi-worker support | Only for development |
| No connection pool | New DB connection each request (slow) | SQLAlchemy async pool in lifespan |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | sibling | 0.34 |
| [[p01_kc_deploy_paas]] | sibling | 0.29 |
| [[p01_kc_context_parallelization]] | sibling | 0.27 |
| [[p05_output_railway_toml]] | related | 0.22 |
| [[p02_agent_railway_superintendent]] | upstream | 0.20 |
| [[KC_N05_NIXPACKS_BUILDPACKS]] | sibling | 0.20 |
| [[p03_sp_railway_superintendent]] | upstream | 0.19 |
| [[p10_lr_daemon_builder]] | downstream | 0.19 |
| [[p06_schema_railway_toml]] | downstream | 0.18 |
| [[p01_kc_docker_patterns]] | sibling | 0.18 |
