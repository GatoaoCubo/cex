---
kind: examples
id: bld_examples_mcp_app_extension
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of mcp_app_extension artifacts
quality: 8.9
title: "Examples MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, examples]
tldr: "Golden and anti-examples of mcp_app_extension artifacts"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
id: p04_mae_figma_design_inspector.md
kind: mcp_app_extension
pillar: P04
app_id: com.figma.design-inspector
version: 1.0.0
entry_url: https://mcp-apps.figma.com/design-inspector/v1/
spec_version: SEP-1865
---
**App**: Figma Design Inspector (MCP Apps Extension, SEP-1865)
**Capabilities**:
- tool:get_frame_spec
- tool:export_component
- resource:component_library
**Permissions**:
- network:https://api.figma.com -- fetch frame metadata (justified: core feature)
- clipboard:write -- copy design tokens (justified: developer workflow)
**Lifecycle**:
- install: MCP client fetches manifest, validates Figma signature, provisions sandbox
- launch: client spawns iframe at entry_url, delivers session token via postMessage
- terminate: client revokes token, clears iframe
**Sandbox**: sandbox="allow-scripts"; CSP: default-src 'self'; connect-src https://api.figma.com; frame-ancestors https://claude.ai https://chatgpt.com
```

## Anti-Example 1: Plain MCP Server (Not An App Extension)
```markdown
---
id: p04_mcp_weather_server.md
kind: mcp_server
---
**Server**: Weather MCP server exposing tool:get_forecast over JSON-RPC.
No UI; returns JSON only.
```
## Why it fails:
This is an mcp_server artifact, NOT an mcp_app_extension. There is no app-manifest, no entry_url, no iframe UI, and no install/launch/terminate lifecycle. MCP servers expose tools over JSON-RPC; Apps Extensions add a sandboxed UI on top of them per SEP-1865.

## Anti-Example 2: Chrome Browser Extension (Wrong Scope)
```markdown
---
id: p04_mae_price_tracker.md
kind: mcp_app_extension
app_id: com.acme.price-tracker
entry_url: chrome-extension://abc123/popup.html
---
**Install**: User installs from Chrome Web Store.
**Runtime**: Runs in the browser's extension process with manifest_version 3.
```
## Why it fails:
Chrome Web Store extensions run inside the browser, not inside an MCP client sandbox. SEP-1865 targets MCP clients (Anthropic Claude, OpenAI ChatGPT), not browsers. The entry_url must be an HTTPS URL loadable in an iframe; `chrome-extension://` is not MCP-compatible and the install flow must be the SEP-1865 manifest handshake, not the Chrome Web Store.
