---
id: p12_dr_railway_superintendent
kind: dispatch_rule
pillar: P12
version: 4.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: null
tags: [dispatch_rule, railway, superintendent, deploy, fastapi, postgresql]
tldr: Route Railway platform tasks to N05 Railway Superintendent when the answer depends on Railway deployment, FastAPI health, PostgreSQL operations, or 4-service topology management.
scope: railway-backend-operations
keywords: [deploy, railway, backend, api, production, staging, database, migration, rollback, health, uvicorn, nixpacks, infra, scale, postgres, middleware, cors, rate-limit, fastapi, postgresql, env, api-lifecycle, infrastructure, superintendent, toml, pool, asyncpg, startup, monitoring]
agent_node: railway_superintendent
model: opus
model_fallback: sonnet
cli: claude
mcps: [postgresql]
receives_from: [N03, N07, N02]
handoff_to: [N03]
priority: 9
confidence_threshold: 0.85
fallback: operations_nucleus
routing_strategy: railway_platform_requirement
---

# Railway Backend Superintendent Dispatch Rule

## Purpose

Dispatch to N05 Railway Superintendent when the user needs Railway platform 
deployment, FastAPI backend lifecycle management, PostgreSQL operations, 
or 4-service topology coordination.

## Route To Railway Superintendent When

- The task involves Railway deployment: railway up, railway logs, railway rollback
- FastAPI health monitoring: /health endpoints, HealthResponse JSON, startup sequence
- PostgreSQL operations: asyncpg pools, migrations, SSL connections, database health
- Environment management: 63 variable validation, DATABASE_URL, API key configuration
- 4-service coordination: api, frontend, dashboard, gateway deployment orchestration
- Nixpacks builds, uvicorn production servers, middleware stack validation

## Strong Positive Signals

- "railway deploy"
- "fastapi health check"  
- "postgresql migration"
- "rollback 4 services"
- "env validation"
- "nixpacks build"
- "uvicorn startup"
- "middleware verification"

## Do Not Route To Railway Superintendent When

- Frontend React/Vite builds (route to N02)
- Non-Railway cloud platforms: AWS, GCP, Azure (route to generic N05)
- Marketing copy or business strategy (route to N02/N06)

## Mixed-Intent Policy

If the request includes both Railway backend and other platforms:

- Railway Superintendent owns Railway/FastAPI/PostgreSQL portions
- Generic N05 is fallback for non-Railway infrastructure

## Decision Rule

If answering correctly requires Railway platform knowledge, FastAPI backend 
lifecycle, or PostgreSQL database operations, dispatch to Railway Superintendent.
