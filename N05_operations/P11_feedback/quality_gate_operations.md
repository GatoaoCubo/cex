---
id: p11_qg_railway_superintendent
kind: quality_gate
pillar: P11
title: "Gate: Railway Backend Superintendent"
version: 4.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.1
tags: [quality_gate, railway, superintendent, deploy, fastapi, postgresql]
tldr: Railway deployment validation gate covering deploy smoke tests, rollback planning, migration safety, environment contracts, health monitoring, and middleware integrity.
density_score: 1.0
related:
  - p11_qg_security
  - p11_qg_performance
  - p11_qg_artifact
  - p05_output_deploy_checklist
  - p03_sp_deploy_ops
  - p02_agent_deploy_ops
  - p02_agent_railway_superintendent
  - p03_sp_railway_superintendent
  - p06_schema_health_response
  - p06_schema_api_response_contract
---

## Definition

| Property | Value |
|----------|-------|
| Metric | railway_deployment_safety_score |
| Threshold | 0.90 |
| Operator | >= |
| Scope | All Railway deployments, health checks, PostgreSQL operations, and 4-service topology changes |

## Railway Deployment Gates

| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| G01 | Deploy smoke test passes within 30 seconds | 30s | true |
| G02 | Rollback plan documented for 4 services (api/frontend/dashboard/gateway) | 100% | true |
| G03 | Database migrations tested for backward compatibility | 100% | true |
| G04 | Environment contract validated (63 variables present) | 100% | true |
| G05 | Health endpoints return 200 with HealthResponse JSON | 100% | true |
| G06 | Middleware stack integrity verified (8 layers ordered correctly) | 100% | true |
| G07 | Startup sequence completes all 14 checks (pass or fallback) | 14/14 | true |
| G08 | API response latency p95 under threshold | < 500ms | false |
| G09 | CORS origins whitelist includes all 4 production domains | 4 origins | true |
| G10 | Rate limiting active with X-RateLimit headers in responses | headers present | true |

## Validation Criteria

- **Deploy Smoke (G01)**: `/health` endpoint responds 200 within 30s of `railway up`
- **Rollback Plan (G02)**: Blast radius assessment + recovery steps for each affected service
- **Migration Safety (G03)**: SQL migrations tested with rollback compatibility
- **Environment Contract (G04)**: All 63 required variables (DATABASE_URL, API keys, pool settings) validated
- **Health Full (G05)**: HealthResponse includes status, version, uptime, database{}, cache{}
- **Middleware Intact (G06)**: CORS→TenantRateLimit→APIKey→RLS→EndpointLimit→BodySize→Exceptions→RequestID order confirmed
- **Startup Clean (G07)**: All 14 lifespan checks pass or gracefully fallback; no silent failures
- **API Latency (G08)**: p95 response time < 500ms under normal load (soft gate, non-blocking)
- **CORS Valid (G09)**: localhost, *.railway.app, *.codexa.com.br, staging origin whitelisted
- **Rate Limit Active (G10)**: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset headers present on all responses
| H02 | `kind` matches the artifact file type | 100% | true |
| H03 | `quality` is `null` in source artifact frontmatter | 100% | true |
| H04 | Output is domain-specific to operations/devops, not generic filler | 100% | true |
| H05 | Findings or fixes are tied to concrete evidence, or the evidence gap is explicitly stated | 100% | true |
| H06 | Validation commands or review basis are reproducible in repo context | 100% | true |
| H07 | Release-affecting output includes rollback or explains why rollback is not relevant | 100% | true |
| H08 | Deploy, CI, or infra guidance does not ignore environment/config assumptions | 100% | true |
| H09 | Output does not claim completion while known failing signals remain unaddressed | 100% | true |

## Soft Gates

| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| S01 | Accuracy of diagnosis or review findings | 0.10 | 0.24 |
| S02 | Validation depth on affected path | 0.10 | 0.24 |
| S03 | CI/CD and deploy safety awareness | 0.10 | 0.18 |
| S04 | Remediation precision and blast-radius control | 0.10 | 0.14 |
| S05 | Rollback and observability quality | 0.10 | 0.10 |
| S06 | Clarity and handoff utility | 0.10 | 0.10 |

## Scoring Formula

`operational_readiness_score = (S01 * 0.24) + (S02 * 0.24) + (S03 * 0.18) + (S04 * 0.14) + (S05 * 0.10) + (S06 * 0.10)`

Pass condition:

- all hard gates pass
- `operational_readiness_score >= 0.88`

## Bypass Policy

- **Allowed by**: orchestrator or repository owner
- **Valid only for**: time-critical incident response or degraded validation infrastructure
- **Required record**: missing evidence, blast radius, rollback path, timestamp, approver

## Audit Trail

Record:

- artifact id and version
- evaluator
- commands, diffs, tests, or logs used as evidence
- pass/fail by hard gate
- soft-gate subscores
- final score
- bypass data if used

Retention: 24 months minimum or active repo lifetime, whichever is longer.

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_security]] | sibling | 0.37 |
| [[p11_qg_performance]] | sibling | 0.35 |
| [[p11_qg_artifact]] | sibling | 0.33 |
| [[p05_output_deploy_checklist]] | upstream | 0.31 |
| [[p03_sp_deploy_ops]] | upstream | 0.30 |
| [[p02_agent_deploy_ops]] | upstream | 0.29 |
| [[p02_agent_railway_superintendent]] | upstream | 0.29 |
| [[p03_sp_railway_superintendent]] | upstream | 0.28 |
| [[p06_schema_health_response]] | upstream | 0.28 |
| [[p06_schema_api_response_contract]] | upstream | 0.27 |
