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
quality: 8.7
tags: [workflow, auto, n07, health, probe, k8s]
tldr: "Health check before dispatching any nucleus — validates doctor, compilation, git state, and builder integrity."
density_score: 0.92
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
