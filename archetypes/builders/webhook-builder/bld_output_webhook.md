---
kind: output_template
id: bld_output_template_webhook
pillar: P04
llm_function: PRODUCE
purpose: Fill-in template for webhook artifact production
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [output_template, webhook, P04, template]
quality: 9.0
density_score: 1.0
domain: "output_template artifact construction"
title: "Output Template Webhook"
related:
  - bld_instruction_webhook
  - bld_schema_webhook
  - bld_examples_webhook
  - p03_sp_webhook_builder
  - webhook-builder
  - p11_qg_webhook
  - bld_collaboration_webhook
  - p01_kc_webhook
  - bld_architecture_webhook
  - bld_knowledge_card_webhook
---
# Output Template: webhook

Copy this template. Replace every `{{var}}` with concrete values.
Remove comment lines (starting with #-) before saving.

---

```markdown
---
id: p04_webhook_{{event_slug}}
kind: webhook
pillar: P04
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
name: "{{Human Readable Webhook Name}}"
direction: {{inbound|outbound}}
event_type: "{{primary.event.type}}"
event_types:
  - "{{primary.event.type}}"
  - "{{secondary.event.type}}"
payload_schema:
  type: object
  required: [{{required_field_1}}, {{required_field_2}}]
  properties:
    {{field_1}}:
      type: {{string|integer|boolean|object|array}}
      description: "{{field description}}"
    {{field_2}}:
      type: {{string|integer|boolean|object|array}}
      description: "{{field description}}"
signature_method: {{hmac_sha256|hmac_sha1|rsa_sha256|none}}
signature_header: "{{X-Signature-Header-Name}}"
retry_policy:
  max_attempts: {{3|5|10}}
  backoff: exponential
  backoff_base_ms: {{1000|2000}}
idempotency_key: "{{payload.field.path}}"
timeout_ms: {{30000}}
quality: null
tags: [webhook, {{event_slug}}, {{provider}}, P04]
tldr: "{{<=160 char dense summary of what this webhook handles}}"
description: "{{<=200 char description of direction, event, and purpose}}"
---
## Overview

{{2-3 sentences: direction (inbound/outbound), event source/destination,
what triggers this webhook and what system receives it.}}

## Events

### {{primary.event.type}}

**Trigger**: {{condition that causes this event to fire}}

**Payload example**:
```json
{
  "`{{field_1}}`": "`{{example_value}}`",
  "`{{field_2}}`": `{{example_value}}`
}
```

### {{secondary.event.type}} (if applicable)

**Trigger**: {{condition}}

**Payload example**: same schema, different values.

## Verification

- **Method**: {{hmac_sha256}}
- **Header**: `{{X-Signature-Header-Name}}`
- **Secret**: stored in env var `{{WEBHOOK_SECRET_ENV_VAR}}`
- **Algorithm**: `HMAC-SHA256(secret, raw_body)` — verify before parsing payload

## Retry & Delivery

- **Max attempts**: {{3}}
- **Backoff**: exponential, base {{1000}}ms
- **Timeout**: {{30000}}ms — respond 2xx within timeout or retry triggered
- **Idempotency key**: `{{payload.id}}` — deduplicate on this field
- **Dead-letter**: after {{3}} failures, route to `{{dead_letter_queue_or_log}}`
```

#- END TEMPLATE
#- Verify: body <= 1024 bytes after removing template comments
#- Verify: id == filename stem (p04_webhook_`{{event_slug}}`.md)

## Cross-References

| Field | Value |
|-------|-------|
| Pillar | P04 (Tools) |
| Kind | output_template |
| Artifact ID | bld_output_template_webhook |
| Validation | validation_schema + cex_score.py post-hook |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_webhook]] | upstream | 0.48 |
| [[bld_schema_webhook]] | downstream | 0.45 |
| [[bld_examples_webhook]] | related | 0.42 |
| [[p03_sp_webhook_builder]] | related | 0.41 |
| [[webhook-builder]] | related | 0.39 |
| [[p11_qg_webhook]] | downstream | 0.38 |
| [[bld_collaboration_webhook]] | related | 0.37 |
| [[p01_kc_webhook]] | upstream | 0.36 |
| [[bld_architecture_webhook]] | related | 0.36 |
| [[bld_knowledge_card_webhook]] | downstream | 0.34 |
