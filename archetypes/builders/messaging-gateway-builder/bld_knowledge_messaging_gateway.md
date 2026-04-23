---
kind: knowledge_card
id: bld_kc_messaging_gateway
pillar: P01
llm_function: INJECT
purpose: Linked KC for messaging_gateway builder -- injected at F3 INJECT
quality: 8.7
title: "KC Link: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, knowledge_card, p01, hermes_origin]
tldr: "Builder-linked KC: messaging_gateway is the HERMES multi-platform transport stub. Boundaries vs webhook/api_client/notifier. Honcho wiring via user_model."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_collaboration_webhook
  - bld_architecture_kind
  - bld_collaboration_builder
  - kind-builder
  - bld_collaboration_notifier
  - bld_collaboration_kind
  - bld_collaboration_retriever
  - bld_collaboration_quality_gate
  - bld_collaboration_model_provider
  - bld_collaboration_streaming_config
---

# KC Link: messaging_gateway Builder

## What This Builder Produces
`messaging_gateway` artifacts (P04) -- stub specifications for HERMES multi-platform
messaging transport. Defines the interface by which an agent receives and sends messages
across Telegram, Discord, Slack, WhatsApp, Signal, and Email simultaneously.

## Canonical KC
Full knowledge card: `N00_genesis/P01_knowledge/library/kind/kc_messaging_gateway.md`
Read it at F3 INJECT before producing any messaging_gateway artifact.

## Critical Facts for Builders
1. **DP5 stub contract**: artifact is interface spec -- no live credentials, no connection code
2. **Cross-platform continuity**: same peer_id across all platforms (HERMES default, do not disable)
3. **DM pairing required**: security.dm_pairing: true for all production stubs
4. **Platform-Transport matrix**: see schema -- Telegram=webhook, Discord=websocket, Signal=polling
5. **Honcho wiring**: gateway populates user_model (P10) on every turn via session.add_messages

## Boundary Quick-Reference
| If user wants... | Route to... |
|-----------------|-------------|
| Single inbound HTTP event | webhook-builder |
| Outbound REST calls | api-client-builder |
| One-way notifications | notifier-builder |
| Voice processing only | stt-provider-builder |
| User memory across sessions | user-model-builder |
| Multi-platform messaging gateway | messaging-gateway-builder (this builder) |

## Quality Floor
Minimum acceptable messaging_gateway artifact:
- id: `p04_mg_{platform}` (namespace compliance)
- platforms_supported non-empty
- active_platforms non-empty subset
- transport fully declared
- security.dm_pairing declared
- All 7 body sections present
- quality: null
- Score >= 9.0 before commit

## Related KCs
- `kc_webhook.md` -- single HTTP event inbound callback pattern
- `kc_api_client.md` -- outbound REST client pattern
- `kc_user_model.md` -- Honcho peer record populated by gateway turns (P10)
- `kc_session_state.md` -- ephemeral session data from gateway turns (P10)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_webhook]] | downstream | 0.30 |
| [[bld_architecture_kind]] | downstream | 0.27 |
| [[bld_collaboration_builder]] | downstream | 0.25 |
| [[kind-builder]] | downstream | 0.25 |
| [[bld_collaboration_notifier]] | downstream | 0.23 |
| [[bld_collaboration_kind]] | downstream | 0.23 |
| [[bld_collaboration_retriever]] | downstream | 0.22 |
| [[bld_collaboration_quality_gate]] | downstream | 0.22 |
| [[bld_collaboration_model_provider]] | downstream | 0.21 |
| [[bld_collaboration_streaming_config]] | downstream | 0.21 |
