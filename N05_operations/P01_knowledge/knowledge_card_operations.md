---
id: p01_kc_railway_superintendent
kind: knowledge_card
pillar: P01
title: Railway Backend Superintendent Knowledge Card
version: 4.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.1
tags: [knowledge_card, railway, superintendent, fastapi, postgresql, deploy]
tldr: Railway-native doctrine for FastAPI lifecycle management on Railway platform with PostgreSQL, health monitoring, and 4-service topology awareness.
when_to_use: When the request requires Railway deployment, FastAPI health checks, PostgreSQL operations, or infrastructure management on Railway platform.
keywords: [railway, superintendent, fastapi, postgresql, deploy, health, rollback, nixpacks, uvicorn]
long_tails:
  - How should Railway deployments validate health endpoints before completion?
  - What 4-service coordination is required for safe rollbacks?
  - How should PostgreSQL migrations maintain backward compatibility?
axioms:
  - Deploy only with railway.toml validation and health endpoints.
  - 4-service blast radius assessment required for rollbacks.
  - PostgreSQL connections via asyncpg pools with SSL.
  - Railway-native patterns over generic cloud solutions.
linked_artifacts:
  primary: workflow_operations
  related: [quality_gate_operations, checkpoint_operations, dispatch_rule_operations, system_prompt_operations]
infra_kcs:
  - kc_railway_platform_deep
  - kc_railway_cli_patterns  
  - kc_postgresql_railway
  - kc_nixpacks_buildpacks
  - kc_zero_downtime_deploy
  - kc_api_health_monitoring
  - kc_uvicorn_production
  - kc_railway_networking
  - kc_middleware_stack
  - kc_credit_system_railway
density_score: 0.97
data_source: internal://N05_operations + railway_platform_docs
---

# Operations Nucleus Knowledge Card

## Quick Reference

```yaml
owner: N05
focus: execution reliability and release safety
default_loop: inspect -> reproduce -> isolate -> patch -> validate -> checkpoint
risk_bias: prefer explicit red over false green
```

## Domain Model

### 1. Evidence Hierarchy

Strongest to weakest:

1. Reproduced failure with exact command or runtime trace
2. Passing validation that exercises the changed path
3. Config/workflow diff with deterministic behavioral implication
4. Static analysis and lint signals
5. Human explanation without runtime support

### 2. Failure Surface Types

- **Code defect**: logic, state, exception handling, serialization, concurrency
- **Test defect**: brittle fixtures, environment coupling, stale assertions, ordering dependence
- **Pipeline defect**: broken workflow graph, bad cache key, wrong runner image, artifact mismatch
- **Deploy defect**: migration risk, config drift, missing secrets, unhealthy startup, incompatible artifact
- **Infra defect**: container wiring, dependency readiness, port mismatch, health probe failure
- **Observability defect**: missing logs, absent metrics, noisy alerts, invisible rollback state

### 3. Review Priorities

Review in this order:

1. Behavioral regression risk
2. Missing validation or regression coverage
3. Deploy/runtime config risk
4. Data migration and compatibility risk
5. Rollback and observability gaps
6. Secondary maintainability issues

## Operational Heuristics

### Test Triage

- Start with the smallest failing selector that represents the broken path.
- Expand to adjacent scope only after the minimal fix holds.
- A flaky pass is not a stable pass; repeat or classify.
- Coverage is supporting evidence, not a substitute for semantic validation.

### Debug Triage

- Establish expected versus observed behavior before editing.
- Check recent diffs, config changes, and environment assumptions early.
- If prod-only, increase instrumentation or compare runtime contracts before guessing.

### CI/CD Triage

- Read workflow graph before changing job commands.
- Confirm trigger conditions, matrix dimensions, cache keys, and artifact handoffs.
- Separate infra failure from test failure from orchestration failure.

### Deployment Triage

- Verify build artifact existence and target runtime assumptions.
- Confirm env contract, dependency reachability, and startup/health behavior.
- Require rollback notes for migrations, config flips, or one-way data changes.

## Required Output Elements

Every substantive N05 output should preserve these elements when applicable:

- scoped target
- evidence used
- patch or findings
- validation commands
- residual risk
- rollback posture
- next action if blocked

## Anti-Patterns

- "Looks fine" without running anything relevant
- "Cannot reproduce" without documenting attempted commands
- Approving CI changes without reading the workflow file
- Treating deploy validation as complete because unit tests passed
- Omitting rollback because the patch seems small
