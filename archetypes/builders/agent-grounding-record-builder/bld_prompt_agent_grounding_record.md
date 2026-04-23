---
kind: instruction
id: bld_instruction_agent_grounding_record
pillar: P03
llm_function: REASON
purpose: Step-by-step build instructions for producing a valid agent_grounding_record artifact
quality: 9.1
title: "Agent Grounding Record Builder -- Instructions"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, instruction]
tldr: "Three-phase protocol: RESEARCH (collect traces), COMPOSE (populate record), VALIDATE (gate checks)"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_system_prompt_agent_grounding_record
  - kc_agent_grounding_record
  - bld_manifest_agent_grounding_record
  - bld_output_template_agent_grounding_record
  - bld_memory_agent_grounding_record
  - bld_knowledge_card_agent_grounding_record
  - bld_examples_agent_grounding_record
  - bld_schema_agent_grounding_record
  - bld_quality_gate_agent_grounding_record
  - bld_collaboration_agent_grounding_record
---
# Agent Grounding Record Builder -- Instructions
## Overview
A grounding record is a structured per-inference provenance artifact. It answers:
"What sources, tools, and model produced this output -- and can I prove it?"
Each record covers exactly ONE inference run. Do not aggregate multiple runs into one record.
## Phase 1 -- RESEARCH (F3 INJECT + F5 CALL)
Collect all evidence from the inference session before writing a single field.
### Step 1.1 -- Identify Tool Calls
| Action                          | Detail                                                                      |
|---------------------------------|-----------------------------------------------------------------------------|
| Extract tool invocation log     | Get tool_name, input payload hash, output payload hash for every call      |
| Record timestamps               | ISO 8601 per tool-call -- not just session start/end                        |
| Measure duration_ms             | Wall-clock milliseconds from invocation to response                        |
| Flag tool-call failures         | If a tool errored, include it with status: "error" and error_code field    |
### Step 1.2 -- Collect RAG-Chunk Metadata
| Action                          | Detail                                                                      |
|---------------------------------|-----------------------------------------------------------------------------|
| List all retrieved chunks       | Every chunk the retriever returned, even if not used in the final output   |
| Capture source_url              | Full URL or internal path -- no source_url = untraceable output (FAIL)     |
| Record retrieval_score          | Cosine similarity or BM25 score as float                                   |
| Compute content_hash            | SHA-256 of the chunk text at retrieval time                                |
| Record chunk_id                 | Unique identifier from the vector store or document store                  |
### Step 1.3 -- Capture Model Reference
| Action                          | Detail                                                                      |
|---------------------------------|-----------------------------------------------------------------------------|
| Model ID                        | Exact model identifier (e.g. claude-sonnet-4-6, gpt-4o-2024-11-20)       |
| Model version                   | Semantic version or checkpoint hash if available                           |
| Provider                        | anthropic / openai / google / self-hosted                                  |
| Model-signature                 | Cryptographic hash or attestation from provider if available               |
### Step 1.4 -- Establish Inference Session Identity
| Action                          | Detail                                                                      |
|---------------------------------|-----------------------------------------------------------------------------|
| Generate inference_id           | UUIDv4 -- unique per inference run, never reused                           |
| Link to session_id              | Parent session if this inference is part of a multi-turn conversation      |
| Get otel_span_id                | The OpenTelemetry span ID for this inference operation                     |
| Timestamp the session           | ISO 8601 with timezone -- start of inference, not start of session         |
### Step 1.5 -- Prepare Output Hash Input
| Action                          | Detail                                                                      |
|---------------------------------|-----------------------------------------------------------------------------|
| Capture raw model output        | Exact bytes before any post-processing or formatting                       |
| Compute output-hash             | SHA-256 of raw output bytes -- this is MANDATORY, cannot be omitted        |
| Record hash algorithm           | Always "sha256" -- no MD5, no SHA-1                                        |
## Phase 2 -- COMPOSE (F6 PRODUCE)
Populate the grounding record fields in this exact order. Use bld_output_template for the structure.
### Step 2.1 -- Header Block
```
inference_id: <UUIDv4>
session_id: <string or null>
timestamp: <ISO 8601 with timezone>
downstream_use: <production | test | eval>
grounding_coverage_pct: <float 0.0-1.0>
```
Compute grounding_coverage_pct as:
  (number of output claims with a traceable RAG-chunk or tool-call source)
  divided by
  (total factual claims in output)
If uncertain, use 0.0 -- do not guess.
### Step 2.2 -- Model Block
```
model:
  id: <exact model identifier>
  version: <version string>
  provider: <provider name>
  model-signature: <hash or attestation string, null if unavailable>
```
### Step 2.3 -- Tool Calls Array
For each tool invocation, one entry:
```
tool_calls:
  - tool_name: <string>
    tool_input_hash: <sha256 of input payload>
    tool_output_hash: <sha256 of output payload>
    duration_ms: <integer>
    timestamp: <ISO 8601>
    status: <success | error>
```
If no tools were called, write: `tool_calls: []`
### Step 2.4 -- RAG Chunks Array
For each retrieved chunk, one entry:
```
rag_chunks:
  - chunk_id: <string>
    source_url: <full URL or internal path>
    retrieval_score: <float>
    content_hash: <sha256 of chunk text at retrieval>
```
If no RAG was used, write: `rag_chunks: []`
### Step 2.5 -- Integrity and Compliance Fields
```
output_hash: <sha256 of raw model output>
otel_span_id: <OTel span ID string>
c2pa_manifest_ref: <C2PA manifest URI or null>
```
## Phase 3 -- VALIDATE (F7 GOVERN)
Run this checklist before finalizing the record. Any FAIL = do not publish.
### Hard Gate Checklist
| Gate | Check                                        | Pass Condition                        |
|------|----------------------------------------------|---------------------------------------|
| H01  | Frontmatter valid YAML                       | No parse errors                       |
| H02  | ID matches naming pattern                    | ^p10_gr_[a-z0-9_]+\.md$              |
| H03  | kind = agent_grounding_record                | Exact string match                    |
| H04  | inference_id present                         | UUIDv4 format                         |
| H05  | output-hash present                          | SHA-256 hex string (64 chars)         |
| H06  | otel_span_id present                         | Non-empty string                      |
| H07  | timestamp is ISO 8601                        | Parseable with timezone               |
| H08  | model.id present                             | Non-empty string                      |
### Soft Quality Checks
| Dimension                | Weight | Check                                             |
|--------------------------|--------|---------------------------------------------------|
| Provenance completeness  | 0.30   | All fields populated, no null where required      |
| RAG-chunk coverage       | 0.25   | Every chunk has source_url and content_hash       |
| Tool-call traceability   | 0.25   | Every tool-call has input/output hashes + timestamp|
| C2PA integration         | 0.10   | c2pa_manifest_ref present or explicitly null      |
| Downstream tracking      | 0.10   | downstream_use field set                          |
### Common Failures and Fixes
| Failure Pattern                       | Fix                                                  |
|---------------------------------------|------------------------------------------------------|
| output-hash missing                   | Recompute SHA-256 from raw model output bytes        |
| RAG chunk has no source_url           | Trace back to retriever config; reject chunk if unknown|
| tool_input_hash = null                | Re-run tool call logging with hash capture enabled   |
| otel_span_id missing                  | Check OTel instrumentation -- span must be active    |
| grounding_coverage_pct > 1.0          | Recompute -- value is a ratio, not a percentage      |
| inference_id reused                   | Generate new UUIDv4 -- IDs are non-reusable          |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_agent_grounding_record]] | related | 0.46 |
| [[kc_agent_grounding_record]] | upstream | 0.40 |
| [[bld_manifest_agent_grounding_record]] | downstream | 0.40 |
| [[bld_output_template_agent_grounding_record]] | downstream | 0.40 |
| [[bld_memory_agent_grounding_record]] | downstream | 0.38 |
| [[bld_knowledge_card_agent_grounding_record]] | upstream | 0.36 |
| [[bld_examples_agent_grounding_record]] | downstream | 0.33 |
| [[bld_schema_agent_grounding_record]] | downstream | 0.32 |
| [[bld_quality_gate_agent_grounding_record]] | downstream | 0.30 |
| [[bld_collaboration_agent_grounding_record]] | downstream | 0.27 |
