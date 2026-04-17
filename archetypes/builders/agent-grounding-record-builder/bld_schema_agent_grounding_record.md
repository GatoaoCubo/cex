---
kind: schema
id: bld_schema_agent_grounding_record
pillar: P06
llm_function: CONSTRAIN
purpose: Field-level schema defining all required and optional fields for agent_grounding_record artifacts
quality: 9.1
title: "Agent Grounding Record -- Schema"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, schema]
tldr: "Complete field schema: inference_id, model block, tool_calls array, rag_chunks array, output-hash, otel_span_id, C2PA ref"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Grounding Record -- Schema

## Root Fields

| Field                  | Type    | Required | Format / Constraint                         | Description                                                   |
|------------------------|---------|----------|---------------------------------------------|---------------------------------------------------------------|
| inference_id           | string  | YES      | UUIDv4 (8-4-4-4-12 hex)                    | Unique ID for this inference run -- never reused              |
| session_id             | string  | NO       | Arbitrary string                            | Parent session ID if part of multi-turn conversation          |
| timestamp              | string  | YES      | ISO 8601 with timezone (e.g. 2026-04-14T15:30:00Z) | Start time of the inference run                    |
| downstream_use         | string  | YES      | Enum: production / test / eval              | Intended use of the output -- drives post-market monitoring   |
| grounding_coverage_pct | float   | YES      | 0.0 to 1.0 inclusive                        | Fraction of output claims with traceable grounding source     |
| output_hash            | string  | YES      | SHA-256 hex (64 lowercase hex chars)        | Hash of raw model output bytes before post-processing        |
| otel_span_id           | string  | YES      | OTel span ID (16 hex chars, W3C format)     | Links record to active OpenTelemetry trace span               |
| c2pa_manifest_ref      | string  | NO       | URI string or null                          | Reference to C2PA content credential manifest                 |

## Model Object

Nested under `model:` key.

| Field          | Type   | Required | Format / Constraint        | Description                                                          |
|----------------|--------|----------|----------------------------|----------------------------------------------------------------------|
| id             | string | YES      | Exact model identifier     | Provider-assigned model ID (e.g. claude-sonnet-4-6)                |
| version        | string | NO       | Semver or checkpoint hash  | Model version; omit only if provider does not expose it             |
| provider       | string | YES      | Enum: anthropic / openai / google / azure / self-hosted | Model provider                        |
| model-signature| string | NO       | Cryptographic hash or attestation URI | Provider attestation of model identity; null if unavailable |

## tool_calls Array

Each element represents one tool invocation. Empty array [] if no tools were called.

| Field             | Type    | Required | Format / Constraint                  | Description                                              |
|-------------------|---------|----------|--------------------------------------|----------------------------------------------------------|
| tool_name         | string  | YES      | Registered tool name                 | Exact name as registered in the tool registry            |
| tool_input_hash   | string  | YES      | SHA-256 hex (64 chars)               | Hash of the serialized tool input payload                |
| tool_output_hash  | string  | YES      | SHA-256 hex (64 chars)               | Hash of the serialized tool output payload               |
| duration_ms       | integer | YES      | Non-negative integer                 | Wall-clock milliseconds from invocation to response      |
| timestamp         | string  | YES      | ISO 8601 with timezone               | Time the tool was invoked (not session start)            |
| status            | string  | YES      | Enum: success / error                | Outcome of the tool call                                 |
| error_code        | string  | NO       | String                               | Error code if status = error; omit on success            |

## rag_chunks Array

Each element represents one retrieved chunk. Empty array [] if no RAG was used.

| Field            | Type   | Required | Format / Constraint          | Description                                                        |
|------------------|--------|----------|------------------------------|--------------------------------------------------------------------|
| chunk_id         | string | YES      | Unique chunk identifier      | ID from the vector store or document store                         |
| source_url       | string | YES      | Full URL or internal path    | NEVER null or "unknown" -- reject chunk if source cannot be traced |
| retrieval_score  | float  | YES      | 0.0 to 1.0                   | Cosine similarity or BM25 score at retrieval time                  |
| content_hash     | string | YES      | SHA-256 hex (64 chars)       | Hash of chunk text at retrieval time (not current state)           |

## Validation Rules

| Rule ID | Field(s)                  | Constraint                                                                     |
|---------|---------------------------|--------------------------------------------------------------------------------|
| V01     | inference_id              | UUIDv4 regex: ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$ |
| V02     | output_hash               | Exactly 64 lowercase hex characters                                            |
| V03     | otel_span_id              | Exactly 16 lowercase hex characters (W3C trace context format)                 |
| V04     | grounding_coverage_pct    | Must be >= 0.0 and <= 1.0                                                      |
| V05     | downstream_use            | Must be one of: production, test, eval                                         |
| V06     | rag_chunks[*].source_url  | Non-empty string; no null, no empty string, no "unknown"                       |
| V07     | tool_calls[*].duration_ms | Non-negative integer (0 is valid for sub-millisecond tools)                   |
| V08     | timestamp                 | Parseable ISO 8601 with timezone offset; UTC (Z) preferred                     |
| V09     | model.id                  | Non-empty string                                                                |
| V10     | model.provider            | One of: anthropic, openai, google, azure, self-hosted                          |

## Byte Budget Guidance

Total artifact max: 4096 bytes. Typical distribution:

| Section              | Typical Bytes | Notes                                                     |
|----------------------|---------------|-----------------------------------------------------------|
| Frontmatter          | 400           | Fixed overhead                                            |
| Root fields          | 300           | inference_id + timestamp + hashes + otel_span_id          |
| model block          | 200           | 4 fields                                                  |
| tool_calls (3 items) | 600           | ~200 bytes per tool call                                  |
| rag_chunks (5 items) | 900           | ~180 bytes per chunk                                      |
| Summary section      | 300           | Human-readable audit summary                              |
| Margin               | 1396          | Buffer for larger tool/chunk counts                       |

If the artifact exceeds 4096 bytes: truncate tool_calls and rag_chunks to counts + hashes only, and reference a full trace log via a pointer field `full_trace_log_ref`.

## JSON Schema (abridged for validation tooling)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["inference_id", "timestamp", "downstream_use",
               "grounding_coverage_pct", "output_hash", "otel_span_id", "model"],
  "properties": {
    "inference_id": { "type": "string", "format": "uuid" },
    "timestamp": { "type": "string", "format": "date-time" },
    "downstream_use": { "type": "string", "enum": ["production", "test", "eval"] },
    "grounding_coverage_pct": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
    "output_hash": { "type": "string", "pattern": "^[0-9a-f]{64}$" },
    "otel_span_id": { "type": "string", "pattern": "^[0-9a-f]{16}$" },
    "model": {
      "type": "object",
      "required": ["id", "provider"],
      "properties": {
        "id": { "type": "string", "minLength": 1 },
        "provider": { "type": "string", "enum": ["anthropic", "openai", "google", "azure", "self-hosted"] }
      }
    },
    "tool_calls": { "type": "array" },
    "rag_chunks": { "type": "array" }
  }
}
```
