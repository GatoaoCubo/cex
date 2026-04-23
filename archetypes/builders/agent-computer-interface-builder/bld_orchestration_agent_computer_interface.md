---
kind: collaboration
id: bld_collaboration_agent_computer_interface
pillar: P12
llm_function: COLLABORATE
purpose: How agent_computer_interface-builder works in crews with other builders
quality: 8.9
title: "Collaboration Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, collaboration]
tldr: "How agent_computer_interface-builder works in crews with other builders"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_agent
  - bld_architecture_kind
  - bld_collaboration_computer_use
  - bld_collaboration_browser_tool
  - kind-builder
  - bld_collaboration_rbac_policy
  - bld_collaboration_system_prompt
  - bld_collaboration_capability_registry
  - bld_collaboration_retriever
  - bld_collaboration_builder
---

## Crew Role
Architects the structured communication protocol and schema that enables an agent to interact with
a specific computing environment via defined commands and state updates. Part of the P08
architecture layer; consumed at F2 BECOME by downstream builder agents.

## Receives From
| Builder (CEX) | What | Format |
| :--- | :--- | :--- |
| agent-builder (P02) | Agent capability requirements | YAML/Markdown |
| mcp-server-builder (P04) | Available tool definitions | JSON Schema |
| sandbox-config-builder (P09) | Security boundaries, execution constraints | YAML |

## Produces For
| Builder (CEX) | What | Format |
| :--- | :--- | :--- |
| computer-use-builder (P08) | ACI extends with GUI-level control | Markdown/Schema |
| browser-tool-builder (P04) | Boundary handoff for web interactions | Markdown |
| agent-computer-interface-builder | Output artifact: agent_computer_interface | Markdown |

## Boundary
Does NOT perform web automation or DOM scraping (handled by browser-tool-builder).
Does NOT perform visual/pixel-based screen control (handled by computer-use-builder).
Does NOT define agent identity or persona (handled by agent-builder).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | sibling | 0.41 |
| [[bld_architecture_kind]] | upstream | 0.38 |
| [[bld_collaboration_computer_use]] | sibling | 0.37 |
| [[bld_collaboration_browser_tool]] | sibling | 0.34 |
| [[kind-builder]] | upstream | 0.32 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.32 |
| [[bld_collaboration_system_prompt]] | sibling | 0.31 |
| [[bld_collaboration_capability_registry]] | sibling | 0.31 |
| [[bld_collaboration_retriever]] | sibling | 0.31 |
| [[bld_collaboration_builder]] | sibling | 0.31 |
