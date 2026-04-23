---
id: n00_curation_nudge_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Curation Nudge -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, curation_nudge, p11, n00, archetype, template, hermes]
density_score: 1.0
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_optimizer
  - bld_schema_bugloop
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A curation_nudge is a proactive in-session self-prompt that asks an agent whether it
should persist a piece of observed knowledge to durable memory (MEMORY.md, entity_memory,
or knowledge_card). It fires when a configurable trigger threshold is reached (turn count,
information density, tool-call count, or user correction). Unlike a guardrail (blocks action),
a quality_gate (pass/fail), or a notifier (external broadcast), a nudge ASKS -- it is
informational and confirmatory.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier (pattern: cn_{{trigger}}) |
| kind | string | yes | Always `curation_nudge` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| trigger.type | enum | yes | turn_count \| density_threshold \| tool_call_count \| user_correction |
| trigger.threshold | integer | yes | Count at which nudge fires (default: 10) |
| cadence.min_interval_turns | integer | yes | Minimum turns between consecutive nudges |
| cadence.max_per_session | integer | yes | Max nudges allowed per session |
| prompt_template | string | yes | Message shown to the agent (must contain {{observation}}) |
| target_memory.destination | enum | yes | MEMORY.md \| entity_memory \| knowledge_card |
| target_memory.auto_write_if_confirmed | boolean | yes | Auto-persist on agent confirmation |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |

## When to use
- When configuring periodic memory-persistence reminders for an agent session
- When preventing knowledge loss at context-window boundaries
- When building HERMES-style agent-curated memory pipelines (Honcho pattern)
- When bridging in-session observation to durable MEMORY.md entries

## Builder
`archetypes/builders/curation-nudge-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind curation_nudge --execute`

## Template variables (open for instantiation)
- `{{trigger}}` -- trigger type slug (e.g., turn_count, density_threshold)
- `{{threshold}}` -- numeric trigger threshold
- `{{observation}}` -- the observation the agent is prompted to persist
- `{{destination}}` -- target memory destination

## Example (minimal)
```yaml
---
id: cn_turn_count
kind: curation_nudge
pillar: P11
nucleus: n04
title: "Curation Nudge: Every 10 Turns"
trigger:
  type: turn_count
  threshold: 10
cadence:
  min_interval_turns: 5
  max_per_session: 3
prompt_template: "Notei {{observation}}. Devo persistir em MEMORY.md?"
target_memory:
  destination: MEMORY.md
  auto_write_if_confirmed: true
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory]
---
```

## Related kinds
- `guardrail` (P11) -- blocks action; nudge ASKS (different semantics)
- `quality_gate` (P11) -- pass/fail check; nudge is informational
- `notifier` (P04) -- external broadcast; nudge is in-session only
- `entity_memory` (P10) -- destination for confirmed nudges
- `memory_summary` (P10) -- companion: compress accumulated knowledge
- `user_model` (P10) -- HERMES Honcho pattern that nudges feed into

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_sandbox_spec]] | upstream | 0.38 |
| [[bld_schema_integration_guide]] | upstream | 0.38 |
| [[bld_schema_optimizer]] | upstream | 0.38 |
| [[bld_schema_bugloop]] | related | 0.38 |
| [[bld_schema_sandbox_config]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_quickstart_guide]] | upstream | 0.37 |
| [[bld_schema_search_strategy]] | upstream | 0.37 |
