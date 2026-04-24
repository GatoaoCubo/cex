---
id: ctx_{{scope}}
kind: context_file
8f: F2_become
pillar: P03
title: "Context File: {{scope}}"
scope: workspace
injection_point: session_start
inheritance_chain: []
max_bytes: 8192
priority: 0
applies_to_nuclei: [all]
version: 1.0.0
quality: null
tags: [context_file, hermes_origin, workspace, instructions]
related:
  - p03_sp_n03_creation_nucleus
  - p03_sp_system-prompt-builder
  - p03_sp_kind_builder
  - p03_sp_context_window_config_builder
  - p03_sp_prompt_cache_builder
  - p03_sp_engineering_nucleus
  - p03_sp_type-def-builder
  - p03_sp__builder_builder
  - p03_sp_multi_modal_config_builder
  - p03_sp_validator-builder
density_score: 1.0
updated: "2026-04-22"
---

<!-- TEMPLATE: replace all {{vars}} before use. Remove this comment in final artifact. -->

## Purpose

A context_file is a workspace-level instruction set automatically injected at session start.
It governs LLM behavior across an entire project or scope boundary without requiring per-prompt
repetition. Context files implement the HERMES pattern of persistent behavioral configuration --
the equivalent of `.cursorrules`, `.clinerules`, or `CLAUDE.md` in other ecosystems, but typed,
composable, and governed by the CEX 8F pipeline.

Context files are NOT system prompts (those live in P03 as `system_prompt` kind). A system prompt
defines agent identity; a context file defines workspace rules that apply across ALL agents in scope.

## Frontmatter Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier: `ctx_{{scope}}` |
| `kind` | string | yes | Always `context_file` |
| `pillar` | string | yes | Always `P03` |
| `scope` | enum | yes | Injection scope: `workspace` / `project` / `nucleus` / `session` |
| `injection_point` | enum | yes | When loaded: `session_start` / `pre_prompt` / `on_demand` |
| `inheritance_chain` | array | no | Parent context files; child overrides parent on conflict |
| `max_bytes` | integer | yes | Hard cap on context file size (default 8192) |
| `priority` | integer | yes | Higher priority wins on conflict (0 = base, 10 = override) |
| `applies_to_nuclei` | array | yes | Which nuclei load this file: `[all]` or `[n01, n03]` |

## Scope Hierarchy

Context files follow an inheritance chain from broadest to narrowest scope. Narrower scopes
override broader ones when rules conflict.

```
workspace (broadest)
  |-- project
       |-- nucleus
            |-- session (narrowest, highest precedence)
```

| Scope | Loaded by | Lifetime | Example use |
|-------|-----------|----------|-------------|
| `workspace` | All nuclei at boot | Entire workspace lifetime | Coding standards, ASCII rule, naming conventions |
| `project` | Nuclei working on a project | Duration of project | Brand voice, domain glossary, tech stack constraints |
| `nucleus` | Single nucleus only | Nucleus session lifetime | N03-specific build patterns, N01 research protocols |
| `session` | Any nucleus, one session | Single session | Temporary overrides, experiment flags, debug modes |

## Injection Points

| Point | When | Use case |
|-------|------|----------|
| `session_start` | Loaded once at boot, before first user message | Persistent rules, identity, constraints |
| `pre_prompt` | Prepended to every prompt assembly | Token-heavy but guarantees visibility |
| `on_demand` | Loaded only when explicitly referenced | Large reference docs, optional context |

## Build Rules

1. ALWAYS {{rule_1}}
2. NEVER {{rule_2}}
3. ALWAYS {{rule_3}}

## Context Assembly Order

When multiple context files apply, they are assembled in this deterministic order:

```
1. workspace-scope context files (sorted by priority ascending)
2. project-scope context files (sorted by priority ascending)
3. nucleus-scope context files (sorted by priority ascending)
4. session-scope context files (sorted by priority ascending)
5. Conflict resolution: last-write-wins (highest priority + narrowest scope)
```

## Conflict Resolution Rules

| Conflict type | Resolution | Example |
|---------------|------------|---------|
| Same field, different scope | Narrower scope wins | Session rule overrides workspace rule |
| Same field, same scope | Higher `priority` wins | priority=5 overrides priority=0 |
| Same field, same scope, same priority | Alphabetical by `id` (deterministic) | `ctx_api` before `ctx_brand` |
| Additive fields (arrays) | Merge, deduplicate | `tags` from both are combined |
| Contradictory rules | Narrower scope wins; log warning | Workspace says ALWAYS X, session says NEVER X |

## Usage Examples

### Minimal context file (workspace coding standards)

```yaml
id: ctx_coding_standards
kind: context_file
scope: workspace
injection_point: session_start
max_bytes: 4096
priority: 0
applies_to_nuclei: [all]
```

### Nucleus-specific context file

```yaml
id: ctx_n03_build_patterns
kind: context_file
scope: nucleus
injection_point: session_start
inheritance_chain: [ctx_coding_standards]
max_bytes: 8192
priority: 5
applies_to_nuclei: [n03]
```

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `system_prompt` | P03 | System prompt = agent identity; context_file = workspace rules |
| `prompt_template` | P03 | Templates are per-task; context_files are per-scope |
| `context_window_config` | P03 | Window config sets token budget; context_file consumes budget |
| `env_config` | P09 | Env config is runtime vars; context_file is behavioral rules |
| `boot_config` | P02 | Boot config initializes agent; context_file layers on workspace rules |

## Quality Rules

1. ALWAYS set `quality: null` -- never self-score
2. ALWAYS compile after saving: `python _tools/cex_compile.py {path}`
3. NEVER commit without running `python _tools/cex_doctor.py`

## Anti-Patterns

- Do NOT put agent identity in a context file (use `system_prompt` instead)
- Do NOT exceed `max_bytes` -- the injection pipeline truncates silently
- Do NOT set `priority` above 10 -- reserved for system-level overrides
- Do NOT use `on_demand` injection for rules that must always apply
- Do NOT duplicate rules already in a parent `inheritance_chain` entry

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | related | 0.30 |
| [[p03_sp_system-prompt-builder]] | related | 0.27 |
| [[p03_sp_kind_builder]] | related | 0.26 |
| [[p03_sp_context_window_config_builder]] | related | 0.26 |
| [[p03_sp_prompt_cache_builder]] | related | 0.24 |
| [[p03_sp_engineering_nucleus]] | related | 0.23 |
| [[p03_sp_type-def-builder]] | related | 0.23 |
| [[p03_sp__builder_builder]] | related | 0.22 |
| [[p03_sp_multi_modal_config_builder]] | related | 0.21 |
| [[p03_sp_validator-builder]] | related | 0.21 |
