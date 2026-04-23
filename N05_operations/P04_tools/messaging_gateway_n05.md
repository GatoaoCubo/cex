---
id: messaging_gateway_n05
kind: messaging_gateway
nucleus: n05
pillar: P04
mirrors: N00_genesis/P04_tools/tpl_messaging_gateway.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Messaging Gateway (Runtime)"
version: 1.0.0
quality: 8.2
tags: [mirror, n05, operations, hermes_assimilation, messaging_gateway]
tldr: "N05-owned gateway stub: uptime SLA, rate-limit enforcement, auth rotation, failure-mode matrix for all platform adapters."
related:
  - kc_integration_guide
  - p10_lr_client_builder
  - bld_knowledge_card_client
  - bld_memory_runtime_rule
  - integration-guide-builder
  - p04_webhook_NAME
  - bld_knowledge_card_secret_config
  - p01_kc_api_rate_limiting_retry_patterns
  - p11_qg_client
  - p09_arch_task_queue
---

## Ownership

N05 OWNS this kind. Operations is responsible for uptime, rate-limit enforcement,
authentication credential rotation, and incident response for all messaging adapters.

## Platform Matrix (Runtime View)

| Platform | SLA Target | Rate Limit (msg/min/user) | Auth Type | Failure Mode | Rollback Procedure |
|----------|------------|---------------------------|-----------|--------------|-------------------|
| telegram | 99.5% | 30 | bot_token | queue + retry 3x | revoke token, rotate via vault |
| discord | 99.5% | 30 | bot_token | queue + retry 3x | regenerate bot token in dev portal |
| slack | 99.9% | 60 | oauth2 | DLQ + alert oncall | rotate OAuth client secret |
| whatsapp | 99.0% | 20 | api_key | drop + log | re-register webhook |
| signal | 98.0% | 10 | linked_device | graceful degrade | re-link device |
| email | 99.9% | 5 | smtp_creds | retry 5x + DLQ | rotate SMTP password |

## Security Posture (IRA Lens)

| Control | Value | Enforcement |
|---------|-------|-------------|
| dm_pairing | mandatory | User must initiate DM before commands work |
| allowed_user_ids | populated in prod | Empty = BLOCKED in production |
| rate_limit_breach | temp ban 15min | Automatic, no human override |
| command_approval_list | [/deploy, /rollback, /scale] | Dangerous commands require 2FA |
| credential_rotation | 90d max | Alert at 75d, block at 91d |
| audit_log | all commands | .cex/runtime/audit/gateway_audit.jsonl |

## Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Platform API 5xx | health check 30s | circuit breaker open | page oncall at 3min |
| Token expired | 401 response | auto-rotate from vault | alert if rotation fails |
| Rate limit hit | 429 response | backoff + queue | drop after queue full |
| Webhook timeout | no ACK 10s | retry 3x exponential | DLQ + alert |
| DNS resolution | connect timeout | fallback endpoint | page infra team |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Message delivery latency p99 | <2s | warn at 1.5s, page at 3s |
| Error rate | <1% | warn at 0.5%, page at 2% |
| Queue depth | <1000 | warn at 500, page at 2000 |
| Auth token age | <90d | warn at 75d, block at 91d |

## Integration Points

- `terminal_backend` (P09): gateway process runs on specified backend
- `hibernation_policy` (P09): idle gateway hibernates per policy
- `sandbox_config` (P09): gateway process isolated per sandbox rules
- `session_state` (P10): each conversation turn produces ephemeral session data
- `user_model` (P10): peer_id linked to gateway user identity
- `schedule` (P12): health checks and credential rotation on schedule

## Stub Notice

HERMES DP5 stub. No live platform connections. To activate: configure platform
credentials in `.cex/config/gateway_{platform}.yaml`, validate via
`python _tools/cex_gateway_check.py --platform {platform}`, then start.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_integration_guide]] | upstream | 0.20 |
| [[p10_lr_client_builder]] | downstream | 0.20 |
| [[bld_knowledge_card_client]] | upstream | 0.19 |
| [[bld_memory_runtime_rule]] | downstream | 0.19 |
| [[integration-guide-builder]] | downstream | 0.19 |
| [[p04_webhook_NAME]] | related | 0.19 |
| [[bld_knowledge_card_secret_config]] | upstream | 0.18 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.17 |
| [[p11_qg_client]] | downstream | 0.17 |
| [[p09_arch_task_queue]] | downstream | 0.17 |
