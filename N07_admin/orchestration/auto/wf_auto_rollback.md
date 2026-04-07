---
id: p12_wf_auto_rollback
kind: workflow
pillar: P12
title: "Auto-Rollback — Revert on deploy/ship failure"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: deploy_fails_health
quality: 9.1
tags: [workflow, auto, n07, rollback, sre, recovery]
tldr: "When auto-ship or deploy fails health check, automatically revert to last known good state."
density_score: 0.91
updated: 2026-04-07
---

# Auto-Rollback

## Trigger
Auto-ship fails at step 2 (tests) or step 3 (doctor), or external deploy fails health probe.

## Industry Pattern
SRE rollback procedure. If new version fails → revert to last known good.

## Steps

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Identify failure point | Ship log / error output | Which step failed |
| 2 | Find last good commit | `git log --oneline` | Commit hash |
| 3 | Stash current changes | `git stash` | Changes preserved |
| 4 | Verify last good state | `cex_doctor.py` + `pytest` | Confirm it's good |
| 5 | Report to user | Show: what failed, what was reverted | User decides next step |

## Rollback Strategies

| Severity | Strategy |
|----------|----------|
| 1 file broke tests | `git checkout {file}` — revert single file |
| Wave broke system | `git stash` — preserve work, revert all |
| Critical corruption | `git reset --hard {last_good}` — nuclear option |

## Safeguards
- NEVER auto-`reset --hard` without user confirmation
- ALWAYS `git stash` before any revert (preserve work)
- ALWAYS run doctor after rollback to confirm recovery

## Failure Mode
If rollback itself fails → stop all operations, alert user: "System in inconsistent state. Manual intervention needed."


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
  workflow: wf_auto_rollback
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

