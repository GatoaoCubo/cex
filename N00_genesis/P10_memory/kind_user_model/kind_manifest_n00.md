---
quality: 8.0
quality: 7.6
id: n00_user_model_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "User Model -- Canonical Manifest"
version: 1.0.0
tags: [manifest, user_model, p10, n00, archetype, template, honcho, dialectic]
density_score: 0.92
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_multimodal_prompt
  - bld_schema_playground_config
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_app_directory_entry
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P10 F2=user-model-builder F3=kc_hermes+honcho+spec_hermes F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A user_model stores a cross-session dialectic representation of a single human peer --
their preferences, working style, inferred intent, and accumulated context. It implements
the Honcho dialectic pattern (plastic-labs/honcho): per-turn insight generation written
back to a durable Collection so agents can query the user's mental model via NL at any time.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique peer identifier (`um_{{peer_id}}`) |
| kind | string | yes | Always `user_model` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable peer name |
| peer_id | string | yes | Canonical peer identifier (workspace-scoped) |
| workspace | string | yes | Tenant namespace for multi-tenancy isolation |
| storage.primary | enum | yes | `sqlite` (default), `pgvector`, `turbopuffer`, `lancedb` |
| storage.fallback_chain | list | yes | Ordered fallback: [sqlite, turbopuffer, lancedb] |
| dialectic.pre_response_insight | bool | yes | Query user model before generating response |
| dialectic.post_response_derive | bool | yes | Write derived conclusions back after response |
| dialectic.compaction_cadence_turns | int | yes | How many turns between Collection compaction |
| collections | list | yes | Named fact groups: preferences, working_style, context_history |
| retention.messages_ttl_days | int | yes | Message retention in days (default 365) |
| retention.derived_facts_ttl_days | int\|null | yes | null = keep derived facts forever |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | null until peer-reviewed |

## When to use
- When an agent must adapt its behavior across sessions based on learned user preferences
- When building personalized copilots that remember working style, communication preferences, and domain context
- When implementing the Honcho dialectic loop: pre-response insight injection + post-response fact derivation

## Builder
`archetypes/builders/user-model-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind user_model --execute`

## Template variables (open for instantiation)
- `{{peer_id}}` -- unique identifier for this user/peer
- `{{workspace_id}}` -- tenant namespace
- `{{NUCLEUS_ROLE}}` -- which nucleus owns this peer record
- `{{SIN_LENS}}` -- cultural DNA driving adaptation behavior

## Example (minimal)
```yaml
---
id: um_gato3_main
kind: user_model
pillar: P10
peer_id: gato3
workspace: cex_default
storage:
  primary: sqlite
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: false
dialectic:
  pre_response_insight: true
  post_response_derive: true
  compaction_cadence_turns: 50
collections:
  - name: preferences
  - name: working_style
  - name: context_history
retention:
  messages_ttl_days: 365
  derived_facts_ttl_days: null
version: 1.0.0
quality: null
tags: [user_model, honcho, dialectic, P10]
---
```

## Related kinds
- `entity_memory` (P10) -- any named entity; user_model is THE HUMAN specifically
- `session_state` (P10) -- single session snapshot; user_model is cross-session
- `memory_architecture` (P10) -- the whole memory stack; user_model is one layer
- `agent_profile` (P08) -- describes the AI agent; user_model describes the HUMAN
- `episodic_memory` (P10) -- event log; user_model is derived facts about the person

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.52 |
| [[bld_schema_integration_guide]] | upstream | 0.51 |
| [[bld_schema_usage_report]] | upstream | 0.50 |
| [[bld_schema_benchmark_suite]] | upstream | 0.49 |
| [[bld_schema_sandbox_spec]] | upstream | 0.48 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.48 |
| [[bld_schema_playground_config]] | upstream | 0.48 |
| [[bld_schema_quickstart_guide]] | upstream | 0.47 |
| [[bld_schema_dataset_card]] | upstream | 0.47 |
| [[bld_schema_app_directory_entry]] | upstream | 0.47 |
