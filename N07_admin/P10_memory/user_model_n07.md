---
id: user_model_n07
kind: user_model
8f: F2_become
nucleus: n07
pillar: P10
mirrors: N00_genesis/P10_memory/tpl_user_model.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - active_mission
    - decision_state
    - teaching_log
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with mission context
peer_id: orchestrator_user
workspace: cex_main
storage:
  primary: sqlite
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: false
dialectic:
  pre_response_insight: true
  post_response_derive: true
  compaction_cadence_turns: 25
collections:
  - name: mission_preferences
  - name: decision_history
  - name: teaching_state
retention:
  messages_ttl_days: 365
  derived_facts_ttl_days: null
version: 1.0.0
quality: 8.3
tags: [mirror, n07, orchestration, user_model, hermes_assimilation]
tldr: "N07 user model: mission context, GDP decision history, taught-term state for orchestrator dispatch"
created: "2026-04-18"
updated: "2026-04-18"
author: n07_admin
related:
  - n07_output_orchestration_audit
  - p01_kc_orchestration_best_practices
  - n07_taught_terms_registry
  - bld_collaboration_team_charter
  - p01_kc_cex_project_overview
  - p12_wf_admin_orchestration
  - agent_card_n07
  - spec_n07_operational_intelligence
  - p12_wf_orchestration_pipeline
  - auto-accept-handoff
density_score: 1.0
---

## Override Rationale

N07's user model is dispatch-centric. Where N04 tracks knowledge preferences and N06
tracks purchase patterns, N07 tracks: what mission is active, what decisions the user
already locked, and which terms have been taught (so N07 never re-teaches).

## Collections (N07 Overrides)

### mission_preferences

| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| default_grid_size | 6 | 0.95 | 2026-04-18 |
| preferred_dispatch_mode | grid > crew > solo | 0.90 | 2026-04-18 |
| autonomy_level | high (minimal GDP) | 0.95 | 2026-04-18 |
| polling_interval_sec | 60-90 | 0.95 | 2026-04-18 |

### decision_history

| Decision ID | Domain | Choice | Locked At |
|-------------|--------|--------|-----------|
| dp_001 | model_tier | opus_all_nuclei | 2026-04-15 |
| dp_002 | dispatch_mode | sequential_preferred | 2026-04-12 |
| dp_003 | brand_bootstrap | skip_dev_repo | 2026-04-10 |

### teaching_state

| Term | Metaphor | Industry | Taught At | Confirmed |
|------|----------|----------|-----------|-----------|
| deck | card file | agent_card | 2026-04-07 | yes |
| draw | retrieval | RAG retrieval | 2026-04-07 | yes |
| mold | archetype | archetype | 2026-04-08 | yes |

## Compaction Cadence

N07 compacts every 25 turns (vs N00 default 50) because orchestrator sessions
are high-throughput: many short dispatches, status checks, and consolidations.
Earlier compaction prevents decision_history from bloating context.

## Dialectic Loop (N07 Flavor)

| Phase | N07 Behavior | N00 Default |
|-------|-------------|-------------|
| pre_response_insight | "What mission is active? What decisions are locked?" | Generic peer.chat |
| post_response_derive | Extract: new decisions, taught terms, dispatch patterns | Generic fact derivation |
| compaction | Merge decision_history entries; archive completed missions | Generic summary |

## API Surface (N07 Extensions)

| Method | N07 Usage |
|--------|-----------|
| peer.chat | "What did the user decide about model routing?" |
| session.context | Bounded to mission scope (active mission only) |
| session.add_messages | Ingest dispatch outcomes + user feedback |
| search | Query decision_history by domain or date |
| session.representation | "User prefers autonomous high-throughput grid dispatch with Opus" |

## Links

- N00 archetype: [[N00_genesis/P10_memory/tpl_user_model.md]]
- N04 canonical owner: [[N04_knowledge/P10_memory/user_model_n04.md]]
- Decision manifest: [[.cex/runtime/decisions/decision_manifest.yaml]]
- Taught terms: [[N07_admin/P10_memory/taught_terms_registry.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n07_output_orchestration_audit]] | downstream | 0.32 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.31 |
| [[n07_taught_terms_registry]] | related | 0.30 |
| [[bld_collaboration_team_charter]] | downstream | 0.28 |
| [[p01_kc_cex_project_overview]] | upstream | 0.28 |
| [[p12_wf_admin_orchestration]] | downstream | 0.27 |
| [[agent_card_n07]] | downstream | 0.26 |
| [[spec_n07_operational_intelligence]] | upstream | 0.25 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.25 |
| [[auto-accept-handoff]] | downstream | 0.25 |
