---
quality: 8.3
quality: 7.8
id: n00_context_file_manifest
kind: knowledge_card
8f: F3_inject
pillar: P03
nucleus: n00
title: "context_file -- Canonical Manifest"
version: 1.0
tags: [manifest, context_file, p03, n00, archetype, hermes_origin, workspace_instructions]
density_score: 0.94
related:
  - bld_schema_kind
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_action_prompt
  - bld_schema_quickstart_guide
  - bld_schema_search_strategy
  - bld_schema_contributor_guide
  - bld_schema_runtime_state
  - bld_schema_benchmark_suite
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A `context_file` is a project-scoped instruction file automatically injected into every agent context window, shaping behavior for a specific scope without being a full system prompt. It implements the HERMES CLAUDE.md / AGENTS.md pattern: static workspace instructions that guide every turn without consuming user-prompt tokens. The artifact is the F3 INJECT layer: read after identity (system_prompt) and before task (action_prompt), it narrows agent behavior to a specific workspace, nucleus, or session without redefining who the agent is.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique identifier: `ctx_{{scope}}` |
| kind | string | yes | Always `context_file` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| scope | enum | yes | `workspace`, `nucleus`, `session`, `global` |
| injection_point | enum | yes | `session_start`, `every_turn`, `f3_inject` |
| inheritance_chain | list | yes | Parent context_file IDs (empty = root) |
| max_bytes | integer | yes | Size budget (default 8192) |
| priority | integer | yes | Load order: 0 = highest priority |
| applies_to_nuclei | list | yes | `[all]` or specific nuclei |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |

## When to use
- When a workspace needs standing instructions for every agent turn (CLAUDE.md / AGENTS.md pattern)
- When a nucleus has nucleus-specific behavioral constraints beyond its system_prompt
- When a session needs ephemeral context that auto-expires on close
- When F3 INJECT needs a structured instruction overlay for a specific scope

## Builder
`archetypes/builders/context-file-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind context_file --execute`

## Template variables (open for instantiation)
- `{{scope}}` -- workspace | nucleus | session | global
- `{{injection_point}}` -- session_start | every_turn | f3_inject
- `{{applies_to_nuclei}}` -- [all] or list of nucleus IDs
- `{{priority}}` -- integer (0 = highest)

## Example (minimal)
```yaml
---
id: ctx_engineering_workspace
kind: context_file
pillar: P03
title: "Engineering Workspace Context"
scope: workspace
injection_point: session_start
inheritance_chain: []
max_bytes: 8192
priority: 0
applies_to_nuclei: [n03]
version: 1.0.0
quality: null
tags: [hermes_origin, workspace, n03, instructions]
---
## Workspace Rules
1. ALWAYS follow 8F pipeline for every artifact
2. NEVER commit without compiling and signaling
3. ASCII-only in all .py and .ps1 files
```

## Boundaries
| context_file IS | context_file IS NOT |
|-----------------|---------------------|
| Project-scoped static instructions auto-injected per turn | `system_prompt` (agent-level identity baseline; loaded once at boot) |
| Workspace/nucleus/session/global scope, not agent-bound | `knowledge_card` (facts and domain knowledge; not instructions) |
| Inheritance-aware overlay (child extends parent) | `prompt_template` (parameterized with `{{vars}}`; requires instantiation) |
| Injected at F3 INJECT stage of 8F | `instruction` (step-by-step procedural recipe; task-scoped) |
| Static file on disk, auto-loaded by harness | `action_prompt` (single-shot task execution; user-driven) |

## Related kinds
- `system_prompt` (P03) -- agent-level identity; context_file overlays on top after BECOME
- `knowledge_card` (P01) -- facts injected alongside; context_file carries instructions not facts
- `prompt_template` (P03) -- parameterized; context_file is static
- `instruction` (P03) -- procedural recipe; context_file is ambient standing rules
- `agent` (P02) -- loads context_file as part of session assembly

## Origin
NousResearch/hermes-agent: `CLAUDE.md` and `AGENTS.md` pattern -- project-scoped workspace instructions
auto-injected into every conversation. CEX elevates this to a first-class kind with scope, inheritance,
priority, and injection-point control.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | downstream | 0.36 |
| [[bld_schema_integration_guide]] | downstream | 0.35 |
| [[bld_schema_reranker_config]] | downstream | 0.34 |
| [[bld_schema_usage_report]] | downstream | 0.34 |
| [[bld_schema_action_prompt]] | downstream | 0.33 |
| [[bld_schema_quickstart_guide]] | downstream | 0.33 |
| [[bld_schema_search_strategy]] | downstream | 0.33 |
| [[bld_schema_contributor_guide]] | downstream | 0.33 |
| [[bld_schema_runtime_state]] | downstream | 0.32 |
| [[bld_schema_benchmark_suite]] | downstream | 0.32 |
