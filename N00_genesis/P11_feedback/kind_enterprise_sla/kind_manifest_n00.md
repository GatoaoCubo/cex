---
id: n00_enterprise_sla_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Enterprise SLA -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, enterprise_sla, p11, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An enterprise_sla is an Enterprise Service Level Agreement template defining uptime commitments, latency guarantees, support response times, and financial remedies for SLA breaches. It establishes the contractual quality baseline that governs CEX platform reliability commitments to enterprise customers.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `enterprise_sla` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| uptime_percent | float | yes | Guaranteed uptime (e.g. 99.9) |
| latency_p95_ms | integer | yes | 95th percentile latency commitment in milliseconds |
| support_response_hours | integer | yes | Maximum initial support response time |
| incident_resolution_hours | integer | yes | Target resolution time for critical incidents |
| credits_per_breach | float | yes | Service credit percentage per SLA breach |
| measurement_window | enum | yes | monthly \| quarterly \| annual |
| exclusions | array | no | Scenarios excluded from SLA coverage |

## When to use
- When closing enterprise contracts requiring formal SLA commitments
- When configuring monitoring alerts to detect SLA breach risk
- When designing the incident response process tied to SLA obligations

## Builder
`archetypes/builders/enterprise_sla-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind enterprise_sla --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sla_enterprise_tier_gold
kind: enterprise_sla
pillar: P11
nucleus: n06
title: "Example Enterprise SLA"
version: 1.0
quality: null
---
# Enterprise SLA: Gold Tier
uptime_percent: 99.9
latency_p95_ms: 2000
support_response_hours: 4
incident_resolution_hours: 24
credits_per_breach: 10.0
measurement_window: monthly
```

## Related kinds
- `incident_report` (P11) -- incident documentation triggered by SLA breaches
- `quality_gate` (P11) -- internal quality threshold aligned with SLA commitments
- `subscription_tier` (P11) -- subscription tier that this SLA applies to
