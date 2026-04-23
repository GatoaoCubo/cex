---
quality: 8.0
quality: 7.8
id: bld_rules_lineage_record
kind: knowledge_card
pillar: P08
title: "Rules: lineage_record Builder Constraints"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
tags: [rules, lineage_record, P01]
llm_function: COLLABORATE
tldr: "Hard constraints and edge cases for lineage_record builder."
density_score: null
related:
  - bld_collaboration_agent
  - p01_kc_agent
  - agent-builder
  - p03_ins_mental_model
  - bld_architecture_agent
  - bld_tools_capability_registry
  - bld_instruction_agent
  - bld_norms
  - bld_knowledge_card_agent
  - bld_schema_input_schema
---

# Rules: lineage_record Builder

## Hard Constraints
1. At least 1 source entity MUST be listed
2. At least 1 activity MUST be listed
3. At least 1 agent MUST be listed
4. sources_count MUST equal len(entities list)
5. activities_count MUST equal len(activities list)
6. quality MUST be null
7. id pattern: `^p01_lr_[a-z][a-z0-9_]+$`

## Edge Cases
| Situation | Resolution |
|-----------|-----------|
| Provenance unknown | Use entity type: unknown; note "provenance not available" |
| Multiple derivation relations | List all in Derivation Relations section |
| Artifact revised from prior version | Use wasRevisionOf derivation type |
| Tool (not nucleus) as agent | agent type: tool; include tool id |
| Human curator as agent | agent type: human; include name/role |
| Circular derivation detected | Flag as data integrity issue; escalate to N04 |
| User confuses with audit_log | Redirect: create audit_log for compliance events |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | downstream | 0.23 |
| [[p01_kc_agent]] | sibling | 0.21 |
| [[agent-builder]] | upstream | 0.20 |
| [[p03_ins_mental_model]] | upstream | 0.19 |
| [[bld_architecture_agent]] | related | 0.19 |
| [[bld_tools_capability_registry]] | upstream | 0.18 |
| [[bld_instruction_agent]] | upstream | 0.18 |
| [[bld_norms]] | related | 0.17 |
| [[bld_knowledge_card_agent]] | sibling | 0.16 |
| [[bld_schema_input_schema]] | upstream | 0.16 |
