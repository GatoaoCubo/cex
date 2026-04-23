---
kind: tools
id: bld_tools_role_assignment
pillar: P04
llm_function: CALL
purpose: Tools available for role_assignment production
quality: 9.0
title: "Tools Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, tools, composable, crewai]
tldr: "Tools available for role_assignment production"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
related:
  - bld_tools_crew_template
  - bld_knowledge_card_role_assignment
  - role-assignment-builder
  - p03_sp_role_assignment_builder
  - bld_examples_role_assignment
  - p11_qg_role_assignment
  - bld_instruction_role_assignment
  - bld_tools_capability_registry
  - bld_tools_roi_calculator
  - p01_kc_agent
---

## Production Tools
| Tool                    | Purpose                                         | When          |
|-------------------------|-------------------------------------------------|---------------|
| cex_compile.py          | Compile role_assignment .md to .yaml binding   | F8 COLLABORATE|
| cex_query.py            | Discover existing agents in .claude/agents/    | F1 CONSTRAIN  |
| cex_retriever.py        | Find similar role_assignments (reuse check)    | F3 INJECT     |
| cex_doctor.py           | Validate agent_id resolves                      | F7 GOVERN     |
| cex_score.py            | Peer-review scoring (HARD + SOFT)              | F7 GOVERN     |
| signal_writer.py        | Signal N07 on completion                       | F8 COLLABORATE|

## Validation Tools
| Tool                      | Purpose                                      | When      |
|---------------------------|----------------------------------------------|-----------|
| cex_validate_agent_id.py  | Resolve .claude/P02_model/*.md or N0x/agents/  | Pre-commit|
| cex_tools_subset.py       | Verify tools_allowed is subset of agent native| F7 GOVERN|
| cex_delegation_lint.py    | Check can_delegate_to uses role_names only   | F7 GOVERN |
| cex_backstory_lint.py     | Flag generic backstories (no domain nouns)   | F7 GOVERN |
| cex_goal_measurability.py | Require threshold/count/gate in goal         | F7 GOVERN |

## External References
- CrewAI Agent class API docs (role + goal + backstory + tools + allow_delegation).
- Microsoft AutoGen ConversableAgent reference (name, system_message, tools).
- OpenAI Agents SDK v0.6+ Agent + transfer functions.
- Google A2A AgentCard specification (agent_id as signed URI).
- `.claude/agents/` registry: 257 sub-agent manifests available as agent_id targets.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_crew_template]] | sibling | 0.51 |
| [[bld_knowledge_card_role_assignment]] | upstream | 0.38 |
| [[role-assignment-builder]] | upstream | 0.32 |
| [[p03_sp_role_assignment_builder]] | upstream | 0.31 |
| [[bld_examples_role_assignment]] | downstream | 0.30 |
| [[p11_qg_role_assignment]] | downstream | 0.29 |
| [[bld_instruction_role_assignment]] | upstream | 0.29 |
| [[bld_tools_capability_registry]] | sibling | 0.28 |
| [[bld_tools_roi_calculator]] | sibling | 0.28 |
| [[p01_kc_agent]] | upstream | 0.27 |
