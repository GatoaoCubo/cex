---
kind: examples
id: bld_examples_signal
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of signal artifacts
pattern: few-shot learning for minimal orchestration events
---

# Examples: signal-builder

## Golden Example

INPUT: "Emit completion signal for codex after finishing signal-builder"

OUTPUT (`p12_sig_satellite_complete.json`):
```json
{
  "satellite": "codex",
  "status": "complete",
  "quality_score": 9.2,
  "timestamp": "2026-03-26T10:45:00-03:00",
  "task": "signal-builder",
  "artifacts": [
    "archetypes/builders/signal-builder/MANIFEST.md",
    "archetypes/builders/signal-builder/SCHEMA.md"
  ],
  "artifacts_count": 13,
  "commit_hash": "abc1234",
  "message": "13 ISO files created and validated"
}
```

WHY THIS IS GOLDEN:
- filename follows `p12_sig_{event}.json`
- JSON payload is atomic and machine-readable
- required fields are present and typed correctly
- optional fields are compact and useful for monitors
- no handoff instructions, routing rules, or workflow logic

## Golden Progress Example

OUTPUT (`p12_sig_batch_progress.json`):
```json
{
  "satellite": "edison",
  "status": "progress",
  "quality_score": 8.4,
  "timestamp": "2026-03-26T11:00:00-03:00",
  "task": "wave2_batch",
  "progress_pct": 60,
  "message": "6 of 10 artifacts validated"
}
```

WHY THIS PASSES:
- `progress_pct` only appears with `status=progress`
- message stays short
- payload remains a single event snapshot

## Anti-Example

BAD OUTPUT (`p12_sig_dispatch.yaml`):
```yaml
satellite: codex
status: complete
keywords:
  - orchestration
  - routing
next_steps:
  - edit README
  - commit changes
```

FAILURES:
1. wrong machine format: YAML instead of JSON
2. no `quality_score`
3. no `timestamp`
4. includes routing keywords -> `dispatch_rule` drift
5. includes action list -> `handoff` drift
