---
id: bld_context_sources_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Context Sources"
version: 1.0.0
quality: 5.4
tags: [builder, event_stream, context]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Context Sources: event_stream
## Mandatory Loads (F3 INJECT)
| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_event_stream.md | Primary definition |
| Schema | archetypes/builders/event-stream-builder/bld_schema_event_stream.md | Field constraints |
| Template | archetypes/builders/event-stream-builder/bld_output_template_event_stream.md | Structure |
| Examples | archetypes/builders/event-stream-builder/bld_examples_event_stream.md | Golden patterns |
| Pillar schema | N00_genesis/P04_tools/_schema.yaml | Pillar constraints |
## Related Kind KCs
| KC | Relationship |
|----|-------------|
| kc_webhook.md | single outbound HTTP push (simpler alternative) |
| kc_process_manager.md | subscribes to event streams to drive process transitions |
| kc_domain_event.md | schema of events flowing through the stream |
| kc_api_client.md | may consume event stream via HTTP SSE or WebSocket |
## External References
| Source | Relevance |
|--------|----------|
| Kafka documentation | Topic configuration reference |
| AWS Kinesis docs | Shard/partition configuration |
| Confluent Schema Registry | Avro/Protobuf compatibility modes |
| Kleppmann DDIA (2017) | Stream processing fundamentals |
