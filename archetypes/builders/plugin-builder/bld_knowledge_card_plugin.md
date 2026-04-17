---
kind: knowledge_card
id: bld_knowledge_card_plugin
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for plugin production — atomic searchable facts
sources: plugin-builder MANIFEST.md + SCHEMA.md, VS Code extensions, WordPress plugins
quality: 9.1
title: "Knowledge Card Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: plugin

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Executive Summary
Plugins are modular extension artifacts that add capabilities to a host system through a defined interface contract with lifecycle management. Each plugin declares the interface it implements, API surface with method signatures, config schema, lifecycle hooks (minimum on_load/on_unload), and isolation level. They differ from hooks (single-event interception), skills (multi-phase workflows), MCP servers (protocol-based providers), and connectors (external service integrations) by providing a complete pluggable API surface with explicit lifecycle and isolation.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools/infrastructure) |
| Kind | `plugin` (exact literal) |
| ID pattern | `p04_plug_{slug}` |
| Required frontmatter | 16 fields |
| Quality gates | 9 HARD + 12 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min lifecycle hooks | 2 (on_load + on_unload) |
| Min API surface entries | 1 (method + signature + return type) |
| Isolation levels | sandboxed, shared, privileged |
## Patterns
| Pattern | Application |
|---------|-------------|
| Interface contract first | Define what plugin MUST implement before writing code |
| Mandatory lifecycle | on_load initializes, on_unload cleans up (leak prevention) |
| Explicit dependencies | Declare all requirements with semver version constraints |
| Isolation declaration | sandboxed (no host access), shared (read host), privileged (full) |
| Config over code | Behavior changes via config_schema, not code modification |
| Hot-reload guard | If hot_reload: true, lifecycle MUST include on_config_change |
| API surface minimalism | Expose only intentional methods; hide internals |
| Priority ordering | Lower priority loads first (infrastructure before features) |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No interface field | Plugin without declared interface is an orphan |
| Missing on_load/on_unload | Fails HARD gate — minimum lifecycle required |
| API surface without method signatures | Callers need concrete API, not descriptions |
| hot_reload: true without on_config_change | Hot-reload without config handler causes stale state |
| No isolation_level declared | Unknown side-effect scope; security risk |
| No version_constraints for host | Incompatible host version causes silent failures |
| Privileged isolation without justification | Violates least privilege principle |
## Application
1. Identify the host interface this plugin implements
2. Define API surface: method name, signature, return type per method
3. Declare lifecycle hooks (minimum: on_load, on_unload)
4. Set isolation_level (sandboxed/shared/privileged)
5. Define config_schema with fields, types, and defaults
6. List dependencies with semver version constraints
7. Set hot_reload flag; add on_config_change if true
8. Validate: 9 HARD + 12 SOFT gates, body <= 4096 bytes
## References
- plugin-builder SCHEMA.md v1.0.0
- VS Code Extension API documentation
- Martin Fowler: Plugin Architecture pattern
- WordPress Plugin API
