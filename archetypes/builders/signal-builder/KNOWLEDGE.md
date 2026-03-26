---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for signal production
sources: P12 schema + P12 examples + codexa-core signal_writer.py
---

# Domain Knowledge: signal

## Core Concept
`signal` is the smallest coordination artifact in P12 orchestration.
It answers a narrow runtime question:
"Which satellite emitted which status, at what quality, at what time?"

Signals are notifications, not instructions.
They are consumed by monitors, supervisors, and next-step dispatchers.

## Minimum Semantic Contract
Every valid signal carries four core facts:
- `satellite`: who emitted the event
- `status`: what happened
- `quality_score`: how good the outcome was, 0.0-10.0
- `timestamp`: when it happened, ISO 8601

This aligns with the current real writer in
`codexa-core/records/core/python/signal_writer.py`, which emits
`satellite`, `status`, `quality_score`, `timestamp`, plus optional extras.

## Status Semantics
| Status | Meaning | Typical consumer action |
|--------|---------|-------------------------|
| complete | Work finished successfully | collect artifacts, continue pipeline |
| error | Work failed or aborted | log, retry, escalate |
| progress | Work still running | update monitor, wait |

`partial` and `timeout` exist in current code, but are not part of the minimal
P12 signal contract in this builder. Treat them as extension statuses only if
the caller explicitly requires compatibility with an external runtime.

## Optional Fields Pattern
Signals may carry a few optional machine fields when useful:
- `task`: short task label
- `artifacts`: changed files or generated outputs
- `artifacts_count`: quick aggregate
- `commit_hash`: git commit reference
- `error_code`: compact failure category
- `message`: short human-readable note
- `progress_pct`: 0-100 for progress signals

Optional fields extend the event. They must not redefine the event.

## Boundary vs Nearby Types
| Type | What it is | Why it is not `signal` |
|------|------------|------------------------|
| handoff | instruction packet with context, tasks, scope fence, commit rules | tells an agent what to do |
| dispatch_rule | routing map from keywords/scope to satellite/model | decides who should receive work |
| workflow | executable sequence of steps | coordinates multiple actions |
| interface | contract/schema between systems | defines stable exchange spec, not a runtime event |

Rule of thumb:
- "Task done / failed / still running" -> `signal`
- "Do this work next" -> `handoff`
- "Route these keywords to this satellite" -> `dispatch_rule`

## Naming Pattern
P12 schema defines: `p12_sig_{{event}}.json`
Examples:
- `p12_sig_satellite_complete.json`
- `p12_sig_batch_progress.json`
- `p12_sig_validation_error.json`

## Operational Constraints
- Must stay under 4096 bytes
- Should remain single-event and append-only
- Should be easy to poll from `.claude/signals/`
- Must degrade gracefully when optional fields are absent
