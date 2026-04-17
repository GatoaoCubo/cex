---
id: n00_discovery_questions_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Discovery Questions -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, discovery_questions, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Discovery Questions is a structured question bank following MEDDIC/BANT sales methodology frameworks. It surfaces buyer pain, budget authority, timeline, and decision criteria in a systematic way. Used by N06 commercial nucleus and sales-facing agents to qualify opportunities and guide prospect conversations toward conversion.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `discovery_questions` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Question bank name and context |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| framework | enum | yes | MEDDIC\|BANT\|SPIN\|JTBD\|custom |
| target_persona | string | yes | Buyer persona this bank targets |
| vertical | string | no | Industry vertical filter |
| questions | list | yes | Ordered question objects with category |
| follow_ups | map | no | Conditional follow-up by response type |

## When to use
- When building sales playbooks for a new product or market segment
- When training a conversational agent to qualify leads
- When designing guided onboarding flows with intent discovery

## Builder
`archetypes/builders/discovery_questions-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind discovery_questions --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- sales reps, conversational agents
- `{{DOMAIN_CONTEXT}}` -- product category and sales motion

## Example (minimal)
```yaml
---
id: discovery_questions_saas_enterprise_meddic
kind: discovery_questions
pillar: P01
nucleus: n06
title: "Enterprise SaaS MEDDIC Discovery"
version: 1.0
quality: null
---
framework: MEDDIC
target_persona: VP of Engineering
questions:
  - category: Metrics
    text: "What KPIs would improve if you solved this problem?"
  - category: Economic Buyer
    text: "Who holds budget authority for this decision?"
```

## Related kinds
- `competitive_matrix` (P01) -- objection handling context
- `customer_segment` (P02) -- ICP definition for targeting questions
- `knowledge_card` (P01) -- supporting facts for answer guidance
