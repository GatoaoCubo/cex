---
kind: instruction
id: bld_instruction_notifier
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for notifier
pattern: 3-phase pipeline
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [instruction, notifier, P04, pipeline]
quality: 9.1
title: "Instruction Notifier"
tldr: "Golden and anti-examples for notifier construction, demonstrating ideal structure and common pitfalls."
domain: "notifier construction"
density_score: 0.90
related:
  - notifier-builder
  - p03_sp_notifier_builder
  - bld_output_template_notifier
  - p11_qg_notifier
  - p01_kc_notifier
  - bld_knowledge_card_notifier
  - bld_examples_notifier
  - bld_schema_notifier
  - bld_architecture_notifier
  - bld_memory_notifier
---
# Instructions: How to Produce a notifier

## Phase 1: RESEARCH
1. Identify the notification use case (transactional, alert, marketing, system health)
2. Choose channel: email, sms, slack, discord, push, in_app, teams
3. Select provider matching channel (SendGrid/AWS SES for email, Twilio for SMS,
   Slack API for slack, Discord Webhooks for discord, Firebase FCM for push)
4. Design message template with `{{variable}}` placeholders for dynamic content
5. Define priority levels and their delivery timing expectations:
   - critical: immediate, retry until delivered, page on-call
   - high: within 2 minutes, retry 3x
   - normal: batched delivery, best-effort
   - low: digest/summary, daily batch
6. Determine rate limits apownte for channel (SMS: 1/s, email: 100/min, Slack: 1/s)
7. Check for existing notifier artifacts to avoid duplicate channels
8. Confirm channel slug for id (e.g. slack -> p04_notify_slack_deploy)

## Phase 2: COMPOSE
1. Read bld_schema_notifier.md — internalize all required fields
2. Read bld_output_template_notifier.md — fill all `{{vars}}`
3. Fill frontmatter: id matches `^p04_notify_[a-z][a-z0-9_]+$`, quality: null
4. Write `## Overview`: channel, provider, use case in 2-3 sentences
5. Write `## Template`: message format per priority, list all `{{vars}}` used
6. Write `## Delivery`: rate_limit object, retry_policy, delivery_guarantee
7. Write `## Configuration`: provider endpoint, credentials reference (no secrets)
8. Count body bytes — must stay <= 1024
9. Verify id matches filename stem exactly

## Phase 3: VALIDATE
1. YAML frontmatter parses without error
2. id matches `^p04_notify_[a-z][a-z0-9_]+$`
3. kind == "notifier"
4. quality == null
5. channel is valid enum value
6. template field defined and non-empty
7. priority is valid enum value
8. rate_limit present for production channels
9. retry_policy present if priority is critical
10. artifact does NOT describe bidirectional HTTP (that is webhook territory)
11. body bytes <= 1024
12. tags list includes "notifier", len >= 3

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify notifier
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | notifier construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[notifier-builder]] | downstream | 0.50 |
| [[p03_sp_notifier_builder]] | downstream | 0.50 |
| [[bld_output_template_notifier]] | downstream | 0.49 |
| [[p11_qg_notifier]] | downstream | 0.44 |
| [[p01_kc_notifier]] | upstream | 0.43 |
| [[bld_knowledge_card_notifier]] | downstream | 0.43 |
| [[bld_examples_notifier]] | downstream | 0.40 |
| [[bld_schema_notifier]] | downstream | 0.39 |
| [[bld_architecture_notifier]] | downstream | 0.38 |
| [[bld_memory_notifier]] | downstream | 0.35 |
