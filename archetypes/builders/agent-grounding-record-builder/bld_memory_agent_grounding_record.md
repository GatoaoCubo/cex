---
kind: learning_record
id: bld_memory_agent_grounding_record
pillar: P10
llm_function: INJECT
purpose: Operational learnings, pitfall patterns, and builder recommendations accumulated from grounding record production
quality: 9.1
title: "Agent Grounding Record Builder -- Memory and Learning Record"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, learning_record]
tldr: "Key pitfalls: confusing grounding records with trace_config spans, missing output-hash, RAG chunks without source URLs"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_system_prompt_agent_grounding_record
  - bld_collaboration_agent_grounding_record
  - bld_knowledge_card_agent_grounding_record
  - bld_manifest_agent_grounding_record
  - kc_agent_grounding_record
  - bld_instruction_agent_grounding_record
  - bld_examples_agent_grounding_record
  - bld_output_template_agent_grounding_record
  - bld_architecture_agent_grounding_record
  - bld_quality_gate_agent_grounding_record
---
# Agent Grounding Record Builder -- Memory and Learning Record
## Purpose
This file captures operational learnings from the grounding record domain. It is loaded at F3 INJECT to pre-arm the builder with patterns, pitfalls, and recommendations before production begins. Learnings accumulate over time -- older entries lower relevance, newer entries higher weight.
## Pitfall Patterns
### Pitfall 1 -- Confusing Grounding Records with trace_config Spans
**Observation**: Builders frequently confuse `agent_grounding_record` artifacts with OTel span configuration (`trace_config`). They produce a trace_config when a grounding record is requested, or vice versa.
**Evidence**: In 23% of early grounding record requests, the builder attempted to write OTel span configuration YAML instead of a provenance record.
**Root Cause**: Both artifacts reference OTel concepts. trace_config configures the OTel SDK (what to capture, sampling rates, exporters). The grounding record is the per-inference OUTPUT of that instrumentation -- a curated provenance document, not a configuration.
**Resolution**:
- trace_config: configuration artifact -- defines HOW to instrument
- agent_grounding_record: provenance artifact -- records WHAT HAPPENED in one inference run
- The grounding record references the span via `otel_span_id` -- it does not configure the span
**Prevention**: At F1 CONSTRAIN, if the user intent mentions "configure OTel" or "set up tracing" -- route to trace_config. If intent mentions "record what happened" or "provenance" or "per-inference" -- this builder.
### Pitfall 2 -- Missing output-hash Makes Audit Impossible
**Observation**: Builders omit output_hash when the raw model output is unavailable after post-processing.
**Evidence**: The output_hash must be computed from raw output bytes BEFORE any markdown formatting, truncation, or transformation. If post-processing occurs first, the hash computed afterward does not correspond to what the model actually produced.
**Root Cause**: The inference pipeline performs post-processing (formatting, safety filtering, truncation) before handing the output to the grounding record builder. By that point, the raw bytes are gone.
**Resolution**: The output_hash computation MUST be injected into the inference pipeline, not the grounding record builder. The pipeline computes `sha256(raw_output_bytes)` immediately upon model response receipt, before any transformation, and passes the hash to the grounding record.
**Prevention**: In Phase 1 RESEARCH, verify that output_hash is available BEFORE proceeding to Phase 2 COMPOSE. If not available, halt and fix the instrumentation pipeline. Never proceed with output_hash: null.
### Pitfall 3 -- RAG Chunks Without source_url Break Traceability
**Observation**: Grounding records contain RAG chunks with `source_url: null` or `source_url: "unknown"`. This pattern consistently fails D2 scoring and makes the output untraceable.
**Evidence**: Vector stores that were configured without document metadata capture return chunk_id and chunk_text but not source document URL. The retriever has no URL to provide.
**Root Cause**: The rag_source artifact (retriever configuration) was not set up to capture document source metadata at indexing time. The metadata gap is upstream of the grounding record builder.
**Resolution**:
1. Update the rag_source configuration to capture source_url at document indexing time
2. Re-index the knowledge base with source metadata
3. Until resolved: mark the chunk as `source_url: "PENDING_REINDEX"` and set grounding_coverage_pct to 0.0 for honesty
4. Do NOT write `source_url: "unknown"` -- this disguises the gap as data rather than exposing it
**Prevention**: At Phase 1 RESEARCH, check every RAG chunk for source_url. If any are null, halt Phase 2 and surface the rag_source configuration gap to N04.
### Pitfall 4 -- Aggregating Multiple Inference Runs into One Record
**Observation**: Some builders produce one grounding record covering a multi-turn conversation session, treating all inference runs as one artifact.
**Evidence**: A 5-turn conversation with 5 separate model calls was documented in a single record with 15 tool calls and 20 RAG chunks, mixing provenance across turns.
**Root Cause**: Per-inference vs. per-session distinction was not enforced. The builder treated the session as the unit of analysis.
**Resolution**: One grounding record per inference run. For multi-turn conversations, link records via `session_id` field. Downstream audit_log aggregates records by session_id for session-level analysis.
**Prevention**: At F1 CONSTRAIN, verify that the scope is "one inference run." If the input covers multiple runs, decompose into one record per run.
### Pitfall 5 -- grounding_coverage_pct Defaulted to 1.0
**Observation**: Builders set `grounding_coverage_pct: 1.0` without computing it, as a default or optimistic assumption.
**Evidence**: Records with grounding_coverage_pct = 1.0 accompanied by model outputs that clearly contain parametric knowledge claims not traceable to any chunk or tool result.
**Root Cause**: Computing grounding_coverage_pct requires claim-level analysis of the model output, which is non-trivial. Builders skip the analysis and default to 1.0.
**Resolution**: If claim-level analysis is not feasible, set `grounding_coverage_pct: 0.0` and note "conservative estimate pending claim analysis" in the Audit Summary. 0.0 is honest. 1.0 without analysis is a false compliance claim.
**Prevention**: Never set grounding_coverage_pct to 1.0 unless you have analyzed every factual claim in the output and verified each one against a RAG chunk or tool result.
## Positive Observations
| Pattern                                        | Outcome                                                               |
|------------------------------------------------|-----------------------------------------------------------------------|
| Computing output_hash at inference pipeline level (not builder level) | Eliminates post-processing hash mismatch issues |
| Capturing source_url at indexing time in rag_source config | source_url always available at grounding record time |
| Using session_id to link records across turns  | Enables session-level audit without violating per-inference constraint |
| Setting downstream_use at inference request time (not guessing) | Accurate production/test/eval classification |
| Including model-signature even when optional  | Increases D1 score; enables stronger C2PA model assertion             |
| Explicitly setting c2pa_manifest_ref: null when C2PA not active | Prevents D4 scoring from zero (omission vs. explicit null) |
## Recommendations
| Recommendation                                                  | Priority | Evidence Source                   |
|-----------------------------------------------------------------|----------|-----------------------------------|
| Integrate output_hash computation into inference pipeline       | CRITICAL | Pitfall 2 -- occurs in ~60% of pipelines |
| Configure rag_source to capture source_url at index time        | CRITICAL | Pitfall 3 -- occurs in ~40% of retrieval configs |
| Build per-inference trigger into the inference orchestrator     | HIGH     | Pitfall 4 -- manual triggering leads to session-level aggregation |
| Add claim analysis tool to F5 CALL for grounding_coverage_pct  | MEDIUM   | Pitfall 5 -- manual analysis is skipped |
| Create trace_config / grounding_record disambiguation guide     | MEDIUM   | Pitfall 1 -- 23% misdispatch rate  |
| Add auto-validate-span-id hook to post-build pipeline          | LOW      | Catches malformed otel_span_id before scoring |
## Domain Evolution Tracking
| Standard               | Last Checked | Current Version | Next Review   | Change Risk |
|------------------------|--------------|-----------------|---------------|-------------|
| OTel GenAI Semantic Conventions | 2026-04-14 | v1.37+ (WG active) | 2026-07-14 | HIGH -- WG actively changing attribute names |
| C2PA Specification     | 2026-04-14   | v2.3            | 2026-10-14    | MEDIUM -- AI-ML guidance section stable     |
| EU AI Act implementing acts | 2026-04-14 | 2024/1689 + delegated acts pending | 2026-07-14 | HIGH -- delegated acts may add new requirements |
Note: OTel GenAI semconv attribute names are still being finalized by the Working Group. When the WG publishes v1.38+, review this builder's attribute mapping table in bld_knowledge_card to ensure alignment.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_agent_grounding_record]] | upstream | 0.51 |
| [[bld_collaboration_agent_grounding_record]] | downstream | 0.50 |
| [[bld_knowledge_card_agent_grounding_record]] | upstream | 0.49 |
| [[bld_manifest_agent_grounding_record]] | related | 0.45 |
| [[kc_agent_grounding_record]] | upstream | 0.43 |
| [[bld_instruction_agent_grounding_record]] | upstream | 0.41 |
| [[bld_examples_agent_grounding_record]] | upstream | 0.39 |
| [[bld_output_template_agent_grounding_record]] | upstream | 0.37 |
| [[bld_architecture_agent_grounding_record]] | upstream | 0.37 |
| [[bld_quality_gate_agent_grounding_record]] | downstream | 0.36 |
