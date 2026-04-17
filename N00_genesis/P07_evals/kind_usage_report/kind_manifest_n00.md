---
id: n00_usage_report_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Usage Report -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, usage_report, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Usage report defines a usage analytics report specification for billing reconciliation, capacity planning, and CFO dashboards. It specifies the metrics collected (token consumption, API calls, active users, artifact builds), aggregation granularity, cost attribution logic, and report distribution format. Usage reports bridge the operational data layer and business decision-making for AI infrastructure investment.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `usage_report` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Report name + period |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| reporting_period | enum | yes | daily / weekly / monthly / quarterly |
| metrics | list | yes | Tracked metrics with unit and aggregation |
| cost_attribution | object | yes | How costs are allocated (per nucleus, per user, per kind) |
| distribution | list | yes | Recipients and format (email/dashboard/API) |
| anomaly_detection | bool | yes | Whether to flag usage spikes or drops |

## When to use
- Building the monthly billing report for AI API consumption by nucleus
- Creating a CFO-facing dashboard showing AI infrastructure ROI
- Setting up anomaly alerts for unexpected usage spikes that indicate runaway costs

## Builder
`archetypes/builders/usage_report-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind usage_report --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N06 commercial owns reporting; N05 operations collects data
- `{{SIN_LENS}}` -- Strategic Greed: every token tracked, every dollar attributed
- `{{TARGET_AUDIENCE}}` -- CFO, CTO, and nucleus owners reviewing cost and utilization
- `{{DOMAIN_CONTEXT}}` -- provider mix, nucleus count, budget thresholds

## Example (minimal)
```yaml
---
id: usage_report_cex_monthly_api
kind: usage_report
pillar: P07
nucleus: n06
title: "CEX API Usage Report -- Monthly"
version: 1.0
quality: null
---
reporting_period: monthly
anomaly_detection: true
cost_attribution: {by_nucleus: true, by_provider: true, by_kind: false}
metrics:
  - {name: total_tokens_consumed, unit: tokens, aggregation: sum}
  - {name: total_api_cost_usd, unit: USD, aggregation: sum}
  - {name: builds_completed, unit: count, aggregation: sum}
```

## Related kinds
- `cohort_analysis` (P07) -- cohort retention analysis that contextualizes usage trends
- `benchmark` (P07) -- cost-per-run benchmarks that feed into the usage report
- `experiment_tracker` (P07) -- experiment costs that must be excluded from production usage
