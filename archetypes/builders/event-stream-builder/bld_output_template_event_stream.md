---
id: bld_output_template_event_stream
kind: output_template
pillar: P04
title: "Event Stream Builder -- Output Template"
version: 1.0.0
quality: 6.7
tags: [builder, event_stream, template]
llm_function: PRODUCE
density_score: 1.0
updated: "2026-04-17"
---
# Output Template: event_stream
```yaml
---
id: p04_es_{slug}
kind: event_stream
pillar: P04
title: "Event Stream: {Name}"
version: 0.1.0
event_types:
  - "{DomainEvent1}"
  - "{DomainEvent2}"
producer: "{ServiceOrAggregate}"
consumer_groups:
  - name: "{GroupName}"
    offset_policy: "{latest|earliest|timestamp}"
    lag_tolerance: "{N events or M seconds}"
partition_key: "{fieldName (e.g., orderId)}"
partition_count: {N}
retention_hours: {N}
retention_bytes: "{N}GB"
delivery: "{at_most_once|at_least_once|exactly_once}"
schema_format: "{avro|protobuf|json_schema|json}"
schema_registry: "{URL or service name}"
compatibility_mode: "{FULL|BACKWARD|FORWARD|NONE}"
throughput_estimate: "{N} events/sec"
ordering_guarantee: "{global|per_partition|none}"
monitoring:
  lag_threshold: "{N events}"
  alert_on: [consumer_lag, producer_error, retention_exceeded]
quality: null
tags: [event_stream, {domain_slug}, P04]
tldr: "{Name} stream: {N} event types, {partition_count} partitions, {retention_hours}h retention, {delivery}"
---

## Producer
**Service**: {ProducerName}
**Throughput**: {estimate events/sec}
**Encoding**: {schema_format} + {schema_registry}

## Consumer Groups
| Group | Offset Policy | Lag Tolerance | Purpose |
|-------|--------------|---------------|---------|
| {GroupName} | {latest/earliest} | {N events/sec} | {purpose} |

## Partitioning
**Key**: `{fieldName}` -- ensures ordered processing per {entity}
**Count**: {N} partitions
**Ordering**: {per_partition/global/none}

## Retention
**Time**: {N} hours ({M} days)
**Bytes**: {N} GB
**Replay window**: consumers can seek back up to {retention_hours} hours

## Schema
**Format**: {avro/protobuf/json}
**Registry**: {registry_url}
**Compatibility**: {FULL/BACKWARD} -- {implication for schema evolution}

## Operations
**Lag SLA**: consumer lag < {N} events; alert if exceeded {duration}
**Producer errors**: alert on > {N}% error rate
```
