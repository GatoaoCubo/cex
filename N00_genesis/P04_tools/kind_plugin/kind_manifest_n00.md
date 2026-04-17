---
id: n00_plugin_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Plugin -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, plugin, p04, n00, archetype, template]
density_score: 0.99
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A plugin is a pluggable extension that adds capabilities to a host system (LLM client, IDE, platform) through a defined extension API without modifying the host core. In CEX, plugins extend nucleus capabilities: adding new tool types, output formatters, or retrieval backends that can be dropped in without rebuilding the nucleus. The output is a self-contained extension module with an install manifest, API contract, and lifecycle hooks.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `plugin` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| host_system | string | yes | Target host: claude_code, vscode, nucleus, platform |
| extension_point | string | yes | Which API the plugin hooks into |
| install_manifest | map | yes | Files, permissions, and dependencies required |
| api_version | string | yes | Host extension API version this plugin targets |

## When to use
- When adding a new capability to Claude Code or another LLM client without core modification
- When packaging a reusable CEX extension (e.g., custom retriever backend) for distribution
- When the mcp_app_extension pattern is too heavy and a simpler plug-in surface suffices

## Builder
`archetypes/builders/plugin-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind plugin --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: plugin_cex_retriever_vscode
kind: plugin
pillar: P04
nucleus: n04
title: "CEX Retriever VSCode Plugin"
version: 1.0
quality: null
---
host_system: vscode
extension_point: chat_participant
api_version: "1.87"
install_manifest:
  entry_point: extension.js
  permissions: [workspace_read, chat_access]
```

## Related kinds
- `mcp_server` (P04) -- richer alternative when plugin needs to expose multiple tools
- `toolkit` (P04) -- collection of capabilities that a plugin bundles for a host
- `skill` (P04) -- reusable capability unit that plugins may expose as extension points
- `hook_config` (P04) -- hook configuration that plugins may register on the host system
