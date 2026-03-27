---
id: p03_ins_plugin
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Plugin Builder Instructions
target: plugin-builder agent
phases_count: 3
prerequisites:
  - The capability to be added as a plugin is named and described
  - The interface contract or extension point the plugin will implement is known
  - At least one API method or tool the plugin must expose is identified
validation_method: checklist
domain: plugin
quality: null
tags:
  - instruction
  - plugin
  - extension
  - P04
idempotent: true
atomic: false
rollback: "Delete the produced plugin artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Research interface contract and dependencies, compose API surface with lifecycle hooks and config schema, validate gates and write a plugin artifact."
density_score: 0.89
---

## Context

The plugin-builder receives an **extensibility requirement** and produces a `plugin` artifact defining how that capability integrates into the host system as a pluggable extension — with its own interface contract, lifecycle, configuration, and API surface.

**Input variables**:
- `{{plugin_name}}` — name of the plugin in snake_case (e.g., `metrics_exporter`, `auth_provider`, `cache_layer`)
- `{{interface}}` — the interface contract or extension point the plugin implements (e.g., `IMetricsExporter`, `IAuthProvider`)
- `{{capability}}` — what capability the plugin adds to the host system (1–2 sentences)
- `{{api_methods}}` — list of methods/tools the plugin must expose (e.g., `export_metric(name, value, tags)`)
- `{{dependencies}}` — other plugins or system components this plugin requires (with version constraints if known)
- `{{hot_reload}}` — boolean: does this plugin support reconfiguration without restart? Default: `false`

**Output**: a single `plugin` artifact at `p04_plug_{{plugin_name}}.md` with interface contract, API surface table, lifecycle hooks, config schema, dependency declarations, and testing strategy.

**Boundaries**: defines pluggable extensions only. Does NOT define event interception without a full lifecycle (use hook-builder), multi-phase executable workflows (use skill-builder), background persistent processes (use daemon-builder), or MCP protocol servers (use mcp-server-builder).

---

## Phases

### Phase 1: RESEARCH

**Goal**: Understand the extension point, design the API surface, and plan the lifecycle before writing.

1. Identify the `{{interface}}` contract the plugin implements. If the interface does not yet exist, define its required methods as part of this artifact (mark as `[NEW INTERFACE]`).
2. Define the API surface: for each method in `{{api_methods}}`, record input parameters (name, type), output (type, description), and a one-line description of what the method does.
3. Determine dependencies from `{{dependencies}}`. For each dependency, record: artifact ID or system name, minimum version, and whether it is required or optional.
4. Select isolation level: `sandboxed` (no shared state, strict IPC), `shared` (shares host memory/resources), or `privileged` (full host access). Choose the minimum level necessary.
5. Determine lifecycle events. Minimum required: `on_load` (plugin initialized) and `on_unload` (plugin torn down). Add as needed:
   - `on_enable`: plugin activated after load
   - `on_disable`: plugin deactivated but not torn down
   - `on_config_change`: config updated at runtime (required if `{{hot_reload}} = true`)
   - `on_error`: called when an unhandled error occurs within the plugin
6. Design config schema: list each config key with type, default value, and whether it is required or optional.
7. Evaluate `{{hot_reload}}`. If `true`, confirm `on_config_change` is in the lifecycle. If `false`, mark hot-reload as unsupported.
8. Search existing plugins via brain_query [IF MCP]: `plugin {{interface}} {{capability}}`. Avoid duplicates; if found, determine whether update or merge is needed.
9. Determine testing strategy: unit tests (mock host interface), integration tests (real host, test config), and what mocks are needed.

**Exit**: interface contract defined, all API methods have input/output specs, lifecycle minimum (on_load + on_unload) confirmed, config schema drafted, hot_reload status resolved.

---

### Phase 2: COMPOSE

**Goal**: Produce all artifact fields and body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.

10. Read SCHEMA.md — source of truth for all 16 required fields.
11. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
12. Generate `plugin_slug` in snake_case. Set `id = p04_plug_{{plugin_slug}}` matching `^p04_plug_[a-z][a-z0-9_]+$`.
13. Fill frontmatter: all 16 required fields. Set `quality: null` — never self-score.
14. Set `interface` to the contract name from Phase 1 step 1.
15. Set `lifecycle` list to include at minimum `[on_load, on_unload]`. Add additional hooks as determined in step 5.
16. Set `api_surface_count` to exactly match the number of methods in the API Surface table (zero drift).
17. Write **Interface Contract** section: contract name, required methods list, and whether this is an existing or new interface.
18. Write **API Surface** section: table with columns `method | input | output | description`. One row per method.
19. Write **Configuration** section: config schema table with columns `key | type | default | required | description`.
20. Write **Lifecycle Hooks** section: table with columns `event | trigger | behavior`. One row per lifecycle event.
21. Write **Dependencies** section: table with columns `name | version | required`. One row per dependency.
22. Write **Testing** section: describe unit test approach (what to mock), integration test approach (what to test with real host), and list required mocks.
23. Verify body <= 2048 bytes.
24. Verify `api_surface_count` matches actual rows in the API Surface table.

**Exit**: all 16 required fields populated, `api_surface_count` matches table, body within byte limit, `on_config_change` present if `hot_reload: true`.

---

### Phase 3: VALIDATE

**Goal**: Verify all quality gates before writing the final artifact.

25. Check QUALITY_GATES.md — verify all 9 HARD gates manually.
26. Confirm `id` matches `^p04_plug_[a-z][a-z0-9_]+$`.
27. Confirm `kind == plugin`.
28. Confirm `quality == null`.
29. Confirm `api_surface_count` matches the actual number of rows in the API Surface table (zero drift — this is a common failure point).
30. Confirm `lifecycle` contains at least `[on_load, on_unload]`.
31. Confirm `dependencies` use artifact IDs or system names with version constraints, not vague descriptions.
32. If `hot_reload: true`: confirm `on_config_change` is in the lifecycle list. If missing, either add it or set `hot_reload: false`.
33. Score SOFT gates against QUALITY_GATES.md.
34. If score < 8.0: revise in same pass before outputting. Do not output a failing artifact.
35. Write the final artifact using the Output Contract template below.

---

## Output Contract

```
---
id: p04_plug_{{plugin_slug}}
kind: plugin
pillar: P04
domain: {{domain}}
version: 1.0.0
created: {{date}}
author: plugin-builder
interface: {{interface_contract_name}}
isolation: {{sandboxed|shared|privileged}}
hot_reload: {{true|false}}
lifecycle: [on_load, on_unload, {{additional_hooks}}]
api_surface_count: {{n}}
quality: null
tags: [plugin, {{plugin_slug}}, {{domain}}, extension]
---

## Interface Contract

**Contract**: `{{interface_contract_name}}`
**Type**: {{existing|new_interface}}

Required methods:
- `{{method_signature_1}}`
- `{{method_signature_2}}`

## API Surface

| Method | Input | Output | Description |
|--------|-------|--------|-------------|
| `{{method_name}}` | `{{param}}: {{type}}` | `{{return_type}}` | {{one_line_description}} |

## Configuration

| Key | Type | Default | Required | Description |
|-----|------|---------|----------|-------------|
| `{{config_key}}` | {{type}} | `{{default}}` | {{true|false}} | {{description}} |

## Lifecycle Hooks

| Event | Trigger | Behavior |
|-------|---------|---------|
| on_load | Plugin initialized by host | {{initialization_behavior}} |
| on_unload | Plugin torn down by host | {{teardown_behavior}} |
| {{on_config_change}} | Config updated at runtime | {{config_reload_behavior}} |

## Dependencies

| Name | Version | Required |
|------|---------|----------|
| `{{dependency_name}}` | `>={{version}}` | {{true|false}} |

## Testing

- **Unit**: mock `{{interface_contract_name}}` host; test each method in isolation
- **Integration**: real host with test config `{{test_config_description}}`
- **Mocks required**: `{{mock_1}}`, `{{mock_2}}`
```

---

## Validation

| # | Gate | Type |
|---|------|------|
| 1 | `id` matches `^p04_plug_[a-z][a-z0-9_]+$` | HARD |
| 2 | `kind == plugin` exactly | HARD |
| 3 | `quality: null` is set | HARD |
| 4 | `api_surface_count` matches actual row count in API Surface table | HARD |
| 5 | `lifecycle` contains at minimum `[on_load, on_unload]` | HARD |
| 6 | If `hot_reload: true`, `on_config_change` is in lifecycle | HARD |
| 7 | Dependencies use artifact IDs or system names with version constraints | HARD |
| 8 | All 16 required frontmatter fields are populated | HARD |
| 9 | `interface` field names a concrete contract, not a vague description | HARD |
| 10 | Body <= 2048 bytes | SOFT |
| 11 | Config schema has at least one key defined | SOFT |
| 12 | Testing section covers both unit and integration approaches | SOFT |

---

## Metacognition

**Does**:
- Defines pluggable extensions with a complete interface contract, lifecycle, and API surface
- Encodes configuration schema with defaults for runtime customization
- Documents dependencies with version constraints and testing strategy

**Does NOT**:
- Define event interception hooks without full lifecycle (use hook-builder)
- Define multi-phase executable workflows (use skill-builder)
- Define background persistent processes (use daemon-builder)
- Define MCP protocol servers (use mcp-server-builder)

**Chaining**: output feeds plugin registry (interface + lifecycle), host loader (dependencies + isolation level), test runner (testing section). Input from extensibility requirements, interface catalog, dependency version matrix.
