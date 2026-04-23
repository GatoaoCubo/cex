---
kind: architecture
id: bld_architecture_action_prompt
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of action_prompt — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_action_prompt
  - bld_architecture_system_prompt
  - bld_architecture_chain
  - action-prompt-builder
  - bld_knowledge_card_action_prompt
  - p11_qg_action_prompt
  - bld_architecture_instruction
  - bld_collaboration_action_prompt
  - p03_sp_action_prompt_builder
  - bld_architecture_agent
---

# Architecture: action_prompt in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 21-field metadata header (id, kind, pillar, domain, task, input_schema, output_schema, etc.) | action-prompt-builder | required |
| task_description | One-sentence statement of what the agent must accomplish | author | required |
| input_contract | Typed specification of what the prompt receives (fields, types, constraints) | author | required |
| output_contract | Typed specification of what the prompt must return (format, fields, validation) | author | required |
| edge_cases | Explicit handling rules for boundary conditions and malformed inputs | author | required |
| validation_criteria | Conditions that define a correct and complete output | author | required |
| execution_context | Runtime constraints (model, temperature, max_tokens, timeout) | boot_config | optional |
## Dependency Graph
```
knowledge_card   --produces-->  action_prompt  --consumed_by-->  agent
output_schema    --produces-->  action_prompt  --referenced_by-> chain
system_prompt    --depends-->   action_prompt
action_prompt    --signals-->   next_action_prompt (via chain)
action_prompt    --produces-->  validated_output
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | action_prompt | data_flow | domain context injected into task description |
| output_schema (P05/P06) | action_prompt | data_flow | output format specification |
| system_prompt (P03) | action_prompt | depends | identity constraints scope which tasks are valid |
| action_prompt | agent (P02) | data_flow | task instruction with typed I/O contract |
| action_prompt | chain (P03) | data_flow | atomic step composed into multi-step sequence |
| action_prompt | validated_output | produces | structured result matching output_contract |
| validated_output | signal (P12) | signals | completion event after successful execution |
## Boundary Table
| action_prompt IS | action_prompt IS NOT |
|------------------|----------------------|
| A task-focused prompt with explicit typed input and output | A persona or identity definition (system_prompt) |
| Atomic — one task, one invocation, one output | A sequence of steps (chain, instruction) |
| Injected at runtime for a specific execution context | A reusable template with `{{vars}}` for generic use (prompt_template) |
| Validated against a typed output contract | A raw user message without I/O specification |
| Consumed once per task instance | A persistent configuration loaded at agent boot |
| The bridge between orchestration dispatch and agent execution | An orchestration artifact (handoff, workflow, dispatch_rule) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Context | knowledge_card, output_schema, system_prompt | Supply domain facts, output format, and identity constraints |
| Definition | frontmatter, task_description, input_contract, output_contract | Specify what the task is and what valid I/O looks like |
| Constraints | edge_cases, validation_criteria, execution_context | Define handling rules, success conditions, and runtime limits |
| Execution | agent (P02) consuming the prompt | LLM performs the task using the injected action_prompt |
| Output | validated_output, signal | Structured result passed downstream or used to trigger next step |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_action_prompt]] | upstream | 0.46 |
| [[bld_architecture_system_prompt]] | sibling | 0.41 |
| [[bld_architecture_chain]] | sibling | 0.41 |
| [[action-prompt-builder]] | upstream | 0.41 |
| [[bld_knowledge_card_action_prompt]] | upstream | 0.40 |
| [[p11_qg_action_prompt]] | downstream | 0.37 |
| [[bld_architecture_instruction]] | sibling | 0.36 |
| [[bld_collaboration_action_prompt]] | downstream | 0.34 |
| [[p03_sp_action_prompt_builder]] | upstream | 0.32 |
| [[bld_architecture_agent]] | sibling | 0.31 |
