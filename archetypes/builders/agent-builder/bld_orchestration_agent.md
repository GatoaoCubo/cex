---
kind: collaboration
id: bld_collaboration_agent
pillar: P12
llm_function: COLLABORATE
purpose: How agent-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_boot_config
  - agent-builder
  - bld_collaboration_agent_package
  - bld_collaboration_system_prompt
  - bld_architecture_agent
  - p01_kc_agent
  - bld_collaboration_knowledge_card
  - bld_collaboration_model_card
  - bld_collaboration_instruction
  - bld_knowledge_card_agent
---

# Collaboration: agent-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "who is this agent, what can it do, what are its constraints, and how is it structured?"
I do not write system prompts. I do not define skills or model cards.
I produce agent definitions so downstream builders can configure, package, and deploy the agent.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for agent expertise"
  2. agent-builder -> "agent definition (persona + capabilities + agent_package)"
  3. instruction-builder -> "execution steps for agent tasks"
  4. boot-config-builder -> "provider-specific initialization config"
  5. agent-package-builder -> "portable deployable package"
```
### Crew: "Agent Identity Stack"
```
  1. agent-builder -> "agent definition with capabilities"
  2. fallback-chain-builder -> "model degradation sequence"
  3. guardrail-builder -> "safety boundaries for agent behavior"
```
## Handoff Protocol
### I Receive
- seeds: agent name, domain, target capabilities, agent_group assignment
- optional: existing persona sketch, tool list, routing keywords
### I Produce
- agent artifact with agent_package skeleton (10+ spec files)
- committed to: `cex/P02/examples/p02_agent_{name}/`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- knowledge-card-builder: provides domain knowledge that shapes agent expertise
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| boot-config-builder | Needs agent identity to configure provider startup |
| agent-package-builder | Packages agent definition into portable bundle |
| dispatch-rule-builder | Creates routing rules that target this agent |
| guardrail-builder | Defines safety boundaries scoped to agent capabilities |
| interface-builder | Defines contracts between this agent and others |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_boot_config]] | sibling | 0.59 |
| [[agent-builder]] | upstream | 0.57 |
| [[bld_collaboration_agent_package]] | sibling | 0.57 |
| [[bld_collaboration_system_prompt]] | sibling | 0.52 |
| [[bld_architecture_agent]] | upstream | 0.46 |
| [[p01_kc_agent]] | upstream | 0.46 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.44 |
| [[bld_collaboration_model_card]] | sibling | 0.43 |
| [[bld_collaboration_instruction]] | sibling | 0.42 |
| [[bld_knowledge_card_agent]] | upstream | 0.41 |
