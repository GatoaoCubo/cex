---
kind: instruction
id: bld_instruction_mcp_app_extension
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for mcp_app_extension
quality: 8.9
title: "Instruction MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, instruction]
tldr: "Step-by-step production process for mcp_app_extension"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_mcp_app_extension_builder
  - mcp-app-extension-builder
  - p04_qg_mcp_app_extension
  - bld_knowledge_card_mcp_app_extension
  - bld_schema_mcp_app_extension
  - bld_output_template_mcp_app_extension
  - bld_examples_mcp_app_extension
  - bld_collaboration_mcp_app_extension
  - bld_tools_mcp_app_extension
  - p10_lr_mcp_app_extension_builder
---

## Phase 1: RESEARCH
1. Read the latest SEP-1865 draft (Anthropic + OpenAI, AAIF Linux Foundation track).
2. Confirm compatibility with the MCP base spec 2025-11-25.
3. List MCP tools and resources the app needs; map each to a capability declaration.
4. Enumerate permission scopes required (file-access, network, clipboard, camera) and justify each.
5. Identify the target MCP clients (Claude Desktop, ChatGPT desktop, third-party) and their sandbox policies.
6. Audit for overlap with plain mcp_server kind -- if there is no iframe UI, this is NOT an app extension.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required manifest fields (app_id, version, entry_url, capabilities, permissions).
2. Populate OUTPUT_TEMPLATE.md using validated manifest data.
3. Set app_id using the pattern `^p04_mae_[a-z][a-z0-9_]+$` with no dots.
4. Set entry_url to an HTTPS URL that the MCP client will load inside a sandboxed iframe.
5. List capabilities as an array of MCP tool or resource names the app may invoke.
6. List permissions as explicit scope strings; NEVER request permissions the app does not use.
7. Document install, launch, and terminate handlers with postMessage payload shapes.
8. Declare a Content Security Policy (CSP) that forbids parent-frame DOM access.
9. Proofread against SEP-1865 examples (Anthropic MCP docs) for conformance.

## Phase 3: VALIDATE
- [ ] All required manifest fields present (app_id, version, entry_url, capabilities, permissions).
- [ ] app_id matches the p04_mae_ pattern; no dots, lowercase only.
- [ ] entry_url is HTTPS and reachable.
- [ ] Each capability maps to a real MCP tool or resource in the server contract.
- [ ] Every permission has a written justification; no unused scopes.
- [ ] Install, launch, terminate flows documented with postMessage schemas.
- [ ] Sandbox CSP excludes parent-frame DOM, eval, and inline scripts.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_mcp_app_extension_builder]] | related | 0.54 |
| [[mcp-app-extension-builder]] | downstream | 0.48 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.47 |
| [[bld_knowledge_card_mcp_app_extension]] | upstream | 0.47 |
| [[bld_schema_mcp_app_extension]] | downstream | 0.40 |
| [[bld_output_template_mcp_app_extension]] | downstream | 0.40 |
| [[bld_examples_mcp_app_extension]] | downstream | 0.39 |
| [[bld_collaboration_mcp_app_extension]] | downstream | 0.39 |
| [[bld_tools_mcp_app_extension]] | downstream | 0.36 |
| [[p10_lr_mcp_app_extension_builder]] | downstream | 0.35 |
