---
id: p12_sig_admin_orchestration
title: "Signal Admin"
kind: signal
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 9.2
tags: [signal, orchestration, N07, complete, error, progress]
tldr: "Signal protocol for N07 orchestration — complete/error/progress payloads with quality score and artifact references."
density_score: 1.0
---

# Signal Protocol: N07 Orchestration

## Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| agent_group | string | YES | Lowercase slug of emitting nucleus (e.g. n03, n07) |
| status | string | YES | "complete", "error", or "progress" |
| quality_score | float/null | YES | Quality score (0.0-10.0) or null |
| timestamp | string | YES | ISO 8601 datetime |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| task | string | Short label of related task |
| artifacts | array | Paths to produced artifacts |
| artifacts_count | integer | Number of artifacts produced |
| commit_hash | string | Git commit hash |
| error_code | string | Short error classifier |
| message | string | Brief context description |
| progress_pct | integer | Progress percentage (0-100) |

## Signal Emission Command

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', '{status}', {score}, '{mission}')"
```

## Real Examples from Bootstrap

### N03 Complete Signal (builder finished)
```json
{
  "agent_group": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-30T14:00:00Z",
  "task": "bootstrap_f1",
  "artifacts": [
    "N07_admin/P02_model/agent_admin.md",
    "N07_admin/P03_prompt/system_prompt_admin.md",
    "N07_admin/P01_knowledge/knowledge_card_admin.md"
  ],
  "artifacts_count": 3,
  "commit_hash": "abc123def"
}
```

### N07 Mission Complete Signal (orchestrator finished)
```json
{
  "agent_group": "n07",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-30T15:30:00Z",
  "task": "bootstrap_f1_mission",
  "artifacts_count": 10,
  "message": "All 10 N07 artifacts rebuilt, quality 9.0+"
}
```

### N05 Error Signal (ops builder failed)
```json
{
  "agent_group": "n05",
  "status": "error",
  "quality_score": null,
  "timestamp": "2026-03-30T16:00:00Z",
  "task": "deploy_staging",
  "error_code": "test_failure",
  "message": "3 unit tests failed in auth module"
}
```

### N01 Progress Signal (research in progress)
```json
{
  "agent_group": "n01",
  "status": "progress",
  "quality_score": null,
  "timestamp": "2026-03-30T14:30:00Z",
  "task": "market_analysis_q1",
  "progress_pct": 45,
  "message": "Analyzed 3 of 7 competitor reports"
}
```

## Status Vocabulary

| Status | Meaning | Terminal | Quality Required |
|--------|---------|----------|------------------|
| complete | Task finished successfully | YES | YES (>= 8.0) |
| error | Task failed, needs intervention | YES | NO (null) |
| progress | Task ongoing, partial update | NO | NO (null) |

## Consumer Contract

- **MUST** handle: `agent_group`, `status`, `quality_score`, `timestamp`
- **MAY** process optional fields, ignoring absent ones
- **MUST NOT** assume signal contains routing or execution instructions
- **MUST** treat `quality_score: null` as "not yet evaluated"

## Signal File Location

Signals are written to `.cex/runtime/signals/` with naming:
`{nucleus}_{status}_{timestamp}.json`

Example: `n03_complete_20260330T140000.json`

## Orchestrator Signal Handling

N07 reads signals to:
1. Detect builder completion — validate quality
2. Detect errors — decide retry or escalate
3. Track progress — update mission status
4. Move handoffs from `_active/` to `_done/` on acceptance

## References

- Signal writer: _tools/signal_writer.py
- Handoff protocol: N07_admin/P12_orchestration/handoff_admin.md
- Quality gate: N07_admin/P11_feedback/quality_gate_admin.md
- Grid ops (diagnostics, crash detection): N07_admin/P10_memory/grid_orchestration_mastery.md
