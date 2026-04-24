---
quality: 8.0
quality: 7.6
id: kc_messaging_gateway
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "KC: messaging_gateway"
version: 1.0.0
tags: [knowledge_card, messaging_gateway, p04, hermes_origin, honcho, multi_platform, gateway]
density_score: 0.92
related:
  - p01_kc_supabase_mcp
  - bld_examples_connector
  - bld_sp_manifest_software_project
  - bld_collaboration_webhook
  - p01_kc_webhook
  - webhook-builder
  - p03_ins_path_config
  - bld_memory_path_config
  - p03_sp_webhook_builder
  - atom_03_openai_agents_sdk
updated: "2026-04-22"
---

## Definition
A `messaging_gateway` is a long-lived, bidirectional, multi-platform messaging transport
abstraction. It accepts messages from Telegram, Discord, Slack, WhatsApp, Signal, and Email
simultaneously, routes them through a unified agent pipeline, and delivers replies back to
the originating platform -- all under a single session model with shared memory.

## Origin: HERMES / NousResearch
`messaging_gateway` was assimilated from the HERMES agent framework (NousResearch).
HERMES `gateway/` handles multi-platform dispatch as a single process. The key insight:
platform is transport, not identity. The user is the same peer regardless of whether
they message via Telegram today or Discord tomorrow. CEX captures this with cross-platform
continuity enabled by default.

Related HERMES assimilation: `user_model` (W1.1) implements the Honcho peer/session/collection
pattern that the gateway populates on every turn.

## Honcho Integration
The gateway bridges messaging platforms to the Honcho dialectic loop:
```
Platform message arrives
  |
  +-> gateway routes to session.add_messages([msg])   # P10 session_state
  |
  +-> pre-response: peer.chat(insight_query)          # P10 user_model
  |     -> static insight injected into context
  |
  +-> LLM generates response
  |
  +-> gateway delivers reply to originating platform
  |
  +-> post-response: derive conclusions -> collections # P10 user_model
```

## Stub Contract (DP5)
Decision DP5 (locked 2026-04-18): stub-only. The `messaging_gateway` kind specifies the
INTERFACE, not the implementation. No live Telegram/Discord/Slack code is embedded in the
artifact. Actual credentials and process startup live outside CEX artifacts (`.cex/config/`
and `hermes gateway` CLI).

## Storage
Gateway state is ephemeral -- each message turn produces a `session_state` artifact.
Durable memory lives in `user_model` (cross-session dialectic peer record).
The gateway itself is stateless between turns.

## Boundaries
| messaging_gateway IS | messaging_gateway IS NOT |
|----------------------|--------------------------|
| Long-lived bidirectional multi-platform transport | `webhook` (single-event inbound HTTP callback) |
| Cross-platform continuity (same peer, any transport) | `api_client` (outbound only, request-response) |
| Duplex conversation with memory | `notifier` (one-way broadcast, no conversation) |
| Multi-platform simultaneous | `browser_tool` (web browsing, not messaging) |
| Stub spec (no live impl) | A runtime or deployment (live code lives in hermes CLI) |

## Platform Adapters
| Platform | Transport | Auth | Voice |
|----------|-----------|------|-------|
| Telegram | webhook | bot_token | yes (optional stt_provider) |
| Discord | websocket | bot_token | yes (optional stt_provider) |
| Slack | webhook | oauth | no |
| WhatsApp | webhook | app_password | yes (optional stt_provider) |
| Signal | polling | app_password | yes (optional stt_provider) |
| Email | polling (IMAP) | app_password | no |

## Security Model
- **DM pairing**: users must initiate a DM before commands are accepted (HERMES default)
- **allowed_user_ids**: explicit allowlist; empty = open (dev only)
- **command_approval_list**: specific commands requiring operator approval
- **rate_limit_per_user_per_min**: 30 default; prevents platform abuse bans

## Shared Slash Commands
A key HERMES property: the same `/command` set works on ALL active platforms. The gateway
normalizes platform-specific command syntax to the shared interface before passing to agent.

## Related Kinds
- `user_model` (P10): the peer record populated by gateway turns (Honcho dialectic)
- `session_state` (P10): ephemeral session snapshot from each gateway conversation turn
- `webhook` (P04): single-event inbound HTTP -- simpler, no cross-platform continuity
- `api_client` (P04): outbound REST client -- no inbound, no conversation state
- `notifier` (P04): outbound-only broadcast -- complements gateway for push notifications
- `stt_provider` (P04): voice memo transcription adapter for voice-capable platforms
- `voice_pipeline` (P04): full voice pipeline -- gateway can use this for voice turns

## Builder
`archetypes/builders/messaging-gateway-builder/`

## Upstream Sources
- NousResearch/hermes-agent: `gateway/` directory -- multi-platform dispatch process
- plastic-labs/honcho: peer/session/collection model wired into gateway turn loop

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_mcp]] | sibling | 0.25 |
| [[bld_examples_connector]] | downstream | 0.21 |
| [[bld_sp_manifest_software_project]] | downstream | 0.21 |
| [[bld_collaboration_webhook]] | downstream | 0.20 |
| [[p01_kc_webhook]] | sibling | 0.20 |
| [[webhook-builder]] | downstream | 0.20 |
| [[p03_ins_path_config]] | downstream | 0.19 |
| [[bld_memory_path_config]] | downstream | 0.19 |
| [[p03_sp_webhook_builder]] | downstream | 0.19 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.18 |
