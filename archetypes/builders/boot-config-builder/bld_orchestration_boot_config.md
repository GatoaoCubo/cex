---
kind: collaboration
id: bld_collaboration_boot_config
pillar: P12
llm_function: COLLABORATE
purpose: How boot-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Boot Config"
version: "1.0.0"
author: n03_builder
tags: [boot_config, builder, examples]
tldr: "Golden and anti-examples for boot config construction, demonstrating ideal structure and common pitfalls."
domain: "boot config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_agent
  - bld_collaboration_agent_package
  - bld_collaboration_model_provider
  - boot-config-builder
  - bld_collaboration_fallback_chain
  - bld_collaboration_env_config
  - bld_collaboration_model_card
  - bld_collaboration_instruction
  - bld_collaboration_knowledge_card
  - bld_collaboration_system_prompt
---

# Collaboration: boot-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how does this agent initialize on a specific provider runtime?"
I do not define agents. I do not set environment variables.
I configure provider-specific startup so agents boot correctly on any runtime.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. agent-builder -> "agent definition (persona + capabilities)"
  3. instruction-builder -> "execution steps"
  4. boot-config-builder -> "provider-specific initialization config"
  5. agent-package-builder -> "portable deployable package"
```
### Crew: "Multi-Provider Deployment"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "config per provider (claude, cursor, codex)"
  3. env-config-builder -> "environment variables per deployment"
  4. fallback-chain-builder -> "model degradation per provider"
```
## Handoff Protocol
### I Receive
- seeds: agent name, target provider (claude, cursor, codex), model preference
- optional: MCP list, CLI flags, token budget, timeout values
### I Produce
- boot_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P02/examples/p02_boot_{agent}_{provider}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides agent identity (name, role, capabilities) for config
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-package-builder | Includes boot_config in portable agent package |
| fallback-chain-builder | Needs provider constraints to set degradation timeouts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | sibling | 0.70 |
| [[bld_collaboration_agent_package]] | sibling | 0.57 |
| [[bld_collaboration_model_provider]] | sibling | 0.54 |
| [[boot-config-builder]] | upstream | 0.49 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.46 |
| [[bld_collaboration_env_config]] | sibling | 0.46 |
| [[bld_collaboration_model_card]] | sibling | 0.45 |
| [[bld_collaboration_instruction]] | sibling | 0.42 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.42 |
| [[bld_collaboration_system_prompt]] | sibling | 0.41 |
