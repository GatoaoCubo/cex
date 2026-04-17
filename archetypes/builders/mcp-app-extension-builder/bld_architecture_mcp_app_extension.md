---
kind: architecture
id: bld_architecture_mcp_app_extension
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of mcp_app_extension -- inventory, dependencies
quality: 9.0
title: "Architecture MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, architecture]
tldr: "Component map of mcp_app_extension -- inventory, dependencies"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name              | Role                                  | Pillar | Status  |
|-----------------------|---------------------------------------|--------|---------|
| bld_manifest          | Builder identity + routing            | P05    | Active  |
| bld_instruction       | Production phases                     | P03    | Active  |
| bld_system_prompt     | Persona + SEP-1865 rules              | P03    | Active  |
| bld_schema            | Manifest field contract               | P06    | Active  |
| bld_quality_gate      | HARD and SOFT validation              | P11    | Active  |
| bld_output_template   | App-manifest skeleton                 | P05    | Active  |
| bld_examples          | Golden + anti-examples                | P07    | Active  |
| bld_knowledge_card    | SEP-1865, MCP spec, AAIF context      | P01    | Active  |
| bld_architecture      | This component map                    | P08    | Active  |
| bld_collaboration     | Crew role + handoffs                  | P12    | Active  |
| bld_config            | Naming, paths, limits                 | P09    | Active  |
| bld_memory            | Learning record on sandbox pitfalls   | P10    | Active  |
| bld_tools             | install, launch, terminate tooling    | P04    | Active  |

## Dependencies
| From              | To                  | Type          |
|-------------------|---------------------|---------------|
| bld_manifest      | bld_config          | configuration |
| bld_instruction   | bld_system_prompt   | dependency    |
| bld_output_template | bld_schema        | dependency    |
| bld_quality_gate  | bld_examples        | validation    |
| bld_collaboration | bld_memory          | coordination  |
| bld_tools         | MCP client (iframe) | integration   |
| bld_tools         | MCP server (JSON-RPC)| integration  |

## Architectural Position
mcp_app_extension sits at the boundary between MCP (model-context plumbing) and rendered UI. It extends the MCP spec 2025-11-25 with a manifest + install/launch/terminate lifecycle so clients (Anthropic Claude, OpenAI ChatGPT) can safely host third-party iframe UIs governed by the AAIF (Linux Foundation). It depends on mcp_server (for the tool + resource surface) but is distinct from it: mcp_server handles protocol; mcp_app_extension handles packaged UI.
