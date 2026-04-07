---
id: p12_wf_auto_hydrate
kind: workflow
pillar: P12
title: "Auto-Hydrate — Enrich user input before routing"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: every_user_input
quality: 9.1
tags: [workflow, auto, n07, hydrate, enrichment]
tldr: "Automatically enriches raw user input with brand context, memory, and KC signals before any nucleus receives it."
density_score: 0.92
updated: 2026-04-07
---

# Auto-Hydrate

## Trigger
Every user input that will be routed to a nucleus.

## Industry Pattern
Data enrichment (ETL extract-transform-load). Raw input is "extracted," brand/memory context is "transformed" in, enriched prompt is "loaded" to nucleus.

## Steps

| # | Action | Tool | Condition |
|---|--------|------|-----------|
| 1 | Parse intent | `cex_intent.py` | Always |
| 2 | Resolve kind + pillar | `cex_8f_motor.py` F1 | Always |
| 3 | Inject brand context | `brand_inject.py` | If `brand_config.yaml` exists |
| 4 | Load decision manifest | read `decision_manifest.yaml` | If manifest exists |
| 5 | Select relevant memory | `cex_memory_select.py` | If builder memory exists |
| 6 | Select relevant KCs | `cex_query.py` | If kind KC exists |
| 7 | Compose enriched prompt | `cex_crew_runner.py compose_prompt()` | Always |
| 8 | Route to nucleus | dispatch or in-session | Always |

## Input
Raw user text: `"quero uma landing page"`

## Output
Enriched prompt with: intent classification + brand vars + memory + KC context + builder specs.

## Failure Mode
If any enrichment step fails → skip it, log warning, continue with partial context.
Never block routing because enrichment failed.


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
  workflow: wf_auto_hydrate
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

