---
id: bld_knowledge_card_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Knowledge Card"
version: 1.0.0
quality: 7.5
tags: [builder, event_stream, knowledge]
llm_function: INJECT
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_webhook
  - p01_kc_signal
  - p01_kc_webhook
  - webhook-builder
  - p03_sp_webhook_builder
  - bld_memory_webhook
  - bld_architecture_webhook
  - bld_instruction_webhook
  - bld_collaboration_hook
  - bld_knowledge_card_hook_config
---
# Knowledge: event_stream
## Core Concept
Event Stream is a configuration artifact for real-time ordered event feeds.
It specifies how domain events are published, partitioned, retained, and consumed.
Industry: Kafka topic, Kinesis stream, Azure Event Hub.
## When to Use
- Multiple consumers need the same domain events independently
- Events must be replayed (audit, reprocessing, new consumer catch-up)
- Order matters within an entity's events (user actions, order updates)
- Real-time processing at high throughput (>100 events/sec)
## When NOT to Use
- Single HTTP push to one endpoint: use webhook
- Internal CEX nucleus coordination: use signal
- One-time notification: use webhook or direct command
- Scheduled batch: use schedule
## Key Configuration Dimensions
1. Partitioning: determines parallelism and ordering scope
2. Retention: determines replay window (how far back consumers can read)
3. Delivery: determines consumer idempotency requirements
4. Consumer groups: each group reads independently with its own offset
5. Schema: determines event shape and evolution policy
## CEX Integration
- Pillar: P04 (Tools)
- Builder: event-stream-builder (13 ISOs)
- Related: webhook (P04), signal (internal), process_manager (P12)
- Produced by: N05 (Operations) or N03 (Engineering)
- max_bytes: 3072

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_webhook]] | related | 0.30 |
| [[p01_kc_signal]] | sibling | 0.29 |
| [[p01_kc_webhook]] | sibling | 0.27 |
| [[webhook-builder]] | related | 0.27 |
| [[p03_sp_webhook_builder]] | related | 0.25 |
| [[bld_memory_webhook]] | downstream | 0.21 |
| [[bld_architecture_webhook]] | related | 0.20 |
| [[bld_instruction_webhook]] | upstream | 0.20 |
| [[bld_collaboration_hook]] | downstream | 0.20 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.19 |
