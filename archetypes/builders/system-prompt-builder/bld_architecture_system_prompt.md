---
kind: architecture
id: bld_architecture_system_prompt
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of system_prompt — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture System Prompt"
version: "1.0.0"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_system_prompt
  - bld_architecture_agent
  - system-prompt-builder
  - agent-builder
  - p03_sp_system-prompt-builder
  - bld_collaboration_agent
  - p01_kc_agent
  - bld_architecture_mental_model
  - bld_memory_system_prompt
  - bld_architecture_action_prompt
---

# Architecture: system_prompt in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, target_agent, etc.) | system-prompt-builder | active |
| persona_definition | Who the agent is — role, expertise, and behavioral identity | author | active |
| always_rules | Mandatory behaviors the agent must follow in every interaction | author | active |
| never_rules | Prohibited behaviors the agent must avoid without exception | author | active |
| knowledge_boundary | What the agent knows and explicitly does not know | author | active |
| tone_calibration | Communication style, formality level, and language preferences | author | active |
| output_format | Default response structure the agent should follow | author | active |
## Dependency Graph
```
knowledge_card  --produces-->  system_prompt  --consumed_by-->  agent
mental_model    --depends-->   system_prompt  --constrains-->   action_prompt
system_prompt   --signals-->   identity_load
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | system_prompt | data_flow | domain expertise informing persona and boundaries |
| system_prompt | agent (P02) | consumes | agent loads system prompt as identity at boot |
| system_prompt | action_prompt (P03) | dependency | task prompts must operate within identity constraints |
| system_prompt | mental_model (P02) | dependency | mental model scope constrained by system prompt |
| system_prompt | identity_load (P12) | signals | emitted when agent loads its identity |
| response_format (P05) | system_prompt | data_flow | output format injected into system prompt |
## Boundary Table
| system_prompt IS | system_prompt IS NOT |
|------------------|----------------------|
| A fixed identity definition with persona and ALWAYS/NEVER rules | A task-specific instruction (action_prompt P03) |
| Loaded once at agent boot — persistent across interactions | A step-by-step recipe (instruction P03) |
| Defines who the agent is and how it behaves | A reusable template with `{{variable}}` slots (prompt_template P03) |
| Constrains tone, knowledge boundary, and output format | A meta-prompt that generates other prompts |
| Scoped to one agent with specific domain expertise | A universal prompt applied to all agents |
| Constitutional — defines what the agent must and must not do | A suggestion or guideline that can be overridden |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Knowledge | knowledge_card, response_format | Supply domain expertise and output structure |
| Identity | frontmatter, persona_definition, knowledge_boundary | Define who the agent is and what it knows |
| Rules | always_rules, never_rules | Mandate and prohibit specific behaviors |
| Style | tone_calibration, output_format | Calibrate communication style and response structure |
| Consumers | agent, action_prompt, mental_model | Systems that load and operate within the identity |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_system_prompt]] | upstream | 0.46 |
| [[bld_architecture_agent]] | sibling | 0.45 |
| [[system-prompt-builder]] | upstream | 0.42 |
| [[agent-builder]] | upstream | 0.39 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.39 |
| [[bld_collaboration_agent]] | downstream | 0.39 |
| [[p01_kc_agent]] | upstream | 0.37 |
| [[bld_architecture_mental_model]] | sibling | 0.37 |
| [[bld_memory_system_prompt]] | downstream | 0.35 |
| [[bld_architecture_action_prompt]] | sibling | 0.34 |
