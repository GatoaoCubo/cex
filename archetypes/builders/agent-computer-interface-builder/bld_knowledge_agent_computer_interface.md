---
kind: knowledge_card
id: bld_knowledge_card_agent_computer_interface
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for agent_computer_interface production
quality: 9.1
title: "Knowledge Card Agent Computer Interface"
version: "1.0.0"
author: n01_review
tags: [agent_computer_interface, builder, knowledge_card, aci, mcp, autogen]
tldr: "Core domain knowledge for ACI artifacts: protocol patterns, action/observation schemas, security boundaries, and industry citations."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_tools_agent_computer_interface
  - bld_examples_agent_computer_interface
  - bld_output_template_agent_computer_interface
  - bld_architecture_agent_computer_interface
  - p11_qg_agent_computer_interface
  - p03_sp_agent_computer_interface_builder
  - atom_19_agent_taxonomy_surveys
  - bld_collaboration_agent_computer_interface
  - hybrid_review3_n01
  - bld_schema_agent_computer_interface
---

## What Is an agent_computer_interface?
An ACI (Agent-Computer Interface) is the formal protocol layer between an LLM agent and a
computing environment. Unlike APIs (designed for software-to-software) or GUIs (designed for
humans), an ACI is optimized for LLM consumption: structured schemas, typed actions, and
deterministic observation formats that minimize ambiguity for autonomous agents.

## Industry Reference: Protocol Patterns
| Protocol | Source | Use Case | Transport |
|----------|--------|---------|-----------|
| MCP (Model Context Protocol) | Anthropic | Tool exposure to LLM agents | stdio / HTTP SSE |
| AutoGen tool_use | Microsoft | Multi-agent function calling | Python function calls |
| LangGraph ToolNode | LangChain | State machine tool invocation | Python in-process |
| OpenAI Assistants tool_call | OpenAI | Tool definitions + code interpreter | REST API |
| JSON-RPC 2.0 | IETF | Generic remote procedure call | TCP / Unix socket |

## Action Space Patterns
| Interface Type | Action Examples | Observation Type | Standard |
|---------------|----------------|-----------------|----------|
| terminal | bash_exec, file_read, file_write | stdout, stderr, exit_code | POSIX |
| browser | navigate, click, type, screenshot | page_content, screenshot | W3C WebDriver |
| GUI | mouse_move, click, key_press | screenshot, accessibility_tree | ARIA / AT-SPI |
| API | http_get, http_post, http_put | response_body, status_code | OpenAPI |
| file_system | read, write, list, delete | file_content, directory_listing | POSIX |
| code_execution | run_python, run_js, run_bash | output, errors, artifacts | subprocess |

## ACI Boundary (vs Adjacent Kinds)
| Kind | Difference |
|------|-----------|
| browser_tool | Web-specific DOM automation; ACI is protocol-level, not DOM-level |
| computer_use | Pixel-based screen control; ACI uses structured schemas, not vision |
| mcp_server | MCP is one ACI protocol implementation; ACI is the broader abstraction |
| cli_tool | A CLI is one type of ACI action; ACI defines the full interface, not just the command |

## Security Patterns for Autonomous Agents
| Threat | Mitigation | Enforcement |
|--------|-----------|------------|
| Command injection | Typed schema with allowlisted actions | JSON Schema validation |
| Privilege escalation | Sandbox with minimum required permissions | seccomp / AppArmor |
| Unbounded loops | Rate limiting per session | Token or time budget |
| Credential exposure | No secrets in ACI schema | cex_sanitize.py check |

## Quality Indicators
| Indicator | Good ACI | Poor ACI |
|-----------|---------|---------|
| Action schema | Typed inputs + outputs + error states | Free-form command strings |
| Observation format | Structured JSON fields | Raw text blobs |
| Error handling | Named codes with recovery strategies | Unhandled or implicit errors |
| Security | Scoped, auth-defined, rate-limited | Open execution, no boundaries |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_agent_computer_interface]] | downstream | 0.57 |
| [[bld_examples_agent_computer_interface]] | downstream | 0.43 |
| [[bld_output_template_agent_computer_interface]] | downstream | 0.42 |
| [[bld_architecture_agent_computer_interface]] | downstream | 0.34 |
| [[p11_qg_agent_computer_interface]] | downstream | 0.32 |
| [[p03_sp_agent_computer_interface_builder]] | downstream | 0.31 |
| [[atom_19_agent_taxonomy_surveys]] | sibling | 0.29 |
| [[bld_collaboration_agent_computer_interface]] | downstream | 0.28 |
| [[hybrid_review3_n01]] | sibling | 0.28 |
| [[bld_schema_agent_computer_interface]] | downstream | 0.26 |
