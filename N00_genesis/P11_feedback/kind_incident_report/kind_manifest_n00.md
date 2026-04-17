---
id: n00_incident_report_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Incident Report -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, incident_report, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An incident_report provides structured AI incident documentation and post-mortem analysis for failures, safety violations, or unexpected behaviors in the CEX system. It captures timeline, impact, root cause, contributing factors, and corrective actions, creating institutional memory that prevents recurrence and satisfies regulatory reporting requirements.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `incident_report` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| severity | enum | yes | critical \| high \| medium \| low |
| incident_type | enum | yes | safety_violation \| quality_failure \| outage \| data_breach \| bias_event |
| detected_at | datetime | yes | When incident was first detected |
| resolved_at | datetime | no | When incident was resolved |
| affected_nuclei | array | yes | Nuclei involved in the incident |
| root_cause | string | yes | Primary root cause analysis |
| contributing_factors | array | yes | Secondary factors that amplified the incident |
| corrective_actions | array | yes | Actions taken or planned to prevent recurrence |
| audit_log_ref | string | no | Reference to audit log entries covering this incident |

## When to use
- After any safety guardrail violation or unexpected agent behavior
- When a nucleus produces output below quality threshold 8.0 after max retries
- When regulatory reporting requires incident documentation (EU AI Act Article 73)

## Builder
`archetypes/builders/incident_report-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind incident_report --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ir_n02_brand_safety_violation_001
kind: incident_report
pillar: P11
nucleus: n02
title: "Example Incident Report"
version: 1.0
quality: null
---
# Incident: N02 Brand Safety Violation
severity: high
incident_type: safety_violation
detected_at: "2026-04-17T09:45:00Z"
root_cause: "Content filter threshold set too low for competitor mentions"
corrective_actions: [{action: "Raise block_threshold to 0.8", owner: n05}]
```

## Related kinds
- `audit_log` (P11) -- log evidence referenced by this incident report
- `guardrail` (P11) -- violated guardrail documented in the report
- `learning_record` (P10) -- learning derived from this incident to prevent recurrence
