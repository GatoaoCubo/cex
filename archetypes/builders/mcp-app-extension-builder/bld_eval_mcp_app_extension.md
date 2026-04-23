---
kind: quality_gate
id: p04_qg_mcp_app_extension
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for mcp_app_extension
quality: 9.0
title: "Quality Gate MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for mcp_app_extension"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_mcp_app_extension
  - p03_sp_mcp_app_extension_builder
  - bld_instruction_mcp_app_extension
  - bld_knowledge_card_mcp_app_extension
  - bld_output_template_mcp_app_extension
  - mcp-app-extension-builder
  - bld_collaboration_mcp_app_extension
  - bld_schema_mcp_app_extension
  - bld_tools_mcp_app_extension
  - p10_lr_mcp_app_extension_builder
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| SEP-1865 manifest conformance | 100% | equals | All mcp_app_extension artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p04_mae_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'mcp_app_extension' | Kind field incorrect or set to mcp_server |
| H04 | app_id present and follows reverse-DNS or p04_mae slug | Missing or malformed app_id |
| H05 | entry_url is HTTPS and present | Non-HTTPS URL or missing |
| H06 | capabilities array present and each maps to MCP tool/resource | Missing or unmapped capabilities |
| H07 | permissions array present with per-scope justification | Missing scopes or unjustified grants |
| H08 | Install, launch, terminate handlers documented | Any lifecycle phase missing |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | SEP-1865 manifest completeness (app_id, version, entry_url, capabilities, permissions) | 0.25 | All present = 1.0, partial = 0.5, <50% = 0 |
| D02 | Capability-to-tool mapping accuracy (matches backing mcp_server) | 0.20 | All capabilities map to real tools/resources = 1.0, partial = 0.5, none = 0 |
| D03 | Permission-grant minimality (Anthropic + OpenAI review criteria) | 0.20 | All scopes justified = 1.0, partial = 0.5, unjustified = 0 |
| D04 | Sandbox policy rigor (CSP, iframe flags, no parent-frame DOM) | 0.20 | Full CSP + isolation = 1.0, partial = 0.5, missing = 0 |
| D05 | Lifecycle handler clarity (install, launch, terminate postMessage schemas) | 0.15 | All three documented with payloads = 1.0, partial = 0.5, none = 0 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-publish to MCP app directory |
| PUBLISH | >=8.0 | Auto-publish after AAIF checklist |
| REVIEW | >=7.0 | Require manual security review |
| REJECT | <7.0 | Reject and flag for correction |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Emergency patch for active Anthropic/OpenAI client | MCP Apps Extension maintainer | AAIF escalation log |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
