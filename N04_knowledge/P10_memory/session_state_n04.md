---
id: session_state_n04
kind: session_state
8f: F8_collaborate
nucleus: n04
pillar: P10
mirrors: N00_genesis/P10_memory/tpl_session_state.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: GULA DO CONHECIMENTO
  required_fields:
    - sources
    - retrieval_method
    - freshness
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
version: 1.0.0
quality: 7.6
tags: [mirror, n04, knowledge, session_state, hermes_assimilation, retrieval_history, citation_trail]
related:
  - p01_kc_session_state
  - bld_memory_session_state
  - bld_tools_session_state
  - bld_collaboration_session_state
  - p01_kc_session_backend
  - p03_sp_session_state_builder
  - session-state-builder
  - bld_architecture_session_backend
  - bld_config_session_state
  - bld_schema_session_state
---

## Override Rationale

N04's session state is a **knowledge session**: every tool call, retrieval operation,
and source citation is logged in the session. This makes the session state itself a
queryable provenance record -- at any point during a session, N04 can answer:
"what have we retrieved, from where, and with what confidence?"

## N04 Session State Schema

### Active KC Tracking

| Field | Type | Description |
|-------|------|-------------|
| `active_kind` | str | Current kind being produced or queried |
| `active_pillar` | str | Current pillar in scope |
| `active_kc_refs` | list[str] | KC file paths loaded in this session |
| `builder_loaded` | str \| null | Current builder ISOs loaded (F2 BECOME state) |

### Retrieval History

| Seq | Query | Method | Top Result | Confidence | Retrieved At |
|-----|-------|--------|-----------|------------|-------------|
| 1 | `{{query}}` | {{method}} | `{{path}}` | {{0.0-1.0}} | {{HH:MM:SS}} |

### Citation Trail

| Claim | Source | Path | Confidence | Verified |
|-------|--------|------|------------|---------|
| `{{claim_summary}}` | {{source_id}} | `{{path}}` | {{0.0-1.0}} | {{true\|false}} |

### Corpus Gaps

| Gap | Triggered By | Status |
|-----|-------------|--------|
| `{{gap_description}}` | {{skill_or_query}} | `open \| queued \| ingested` |

## Session Lifecycle

| Phase | N04 Action |
|-------|-----------|
| `session_start` | Load user_model_n04, initialize retrieval_history, clear citation_trail |
| `per_turn` | Append retrieval ops, update active_kind, log any new taught_terms |
| `pre_persist` | Check curation_nudge threshold; if met, emit nudge |
| `session_end` | Archive retrieval_history to learning_record_n04; emit final curation_nudge if unconfirmed items remain |

## Retention Policy

- `retrieval_history`: kept for session duration; archived to `mem_learning_record_n04.md` on session_end
- `citation_trail`: retained indefinitely in `entity_memory_n04.md` (sources are permanent)
- `corpus_gaps`: forwarded to `revision_loop_policy_n04.md` for next-session ingestion planning

## Links

- N00 archetype: [[N00_genesis/P10_memory/tpl_session_state.md]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_session_state.md]]
- Related: [[N04_knowledge/P10_memory/mem_runtime_state_n04.md]]
- Related: [[N04_knowledge/P11_feedback/curation_nudge_n04.md]]
- Related: [[N04_knowledge/P11_feedback/learning_record_n04.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_session_state]] | related | 0.37 |
| [[bld_memory_session_state]] | related | 0.36 |
| [[bld_tools_session_state]] | upstream | 0.35 |
| [[bld_collaboration_session_state]] | related | 0.33 |
| [[p01_kc_session_backend]] | related | 0.33 |
| [[p03_sp_session_state_builder]] | upstream | 0.32 |
| [[session-state-builder]] | related | 0.32 |
| [[bld_architecture_session_backend]] | upstream | 0.28 |
| [[bld_config_session_state]] | upstream | 0.28 |
| [[bld_schema_session_state]] | upstream | 0.27 |
