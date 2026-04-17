# P07 Evaluation — N05 Operations

> Gating Wrath · quality gates, regression checks, deploy validation

## Scope in N05
Quality enforcement at operational boundaries: pre-deploy gates,
smoke tests, regression checks, rollback triggers, SLA probes.
Wrath drives merciless gating — anything below the floor is
blocked, not warned. This pillar is N05's cultural identity.

## Kinds that live here
- `quality_gate` — hard gates before merge/deploy
- `regression_check` — detect drops in SLIs post-deploy
- `smoke_eval` — fast post-deploy health probes
- `benchmark` — performance baselines per release

## Related
- `tools/` — the test runners and probe tools these gates invoke
- `config/` — feature flags and thresholds read by gates
