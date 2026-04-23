---
id: p04_mg_{{platform}}
kind: messaging_gateway
pillar: P04
nucleus: n05
title: "Messaging Gateway: {{platform}}"
version: 1.0.0
quality: null
platforms_supported: [telegram, discord, slack, whatsapp, signal, email]
active_platforms: ["{{platform}}"]
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
tags: [messaging_gateway, "{{platform}}", hermes_origin, stub, p04]
density_score: 1.0
updated: "2026-04-22"
---

## Overview

{{platform}} gateway stub for the HERMES multi-platform messaging architecture.
Defines the transport configuration, security posture, and feature flags for this
platform adapter. Part of a unified gateway that routes all platforms to the same
agent and memory layer, ensuring cross-platform continuity via a shared peer_id.

## Platform Compatibility Matrix

| Platform | Transport | Auth method | Bot API | Slash commands | Voice memo | File sharing | Threads |
|----------|-----------|------------|---------|----------------|------------|-------------|---------|
| Telegram | webhook / long-poll | bot_token | BotFather API | yes (native) | yes (ogg) | yes | yes |
| Discord | webhook / gateway WS | bot_token | Discord API v10 | yes (native) | no | yes | yes |
| Slack | webhook / Events API | oauth / bot_token | Slack Web API | yes (native) | no | yes | yes |
| WhatsApp | webhook | api_token | WhatsApp Business API | no (menu-based) | yes (ogg) | yes | no |
| Signal | webhook / REST | uuid + key | Signal REST API | no (prefix-based) | yes | yes | no |
| Email | IMAP/SMTP | oauth / app_password | provider-specific | no (subject-based) | no | yes (attach) | yes (threading) |

### Platform-Specific Configuration

```yaml
# Telegram
telegram:
  bot_token: "{{TELEGRAM_BOT_TOKEN}}"
  webhook_url: "https://{{DOMAIN}}/webhook/telegram"
  parse_mode: MarkdownV2
  allowed_updates: [message, callback_query, inline_query]

# Discord
discord:
  bot_token: "{{DISCORD_BOT_TOKEN}}"
  application_id: "{{DISCORD_APP_ID}}"
  gateway_intents: [GUILD_MESSAGES, DIRECT_MESSAGES, MESSAGE_CONTENT]

# Slack
slack:
  bot_token: "{{SLACK_BOT_TOKEN}}"
  signing_secret: "{{SLACK_SIGNING_SECRET}}"
  socket_mode: false
  event_subscriptions: [message.im, app_mention]
```

## Platform Configuration

| Platform | Status | Transport | Auth |
|----------|--------|-----------|------|
| {{platform}} | active | webhook | bot_token |

## Security

| Control | Value | Notes |
|---------|-------|-------|
| dm_pairing | true | Users must initiate DM before commands work |
| allowed_user_ids | [] | Empty = open; populate for production |
| rate_limit | 30/min/user | Prevents abuse |
| command_approval_list | [] | Commands requiring explicit approval |

### Security Hardening Checklist

- Validate webhook signatures (platform-specific HMAC verification)
- Store bot tokens in `secret_config` (P09), never in gateway artifact
- Enable `dm_pairing` in production (prevents unsolicited bot commands)
- Populate `allowed_user_ids` for private/internal deployments
- Set `rate_limit_per_user_per_min` based on expected usage patterns
- Log all command invocations for audit trail
- Rotate bot tokens quarterly or on suspected compromise

## Features

| Feature | Status | Dependency |
|---------|--------|------------|
| cross_platform_continuity | enabled | peer_id must be consistent |
| shared_slash_commands | enabled | All platforms share same /cmd set |
| voice_memo_transcription | disabled | Enable via stt_provider integration |

## Shared Slash Commands

| Command | Description | Platforms supported |
|---------|-------------|-------------------|
| /help | List available commands | Telegram, Discord, Slack |
| /status | Agent status and memory summary | Telegram, Discord, Slack |
| /reset | Clear current session context | Telegram, Discord, Slack |
| /personality | Switch agent persona (hot-swap) | Telegram, Discord, Slack |
| /feedback | Submit feedback on last response | All (adapted per platform) |

## Message Flow Architecture

```
User message (any platform)
  |
  v
Platform Adapter (normalize to canonical format)
  |
  v
Gateway Router (peer_id lookup, session resolution)
  |
  v
Agent Core (system_prompt + personality + context)
  |
  v
Response Generator (8F pipeline if artifact request)
  |
  v
Platform Adapter (format for target platform)
  |
  v
User receives response (native platform format)
```

## Integration Points

- `user_model` (P10): peer_id linked to gateway user identity
- `session_state` (P10): each conversation turn produces ephemeral session data
- `stt_provider` (P04): voice memo transcription (when enabled)
- `agent_profile` (P08): gateway routes to this agent
- `secret_config` (P09): bot tokens and API keys stored securely
- `rate_limit_config` (P09): per-user, per-platform rate limiting

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `user_model` | P10 | Tracks user identity across platforms via peer_id |
| `session_state` | P10 | Ephemeral conversation state per session |
| `stt_provider` | P04 | Speech-to-text for voice memo transcription |
| `agent_card` | P08 | Deployment spec for the agent receiving gateway messages |
| `secret_config` | P09 | Secure storage for platform bot tokens |
| `webhook` | P04 | Generic webhook kind; gateway is a specialized multi-platform webhook |

## Transport: Webhook vs Polling

| Aspect | Webhook (push) | Long-polling (pull) |
|--------|---------------|---------------------|
| Latency | Low (~100ms) | Medium (~1-5s poll interval) |
| Server requirement | Public HTTPS endpoint | None (outbound only) |
| Reliability | Depends on uptime | Self-healing on reconnect |
| SSL required | Yes (most platforms mandate TLS) | No (outbound HTTPS) |
| Firewall friendly | No (inbound port needed) | Yes (outbound only) |
| Scale pattern | Stateless, horizontal | Stateful, per-connection |
| Best for | Production deployments | Development, NAT/firewall constrained |
| Supported by | Telegram, Slack, WhatsApp, Discord | Telegram, Discord (gateway WS) |

## Rate Limits by Platform

| Platform | Messages/sec (bot) | Messages/min (user) | API calls/min | Bulk limit | Notes |
|----------|-------------------|---------------------|---------------|------------|-------|
| Telegram | 30 msg/s global | 20/min per chat | 30 API/s | 1 msg/s per chat | Group chats: 20 msg/min |
| Discord | 5 msg/channel/5s | 5/5s per channel | 50 req/s | 10k msg/10min | Per-route bucket system |
| Slack | 1 msg/s per channel | no per-user limit | 1 req/s (tier 1) | varies by tier | Web API uses tiered rate limits |
| WhatsApp | 80 msg/s (business) | platform-managed | 200 req/s | 1k contacts/broadcast | 24h session window policy |
| Signal | 1 msg/s | platform-managed | 10 req/s | no bulk API | Rate limits are conservative |
| Email | provider-limited | provider-limited | provider-limited | varies | Gmail: 500/day, SES: configurable |

## Canonical Message Format

All platform adapters normalize inbound messages to this canonical format before
routing to the agent core. Outbound responses are denormalized back to platform-native format.

```json
{
  "message_id": "msg_{{platform}}_{{uuid}}",
  "peer_id": "peer_{{user_hash}}",
  "platform": "{{platform}}",
  "timestamp": "2026-04-22T14:30:00Z",
  "type": "text",
  "content": {
    "text": "user message body",
    "attachments": [],
    "reply_to": null
  },
  "metadata": {
    "chat_type": "dm",
    "thread_id": null,
    "platform_user_id": "{{platform_specific_id}}",
    "locale": "en-US"
  }
}
```

## Stub Notice

This is a HERMES DP5 stub. No live platform connections are implemented here.
To activate: configure platform credentials in `.cex/config/gateway_{{platform}}.yaml`
and run `hermes gateway setup && hermes gateway start`.
