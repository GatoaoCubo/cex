---
id: p05_output_health_endpoint
kind: output_validator
pillar: P05
title: "Health Endpoint Template — FastAPI /health + /ready"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.0
tags: [output, template, health, fastapi, monitoring]
tldr: "Copy-paste FastAPI health endpoints — /health, /ready, /pipeline/health with real Pydantic models."
density_score: 0.98
---

# Health Endpoint Template

## Purpose
Production-ready health check endpoints for FastAPI services on Railway.
Includes database pool check, cache check, and pipeline tier availability.

---

## Complete Python Implementation

```python
"""Health check endpoints — copy-paste ready for FastAPI."""
from datetime import datetime, timezone
from time import time
from typing import Optional

from fastapi import APIRouter, Response
from pydantic import BaseModel

router = APIRouter(tags=["health"])

# ─── Track startup time ─────────────────────────────────────
_start_time = time()


# ─── Models ──────────────────────────────────────────────────
class ServiceStatus(BaseModel):
    status: str  # "healthy" | "unhealthy"
    connected: bool
    latency_ms: Optional[float] = None
    pool_size: Optional[int] = None


class HealthResponse(BaseModel):
    status: str  # "healthy" | "degraded" | "unhealthy"
    version: str
    timestamp: str
    uptime_seconds: float
    environment: str
    database: ServiceStatus
    cache: ServiceStatus


class PipelineHealthResponse(BaseModel):
    status: str
    pipeline: str
    available_tiers: list[str]  # ["local", "cloud", "e2b"]
    timestamp: str


# ─── Health Checks ───────────────────────────────────────────
async def check_database() -> ServiceStatus:
    """Check asyncpg pool connectivity."""
    from app.database import get_pool  # adjust import
    try:
        pool = get_pool()
        start = time()
        async with pool.acquire() as conn:
            await conn.fetchval("SELECT 1")
        latency = (time() - start) * 1000
        return ServiceStatus(
            status="healthy",
            connected=True,
            latency_ms=round(latency, 2),
            pool_size=pool.get_size(),
        )
    except Exception:
        return ServiceStatus(status="unhealthy", connected=False)


async def check_cache() -> ServiceStatus:
    """Check Redis connectivity."""
    from app.cache import get_redis  # adjust import
    try:
        redis = get_redis()
        if redis is None:
            return ServiceStatus(status="healthy", connected=False)  # in-memory fallback
        start = time()
        await redis.ping()
        latency = (time() - start) * 1000
        return ServiceStatus(
            status="healthy",
            connected=True,
            latency_ms=round(latency, 2),
        )
    except Exception:
        return ServiceStatus(status="unhealthy", connected=False)


# ─── Endpoints ───────────────────────────────────────────────
@router.get("/health", response_model=HealthResponse)
async def health_check(response: Response):
    """
    Main health endpoint. No auth required.
    Railway uses this for deploy health checks.
    
    Returns:
        - healthy: all services OK
        - degraded: database unhealthy but app running
        - unhealthy: critical failure
    """
    import os
    from app import __version__  # adjust import

    db = await check_database()
    cache = await check_cache()

    # Determine overall status
    if db.status == "unhealthy":
        overall = "degraded"
        response.status_code = 200  # Still return 200 for Railway
    else:
        overall = "healthy"

    return HealthResponse(
        status=overall,
        version=__version__,
        timestamp=datetime.now(timezone.utc).isoformat(),
        uptime_seconds=round(time() - _start_time, 2),
        environment=os.getenv("ENV", "development"),
        database=db,
        cache=cache,
    )


@router.get("/ready")
async def readiness_check():
    """
    Readiness probe — returns 200 only when fully initialized.
    Use for load balancer routing decisions.
    """
    db = await check_database()
    if db.status == "unhealthy":
        return Response(status_code=503, content='{"status": "not ready"}',
                        media_type="application/json")
    return {"status": "ready"}


@router.get("/pipeline/health", response_model=PipelineHealthResponse)
async def pipeline_health():
    """Check which execution tiers are available."""
    import os

    tiers = ["local"]  # always available
    if os.getenv("ANTHROPIC_API_KEY") or os.getenv("OPENAI_API_KEY"):
        tiers.append("cloud")
    if os.getenv("E2B_API_KEY"):
        tiers.append("e2b")

    return PipelineHealthResponse(
        status="healthy" if len(tiers) >= 2 else "degraded",
        pipeline="execution",
        available_tiers=tiers,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
```

## Response Examples

### Healthy
```json
{
  "status": "healthy",
  "version": "2.1.0",
  "timestamp": "2026-04-01T12:00:00.000Z",
  "uptime_seconds": 3642.51,
  "environment": "production",
  "database": {
    "status": "healthy",
    "connected": true,
    "latency_ms": 1.23,
    "pool_size": 5
  },
  "cache": {
    "status": "healthy",
    "connected": true,
    "latency_ms": 0.45,
    "pool_size": null
  }
}
```

### Degraded
```json
{
  "status": "degraded",
  "version": "2.1.0",
  "database": {
    "status": "unhealthy",
    "connected": false
  },
  "cache": {
    "status": "healthy",
    "connected": true
  }
}
```

## Integration

```python
# In main.py
from app.health import router as health_router
app.include_router(health_router)
```
