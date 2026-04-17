---
id: bld_examples_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Examples"
version: 1.0.0
quality: 5.1
tags: [builder, event_stream, examples]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
---
# Examples: event_stream
## Golden Example: Order Events
```yaml
id: p04_es_order_events
kind: event_stream
event_types: [OrderPlaced, OrderPaid, OrderShipped, OrderCancelled]
producer: OrderService
consumer_groups:
  - name: fulfillment-group
    offset_policy: latest
    lag_tolerance: 1000 events
  - name: analytics-group
    offset_policy: earliest
    lag_tolerance: 10000 events
partition_key: orderId
partition_count: 12
retention_hours: 168
retention_bytes: "50GB"
delivery: at_least_once
schema_format: avro
compatibility_mode: BACKWARD
throughput_estimate: "5000 events/sec peak"
ordering_guarantee: per_partition
```
## Golden Example: User Activity Stream
```yaml
id: p04_es_user_activity
kind: event_stream
event_types: [UserLoggedIn, PageViewed, ItemAddedToCart, CheckoutStarted]
producer: WebApp
consumer_groups:
  - name: personalization-group
    offset_policy: latest
    lag_tolerance: 500 events
partition_key: userId
partition_count: 24
retention_hours: 72
delivery: at_most_once
schema_format: json_schema
```
## Anti-Pattern: No Partition Key
```yaml
# WRONG -- round-robin loses per-entity ordering
partition_key: null
# CORRECT: use entity identifier as key
partition_key: userId
```
## Anti-Pattern: Confusing with Webhook
```yaml
# WRONG -- webhook is for single HTTP push, not stream
kind: event_stream
consumer_groups: [{name: slack, offset_policy: latest}]
delivery: http_push  # not a valid delivery for event_stream
# CORRECT: if single HTTP push, use webhook kind instead
```
