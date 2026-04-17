---
id: p01_kc_zero_downtime_deploy
kind: knowledge_card
type: infrastructure
pillar: P01
title: "Zero-Downtime Deployment"
version: 1.0.0
created: 2026-03-30
author: n05_operations
domain: infrastructure
quality: 9.0
tags: [zero-downtime, deployment, blue-green, rolling, health-check]
tldr: "Zero-downtime via health checks + graceful shutdown + rolling deploys. 30-30-60 startup pattern: 30s warmup, 30s health probe, 60s traffic ramp."
when_to_use: "When deploying production services that must not drop requests"
keywords: [zero-downtime, rolling-deploy, blue-green, health-check, graceful-shutdown]
density_score: 0.93
---

# Zero-Downtime Deployment

## Strategies

| Strategy | Complexity | Rollback Speed | Resource Cost |
|----------|-----------|----------------|---------------|
| Rolling update | Low | Medium (redeploy) | 1x + 1 instance | 
| Blue-green | Medium | Instant (swap) | 2x |
| Canary | High | Fast (route shift) | 1x + small % |

## 30-30-60 Startup Pattern

| Phase | Duration | Action |
|-------|----------|--------|
| Warmup | 30s | App starts, loads config, connects DB |
| Health probe | 30s | Readiness endpoint returns 200 |
| Traffic ramp | 60s | Gradually shift traffic from old → new |

## Health Endpoint Contract
```json
GET /health → 200 { "status": "ok", "uptime": 123, "version": "1.2.3" }
GET /health → 503 { "status": "starting" }  // during warmup
```

## Graceful Shutdown
1. Receive SIGTERM
2. Stop accepting new connections
3. Drain in-flight requests (30s timeout)
4. Close DB connections
5. Exit 0

## Anti-Pattern
Kill -9 on deploy = dropped requests. Always handle SIGTERM gracefully.
