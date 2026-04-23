---
kind: architecture
id: bld_architecture_messaging_gateway
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of messaging_gateway -- inventory, dependencies, and architectural position
quality: 8.8
title: "Architecture: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, architecture, p04, hermes_origin]
tldr: "Component inventory: platform adapters + transport layer + security + feature flags + Honcho wiring. Sits in P04 tools layer between external platforms and agent pipeline."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_architecture_social_publisher
  - bld_collaboration_transport_config
  - p01_kc_supabase_mcp
  - p03_sp_integration_guide_builder
  - integration-guide-builder
  - p03_ins_path_config
  - bld_architecture_session_state
  - bld_memory_path_config
  - atom_03_openai_agents_sdk
  - bld_sp_manifest_software_project
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| platforms_supported | Full platform enum the gateway knows about | messaging_gateway | required |
| active_platforms | Subset with credentials configured | messaging_gateway | required |
| transport.protocol | websocket/webhook/polling per platform | messaging_gateway | required |
| transport.auth_type | bot_token/oauth/app_password per platform | messaging_gateway | required |
| security.dm_pairing | Require DM initiation before commands | messaging_gateway | required |
| security.allowed_user_ids | Explicit user allowlist | messaging_gateway | required |
| security.rate_limit_per_user_per_min | Per-user rate cap | messaging_gateway | required |
| security.command_approval_list | Commands needing operator approval | messaging_gateway | required |
| features.cross_platform_continuity | Shared session_id across platforms | messaging_gateway | required |
| features.shared_slash_commands | Same /cmd set on all platforms | messaging_gateway | required |
| features.voice_memo_transcription | Voice memo -> text via stt_provider | messaging_gateway | required |
| stt_provider | Voice transcription backend (P04) | P04 runtime | consumer |
| user_model | Cross-session peer record populated by turns (P10) | P10 runtime | consumer |
| session_state | Ephemeral session snapshot per turn (P10) | P10 runtime | consumer |
| agent_profile | The agent this gateway routes to (P08) | P08 | consumer |

## Dependency Graph
```
Platform message (Telegram/Discord/Slack/...)
  |
  +-> transport adapter (webhook/websocket/polling)
  |     -> validates auth (bot_token/oauth/app_password)
  |     -> checks security.dm_pairing (is user paired?)
  |     -> checks security.allowed_user_ids (is user allowed?)
  |     -> enforces rate_limit_per_user_per_min
  |
  +-> [voice memo path] -> stt_provider -> text_message
  |
  +-> normalized message -> agent pipeline
  |     -> session.add_messages([msg]) -> session_state (P10)
  |     -> pre-response peer.chat() -> user_model (P10)
  |     -> LLM generation
  |     -> post-response derive -> user_model (P10)
  |
  +-> reply -> transport adapter -> originating platform
```

## Boundary Table
| messaging_gateway IS | messaging_gateway IS NOT |
|----------------------|--------------------------|
| Long-lived bidirectional multi-platform transport | `webhook` (single HTTP event callback) |
| Cross-platform continuity (same peer, any transport) | `api_client` (outbound REST, no conversation) |
| Security gateway (DM pairing, allowlists, rate limits) | `notifier` (one-way broadcast, no conversation) |
| Stub spec (DP5) -- interface, not implementation | A running process (that is hermes gateway CLI) |
| Platform normalizer -> unified agent pipeline | `browser_tool` (web browsing automation) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| adapter | platforms_supported, active_platforms, transport | Platform connection config |
| security | dm_pairing, allowed_user_ids, rate_limit, command_approval_list | Access control |
| features | cross_platform_continuity, shared_slash_commands, voice_memo_transcription | Capability flags |
| integration | user_model, session_state, stt_provider, agent_profile | Runtime wiring |
| stub | DP5 contract, activation path | Deployment boundary |

## HERMES Gateway Architecture (end-to-end)
```
[Telegram]  [Discord]  [Slack]  [WhatsApp]  [Signal]  [Email]
    |            |         |         |            |        |
    +------------+---------+---------+------------+--------+
                           |
                     gateway process
                     (hermes gateway start)
                           |
                  +--------+--------+
                  |                 |
             security            routing
             (dm_pairing,        (platform -> agent)
              allowlist,
              rate_limit)
                  |
           unified agent call
           (same agent, same memory, any platform)
                  |
         Honcho dialectic loop
         (user_model P10 + session_state P10)
```

## Stub Notice (DP5)
This architecture document describes the INTERFACE. The HERMES process that
implements it is started with `hermes gateway setup && hermes gateway start`.
CEX artifacts specify WHAT; HERMES CLI does HOW.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_social_publisher]] | sibling | 0.20 |
| [[bld_collaboration_transport_config]] | downstream | 0.20 |
| [[p01_kc_supabase_mcp]] | upstream | 0.19 |
| [[p03_sp_integration_guide_builder]] | upstream | 0.18 |
| [[integration-guide-builder]] | upstream | 0.18 |
| [[p03_ins_path_config]] | upstream | 0.18 |
| [[bld_architecture_session_state]] | sibling | 0.17 |
| [[bld_memory_path_config]] | downstream | 0.17 |
| [[atom_03_openai_agents_sdk]] | upstream | 0.17 |
| [[bld_sp_manifest_software_project]] | upstream | 0.16 |
