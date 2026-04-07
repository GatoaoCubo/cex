---
id: p12_signal_builder_construction
kind: signal
pillar: P12
title: "Signal Protocol — N03 Builder"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: null
tags: [signal, builder, N03, protocol, orchestration, complete, error]
tldr: "Signal protocol for N03 Builder — emits complete/error/progress signals to .cex/runtime/signals/ for N07 consumption."
density_score: 0.93
linked_artifacts:
  primary: "N03_builder/orchestration/handoff_builder.md"
  related:
    - N03_builder/orchestration/workflow_builder.md
    - N07_admin/orchestration/signal_admin.md
---

# Signal Protocol — N03 Builder

## Purpose

N03 Builder communicates task state to N07 Orchestrator via JSON signals
written to `.cex/runtime/signals/`. Signals are the ONLY inter-nucleus
communication mechanism — no direct calls, no shared state.

## Signal Types

### Complete
Emitted when task finishes successfully with all artifacts committed.

```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', 9.0)
```

```json
{
  "agent_group": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-04-07T19:55:00-03:00",
  "task": "bootstrap_fractal",
  "artifacts": [
    "N03_builder/agents/agent_builder.md",
    "N03_builder/prompts/system_prompt_builder.md"
  ],
  "artifacts_count": 2
}
```

### Error
Emitted when task fails and N03 cannot recover.

```python
write_signal('n03', 'error', 0.0, 'schema validation failed at F7')
```

```json
{
  "agent_group": "n03",
  "status": "error",
  "quality_score": 0.0,
  "timestamp": "2026-04-07T19:55:00-03:00",
  "error": "schema validation failed at F7",
  "failed_step": "F7_GOVERN"
}
```

### Progress
Emitted during long tasks to indicate ongoing work.

```python
write_signal('n03', 'progress', 0.0, 'built 4 of 12 artifacts')
```

```json
{
  "agent_group": "n03",
  "status": "progress",
  "quality_score": 0.0,
  "timestamp": "2026-04-07T19:55:00-03:00",
  "message": "built 4 of 12 artifacts",
  "progress_pct": 33
}
```

## Signal Path

```
.cex/runtime/signals/n03_{status}.json
```

Example: `.cex/runtime/signals/n03_complete.json`

## Signal Rules

1. ALWAYS signal on task completion — never exit silently
2. ALWAYS commit before signaling — signal implies work is committed
3. NEVER emit `complete` if any BLOCKER gate failed
4. ALWAYS include `artifacts` list in complete signals
5. Use `progress` every 3-4 artifacts during batch builds
6. Signal is fire-and-forget — N07 polls, N03 doesn't wait

## N07 Consumption

N07 reads signals via:
```bash
bash _spawn/dispatch.sh status
# or
python _tools/cex_signal_watch.py --nucleus n03
```

## References

- Handoff contract: N03_builder/orchestration/handoff_builder.md
- N07 signal protocol: N07_admin/orchestration/signal_admin.md
- Signal writer: `_tools/signal_writer.py`
