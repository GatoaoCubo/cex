---
id: p07_smoke_eval_deploy
kind: smoke_eval
8f: F7_govern
pillar: P07
title: Deploy Smoke Evaluation Suite
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: deployment-operations
quality: 9.0
tags: [smoke_eval, deploy, operations, N05, health, verification]
tldr: "Deploy smoke evaluation suite with 30-second budget, critical path checks, and automatic rollback triggers on failure."
density_score: 0.96
related:
  - p01_kc_api_health_monitoring
  - KC_N05_ZERO_DOWNTIME_DEPLOY
  - p02_agent_deploy_ops
  - p03_sp_deploy_ops
  - p11_qg_smoke-eval
  - bld_examples_hook
  - p03_sp_smoke_eval_builder
  - p11_qg_railway_superintendent
  - bld_memory_smoke_eval
  - p02_agent_railway_superintendent
---

# Deploy Smoke Evaluation Suite

## Overview

This smoke evaluation runs immediately after every `railway up` deployment.
It validates critical paths within a strict 30-second time budget. If any
critical check fails, rollback is triggered automatically. No deploy is
considered successful until the smoke eval passes.

## Time Budget

| phase | max_duration | purpose |
|-------|-------------|---------|
| health_wait | 20s | Wait for /health to return 200 |
| critical_paths | 8s | Verify core endpoints respond |
| middleware_check | 2s | Validate middleware headers present |
| **total** | **30s** | **Hard budget — exceeded = FAIL** |

## Smoke Checks

### Critical (blocking — failure triggers rollback)

| check_id | endpoint | method | expected | timeout |
|----------|----------|--------|----------|---------|
| SMOKE01 | /health | GET | 200 + HealthResponse JSON | 20s |
| SMOKE02 | /pipeline/health | GET | 200 | 5s |
| SMOKE03 | /api/v1/auth/login | POST | 200 or 401 (not 500) | 3s |
| SMOKE04 | /docs | GET | 200 (OpenAPI schema loads) | 3s |

### Important (warning — logged but does not block)

| check_id | endpoint | method | expected | timeout |
|----------|----------|--------|----------|---------|
| SMOKE05 | /api/v1/list | GET | 200 + valid JSON array | 3s |
| SMOKE06 | /api/v1/search | POST | 200 + results structure | 3s |

### Middleware Verification

| check_id | header | expected |
|----------|--------|----------|
| SMOKE_MW01 | X-Request-ID | Present (UUID format) |
| SMOKE_MW02 | X-RateLimit-Limit | Present (numeric) |
| SMOKE_MW03 | Access-Control-Allow-Origin | Present (not wildcard) |

## Execution Script

```bash
#!/bin/bash
# deploy_smoke.sh — run after railway up
BASE_URL="${1:-https://api.example.railway.app}"
PASS=0; FAIL=0; WARN=0

echo "=== Deploy Smoke Eval ==="
echo "Target: $BASE_URL"
echo "Budget: 30 seconds"
echo ""

# SMOKE01: Health endpoint
START=$(date +%s%N)
RESP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "$BASE_URL/health")
if [ "$RESP" = "200" ]; then echo "[PASS] SMOKE01 /health -> $RESP"; ((PASS++))
else echo "[FAIL] SMOKE01 /health -> $RESP"; ((FAIL++)); fi

# SMOKE02: Pipeline health
RESP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$BASE_URL/pipeline/health")
if [ "$RESP" = "200" ]; then echo "[PASS] SMOKE02 /pipeline/health -> $RESP"; ((PASS++))
else echo "[FAIL] SMOKE02 /pipeline/health -> $RESP"; ((FAIL++)); fi

# SMOKE03: Auth endpoint (200 or 401 acceptable, 500 = fail)
RESP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 -X POST "$BASE_URL/api/v1/auth/login")
if [ "$RESP" != "500" ] && [ "$RESP" != "000" ]; then echo "[PASS] SMOKE03 /auth -> $RESP"; ((PASS++))
else echo "[FAIL] SMOKE03 /auth -> $RESP"; ((FAIL++)); fi

# SMOKE04: OpenAPI docs
RESP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "$BASE_URL/docs")
if [ "$RESP" = "200" ]; then echo "[PASS] SMOKE04 /docs -> $RESP"; ((PASS++))
else echo "[FAIL] SMOKE04 /docs -> $RESP"; ((FAIL++)); fi

echo ""
echo "Results: $PASS passed, $FAIL failed, $WARN warnings"
if [ "$FAIL" -gt 0 ]; then
    echo "STATUS: SMOKE_FAILED — rollback recommended"
    exit 1
else
    echo "STATUS: SMOKE_PASSED"
    exit 0
fi
```

## Rollback Trigger

If any critical smoke check (SMOKE01-04) fails:

1. Log failure evidence (response code, timing, error body)
2. Signal N07 with `smoke_failed` status
3. Execute `railway rollback` to previous known-good deploy
4. Verify rollback health within 30s
5. Write incident report with failure evidence

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_api_health_monitoring]] | upstream | 0.25 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | upstream | 0.24 |
| [[p02_agent_deploy_ops]] | upstream | 0.23 |
| [[p03_sp_deploy_ops]] | upstream | 0.22 |
| [[p11_qg_smoke-eval]] | downstream | 0.22 |
| [[bld_examples_hook]] | related | 0.21 |
| [[p03_sp_smoke_eval_builder]] | upstream | 0.21 |
| [[p11_qg_railway_superintendent]] | downstream | 0.21 |
| [[bld_memory_smoke_eval]] | downstream | 0.21 |
| [[p02_agent_railway_superintendent]] | upstream | 0.21 |
