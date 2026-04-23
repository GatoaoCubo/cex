---
id: p06_schema_api_response_contract
kind: input_schema
pillar: P06
title: "API Response Contract"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.1
tags: [schema, api, response, contract, fastapi]
tldr: "Standard API response format — success/error envelopes, required headers, status codes."
density_score: 1.0
related:
  - tpl_response_format
  - p06_schema_health_response
  - p06_schema_env_contract
  - p11_qg_railway_superintendent
  - kc_api_reference
  - kc_test_ollama_wrapper
  - p05_output_middleware_stack
  - p01_kc_llm_output_parsing_validation
  - p01_kc_fastapi_patterns
  - p09_rate_limit_config
---

# API Response Contract

## Schema Purpose
Every FastAPI endpoint MUST return responses conforming to this contract.
Ensures consistent client-side parsing and error handling.

---

## Success Response Envelope

```json
{
  "status": "success",
  "data": { },
  "timestamp": "2026-04-01T12:00:00.000Z",
  "request_id": "req_abc123def456"
}
```

### Rules
- `status`: always `"success"` for 2xx responses
- `data`: the actual payload (object, array, or null)
- `timestamp`: ISO 8601 UTC with milliseconds
- `request_id`: matches `X-Request-Id` header

## Error Response Envelope

```json
{
  "detail": "Human-readable error message",
  "status_code": 422,
  "errors": [
    { "field": "email", "message": "Invalid email format" }
  ],
  "docs": "/docs",
  "support": null,
  "request_id": "req_abc123def456"
}
```

### Rules by Status Code

| Code | When | `detail` | `support` |
|------|------|----------|-----------|
| 400 | Bad request / validation | field-specific errors | null |
| 401 | Missing or invalid auth | "Authentication required" | null |
| 403 | Insufficient permissions | "Insufficient permissions" | null |
| 404 | Resource not found | "Resource not found" | `docs: "/docs"` |
| 409 | Conflict / duplicate | "Resource already exists" | null |
| 422 | Validation error | Pydantic error detail | null |
| 429 | Rate limited | "Rate limit exceeded" | retry-after header |
| 500 | Internal error | "Internal server error" | `support: "email"` |
| 503 | Service degraded | "Service temporarily unavailable" | null |

## Required Response Headers

```yaml
headers:
  X-Request-Id:
    format: "req_{uuid4_short}"
    source: "RequestIdTiming middleware"
    required: true

  X-Process-Time:
    format: "float seconds (e.g., 0.042)"
    source: "RequestIdTiming middleware"
    required: true

  X-RateLimit-Limit:
    format: "integer (requests per minute)"
    values: { free: 60, pro: 120, business: 300 }
    required: true

  X-RateLimit-Remaining:
    format: "integer"
    required: true

  X-RateLimit-Reset:
    format: "unix timestamp (seconds)"
    required: true

  Content-Type:
    value: "application/json; charset=utf-8"
    required: true
```

## Pagination (when applicable)

```json
{
  "status": "success",
  "data": [],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150,
    "total_pages": 8,
    "has_next": true,
    "has_prev": false
  },
  "timestamp": "2026-04-01T12:00:00.000Z",
  "request_id": "req_abc123"
}
```

## Validation

```yaml
validation:
  every_2xx_has: [status, data, timestamp, request_id]
  every_4xx_5xx_has: [detail, status_code, request_id]
  every_response_has_headers: [X-Request-Id, X-Process-Time, Content-Type]
  rate_limited_has_headers: [X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset]
  no_plain_text_errors: true
  no_html_error_pages: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_response_format]] | upstream | 0.28 |
| [[p06_schema_health_response]] | sibling | 0.27 |
| [[p06_schema_env_contract]] | sibling | 0.25 |
| [[p11_qg_railway_superintendent]] | downstream | 0.24 |
| [[kc_api_reference]] | upstream | 0.22 |
| [[kc_test_ollama_wrapper]] | related | 0.22 |
| [[p05_output_middleware_stack]] | upstream | 0.21 |
| [[p01_kc_llm_output_parsing_validation]] | upstream | 0.21 |
| [[p01_kc_fastapi_patterns]] | upstream | 0.21 |
| [[p09_rate_limit_config]] | downstream | 0.20 |
