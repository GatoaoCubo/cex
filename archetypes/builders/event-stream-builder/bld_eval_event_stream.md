---
id: bld_quality_gate_event_stream
kind: quality_gate
pillar: P04
title: "Event Stream Builder -- Quality Gate"
version: 1.0.0
quality: 8.3
tags: [builder, event_stream, quality_gate]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_notifier
  - p11_qg_agent_computer_interface
  - p11_qg_retriever
  - p11_qg_creation_artifacts
  - p11_qg_quality_gate
  - p11_qg_function_def
  - p11_qg_few_shot_example
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_chunk_strategy
---

## Quality Gate

# Gate: event_stream
## Threshold
>= 7.0 to publish; >= 9.0 for reference
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p04_es_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `event_stream` | Any other value |
| H05 | quality == null | Non-null |
| H06 | event_types list has >= 1 entry | Empty |
| H07 | producer defined | Missing |
| H08 | consumer_groups has >= 1 entry | Empty |
| H09 | partition_key defined | Missing |
| H10 | delivery enum value valid | Invalid value |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Partition count and ordering guarantee specified | 0.15 |
| S02 | Retention hours AND bytes both specified | 0.20 |
| S03 | Schema format and compatibility mode defined | 0.20 |
| S04 | Each consumer group has offset_policy and lag_tolerance | 0.15 |
| S05 | Throughput estimate present | 0.10 |
| S06 | Monitoring thresholds defined | 0.10 |
| S07 | Boundary from webhook and signal stated in tldr or notes | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
