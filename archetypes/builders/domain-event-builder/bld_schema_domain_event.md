---
id: bld_schema_domain_event
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema for domain_event
version: 1.0.0
quality: null
tags: [domain_event, schema, ddd]
title: "Schema Domain Event"
---
# Schema: domain_event
## Frontmatter Fields (Required)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (de_{agg}_{verb}) | YES | snake_case, past tense verb |
| kind | literal "domain_event" | YES | — |
| pillar | literal "P12" | YES | — |
| title | string | YES | Human-readable event name |
| version | semver | YES | 1.0.0 start |
| quality | null | YES | Never self-score |
| aggregate_root | string | YES | Class name of owning aggregate |
| bounded_context | string | YES | Context namespace |
| event_version | string (v1, v2...) | YES | Schema version for consumers |
| occurred_at | ISO-8601 UTC string | YES | When the fact occurred |
| causation_id | uuid or null | REC | Command/event that caused this |
| correlation_id | uuid or null | REC | Saga or trace identifier |
| tags | list[string] | YES | >= 3 tags |

## Payload Section (Required in body)
```yaml
payload:
  {field_name}: {type}  # fields carried at occurrence time
```
All payload fields are immutable -- snapshot at occurred_at.

## Optional Fields
| Field | Type | Notes |
|-------|------|-------|
| consumers | list[string] | Bounded contexts subscribing |
| schema_ref | string | JSON Schema / Avro ref |
| idempotency_key | string | For exactly-once processing |

## ID Pattern
`^de_[a-z][a-z0-9_]+$`
Example: de_order_placed_v1, de_payment_failed, de_user_registered

## Constraints
- max_bytes: 3072
- event name in title MUST be past tense
- payload MUST be populated (min 1 field)
- occurred_at MUST be ISO-8601 with timezone
