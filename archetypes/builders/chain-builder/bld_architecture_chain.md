---
kind: architecture
id: bld_architecture_chain
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of chain — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| step | Single LLM call unit — one prompt in, one output out | chain | required |
| data_flow | Typed binding that passes output of step N to input of step N+1 | chain | required |
| error_handling | Strategy applied when a step fails (fail_fast, skip, retry, fallback) | chain | required |
| context_pass | Mechanism for carrying shared context across all steps | chain | required |
| branching_logic | Conditional routing — directs flow to different step paths | chain | optional |
| system_prompt | Agent persona injected into step prompts | P03 | external |
| output_schema | Typed contract defining step output shape | P05/P06 | external |
| knowledge_card | Domain facts injected into one or more steps | P01 | external |
| workflow | Runtime orchestrator that may embed this chain as a substep | P12 | consumer |
## Dependency Graph
```
knowledge_card  --produces--> step
system_prompt   --produces--> step
output_schema   --produces--> step
step            --produces--> data_flow
data_flow       --produces--> step
step            --depends-->  error_handling
context_pass    --produces--> step
branching_logic --depends-->  data_flow
workflow        --depends-->  chain
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card | step | produces | domain facts for prompt hydration |
| system_prompt | step | produces | persona and operational rules |
| output_schema | step | produces | typed output contract |
| step | data_flow | produces | step output (text or structured) |
| data_flow | step | produces | input for next step |
| step | error_handling | depends | failure signal triggering strategy |
| context_pass | step | produces | shared context available to all steps |
| branching_logic | data_flow | depends | conditional routing decision |
| workflow | chain | depends | embeds chain as a prompt substep |
## Boundary Table
| chain IS | chain IS NOT |
|----------|-------------|
| Sequential prompt pipeline — output A feeds input B | A runtime orchestrator managing agents and tools (that is workflow) |
| Text-to-text transformations only | A task dependency graph without execution semantics (that is dag) |
| One LLM call per step | An intra-prompt reasoning technique (that is chain_of_thought) |
| Defined data flow with typed bindings between steps | A single-task action prompt (that is action_prompt) |
| Error handling strategy at step level | A step-by-step agent execution protocol (that is instruction) |
| Composable — consumed by workflows as a substep | Contains agents, tools, or signals |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| knowledge | knowledge_card, system_prompt | Provide domain context and persona for step prompts |
| composition | step, context_pass, branching_logic | Define the individual LLM calls and conditional routing |
| data | data_flow, output_schema | Type and route data between steps |
| resilience | error_handling | Define behavior when a step fails |
| integration | workflow (consumer) | Runtime orchestration that embeds chains |
