---
kind: architecture
id: bld_architecture_agent_grounding_record
pillar: P08
llm_function: CONSTRAIN
purpose: Component inventory, dependency map, and system position for the agent_grounding_record builder
quality: 9.1
title: "Agent Grounding Record Builder -- Architecture"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, architecture]
tldr: "13 ISOs, 3 external standards (OTel, C2PA, SHA-256), P10 pillar position, upstream/downstream artifact map"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_manifest_agent_grounding_record
  - bld_architecture_memory_architecture
  - bld_architecture_agent_name_service_record
  - bld_architecture_consolidation_policy
  - bld_architecture_reasoning_strategy
  - bld_collaboration_agent_grounding_record
  - bld_architecture_procedural_memory
  - bld_architecture_tts_provider
  - bld_architecture_vad_config
  - bld_architecture_webinar_script
---
# Agent Grounding Record Builder -- Architecture

## Component Inventory (13 ISOs)

| # | ISO File | Kind | F | Role |
|---|----------|------|---|------|
| 1 | bld_manifest | type_builder | BECOME | Builder identity, routing |
| 2 | bld_instruction | instruction | REASON | 3-phase protocol: RESEARCH, COMPOSE, VALIDATE |
| 3 | bld_system_prompt | system_prompt | BECOME | Provenance specialist identity |
| 4 | bld_schema | schema | CONSTRAIN | Field definitions, types, JSON Schema |
| 5 | bld_quality_gate | quality_gate | GOVERN | H01-H08 + 5D scoring |
| 6 | bld_output_template | output_template | PRODUCE | Fill-in rendering template |
| 7 | bld_examples | examples | GOVERN | Golden + 2 anti-examples |
| 8 | bld_knowledge_card | knowledge_card | INJECT | OTel, C2PA, EU AI Act domain KC |
| 9 | bld_architecture | architecture | CONSTRAIN | Component map (this file) |
|10 | bld_collaboration | collaboration | COLLABORATE | Upstream/downstream flows |
|11 | bld_config | config | CONSTRAIN | Naming, paths, limits, hooks |
|12 | bld_memory | learning_record | INJECT | Pitfall patterns, learnings |
|13 | bld_tools | tools | CALL | Production + validation tools |
## 8F Activation Map

| 8F Function  | ISOs Loaded                                    | Purpose                                           |
|--------------|------------------------------------------------|---------------------------------------------------|
| F1 CONSTRAIN | bld_schema, bld_config, bld_architecture       | Validate naming, byte limit, required fields      |
| F2 BECOME    | bld_manifest, bld_system_prompt                | Adopt provenance specialist identity              |
| F3 INJECT    | bld_knowledge_card, bld_memory, bld_examples   | Load OTel/C2PA context + operational patterns     |
| F4 REASON    | bld_instruction                                | Phase-by-phase build protocol                     |
| F5 CALL      | bld_tools                                      | Hash verification, OTel validator, compile        |
| F6 PRODUCE   | bld_output_template                            | Render complete grounding record                  |
| F7 GOVERN    | bld_quality_gate, bld_examples                 | Hard gates + 5D scoring + anti-example comparison |
| F8 COLLABORATE| bld_collaboration                             | Signal upstream/downstream, commit, archive       |
## System Position

Inputs: trace_config (OTel span) + rag_source (chunk metadata) + toolkit (tool logs) + model_provider (model ref).
Output: p10_gr_[inference_id].md -> audit_log (aggregation) + conformity_assessment (EU AI Act evidence) + c2pa_manifest (content credentials).
## Dependency Map

### Internal CEX Dependencies

| Dependency Kind   | Artifact Path                              | How Used                                            |
|-------------------|--------------------------------------------|-----------------------------------------------------|
| trace_config      | P09/*/p09_tc_*.yaml                        | Provides otel_span_id via OTel instrumentation      |
| rag_source        | P01/*/p01_rs_*.md                          | Provides chunk_id, source_url metadata per chunk    |
| model_provider    | P02/*/p02_mp_*.md                          | Provides model.id, model.version, model.provider    |
| toolkit           | P04/*/p04_tk_*.md                          | Provides tool_name registry for tool_calls logging  |
| knowledge_index   | P10/*/p10_ki_*.md                          | May be queried as source for RAG chunks             |

### External Standard Dependencies

| Standard                    | Version  | Dependency Type | Required For                                  |
|-----------------------------|----------|-----------------|-----------------------------------------------|
| OTel GenAI Semantic Conventions | v1.37+ | Conceptual  | otel_span_id format, span attribute mapping   |
| C2PA Specification          | v2.3     | Conceptual      | c2pa_manifest_ref format, binding semantics   |
| SHA-256 (FIPS 180-4)        | FIPS 180-4 | Algorithm     | output_hash, content_hash, tool I/O hashes    |
| ISO 8601                    | 2019     | Format standard | All timestamp fields                          |
| W3C Trace Context           | Level 2  | Format standard | otel_span_id (16 hex char format)             |
| RFC 4122                    | 2005     | Format standard | inference_id (UUIDv4 format)                  |
## Pillar Position

| Property  | Value                    |
|-----------|--------------------------|
| Pillar    | P10 (Memory)             |
| Subdir    | P10_memory/grounding/    |
| Naming    | p10_gr_[prefix].md     |
| Max bytes | 4096                     |

P10 (Memory) is appropriate because grounding records are persistence artifacts -- they record the state of an inference run for future retrieval, audit, and analysis. They are not outputs (P05), not schemas (P06), not configurations (P09) -- they are memory artifacts that encode what happened during inference.
## Data Flow

3-phase: RESEARCH (collect OTel span + tool logs + RAG chunks + model ref) -> COMPOSE (sha256 hashes + grounding_coverage_pct + assemble per output_template) -> VALIDATE (H01-H08 gates + D1-D5 scoring). Output: p10_gr_[prefix].md to P10_memory/grounding/; signal to .cex/runtime/signals/.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_agent_grounding_record]] | downstream | 0.51 |
| [[bld_architecture_memory_architecture]] | sibling | 0.41 |
| [[bld_architecture_agent_name_service_record]] | sibling | 0.40 |
| [[bld_architecture_consolidation_policy]] | sibling | 0.38 |
| [[bld_architecture_reasoning_strategy]] | sibling | 0.37 |
| [[bld_collaboration_agent_grounding_record]] | downstream | 0.37 |
| [[bld_architecture_procedural_memory]] | sibling | 0.36 |
| [[bld_architecture_tts_provider]] | sibling | 0.36 |
| [[bld_architecture_vad_config]] | sibling | 0.36 |
| [[bld_architecture_webinar_script]] | sibling | 0.35 |
