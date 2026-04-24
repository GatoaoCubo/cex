---
id: p08_adr_001_railway_topology
kind: context_doc
8f: F3_inject
pillar: P08
title: "ADR-001: Railway 4-Service Topology"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: architecture-operations
quality: 8.9
tags: [context_doc, architecture, operations, N05, railway, topology, ADR]
tldr: "Architecture decision record for the 4-service Railway topology (api, frontend, dashboard, gateway) and its operational implications."
density_score: 0.96
related:
  - p03_sp_railway_superintendent
  - p05_output_rollback_plan
  - p08_ac_railway_superintendent
  - p02_agent_railway_superintendent
  - p05_output_deploy_checklist
  - p01_kc_railway_platform_deep
  - p03_sp_deploy_ops
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p12_dr_railway_superintendent
  - p02_agent_deploy_ops
---

# ADR-001: Railway 4-Service Topology

## Status

**Accepted** — 2026-04-07

## Context

The CEX backend runs on Railway platform. The deployment topology consists of
4 services that share infrastructure but have independent deploy lifecycles.
Operational decisions about rollback, health monitoring, and blast radius
assessment all depend on this topology.

## Decision

Adopt a 4-service topology on Railway:

| service | role | tech_stack | health_endpoint |
|---------|------|------------|-----------------|
| api | Core backend API | FastAPI + PostgreSQL + uvicorn | /health |
| frontend | Client-facing web app | React + Vite | /index.html |
| dashboard | Internal admin panel | React + Vite | /index.html |
| gateway | API gateway / proxy | Nginx or Caddy | /health |

## Consequences

### Positive

- **Independent scaling**: Each service scales based on its own resource needs
- **Isolated deploys**: API deploy doesn't require frontend redeploy
- **Blast radius containment**: Service failure is isolated to one component
- **Clear ownership**: N05 owns api + gateway, N02/N03 own frontend + dashboard

### Negative

- **Rollback complexity**: Must assess cross-service dependencies before rollback
- **Environment variable duplication**: Some env vars (e.g., API_URL) duplicated across services
- **Health monitoring overhead**: 4 health endpoints to monitor instead of 1
- **Deploy ordering constraints**: API must be healthy before frontend can reach it

### Operational Rules

1. Always assess 4-service blast radius before any rollback
2. API deploy must complete before frontend deploy if API contract changes
3. Gateway configuration changes require full topology health verification
4. Each service has independent railway.toml with service-specific config
5. Database migrations only affect api service — others are stateless

## Alternatives Considered

| alternative | reason_rejected |
|-------------|----------------|
| Monolith (1 service) | No isolation, blast radius = everything |
| Microservices (10+ services) | Over-engineering for current scale |
| Docker Compose | Railway-native is simpler, no container management |
| Kubernetes | Overkill for 4 services, Railway handles infra |

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_railway_superintendent]] | upstream | 0.49 |
| [[p05_output_rollback_plan]] | upstream | 0.43 |
| [[p08_ac_railway_superintendent]] | related | 0.43 |
| [[p02_agent_railway_superintendent]] | upstream | 0.42 |
| [[p05_output_deploy_checklist]] | upstream | 0.40 |
| [[p01_kc_railway_platform_deep]] | upstream | 0.39 |
| [[p03_sp_deploy_ops]] | upstream | 0.37 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | upstream | 0.37 |
| [[p12_dr_railway_superintendent]] | downstream | 0.36 |
| [[p02_agent_deploy_ops]] | upstream | 0.34 |
