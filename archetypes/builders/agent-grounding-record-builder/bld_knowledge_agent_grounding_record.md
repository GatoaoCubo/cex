---
kind: knowledge_card
id: bld_knowledge_card_agent_grounding_record
pillar: P01
llm_function: INJECT
purpose: Domain knowledge reference for OTel GenAI semconv, C2PA, and per-inference provenance standards
quality: 9.2
title: "Agent Grounding Record -- Knowledge Card"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, knowledge_card]
tldr: "OTel v1.37+ GenAI semconv + C2PA v2.3 AI-ML guidance + EU AI Act provenance requirements -- complete domain reference"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_manifest_agent_grounding_record
  - bld_system_prompt_agent_grounding_record
  - kc_agent_grounding_record
  - bld_instruction_agent_grounding_record
  - bld_output_template_agent_grounding_record
  - bld_memory_agent_grounding_record
  - bld_collaboration_agent_grounding_record
  - bld_architecture_agent_grounding_record
  - bld_examples_agent_grounding_record
  - bld_quality_gate_agent_grounding_record
---
# Agent Grounding Record -- Knowledge Card

## Domain Overview

Per-inference provenance is the practice of recording, for each AI inference run, the exact sources and transformations that produced the output. This enables:

1. **Auditability**: Regulators and downstream consumers can verify AI outputs against their stated sources.
2. **EU AI Act compliance**: Article 9 (risk management) and Article 72 (post-market-monitoring) require traceability of high-risk AI system outputs.
3. **Content authenticity**: C2PA content credentials allow consumers to verify the provenance of AI-generated content.
4. **Observability**: OTel GenAI semantic conventions standardize how AI inference is instrumented for distributed tracing.

The grounding record is the per-inference artifact that binds these four concerns into a single, structured, machine-verifiable document.

## Key Concepts

| Concept               | Definition                                                                                             | CEX Field          |
|-----------------------|--------------------------------------------------------------------------------------------------------|--------------------|
| grounding             | The act of anchoring an AI output claim to a traceable external source (RAG chunk or tool result)      | rag_chunks, tool_calls |
| provenance            | The documented origin and transformation history of an AI output                                       | Full record structure |
| per-inference         | One record per inference run; not aggregated across sessions or turns                                  | inference_id        |
| tool-call trace       | Log of every external tool invoked during an inference run, including inputs and outputs               | tool_calls array    |
| RAG-chunk             | A retrieved text segment from a knowledge source used to augment the model's context                   | rag_chunks array    |
| model-signature       | A cryptographic attestation of the model identity, issued by the model provider                        | model.model-signature |
| output-hash           | SHA-256 hash of the raw model output, used to prove the record corresponds to a specific response      | output_hash         |
| C2PA manifest         | A structured content credential (C2PA v2.3) that binds provenance metadata to a piece of content      | c2pa_manifest_ref   |
| OTel span             | An OpenTelemetry distributed trace span representing one unit of work (one inference operation)        | otel_span_id        |
| traceability chain    | The end-to-end linkage from user input through retrieval, tools, and model to the final output hash    | Full record         |
| downstream use        | The intended application of the inference output (production / test / eval)                            | downstream_use      |
| grounding coverage    | The fraction of output claims that can be traced to an explicit grounding source                       | grounding_coverage_pct |

## Industry Standards

| Standard                          | Version     | Relevance                                                                              |
|-----------------------------------|-------------|----------------------------------------------------------------------------------------|
| OTel GenAI Semantic Conventions   | v1.37+ (WG) | Defines span attributes for AI inference: model ID, input tokens, output tokens, tool calls |
| C2PA (Coalition for Content Provenance) | v2.3 | AI-ML guidance: content credentials for AI-generated outputs, model assertions        |
| SHA-256 (FIPS 180-4)              | FIPS 180-4  | Hash standard for output_hash, content_hash, tool input/output hashes                 |
| ISO 8601                          | 2019        | Timestamp format for all time fields                                                   |
| W3C Provenance (PROV-DM)          | 2013        | Conceptual model for provenance: entities, activities, agents                          |
| W3C Trace Context                 | Level 2     | Defines traceparent header format; otel_span_id follows W3C 16-hex-char format         |
| EU AI Act                         | 2024/1689   | Articles 9 + 72 + 73: risk management + post-market-monitoring + incident reporting    |

## OTel GenAI Semantic Conventions -- Key Attributes

The grounding record maps to OTel GenAI semconv attributes. When instrumenting the inference pipeline, these OTel attributes SHOULD be captured and referenced in the grounding record.

| OTel Attribute                     | Type   | Grounding Record Field      | Notes                                              |
|------------------------------------|--------|-----------------------------|----------------------------------------------------|
| gen_ai.system                      | string | model.provider              | "anthropic", "openai", "google", etc.              |
| gen_ai.request.model               | string | model.id                    | Requested model identifier                         |
| gen_ai.response.model              | string | model.id (prefer this)      | Actual model that responded (may differ from request) |
| gen_ai.operation.name              | string | -- (context only)           | "chat", "completions", "embeddings"                |
| gen_ai.usage.input_tokens          | int    | -- (optional extension)     | Input token count                                  |
| gen_ai.usage.output_tokens         | int    | -- (optional extension)     | Output token count                                 |
| gen_ai.tool.call.id                | string | tool_calls[*].tool_name     | Tool invocation ID                                 |
| gen_ai.tool.name                   | string | tool_calls[*].tool_name     | Tool name as registered                            |

The OTel span identified by `otel_span_id` SHOULD contain these attributes. The grounding record is a STRUCTURED PROVENANCE LAYER built on top of the raw OTel span -- it is not a replacement for OTel instrumentation.

## C2PA v2.3 AI-ML Guidance -- Key Concepts

C2PA v2.3 introduced specific guidance for AI-generated content. A C2PA manifest contains assertions that can be bound to an AI output.

| C2PA Assertion Type         | Purpose                                                                    | Grounding Record Linkage           |
|-----------------------------|----------------------------------------------------------------------------|------------------------------------|
| c2pa.training-mining        | Documents if the model was trained on content                              | Linked via c2pa_manifest_ref       |
| c2pa.ai-generative-training | Declares AI-generated training data usage                                  | Linked via c2pa_manifest_ref       |
| c2pa.actions                | Records what actions were taken to produce the content                     | Linked via c2pa_manifest_ref       |
| c2pa.hash.data              | Cryptographic hash binding the manifest to specific content bytes          | output_hash is the binding anchor  |
| c2pa.soft-binding           | Non-cryptographic binding for content that may be transformed              | Alternative to output_hash         |

The grounding record's `output_hash` serves as the cryptographic anchor for C2PA hard-binding. The `c2pa_manifest_ref` URI points to the full C2PA manifest that contains the broader content credential chain.

## EU AI Act -- Provenance Requirements (High-Risk Systems)

| Article | Requirement                              | How Grounding Record Fulfills It                              |
|---------|------------------------------------------|---------------------------------------------------------------|
| Art. 9  | Risk management system                   | Grounding records enable systematic tracking of output sources |
| Art. 12 | Record-keeping                           | Grounding records ARE the per-inference records required      |
| Art. 72 | Post-market monitoring                   | downstream_use field enables filtering production records      |
| Art. 73 | Serious incident reporting               | output_hash + inference_id enable precise incident attribution |

Note: EU AI Act applicability depends on system classification. Consult legal counsel for classification decisions. These grounding records provide the technical foundation for compliance -- they do not constitute legal compliance in themselves.

## Relationship to Adjacent Artifact Kinds

| Kind             | Relationship                                                                                    |
|------------------|-------------------------------------------------------------------------------------------------|
| trace_config     | Configures the OTel pipeline that PRODUCES the spans this record references -- different layer  |
| model_card       | Documents the MODEL -- training data, capabilities, limitations -- not per-inference           |
| rag_source       | Configures the retrieval pipeline -- this record captures the RESULTS of that pipeline         |
| audit_log        | Aggregates multiple grounding records for audit purposes -- uses this record as input           |
| conformity_assessment | Uses grounding records as evidence for EU AI Act conformity assessment               |
| learning_record  | Captures learnings FROM grounding records -- pattern analysis across many records              |

## Common Pitfalls

| Pitfall                                          | Consequence                                                    | Prevention                                    |
|--------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------|
| Confusing grounding record with trace_config     | Wrong artifact for the intent; trace_config is configuration  | Read bld_collaboration for boundary definition |
| Missing output-hash                              | Record proves nothing; audit is impossible                     | Compute before post-processing                |
| RAG chunks without source_url                    | Output is untraceable; C2PA binding fails                      | Fix RAG pipeline to capture source metadata   |
| Aggregating multiple inference runs              | Violates per-inference constraint; provenance becomes ambiguous| Generate one record per inference run         |
| Using SHA-1 or MD5 for hashes                   | Not FIPS-compliant; considered broken for provenance use       | Use SHA-256 exclusively                       |
| grounding_coverage_pct = 1.0 without analysis   | Misleading compliance claim                                    | Compute honestly; 0.0 is better than false 1.0|

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_agent_grounding_record]] | downstream | 0.55 |
| [[bld_system_prompt_agent_grounding_record]] | downstream | 0.53 |
| [[kc_agent_grounding_record]] | sibling | 0.49 |
| [[bld_instruction_agent_grounding_record]] | downstream | 0.47 |
| [[bld_output_template_agent_grounding_record]] | downstream | 0.42 |
| [[bld_memory_agent_grounding_record]] | downstream | 0.41 |
| [[bld_collaboration_agent_grounding_record]] | downstream | 0.39 |
| [[bld_architecture_agent_grounding_record]] | downstream | 0.36 |
| [[bld_examples_agent_grounding_record]] | downstream | 0.35 |
| [[bld_quality_gate_agent_grounding_record]] | downstream | 0.31 |
