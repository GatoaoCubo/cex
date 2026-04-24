---
id: curation_nudge_n07
kind: curation_nudge
8f: F6_produce
nucleus: n07
pillar: P11
mirrors: N00_genesis/P11_feedback/tpl_curation_nudge.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
trigger:
  type: wave_completion
  threshold: 1
cadence:
  min_interval_turns: 10
  max_per_session: 5
version: 1.0.0
quality: 8.5
tags: [mirror, n07, orchestration, curation_nudge, hermes_assimilation]
tldr: "N07 mission nudge: wave complete -> persist lessons to MEMORY.md, update decision manifest"
created: "2026-04-18"
updated: "2026-04-18"
author: n07_admin
related:
  - n07_output_orchestration_audit
  - spec_mission_100pct_coverage
  - bld_collaboration_memory_type
  - bld_collaboration_memory_scope
  - p12_wf_orchestration_pipeline
  - bld_manifest_memory_type
  - memory-scope-builder
  - p01_kc_memory_scope
  - p12_wf_admin_orchestration
  - p12_wf_create_orchestration_agent
density_score: 1.0
---

## Override Rationale

N07's curation nudge fires on **wave completion**, not density threshold.
After each wave consolidation, N07 nudges: "Persist dispatch lessons to MEMORY.md?"
This captures: which nuclei succeeded/failed, optimal wave composition, routing insights.

## Trigger Configuration (N07)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Trigger type | wave_completion | Fire after each wave consolidation |
| Threshold | 1 | Every wave completion triggers nudge |
| Min interval | 10 turns | Prevent nudge during rapid multi-wave dispatch |
| Max per session | 5 | Cap at 5 nudges per mission (typical max waves) |
| Observation source | consolidation_report + signal_log | What to surface |

## Prompt Templates (N07)

### Post-wave lesson nudge
```
W{{n}} complete. {{successes}}/{{total}} nuclei delivered.
Lessons: {{key_observations}}.
Persist to MEMORY.md? [S/N]
```

### Decision manifest update nudge
```
{{n}} new decisions locked during this wave.
Update decision_manifest.yaml for future missions? [S/N]
```

### Routing insight nudge
```
N{{x}} took {{time}}min (expected {{expected}}min).
Record routing adjustment? [S/N]
```

## Target Memory Destinations

| Destination | Kind | Trigger Condition |
|-------------|------|-------------------|
| `MEMORY.md` | index | Wave lesson confirmed |
| `decision_manifest.yaml` | decision_record | New decision locked |
| `taught_terms_registry.md` | entity_memory | New term taught during dispatch |
| `.cex/runtime/decisions/` | decision_record | Routing adjustment confirmed |

## Auto-write Behavior

When user confirms a nudge:
1. N07 writes to destination artifact
2. Appends pointer to MEMORY.md if new entry
3. Stamps `freshness: {{YYYY-MM-DD}}` on the entry
4. Logs nudge outcome to consolidation report

## Links

- N00 archetype: [[N00_genesis/P11_feedback/tpl_curation_nudge.md]]
- N04 canonical owner: [[N04_knowledge/P11_feedback/curation_nudge_n04.md]]
- N01 research sibling: [[N01_intelligence/P11_feedback/curation_nudge_n01.md]]
- MEMORY.md: [[.claude/projects/C--Users-CEX-Documents-GitHub-cex/memory/MEMORY.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n07_output_orchestration_audit]] | downstream | 0.28 |
| [[spec_mission_100pct_coverage]] | upstream | 0.24 |
| [[bld_collaboration_memory_type]] | downstream | 0.24 |
| [[bld_collaboration_memory_scope]] | downstream | 0.23 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.23 |
| [[bld_manifest_memory_type]] | upstream | 0.22 |
| [[memory-scope-builder]] | upstream | 0.22 |
| [[p01_kc_memory_scope]] | upstream | 0.22 |
| [[p12_wf_admin_orchestration]] | downstream | 0.22 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.21 |
