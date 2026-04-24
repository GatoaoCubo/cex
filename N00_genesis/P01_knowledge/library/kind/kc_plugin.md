---
id: p01_kc_plugin
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Plugin — Deep Knowledge for plugin"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: plugin
quality: 9.1
tags: [plugin, P04, CALL, kind-kc, extensibility]
tldr: "Discoverable, versioned, independently loadable extension that adds capabilities to the agent system at runtime via a declared interface contract"
when_to_use: "Building, reviewing, or reasoning about plugin artifacts"
keywords: [plugin, extension, pluggable, runtime, interface]
feeds_kinds: [plugin]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_collaboration_plugin
  - bld_memory_plugin
  - bld_architecture_plugin
  - p11_qg_plugin
  - plugin-builder
  - p03_sp_plugin_builder
  - bld_tools_plugin
  - bld_config_plugin
  - p01_kc_plugin_marketplace
  - bld_knowledge_card_plugin
---

# Plugin

## Spec
```yaml
kind: plugin
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_plug_{{name}}.md + .yaml
core: false
```

## What It Is
A plugin is a self-contained, versioned, independently loadable extension that adds capabilities to the agent system through a declared interface. It is registered at startup, discoverable via a manifest, and invocable at runtime. It is NOT a hook (which fires reactively on a specific event, not on-demand), NOT a skill (which is a multi-phase procedural recipe without the plugin lifecycle of discovery, registration, and versioning).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Custom tool via @tool or BaseTool | Tools are plugins; no separate concept |
| LlamaIndex | QueryEngineTool, FunctionTool | Plugin-like; registered on agent at init |
| CrewAI | Tool class with __call__ | Self-contained tool = plugin pattern |
| DSPy | Module as composable component | DSPy modules compose like plugins |
| Haystack | ComponentBase (custom component) | Pipeline components as registered plugins |
| OpenAI | ChatGPT Plugins (deprecated) | Replaced by Assistants tools API |
| Anthropic | MCP tool server | Closest equivalent; protocol-level plugin |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| interface_version | str | required | Must match host version; breaking change guard |
| lazy_load | bool | false | True = load on first call; saves startup RAM |
| isolated | bool | false | True = subprocess isolation for untrusted code |
| depends_on | list | [] | Dependency resolution at registration |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Lazy load | Optional rarely-used capability | Load browser_tool plugin only when needed |
| Versioned interface | Multi-version plugin host | plugin_api_version: "2.0" in manifest |
| Sandboxed execution | Untrusted third-party plugin | subprocess + timeout + resource limits |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No interface version in manifest | Breaking changes silently crash host | Declare interface_version; validate at load |
| Global mutable state in plugin | Interferes across parallel calls | Pass context via arguments; no class-level state |
| Synchronous blocking call | Stalls host event loop | Async interface required for all plugins |

## Integration Graph
```
[plugin_registry] --> [discover + load] --> [plugin] --> [capability_output]
       |                                       |
[manifest, version]              [interface_version, isolated, lazy_load]
```

## Decision Tree
- IF capability is event-triggered THEN use hook
- IF capability is multi-phase structured recipe THEN use skill
- IF capability needs full protocol server THEN use mcp_server
- DEFAULT: plugin for any discoverable, independently versioned runtime extension

## Quality Criteria
- GOOD: interface_version declared, loads without side effects, returns typed output
- GREAT: lazy load, isolated execution, versioned manifest, dependency graph resolved
- FAIL: no interface contract, global mutable state, no version declaration in manifest

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_plugin]] | downstream | 0.52 |
| [[bld_memory_plugin]] | downstream | 0.49 |
| [[bld_architecture_plugin]] | downstream | 0.49 |
| [[p11_qg_plugin]] | downstream | 0.48 |
| [[plugin-builder]] | downstream | 0.48 |
| [[p03_sp_plugin_builder]] | downstream | 0.47 |
| [[bld_tools_plugin]] | downstream | 0.45 |
| [[bld_config_plugin]] | downstream | 0.42 |
| [[p01_kc_plugin_marketplace]] | sibling | 0.39 |
| [[bld_knowledge_card_plugin]] | sibling | 0.38 |
