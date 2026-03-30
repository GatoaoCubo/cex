---
kind: architecture
id: bld_architecture_instruction
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of instruction — inventory, dependencies, and architectural position
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
| Includes rollback for failure recovery | Multi-agent orchestration across agent_nodes |
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
