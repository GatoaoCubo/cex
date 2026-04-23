---
id: n00_webhook_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Webhook -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, webhook, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_webhook
  - webhook-builder
  - bld_collaboration_webhook
  - p03_sp_webhook_builder
  - bld_examples_webhook
  - p01_kc_webhook
  - bld_memory_webhook
  - bld_schema_dataset_card
  - bld_output_template_webhook
  - bld_architecture_webhook
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A webhook is an HTTP event-driven endpoint that receives inbound events from external systems (Stripe payment, GitHub push, Slack action) and triggers agent workflows in response, or sends outbound HTTP POST notifications to external systems when CEX events occur. It defines the endpoint URL, payload schema, signature verification, and the action triggered on receipt. The output is a complete webhook handler specification with security validation and idempotency handling.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `webhook` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| direction | string | yes | inbound, outbound, or bidirectional |
| endpoint_path | string | yes | URL path for the webhook endpoint |
| payload_schema | object | yes | JSON Schema defining expected payload structure |
| signature_header | string | no | Header name for HMAC signature verification |

## When to use
- When integrating external services (Stripe, GitHub, Slack) that push events to CEX
- When N05 Operations needs to trigger agent workflows from external system events
- When a social_publisher or notifier needs outbound webhooks to deliver to third-party platforms

## Builder
`archetypes/builders/webhook-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind webhook --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: wh_stripe_payment_received
kind: webhook
pillar: P04
nucleus: n06
title: "Stripe Payment Received Webhook"
version: 1.0
quality: null
---
direction: inbound
endpoint_path: "/webhooks/stripe/payment"
signature_header: "Stripe-Signature"
payload_schema:
  type: object
  properties:
    type: {type: string}
    data:
      type: object
      properties:
        object: {type: object}
  required: [type, data]
```

## Related kinds
- `api_client` (P04) -- outbound API client that complements inbound webhook events
- `notifier` (P04) -- delivery mechanism for outbound webhook-style notifications
- `hook` (P04) -- internal lifecycle hook that differs from external webhook integrations
- `daemon` (P04) -- background processor that handles high-volume inbound webhook queues

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_webhook]] | downstream | 0.53 |
| [[webhook-builder]] | related | 0.52 |
| [[bld_collaboration_webhook]] | related | 0.51 |
| [[p03_sp_webhook_builder]] | related | 0.47 |
| [[bld_examples_webhook]] | related | 0.45 |
| [[p01_kc_webhook]] | sibling | 0.44 |
| [[bld_memory_webhook]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.38 |
| [[bld_output_template_webhook]] | related | 0.38 |
| [[bld_architecture_webhook]] | related | 0.38 |
