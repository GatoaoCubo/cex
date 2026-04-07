---
id: p12_wf_auto_health
kind: workflow
pillar: P12
title: "Auto-Health — Probe system before dispatch"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: before_dispatch
quality: 9.1
tags: [workflow, auto, n07, health, probe, k8s]
tldr: "Health check before dispatching any nucleus — validates doctor, compilation, git state, and builder integrity."
density_score: 0.92
updated: 2026-04-07
---

# Auto-Health

## Trigger
Before any `/grid` or `/dispatch` command executes.

## Industry Pattern
Kubernetes readiness/liveness probes. Check system health before sending traffic.

## Steps

| # | Action | Tool | Pass Criteria |
|---|--------|------|---------------|
| 1 | Run doctor | `cex_doctor.py` | 0 FAIL (WARN ok) |
| 2 | Check compilation | `cex_compile.py --all` | 100% success |
| 3 | Git clean check | `git status --porcelain` | No uncommitted changes |
| 4 | Verify target nucleus boot | `test -f boot/{nucleus}.cmd` | File exists |
| 5 | Verify builder integrity | doctor row for target kind | PASS |
| 6 | Check disk space | `df` or equivalent | >500MB free |

## Verdicts

| Result | Action |
|--------|--------|
| All pass | Proceed with dispatch |
| 1-2 WARN | Proceed with warning to user |
| Any FAIL | Block dispatch. Show failed checks. Suggest `/doctor` |

## Failure Mode
Health check itself fails → log error, proceed with dispatch (don't block on broken health check).


## Operational Constraints

This automated workflow operates under strict resource and safety boundaries:

- **Budget cap**: maximum token expenditure per execution enforced via runtime counter
- **Idempotency**: re-running the workflow produces no side effects if previous run succeeded
- **Rollback safe**: every state change creates a checkpoint enabling full reversal
- **Audit logged**: execution start, each step completion, and final status written to log

### Execution Trace

```yaml
# Workflow execution record
trace:
  workflow: wf_auto_health
  started: 2026-04-07T15:00:00
  status: completed
  steps_total: 4
  steps_passed: 4
  duration_seconds: 45
  token_usage: 12000
  artifacts_modified: 3
```

| Phase | Action | Gate |
|-------|--------|------|
| Pre-check | Validate inputs and prerequisites | Abort on missing dependency |
| Execute | Run core workflow logic | Monitor for errors |
| Post-check | Verify outputs meet quality threshold | Flag regressions |
| Cleanup | Archive temp files, update signals | Always runs |

