---
kind: schema
id: bld_schema_messaging_gateway
pillar: P04
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for messaging_gateway
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, schema, p04, hermes_origin]
tldr: "messaging_gateway schema: platforms + transport + security + features. Max 4096 bytes. Stub only (DP5). ID: p04_mg_{platform}."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_config
  - bld_schema_pitch_deck
  - bld_schema_sandbox_spec
---

# Schema: messaging_gateway

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_mg_{slug}) | YES | - | Namespace compliance |
| kind | literal "messaging_gateway" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable gateway name |
| platforms_supported | list[string] | YES | - | Full platform enum this gateway supports |
| active_platforms | list[string] | YES | - | Subset currently configured and active |
| transport.protocol | enum | YES | - | websocket, webhook, or polling |
| transport.auth_type | enum | YES | - | bot_token, oauth, or app_password |
| security.dm_pairing | bool | YES | true | Require DM pairing before commands |
| security.command_approval_list | list[string] | YES | [] | Commands needing explicit approval |
| security.allowed_user_ids | list[string] | YES | [] | Allowlist; empty = open (dev only) |
| security.rate_limit_per_user_per_min | int | YES | 30 | Per-user rate limit |
| features.voice_memo_transcription | bool | YES | false | Requires stt_provider |
| features.cross_platform_continuity | bool | YES | true | Shared session_id across platforms |
| features.shared_slash_commands | bool | YES | true | Unified /commands on all platforms |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "messaging_gateway" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern
Regex: `^p04_mg_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
Primary slug = primary active platform (e.g., `telegram`, `discord`, `all`).

## Platform Enum
Valid values for platforms_supported and active_platforms:
`[telegram, discord, slack, whatsapp, signal, email]`

## Transport Enum
| Field | Valid Values |
|-------|-------------|
| transport.protocol | websocket, webhook, polling |
| transport.auth_type | bot_token, oauth, app_password |

## Platform-Transport Matrix (HERMES defaults)
| Platform | Protocol | Auth |
|----------|----------|------|
| telegram | webhook | bot_token |
| discord | websocket | bot_token |
| slack | webhook | oauth |
| whatsapp | webhook | app_password |
| signal | polling | app_password |
| email | polling | app_password |

## Body Structure (required sections)
1. `## Overview` -- what platforms this gateway covers, deployment context
2. `## Platform Configuration` -- table: Platform | Status | Transport | Auth
3. `## Security` -- table: Control | Value | Notes
4. `## Features` -- table: Feature | Status | Dependency
5. `## Shared Slash Commands` -- table: Command | Description (at least /help, /status, /reset)
6. `## Integration Points` -- links to user_model, session_state, stt_provider, agent_profile
7. `## Stub Notice` -- DP5 declaration and activation path

## Constraints
- max_bytes: 4096 (stub spec -- not an implementation doc)
- naming: p04_mg_{platform}.yaml (one file per primary platform or "all")
- machine_format: yaml (compiled artifact)
- id == filename stem
- active_platforms MUST be a non-empty subset of platforms_supported
- transport MUST be declared (no implicit defaults)
- quality: null always
- STUB ONLY: no live platform credentials or connection code in artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.58 |
| [[bld_schema_reranker_config]] | sibling | 0.57 |
| [[bld_schema_quickstart_guide]] | sibling | 0.57 |
| [[bld_schema_integration_guide]] | sibling | 0.56 |
| [[bld_schema_dataset_card]] | sibling | 0.56 |
| [[bld_schema_search_strategy]] | sibling | 0.56 |
| [[bld_schema_benchmark_suite]] | sibling | 0.55 |
| [[bld_schema_sandbox_config]] | sibling | 0.55 |
| [[bld_schema_pitch_deck]] | sibling | 0.55 |
| [[bld_schema_sandbox_spec]] | sibling | 0.55 |
