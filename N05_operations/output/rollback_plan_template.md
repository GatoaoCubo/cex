---
id: p05_output_rollback_plan
kind: output_validator
pillar: P05
title: Railway Rollback Plan Template
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.0
tags: [output, rollback, plan, railway, 4-service, emergency]
tldr: Rollback plan template for Railway 4-service topology with blast radius assessment and recovery coordination.
output_type: rollback_plan
format: markdown
---

# Railway Rollback Plan

## Incident Details

**Date/Time:** _______________
**Environment:** _______________
**Triggered by:** _______________
**Impact Level:** [ ] Minor [ ] Major [ ] Critical
**Estimated Downtime:** _______________

## 4-Service Blast Radius Assessment

### API Service (FastAPI Backend)
- **Status:** [ ] Affected [ ] Stable [ ] Unknown
- **Issues:** _______________
- **Dependencies:** Database, Cache, Auth
- **Rollback Required:** [ ] Yes [ ] No

### Frontend Service (React/Vite)
- **Status:** [ ] Affected [ ] Stable [ ] Unknown  
- **Issues:** _______________
- **Dependencies:** API endpoints, CDN
- **Rollback Required:** [ ] Yes [ ] No

### Dashboard Service (Admin)
- **Status:** [ ] Affected [ ] Stable [ ] Unknown
- **Issues:** _______________
- **Dependencies:** API auth, user management
- **Rollback Required:** [ ] Yes [ ] No

### Gateway Service (Proxy/Load Balancer)
- **Status:** [ ] Affected [ ] Stable [ ] Unknown
- **Issues:** _______________
- **Dependencies:** Routing rules, SSL certs
- **Rollback Required:** [ ] Yes [ ] No

## Rollback Execution Plan

### Step 1: Stop Traffic (if critical)
```bash
# Temporarily block traffic to affected services
railway env set MAINTENANCE_MODE=true
```

### Step 2: Database Rollback (if needed)
```bash
# Check migration status
railway connect postgres
# Execute rollback migration if required
# CRITICAL: Test in staging first
```

### Step 3: Service Rollbacks
```bash
# API service rollback
railway rollback --service api --to-deployment [DEPLOYMENT_ID]

# Frontend rollback (if needed)  
railway rollback --service frontend --to-deployment [DEPLOYMENT_ID]

# Dashboard rollback (if needed)
railway rollback --service dashboard --to-deployment [DEPLOYMENT_ID]

# Gateway rollback (if needed)
railway rollback --service gateway --to-deployment [DEPLOYMENT_ID]
```

### Step 4: Health Verification
```bash
# Verify health endpoints
curl -f https://api.domain.com/health
curl -f https://dashboard.domain.com/health

# Check service communication
# Verify authentication flows
# Confirm database connectivity
```

### Step 5: Traffic Restoration
```bash
# Remove maintenance mode
railway env set MAINTENANCE_MODE=false

# Monitor logs for errors
railway logs --service api --tail
```

## Validation Checklist

- [ ] **Health Endpoints Responding**
  - API /health returns 200
  - Database connections active
  - Cache operational (or fallback)

- [ ] **Service Communication**
  - Frontend → API calls working
  - Dashboard → API authentication
  - Gateway → Service routing

- [ ] **Data Integrity**
  - Database queries successful
  - No data corruption detected
  - User sessions preserved

- [ ] **Performance Metrics**
  - Response times within normal range
  - Error rates below threshold
  - Resource utilization stable

## Recovery Time Objectives

- **Critical Path Recovery:** 5 minutes
- **Full Service Recovery:** 15 minutes
- **Performance Baseline:** 30 minutes
- **Post-Incident Review:** 24 hours

## Communication Plan

**Internal Notifications:**
- [ ] Railway superintendent notified
- [ ] Database team alerted
- [ ] Frontend team coordinated
- [ ] Stakeholders informed

**External Communications:**
- [ ] Status page updated (if applicable)
- [ ] Customer notifications (if needed)
- [ ] Support team briefed

## Post-Rollback Actions

- [ ] Incident report created
- [ ] Root cause analysis scheduled
- [ ] Monitoring alert review
- [ ] Process improvement identified

**Rollback executed by:** _______________
**Completion time:** _______________
**Services restored:** _______________
**Follow-up required:** _______________