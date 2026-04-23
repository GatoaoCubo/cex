---
kind: architecture
id: bld_architecture_agent
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agent — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-builder
  - bld_collaboration_agent
  - p01_kc_agent
  - bld_knowledge_card_agent
  - bld_collaboration_system_prompt
  - p03_sp_agent_builder
  - p03_ins_mental_model
  - bld_instruction_agent
  - bld_architecture_boot_config
  - agent-profile-builder
---

# Architecture: agent in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 10-field identity header (id, kind, pillar, domain, agent_group, llm_function, version, tags, etc.) | agent-builder | required |
| persona | Natural-language description of who the agent is and its domain expertise | author | required |
| capabilities | List of concrete things the agent can do (4-8 items) | author | required |
| agent_package/ | Directory of 10+ spec files providing full structured identity | agent-builder | required |
| ISO_*_MANIFEST.md | Capabilities list, version, routing keywords | agent-builder | required |
| ISO_*_INSTRUCTIONS.md | Step-by-step execution protocol | agent-builder | required |
| ISO_*_ARCHITECTURE.md | Boundary, dependencies, and position of the agent's output type | agent-builder | required |
| ISO_*_EXAMPLES.md | 3+ input/output examples demonstrating correct behavior | agent-builder | required |
| ISO_*_SYSTEM_INSTRUCTION.md | System prompt loaded at agent boot | agent-builder | required |
| ISO_*_ERROR_HANDLING.md | Error taxonomy and recovery protocols | agent-builder | required |
| routing_entry | Registration in the agent routing index for discovery | system | required |
## Dependency Graph
```
system_prompt    --produces-->  agent  --produces-->  agent_package
knowledge_card   --produces-->  agent  --consumed_by-> router
mental_model     --depends-->   agent  --consumed_by-> workflow
model_card       --depends-->   agent  --consumed_by-> spawn_config
boot_config      --depends-->   agent  --produces-->   skill
agent            --signals-->   routing_entry (registration)
```
| From | To | Type | Data |
|------|----|------|------|
| system_prompt (P03) | agent | data_flow | persona, tone, operating rules loaded at boot |
| knowledge_card (P01) | agent | data_flow | domain facts injected into context |
| mental_model (P02) | agent | depends | routing logic and decision patterns |
| model_card (P02) | agent | depends | LLM capabilities and cost constraints |
| boot_config (P02) | agent | depends | provider-specific initialization parameters |
| agent | agent_package (P02) | produces | portable distributable bundle of the agent |
| agent | skill (P04) | produces | reusable capability extracted from agent behavior |
| agent | router (P02) | data_flow | routing destination registered for task dispatch |
| agent | workflow (P12) | data_flow | node in orchestration graph |
| agent | spawn_config (P12) | data_flow | spawn target with identity and constraints |
## Boundary Table
| agent IS | agent IS NOT |
|----------|--------------|
| A runtime identity — persona + capabilities + structured agent_package | A skill (executable capability without persistent identity) |
| The definition of who executes, what they know, and what tools they have | A system prompt (how the agent speaks, not who it is) |
| Persistent — defined once, instantiated many times | A mental_model (design-time blueprint, not runtime entity) |
| Scoped to a agent_group with specific tool access | A model_card (LLM spec, not agent identity) |
| A destination for routing and orchestration | A boot_config (initialization params, not agent definition) |
| Packaged into agent_package with 10+ required builder specs | An agent_package (the distributable bundle, not the source definition) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Inputs | system_prompt, knowledge_card, mental_model, model_card, boot_config | Supply identity, domain knowledge, routing logic, LLM spec, init params |
| Identity | frontmatter, persona, capabilities, routing_entry | Define who the agent is, what it does, and how it is discovered |
| Structure | agent_package/ (10+ spec files) | Provide fully navigable, versioned agent specification |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | upstream | 0.64 |
| [[bld_collaboration_agent]] | downstream | 0.61 |
| [[p01_kc_agent]] | upstream | 0.54 |
| [[bld_knowledge_card_agent]] | upstream | 0.50 |
| [[bld_collaboration_system_prompt]] | upstream | 0.40 |
| [[p03_sp_agent_builder]] | upstream | 0.40 |
| [[p03_ins_mental_model]] | upstream | 0.38 |
| [[bld_instruction_agent]] | upstream | 0.38 |
| [[bld_architecture_boot_config]] | sibling | 0.38 |
| [[agent-profile-builder]] | upstream | 0.37 |
