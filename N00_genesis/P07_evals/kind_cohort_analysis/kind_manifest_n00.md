---
id: n00_cohort_analysis_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Cohort Analysis -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, cohort_analysis, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Cohort analysis produces a retention measurement and LTV modeling specification that groups users by a common attribute (signup date, acquisition channel, plan tier) and tracks their behavior over time. It defines cohort segmentation logic, retention curve methodology, LTV calculation approach, and the reporting cadence. Results drive product, pricing, and marketing decisions.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `cohort_analysis` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Cohort name + dimension + "Analysis" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| cohort_dimension | string | yes | Attribute used to form cohorts (signup_week, channel, etc.) |
| retention_window_days | int | yes | How many days to track cohort retention |
| ltv_model | enum | yes | historical / predictive / sMBR |
| event_definition | string | yes | What constitutes a retention event |
| reporting_cadence | enum | yes | weekly / monthly / quarterly |

## When to use
- Measuring the impact of a product or onboarding change on user retention
- Building the retention and LTV model for pricing or fundraising purposes
- Identifying acquisition channels with systematically higher long-term value

## Builder
`archetypes/builders/cohort_analysis-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind cohort_analysis --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence produces; N06 commercial consumes for LTV
- `{{SIN_LENS}}` -- Analytical Envy: no cohort left unexamined, no trend left unnoticed
- `{{TARGET_AUDIENCE}}` -- product managers, growth teams, investors
- `{{DOMAIN_CONTEXT}}` -- product lifecycle stage, user volume, retention baseline

## Example (minimal)
```yaml
---
id: cohort_analysis_cex_weekly_signup
kind: cohort_analysis
pillar: P07
nucleus: n01
title: "CEX Weekly Signup Cohort Retention Analysis"
version: 1.0
quality: null
---
cohort_dimension: signup_week
retention_window_days: 90
ltv_model: predictive
event_definition: "Built at least 1 artifact via 8F pipeline"
reporting_cadence: weekly
```

## Related kinds
- `usage_report` (P07) -- aggregated usage data feeding cohort analysis
- `experiment_tracker` (P07) -- A/B test results segmented by cohort
- `user_journey` (P05) -- strategic context for interpreting cohort drop-off
