---
id: p06_schema_middleware_stack_contract
kind: input_schema
8f: F1_constrain
pillar: P06
title: "Middleware Stack Contract — 8 Layers"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.0
tags: [schema, middleware, fastapi, cors, auth, rate-limit]
tldr: "8-layer ordered middleware stack — CORS outermost, request_id innermost. Order is law."
density_score: 0.95
related:
  - p05_output_middleware_stack
  - p01_kc_fastapi_patterns
  - spec_n05_part2
  - p06_schema_api_response_contract
  - bld_sp_architecture_software_project
  - p04_ex_software_project_api_service
  - bld_sp_memory_software_project
  - p11_qg_security
  - kc_api_reference
  - bld_quality_gate_supabase_data_layer
---

# Middleware Stack Contract — 8 Layers

## Schema Purpose
Defines the exact middleware order for all FastAPI services.
Order is critical: outer middleware runs first on request, last on response.

---

## Stack (Outermost → Innermost)

```
Request →
  [1] CORS                    ← outermost (must handle preflight first)
  [2] TenantRateLimit         ← per-tenant throttle before auth
  [3] APIKeyAuth              ← JWT + API key validation
  [4] RLS                     ← Row-Level Security (X-User-ID injection)
  [5] EndpointRateLimit       ← per-endpoint LLM ops throttle
  [6] BodySizeLimit           ← reject oversized payloads
  [7] CatchAllExceptions      ← convert exceptions to JSON
  [8] RequestIdTiming         ← X-Request-Id + X-Process-Time
→ Route Handler
```

## Layer Specifications

### Layer 1: CORS (Outermost)

```yaml
cors:
  position: 1
  reason: "Must handle OPTIONS preflight before any auth check"
  config:
    allow_origins_regex: 'https?://(localhost|.*\.railway\.app|.*\.codexa\.com\.br)'
    allow_methods: ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
    allow_headers: ["*"]
    allow_credentials: true
    max_age: 600
```

### Layer 2: TenantRateLimit

```yaml
tenant_rate_limit:
  position: 2
  reason: "Throttle before expensive auth checks"
  tiers:
    free: { requests_per_minute: 60 }
    pro: { requests_per_minute: 120 }
    business: { requests_per_minute: 300 }
  key: "X-API-Key or IP fallback"
  response_429: { detail: "Rate limit exceeded", retry_after: "seconds" }
```

### Layer 3: APIKeyAuth

```yaml
api_key_auth:
  position: 3
  reason: "Authenticate before RLS can inject user context"
  methods:
    - jwt_bearer: "Authorization: Bearer <token>"
    - api_key: "X-API-Key: <key>"
  skip_paths: ["/health", "/docs", "/openapi.json", "/redoc"]
  response_401: { detail: "Authentication required" }
```

### Layer 4: RLS (Row-Level Security)

```yaml
rls:
  position: 4
  reason: "Needs authenticated user from Layer 3"
  action: "Inject X-User-ID into request state"
  db_behavior: "SET app.current_user_id = <user_id> per connection"
  depends_on: "Layer 3 (APIKeyAuth)"
```

### Layer 5: EndpointRateLimit

```yaml
endpoint_rate_limit:
  position: 5
  reason: "Protect expensive LLM endpoints after auth"
  targets:
    - path_pattern: "/pipeline/*"
      limit: 10_per_minute
    - path_pattern: "/pesquisa/*"
      limit: 20_per_minute
    - path_pattern: "/anuncio/*"
      limit: 30_per_minute
  default: null  # no per-endpoint limit
```

### Layer 6: BodySizeLimit

```yaml
body_size_limit:
  position: 6
  reason: "Reject oversized payloads before processing"
  limits:
    default: "5MB"
    upload_endpoints: "10MB"
  response_413: { detail: "Request body too large" }
```

### Layer 7: CatchAllExceptions

```yaml
catch_all:
  position: 7
  reason: "Must be inside CORS (so error responses have CORS headers)"
  behavior: "Convert any unhandled exception to JSON 500 response"
  log: "logger.exception() with request_id"
  response_500: { detail: "Internal server error", support: "support@codexa.com.br" }
```

### Layer 8: RequestIdTiming (Innermost)

```yaml
request_id_timing:
  position: 8
  reason: "Innermost to measure actual handler time"
  request_id:
    format: "req_{uuid4_short}"
    header: "X-Request-Id"
    propagate: "attach to request.state"
  timing:
    header: "X-Process-Time"
    format: "float seconds"
    start: "before handler"
    end: "after handler"
```

## Order Rules (Invariants)

```yaml
invariants:
  - "CORS is always position 1 (outermost)"
  - "Auth (Layer 3) runs before RLS (Layer 4)"
  - "CatchAll (Layer 7) is inside CORS so errors get CORS headers"
  - "RequestIdTiming (Layer 8) is innermost for accurate timing"
  - "TenantRateLimit (Layer 2) runs before Auth to protect from brute force"
```

## FastAPI Registration Order

```python
# IMPORTANT: add_middleware is LIFO — last added = outermost
# So add in REVERSE order (8 → 1)
app.add_middleware(RequestIdTimingMiddleware)         # 8 - innermost
app.add_middleware(CatchAllExceptionsMiddleware)      # 7
app.add_middleware(BodySizeLimitMiddleware)            # 6
app.add_middleware(EndpointRateLimitMiddleware)        # 5
app.add_middleware(RLSMiddleware)                      # 4
app.add_middleware(APIKeyAuthMiddleware)               # 3
app.add_middleware(TenantRateLimitMiddleware)          # 2
app.add_middleware(CORSMiddleware, **cors_config)      # 1 - outermost
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_middleware_stack]] | upstream | 0.36 |
| [[p01_kc_fastapi_patterns]] | upstream | 0.33 |
| [[spec_n05_part2]] | related | 0.22 |
| [[p06_schema_api_response_contract]] | sibling | 0.22 |
| [[bld_sp_architecture_software_project]] | downstream | 0.21 |
| [[p04_ex_software_project_api_service]] | upstream | 0.20 |
| [[bld_sp_memory_software_project]] | downstream | 0.19 |
| [[p11_qg_security]] | downstream | 0.18 |
| [[kc_api_reference]] | upstream | 0.18 |
| [[bld_quality_gate_supabase_data_layer]] | upstream | 0.16 |
