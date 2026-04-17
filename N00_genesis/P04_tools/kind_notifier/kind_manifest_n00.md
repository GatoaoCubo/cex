---
id: n00_notifier_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Notifier -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, notifier, p04, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A notifier delivers push notifications through external channels (email, SMS, Slack, Discord, Teams) when agents need to alert humans or trigger downstream systems. It abstracts delivery provider APIs into a unified send interface with templating, retry logic, and delivery confirmation. The output is a notification delivery tool that agents call after completing tasks, hitting quality gates, or detecting errors requiring human attention.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `notifier` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| channels | list | yes | Supported delivery channels: email, slack, discord, sms |
| default_channel | string | yes | Primary channel used when not specified |
| retry_policy | map | yes | Max retries and backoff per channel |
| template_support | boolean | yes | Whether notifier supports message templating |

## When to use
- When an agent completes a wave and must alert the user via Slack or email
- When a quality gate failure requires immediate human review notification
- When building a daemon that monitors conditions and sends alerts on trigger

## Builder
`archetypes/builders/notifier-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind notifier --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: notifier_slack_cex_alerts
kind: notifier
pillar: P04
nucleus: n07
title: "CEX Slack Alert Notifier"
version: 1.0
quality: null
---
channels: [slack, email]
default_channel: slack
template_support: true
retry_policy:
  slack: {max: 3, backoff: 5s}
  email: {max: 5, backoff: 30s}
```

## Related kinds
- `daemon` (P04) -- background monitor that triggers the notifier on condition detection
- `webhook` (P04) -- inbound event that may trigger a notifier as part of the response
- `hook` (P04) -- lifecycle hook that calls the notifier on Stop or quality gate events
- `social_publisher` (P04) -- publishing tool that complements notifier for outbound content
