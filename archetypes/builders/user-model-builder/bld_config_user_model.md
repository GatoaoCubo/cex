---
quality: 8.4
quality: 8.0
kind: config
id: bld_config_user_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for user_model
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
title: "Config: user_model Production Rules"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, config, P09]
tldr: "Naming, paths, size limits, storage enum, collection rules, compaction constraints for user_model artifacts."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_config_constraint_spec
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_config_hook_config
  - bld_config_chunk_strategy
  - bld_config_checkpoint
  - bld_config_kind
---

# Config: user_model Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_um_{peer_id}.md` | `p10_um_gato3_main.md` |
| Builder directory | kebab-case | `user-model-builder/` |
| Frontmatter fields | snake_case | `peer_id`, `workspace`, `compaction_cadence_turns` |
| Peer slug | snake_case, lowercase, no hyphens | `gato3_main`, `alice_smith`, `support_user_42` |
| Collection names | snake_case, lowercase | `preferences`, `working_style`, `context_history` |
| Workspace names | snake_case, lowercase | `cex_default`, `support_prod`, `dev_local` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: nucleus P10 dir or `N00_genesis/P10_memory/examples/p10_um_{peer_id}.md`
- Template: `N00_genesis/P10_memory/tpl_user_model.md`
- Compiled: same dir `/compiled/p10_um_{peer_id}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~6000 bytes
- Density: >= 0.85 (no filler)

## Storage Backend Enum
| Value | Default | When to use |
|-------|---------|-------------|
| sqlite | YES | Local dev, single-node, no vector search needed |
| pgvector | no | Production, Postgres infra, vector similarity at scale |
| turbopuffer | no | Serverless vector, fallback-2 |
| lancedb | no | Embedded, edge deployments, fallback-3 |
Rule: fallback_chain MUST be a list ordered by preference. SQLite must appear in chain.

## Collections Rules
| Rule | Constraint |
|------|-----------|
| Minimum collections | 3 (preferences + working_style + context_history or equivalent) |
| Collection name | snake_case, <= 30 chars |
| Custom collections | Allowed; name must match domain need |
| Max collections | No hard limit; > 7 suggests consolidation |

## Dialectic Config
| Field | Default | Constraint |
|-------|---------|-----------|
| pre_response_insight | true | SHOULD be true for personalization |
| post_response_derive | true | SHOULD be true for learning |
| compaction_cadence_turns | 50 | MUST be positive integer; lower = more frequent (costlier) |

## Retention Conventions
| Field | Default | Meaning |
|-------|---------|---------|
| messages_ttl_days | 365 | Purge raw messages after N days |
| derived_facts_ttl_days | null | null = keep derived facts forever |
Note: GDPR-sensitive deployments should set derived_facts_ttl_days <= 730.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_constraint_spec]] | sibling | 0.33 |
| [[bld_config_memory_scope]] | sibling | 0.32 |
| [[bld_config_retriever_config]] | sibling | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_config_output_validator]] | sibling | 0.30 |
| [[bld_config_handoff_protocol]] | sibling | 0.29 |
| [[bld_config_hook_config]] | sibling | 0.28 |
| [[bld_config_chunk_strategy]] | sibling | 0.28 |
| [[bld_config_checkpoint]] | sibling | 0.27 |
| [[bld_config_kind]] | sibling | 0.27 |
