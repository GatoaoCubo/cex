---
kind: collaboration
id: bld_collaboration_toolkit
pillar: P02
llm_function: COLLABORATE
purpose: How toolkit-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - toolkit-builder
  - bld_collaboration_agent
  - p03_sp_toolkit_builder
  - p03_ins_toolkit_builder
  - bld_tools_toolkit
  - bld_architecture_toolkit
  - bld_collaboration_role_assignment
  - bld_config_toolkit
  - bld_knowledge_card_toolkit
  - bld_collaboration_system_prompt
---

# Collaboration: toolkit-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what tools does this agent have, what requires confirmation, and what is denied?"
I produce YAML permission bundles for agent tool access: tool definitions with confirmation tiers, deny lists, and MCP endpoint mapping. I do NOT implement tools (N05 operations), define agent identity (system-prompt-builder), model workflows (workflow-primitive-builder), or set routing policy (dispatch-rule-builder).
## Crew Compositions
### Crew: "Agent Provisioning"
```
  1. system-prompt-builder  -> "defines WHO the agent is — identity, rules, boundaries"
  2. toolkit-builder        -> "defines WHAT TOOLS the agent can use — permissions, tiers, denials"
  3. instruction-builder    -> "defines WHAT the agent does — phases, inputs, outputs"
  4. config-builder         -> "defines HOW the agent operates — naming, paths, limits"
```
### Crew: "Tool Security Audit"
```
  1. toolkit-builder        -> "defines the permission bundle with confirmation tiers"
  2. quality-gate-builder   -> "validates least-privilege compliance and risk coverage"
  3. memory-builder         -> "records tool usage patterns for quarterly review"
```
### Crew: "MCP Integration Pipeline"
```
  1. toolkit-builder        -> "maps tools to MCP server endpoints with availability checks"
  2. config-builder         -> "sets MCP server connection parameters and timeouts"
  3. signal-builder         -> "emits tool execution status signals for monitoring"
```
## Handoff Protocol
### I Receive
- seeds: target agent/nucleus name, required operations list, risk profile per operation
- optional: MCP server availability data, existing toolkit overlaps, usage history
### I Produce
- toolkit artifact (YAML, fields: name, tools, category, requires_confirmation, denied_for, max 4096 bytes)
- committed to: `cex/P04_tools/compiled/p04_tk_{name}.yaml`
### I Signal
- signal: complete (with tool count and confirmation tier distribution)
- if any write tool lacks confirmation: signal warning with affected tools
## Builders I Depend On
- system-prompt-builder: provides agent identity context for understanding tool needs
- config-builder: provides MCP server connection parameters
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder             | references toolkit to know which tools are available |
| instruction-builder       | references toolkit to constrain tool usage in instructions |
| quality-gate-builder      | validates toolkit against least-privilege and risk standards |
| dispatch-rule-builder     | checks toolkit availability before routing tasks |
| skill-loader              | reads toolkit to inject tool lists into agent prompts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[toolkit-builder]] | downstream | 0.50 |
| [[bld_collaboration_agent]] | sibling | 0.47 |
| [[p03_sp_toolkit_builder]] | downstream | 0.47 |
| [[p03_ins_toolkit_builder]] | downstream | 0.46 |
| [[bld_tools_toolkit]] | downstream | 0.45 |
| [[bld_architecture_toolkit]] | downstream | 0.44 |
| [[bld_collaboration_role_assignment]] | sibling | 0.41 |
| [[bld_config_toolkit]] | downstream | 0.41 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.41 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
