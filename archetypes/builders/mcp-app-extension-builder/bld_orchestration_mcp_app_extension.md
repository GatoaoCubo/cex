---
kind: collaboration
id: bld_collaboration_mcp_app_extension
pillar: P12
llm_function: COLLABORATE
purpose: How mcp_app_extension-builder works in crews with other builders
quality: 8.9
title: "Collaboration MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, collaboration]
tldr: "How mcp_app_extension-builder works in crews with other builders"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - mcp-app-extension-builder
  - p03_sp_mcp_app_extension_builder
  - bld_tools_mcp_app_extension
  - bld_knowledge_card_mcp_app_extension
  - p10_lr_mcp_app_extension_builder
  - bld_examples_mcp_app_extension
  - bld_instruction_mcp_app_extension
  - bld_collaboration_mcp_server
  - p04_qg_mcp_app_extension
  - bld_collaboration_agent_computer_interface
---

## Crew Role
Authors MCP Apps Extension manifests per SEP-1865, aligning capability + permission scopes with the backing mcp_server and with AAIF (Linux Foundation) review criteria used by Anthropic and OpenAI MCP clients.

## Receives From
| Builder              | What                                    | Format   |
|----------------------|-----------------------------------------|----------|
| mcp_server-builder   | Tool + resource surface of the server   | JSON-RPC |
| security-reviewer    | Sandbox CSP baseline, permission policy | Markdown |
| ui-designer          | Iframe UI entry_url + asset references  | URL list |

## Produces For
| Builder              | What                                    | Format   |
|----------------------|-----------------------------------------|----------|
| mcp_client (Anthropic, OpenAI) | App-manifest for install handshake | JSON  |
| AAIF reviewer        | Permission justification sheet          | Markdown |
| app_directory_entry-builder | Listing summary for distribution  | Markdown |

## Boundary
Does NOT produce plain mcp_server artifacts (handled by `mcp_server-builder`), browser extensions for the Chrome Web Store (out of MCP scope), or webhooks (handled by `webhook-builder`). Does NOT manage runtime tool invocation -- that is the MCP JSON-RPC layer. Focus is strictly on manifest, install, launch, terminate, capabilities, permissions, and sandbox policy per SEP-1865.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mcp-app-extension-builder]] | upstream | 0.48 |
| [[p03_sp_mcp_app_extension_builder]] | upstream | 0.47 |
| [[bld_tools_mcp_app_extension]] | upstream | 0.44 |
| [[bld_knowledge_card_mcp_app_extension]] | upstream | 0.42 |
| [[p10_lr_mcp_app_extension_builder]] | upstream | 0.37 |
| [[bld_examples_mcp_app_extension]] | upstream | 0.37 |
| [[bld_instruction_mcp_app_extension]] | upstream | 0.35 |
| [[bld_collaboration_mcp_server]] | sibling | 0.34 |
| [[p04_qg_mcp_app_extension]] | upstream | 0.33 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.31 |
