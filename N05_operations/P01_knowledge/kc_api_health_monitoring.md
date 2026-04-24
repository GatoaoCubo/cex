---
id: KC_N05_API_HEALTH_MONITORING
title: API Health Monitoring — /health, /ready, /live, Logging, Sentry, OpenTelemetry
domain: N05_operations
kind: knowledge_card
8f: F3_inject
pillar: P05
tags: [health, monitoring, observability, logging, sentry, opentelemetry, correlation-id, p95, p99, error-budget]
quality: 9.0
sources:
  - https://docs.railway.com/guides/healthchecks
  - https://github.com/zhanymkanov/fastapi-best-practices
  - https://sentry.io/for/fastapi/
  - https://opentelemetry.io/docs/languages/python/
created: 2026-04-01
related:
  - p01_kc_fastapi_patterns
  - p05_output_health_endpoint
  - p05_output_middleware_stack
  - p01_kc_error_handling_python
  - KC_N05_ZERO_DOWNTIME_DEPLOY
  - p01_kc_api_health_monitoring
  - p06_schema_health_response
  - SPEC_06_multi_provider
  - KC_N05_UVICORN_PRODUCTION
  - bld_sp_knowledge_card_software_project
---

# KC: API Health Monitoring

**Domain**: Operations / Observability  
**Sources**: Railway health docs, FastAPI best practices, OpenTelemetry, Sentry  
**Quality**: 9.0

---

## 1. Three Probe Types

| Probe | Path | Purpose | Depth |
|-------|------|---------|-------|
| **Health** | `/health` | Is the process alive? | Shallow — no DB |
| **Ready** | `/ready` | Can it serve traffic? | Deep — checks DB, cache |
| **Live** | `/live` | Should it be restarted? | Medium — detects deadlock |

**Railway uses only `/health`** as a deploy gate (returns 200 = traffic swap proceeds). Kubernetes uses all three as separate probes.

---

## 2. Endpoint Implementations

```python
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import time

app = FastAPI()
_start_time = time.time()

# --- Shallow: process alive ---
@app.get("/health")
async def health():
    return {"status": "ok", "uptime_s": int(time.time() - _start_time)}

# --- Deep: dependencies ok ---
@app.get("/ready")
async def ready():
    checks = {}
    overall = "ready"

    # DB check
    try:
        async with db_pool.connect() as conn:
            await conn.execute(text("SELECT 1"))
        checks["db"] = "ok"
    except Exception as e:
        checks["db"] = f"error: {e}"
        overall = "not_ready"

    # Cache check (optional)
    try:
        await redis.ping()
        checks["cache"] = "ok"
    except Exception as e:
        checks["cache"] = f"error: {e}"
        # cache down = degraded, not failed

    code = status.HTTP_200_OK if overall == "ready" else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse(status_code=code, content={"status": overall, "checks": checks})

# --- Liveness: detect stuck process ---
@app.get("/live")
async def live():
    # Add custom liveness logic if needed (e.g., queue not stuck)
    return {"status": "alive"}
```

---

## 3. Structured JSON Logging

Replace print/plain text logs with structured JSON for log aggregation (Railway, Datadog, etc.):

```python
import logging
import json
import time
from typing import Any

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        # Merge extra fields
        for key, val in record.__dict__.items():
            if key not in ("msg", "args", "levelname", "levelno", "pathname",
                           "filename", "module", "exc_info", "exc_text",
                           "stack_info", "lineno", "funcName", "created",
                           "msecs", "relativeCreated", "thread", "threadName",
                           "processName", "process", "name", "message"):
                log_data[key] = val
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)

def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler])
```

---

## 4. Correlation IDs

Every request gets a unique ID that propagates through all log lines:

```python
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import contextvars

request_id_var: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="")

class CorrelationIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        req_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_var.set(req_id)
        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        return response

app.add_middleware(CorrelationIDMiddleware)

# In any log call:
logger.info("Processing payment", extra={"request_id": request_id_var.get(), "user_id": user_id})
```

**Output in logs:**
```json
{"timestamp": "2026-04-01T12:00:00", "level": "INFO", "message": "Processing payment",
 "request_id": "a3f2b1c4-...", "user_id": "usr_123"}
```

---

## 5. Uptime Tracking

```python
import time

_start_time: float = time.time()

def get_uptime() -> dict:
    elapsed = time.time() - _start_time
    return {
        "uptime_seconds": int(elapsed),
        "uptime_human": f"{int(elapsed // 3600)}h {int((elapsed % 3600) // 60)}m"
    }

@app.get("/health")
async def health():
    return {"status": "ok", **get_uptime()}
```

---

## 6. p95/p99 Latency Tracking

Track response time percentiles with middleware:

```python
import time
import statistics
from collections import deque
from threading import Lock

_latencies: deque = deque(maxlen=1000)  # rolling window
_lock = Lock()

class LatencyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        with _lock:
            _latencies.append(duration_ms)
        response.headers["X-Response-Time-Ms"] = f"{duration_ms:.1f}"
        return response

def get_percentiles() -> dict:
    with _lock:
        if not _latencies:
            return {}
        sorted_lat = sorted(_latencies)
        n = len(sorted_lat)
        return {
            "p50_ms": sorted_lat[int(n * 0.50)],
            "p95_ms": sorted_lat[int(n * 0.95)],
            "p99_ms": sorted_lat[int(n * 0.99)],
            "count": n,
        }

@app.get("/metrics")
async def metrics():
    return get_percentiles()
```

---

## 7. Error Budgets

Error budget = percentage of requests allowed to fail within a time window (SLO-based):

```
SLO: 99.9% availability → error budget = 0.1% of requests
Monthly budget: 43.8 minutes of downtime OR equivalent error rate
```

**Simple error rate tracker:**

```python
from collections import deque
import time

_request_log: deque = deque(maxlen=10000)  # (timestamp, is_error)

class ErrorBudgetMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        is_error = response.status_code >= 500
        _request_log.append((time.time(), is_error))
        return response

def get_error_rate(window_seconds: int = 3600) -> dict:
    cutoff = time.time() - window_seconds
    recent = [(ts, err) for ts, err in _request_log if ts > cutoff]
    if not recent:
        return {"error_rate": 0.0, "sample_size": 0}
    errors = sum(1 for _, err in recent if err)
    return {
        "error_rate_pct": round(errors / len(recent) * 100, 3),
        "errors": errors,
        "total": len(recent),
        "window_h": window_seconds / 3600,
    }
```

---

## 8. Sentry Integration (FastAPI)

```bash
pip install sentry-sdk[fastapi]
```

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    integrations=[
        FastApiIntegration(transaction_style="endpoint"),
        SqlalchemyIntegration(),
    ],
    traces_sample_rate=0.1,    # 10% of requests traced (performance)
    profiles_sample_rate=0.1,  # 10% profiled
    environment=settings.ENVIRONMENT,
    release=settings.APP_VERSION,
)
```

**What Sentry captures automatically:**
- Unhandled exceptions + stack traces
- Slow DB queries (via SqlalchemyIntegration)
- Request context (URL, headers, user)
- Performance traces (via traces_sample_rate)

**Manual error capture:**
```python
try:
    result = risky_operation()
except Exception as e:
    sentry_sdk.capture_exception(e)
    raise
```

---

## 9. OpenTelemetry (Python)

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

# Setup tracer
provider = TracerProvider()
exporter = OTLPSpanExporter(endpoint=settings.OTEL_ENDPOINT)
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

# Auto-instrument FastAPI
FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)

# Manual spans
tracer = trace.get_tracer(__name__)

@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    with tracer.start_as_current_span("fetch_order") as span:
        span.set_attribute("order.id", order_id)
        order = await db.get_order(order_id)
        return order
```

---

## 10. Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|-------------|---------|-----|
| `/health` hits DB | Deploy fails if DB slow | Shallow `/health`, deep `/ready` |
| Plain text logs | Unparseable in log aggregators | Structured JSON |
| No correlation ID | Can't trace a request across logs | Add middleware |
| print() for logging | No level, no structure, no routing | Use `logging` module |
| Catching all exceptions silently | Errors disappear | Log + re-raise or capture to Sentry |
| traces_sample_rate=1.0 in prod | 10x performance overhead | Use 0.05-0.10 in production |
| No error budget tracking | Can't know SLO status | Track 5xx rate vs total |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_fastapi_patterns]] | sibling | 0.43 |
| [[p05_output_health_endpoint]] | related | 0.43 |
| [[p05_output_middleware_stack]] | related | 0.42 |
| [[p01_kc_error_handling_python]] | sibling | 0.41 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | sibling | 0.33 |
| [[p01_kc_api_health_monitoring]] | sibling | 0.25 |
| [[p06_schema_health_response]] | downstream | 0.24 |
| [[SPEC_06_multi_provider]] | upstream | 0.24 |
| [[KC_N05_UVICORN_PRODUCTION]] | sibling | 0.22 |
| [[bld_sp_knowledge_card_software_project]] | sibling | 0.21 |
