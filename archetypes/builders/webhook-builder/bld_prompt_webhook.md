---
kind: instruction
id: bld_instruction_webhook
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for webhook artifacts
pattern: 3-phase pipeline (Research -> Compose -> Validate)
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [instruction, webhook, P03, pipeline]
quality: 9.1
density_score: 0.91
domain: "instruction artifact construction"
title: "Instruction Webhook"
tldr: "Defines the instruction specification for instruction webhook, with structural rules, validation gates, and integration points."
related:
  - bld_output_template_webhook
  - p11_qg_webhook
  - p03_sp_webhook_builder
  - webhook-builder
  - bld_examples_webhook
  - bld_config_webhook
  - p01_kc_webhook
  - bld_schema_webhook
  - bld_collaboration_webhook
  - bld_instruction_output_validator
---
# Instructions: How to Produce a webhook

## Phase 1: RESEARCH

1. Identify the event source or destination (Stripe, GitHub, Slack, Twilio, costm)
2. Determine direction: inbound (your endpoint receives events) or outbound (you push events)
3. List all event types with trigger conditions (e.g., "payment.completed — charge succeeds")
4. Define payload schema for each event type (fields, types, required)
5. Identify signature verification method: HMAC-SHA256 is standard; note the secret header name
6. For outbound: define retry policy (max attempts, backoff multiplier, dead-letter)
7. For inbound: identify idempotency key field to prevent double-processing
8. Search for existing webhook artifacts — avoid duplicates (grep p04_webhook_)
9. Confirm event slug: lowercase, underscores, no hyphens (e.g., payment_completed)

## Phase 2: COMPOSE

1. Read `bld_schema_webhook.md` — verify all required fields
2. Read `bld_output_template_webhook.md` — fill every `{{var}}`
3. Write frontmatter: id matches `p04_webhook_{event_slug}`, quality: null
4. Write `## Overview`: direction, source/destination, use case in 2-3 sentences
5. Write `## Events`: for each event_type — trigger condition + minimal payload example
6. Write `## Verification`: method name, header, how secret is stored (env var)
7. Write `## Retry & Delivery`: attempts, backoff formula, timeout_ms, idempotency key
8. Count body bytes — must be <= 1024
9. Verify id matches filename stem exactly

## Phase 3: VALIDATE

Run gates in order — stop at first HARD failure:

1. YAML frontmatter parses without error
2. id matches regex `^p04_webhook_[a-z][a-z0-9_]+$`
3. kind == "webhook"
4. quality == null
5. All required fields present: id, name, direction, event_type, payload_schema
6. direction is "inbound" or "outbound" (no other values)
7. event_type is a non-empty string
8. payload_schema is a defined object (not empty `{}`)
9. body <= 1024 bytes
10. No persistent lifecycle language (no "server", "daemon", "listen forever")
11. Inbound: signature_method present and != "none" (security gate)
12. Outbound: retry_policy present with max_attempts > 0

## Escalation

- Ambiguous direction: ask "Does your system receive this event or send it?"
- Unknown payload schema: use `additionalProperties: true` with known fields only
- Exceeds 1024 bytes: compress Overview to 1 sentence, merge small event examples
- No signature info available: use hmac_sha256 as default, flag for secret setup

## Template Loading

```yaml
# This instruction is ISO 3 of 13 in the builder stack
loader: cex_skill_loader.py
injection_point: F3_compose
priority: high
```

```bash
# Verify instruction loads correctly
python _tools/cex_skill_loader.py --verify instruction artifact construction
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_webhook]] | downstream | 0.45 |
| [[p11_qg_webhook]] | downstream | 0.44 |
| [[p03_sp_webhook_builder]] | downstream | 0.43 |
| [[webhook-builder]] | downstream | 0.39 |
| [[bld_examples_webhook]] | downstream | 0.38 |
| [[bld_config_webhook]] | downstream | 0.36 |
| [[p01_kc_webhook]] | upstream | 0.35 |
| [[bld_schema_webhook]] | downstream | 0.35 |
| [[bld_collaboration_webhook]] | downstream | 0.34 |
| [[bld_instruction_output_validator]] | sibling | 0.33 |
