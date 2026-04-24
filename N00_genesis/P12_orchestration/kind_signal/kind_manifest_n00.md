---
id: n00_signal_manifest
kind: knowledge_card
8f: F3_inject
pillar: P12
nucleus: n00
title: "Signal -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, signal, p12, n00, archetype, template]
density_score: 1.0
related:
  - p12_sig_admin_orchestration
  - signal-builder
  - bld_collaboration_signal
  - bld_schema_reward_signal
  - p12_sig_builder_nucleus
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_nucleus_def
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A signal is an inter-agent communication message that notifies N07 or other nuclei of a state change -- task completion, error, or progress update. It is the lightweight coordination primitive that enables the autonomous lifecycle loop: N07 watches for signals to know when to consolidate, advance waves, or trigger escalation without polling or blocking.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `signal` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| signal_type | enum | yes | complete \| error \| progress \| warning \| heartbeat |
| emitter_nucleus | string | yes | Nucleus that sent this signal |
| mission | string | yes | Mission or wave this signal belongs to |
| quality_score | float | no | Quality score of produced artifact (for complete signals) |
| artifact_refs | array | no | Artifacts produced by the signaling nucleus |
| error_message | string | no | Error description (for error signals) |
| emitted_at | datetime | yes | Signal emission timestamp |

## When to use
- When a nucleus completes its F8 COLLABORATE step (mandatory signal)
- When N07 needs to detect wave completion without blocking on a process
- When building event-driven orchestration pipelines that react to nucleus state changes

## Builder
`archetypes/builders/signal-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind signal --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: signal_n03_complete_wave2
kind: signal
pillar: P12
nucleus: n03
title: "Example Signal"
version: 1.0
quality: null
---
# Signal: N03 Wave 2 Complete
signal_type: complete
emitter_nucleus: n03
mission: FRACTAL_FILL_W2
quality_score: 9.1
artifact_refs: [agent_card_n05, agent_card_n06]
emitted_at: "2026-04-17T15:22:00Z"
```

## Related kinds
- `handoff` (P12) -- handoff that specifies which signal the nucleus should emit
- `spawn_config` (P12) -- spawn configuration that monitors for this signal
- `runtime_state` (P10) -- N07 runtime state updated when this signal is received

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_sig_admin_orchestration]] | related | 0.42 |
| [[signal-builder]] | related | 0.42 |
| [[bld_collaboration_signal]] | related | 0.40 |
| [[bld_schema_reward_signal]] | upstream | 0.40 |
| [[p12_sig_builder_nucleus]] | related | 0.39 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.38 |
| [[bld_schema_dataset_card]] | upstream | 0.38 |
| [[bld_schema_nucleus_def]] | upstream | 0.38 |
| [[bld_schema_benchmark_suite]] | upstream | 0.37 |
