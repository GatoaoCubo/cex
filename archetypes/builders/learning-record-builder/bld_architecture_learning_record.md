---
kind: architecture
id: bld_architecture_learning_record
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of learning_record — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_learning_record_builder
  - bld_architecture_session_state
  - learning-record-builder
  - bld_collaboration_learning_record
  - p01_kc_learning_record
  - p03_ins_learning_record
  - bld_architecture_pattern
  - bld_architecture_runtime_state
  - p03_sp_session_state_builder
  - ex_learning_record_ad_success
---

# Architecture: learning_record in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22-field metadata header (id, kind, pillar, domain, agent_group, score, etc.) | learning-record-builder | active |
| experience_summary | Dense description of the event or task that produced the learning | author | active |
| patterns | Success patterns extracted with reproducibility assessment | author | active |
| anti_patterns | Failure patterns with root cause and avoidance guidance | author | active |
| impact_score | Numeric score (0.0-10.0) measuring significance of the learning | author | active |
| reproducibility | How reliably this pattern recurs across contexts and agent_groups | author | active |
| context_block | Agent_group, domain, task, and environmental conditions of the experience | author | active |
## Dependency Graph
```
session_state  --produces-->  learning_record  --consumed_by-->  knowledge_system
agent          --produces-->  learning_record  --indexed_by-->   knowledge_index
learning_record  --signals-->  memory_update
```
| From | To | Type | Data |
|------|----|------|------|
| session_state (P10) | learning_record | data_flow | ephemeral session data distilled into persistent record |
| agent (P02) | learning_record | produces | agent experience captured as structured learning |
| learning_record | knowledge_card (P01) | data_flow | high-scoring patterns promoted to atomic facts |
| learning_record | knowledge_index (P01) | consumes | indexed for retrieval by future agents |
| learning_record | memory_update (P12) | signals | triggers memory consolidation pipeline |
| scoring_rubric (P07) | learning_record | dependency | rubric defines how impact_score is calculated |
## Boundary Table
| learning_record IS | learning_record IS NOT |
|--------------------|------------------------|
| A persistent record of experience with patterns and anti-patterns | A distilled atomic fact (knowledge_card P01) |
| Scored by impact and reproducibility | An ephemeral snapshot of current session (session_state P10) |
| Accumulated across sessions with agent_group context | A design-time cognitive map (mental_model P02) |
| Indexed for retrieval by future agents | An abstract truth without experiential basis (axiom P10) |
| Produced from real task execution outcomes | A theoretical pattern without observed evidence |
| Dense (>=0.80 density), max 3KB | A verbose narrative or unstructured log |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | session_state, agent execution | Supply raw experience data from task execution |
| Capture | frontmatter, experience_summary, context_block | Record what happened, where, and under what conditions |
| Analysis | patterns, anti_patterns, impact_score, reproducibility | Extract structured learning with quality metrics |
| Integration | knowledge_index, knowledge_card | Index for retrieval and promote high-value patterns |
| Notification | memory_update signal | Trigger downstream consolidation and routing |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_learning_record_builder]] | upstream | 0.41 |
| [[bld_architecture_session_state]] | sibling | 0.40 |
| [[learning-record-builder]] | downstream | 0.39 |
| [[bld_collaboration_learning_record]] | downstream | 0.34 |
| [[p01_kc_learning_record]] | downstream | 0.30 |
| [[p03_ins_learning_record]] | upstream | 0.29 |
| [[bld_architecture_pattern]] | sibling | 0.29 |
| [[bld_architecture_runtime_state]] | sibling | 0.29 |
| [[p03_sp_session_state_builder]] | upstream | 0.27 |
| [[ex_learning_record_ad_success]] | downstream | 0.27 |
