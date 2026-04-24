---
id: p01_kc_api_health_monitoring
kind: knowledge_card  
8f: F3_inject
pillar: P01
title: "API Health Monitoring Patterns"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01" 
author: "N04_knowledge"
domain: infrastructure
quality: 9.1
tags: [api_monitoring, health_checks, infrastructure, uptime, observability]
tldr: "API health monitoring ensures service availability through status endpoints, uptime tracking, and dependency validation with structured response formats."
when_to_use: "Implement when building APIs requiring availability monitoring, SLA tracking, or dependency health validation."
keywords: [health_endpoint, uptime, status_check, api_monitoring]
long_tails:
  - How to implement /health endpoint with database connectivity checks
  - API health monitoring patterns for microservices architecture
axioms:
  - ALWAYS include database connectivity in health checks
  - NEVER expose internal system details in public health endpoints
linked_artifacts:
  primary: null
  related: []
density_score: 1.0
data_source: "Infrastructure monitoring best practices"
related:
  - p06_schema_health_response
  - p05_output_health_endpoint
  - p05_output_deploy_checklist
  - p02_agent_railway_superintendent
  - p01_kc_zero_downtime_deploy
  - p08_ac_railway_superintendent
  - p12_wf_auto_health
  - p11_qg_performance
  - p08_adr_001_railway_topology
  - KC_N05_ZERO_DOWNTIME_DEPLOY
---

# API Health Monitoring Patterns

## Quick Reference
```yaml
topic: API Health Monitoring
scope: Service availability validation through structured endpoints
owner: Infrastructure/DevOps Team
criticality: high
```

## Key Concepts
- **HealthResponse**: Structured response containing status, version, timestamp, uptime metrics
- **Status Codes**: HTTP 200 (healthy), 503 (degraded), 500 (unhealthy) with consistent JSON schema
- **Dependency Validation**: Database, cache, external API connectivity checks within health endpoint
- **Uptime Tracking**: Service start time, total uptime duration, request counter metrics
- **Pipeline Health**: Separate `/pipeline/health` for CI/CD and deployment status monitoring
- **Graceful Degradation**: Partial service availability reporting when non-critical dependencies fail

## Strategy Phases
1. **Endpoint Design**: Implement `/health` with HealthResponse schema including status/version/timestamp/uptime
2. **Dependency Integration**: Add database ping, cache connectivity, external service validation to health checks
3. **Monitoring Setup**: Configure uptime tracking, alerting thresholds, and dashboard visualization

## Golden Rules
- Include database connectivity test in every health endpoint implementation
- Return HTTP 503 for degraded state when non-critical dependencies fail
- Always include service version and uptime metrics in health responses
- Implement separate pipeline health endpoint for deployment status monitoring
- Cache dependency check results for 30-60 seconds to prevent health endpoint overload

## Flow
```text
[Request] -> [Health Endpoint] -> [Check Database] -> [Check Cache] -> [Return Status + Metrics]
```

## Comparativo
| Aspect | Basic Health Check | Full Health Check |
|--------|-------------------|-------------------|
| Response Time | <50ms | <200ms |
| Dependencies | None | DB + Cache + APIs |
| Information | Status only | Full metrics |
| Use Case | Load balancer | Monitoring dashboard |

## References
- Related pattern: Circuit breaker implementation for dependency isolation
- Source: https://microservices.io/patterns/observability/health-check-api.html

## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_health_response]] | downstream | 0.50 |
| [[p05_output_health_endpoint]] | downstream | 0.33 |
| [[p05_output_deploy_checklist]] | downstream | 0.26 |
| [[p02_agent_railway_superintendent]] | downstream | 0.25 |
| [[p01_kc_zero_downtime_deploy]] | sibling | 0.24 |
| [[p08_ac_railway_superintendent]] | downstream | 0.24 |
| [[p12_wf_auto_health]] | downstream | 0.23 |
| [[p11_qg_performance]] | downstream | 0.22 |
| [[p08_adr_001_railway_topology]] | downstream | 0.22 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | sibling | 0.21 |
