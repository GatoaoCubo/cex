---
id: p01_kc_operations_nucleus
kind: knowledge_card
pillar: P01
title: Operations Nucleus Knowledge Card
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n05_operations
domain: operations-engineering
quality: 8.9
tags: [knowledge_card, N05, operations, ci-cd, deploy]
tldr: Distilled operational doctrine for code review, testing, debugging, deployment, CI/CD, infrastructure, and monitoring.
when_to_use: When a task requires execution safety, reproducibility, test evidence, pipeline diagnosis, or release governance.
keywords: [review, test, debug, deploy, ci, cd, docker, observability]
long_tails:
  - How should N05 triage a failing pipeline before changing code?
  - What evidence is required before marking a release as safe?
  - How should an ops-focused agent handle flaky tests and rollback risk?
axioms:
  - Reproduce before repairing.
  - Test before claiming.
  - Deploy only with rollback and observability.
linked_artifacts:
  primary: workflow_operations
  related: [quality_gate_operations, checkpoint_operations, dispatch_rule_operations]
density_score: 0.93
data_source: internal://N05_operations
---

# Operations Nucleus Knowledge Card

## Quick Reference

```yaml
owner: N05
focus: execution reliability
criticality: high
default_mode: inspect -> reproduce -> patch -> validate -> signal
```

## Core Concepts

- **Execution Evidence**: command output, failing test traces, logs, and diff inspection are stronger than narrative explanation
- **Operational Risk**: migration breakage, secret/config drift, unhealthy dependencies, missing rollback, and blind spots in monitoring
- **Progressive Validation**: targeted checks first, full-path validation second, production guidance last
- **Blast Radius Control**: prefer narrow changes, scoped deploys, feature flags, and reversible steps

## Standard Operating Loop

1. Inspect repository state, changed files, and relevant configs.
2. Reproduce the issue or confirm the review target with concrete commands.
3. Isolate the smallest failing surface: test, function, service, job, or container.
4. Apply the minimal fix that restores correctness without incidental refactor.
5. Validate locally with the most relevant automated checks.
6. Record residual risk, rollback notes, and operational follow-up.

## Review Heuristics

- Missing regression tests on changed behavior is a release risk.
- CI config changes require checking job dependencies, caching, secrets, and branch filters.
- Docker or infra changes require startup, health, and environment contract validation.
- "Works locally" is not sufficient without matching the failing runtime path.

## Debug Heuristics

- Compare expected path vs observed path before editing.
- Prefer logs, stack traces, failing assertions, and config diff over speculative fixes.
- If a bug cannot be reproduced, classify the uncertainty and tighten instrumentation instead of guessing.

## Deploy Heuristics

- A release is not ready without build success, test evidence, config review, and rollback path.
- Post-deploy checks should cover health endpoint, key business flow, metrics, and alert noise.
- Schema or migration changes require compatibility and rollback discussion even when tests pass.
