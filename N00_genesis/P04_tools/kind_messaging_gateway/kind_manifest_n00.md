---
quality: 8.0
quality: 7.6
id: n00_messaging_gateway_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "Messaging Gateway -- Canonical Manifest"
version: 1.0.0
tags: [manifest, messaging_gateway, p04, n00, archetype, template, hermes_origin]
density_score: 0.92
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_action_paradigm
  - bld_schema_benchmark_suite
  - bld_schema_tts_provider
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+webhook+api_client F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A messaging_gateway is a long-lived, bidirectional, multi-platform messaging transport
abstraction. It manages simultaneous connections to Telegram, Discord, Slack, WhatsApp,
Signal, and Email under a unified session model -- routing inbound messages from any
platform to a single agent, and routing agent replies back to the originating platform.
Cross-platform conversation continuity is the defining property: the same peer_id, the
same memory, the same context -- regardless of which app the human picked up today.

The output is a stub specification (HERMES DP5: no live impl) defining the platform
credentials schema, auth model, security posture (DM pairing, command approval, allowlists),
shared slash-command surface, and optional voice memo transcription adapter.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (p04_mg_{platform}) | yes | Unique artifact identifier |
| kind | literal "messaging_gateway" | yes | Type integrity |
| pillar | literal "P04" | yes | Pillar assignment |
| title | string | yes | Human-readable gateway name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| platforms_supported | list[string] | yes | Full platform enum supported |
| active_platforms | list[string] | yes | Subset actually configured |
| transport.protocol | enum | yes | websocket, webhook, or polling |
| transport.auth_type | enum | yes | bot_token, oauth, app_password |
| security.dm_pairing | bool | yes | Require DM pairing before commands |
| security.allowed_user_ids | list | yes | Allowlist; empty = open (dev only) |
| features.cross_platform_continuity | bool | yes | Shared session_id across platforms |
| features.shared_slash_commands | bool | yes | Same /commands on all platforms |
| features.voice_memo_transcription | bool | no | Requires stt_provider integration |

## When to use
- When an agent must receive commands from multiple messaging platforms simultaneously
- When cross-platform conversation continuity is needed (same memory, different transport)
- When HERMES-pattern gateway configuration is being specified for a deployment

## Builder
`archetypes/builders/messaging-gateway-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind messaging_gateway --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context
- `{{PLATFORM}}` -- primary platform slug (telegram, discord, slack, etc.)

## Example (minimal stub)
```yaml
---
id: p04_mg_telegram
kind: messaging_gateway
pillar: P04
nucleus: n05
title: "Messaging Gateway: Telegram"
version: 1.0.0
quality: null
platforms_supported: [telegram, discord, slack]
active_platforms: [telegram]
transport:
  protocol: webhook
  auth_type: bot_token
security:
  dm_pairing: true
  command_approval_list: []
  allowed_user_ids: []
  rate_limit_per_user_per_min: 30
features:
  voice_memo_transcription: false
  cross_platform_continuity: true
  shared_slash_commands: true
tags: [messaging_gateway, telegram, hermes_origin, stub, p04]
---
```

## Related kinds
- `webhook` (P04) -- single-event inbound HTTP; messaging_gateway is long-lived bidirectional
- `api_client` (P04) -- outbound only; messaging_gateway is duplex
- `notifier` (P04) -- one-way broadcast; messaging_gateway has conversation
- `browser_tool` (P04) -- web browsing; messaging_gateway is messaging transport
- `stt_provider` (P04) -- voice transcription provider plugged into gateway voice_memo feature
- `session_state` (P10) -- ephemeral session data produced by gateway interactions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_schema_sandbox_spec]] | downstream | 0.37 |
| [[bld_schema_quickstart_guide]] | downstream | 0.37 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_action_paradigm]] | downstream | 0.37 |
| [[bld_schema_benchmark_suite]] | downstream | 0.37 |
| [[bld_schema_tts_provider]] | downstream | 0.37 |
