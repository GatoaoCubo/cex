---
id: p05_output_deploy_checklist
kind: output_validator
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

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | operations | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Operations artifacts follow CEX 8F pipeline from intent to publication
- Quality gates enforce minimum 8.0 threshold for all published artifacts
- Cross-nucleus references use explicit id-based linking, not path-based
- Version tracking enables rollback to any previous artifact state

