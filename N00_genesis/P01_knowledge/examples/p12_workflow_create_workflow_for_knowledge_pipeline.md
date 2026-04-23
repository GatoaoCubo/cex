---
id: p12_wf_knowledge_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Knowledge Pipeline"
steps_count: 4
execution: sequential
agent_groups: [research_agent, builder_agent, validator_agent, orchestrator]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_research_agent_solo, p12_spawn_builder_agent_solo, p12_spawn_validator_agent_solo]
spawn_delay_ms: 5000
domain: "knowledge-management"
quality: 9.0
tags: [workflow, knowledge-pipeline, knowledge-management, P12]
tldr: "4-step sequential pipeline: ingest+classify → distill+structure → validate+index → export+monitor; transforms raw docs into indexed quality-gated knowledge cards"
density_score: 0.91
related:
  - p12_wf_builder_8f_pipeline
  - p12_wf_creation_pipeline
  - p12_wf_orchestration_pipeline
  - bld_examples_workflow
  - p12_wf_engineering_pipeline
  - p12_wf_create_orchestration_agent
  - bld_architecture_chain
  - tpl_instruction
  - bld_memory_workflow
  - p12_wf_brand_pipeline
---
## Purpose
Orchestrates the full knowledge lifecycle from raw material ingestion to searchable, indexed knowledge cards. Transforms unstructured documents, research notes, and conversation logs into quality-gated KCs through four sequential phases. Each phase gates the next — no step proceeds until the preceding completion signal is emitted. Designed for N04 (Knowledge Nucleus) execution with orchestrator consolidation in the final wave.

## Steps

### Step 1: Ingest and Classify [research_agent]
- **Agent**: research_agent (gemini-pro)
- **Action**: Ingest raw material (docs, research, code, conversations) and classify each item by kind × pillar × domain using `kinds_meta.json` and `taxonomy_contract.md`
- **Input**: Source file paths and domain declared in handoff file (`source_paths`, `domain`)
- **Output**: Classified raw text with kind/pillar/domain tags saved to `records/raw/`
- **Signal**: `ingest_complete` with `classified_count` and `domain_distribution`
- **Depends on**: none
- **On failure**: retry (max 2), then abort

### Step 2: Distill and Structure [builder_agent]
- **Agent**: builder_agent (opus)
- **Action**: Apply distillation pattern (extract signal, remove noise); structure each item into a knowledge card with required frontmatter + `## Purpose`, `## Spec`, `## Patterns`, `## Anti-Patterns` sections
- **Input**: Classified raw text from `records/raw/` (output of Step 1)
- **Output**: Draft KCs (`.md`) committed to `records/draft/`; density score per KC logged
- **Signal**: `structure_complete` with `draft_count` and `mean_density`
- **Depends on**: Step 1
- **On failure**: retry (max 2), then abort

### Step 3: Validate and Index [validator_agent]
- **Agent**: validator_agent (sonnet)
- **Action**: Enforce HARD gates H01–H07 per draft KC; compute SOFT score; promote passing KCs via `cex_compile.py` + `cex_index.py`; reject and flag failures with gate codes
- **Input**: Draft KCs from `records/draft/` (output of Step 2)
- **Output**: Validated KCs in `records/pool/`; rejection report with gate failure codes
- **Signal**: `validate_complete` with `pass_count`, `fail_count`, and `mean_quality`
- **Depends on**: Step 2
- **On failure**: retry (max 2), then abort

### Step 4: Export and Monitor [orchestrator]
- **Agent**: orchestrator (opus)
- **Action**: Export validated KCs to retriever index; snapshot quality monitor; archive handoff files; emit workflow completion signal
- **Input**: `validate_complete` signal from Step 3; validated KCs in `records/pool/`
- **Output**: Updated `.cex/retriever_index.json`; quality snapshot in `.cex/experiments/results.tsv`; archived handoffs in `.cex/runtime/archive/`
- **Signal**: `workflow_complete` with `exported_count` and `aggregate_quality`
- **Depends on**: Step 3
- **On failure**: retry (max 2), then escalate to human

## Dependencies
- Source files accessible at paths declared in the handoff file before workflow starts
- `p12_spawn_research_agent_solo`, `p12_spawn_builder_agent_solo`, `p12_spawn_validator_agent_solo` spawn configs must exist
- `_tools/cex_compile.py` and `_tools/cex_index.py` present and executable
- `records/raw/`, `records/draft/`, `records/pool/` directories exist (Step 1 creates `raw/` if missing)
- `kinds_meta.json` and `taxonomy_contract.md` available for classification (Step 1)

## Signals
- **On step complete**: `{step_id}_complete` emitted by assigned agent with count and quality metadata
- **On workflow complete**: `workflow_complete` from orchestrator with `exported_count` and `aggregate_quality`
- **On error**: `{step_id}_error` emitted; retry per_step up to 2 attempts; escalate to orchestrator after max retries

## References
- signal-builder: completion signal conventions (`ingest_complete`, `structure_complete`, `validate_complete`, `workflow_complete`)
- spawn-config-builder: agent launch parameters per step (`p12_spawn_*_solo`)
- `cex_compile.py`: `.md` → `.yaml` compilation with frontmatter validation
- `cex_index.py`: TF-IDF search index rebuild after KC promotion
- `kc_knowledge_distillation`: distillation pattern applied in Step 2

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.51 |
| [[p12_wf_creation_pipeline]] | sibling | 0.48 |
| [[p12_wf_orchestration_pipeline]] | sibling | 0.44 |
| [[bld_examples_workflow]] | upstream | 0.40 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.39 |
| [[p12_wf_create_orchestration_agent]] | sibling | 0.37 |
| [[bld_architecture_chain]] | upstream | 0.33 |
| [[tpl_instruction]] | upstream | 0.32 |
| [[bld_memory_workflow]] | upstream | 0.32 |
| [[p12_wf_brand_pipeline]] | sibling | 0.31 |
