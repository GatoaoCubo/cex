---
kind: architecture
id: bld_architecture_instruction
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of instruction — inventory, dependencies, and architectural position
quality: 9.0
title: "Architecture Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - instruction-builder
  - p01_kc_instruction
  - bld_collaboration_instruction
  - p03_sp_instruction_builder
  - bld_architecture_skill
  - bld_architecture_chain
  - bld_architecture_action_prompt
  - p03_ins_skill_builder
  - p10_lr_instruction_builder
  - p11_qg_instruction
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| prerequisites | Conditions and resources that must exist before execution begins | author | required |
| steps | Ordered atomic actions the executor follows sequentially | author | required |
| validation_criteria | Observable outcomes that confirm each step succeeded | author | required |
| rollback_procedure | Reversal actions if execution fails midway | author | required |
| idempotency_flag | Whether repeated execution produces the same result safely | author | required |
| dependencies | Other instructions or artifacts this instruction relies on | author | optional |
| timeout_guidance | Expected duration and when to escalate | author | optional |
| scope_note | Explicit boundaries on what this instruction modifies | author | optional |
## Dependency Graph
```
action_prompt  --provides_context_to--> instruction
knowledge_card --informs--> instruction
instruction    --consumed_by--> agent
instruction    --referenced_by--> skill
skill          --depends_on--> instruction
```
| From | To | Type | Data |
|------|----|------|------|
| action_prompt | instruction | data_flow | task context, goal, and constraints |
| knowledge_card | instruction | data_flow | domain facts required for step accuracy |
| instruction | agent | data_flow | ordered steps, prerequisites, rollback |
| instruction | skill | data_flow | sub-procedure referenced by skill phases |
| skill | instruction | depends | skill phase delegates to instruction for execution |
## Boundary Table
| instruction IS | instruction IS NOT |
|----------------|-------------------|
| Step-by-step recipe for a single executor | Conversational prompt with response format |
| Specifies exact actions, not goals | Agent identity or persona definition |
| Includes rollback for failure recovery | Multi-agent orchestration across agent_groups |
| One-shot execution without lifecycle phases | Structured workflow with branching logic |
| Single-agent scope | Task delegation package to a remote receiver |
| Verifiable: each step has validation criteria | Event-triggered side-effect handler |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Entry gate | prerequisites, dependencies | Ensure conditions are met before starting |
| Execution | steps, scope_note, timeout_guidance | Provide the ordered recipe to follow |
| Verification | validation_criteria | Confirm each step completed correctly |
| Recovery | rollback_procedure, idempotency_flag | Handle failure without data corruption |
| Integration | action_prompt, knowledge_card | Supply context and domain knowledge to steps |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[instruction-builder]] | upstream | 0.48 |
| [[p01_kc_instruction]] | upstream | 0.45 |
| [[bld_collaboration_instruction]] | downstream | 0.43 |
| [[p03_sp_instruction_builder]] | upstream | 0.42 |
| [[bld_architecture_skill]] | sibling | 0.32 |
| [[bld_architecture_chain]] | sibling | 0.31 |
| [[bld_architecture_action_prompt]] | sibling | 0.31 |
| [[p03_ins_skill_builder]] | upstream | 0.30 |
| [[p10_lr_instruction_builder]] | downstream | 0.29 |
| [[p11_qg_instruction]] | downstream | 0.29 |
