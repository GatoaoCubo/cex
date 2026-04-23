---
id: n00_agent_grounding_record_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Agent Grounding Record -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, agent_grounding_record, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_audit_log
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_eval_metric
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An agent_grounding_record captures per-inference provenance: which tool calls were made, which RAG chunks were retrieved, and which model version signed the output. It enables reproducibility, auditability, and debugging of agent decisions at the individual inference level.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_grounding_record` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| inference_id | string | yes | Unique ID for the inference run |
| model_signature | string | yes | Model name + version that produced the output |
| tool_calls | array | yes | List of tool invocations with inputs/outputs |
| rag_chunks | array | no | Retrieved document chunks with scores and sources |
| timestamp | datetime | yes | ISO-8601 timestamp of inference |
| nucleus | string | yes | Nucleus that ran the inference |

## When to use
- When you need to audit why an agent produced a specific output
- When debugging RAG pipelines or tool call failures
- When building compliance reports that require inference-level provenance

## Builder
`archetypes/builders/agent_grounding_record-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_grounding_record --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: agr_n04_session_001
kind: agent_grounding_record
pillar: P10
nucleus: n04
title: "Example Agent Grounding Record"
version: 1.0
quality: null
---
# Inference Provenance
inference_id: inf_20260417_001
model_signature: claude-sonnet-4-6
tool_calls: [{tool: read_file, input: kc_agent.md, output: "200 chars"}]
```

## Related kinds
- `learning_record` (P10) -- captures what worked/failed after grounding is analyzed
- `audit_log` (P11) -- immutable audit trail that may reference grounding records
- `runtime_state` (P10) -- session-level state that grounding records augment

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.47 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.46 |
| [[bld_schema_audit_log]] | upstream | 0.45 |
| [[bld_schema_dataset_card]] | upstream | 0.45 |
| [[bld_schema_integration_guide]] | upstream | 0.45 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.44 |
| [[bld_schema_eval_metric]] | upstream | 0.44 |
| [[bld_schema_pitch_deck]] | upstream | 0.43 |
| [[bld_schema_action_paradigm]] | upstream | 0.43 |
