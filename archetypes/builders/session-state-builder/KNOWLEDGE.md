---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for session_state production
sources: P10 schema + CODEXA session patterns
---

# Domain Knowledge: session_state

## Core Concept
`session_state` is the ephemeral snapshot of an agent's execution context.
It answers: "What is this agent doing right now, how far along, and where can we recover?"

Session states are observations, not instructions or accumulated knowledge.
They are consumed by monitors, recovery tools, and post-session extractors.

## Minimum Semantic Contract
Every valid session_state carries:
- `session_id`: unique execution context
- `agent`: who is executing
- `status`: lifecycle phase
- `started_at`: when execution began

Plus standard CEX fields: id, kind, lp, version, dates, author, quality, tags, tldr.

## Status Semantics
| Status | Meaning | Typical consumer action |
|--------|---------|-------------------------|
| active | Session in progress | monitor, update dashboard |
| paused | Session suspended, recoverable | wait for resume or timeout |
| completed | Session ended normally | extract learning, archive |
| aborted | Session ended abnormally | investigate, retry if needed |

## Optional Fields Pattern
Session states may carry runtime metrics:
- `active_tasks` / `completed_tasks`: task progress tracking
- `context_window_used` / `context_window_max`: token budget monitoring
- `tools_called` / `tool_call_count`: execution intensity
- `errors` / `error_count`: failure tracking
- `checkpoints` / `last_checkpoint`: recovery points
- `duration_seconds`: elapsed time

Optional fields extend the snapshot. They must not transform it into persistent state.

## Boundary vs Nearby Types
| Type | What it is | Why it is not `session_state` |
|------|------------|-------------------------------|
| runtime_state | persistent state across sessions | carries routing decisions, survives session end |
| learning_record | accumulated learning over time | stores patterns, scores, outcomes across sessions |
| brain_index | search index configuration | configures BM25/FAISS, not session data |
| axiom | immutable fundamental rule | permanent, not ephemeral |

Rule of thumb:
- "Agent state right now" -> `session_state`
- "Agent state across sessions" -> `runtime_state`
- "What the agent learned" -> `learning_record`

## Naming Pattern
P10 schema defines: `p10_ss_{session}.yaml`
Examples:
- `p10_ss_edison_wave19_build.yaml`
- `p10_ss_atlas_deploy_v2.yaml`
- `p10_ss_shaka_research_competitors.yaml`

## Operational Constraints
- Must stay under 3072 bytes
- Should remain a single-point snapshot, not a time series
- Should be easy to parse programmatically
- Must degrade gracefully when optional fields are absent
