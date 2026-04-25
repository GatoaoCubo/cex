---
quality: 7.6
quality: 7.3
id: bld_schema_domain_event
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema for domain_event
version: 1.0.0
tags: [domain_event, schema, ddd]
title: "Schema Domain Event"
author: builder
tldr: "Formal schema for domain_event"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_audit_log
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_config
  - bld_schema_multimodal_prompt
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

## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.65 |
| [[bld_schema_usage_report]] | related | 0.64 |
| [[bld_schema_benchmark_suite]] | related | 0.64 |
| [[bld_schema_pitch_deck]] | related | 0.63 |
| [[bld_schema_audit_log]] | related | 0.63 |
| [[bld_schema_dataset_card]] | related | 0.62 |
| [[bld_schema_integration_guide]] | related | 0.62 |
| [[bld_schema_quickstart_guide]] | related | 0.62 |
| [[bld_schema_sandbox_config]] | related | 0.61 |
| [[bld_schema_multimodal_prompt]] | related | 0.61 |
