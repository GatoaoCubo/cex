---
id: p06_schema_health_response
kind: input_schema
8f: F1_constrain
pillar: P06
title: Health Check Response Schema
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.1
tags: [schema, health, response, monitoring, fastapi]
tldr: Schema for HealthResponse JSON validation covering status, version, uptime, database, and cache health indicators.
schema_type: json_response
validation_level: strict
related:
  - p01_kc_api_health_monitoring
  - p05_output_health_endpoint
  - p06_schema_env_contract
  - p03_ch_content_pipeline
  - bld_schema_validation_schema
  - tpl_response_format
  - p06_schema_api_response_contract
  - p03_ch_kc_to_notebooklm
  - p04_function_def_NAME
  - bld_schema_model_registry
---

# Health Check Response Schema

## Purpose

Validates /health endpoint JSON responses for Railway FastAPI applications
to ensure consistent monitoring and observability data structure.

## Schema Definition

```yaml
health_response:
  required: true
  properties:
    status:
      type: string
      enum: ["healthy", "degraded", "unhealthy"]
      required: true
    version:
      type: string
      pattern: "^\\d+\\.\\d+\\.\\d+"
      required: true
    timestamp:
      type: string
      format: iso8601
      required: true
    uptime_seconds:
      type: integer
      minimum: 0
      required: true
    environment:
      type: string
      enum: ["development", "staging", "production"]
      required: true
    database:
      type: object
      required: true
      properties:
        status: {type: string, enum: ["connected", "disconnected", "error"]}
        pool_size: {type: integer, minimum: 0}
        active_connections: {type: integer, minimum: 0}
        ssl_enabled: {type: boolean}
    cache:
      type: object
      required: false
      properties:
        status: {type: string, enum: ["connected", "disconnected", "fallback"]}
        hit_rate: {type: number, minimum: 0, maximum: 1}
        memory_usage_mb: {type: number, minimum: 0}
```

## Validation Rules

- status must indicate current service health level
- version must follow semantic versioning format
- uptime_seconds tracks service restart cycles
- database status required for PostgreSQL health
- cache status optional for Redis/fallback scenarios

## Example Valid Response

```json
{
  "status": "healthy",
  "version": "1.2.3",
  "timestamp": "2026-04-01T12:00:00Z",
  "uptime_seconds": 3600,
  "environment": "production",
  "database": {
    "status": "connected",
    "pool_size": 20,
    "active_connections": 5,
    "ssl_enabled": true
  },
  "cache": {
    "status": "connected", 
    "hit_rate": 0.85,
    "memory_usage_mb": 128
  }
}
```


## Health Check Implementation

Health check endpoints follow a standardized response format:

- **Response time**: health endpoint must respond within 500ms under normal load
- **Dependency cascading**: check reports status of each downstream dependency individually
- **Degraded state**: partial failures reported as DEGRADED, not DOWN, with detail
- **History retention**: last 100 health check results stored for trend analysis

### Endpoint Specification

```yaml
# Health check response schema
health:
  status: UP | DEGRADED | DOWN
  timestamp: ISO8601
  version: semver
  checks:
    - name: database
      status: UP
      latency_ms: 12
    - name: cache
      status: UP
      latency_ms: 3
  uptime_seconds: 86400
```

| Status | Meaning | Alert Level |
|--------|---------|-------------|
| UP | All checks pass | None |
| DEGRADED | Non-critical check failed | Warning |
| DOWN | Critical check failed | Critical |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_api_health_monitoring]] | upstream | 0.39 |
| [[p05_output_health_endpoint]] | upstream | 0.38 |
| [[p06_schema_env_contract]] | sibling | 0.31 |
| [[p03_ch_content_pipeline]] | upstream | 0.27 |
| [[bld_schema_validation_schema]] | related | 0.24 |
| [[tpl_response_format]] | upstream | 0.24 |
| [[p06_schema_api_response_contract]] | sibling | 0.23 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.23 |
| [[p04_function_def_NAME]] | upstream | 0.22 |
| [[bld_schema_model_registry]] | related | 0.22 |
