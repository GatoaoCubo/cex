---
id: n00_hook_config_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Hook Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, hook_config, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A hook_config defines the lifecycle configuration for builder execution hooks, specifying which hooks are active, their execution order, timeout budgets, and failure behavior. It is the registry that settings.json reads to know which hook handlers to fire at each lifecycle event. The output is a structured configuration artifact that governs the full hook pipeline for a nucleus or global scope.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `hook_config` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| hooks | list | yes | Ordered list of hook definitions with event and handler |
| global_timeout_ms | integer | yes | Maximum total hook chain execution time |
| on_failure | string | yes | abort, warn, or continue |
| nucleus_scope | string | no | Which nucleus this config applies to (null = global) |

## When to use
- When configuring the settings.json hooks section for a nucleus or the global CEX system
- When adding new lifecycle behaviors (auto-compile, memory decay) that must be centrally managed
- When auditing which hooks are active and in what order they fire

## Builder
`archetypes/builders/hook_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind hook_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: hc_global_cex_hooks
kind: hook_config
pillar: P04
nucleus: n07
title: "CEX Global Hook Configuration"
version: 1.0
quality: null
---
global_timeout_ms: 30000
on_failure: warn
nucleus_scope: null
hooks:
  - event: SessionStart
    handler: "python _tools/cex_hooks_native.py session-start"
  - event: PostToolUse
    handler: "python _tools/cex_hooks_native.py post-tool-use"
  - event: Stop
    handler: "python _tools/cex_hooks_native.py stop"
```

## Related kinds
- `hook` (P04) -- individual hook definition referenced by hook_config
- `daemon` (P04) -- always-on alternative to event-based hook execution
- `env_config` (P09) -- environment config that complements hook_config at boot
- `nucleus_def` (P08) -- nucleus definition that references the applicable hook_config
