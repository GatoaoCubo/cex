---
id: bld_scoring_rubric_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Scoring Rubric"
version: 1.0.0
quality: null
tags: [builder, event_stream, scoring]
llm_function: GOVERN
---
# Scoring Rubric: event_stream
## 5D Dimensions
| Dim | Name | Weight | Description |
|-----|------|--------|-------------|
| D1 | Configuration Completeness | 0.30 | Partitioning, retention, schema, delivery all specified? |
| D2 | Consumer Group Design | 0.20 | Each consumer group has independent offset and lag SLA? |
| D3 | Operational Readiness | 0.20 | Monitoring thresholds and alerts defined? |
| D4 | Schema Governance | 0.15 | Schema format + registry + compatibility mode specified? |
| D5 | Throughput Sizing | 0.15 | Partition count justified against throughput estimate? |
## D1 Scoring Guide
| Score | Criteria |
|-------|----------|
| 1.0 | partition_key, partition_count, retention_hours, retention_bytes, delivery, schema_format all present |
| 0.7 | 4-5 of 6 present |
| 0.3 | 2-3 of 6 present |
| 0.0 | Fewer than 2 core config fields |
## D3 Scoring Guide
| Score | Criteria |
|-------|----------|
| 1.0 | Lag threshold, alert conditions, and response action all defined |
| 0.5 | Lag threshold defined but no alert or response |
| 0.0 | No monitoring config |
