---
id: n00_nps_survey_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "NPS Survey -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, nps_survey, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An nps_survey configures a Net Promoter Score survey with question text, scale definition, follow-up question logic, and user segmentation rules. It enables CEX-powered products to systematically collect customer satisfaction signals that feed back into the quality and improvement loops.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `nps_survey` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| primary_question | string | yes | Main NPS question text |
| scale | object | yes | Scale definition (min, max, labels) |
| followup_detractor | string | yes | Open-text question for score 0-6 |
| followup_promoter | string | yes | Open-text question for score 9-10 |
| segments | array | no | User segments with different question variants |
| trigger | enum | yes | post_session \| post_purchase \| time_based \| milestone |
| suppress_after_days | integer | yes | Days to suppress repeat survey per user |

## When to use
- When measuring customer satisfaction after a CEX nucleus interaction
- When segmenting feedback to understand detractor vs. promoter drivers
- When feeding qualitative NPS insights into self_improvement_loop

## Builder
`archetypes/builders/nps_survey-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind nps_survey --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: nps_cex_post_session
kind: nps_survey
pillar: P11
nucleus: n06
title: "Example NPS Survey"
version: 1.0
quality: null
---
# NPS Survey: Post-Session Feedback
primary_question: "How likely are you to recommend CEX to a colleague?"
scale: {min: 0, max: 10, low_label: "Not likely", high_label: "Extremely likely"}
trigger: post_session
suppress_after_days: 30
```

## Related kinds
- `reward_signal` (P11) -- NPS responses converted to quality signals
- `ab_test_config` (P11) -- A/B test measuring NPS differences between variants
- `self_improvement_loop` (P11) -- loop that consumes NPS data for improvement
