---
id: n00_hook_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "Hook -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, hook, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_hook
  - bld_schema_hook_config
  - hook-builder
  - p03_sp_hook_builder
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_collaboration_hook
  - bld_schema_integration_guide
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A hook is a pre/post processing interceptor that executes at specific lifecycle events in the builder pipeline (before tool use, after tool use, on session start, on stop). It enables cross-cutting concerns like validation, logging, memory decay, and signal emission without modifying core builder logic. The output is a hook handler definition registered in settings.json that fires automatically at the configured lifecycle event.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `hook` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| lifecycle_event | string | yes | PreToolUse, PostToolUse, SessionStart, Stop, PostCompact |
| handler | string | yes | Command or script executed when hook fires |
| scope | string | yes | global, nucleus, or kind-specific |
| blocking | boolean | yes | Whether hook failure blocks the triggering operation |

## When to use
- When implementing pre-commit validation, auto-compile, or memory decay as automatic pipeline steps
- When building the cex_hooks_native.py integration that fires on Claude Code lifecycle events
- When a builder ISO needs automatic behavior (signal emission, quality check) without manual invocation

## Builder
`archetypes/builders/hook-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind hook --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: hook_post_tool_compile
kind: hook
pillar: P04
nucleus: n07
title: "Post-Tool Compile Hook"
version: 1.0
quality: null
---
lifecycle_event: PostToolUse
handler: "python _tools/cex_hooks_native.py post-tool-use"
scope: global
blocking: false
```

## Related kinds
- `hook_config` (P04) -- configuration that registers and manages multiple hooks
- `daemon` (P04) -- long-running alternative to event-triggered hooks
- `cli_tool` (P04) -- the CLI command that hook handlers typically invoke
- `learning_record` (P11) -- artifact that hooks may write when capturing session learnings

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_hook]] | downstream | 0.47 |
| [[bld_schema_hook_config]] | downstream | 0.46 |
| [[hook-builder]] | related | 0.42 |
| [[p03_sp_hook_builder]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_usage_report]] | downstream | 0.39 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_collaboration_hook]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
