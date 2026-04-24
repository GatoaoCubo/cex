---
id: p01_kc_fastapi_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "FastAPI Patterns — Routers, Middleware, Auth, Lifecycle"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [fastapi, api, middleware, auth, python]
tldr: "Production FastAPI patterns from codexa-core (86K lines): middleware stack (CORS→RateLimit→Auth→RLS→Timing), router organization, health checks, lifecycle events, error handling, body size limits."
density_score: 0.93
related:
  - p05_output_middleware_stack
  - KC_N05_API_HEALTH_MONITORING
  - p06_schema_middleware_stack_contract
  - p05_output_health_endpoint
  - p01_kc_error_handling_python
  - KC_N05_UVICORN_PRODUCTION
  - p06_schema_startup_sequence
  - bld_sp_knowledge_card_software_project
  - p04_ex_software_project_api_service
  - KC_N05_ZERO_DOWNTIME_DEPLOY
---

# FastAPI Patterns

## App Structure

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My API", version="2.0.0",
    docs_url="/docs", redoc_url="/redoc",
)
```

## Middleware Stack (Order Matters)

Middleware wraps request/response. **Last added = outermost = runs first.**

```python
# Innermost → Outermost (execution order: 5,4,3,2,1 on request)
app.add_middleware(EndpointRateLimitMiddleware)  # 5: per-endpoint limits
app.add_middleware(RLSMiddleware)                 # 4: row-level security
app.add_middleware(APIKeyMiddleware)              # 3: auth check
app.add_middleware(TenantRateLimitMiddleware)     # 2: per-tenant limits
app.add_middleware(CORSMiddleware, ...)           # 1: CORS (outermost!)
```

**Critical**: CORS must be outermost so error responses from auth/rate-limit also get CORS headers. Without this, browser blocks 401/403 responses.

### Custom Middleware Pattern

```python
@app.middleware("http")
async def request_timing(request: Request, call_next):
    import uuid, time
    request_id = request.headers.get("X-Request-Id") or str(uuid.uuid4())[:8]
    request.state.request_id = request_id
    start = time.time()
    response = await call_next(request)
    response.headers["X-Request-Id"] = request_id
    response.headers["X-Process-Time"] = f"{(time.time()-start)*1000:.0f}ms"
    return response
```

### Auth Middleware (API Key + JWT)

```python
class APIKeyMiddleware(BaseHTTPMiddleware):
    PUBLIC_PATHS = {"/", "/health", "/docs", "/api/v1/auth/login"}
    PUBLIC_PREFIXES = ("/webhooks/",)

    async def dispatch(self, request, call_next):
        path = request.url.path
        if path in self.PUBLIC_PATHS or request.method == "OPTIONS":
            return await call_next(request)
        # Allow Bearer tokens (JWT handled by route deps)
        if request.headers.get("Authorization","").startswith("Bearer "):
            return await call_next(request)
        api_key = request.headers.get("X-API-Key")
        if not api_key or api_key not in _load_api_keys():
            return JSONResponse(status_code=401, content={"detail": "Missing/invalid key"})
        return await call_next(request)
```

## Router Organization

```
api/
├── main.py            # App creation, middleware, lifecycle
├── v1/                # Versioned routes
│   ├── __init__.py    # Aggregates all routers
│   ├── anuncios.py    # Domain router
│   ├── pesquisas.py
│   └── billing.py
├── core/              # Business logic (no routes)
│   ├── db.py          # Database pool
│   ├── cache.py       # Redis cache
│   └── llm_gateway.py # LLM calls
├── middleware/         # Custom middleware
│   ├── auth.py
│   ├── rate_limit.py
│   └── rls.py
├── services/          # External integrations
└── tests/             # API tests
    ├── conftest.py
    └── test_*.py
```

## Health Check Pattern

```python
@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    db_status = await db_health()
    cache_status = await cache_health()
    overall = "degraded" if db_status["status"] == "unhealthy" else "healthy"
    return HealthResponse(
        status=overall, version=APP_VERSION,
        uptime_seconds=round(time.time() - _start_time, 2),
        database=db_status, cache=cache_status,
    )
```

## Lifecycle Events

```python
@app.on_event("startup")
async def startup():
    await init_db_pool()     # asyncpg connection pool
    await init_redis()       # Redis cache
    await run_migrations()   # Auto-migrate on deploy
    logger.info("API started", extra={"version": APP_VERSION})

@app.on_event("shutdown")
async def shutdown():
    await close_db_pool()
    await close_redis()
```

## Body Size Limit

```python
@app.middleware("http")
async def body_size_limit(request: Request, call_next):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > 5_000_000:  # 5MB
        return JSONResponse(status_code=413, content={"detail": "Body too large"})
    return await call_next(request)
```

## Error Handling

```python
@app.middleware("http")
async def catch_all(request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.error("Unhandled: %s %s -> %s", request.method, request.url.path, exc)
        return JSONResponse(status_code=500, content={"detail": "Internal error"})

@app.exception_handler(404)
async def not_found(request, exc):
    return JSONResponse(status_code=404,
        content={"detail": f"Not found: {request.url.path}", "docs": "/docs"})
```

## Anti-Patterns

- ❌ CORS not outermost (error responses blocked by browser)
- ❌ Business logic in route handlers (use core/ services)
- ❌ No health check (load balancer can't verify readiness)
- ❌ `@app.on_event("startup")` doing I/O without error handling
- ❌ Hardcoded CORS origins (use env var with defaults)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_middleware_stack]] | downstream | 0.68 |
| [[KC_N05_API_HEALTH_MONITORING]] | sibling | 0.48 |
| [[p06_schema_middleware_stack_contract]] | downstream | 0.40 |
| [[p05_output_health_endpoint]] | downstream | 0.32 |
| [[p01_kc_error_handling_python]] | sibling | 0.31 |
| [[KC_N05_UVICORN_PRODUCTION]] | sibling | 0.28 |
| [[p06_schema_startup_sequence]] | downstream | 0.27 |
| [[bld_sp_knowledge_card_software_project]] | sibling | 0.25 |
| [[p04_ex_software_project_api_service]] | downstream | 0.24 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | sibling | 0.24 |
