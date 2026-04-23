---
quality: 8.4
id: bld_context_sources_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Context Sources"
version: 1.0.0
quality: 8.3
tags: [builder, event_stream, context]
llm_function: CONSTRAIN
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: event_stream
tldr: "Runtime configuration and mandatory context sources for the event_stream builder (F3 INJECT phase)."
density_score: 1.0
related:
  - bld_knowledge_event_stream
  - bld_schema_event_stream
  - bld_architecture_event_stream
  - bld_model_event_stream
  - bld_prompt_event_stream
  - bld_tools_event_stream
  - bld_output_event_stream
  - bld_eval_event_stream
  - bld_feedback_event_stream
  - bld_orchestration_event_stream
---
# Context Sources: event_stream

## Mandatory Loads (F3 INJECT)

| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_event_stream.md | Primary definition |
| Schema | archetypes/builders/event-stream-builder/bld_schema_event_stream.md | Field constraints |
| Template | archetypes/builders/event-stream-builder/bld_output_event_stream.md | Structure |
| Examples | archetypes/builders/event-stream-builder/bld_eval_event_stream.md | Golden patterns |
| Pillar schema | N00_genesis/P04_tools/_schema.yaml | Pillar constraints |

## Builder ISO Load Order (12 ISOs)

| # | ISO | Pillar | llm_function |
|---|-----|--------|--------------|
| 1 | bld_knowledge_event_stream | P01 | INJECT |
| 2 | bld_model_event_stream | P02 | BECOME |
| 3 | bld_prompt_event_stream | P03 | INJECT |
| 4 | bld_tools_event_stream | P04 | CALL |
| 5 | bld_output_event_stream | P05 | PRODUCE |
| 6 | bld_schema_event_stream | P06 | CONSTRAIN |
| 7 | bld_eval_event_stream | P07 | GOVERN |
| 8 | bld_architecture_event_stream | P08 | CONSTRAIN |
| 9 | bld_config_event_stream | P09 | CONSTRAIN |
| 10 | bld_memory_event_stream | P10 | INJECT |
| 11 | bld_feedback_event_stream | P11 | GOVERN |
| 12 | bld_orchestration_event_stream | P12 | COLLABORATE |

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

## Runtime Constraints

| Parameter | Default | Notes |
|-----------|---------|-------|
| max_bytes | 4096 | P04 pillar ceiling |
| format | yaml | Compiled output format |
| requires_external_context | false | Structural kind -- no live MCP needed |
| isolation | none | Standard dispatch |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_event_stream]] | sibling | 0.45 |
| [[bld_schema_event_stream]] | sibling | 0.43 |
| [[bld_architecture_event_stream]] | sibling | 0.41 |
| [[bld_model_event_stream]] | sibling | 0.39 |
| [[bld_prompt_event_stream]] | sibling | 0.37 |
| [[bld_tools_event_stream]] | sibling | 0.35 |
| [[bld_output_event_stream]] | sibling | 0.34 |
| [[bld_eval_event_stream]] | sibling | 0.33 |
| [[bld_feedback_event_stream]] | sibling | 0.32 |
| [[bld_orchestration_event_stream]] | sibling | 0.31 |
