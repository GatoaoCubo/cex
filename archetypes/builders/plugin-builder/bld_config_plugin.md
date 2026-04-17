---
kind: config
id: bld_config_plugin
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: plugin Production Rules

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_plug_{slug}.md` | `p04_plug_metrics_exporter.md` |
| Builder directory | kebab-case | `plugin-builder/` |
| Frontmatter fields | snake_case | `api_surface_count`, `config_schema` |
| Plugin slug | snake_case, lowercase | `metrics_exporter`, `auth_provider` |
| API method names | snake_case | `record_metric`, `health_check` |
| Config field names | snake_case | `endpoint_url`, `flush_interval_ms` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P04_tools/examples/p04_plug_{slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_plug_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80
## Isolation Level Guide
| Level | Host Access | Use case | Risk |
|-------|------------|----------|------|
| sandboxed | None (own memory only) | Untrusted plugins, third-party | Lowest |
| shared | Read host state, call host API | Most internal plugins | Medium |
| privileged | Full host access, modify state | Infrastructure plugins only | Highest |
## Lifecycle Event Guide
| Event | When | Required | Typical Action |
|-------|------|----------|---------------|
| on_load | Plugin loaded into registry | YES | Initialize resources, validate config |
| on_enable | Plugin activated | NO | Start timers, connect to services |
| on_disable | Plugin deactivated (not unloaded) | NO | Stop timers, flush buffers |
| on_unload | Plugin removed from registry | YES | Release resources, final cleanup |
| on_config_change | Config modified at runtime | IF hot_reload | Update internal state from new config |
## Priority Guide
| Range | Category | Example |
|-------|----------|---------|
| 0-49 | Infrastructure | Logging, metrics, auth |
| 50-99 | Core features | Data processing, formatting |
| 100-149 | Standard (default) | Domain-specific extensions |
| 150-199 | Optional | Nice-to-have features |
| 200+ | Low priority | Experimental, debug |
