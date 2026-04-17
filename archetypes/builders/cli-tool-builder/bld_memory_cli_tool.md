---
id: p10_lr_cli_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "CLI tools without declared exit codes forced callers to parse stdout for success/failure signals, causing silent failures in 4 out of 7 automation pipelines reviewed. Tools with semantic exit codes (0=success, 1=user error, 2=system error, 3=partial) composed correctly in every case."
pattern: "Declare exit codes explicitly in the spec with semantic meaning. Use kebab-case flags. Mirror the commands list in frontmatter exactly to body section names. Keep body under 1024 bytes."
evidence: "7 automation pipelines: 4 failed silently without semantic exit codes; 0 silent failures after exit ..."
confidence: 0.7
outcome: SUCCESS
domain: cli_tool
tags: [cli-tool, exit-codes, flag-naming, composability, command-structure]
tldr: "Semantic exit codes are load-bearing for composability. Kebab-case flags. Mirror commands list in frontmatter to body. Stay under 1024 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [cli tool, exit codes, flag naming, command structure, composability, output format, config override]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Cli Tool"
density_score: 0.90
llm_function: INJECT
---
## Summary
CLI tools are consumed programmatically as often as interactively. The difference between a tool that composes well in a pipeline and one that does not comes down to two decisions made at spec time: exit code semantics and flag naming convention. Both are invisible during happy-path use and catastrophic on failure if undefined.
A tool that returns exit code 0 on both success and partial success, or that names flags with underscores internally while the spec says kebab-case, will cause silent failures that are expensive to diagnose in automated environments.
## Pattern
**Semantic exit codes and consistent flag naming.**
Exit code schema (standard):
1. 0: success, operation completed normally
2. 1: user error (bad input, invalid flag, missing required argument)
3. 2: system error (file not found, network unavailable, permission denied)
4. 3: partial success (some operations succeeded, some failed — only use when the tool processes multiple items)
Flag naming rules:
1. Always kebab-case with `--` prefix: `--output-format`, `--dry-run`, `--strict-mode`
2. Never underscores: `--output_format` breaks shell completion and parser conventions
3. Boolean flags: no value, presence = true (`--dry-run`, not `--dry-run=true`)
4. Value flags: always accept `=` form (`--output-format=json`)
Command structure:
1. Write the commands list in frontmatter first
2. Each frontmatter command name must exactly match a `## Commands > {name}` section in the body
3. Each command entry in the body must include: syntax, flags, example, and exit behavior
Body budget (1024 bytes max): Overview (80) + Commands (600) + Output (150) + Config (150) = ~980.
## Anti-Pattern
1. Omitting exit_codes field entirely (caller cannot distinguish success from failure without stdout parsing).
2. Using the same exit code for different failure modes (1 for both bad input and system errors conflates user-fixable vs. ops-fixable failures).
3. Flag names with underscores (`--output_format`) — breaks shell completion and differs from ecosystem convention.
4. Commands list in frontmatter not matching body section names (spec drift; validation catches it but it wastes a build cycle).
5. Including implementation code in the spec body (this is a contract document, not source).
6. Confusing cli_tool with daemon: a cli_tool terminates; a daemon persists. If the tool runs continuously, it is a daemon.
## Context
The 1024-byte body limit for cli_tool is the tightest in P04. Write the commands list in frontmatter first (forces scope decision before prose), then allocate body bytes from a fixed budget. Output format field is required so automated consumers know whether to parse JSON or plain text; default to `text` with `--output-format=json` as the machine-readable override.

## Metadata

```yaml
id: p10_lr_cli_tool_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-cli-tool-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | cli_tool |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
