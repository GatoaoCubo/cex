---
id: n00_session_state_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "Session State -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, session_state, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_session_state
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - session-state-builder
  - bld_architecture_session_state
  - bld_schema_multimodal_prompt
  - bld_collaboration_session_state
  - bld_schema_benchmark_suite
  - bld_schema_runtime_state
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A session_state captures the full ephemeral context of an agent session -- conversation history, working decisions, active tools, and nucleus-specific flags -- as a point-in-time snapshot. It enables session continuity across interruptions, crash recovery, and context handoff between nuclei without losing mid-session progress.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `session_state` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| session_id | string | yes | Unique session identifier |
| nucleus | string | yes | Nucleus that owns this session |
| snapshot_type | enum | yes | ephemeral \| checkpoint \| final |
| conversation_turns | integer | yes | Number of turns recorded |
| active_decisions | object | no | GDP decisions made this session |
| artifacts_produced | array | no | IDs of artifacts created this session |
| created_at | datetime | yes | Session start timestamp |
| snapshot_at | datetime | yes | When this snapshot was taken |

## When to use
- When persisting state before a /compact or context window reset
- When creating a checkpoint before dispatching to another nucleus
- When debugging why an agent lost context mid-mission

## Builder
`archetypes/builders/session_state-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind session_state --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ss_n01_research_session_001
kind: session_state
pillar: P10
nucleus: n01
title: "Example Session State"
version: 1.0
quality: null
---
# Session Snapshot: N01 Research Wave
snapshot_type: checkpoint
conversation_turns: 34
artifacts_produced: [kc_edtech_pricing_001]
snapshot_at: "2026-04-17T10:15:00Z"
```

## Related kinds
- `runtime_state` (P10) -- fine-grained in-flight state that session_state aggregates
- `session_backend` (P10) -- backend that persists this session_state
- `memory_summary` (P10) -- compressed version created when session_state becomes too large

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_session_state]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[session-state-builder]] | related | 0.43 |
| [[bld_architecture_session_state]] | upstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_collaboration_session_state]] | related | 0.42 |
| [[bld_schema_benchmark_suite]] | upstream | 0.42 |
| [[bld_schema_runtime_state]] | upstream | 0.41 |
