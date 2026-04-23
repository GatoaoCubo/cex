---
quality: 8.9
quality: 8.2
kind: schema
id: bld_schema_user_model
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for user_model
pattern: TEMPLATE derives from this. CONFIG restricts this.
title: "Schema: user_model"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, schema, honcho, P10]
tldr: "Formal field spec for user_model: peer_id, workspace, storage, dialectic config, collections, retention, API surface."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_sandbox_spec
  - bld_schema_context_window_config
---

# Schema: user_model

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (um_{{peer_id}}) | YES | - | Namespace compliance |
| kind | literal "user_model" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| title | string | YES | - | Human-readable peer label |
| peer_id | string | YES | - | Canonical peer identifier (workspace-scoped) |
| workspace | string | YES | "default" | Tenant namespace |
| storage.primary | enum | YES | "sqlite" | sqlite, pgvector, turbopuffer, lancedb |
| storage.fallback_chain | list[string] | YES | [sqlite, turbopuffer, lancedb] | Ordered fallback backends |
| storage.pgvector_enabled | bool | YES | false | Enable pgvector for vector search |
| dialectic.pre_response_insight | bool | YES | true | Query user model before generating |
| dialectic.post_response_derive | bool | YES | true | Write derived facts back after response |
| dialectic.compaction_cadence_turns | int | YES | 50 | Turns between collection compaction |
| collections | list[{name: string}] | YES | - | Named fact groups |
| retention.messages_ttl_days | int | YES | 365 | Message retention in days |
| retention.derived_facts_ttl_days | int\|null | YES | null | null = never purge derived facts |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "user_model" and "honcho" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| description | string <= 200ch | REC | - | What peer this model tracks |

## ID Pattern
Regex: `^um_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Peer Profile` -- who this peer is, workspace context, scope
2. `## Collections` -- subsections per collection with Key/Value/Confidence/LastUpdated tables
3. `## Dialectic Loop Status` -- phase, status, last_run table
4. `## API Surface` -- all 5 methods: peer.chat, session.context, session.add_messages, search, session.representation
5. `## Update History` -- version entries table

## Constraints
- max_bytes: 4096 (derived fact model, not a transcript)
- naming: `p10_um_{{peer_id}}.md`
- machine_format: yaml (compiled artifact)
- id == filename stem
- collections list MUST be non-empty (>= 3 named collections)
- storage.primary MUST be one of declared enum values
- dialectic.compaction_cadence_turns MUST be a positive integer
- quality: null always
- NO raw message content in body -- derived insights only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_benchmark_suite]] | sibling | 0.66 |
| [[bld_schema_search_strategy]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_pitch_deck]] | sibling | 0.65 |
| [[bld_schema_sandbox_spec]] | sibling | 0.64 |
| [[bld_schema_context_window_config]] | sibling | 0.64 |
