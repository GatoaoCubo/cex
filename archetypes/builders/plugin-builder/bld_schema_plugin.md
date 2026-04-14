---
kind: schema
id: bld_schema_plugin
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for plugin
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: plugin

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_plug_{slug}) | YES | - | Namespace compliance |
| kind | literal "plugin" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| interface | string | YES | - | Contract/interface this plugin implements |
| lifecycle | list[enum] from [on_load, on_enable, on_disable, on_unload, on_config_change] | YES | - | Supported lifecycle events |
| enabled | boolean | YES | true | Whether plugin is active by default |
| api_surface_count | integer | YES | - | Must match methods in API Surface section |
| dependencies | list[string] | YES | [] | Required plugins or systems |
| domain | string | YES | - | Domain this plugin serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "plugin" |
| tldr | string <= 160ch | YES | - | Dense summary |
| isolation | enum [sandboxed, shared, privileged] | REC | "shared" | Execution isolation level |
| hot_reload | boolean | REC | false | Whether plugin supports live reload |
| config_schema | object | REC | {} | Configuration schema with types and defaults |
| version_constraints | string | REC | "*" | Semver range for host compatibility |
| priority | integer | REC | 100 | Loading order (lower = first) |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## API Method Object
```yaml
method:
  name: string (snake_case identifier)
  description: string (what it does)
  input: object (parameter types)
  output: object (return type)
  idempotent: boolean
```
## Config Schema Object
```yaml
config_schema:
  field_name:
    type: enum [string, integer, boolean, list, object]
    default: any
    required: boolean
    description: string
```
## ID Pattern
Regex: `^p04_plug_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Interface Contract` — what the plugin implements, methods it must provide
2. `## API Surface` — table of exposed methods: name, input, output, description
3. `## Configuration` — config schema with types, defaults, validation
4. `## Lifecycle Hooks` — on_load, on_enable, on_disable, on_unload behavior
5. `## Dependencies` — required plugins/systems with version constraints
6. `## Testing` — how to test the plugin (unit, integration, mock strategy)
7. `## References` — sources and documentation
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_plug_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- api_surface_count MUST match actual methods in API Surface table
- lifecycle MUST contain at least [on_load, on_unload]
- dependencies list must use artifact IDs or system names
- isolation level constrains what APIs the plugin can access
- If hot_reload: true, lifecycle MUST include on_config_change
