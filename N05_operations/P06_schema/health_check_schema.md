---
id: p06_schema_health_response
kind: input_schema
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

