---
kind: knowledge_card
id: bld_knowledge_card_mcp_app_extension
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for mcp_app_extension production
quality: 9.2
title: "Knowledge Card MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, knowledge_card]
tldr: "Domain knowledge for mcp_app_extension production"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - mcp-app-extension-builder
  - p03_sp_mcp_app_extension_builder
  - bld_collaboration_mcp_app_extension
  - bld_instruction_mcp_app_extension
  - bld_examples_mcp_app_extension
  - bld_tools_mcp_app_extension
  - p10_lr_mcp_app_extension_builder
  - p04_qg_mcp_app_extension
  - bld_output_template_mcp_app_extension
  - bld_schema_mcp_app_extension
---

## Domain Overview
mcp_app_extension artifacts declare interactive UI apps that plug into MCP clients (Anthropic Claude, OpenAI ChatGPT) under SEP-1865, the Apps Extension proposal co-developed by Anthropic and OpenAI and governed by the Agentic AI Foundation (AAIF, Linux Foundation). They build on top of the Model Context Protocol spec 2025-11-25: where a plain mcp_server exposes tools and resources over JSON-RPC, an mcp_app_extension adds a packaged HTML UI rendered inside a sandboxed iframe by the client.

An extension is a bundle of: an app-manifest (metadata + capabilities + permissions), an install handshake (manifest fetch, signature validation, sandbox provisioning), a launch flow (iframe spawn with session token via postMessage), and a terminate flow (token revocation, sandbox teardown). The app can only call MCP tools/resources listed in its capabilities, and can only use host APIs inside its permission grants.

## Key Concepts
| Concept             | Definition                                                                     | Source                             |
|---------------------|--------------------------------------------------------------------------------|------------------------------------|
| MCP                 | Model Context Protocol, JSON-RPC contract for tool + resource exchange         | MCP spec 2025-11-25                |
| SEP-1865            | Specification Enhancement Proposal for MCP Apps Extension                      | AAIF (Linux Foundation) draft 2026 |
| App Manifest        | Document declaring app_id, version, entry_url, capabilities, permissions       | SEP-1865 section 3                 |
| Install             | Handshake: client fetches manifest, validates signature, provisions sandbox    | SEP-1865 section 4                 |
| Launch              | Client spawns sandboxed iframe, delivers session token via postMessage         | SEP-1865 section 5                 |
| Terminate           | Graceful teardown: token revoked, sandbox state cleared                        | SEP-1865 section 6                 |
| Capability          | Declared binding to a specific MCP tool or resource                            | MCP spec 2025-11-25 + SEP-1865     |
| Permission Grant    | User-approved scope (file, network, clipboard, camera)                         | SEP-1865 section 7                 |
| Sandbox             | Iframe isolation + CSP + postMessage-only channel; no parent-frame DOM access  | HTML Living Standard + SEP-1865    |
| AAIF                | Agentic AI Foundation, Linux Foundation project governing MCP evolution        | Linux Foundation charter 2026      |

## Industry Standards
- MCP spec 2025-11-25 (base protocol, Anthropic-originated, AAIF-governed)
- SEP-1865 draft 2026 (Apps Extension, Anthropic + OpenAI co-authored)
- HTML Living Standard (iframe sandbox attribute semantics)
- Content Security Policy Level 3 (CSP for iframe isolation)
- postMessage API (cross-origin channel, MDN and WHATWG references)
- OAuth 2.0 session tokens (where reused for launch handshake)

## Common Patterns
1. Treat entry_url as immutable per app_id + version tuple; bump version to change UI.
2. Enumerate capabilities against the backing mcp_server's advertised tools/resources; no wildcards.
3. Justify every permission inline; Anthropic and OpenAI reviewers reject unjustified scopes.
4. Use CSP `frame-ancestors` to pin the allowed MCP client origins.
5. Define postMessage payload schemas for install, launch, terminate so clients can validate them.
6. Keep the UI stateless where possible; persist via MCP resources, not sandbox storage.

## Pitfalls
- Confusing mcp_app_extension with plain mcp_server (the latter has no UI; the former requires iframe).
- Confusing it with a browser extension (Chrome Web Store); browser extensions run in the browser, not in an MCP client sandbox.
- Requesting broad permissions (e.g., `network:*`) that fail AAIF review.
- Using `allow-same-origin` without a documented justification.
- Omitting the terminate handler, leaking sandbox state and session tokens.
- Treating the parent-frame DOM as reachable; the sandbox forbids it and the client will block postMessage attempts that imply such access.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mcp-app-extension-builder]] | downstream | 0.72 |
| [[p03_sp_mcp_app_extension_builder]] | downstream | 0.67 |
| [[bld_collaboration_mcp_app_extension]] | downstream | 0.57 |
| [[bld_instruction_mcp_app_extension]] | downstream | 0.55 |
| [[bld_examples_mcp_app_extension]] | downstream | 0.55 |
| [[bld_tools_mcp_app_extension]] | downstream | 0.55 |
| [[p10_lr_mcp_app_extension_builder]] | downstream | 0.50 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.46 |
| [[bld_output_template_mcp_app_extension]] | downstream | 0.44 |
| [[bld_schema_mcp_app_extension]] | downstream | 0.43 |
