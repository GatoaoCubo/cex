---
id: p12_sig_satellite_complete
kind: signal
pillar: P12
description: "Completion signal emitted by satellite after task execution"
event: satellite_complete
format: json
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [signal, completion, satellite, orchestration]
---

# Signal: satellite_complete

## Purpose
Emitted by satellite after task completion. Consumed by spawn_monitor.ps1 and STELLA for wave tracking.

## Schema
```json
{
  "satellite": "edison",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-24T20:00:00Z",
  "task": "8 P04 examples from real artifacts",
  "artifacts_count": 8,
  "commit": "e8dd58b"
}
```

## Emit
```python
from records.core.python.signal_writer import write_signal
write_signal("edison", "complete", 9.0)
# Writes to .claude/signals/edison_complete_9.0.json
```

## Consume
```powershell
# spawn_monitor.ps1 polls every 30s
Get-ChildItem .claude/signals/*.json | ForEach-Object {
    $sig = Get-Content $_ | ConvertFrom-Json
    if ($sig.status -eq "complete") { "Done: $($sig.satellite)" }
}
```

## Status Values
| Status | Meaning | Action |
|--------|---------|--------|
| complete | Task done, quality passed | Collect + next batch |
| error | Task failed | Log + retry or escalate |
| progress | Still working (heartbeat) | Wait, check stuck timer |
