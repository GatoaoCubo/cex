---
id: p06_is_campaign_performance_metrics
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "campaign performance metrics tracking and analysis"
fields:
  - name: "campaign_id"
    type: "string"
    required: true
    default: null
    description: "Unique identifier for the campaign being measured"
    error_message: "campaign_id is required - provide campaign identifier"
  - name: "metric_name"
    type: "string"
    required: true
    default: null
    description: "Name of the performance metric (CTR, conversion_rate, ROAS, impressions, etc.)"
    error_message: "metric_name is required - specify which metric to track"
  - name: "time_period"
    type: "object"
    required: true
    default: null
    description: "Time range for metric calculation: {start_date, end_date}"
    error_message: "time_period is required - provide date range as {start_date: YYYY-MM-DD, end_date: YYYY-MM-DD}"
  - name: "metric_value"
    type: "float"
    required: true
    default: null
    description: "Numerical value of the performance metric"
    error_message: "metric_value is required - provide numeric performance value"
  - name: "metric_type"
    type: "string"
    required: false
    default: "percentage"
    description: "Type of metric: percentage, count, currency, ratio"
    error_message: null
  - name: "aggregation_method"
    type: "string"
    required: false
    default: "sum"
    description: "How to aggregate metric across time: sum, average, median, max"
    error_message: null
  - name: "filters"
    type: "object"
    required: false
    default: null
    description: "Optional filters: {channel, audience_segment, device_type, geo}"
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse metric_value from string if numeric"
  - from: "integer"
    to: "float"
    rule: "Convert integer metric values to float for consistency"
examples:
  - {campaign_id: "camp_001", metric_name: "CTR", time_period: {start_date: "2026-03-01", end_date: "2026-03-31"}, metric_value: 2.35, metric_type: "percentage"}
  - {campaign_id: "camp_002", metric_name: "conversion_rate", time_period: {start_date: "2026-03-15", end_date: "2026-03-31"}, metric_value: 4.2, filters: {channel: "email", audience_segment: "premium"}}
domain: "marketing-analytics"
quality: 9.1
tags: [input-schema, campaign-metrics, performance-tracking, marketing, analytics]
tldr: "Input contract for campaign performance metrics: requires campaign_id, metric_name, time_period, and metric_value with optional type and filters."
density_score: 0.87
---
# Contract Definition
Campaign performance metrics tracking receives data from marketing analytics systems, reporting dashboards, and campaign management platforms. Callers provide campaign identifier, metric name, time period, and performance values with optional aggregation and filtering parameters.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | campaign_id | string | YES | - | Unique identifier for the campaign being measured |
| 2 | metric_name | string | YES | - | Name of performance metric (CTR, conversion_rate, ROAS, etc.) |
| 3 | time_period | object | YES | - | Time range: {start_date, end_date} |
| 4 | metric_value | float | YES | - | Numerical value of the performance metric |
| 5 | metric_type | string | NO | "percentage" | Type: percentage, count, currency, ratio |
| 6 | aggregation_method | string | NO | "sum" | Aggregation: sum, average, median, max |
| 7 | filters | object | NO | null | Optional filters by channel, audience, device, geo |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | float | Parse metric_value from string if numeric |
| integer | float | Convert integer metric values to float for consistency |

## Examples
```json
{"campaign_id": "camp_001", "metric_name": "CTR", "time_period": {"start_date": "2026-03-01", "end_date": "2026-03-31"}, "metric_value": 2.35, "metric_type": "percentage"}
```

```json
{"campaign_id": "camp_002", "metric_name": "conversion_rate", "time_period": {"start_date": "2026-03-15", "end_date": "2026-03-31"}, "metric_value": 4.2, "filters": {"channel": "email", "audience_segment": "premium"}}
```

## References
- Marketing analytics platforms requiring structured performance data
- Campaign management systems tracking ROI and conversion metrics
- Business intelligence dashboards consuming standardized metric formats