---
kind: collaboration
id: bld_collaboration_agent_card
pillar: P08
llm_function: COLLABORATE
purpose: How agent-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-card-builder
  - bld_collaboration_model_card
  - bld_collaboration_agent
  - bld_knowledge_card_agent_card
  - bld_collaboration_boot_config
  - bld_collaboration_model_provider
  - bld_collaboration_spawn_config
  - bld_collaboration_system_prompt
  - bld_collaboration_workflow
  - bld_memory_agent_card
---

# Collaboration: agent-card-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is this agent_group's role, model, tools, and constraints?"
I define the full architecture of an autonomous agent_group — its domain, LLM model, MCPs, boot sequence, dispatch rules, and scaling. I do NOT define individual agents inside the agent_group (agent-builder), boot configuration per provider (boot-config-builder), or reusable patterns (pattern-builder).
## Crew Compositions
### Crew: "New Agent_group Onboarding"
```
  1. mental-model-builder   -> "defines the agent_group's domain map, personality, and cognitive constraints"
  2. agent-card-builder -> "produces the full agent_card: role, model, MCPs, boot sequence, dispatch rules"
  3. boot-config-builder    -> "generates provider-specific boot configuration from the agent_group spec"
```
### Crew: "Agent_group Architecture Documentation"
```
  1. agent-card-builder -> "produces agent_card with all 24+ frontmatter fields"
  2. system-prompt-builder  -> "authors the agent_group's system prompt using the spec's role and constraints"
  3. diagram-builder        -> "renders the agent_group's architecture and dependency graph visually"
```
### Crew: "Multi-Agent_group Orchestration Design"
```
  1. agent-card-builder -> "specs each agent_group's role, model, and MCPs independently"
  2. dispatch-rule-builder  -> "defines routing rules between agent_groups based on their specs"
  3. dag-builder            -> "assembles the execution graph connecting agent_groups into a workflow"
```
## Handoff Protocol
### I Receive
- seeds: agent_group name, domain description, intended role, available MCPs, model preference
- optional: scaling requirements, existing agent list, known constraints, monitoring needs
### I Produce
- agent_card artifact (YAML frontmatter + Markdown body, 24+ fields, max 300 lines)
- committed to: `cex/P08/examples/agent-card-{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- mental-model-builder: provides the domain map and cognitive constraints that shape the spec
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| boot-config-builder | needs the agent_group spec to generate provider-specific boot configs |
| system-prompt-builder | uses role and constraints from the spec to author the agent_group prompt |
| dispatch-rule-builder | uses agent_group boundaries from the spec to define routing rules |
| dag-builder | uses agent_group capabilities to place them correctly in execution graphs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-card-builder]] | related | 0.57 |
| [[bld_collaboration_model_card]] | sibling | 0.56 |
| [[bld_collaboration_agent]] | sibling | 0.46 |
| [[bld_knowledge_card_agent_card]] | upstream | 0.45 |
| [[bld_collaboration_boot_config]] | sibling | 0.44 |
| [[bld_collaboration_model_provider]] | sibling | 0.43 |
| [[bld_collaboration_spawn_config]] | sibling | 0.42 |
| [[bld_collaboration_system_prompt]] | sibling | 0.42 |
| [[bld_collaboration_workflow]] | sibling | 0.41 |
| [[bld_memory_agent_card]] | downstream | 0.40 |
