---
kind: architecture
id: bld_architecture_plugin
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of plugin — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - plugin-builder
  - bld_collaboration_plugin
  - p03_sp_plugin_builder
  - bld_memory_plugin
  - p11_qg_plugin
  - p01_kc_plugin
  - bld_tools_plugin
  - bld_config_plugin
  - bld_knowledge_card_plugin
  - p01_kc_plugin_marketplace
---

# Architecture: plugin in the CEX

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 16-field metadata header (id, kind, pillar, domain, api_surface, etc.) | plugin-builder | active |
| interface_contract | Methods and signatures the plugin must implement | author | active |
| api_surface | Public methods and tools the plugin exposes to the host system | author | active |
| lifecycle_hooks | Load/enable/disable/unload event handlers | author | active |
| config_schema | Configuration options with defaults and validation rules | author | active |
| dependency_chain | Other plugins or services this plugin requires | author | active |
| isolation_level | Sandboxing and resource limits for the plugin runtime | author | active |
## Dependency Graph
```
host_system     --loads-->      plugin  --exposes-->     api_surface
config_schema   --configures--> plugin  --signals-->     lifecycle_event
plugin          --depends-->    dependency_chain
```
| From | To | Type | Data |
|------|----|------|------|
| host_system | plugin | consumes | host loads plugin via interface contract at startup |
| plugin | api_surface | produces | public methods and tools available to consumers |
| config_schema | plugin | data_flow | configuration options injected at load time |
| plugin | lifecycle_event (P12) | signals | emitted on load, enable, disable, unload transitions |
| plugin | dependency_chain | dependency | requires other plugins or services to function |
| hook (P04) | plugin | dependency | plugins may register hooks for event interception |
## Boundary Table
| plugin IS | plugin IS NOT |
|-----------|---------------|
| A pluggable extension with defined interface contract | An event interceptor without API surface (hook P04) |
| Has lifecycle management (load/enable/disable/unload) | A multi-phase reusable capability (skill P04) |
| Exposes API surface to the host system | A background process running independently (daemon P04) |
| Configured via schema with validated options | A protocol server exposing tools via MCP (mcp_server P04) |
| Isolated with defined resource limits | A tightly coupled core component |
| Hot-reloadable without host restart | A static library compiled into the host |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Contract | frontmatter, interface_contract | Define what the plugin must implement |
| Configuration | config_schema, dependency_chain | Configure options and declare requirements |
| Lifecycle | lifecycle_hooks, isolation_level | Manage load/unload and resource boundaries |
| Interface | api_surface | Expose public methods and tools to consumers |
| Events | lifecycle_event, hook | Signal state changes and intercept events |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[plugin-builder]] | upstream | 0.69 |
| [[bld_collaboration_plugin]] | upstream | 0.68 |
| [[p03_sp_plugin_builder]] | upstream | 0.63 |
| [[bld_memory_plugin]] | downstream | 0.62 |
| [[p11_qg_plugin]] | downstream | 0.62 |
| [[p01_kc_plugin]] | upstream | 0.57 |
| [[bld_tools_plugin]] | upstream | 0.54 |
| [[bld_config_plugin]] | downstream | 0.50 |
| [[bld_knowledge_card_plugin]] | upstream | 0.49 |
| [[p01_kc_plugin_marketplace]] | upstream | 0.47 |
