---
id: p12_wf_auto_ship
kind: workflow
8f: F8_collaborate
pillar: P12
title: "Auto-Ship — CI/CD pipeline when quality gates pass"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: quality_gate_passes
quality: 9.1
tags: [workflow, auto, n07, ship, cicd, deploy]
tldr: "When all quality gates pass: compile all, run tests, git commit, push, signal complete. The CI/CD pipeline of CEX."
density_score: 0.92
updated: 2026-04-07
related:
  - p12_wf_auto_review
  - p12_wf_auto_health
  - p12_wf_auto_rollback
  - p12_wf_auto_security
  - p12_wf_auto_hydrate
  - p12_wf_auto_research
  - bld_collaboration_workflow
  - p12_wf_engineering_pipeline
  - bld_examples_workflow
  - workflow-builder
---

# Auto-Ship

## Trigger
After auto-review passes on all artifacts in a wave/mission.

## Industry Pattern
CI/CD pipeline: build → test → commit → push → signal.

## Steps

| # | Action | Tool | Pass Criteria |
|---|--------|------|---------------|
| 1 | Compile all | `cex_compile.py --all` | 100% success |
| 2 | Run tests | `pytest _tools/tests/ --tb=short` | 0 new failures |
| 3 | Run doctor | `cex_doctor.py` | No new FAIL |
| 4 | Stage changes | `git add -A` | Clean staging |
| 5 | Commit | `git commit -m "[N0X] {summary}"` | Commit created |
| 6 | Push | `git push` | Remote updated |
| 7 | Signal | `signal_writer.py {nucleus} complete {score}` | Signal written |
| 8 | Archive handoffs | Move `*_task.md` to archive | Clean runtime |

## Commit Message Format
```
[{NUCLEUS}] {wave/mission}: {summary}

Artifacts: {count} created, {count} rewritten
Doctor: {PASS}/{WARN}/{FAIL}
Tests: {passed}/{total}
Quality: {avg_score}
```

## Failure Mode
Test failure → abort ship, trigger auto-debug. Never push broken code.
Compile failure → abort ship, fix compilation, retry.


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
  workflow: wf_auto_ship
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_review]] | sibling | 0.63 |
| [[p12_wf_auto_health]] | sibling | 0.54 |
| [[p12_wf_auto_rollback]] | sibling | 0.45 |
| [[p12_wf_auto_security]] | sibling | 0.41 |
| [[p12_wf_auto_hydrate]] | sibling | 0.40 |
| [[p12_wf_auto_research]] | sibling | 0.37 |
| [[bld_collaboration_workflow]] | related | 0.27 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.27 |
| [[bld_examples_workflow]] | upstream | 0.26 |
| [[workflow-builder]] | related | 0.26 |
