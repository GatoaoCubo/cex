# P07 Evaluation — N07 Admin

> Orchestrating Sloth · quality gates for orchestration decisions

## Scope in N07
Quality enforcement on orchestration itself: dispatch validity
gates, handoff depth checks, wave readiness probes, GDP manifest
validation, consolidation-completeness audits. Sloth hates rework
— so gates here block bad dispatches before nuclei spin up.

## Kinds that live here
- `quality_gate` — dispatch-validity and handoff-depth gates
- `scoring_rubric` — rubrics for orchestration quality (dispatch fit, wave order)
- `regression_check` — detect orchestration regressions (signal loss, orphan PIDs)
- `smoke_eval` — fast probes on `.cex/runtime/` state

## Related
- `orchestration/` — the workflows these gates validate
- `feedback/` — learning records from past orchestration failures
