# _ops/ — Operational Workspace

Runtime artifacts produced by N07 (orchestrator) and consumed by N01-N06 (builders).

## Directory Map

```
_ops/
  plans/              Mission DAGs (kind: dag, P12)           [COMMITTED]
  handoffs/
    _active/          Live dispatch instructions (kind: handoff)  [COMMITTED]
    _done/            Auto-archived after signal                  [COMMITTED]
  signals/            Completion signals (kind: signal)           [GITIGNORED]
  reports/            Build reports (kind: learning_record)       [COMMITTED]
  checkpoints/        Wave state snapshots (kind: checkpoint)     [COMMITTED]
  temp/               PIDs, locks, ephemeral (no kind)            [GITIGNORED]
```

## Lifecycle

```
1. N07 creates plan          → _ops/plans/{MISSION}_{date}.md
2. N07 writes handoffs       → _ops/handoffs/_active/{MISSION}_{nucleus}_{seq}.md
3. spawn_grid.ps1 dispatches → N0x reads handoff, executes
4. N0x completes             → _ops/signals/signal_{nucleus}_{timestamp}.json
5. Monitor detects signal    → moves handoff to _ops/handoffs/_done/
6. N0x commits report        → _ops/reports/report_{nucleus}_{mission}_{date}.md
7. Wave complete             → _ops/checkpoints/checkpoint_{mission}_{wave}.md
```

## Naming Conventions

| Dir | Pattern | Example |
|-----|---------|---------|
| plans/ | `{MISSION}_{date}.md` | `BOOTSTRAP_2026-03-30.md` |
| handoffs/ | `{MISSION}_{nucleus}_{seq}.md` | `BOOTSTRAP_n03_01.md` |
| signals/ | `signal_{nucleus}_{timestamp}.json` | `signal_n03_20260330_143000.json` |
| reports/ | `report_{nucleus}_{mission}_{date}.md` | `report_n03_BOOTSTRAP_2026-03-30.md` |
| checkpoints/ | `checkpoint_{mission}_{wave}.md` | `checkpoint_BOOTSTRAP_wave1.md` |

## vs codexa-core (what improved)

| Problem in codexa | Solution in CEX |
|--------------------|-----------------|
| 296 handoffs in flat dir, 8 _archived* folders | _active/ + _done/ split, auto-archive |
| 629 signals never cleaned | signals/ gitignored (ephemeral by design) |
| 130 temp files as junkyard | temp/ gitignored, only PIDs/locks |
| Reports in gitignored .claude/temp/ | reports/ committed (always in git) |
| Plans in STELLA's head | plans/ as versioned DAG artifacts |
| No checkpoints between waves | checkpoints/ snapshot state per wave |
| Inconsistent naming | {MISSION}_{nucleus}_{seq} everywhere |

## Cleanup

- `_ops/handoffs/_done/`: safe to delete after 7 days
- `_ops/signals/`: auto-cleaned by spawn scripts
- `_ops/temp/`: cleared on every `cex stop`
