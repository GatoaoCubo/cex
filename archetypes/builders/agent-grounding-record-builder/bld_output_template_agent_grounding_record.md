---
kind: output_template
id: bld_output_template_agent_grounding_record
pillar: P05
llm_function: PRODUCE
purpose: Canonical output structure for agent_grounding_record artifacts ready for F6 PRODUCE rendering
quality: 9.1
title: "Agent Grounding Record -- Output Template"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, output_template]
tldr: "Fill-in template: frontmatter + inference block + model block + tool_calls + rag_chunks + hashes + audit summary"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
# Agent Grounding Record -- Output Template

## Usage

Replace every `{{PLACEHOLDER}}` with the actual value from the inference session.
Sections marked `[OPTIONAL]` may be omitted if not applicable, but MUST be explicitly
set to null rather than silently omitted for C2PA and model-signature fields.

## TEMPLATE START

```markdown
---
kind: agent_grounding_record
id: p10_gr_{{INFERENCE_ID_PREFIX}}
pillar: P10
llm_function: PRODUCE
purpose: Per-inference provenance record for {{SHORT_DESCRIPTION_OF_INFERENCE_TASK}}
quality: null
title: "Grounding Record -- {{SHORT_DESCRIPTION_OF_INFERENCE_TASK}}"
version: "1.0.0"
author: {{NUCLEUS_OR_SYSTEM_ID}}
tags: [agent_grounding_record, provenance, {{DOMAIN_TAG}}]
tldr: "Inference {{INFERENCE_ID_PREFIX}} -- {{MODEL_ID}} -- {{TOOL_COUNT}} tools -- {{CHUNK_COUNT}} RAG chunks"
domain: "agent_grounding_record construction"
created: "{{TIMESTAMP_DATE_ONLY}}"
updated: "{{TIMESTAMP_DATE_ONLY}}"
density_score: 0.85
---
# Grounding Record -- {{SHORT_DESCRIPTION_OF_INFERENCE_TASK}}
## Inference Identity
| Field                  | Value                                                     |
|------------------------|-----------------------------------------------------------|
| inference_id           | {{UUIDv4}}                                                |
| session_id             | {{SESSION_ID or null}}                                    |
| timestamp              | {{ISO_8601_WITH_TIMEZONE}}                                |
| downstream_use         | {{production or test or eval}}                            |
| grounding_coverage_pct | {{0.0 to 1.0}}                                            |
| otel_span_id           | {{16_HEX_CHAR_SPAN_ID}}                                   |
## Model
| Field          | Value                                                     |
|----------------|-----------------------------------------------------------|
| id             | {{MODEL_ID}}                                              |
| version        | {{MODEL_VERSION or null}}                                 |
| provider       | {{anthropic or openai or google or azure or self-hosted}} |
| model-signature| {{ATTESTATION_STRING or null}}                            |
## Tool Calls
{{TOOL_COUNT}} tool invocations during this inference run.
| # | tool_name       | tool_input_hash (sha256) | tool_output_hash (sha256) | duration_ms | timestamp              | status  |
|---|-----------------|--------------------------|---------------------------|-------------|------------------------|---------|
| 1 | {{TOOL_NAME_1}} | {{INPUT_HASH_1}}         | {{OUTPUT_HASH_1}}         | {{MS_1}}    | {{ISO_TIMESTAMP_1}}    | {{success or error}} |
| 2 | {{TOOL_NAME_2}} | {{INPUT_HASH_2}}         | {{OUTPUT_HASH_2}}         | {{MS_2}}    | {{ISO_TIMESTAMP_2}}    | {{success or error}} |
[Add rows as needed. If no tool calls: write "No tool calls were made in this inference run."]
## RAG Chunks Retrieved
{{CHUNK_COUNT}} chunks retrieved from knowledge sources.
| # | chunk_id       | source_url                                  | retrieval_score | content_hash (sha256) |
|---|----------------|---------------------------------------------|-----------------|-----------------------|
| 1 | {{CHUNK_ID_1}} | {{SOURCE_URL_1}}                            | {{SCORE_1}}     | {{CONTENT_HASH_1}}    |
| 2 | {{CHUNK_ID_2}} | {{SOURCE_URL_2}}                            | {{SCORE_2}}     | {{CONTENT_HASH_2}}    |
[Add rows as needed. If no RAG: write "No retrieval augmentation was used in this inference run."]
## Integrity
| Field             | Value                                                           |
|-------------------|-----------------------------------------------------------------|
| output_hash       | {{SHA256_64_HEX_CHARS}} (SHA-256 of raw model output)          |
| c2pa_manifest_ref | {{C2PA_MANIFEST_URI or null}}                                   |
## Audit Summary
**Inference task**: {{DESCRIPTION_OF_WHAT_THE_INFERENCE_WAS_ASKED_TO_DO}}
**Grounding sources**:
- {{COUNT}} RAG chunks from {{DESCRIBE_SOURCE_SYSTEMS}}
- {{COUNT}} tool calls to {{DESCRIBE_TOOLS_USED}}
**Traceability chain**:
Input -> {{DESCRIBE_RAG_OR_TOOLS}} -> model ({{MODEL_ID}}) -> output (hash: {{FIRST_8_CHARS_OF_OUTPUT_HASH}}...)
**Coverage note**: {{EXPLAIN_GROUNDING_COVERAGE_PCT_VALUE}}
**OTel linkage**: This record is linked to OTel span {{OTEL_SPAN_ID}}. Full trace available in the observability backend.
**C2PA status**: {{NOTE_ON_C2PA_MANIFEST_STATUS}}
```

## TEMPLATE END

## Rendering Notes

| Element              | Guidance                                                                          |
|----------------------|-----------------------------------------------------------------------------------|
| Tool table           | Sort by timestamp ascending; one row per invocation including failed calls        |
| RAG chunk table      | Sort by retrieval_score descending; include all retrieved chunks, not just cited  |
| output_hash          | Must be computed from raw bytes BEFORE any markdown formatting or truncation      |
| grounding_coverage_pct | Compute from actual claim analysis; document methodology in Coverage note      |
| Audit Summary        | Write for a human auditor, not just a machine parser -- prose is appropriate here |
| Byte budget          | Keep total artifact under 4096 bytes; truncate tables with full_trace_log_ref if needed |

## Byte Budget Estimator

```
Frontmatter:          ~400 bytes
Inference Identity:   ~250 bytes
Model block:          ~200 bytes
Tool Calls (per row): ~180 bytes
RAG Chunks (per row): ~170 bytes
Integrity block:      ~150 bytes
Audit Summary:        ~300 bytes
```

For 3 tool calls + 5 RAG chunks: ~400 + 250 + 200 + 540 + 850 + 150 + 300 = ~2690 bytes (within 4096 limit).
For 10 tool calls + 20 RAG chunks: ~5500 bytes -- truncate tables, add full_trace_log_ref pointer.