---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of skill — inventory, dependencies, and architectural position
---

# Architecture: skill in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, trigger, phases_count, etc.) | skill-builder | active |
| trigger_definition | What activates the skill (slash command, keyword, event, or programmatic call) | author | active |
| phase_list | Ordered execution phases with input/output per phase | author | active |
| input_contract | Typed specification of what the skill receives at invocation | author | active |
| output_contract | Typed specification of what the skill produces on completion | author | active |
| user_invocable_flag | Whether the skill is triggered by user (slash command) or agent-only | author | active |

## Dependency Graph

```
agent           --invokes-->    skill  --produces-->     skill_output
trigger_event   --activates-->  skill  --signals-->      completion_signal
skill           --depends-->    knowledge_card
```

| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | skill | consumes | agent invokes skill for reusable capability |
| trigger_event | skill | data_flow | event or command that activates the skill |
| skill | skill_output | produces | structured result from phase execution |
| skill | completion_signal (P12) | signals | emitted when all phases complete |
| knowledge_card (P01) | skill | dependency | domain knowledge injected into skill phases |
| action_prompt (P03) | skill | dependency | individual phases may use action prompts |

## Boundary Table

| skill IS | skill IS NOT |
|----------|--------------|
| A reusable capability with structured phases and trigger | An agent identity with persona and rules (system_prompt P03) |
| Triggered by slash command, keyword, event, or API call | A one-time task prompt (action_prompt P03) |
| Multi-phase with defined input/output per phase | An event interceptor without phases (hook P04) |
| User-invocable or agent-only based on flag | A protocol server exposing tools (mcp_server P04) |
| Produces structured output on completion | A pluggable extension with lifecycle hooks (plugin P04) |
| Scoped to one capability domain | A multi-satellite orchestration (workflow P12) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Trigger | trigger_definition, user_invocable_flag | Define how and by whom the skill is activated |
| Contract | frontmatter, input_contract, output_contract | Specify typed I/O for the skill |
| Execution | phase_list, action_prompt | Ordered phases with per-phase input/output |
| Context | knowledge_card | Domain knowledge supporting phase execution |
| Output | skill_output, completion_signal | Deliver result and signal completion |
