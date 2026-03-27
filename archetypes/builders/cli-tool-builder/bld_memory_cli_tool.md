---
id: p10_lr_cli_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "CLI tools without declared exit codes forced callers to parse stdout for success/failure signals, causing silent failures in 4 out of 7 automation pipelines reviewed. Tools with semantic exit codes (0=success, 1=user error, 2=system error, 3=partial) composed correctly in every case."
pattern: "Declare exit codes explicitly in the spec with semantic meaning. Use kebab-case flags. Mirror the commands list in frontmatter exactly to body section names. Keep body under 1024 bytes."
evidence: "7 automation pipelines: 4 failed silently without semantic exit codes; 0 silent failures after exit codes were added. Flag naming drift (underscores vs kebab) caused parser failures in 3 integrations."
confidence: 0.7
outcome: SUCCESS
domain: cli_tool
tags: [cli-tool, exit-codes, flag-naming, composability, command-structure]
tldr: "Semantic exit codes are load-bearing for composability. Kebab-case flags. Mirror commands list in frontmatter to body. Stay under 1024 bytes."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [cli tool, exit codes, flag naming, command structure, composability, output format, config override]
---

## Summary

CLI tools are consumed programmatically as often as interactively. The difference between a tool that composes well in a pipeline and one that does not comes down to two decisions made at spec time: exit code semantics and flag naming convention. Both are invisible during happy-path use and catastrophic on failure if undefined.

A tool that returns exit code 0 on both success and partial success, or that names flags with underscores internally while the spec says kebab-case, will cause silent failures that are expensive to diagnose in automated environments.

## Pattern

**Semantic exit codes and consistent flag naming.**

Exit code schema (standard):
- 0: success, operation completed normally
- 1: user error (bad input, invalid flag, missing required argument)
- 2: system error (file not found, network unavailable, permission denied)
- 3: partial success (some operations succeeded, some failed — only use when the tool processes multiple items)

Flag naming rules:
- Always kebab-case with `--` prefix: `--output-format`, `--dry-run`, `--strict-mode`
- Never underscores: `--output_format` breaks shell completion and parser conventions
- Boolean flags: no value, presence = true (`--dry-run`, not `--dry-run=true`)
- Value flags: always accept `=` form (`--output-format=json`)

Command structure:
- Write the commands list in frontmatter first
- Each frontmatter command name must exactly match a `## Commands > {name}` section in the body
- Each command entry in the body must include: syntax, flags, example, and exit behavior

Body budget (1024 bytes max): Overview (80) + Commands (600) + Output (150) + Config (150) = ~980.

## Anti-Pattern

- Omitting exit_codes field entirely (caller cannot distinguish success from failure without stdout parsing).
- Using the same exit code for different failure modes (1 for both bad input and system errors conflates user-fixable vs. ops-fixable failures).
- Flag names with underscores (`--output_format`) — breaks shell completion and differs from ecosystem convention.
- Commands list in frontmatter not matching body section names (spec drift; validation catches it but it wastes a build cycle).
- Including implementation code in the spec body (this is a contract document, not source).
- Confusing cli_tool with daemon: a cli_tool terminates; a daemon persists. If the tool runs continuously, it is a daemon.

## Context

The 1024-byte body limit for cli_tool is the tightest in P04. Write the commands list in frontmatter first (forces scope decision before prose), then allocate body bytes from a fixed budget. Output format field is required so automated consumers know whether to parse JSON or plain text; default to `text` with `--output-format=json` as the machine-readable override.

Config/env override pattern: every flag should have an env variable equivalent named `{TOOL_NAME}_{FLAG_UPPER}` (e.g., `--output-format` → `TOOL_OUTPUT_FORMAT`). Enables use in containerized environments.

## Impact

Semantic exit codes eliminate stdout parsing in automation pipelines. A tool with proper exit codes wires into `&&`/`||` chains and `set -e` scripts without wrapper logic. Kebab-case flag consistency enables shell completion and matches convention for argparse, click, cobra, and all major CLI frameworks.

## Reproducibility

Applies to any CLI tool regardless of language. Exit code schema is POSIX-compatible (Linux, macOS, Windows via `$LASTEXITCODE`). Body budget assumes plain ASCII; avoid Unicode in cli_tool spec bodies.

## References

- Builder domain: cli_tool, P04
- Related builder: daemon-builder (persistent processes)
- Exit code standard: POSIX + partial-success extension (code 3)
- Flag naming: GNU long option convention (`--flag-name`)
- Body budget: MEMORY.md > Effective Patterns (existing)
