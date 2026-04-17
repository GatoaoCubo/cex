---
kind: architecture
id: bld_architecture_agent_computer_interface
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agent_computer_interface -- artifact structure, dependencies, 13-ISO layout
quality: 9.1
title: "Architecture Agent Computer Interface"
version: "1.0.0"
author: n01_review
tags: [agent_computer_interface, builder, architecture]
tldr: "Structural map of agent_computer_interface artifacts: action space, observation schema, error protocol, and 8F pipeline integration."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

## Component Inventory (Artifact Fields)
| Name | Role | Required | Notes |
| :--- | :--- | :--- | :--- |
| action_space | Table of agent-invokable commands with input/output schemas | Yes | Core of every ACI |
| observation_schema | Structured fields the agent receives as feedback | Yes | Must be typed |
| error_protocol | Error codes, meanings, and recovery strategies | Yes | Min 3 codes |
| auth_method | Authentication mechanism for the interface | Yes | none/token/mtls/api_key |
| protocol | Communication protocol (json_rpc/cli/rest/grpc/mcp) | Yes | Named + transport |
| transport | Underlying channel (unix_socket/http/stdio/tcp) | Recommended | Enables implementation |
| rate_limit | Max requests per minute | Recommended | Safety for autonomous agents |
| security_constraints | Scope, sandbox, allowlist | Recommended | Execution boundaries |

## 13-ISO Builder Layout
| ISO | Kind | Purpose |
| :--- | :--- | :--- |
| bld_manifest | type_builder | Builder identity, capabilities, routing keywords |
| bld_system_prompt | system_prompt | Builder persona (llm_function: BECOME) |
| bld_instruction | instruction | 3-phase production process (research/compose/validate) |
| bld_schema | schema | SINGLE SOURCE OF TRUTH for frontmatter + body fields |
| bld_output_template | output_template | Fill-in template with guidance prose |
| bld_quality_gate | quality_gate | 10 HARD gates + 8 SOFT dimensions |
| bld_examples | examples | Golden and anti-examples for reference |
| bld_knowledge_card | knowledge_card | Domain knowledge (ACI spec, MCP, AutoGen patterns) |
| bld_tools | tools | Real CEX tools (retriever, doctor, compiler, hooks) |
| bld_config | config | Naming rules, size limits, allowed enums |
| bld_architecture | architecture | This file -- component map and dependency graph |
| bld_collaboration | collaboration | Crew integration with real CEX builders |
| bld_memory | memory | Learned patterns and pitfalls (llm_function: INJECT) |

## Dependency Graph
```
agent (P02)         --defines_capability_for--> agent_computer_interface
mcp_server (P04)    --exposes_tools_via------> agent_computer_interface
sandbox_config (P09)--constrains-------------> agent_computer_interface
agent_computer_interface --extends-----------> computer_use (P08)
agent_computer_interface --boundaries_with---> browser_tool (P04)
agent_computer_interface --consumed_by------> agent (P02)
```

## 8F Pipeline Integration
| Stage | agent_computer_interface Role |
|-------|------------------------------|
| F1 CONSTRAIN | kind=agent_computer_interface, pillar=P08, schema loaded |
| F2 BECOME | agent-computer-interface-builder loaded (13 ISOs) |
| F3 INJECT | kc_agent_computer_interface + MCP spec + AutoGen patterns |
| F4 REASON | plan: overview + action_space + observation + error + security |
| F5 CALL | retriever finds existing ACI specs, doctor verifies builder |
| F6 PRODUCE | generate complete artifact -- all 5 required sections |
| F7 GOVERN | validate 10 HARD gates, density >= 0.85 |
| F8 COLLABORATE | save to P08, compile, commit, signal |

## Boundary Table
| agent_computer_interface IS | agent_computer_interface IS NOT |
|-----------------------------|---------------------------------|
| Formal action/observation schema for agent-system interaction | Web DOM automation (browser_tool) |
| Protocol-level interface definition (JSON-RPC, CLI, MCP) | Pixel-level screen control (computer_use) |
| Typed command set with error handling | Agent identity or persona definition (agent) |
| Security-scoped for autonomous execution | Arbitrary shell script or runbook |
