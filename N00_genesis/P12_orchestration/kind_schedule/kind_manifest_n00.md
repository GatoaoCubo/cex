---
id: n00_schedule_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Schedule -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, schedule, p12, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A schedule is a temporal trigger that initiates a workflow or task at a defined time or recurrence. It is the clock mechanism of the CEX orchestration layer, enabling autonomous overnight runs, periodic quality sweeps, renewal notices, and any time-driven automation without requiring human initiation.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `schedule` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| cron_expression | string | yes | Standard cron expression (5-field or 6-field with seconds) |
| timezone | string | yes | IANA timezone (e.g. America/Sao_Paulo) |
| target_workflow | string | yes | ID of the workflow or task to trigger |
| enabled | boolean | yes | Whether this schedule is active |
| max_concurrent_runs | integer | yes | Maximum simultaneous executions |
| on_miss | enum | yes | skip \| run_once \| run_all |

## When to use
- When configuring overnight quality improvement runs via cron
- When scheduling periodic CEX maintenance tasks (index rebuild, memory prune)
- When setting up time-based renewal workflow triggers

## Builder
`archetypes/builders/schedule-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind schedule --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sched_overnight_quality_sweep
kind: schedule
pillar: P12
nucleus: n07
title: "Example Schedule"
version: 1.0
quality: null
---
# Schedule: Overnight Quality Sweep
cron_expression: "0 2 * * *"
timezone: America/Sao_Paulo
target_workflow: wf_evolve_quality_sweep
enabled: true
max_concurrent_runs: 1
on_miss: skip
```

## Related kinds
- `workflow` (P12) -- workflow triggered by this schedule
- `spawn_config` (P12) -- spawn configuration used when the schedule fires
- `renewal_workflow` (P12) -- renewal workflow that uses schedule triggers per stage
