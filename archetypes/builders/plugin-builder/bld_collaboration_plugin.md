---
kind: collaboration
id: bld_collaboration_plugin
pillar: P04
llm_function: COLLABORATE
purpose: How plugin-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: plugin-builder

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this capability be added as a pluggable extension?"
I define interface contracts, lifecycle hooks (load/enable/disable/unload), API surfaces, config schemas, and isolation levels. I do NOT handle event interception (hook-builder), multi-phase skill workflows (skill-builder), background processes (daemon-builder), or MCP protocol servers (mcp-server-builder).
## Crew Compositions
### Crew: "Extension System Design"
```
  1. interface-builder    -> "defines the abstract contract plugins must implement"
  2. plugin-builder       -> "produces the full plugin with lifecycle and API surface"
  3. hook-builder         -> "adds event interception points around plugin lifecycle calls"
```
### Crew: "Plugin Deployment Pipeline"
```
  1. plugin-builder       -> "defines plugin contract, config schema, and dependencies"
  2. path-config-builder  -> "specifies install path, config dir, log dir per platform"
  3. permission-builder   -> "grants minimum access the plugin needs to operate"
```
### Crew: "Tool Extension"
```
  1. plugin-builder          -> "encapsulates capability as isolated pluggable extension"
  2. mcp-server-builder      -> "exposes plugin API surface via MCP protocol"
  3. skill-builder           -> "wraps plugin capabilities into a user-facing skill workflow"
```
## Handoff Protocol
### I Receive
- seeds: capability name, extension point in host system, required API surface, isolation needs
- optional: hot-reload requirement, dependency list, config schema fields, lifecycle constraints
### I Produce
- plugin artifact (Markdown, max 4KB)
- committed to: `cex/P04/examples/p04_plug_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- interface-builder: defines the contract the plugin must satisfy
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| path-config-builder | plugin declares required directories before paths are specified |
| permission-builder | grants access rights the plugin declared as required |
| hook-builder | plugin registers hooks during on_load lifecycle |
| mcp-server-builder | may wrap plugin API surface as MCP tools |
| skill-builder | may compose plugin capabilities into multi-phase workflows |
