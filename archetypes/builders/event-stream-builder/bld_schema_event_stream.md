---
quality: 8.0
id: bld_schema_event_stream
kind: schema
pillar: P04
title: "Event Stream Builder -- Schema"
version: 1.0.0
quality: 7.6
tags: [builder, event_stream, schema]
llm_function: CONSTRAIN
author: builder
tldr: "Event Stream tools: data contract, field types, and validation rules"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_training_method
  - n06_schema_brand_config
  - bld_schema_enum_def
  - bld_schema_validation_schema
  - bld_schema_retriever_config
  - bld_schema_tagline
  - bld_schema_input_schema
  - bld_schema_prompt_compiler
---
# Schema: event_stream
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p04_es_{slug}` | namespace + slug |
| kind | literal `event_stream` | type integrity |
| pillar | literal `P04` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| event_types | list[string] | domain events flowing through this stream |
| producer | string | service or aggregate that writes to stream |
| consumer_groups | list[{name, offset_policy, lag_tolerance}] | at least 1 group |
| partition_key | string | field used for partitioning |
| partition_count | int | number of partitions |
| retention_hours | int | how long events are retained |
| delivery | enum(at_most_once, at_least_once, exactly_once) | delivery semantics |
| schema_format | enum(avro, protobuf, json_schema, json) | event envelope format |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| retention_bytes | string | max bytes retained (e.g. "100GB") |
| throughput_estimate | string | expected events/sec |
| schema_registry | string | URL or service name |
| compatibility_mode | enum(FULL, BACKWARD, FORWARD, NONE) | schema evolution policy |
| monitoring | object | lag threshold, alert_on |
| ordering_guarantee | enum(global, per_partition, none) | ordering semantics |
## ID Pattern
Regex: `^p04_es_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Producer` -- who writes, throughput estimate
2. `## Consumer Groups` -- each group with offset and lag config
3. `## Partitioning` -- key, count, ordering guarantee
4. `## Retention` -- time, bytes, replay window
5. `## Schema` -- format, registry, compatibility
6. `## Operations` -- monitoring, alerts, lag SLA
## Constraints
- max_bytes: 3072
- naming: p04_es_{slug}.md
- quality: null always

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
| [[bld_schema_model_registry]] | sibling | 0.45 |
| [[bld_schema_experiment_tracker]] | sibling | 0.43 |
| [[bld_schema_training_method]] | sibling | 0.39 |
| [[n06_schema_brand_config]] | downstream | 0.39 |
| [[bld_schema_enum_def]] | sibling | 0.38 |
| [[bld_schema_validation_schema]] | sibling | 0.36 |
| [[bld_schema_retriever_config]] | sibling | 0.36 |
| [[bld_schema_tagline]] | sibling | 0.35 |
| [[bld_schema_input_schema]] | sibling | 0.35 |
| [[bld_schema_prompt_compiler]] | sibling | 0.35 |
