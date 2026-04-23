---
id: n00_cli_tool_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "CLI Tool -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, cli_tool, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_cli_tool
  - p01_kc_cli_tool
  - bld_schema_reranker_config
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A cli_tool is a command-line interface tool that agents can invoke as a subprocess, capturing stdout, stderr, and exit codes as structured observations. It wraps external CLI binaries (git, docker, kubectl, npm) or custom scripts with a typed interface, argument validation, and timeout management. The output is a tool definition that agents call during F5 CALL to execute system-level operations.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `cli_tool` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| binary | string | yes | CLI binary name or path (e.g., git, docker, python) |
| commands | list | yes | Supported subcommands with argument specs |
| timeout_seconds | integer | yes | Maximum execution time before kill |
| working_dir | string | no | Default working directory for command execution |

## When to use
- When an agent needs to execute git, docker, kubectl, or custom shell commands
- When N05 Operations builds tools that wrap infrastructure commands for agent use
- When the F8 COLLABORATE step needs typed CLI wrappers for compile, commit, and signal

## Builder
`archetypes/builders/cli_tool-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind cli_tool --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ct_git_ops
kind: cli_tool
pillar: P04
nucleus: n05
title: "Git Operations CLI Tool"
version: 1.0
quality: null
---
binary: git
timeout_seconds: 60
commands:
  - name: commit
    args: ["-m", "{message}"]
  - name: push
    args: ["origin", "{branch}"]
  - name: log
    args: ["--oneline", "--since={since}"]
```

## Related kinds
- `code_executor` (P04) -- sandboxed runtime for executing code rather than CLI commands
- `hook` (P04) -- pre/post hooks that wrap cli_tool invocations
- `toolkit` (P04) -- collection that bundles multiple cli_tools for an agent
- `function_def` (P04) -- LLM-callable JSON schema wrapper for cli_tool commands

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_cli_tool]] | downstream | 0.45 |
| [[p01_kc_cli_tool]] | sibling | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_sandbox_spec]] | downstream | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_benchmark_suite]] | downstream | 0.37 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.36 |
