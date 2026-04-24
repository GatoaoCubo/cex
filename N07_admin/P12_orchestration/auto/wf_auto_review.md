---
id: p12_wf_auto_review
kind: workflow
8f: F8_collaborate
pillar: P12
title: "Auto-Review — Validate nucleus output on arrival"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: nucleus_output_arrives
quality: 8.7
tags: [workflow, auto, n07, review, quality, gate]
tldr: "When a nucleus signals complete, auto-review its output: frontmatter, compilation, quality gate, doctor check."
density_score: 0.92
updated: 2026-04-07
related:
  - p12_wf_auto_ship
  - p12_wf_auto_health
  - p12_wf_auto_security
  - p12_wf_auto_hydrate
  - p12_wf_auto_research
  - p12_wf_auto_rollback
  - p11_qg_admin_orchestration
  - p11_qg_workflow
  - bld_examples_workflow
  - p03_sp_workflow-builder
---

# Auto-Review

## Trigger
Nucleus signals complete (`signal_writer.py`), or new commits detected from a dispatched nucleus.

## Industry Pattern
Pull Request review / code review gate. Output doesn't ship until it passes review.

## Steps

| # | Action | Tool | Pass Criteria |
|---|--------|------|---------------|
| 1 | Detect new artifacts | `git log --oneline -N` | Commits from nucleus |
| 2 | Compile all new files | `cex_compile.py {paths}` | 100% compile success |
| 3 | Run doctor on changed builders | `cex_doctor.py` | 0 new FAIL |
| 4 | Check frontmatter completeness | grep for required fields | All present |
| 5 | Check quality:null policy | `grep "quality: null"` on new files | quality:null (not self-scored) |
| 6 | Check density | `grep density_score` | >= 0.85 |
| 7 | Verify signal was sent | `ls .cex/runtime/signals/{nucleus}_*` | Signal exists |

## Verdicts

| Result | Action |
|--------|--------|
| All pass | Mark task complete. Proceed to consolidate. |
| Minor issues (WARN) | Auto-fix if possible (compile, add missing field). Log. |
| Major failure | Flag to user: "N0X output needs attention: {issue}" |

## Auto-Fix Capabilities
- Missing `quality: null` → inject it
- Missing compilation → run `cex_compile.py`
- Missing signal → write signal with score from review

## Failure Mode
Review itself fails → log error, mark output as "unreviewed," proceed.


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
  workflow: wf_auto_review
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
| [[p12_wf_auto_ship]] | sibling | 0.53 |
| [[p12_wf_auto_health]] | sibling | 0.51 |
| [[p12_wf_auto_security]] | sibling | 0.41 |
| [[p12_wf_auto_hydrate]] | sibling | 0.40 |
| [[p12_wf_auto_research]] | sibling | 0.37 |
| [[p12_wf_auto_rollback]] | sibling | 0.35 |
| [[p11_qg_admin_orchestration]] | upstream | 0.26 |
| [[p11_qg_workflow]] | related | 0.25 |
| [[bld_examples_workflow]] | upstream | 0.24 |
| [[p03_sp_workflow-builder]] | upstream | 0.24 |
