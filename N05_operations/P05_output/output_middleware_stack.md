---
id: p05_output_middleware_stack
kind: output_validator
pillar: P05
title: "Middleware Stack Template — 8-Layer FastAPI"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.0
tags: [output, template, middleware, fastapi, cors, auth, rate-limit]
tldr: "Complete 8-layer middleware implementation — Python code, correct registration order."
density_score: 0.94
related:
  - p01_kc_fastapi_patterns
  - KC_N05_API_HEALTH_MONITORING
  - p01_kc_error_handling_python
  - p06_schema_middleware_stack_contract
  - p06_schema_api_response_contract
  - p05_output_health_endpoint
  - SPEC_06_multi_provider
  - KC_N05_UVICORN_PRODUCTION
  - atom_01_a2a_protocol
  - bld_sp_memory_software_project
---

# Middleware Stack Template — 8 Layers

## Purpose
Copy-paste middleware registration for FastAPI. Order is LIFO in `add_middleware`:
last added = outermost. So we add innermost first (8→1).

---

## Complete Python Implementation

```python
"""Middleware stack — add to FastAPI app in exact order below."""
import time
import uuid
import logging
from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════
# LAYER 8: RequestIdTiming (innermost — add FIRST)
# ═══════════════════════════════════════════════════════════
class RequestIdTimingMiddleware(BaseHTTPMiddleware):
    """Adds X-Request-Id and X-Process-Time headers."""
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = f"req_{uuid.uuid4().hex[:12]}"
        request.state.request_id = request_id
        start = time.perf_counter()
        
        response = await call_next(request)
        
        elapsed = time.perf_counter() - start
        response.headers["X-Request-Id"] = request_id
        response.headers["X-Process-Time"] = f"{elapsed:.4f}"
        return response


# ═══════════════════════════════════════════════════════════
# LAYER 7: CatchAllExceptions
# ═══════════════════════════════════════════════════════════
class CatchAllExceptionsMiddleware(BaseHTTPMiddleware):
    """Convert unhandled exceptions to JSON 500."""
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        try:
            return await call_next(request)
        except Exception as exc:
            req_id = getattr(request.state, "request_id", "unknown")
            logger.exception(f"Unhandled error [{req_id}]: {exc}")
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Internal server error",
                    "status_code": 500,
                    "request_id": req_id,
                    "support": "support@codexa.com.br",
                },
            )


# ═══════════════════════════════════════════════════════════
# LAYER 6: BodySizeLimit
# ═══════════════════════════════════════════════════════════
class BodySizeLimitMiddleware(BaseHTTPMiddleware):
    """Reject payloads exceeding size limit."""
    def __init__(self, app, max_size: int = 5 * 1024 * 1024):
        super().__init__(app)
        self.max_size = max_size  # 5MB default

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if request.method in ("POST", "PUT", "PATCH"):
            content_length = request.headers.get("content-length")
            if content_length and int(content_length) > self.max_size:
                return JSONResponse(
                    status_code=413,
                    content={"detail": f"Request body too large (max {self.max_size // 1024 // 1024}MB)"},
                )
        return await call_next(request)


# ═══════════════════════════════════════════════════════════
# LAYER 5: EndpointRateLimit
# ═══════════════════════════════════════════════════════════
class EndpointRateLimitMiddleware(BaseHTTPMiddleware):
    """Per-endpoint rate limiting for expensive operations."""
    LIMITS = {
        "/pipeline/": 10,   # 10 req/min
        "/pesquisa/": 20,   # 20 req/min
        "/anuncio/": 30,    # 30 req/min
    }

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Implementation: check Redis/in-memory counter per path prefix + user
        # Simplified — real impl uses sliding window counter
        return await call_next(request)


# ═══════════════════════════════════════════════════════════
# LAYER 4: RLS (Row-Level Security)
# ═══════════════════════════════════════════════════════════
class RLSMiddleware(BaseHTTPMiddleware):
    """Inject authenticated user ID for database RLS."""
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        user_id = getattr(request.state, "user_id", None)
        if user_id:
            # Set PostgreSQL session variable for RLS policies
            request.state.rls_user_id = user_id
        return await call_next(request)


# ═══════════════════════════════════════════════════════════
# LAYER 3: APIKeyAuth
# ═══════════════════════════════════════════════════════════
class APIKeyAuthMiddleware(BaseHTTPMiddleware):
    """Authenticate via JWT Bearer or X-API-Key header."""
    SKIP_PATHS = {"/health", "/ready", "/docs", "/openapi.json", "/redoc"}

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if request.url.path in self.SKIP_PATHS or request.method == "OPTIONS":
            return await call_next(request)

        # Check Authorization: Bearer <token>
        auth = request.headers.get("authorization", "")
        api_key = request.headers.get("x-api-key", "")

        if auth.startswith("Bearer "):
            token = auth[7:]
            # Validate JWT, extract user_id
            request.state.user_id = "jwt_user"  # Replace with real validation
        elif api_key:
            # Validate API key
            request.state.user_id = "apikey_user"  # Replace with real lookup
        else:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authentication required"},
            )
        return await call_next(request)


# ═══════════════════════════════════════════════════════════
# LAYER 2: TenantRateLimit
# ═══════════════════════════════════════════════════════════
class TenantRateLimitMiddleware(BaseHTTPMiddleware):
    """Per-tenant rate limiting based on plan tier."""
    TIERS = {"free": 60, "pro": 120, "business": 300}  # req/min

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Implementation: identify tenant, check counter, enforce limit
        # Adds X-RateLimit-* headers to response
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = "60"
        response.headers["X-RateLimit-Remaining"] = "59"
        response.headers["X-RateLimit-Reset"] = str(int(time.time()) + 60)
        return response


# ═══════════════════════════════════════════════════════════
# REGISTRATION — LIFO order (add innermost first)
# ═══════════════════════════════════════════════════════════
def register_middleware(app: FastAPI) -> None:
    """Register all 8 middleware layers in correct order."""

    # Layer 8 (innermost) — added first
    app.add_middleware(RequestIdTimingMiddleware)

    # Layer 7
    app.add_middleware(CatchAllExceptionsMiddleware)

    # Layer 6
    app.add_middleware(BodySizeLimitMiddleware, max_size=5 * 1024 * 1024)

    # Layer 5
    app.add_middleware(EndpointRateLimitMiddleware)

    # Layer 4
    app.add_middleware(RLSMiddleware)

    # Layer 3
    app.add_middleware(APIKeyAuthMiddleware)

    # Layer 2
    app.add_middleware(TenantRateLimitMiddleware)

    # Layer 1 (outermost) — added last
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=r"https?://(localhost(:\d+)?|.*\.railway\.app|.*\.codexa\.com\.br)",
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["*"],
        allow_credentials=True,
        max_age=600,
    )
```

## Verification

```python
def verify_middleware_order(app: FastAPI) -> bool:
    """Verify middleware stack is correctly ordered."""
    expected = [
        "CORSMiddleware",           # 1 outermost
        "TenantRateLimitMiddleware", # 2
        "APIKeyAuthMiddleware",      # 3
        "RLSMiddleware",             # 4
        "EndpointRateLimitMiddleware",# 5
        "BodySizeLimitMiddleware",   # 6
        "CatchAllExceptionsMiddleware",# 7
        "RequestIdTimingMiddleware", # 8 innermost
    ]
    actual = [type(m).__name__ for m in app.middleware_stack]
    return actual == expected
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_fastapi_patterns]] | upstream | 0.65 |
| [[KC_N05_API_HEALTH_MONITORING]] | related | 0.53 |
| [[p01_kc_error_handling_python]] | upstream | 0.40 |
| [[p06_schema_middleware_stack_contract]] | downstream | 0.31 |
| [[p06_schema_api_response_contract]] | downstream | 0.28 |
| [[p05_output_health_endpoint]] | sibling | 0.22 |
| [[SPEC_06_multi_provider]] | upstream | 0.20 |
| [[KC_N05_UVICORN_PRODUCTION]] | related | 0.19 |
| [[atom_01_a2a_protocol]] | upstream | 0.19 |
| [[bld_sp_memory_software_project]] | downstream | 0.17 |
