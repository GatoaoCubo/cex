---
quality: 8.4
quality: 8.0
kind: config
id: bld_config_messaging_gateway
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration knobs for messaging_gateway artifacts
pattern: Override defaults at build time or deployment time
title: "Config: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, config, p09, hermes_origin]
tldr: "Config knobs: active_platforms, rate_limit, dm_pairing, voice toggle, command approvals. External credentials stay in .cex/config/ not in artifact."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.89
related:
  - bld_schema_model_card
  - bld_architecture_social_publisher
  - ex_env_config_default
  - bld_knowledge_card_notifier
  - p03_sp_social_publisher_builder
  - bld_collaboration_oauth_app_config
  - n02_tool_social_publisher
  - bld_schema_model_provider
  - bld_collaboration_retriever_config
  - bld_output_template_path_config
---

# Config: messaging_gateway

## Build-Time Overrides (safe to embed in artifact)
| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| active_platforms | [telegram] | subset of platforms_supported | Which platforms to activate |
| transport.protocol | webhook | websocket, webhook, polling | Per-platform protocol |
| transport.auth_type | bot_token | bot_token, oauth, app_password | Per-platform auth |
| security.dm_pairing | true | bool | Always true for production |
| security.rate_limit_per_user_per_min | 30 | 1-300 | Platform ban threshold: Telegram ~100 |
| security.command_approval_list | [] | list[string] | Privileged /commands |
| security.allowed_user_ids | [] | list[string] | Empty = open (dev only) |
| features.voice_memo_transcription | false | bool | Requires stt_provider configured |
| features.cross_platform_continuity | true | bool | HERMES default -- do not disable |
| features.shared_slash_commands | true | bool | HERMES default -- do not disable |

## Runtime Config (external, NOT in artifact)
These values are set in `.cex/config/gateway_{platform}.yaml` and are NEVER
embedded in messaging_gateway artifacts (DP5 stub contract):
| Parameter | Location | Notes |
|-----------|----------|-------|
| TELEGRAM_BOT_TOKEN | .cex/config/gateway_telegram.yaml | Rotate via BotFather |
| DISCORD_BOT_TOKEN | .cex/config/gateway_discord.yaml | Discord dev portal |
| SLACK_APP_TOKEN | .cex/config/gateway_slack.yaml | OAuth scopes: chat:write |
| WHATSAPP_APP_PASSWORD | .cex/config/gateway_whatsapp.yaml | Meta Business API |
| SIGNAL_APP_PASSWORD | .cex/config/gateway_signal.yaml | signal-cli registration |
| EMAIL_APP_PASSWORD | .cex/config/gateway_email.yaml | App-specific password (Gmail/Outlook) |

## Platform-Specific Rate Limits (reference)
| Platform | Safe Max req/min | Notes |
|----------|-----------------|-------|
| Telegram | 30 messages/sec per bot | 1 msg/sec per chat |
| Discord | 50 req/sec global | 5 per 5s per channel |
| Slack | 1 msg/sec per channel | Burst: 20/min |
| WhatsApp | 80/min business | Per message tier |
| Signal | No published limit | Be conservative: 10/min |
| Email | 100/day for SMTP | Depends on provider |

## Mirror-Overridable Fields
These fields can be overridden by nucleus-specific mirrors (Wave 3 scope):
- `security.allowed_user_ids` -- N06 commercial may lock to paying customers
- `features.voice_memo_transcription` -- N01 intelligence may enable for research
- `security.rate_limit_per_user_per_min` -- N02 marketing may relax for campaigns

## Forbidden Overrides
Mirror nuclei MUST NOT change:
- `kind` (always messaging_gateway)
- `pillar` (always P04)
- frontmatter schema structure
- DP5 stub contract (no live code in any mirror)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_card]] | upstream | 0.21 |
| [[bld_architecture_social_publisher]] | upstream | 0.18 |
| [[ex_env_config_default]] | related | 0.18 |
| [[bld_knowledge_card_notifier]] | upstream | 0.18 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.17 |
| [[bld_collaboration_oauth_app_config]] | downstream | 0.17 |
| [[n02_tool_social_publisher]] | upstream | 0.17 |
| [[bld_schema_model_provider]] | upstream | 0.17 |
| [[bld_collaboration_retriever_config]] | downstream | 0.17 |
| [[bld_output_template_path_config]] | upstream | 0.16 |
