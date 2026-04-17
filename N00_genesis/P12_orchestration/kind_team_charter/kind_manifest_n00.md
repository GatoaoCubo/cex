---
id: n00_team_charter_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Team Charter -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, team_charter, p12, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A team_charter is the mission contract for a specific crew instance, binding a crew_template to a concrete mission with defined scope, budget, deadline, quality gate, and success criteria. It is what transforms a reusable crew blueprint into an actionable deployment -- the difference between a recipe and a specific meal being cooked tonight.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `team_charter` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| crew_template_ref | string | yes | ID of the crew_template being instantiated |
| mission_statement | string | yes | One-sentence mission for this specific deployment |
| scope | string | yes | Boundaries of what is and is not included |
| budget_tokens | integer | yes | Maximum token budget across all roles |
| deadline | datetime | yes | Hard deadline for crew completion |
| quality_gate | float | yes | Minimum quality score for final output |
| success_criteria | array | yes | Measurable conditions that define mission success |

## When to use
- When launching a crew for a specific product launch, campaign, or mission
- When instantiating a grid-of-crews where each cell has its own charter
- When defining the quality gate and budget for a multi-role team execution

## Builder
`archetypes/builders/team_charter-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind team_charter --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tc_product_launch_saas_q2
kind: team_charter
pillar: P12
nucleus: n07
title: "Example Team Charter"
version: 1.0
quality: null
---
# Team Charter: SaaS Q2 Product Launch
crew_template_ref: ct_product_launch_v1
mission_statement: "Launch CEX SaaS public beta with full marketing kit by 2026-05-01"
budget_tokens: 500000
deadline: "2026-05-01T00:00:00Z"
quality_gate: 9.0
success_criteria: ["landing_page live", "3 ad variants approved", "pricing page complete"]
```

## Related kinds
- `crew_template` (P12) -- template this charter instantiates
- `dispatch_rule` (P12) -- rules that fire when crew completes this charter
- `handoff` (P12) -- handoffs generated per role when charter is activated
