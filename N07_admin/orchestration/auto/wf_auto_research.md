---
id: p12_wf_auto_research
kind: workflow
pillar: P12
title: "Auto-Research — Fill knowledge gaps during planning"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: knowledge_gap_detected
quality: 9.1
tags: [workflow, auto, n07, research, gap, intelligence]
tldr: "When /plan detects a knowledge gap (missing KC, unknown domain), auto-triggers N01 research before proceeding."
density_score: 0.91
updated: 2026-04-07
---

# Auto-Research

## Trigger
During `/plan` decomposition, when a required KC doesn't exist or domain is unfamiliar.

## Industry Pattern
Competitive intelligence / just-in-time research. Don't plan blind — gather intel first.

## Steps

| # | Action | Tool | Condition |
|---|--------|------|-----------|
| 1 | Detect gap | `cex_query.py` returns 0 results | Kind or domain KC missing |
| 2 | Classify gap type | Intent analysis | KC missing vs domain unknown vs data stale |
| 3 | Route to N01 | `dispatch solo n01` or in-session | If N01 available |
| 4 | Wait for signal | `ls .cex/runtime/signals/n01_*` | Max 5 min timeout |
| 5 | Ingest result | Read N01 output KC | Always |
| 6 | Resume planning | Return to `/plan` step that triggered gap | Always |

## Gap Types

| Type | Example | Action |
|------|---------|--------|
| Kind KC missing | No `kc_landing_page.md` | N01 creates it from web research |
| Domain unknown | User mentions "Web3" but no Web3 KCs | N01 researches domain basics |
| Data stale | KC exists but >90 days old | N01 refreshes with current data |
| Competitor unknown | User names competitor not in any KC | N01 creates competitive brief |

## Failure Mode
N01 unavailable or timeout → proceed with planning using available context. Flag gap in plan as "unresearched."


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
  workflow: wf_auto_research
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

