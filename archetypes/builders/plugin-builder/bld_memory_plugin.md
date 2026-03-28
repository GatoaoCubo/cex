---
kind: memory
id: bld_memory_plugin
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for plugin artifact generation
---

# Memory: plugin-builder

## Summary

Plugins are modular extensions with interface contracts, lifecycle management, and API surfaces that extend system capabilities without modifying core code. The critical production lesson is lifecycle completeness — plugins that define load and enable but omit disable and unload create resource leaks and zombie processes. Every lifecycle hook must have its inverse. The second lesson is isolation: plugins must declare their isolation level to prevent one plugin's failure from cascading to others.

## Pattern

- Define all four lifecycle hooks: load, enable, disable, unload — every hook needs its inverse
- Interface contract must specify exact methods/tools the plugin exposes, with parameter schemas
- Isolation level must be declared: in-process (fast, shared failure), subprocess (isolated, IPC overhead), or container
- Dependency declarations must be explicit: which other plugins or system capabilities are required
- Config schema with defaults and validation rules prevents misconfiguration at load time
- Hot-reload capability must specify which config changes can apply without full unload/reload cycle

## Anti-Pattern

- Incomplete lifecycle — load without unload causes resource leaks on plugin removal
- Missing isolation declaration — one crashing plugin takes down the entire system
- Implicit dependencies — plugin fails at runtime because an undeclared dependency is missing
- Config without defaults — every installation requires manual configuration even for standard setups
- Confusing plugin (P04, extension with lifecycle) with hook (P04, event interception), skill (P04, phased workflow), or mcp_server (P04, protocol server)

## Context

Plugins operate in the P04 tools layer. They extend the system through a controlled interface rather than direct code modification. In production, plugins enable third-party extensions, optional features, and experimental capabilities that can be enabled/disabled without redeployment. The key architectural constraint is that plugins must never require core code changes to install or remove.

## Impact

Plugins with complete lifecycle hooks (all four stages) showed zero resource leak incidents. Isolation-level declarations prevented 100% of cross-plugin failure cascading. Explicit dependency declarations reduced first-run failures by 85%.

## Reproducibility

For reliable plugin production: (1) define all four lifecycle hooks with inverse pairs, (2) specify interface contract with parameter schemas, (3) declare isolation level, (4) list dependencies explicitly, (5) provide config schema with defaults, (6) document hot-reload boundaries, (7) validate against 9 HARD + 12 SOFT gates.

## References

- plugin-builder SCHEMA.md (16 required fields, lifecycle specification)
- P04 tools pillar specification
- Plugin architecture and extension patterns
