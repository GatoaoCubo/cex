---
kind: tools
id: bld_tools_mcp_app_extension
pillar: P04
llm_function: CALL
purpose: Tools available for mcp_app_extension production
quality: 8.9
title: "Tools MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, tools]
tldr: "Tools available for mcp_app_extension production"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_mcp_app_extension_builder
  - bld_collaboration_mcp_app_extension
  - bld_knowledge_card_mcp_app_extension
  - mcp-app-extension-builder
  - p10_lr_mcp_app_extension_builder
  - p04_qg_mcp_app_extension
  - bld_instruction_mcp_app_extension
  - bld_tools_agents_md
  - bld_tools_marketplace_app_manifest
  - bld_examples_mcp_app_extension
---

## Production Tools
| Tool              | Purpose                                       | When                         |
|-------------------|-----------------------------------------------|------------------------------|
| cex_compile.py    | Compile manifest markdown to YAML + JSON      | Post-authoring               |
| cex_score.py      | Peer-review quality gate scoring              | After manifest draft is done |
| cex_retriever.py  | Find similar SEP-1865 manifests for reuse     | During F3 INJECT             |
| cex_doctor.py     | Lint manifest + referenced mcp_server contract| Pre-validation               |
| mcp_client_probe  | Dry-run install handshake vs Anthropic/OpenAI | Pre-publish smoke test       |
| sep1865_lint      | Validate manifest against SEP-1865 draft JSON schema | Every save                |

## Validation Tools
| Tool              | Purpose                                       | When                         |
|-------------------|-----------------------------------------------|------------------------------|
| val_check.py      | Verify required fields, HTTPS entry_url       | Pre-deployment               |
| val_csp.py        | Parse CSP, assert no parent-frame DOM access  | Sandbox review               |
| val_cap_map.py    | Match capabilities against backing mcp_server | Dependency audit             |
| val_perm_min.py   | Flag unjustified permission scopes            | AAIF review prep             |

## External References
- MCP spec 2025-11-25 (Anthropic, AAIF Linux Foundation)
- SEP-1865 draft 2026 (Anthropic + OpenAI Apps Extension proposal)
- Anthropic MCP documentation portal (install, launch, terminate reference flows)
- OpenAI plugins history (legacy reference for permission-grant patterns)
- AAIF governance charter (certification + bypass criteria)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_mcp_app_extension_builder]] | upstream | 0.46 |
| [[bld_collaboration_mcp_app_extension]] | downstream | 0.44 |
| [[bld_knowledge_card_mcp_app_extension]] | upstream | 0.41 |
| [[mcp-app-extension-builder]] | downstream | 0.41 |
| [[p10_lr_mcp_app_extension_builder]] | downstream | 0.39 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.37 |
| [[bld_instruction_mcp_app_extension]] | upstream | 0.33 |
| [[bld_tools_agents_md]] | sibling | 0.31 |
| [[bld_tools_marketplace_app_manifest]] | sibling | 0.29 |
| [[bld_examples_mcp_app_extension]] | downstream | 0.26 |
