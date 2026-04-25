---
id: p05_output_deploy_checklist
kind: output_validator
8f: F6_produce
pillar: P05
title: Railway Deploy Checklist Template
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.0
tags: [output, deploy, checklist, railway, fastapi, postgresql]
tldr: Deploy validation checklist template for Railway FastAPI backend deployments with health monitoring and rollback readiness.
output_type: checklist
format: markdown
related:
  - p05_output_rollback_plan
  - p02_agent_railway_superintendent
  - p03_sp_railway_superintendent
  - p08_ac_railway_superintendent
  - p12_dr_railway_superintendent
  - p02_agent_deploy_ops
  - p03_sp_deploy_ops
  - p01_kc_railway_platform_deep
  - p01_kc_deploy_paas
  - spec_n05_railway_superintendent
---

# Railway Deploy Checklist

## Pre-Deploy Validation

- [ ] **Railway TOML Validated**
  - buildCommand configured for nixpacks
  - startCommand targets uvicorn FastAPI app
  - healthcheckPath set to "/health"
  - healthcheckTimeout ≤ 30 seconds

- [ ] **Environment Contract (63 variables)**
  - DATABASE_URL (PostgreSQL with SSL)
  - ANTHROPIC_API_KEY + OPENAI_API_KEY
  - DB_POOL_MIN=3, DB_POOL_MAX=20
  - ENV set to correct environment
  - All rate limit tiers configured

- [ ] **PostgreSQL Health**
  - asyncpg connection pool tested
  - SSL negotiation successful
  - Migration compatibility verified
  - Backup/restore tested if schema changes

## Deploy Execution

- [ ] **Railway Deploy**
  - `railway up` executed successfully
  - Nixpacks build completed without errors
  - Uvicorn started with correct workers
  - Service healthy in Railway dashboard

- [ ] **Health Check (30s window)**
  - `/health` endpoint returns 200 OK
  - HealthResponse JSON structure valid
  - Database status "connected"
  - Cache status confirmed
  - Uptime counter active

## Post-Deploy Verification

- [ ] **4-Service Topology Check**
  - API service (FastAPI backend) ✓
  - Frontend service communication ✓
  - Dashboard service access ✓
  - Gateway routing intact ✓

- [ ] **Middleware Stack Integrity**
  - CORS headers present
  - Rate limiting active (per tier)
  - Authentication middleware responding
  - Request ID correlation working

- [ ] **Monitoring & Observability**
  - Railway logs streaming
  - PostgreSQL connection metrics
  - API response time baselines
  - Error rate within thresholds

## Rollback Readiness

- [ ] **Rollback Plan Documented**
  - Previous version ID recorded
  - Database migration rollback steps
  - 4-service coordination plan
  - Estimated rollback time: ___

- [ ] **Emergency Contacts**
  - Railway superintendent: available
  - Database admin: notified
  - Frontend team: coordinated
  - Monitoring alerts: configured

## Sign-Off

**Deploy completed by:** _______________
**Date/Time:** _______________  
**Environment:** _______________
**Health status:** _______________
**Rollback plan:** _______________

**Notes/Issues:**
_______________________________________________

## Rollback Triggers

| Condition | Action | SLA |
|-----------|--------|-----|
| Health endpoint returns non-200 within 30s of deploy | auto-rollback | 60s |
| p95 latency exceeds 2x baseline | alert + manual decision | 5min |
| Error rate > 5% for 2 consecutive minutes | auto-rollback | 120s |
| Database migration failure | halt deploy, rollback migration | immediate |
| Startup sequence < 14/14 checks pass | halt, investigate | immediate |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_rollback_plan]] | sibling | 0.56 |
| [[p02_agent_railway_superintendent]] | upstream | 0.55 |
| [[p03_sp_railway_superintendent]] | upstream | 0.52 |
| [[p08_ac_railway_superintendent]] | downstream | 0.50 |
| [[p12_dr_railway_superintendent]] | downstream | 0.47 |
| [[p02_agent_deploy_ops]] | upstream | 0.46 |
| [[p03_sp_deploy_ops]] | upstream | 0.46 |
| [[p01_kc_railway_platform_deep]] | upstream | 0.44 |
| [[p01_kc_deploy_paas]] | upstream | 0.43 |
| [[spec_n05_railway_superintendent]] | downstream | 0.43 |
