---

```markdown
quality: 9.0
title: "Middleware Stack"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for knowledge, demonstrating ideal structure and common pitfalls."
domain: "knowledge"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
id: p01_kc_middleware_stack
kind: knowledge_card
pillar: P01
---

# FastAPI 8-Layer Ordered Middleware Stack

## Key Concepts

**Middleware Execution Order**: FastAPI middleware executes in LIFO (Last In, First Out) order for requests and FIFO (First In, First Out) for responses. The order you add middleware matters critically.

**8-Layer Production Stack**: A battle-tested middleware ordering for production FastAPI applications that handles security, rate limiting, and operational concerns in the correct sequence.

## Patterns

### 1. CORS (Cross-Origin Resource Sharing)
1. **Position**: Outermost layer
2. **Purpose**: Handle preflight OPTIONS requests before any authentication
3. **Pattern**: Must execute first to prevent CORS failures on authenticated endpoints
```python
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
```

### 2. TenantRateLimit
1. **Position**: Second layer
2. **Purpose**: Tenant-level rate limiting before individual authentication
3. **Pattern**: Prevents abuse at the organization/tenant level
```python
app.add_middleware(TenantRateLimitMiddleware, rate_limit="1000/hour")
```

### 3. APIKey Authentication
1. **Position**: Third layer  
2. **Purpose**: Extract and validate API keys from headers/query params
3. **Pattern**: Sets user context for downstream middleware
```python
app.add_middleware(APIKeyMiddleware, header_name="X-API-Key")
```

### 4. RLS (Row Level Security)
1. **Position**: Fourth layer
2. **Purpose**: Set database security context based on authenticated user
3. **Pattern**: Configures database session for multi-tenant data isolation
```python
app.add_middleware(RLSMiddleware, tenant_header="X-Tenant-ID")
```

### 5. EndpointRateLimit
1. **Position**: Fifth layer
2. **Purpose**: Per-user, per-endpoint rate limiting
3. **Pattern**: Fine-grained rate limiting after authentication context is established
```python
app.add_middleware(EndpointRateLimitMiddleware, rate_limit="100/minute")
```

### 6. BodySize Validation
1. **Position**: Sixth layer
2. **Purpose**: Reject oversized request bodies early
3. **Pattern**: Prevents memory exhaustion from large payloads
```python
app.add_middleware(BodySizeMiddleware, max_size=10 * 1024 * 1024)  # 10MB
```

### 7. Exception Handling
1. **Position**: Seventh layer
2. **Purpose**: Catch and format all unhandled exceptions
3. **Pattern**: Provides consistent error responses and logging
```python
app.add_middleware(ExceptionMiddleware, include_traceback=False)
```

### 8. Request ID
1. **Position**: Innermost layer
2. **Purpose**: Generate unique request IDs for tracing and logging
3. **Pattern**: Injects correlation IDs for observability
```python
app.add_middleware(RequestIDMiddleware, header_name="X-Request-ID")
```

## Implementation Order

```python
from fastapi import FastAPI
app = FastAPI()

# Add in reverse order of desired execution
app.add_middleware(RequestIDMiddleware)           # 8 (innermost)
app.add_middleware(ExceptionMiddleware)          # 7
app.add_middleware(BodySizeMiddleware)           # 6  
app.add_middleware(EndpointRateLimitMiddleware)  # 5
app.add_middleware(RLSMiddleware)                # 4
app.add_middleware(APIKeyMiddleware)             # 3
app.add_middleware(TenantRateLimitMiddleware)    # 2
app.add_middleware(CORSMiddleware)               # 1 (outermost)
```

## Execution Flow

**Request Path**: CORS → TenantRate → APIKey → RLS → EndpointRate → BodySize → Exceptions → RequestID → Route Handler

**Response Path**: RequestID → Exceptions → BodySize → EndpointRate → RLS → APIKey → TenantRate → CORS → Client

## Critical Dependencies

1. **CORS before Auth**: Prevents CORS failures on authenticated OPTIONS requests
2. **TenantRate before APIKey**: Allows tenant-level blocking before user lookup
3. **APIKey before RLS**: User context required for database security policies  
4. **RLS before EndpointRate**: Database context needed for user-specific rate limits
5. **BodySize before Exceptions**: Reject large payloads before application logic
6. **Exceptions before RequestID**: Ensure request IDs appear in error responses
```

This knowledge card covers the FastAPI 8-layer middleware stack with the proper YAML frontmatter and structured content focusing on the key concepts and implementation patterns for each middleware layer.

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | knowledge |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
