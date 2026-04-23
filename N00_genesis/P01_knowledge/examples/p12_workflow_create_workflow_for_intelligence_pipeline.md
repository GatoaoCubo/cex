---
id: p12_wf_intelligence_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Intelligence Pipeline"
steps_count: 3
execution: sequential
agent_groups: [n01, n04, n07]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [n01_research_complete, n04_analysis_complete, workflow_complete, workflow_error]
spawn_configs: [p12_spawn_n01_solo_research, p12_spawn_n04_solo_analysis]
domain: "intelligence"
quality: 9.0
tags: [workflow, intelligence, research, sequential, P12]
tldr: "3-step sequential pipeline: N01 collects intelligence, N04 processes into knowledge artifacts, N07 consolidates into actionable brief"
density_score: 0.91
related:
  - p12_wf_orchestration_pipeline
  - p12_wf_create_orchestration_agent
  - spec_n01_n04_verticalization
  - p12_wf_creation_pipeline
  - p12_wf_knowledge_pipeline
  - bld_examples_workflow
  - n07_output_orchestration_audit
  - p01_kc_orchestration_best_practices
  - bld_collaboration_kind
  - p12_wf_admin_orchestration
---
## Purpose
Orchestrates end-to-end intelligence gathering and analysis. N01 (Gemini 2.5-pro, 1M ctx) collects raw data from multiple sources; N04 processes findings into structured knowledge cards and embedding-ready artifacts; N07 consolidates into a final intelligence brief and archives all handoffs. Each step gates the next — no parallel execution — to preserve analytical rigor and data provenance.

## Steps

### Step 1: Intelligence Collection [n01]
- **Agent**: n01 (gemini-2.5-pro)
- **Action**: Gather raw intelligence from designated sources; produce research artifacts with source citations
- **Input**: Collection targets and scope from `.cex/runtime/handoffs/{MISSION}_n01.md`
- **Output**: Research artifacts committed to `N01_intelligence/` with quality score
- **Signal**: `n01_research_complete` (emitted after commit; includes `data_quality_score`)
- **Depends on**: none (initial step)
- **On failure**: retry (max 1), then emit `n01_error` → escalate to N07

### Step 2: Knowledge Analysis [n04]
- **Agent**: n04 (gemini-2.5-pro)
- **Action**: Process N01 research artifacts into structured knowledge cards, embedding configs, and retrieval-ready chunks
- **Input**: Research artifacts from `N01_intelligence/` produced in Step 1
- **Output**: Knowledge cards and embedding configs committed to `N04_knowledge/`
- **Signal**: `n04_analysis_complete` (emitted after commit; includes `artifacts_count`)
- **Depends on**: Step 1 (`n01_research_complete`)
- **On failure**: retry (max 1), then emit `n04_error` → escalate to N07

### Step 3: Consolidation [n07]
- **Agent**: n07 (claude-opus)
- **Action**: Review N01 + N04 outputs; compose final intelligence brief; archive handoffs; push consolidated commit
- **Input**: Signals `n01_research_complete` + `n04_analysis_complete`; git log; artifacts in N01 and N04 directories
- **Output**: Intelligence brief at `N07_orchestration/briefs/{MISSION}_brief.md`; archived handoffs; consolidated git commit
- **Signal**: `workflow_complete` (includes aggregate quality, step scores, artifact count)
- **Depends on**: Steps 1 and 2
- **On failure**: abort; emit `workflow_error` with last known state

## Dependencies
- Handoff file must exist at `.cex/runtime/handoffs/{MISSION}_n01.md` before workflow starts
- `spawn_configs` referenced must be valid: `p12_spawn_n01_solo_research`, `p12_spawn_n04_solo_analysis`
- N01 and N04 cannot git commit — N07 consolidates their output (see n07-orchestrator.md)
- `.cex/runtime/signals/` directory must be writable for signal emission

## Signals
- **`n01_research_complete`**: emitted by N07 on N01's behalf after consolidating N01 output; carries `data_quality_score`
- **`n04_analysis_complete`**: emitted by N07 on N04's behalf after consolidating N04 output; carries `artifacts_count`
- **`workflow_complete`**: emitted by N07 after brief is committed and handoffs archived; carries `aggregate_quality` and `step_scores` map
- **`workflow_error`**: emitted on unrecoverable failure; carries `failed_step` and `last_known_state`
- Signal schema: see `signal-builder` conventions; all signals written to `.cex/runtime/signals/`

## References
- N01 rules: `.claude/rules/n01-intelligence.md`
- N04 rules: `.claude/rules/n04-knowledge.md`
- N07 consolidate protocol: `.claude/rules/n07-orchestrator.md` § Consolidate Protocol
- Signal conventions: `signal-builder` (P12)
- Spawn configs: `spawn-config-builder` (P12)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_orchestration_pipeline]] | sibling | 0.51 |
| [[p12_wf_create_orchestration_agent]] | sibling | 0.41 |
| [[spec_n01_n04_verticalization]] | upstream | 0.36 |
| [[p12_wf_creation_pipeline]] | sibling | 0.35 |
| [[p12_wf_knowledge_pipeline]] | sibling | 0.34 |
| [[bld_examples_workflow]] | upstream | 0.33 |
| [[n07_output_orchestration_audit]] | related | 0.33 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.32 |
| [[bld_collaboration_kind]] | related | 0.31 |
| [[p12_wf_admin_orchestration]] | sibling | 0.30 |
