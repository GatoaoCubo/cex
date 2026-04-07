---
kind: schema
id: bld_schema_signal
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for signal - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: signal
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `signal` |
| Machine format | `json` |
| Naming | `p12_sig_{event}.json` |
| Max bytes | 4096 |
## Required Payload Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| agent_group | string, non-empty, lowercase slug preferred | YES | - | emitting agent/agent_group |
| status | enum (`complete`, `error`, `progress`) | YES | - | atomic event state |
| quality_score | number, `0.0 <= x <= 10.0` | YES | - | event quality/outcome score |
| timestamp | string, ISO 8601 datetime | YES | - | emission moment |
## Optional Payload Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| task | string | NO | omitted | short task summary |
| artifacts | list[string] | NO | omitted | changed or generated artifacts |
| artifacts_count | integer, `>= 0` | NO | omitted | compact summary count |
| commit_hash | string | NO | omitted | commit reference when applicable |
| error_code | string | NO | omitted | stable error category |
| message | string | NO | omitted | short human-readable note |
| progress_pct | integer, `0-100` | NO | omitted | only for `progress` signals |
## Semantic Rules
1. One signal describes one event from one emitter
2. `status=complete` means work concluded successfully enough to advance
3. `status=error` means work failed or blocked
4. `status=progress` means work is ongoing and not yet terminal
5. `progress_pct` is valid only when `status=progress`
6. Optional fields extend context but never replace the required four fields
## Boundary Rules
`signal` IS:
- atomic runtime notification
- status exchange between agents/supervisors
- lightweight machine-readable event
`signal` IS NOT:
- `handoff`: no task list, no scope fence, no execution instructions
- `dispatch_rule`: no keyword map, no routing policy, no agent_group selection rules
- `workflow`: no step graph, no sequencing logic
## Canonical Minimal Example
```json
{
  "agent_group": "codex",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-26T10:30:00-03:00"
}
```
