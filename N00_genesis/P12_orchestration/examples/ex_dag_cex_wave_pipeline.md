---
id: p12_dag_cex_wave_pipeline
kind: dag
pillar: P12
title: "DAG: CEX Wave Migration Pipeline"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [dag, cex, migration, pipeline, waves]
tldr: "7-wave DAG for migrating 9916 organization-core MD files into CEX — P01 KCs first, then prompts/skills, then agents, then infra/P08-P12"
max_bytes: 1024
density_score: 0.90
source: organization-core/C:/Users/PC/Documents/GitHub/cex/archetypes/MIGRATION_MAP.md (PLANO DE EXECUCAO)
linked_artifacts:
  map: archetypes/MIGRATION_MAP.md
related:
  - p12_wf_knowledge_pipeline
  - p12_crew_agent_group_grid
  - p08_cmap_organization_core
  - p08_sat_edison
  - p12_spawn_grid_continuous
  - p10_lr_continuous_batching
  - p01_kc_lp12_orchestration
  - p12_wf_admin_orchestration
  - spec_cex_system_map
  - p08_pat_continuous_batching
---

# DAG: CEX Wave Migration Pipeline

## Pipeline

```
[W5.1 P01 KCs] ─────────────────────────────────────┐
[W5.2 P03 Prompts] ──────────────────────────────────┤
[W5.3 P04 Skills] ───────────────────────────────────┤── [W5.7 Archive]
[W5.4 P02 Agents] ──── depends on W5.1 (KC context) ─┤
[W5.5 P08-P12 Infra] ─ depends on W5.1+W5.4 ─────────┤
[W5.6 INVESTIGATE] ──── depends on W5.1-W5.5 ─────────┘
```

## Node Definitions

| Node | Agent_group | Volume | Input | Output |
|------|-----------|--------|-------|--------|
| W5.1 | knowledge_agent | 519 KCs quality>=7 | records/pool/knowledge/ | P01 examples |
| W5.2 | knowledge_agent | 638 active prompts | records/pool/prompts/ | P03 examples |
| W5.3 | knowledge_agent | 128 skills | records/skills/*/SKILL.md | P04 examples |
| W5.4 | builder_agent | 125 agent dirs | records/agents/*/iso_vectorstore/ | P02 examples |
| W5.5 | knowledge_agent | ~339 infra files | records/framework/ + .claude/ | P08-P12 examples |
| W5.6 | knowledge_agent | ~4596 unclassified | records/* (INVESTIGATE bucket) | audit + classify |
| W5.7 | ALL | ~561+ low quality | pool + .claude/handoffs/ | archived artifacts |

## Dependencies

```yaml
dependencies:
  W5.4_agents:
    requires: [W5.1_kcs]  # agents reference KCs for domain context
  W5.5_infra:
    requires: [W5.1_kcs, W5.4_agents]  # infra docs reference both
  W5.6_investigate:
    requires: [W5.1, W5.2, W5.3, W5.4, W5.5]  # classify what's left
  W5.7_archive:
    requires: [W5.6_investigate]  # archive only after full classification
```

## Execution Mode

| Wave | Mode | Agent_groups | Estimated Batches |
|------|------|-----------|-------------------|
| W5.1 | grid continuous | knowledge_agent | ~10 batches (519 KCs) |
| W5.2 | grid continuous | knowledge_agent | ~7 batches (638 prompts) |
| W5.3 | solo | knowledge_agent | 1 batch (128 skills) |
| W5.4 | grid continuous | builder_agent | ~5 batches (125 agents) |
| W5.5 | solo | knowledge_agent | 1-2 batches (~339 files) |

## Quality Gate

Each wave requires commit + signal >= 8.0 before next wave starts.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_knowledge_pipeline]] | related | 0.22 |
| [[p12_crew_agent_group_grid]] | related | 0.22 |
| [[p08_cmap_organization_core]] | upstream | 0.22 |
| [[p08_sat_edison]] | upstream | 0.19 |
| [[p12_spawn_grid_continuous]] | related | 0.19 |
| [[p10_lr_continuous_batching]] | upstream | 0.18 |
| [[p01_kc_lp12_orchestration]] | upstream | 0.18 |
| [[p12_wf_admin_orchestration]] | related | 0.18 |
| [[spec_cex_system_map]] | upstream | 0.18 |
| [[p08_pat_continuous_batching]] | upstream | 0.18 |
