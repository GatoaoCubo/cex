---
id: p01_kc_error_handling_python
kind: knowledge_card
pillar: P01
title: "Error Handling Python — Exception Hierarchy, Retry, Circuit Breaker"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [error-handling, exceptions, retry, circuit-breaker, logging, python]
tldr: "Production error handling from codexa-core: custom exception hierarchy, structured logging with request IDs, retry with exponential backoff, circuit breaker for external services, graceful degradation."
density_score: 0.90
related:
  - SPEC_06_multi_provider
  - kc_model_context_protocol
  - KC_N05_API_HEALTH_MONITORING
  - SPEC_05_skills_runtime
  - bld_examples_repo_map
  - SPEC_07_gdp_enforcement
  - p09_ratelimit_anthropic_tier2
  - bld_sp_examples_software_project
  - kc_agentic_rag
  - atom_08_crewai
---

# Error Handling Python

## Exception Hierarchy

```python
class AppError(Exception):
    """Base for all application errors."""
    def __init__(self, message: str, code: str = "UNKNOWN", status: int = 500):
        self.message = message
        self.code = code
        self.status = status

class ValidationError(AppError):
    def __init__(self, message: str, field: str = None):
        super().__init__(message, code="VALIDATION_ERROR", status=422)
        self.field = field

class NotFoundError(AppError):
    def __init__(self, resource: str, id: str):
        super().__init__(f"{resource} {id} not found", code="NOT_FOUND", status=404)

class AuthError(AppError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, code="AUTH_ERROR", status=401)

class RateLimitError(AppError):
    def __init__(self, limit: int, reset_at: str):
        super().__init__(f"Rate limit exceeded ({limit}/min)", code="RATE_LIMIT", status=429)
        self.reset_at = reset_at

class ExternalServiceError(AppError):
    def __init__(self, service: str, detail: str):
        super().__init__(f"{service}: {detail}", code="EXTERNAL_ERROR", status=502)
```

## FastAPI Error Handler

```python
@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status,
        content={
            "error": exc.code,
            "message": exc.message,
            "request_id": getattr(request.state, "request_id", None),
        },
    )
```

## Structured Logging

```python
import logging
from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar("request_id", default="-")

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get("-")
        return True

def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)s] [req:%(request_id)s] %(name)s: %(message)s'
    ))
    handler.addFilter(RequestIdFilter())
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.INFO)
```

**Pattern**: Every log line includes `request_id` for tracing across middleware/services.

## Retry with Exponential Backoff

```python
import asyncio
import random

async def retry_async(fn, max_retries=3, base_delay=1.0, max_delay=30.0):
    """Retry with exponential backoff + jitter."""
    for attempt in range(max_retries + 1):
        try:
            return await fn()
        except (ConnectionError, TimeoutError) as e:
            if attempt == max_retries:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.1)
            await asyncio.sleep(delay + jitter)
            logging.warning(f"Retry {attempt+1}/{max_retries}: {e}")
```

## Circuit Breaker

```python
class CircuitBreaker:
    """Prevents cascading failures to external services."""
    def __init__(self, failure_threshold=5, reset_timeout=60):
        self.failures = 0
        self.threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.last_failure = 0
        self.state = "CLOSED"  # CLOSED | OPEN | HALF_OPEN

    async def call(self, fn):
        if self.state == "OPEN":
            if time.time() - self.last_failure > self.reset_timeout:
                self.state = "HALF_OPEN"
            else:
                raise ExternalServiceError("circuit-breaker", "Service unavailable")

        try:
            result = await fn()
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure = time.time()
            if self.failures >= self.threshold:
                self.state = "OPEN"
            raise
```

## Graceful Degradation

```python
async def get_data_with_fallback(id: str):
    """Try primary → cache → default."""
    try:
        return await db.fetch(id)
    except DatabaseError:
        logging.warning("DB down, trying cache")
        try:
            return await cache.get(f"data:{id}")
        except CacheError:
            logging.error("Cache also down, returning default")
            return default_data(id)
```

## Catch-All Middleware

```python
@app.middleware("http")
async def catch_all(request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logging.error("Unhandled: %s %s -> %s", request.method, request.url.path, exc)
        return JSONResponse(status_code=500, content={"detail": "Internal error"})
```

## Anti-Patterns

- ❌ Bare `except:` (catches SystemExit, KeyboardInterrupt)
- ❌ Logging raw exception without request context
- ❌ Retry without backoff (hammers failing service)
- ❌ No circuit breaker for external APIs (cascading failure)
- ❌ Returning 500 with stack trace to client (security leak)
- ❌ Catching exceptions and silently continuing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[SPEC_06_multi_provider]] | related | 0.34 |
| [[kc_model_context_protocol]] | sibling | 0.31 |
| [[KC_N05_API_HEALTH_MONITORING]] | sibling | 0.30 |
| [[SPEC_05_skills_runtime]] | related | 0.30 |
| [[bld_examples_repo_map]] | downstream | 0.29 |
| [[SPEC_07_gdp_enforcement]] | related | 0.27 |
| [[p09_ratelimit_anthropic_tier2]] | downstream | 0.27 |
| [[bld_sp_examples_software_project]] | downstream | 0.27 |
| [[kc_agentic_rag]] | sibling | 0.25 |
| [[atom_08_crewai]] | sibling | 0.25 |
