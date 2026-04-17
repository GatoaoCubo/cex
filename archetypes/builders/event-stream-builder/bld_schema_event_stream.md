---
id: bld_schema_event_stream
kind: schema
pillar: P04
title: "Event Stream Builder -- Schema"
version: 1.0.0
quality: 7.1
tags: [builder, event_stream, schema]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
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
