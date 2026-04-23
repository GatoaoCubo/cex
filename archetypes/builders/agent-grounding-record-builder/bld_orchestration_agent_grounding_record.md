---
kind: collaboration
id: bld_collaboration_agent_grounding_record
pillar: P12
llm_function: COLLABORATE
purpose: Define crew role, upstream inputs, downstream consumers, and boundary conditions for grounding records
quality: 9.1
title: "Agent Grounding Record Builder -- Collaboration"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, collaboration]
tldr: "Receives span IDs from trace_config, chunk metadata from rag_source, tool logs from toolkit -- produces evidence for conformity_assessment and audit_log"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_agent_grounding_record
  - bld_memory_agent_grounding_record
  - bld_system_prompt_agent_grounding_record
  - bld_manifest_agent_grounding_record
  - bld_architecture_agent_grounding_record
  - bld_quality_gate_agent_grounding_record
  - kc_agent_grounding_record
  - bld_instruction_agent_grounding_record
  - bld_output_template_agent_grounding_record
  - bld_tools_agent_grounding_record
---
# Agent Grounding Record Builder -- Collaboration
## Crew Role
| Property | Value |
|----------|-------|
| Role | Per-inference provenance recorder and traceability chain builder |
| Primary nucleus | N04 (Knowledge) -- grounding records are memory/knowledge artifacts |
| Secondary nucleus | N05 (Operations) -- when OTel pipeline integration work is required |
| Trigger | Any AI inference run requiring auditability (production) or compliance (EU AI Act) |
| Output cadence | One artifact per inference run; async post-inference |

## Receives From (Upstream)

| Source | Path | Data | Required? |
|--------|------|------|-----------|
| trace_config | P09/*/p09_tc_*.yaml | otel_span_id | YES |
| rag_source | P01/*/p01_rs_*.md | chunk_id, source_url, retrieval_score | When RAG used |
| model_provider | P02/*/p02_mp_*.md | model.id, version, provider, signature | YES |
| toolkit | P04/*/p04_tk_*.md | tool_name registry, invocation logs | When tools used |
| knowledge_index | P10/*/p10_ki_*.md | chunk_id resolution | Optional |

**trace_config contract**: emit `gen_ai.operation.name` span, 16-hex span ID (W3C), ISO 8601 timestamps. Absent = H06 FAIL.
**rag_source contract**: log chunk_id + source_url (never null) + retrieval_score (0-1) + chunk text. Missing source_url = D2 collapses to 0.0.

## Produces For (Downstream)

| Consumer | Path | What It Uses | Priority |
|---------|------|--------------|---------|
| conformity_assessment | P08/*/p08_ca_*.md | PMM evidence (EU AI Act Art. 72) | HIGH |
| audit_log | P10/*/p10_al_*.md | Aggregated inference audit trail | HIGH |
| c2pa_manifest | External URI | output_hash + inference_id | MEDIUM |
| learning_record | P10/*/p10_lr_*.md | Cross-record pattern analysis | LOW |
| regression_check | P11/*/p11_rc_*.md | Grounding coverage trends | LOW |

**conformity_assessment contract**: expects inference_id + downstream_use="production" + grounding_coverage_pct + output_hash + c2pa_manifest_ref.
**audit_log contract**: records in P10_memory/grounding/ (p10_gr_INFERENCE_ID.md), complete, indexed by inference_id + timestamp.

## Boundary Definitions

| IS responsible for | IS NOT responsible for |
|-------------------|----------------------|
| Per-inference provenance (one record per run) | Training-time provenance (model_card) |
| Raw output-hash computation | Model behavior evaluation (benchmark / llm_judge) |
| Linking to OTel span via otel_span_id | Configuring OTel instrumentation (trace_config) |
| Capturing RAG-chunk metadata | Designing the RAG pipeline (rag_source) |
| Linking to C2PA manifest | Generating the C2PA manifest (external tool) |
| Recording tool invocations with hashes | Defining tool interface (toolkit / mcp_server) |
| grounding_coverage_pct computation | Semantic quality scoring (scoring_rubric) |

grounding record = STRUCTURED PROVENANCE LAYER above raw OTel spans. trace_config configures what to capture; agent_grounding_record records what happened. Spans are raw telemetry; grounding records are compliance-grade provenance.

## Signal Protocol

```bash
python _tools/cex_compile.py P10_memory/grounding/p10_gr_INFERENCE_ID.md
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
git add P10_memory/grounding/p10_gr_INFERENCE_ID.md
git commit -m "[N04] add grounding record p10_gr_INFERENCE_ID -- per-inference provenance"
```

## Multi-Nucleus Workflow

Wave 1: N04 produces grounding records -> Wave 2: N05 validates OTel + schema -> Wave 3: N04 aggregates into audit_log; N06 prepares conformity_assessment evidence. Use proposal pattern for shared file modifications. See `.claude/rules/shared-file-proposal.md`.

## Collaboration Checklist

| Check | Gate |
|-------|------|
| All hard gates H01-H08 pass | HARD |
| Score >= 9.0 (or >= 8.0 with waiver) | SOFT |
| Artifact saved to P10_memory/grounding/ | REQUIRED |
| cex_compile.py run without errors | REQUIRED |
| Signal sent to N07 | REQUIRED |
| Git commit with tracing message | REQUIRED |
| audit_log index updated (if exists) | RECOMMENDED |
| c2pa_manifest_ref resolved (if C2PA active) | RECOMMENDED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_agent_grounding_record]] | upstream | 0.54 |
| [[bld_memory_agent_grounding_record]] | upstream | 0.53 |
| [[bld_system_prompt_agent_grounding_record]] | upstream | 0.50 |
| [[bld_manifest_agent_grounding_record]] | upstream | 0.48 |
| [[bld_architecture_agent_grounding_record]] | upstream | 0.47 |
| [[bld_quality_gate_agent_grounding_record]] | upstream | 0.40 |
| [[kc_agent_grounding_record]] | upstream | 0.39 |
| [[bld_instruction_agent_grounding_record]] | upstream | 0.39 |
| [[bld_output_template_agent_grounding_record]] | upstream | 0.39 |
| [[bld_tools_agent_grounding_record]] | upstream | 0.37 |
