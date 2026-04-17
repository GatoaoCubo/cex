---
id: bld_scoring_rubric_alert_rule
kind: scoring_rubric
pillar: P07
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [alert_rule, scoring, rubric]
title: "Scoring Rubric: alert_rule"
---
# Scoring Rubric: alert_rule
## 5 Dimensions
| # | Dimension | Weight | Description |
|---|-----------|--------|-------------|
| D1 | Expression precision | 30% | PromQL-style with numeric threshold, valid metric name |
| D2 | Severity configuration | 25% | Correct severity + routing + for_duration alignment |
| D3 | Actionability | 20% | Runbook URL or steps; automated response defined |
| D4 | Observability integration | 15% | Prometheus labels + annotations for Alertmanager |
| D5 | Naming clarity | 10% | PascalCase alert_name; clear id pattern |

## Scoring Formula
`score = (D1*0.30 + D2*0.25 + D3*0.20 + D4*0.15 + D5*0.10) * 10`

## Dimension Scoring Guide
### D1 Expression precision (0-10)
- 10: valid PromQL with metric name + numeric threshold + window
- 7: expression present with threshold but no time window
- 4: expression present without numeric threshold
- 0: no metric_expression

### D2 Severity configuration (0-10)
- 10: severity + routing + for_duration aligned to best practice
- 6: severity + routing, for_duration suboptimal
- 3: severity only
- 0: missing severity

### D3 Actionability (0-10)
- 10: runbook_url + automated_response both present
- 6: runbook only or automated only
- 3: "see playbook" without link
- 0: no actionability guidance

### D4 Observability integration (0-10)
- 10: severity + team + service labels + summary annotation
- 5: some labels
- 0: no labels or annotations

### D5 Naming clarity (0-10)
- 10: PascalCase alert_name + snake_case id + descriptive title
- 5: one naming issue
- 0: multiple naming issues
