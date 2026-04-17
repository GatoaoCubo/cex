---
id: bld_schema_data_contract
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
quality: null
tags: [data_contract, schema]
title: "Schema Data Contract"
---
# Schema: data_contract
## Frontmatter Fields (Required)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (dc_{prod}_{cons}_{entity}) | YES | snake_case |
| kind | literal "data_contract" | YES | — |
| pillar | literal "P06" | YES | — |
| title | string | YES | Human-readable contract name |
| version | semver | YES | Artifact version |
| quality | null | YES | Never self-score |
| producer_system | string | YES | System/team producing data |
| consumer_system | string | YES | System/team consuming data |
| entity | string | YES | Data entity name (PascalCase) |
| contract_version | semver | YES | Independent from impl version |
| effective_date | date YYYY-MM-DD | YES | When contract takes effect |
| tags | list[string] | YES | >= 3 tags |

## Body Sections (Required)
```markdown
## Schema
| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| {field} | {type} | {true/false} | {description} |

## SLA
| Metric | Threshold | Notes |
|--------|-----------|-------|
| freshness | {Xs / Xmin / 1h / daily} | Max age of data |
| availability | {99.X%} | Uptime guarantee |
| latency_p99 | {Xms} | 99th percentile response |

## Versioning Policy
- backward_compatible: {true/false}
- breaking_change_policy: {description}
- deprecation_notice: {X days}
```

## ID Pattern
`^dc_[a-z][a-z0-9_]+$`
Example: dc_sales_billing_order, dc_events_analytics_clickstream

## Constraints
- max_bytes: 4096
- schema section min 1 typed field
- SLA section min 1 numeric threshold
- contract_version independent from software version
