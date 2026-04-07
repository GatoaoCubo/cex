---
kind: knowledge_card
id: bld_knowledge_card_cli_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for cli_tool production — command-line tool specification
sources: POSIX conventions, GNU CLI standards, 12-Factor CLI patterns
quality: 9.1
title: "Knowledge Card Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: cli_tool
## Executive Summary
CLI tools are atomic command-line executables that run a task and terminate. They define commands, flags, args, output formats, and exit codes. CLI tools are POSIX-compatible single-invocation programs — they do not persist in background (daemon), accept connections (server), or maintain inter-invocation state.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Output formats | text, json, table, yaml |
| Exit code 0 | success |
| Exit codes 1-125 | application-defined errors |
| Streams | stdout (data), stderr (progress/errors) |
| Flag convention | --long-form (required), -s short (optional) |
## Patterns
- **Command design**: single command for one-purpose tools; subcommands for multi-purpose tools; flag-driven for configuration-heavy operations
- **POSIX exit codes**: 0=success, 1=general error, 126=cannot execute, 127=not found, 128+N=killed by signal N
- **Stream discipline**: structured data to stdout only; progress, warnings, and errors to stderr — never mix data with diagnostic output
- **Flag conventions**: always provide --long-form (kebab-case); short form (-v) optional; booleans are true-if-present
| Pattern | Example | When to use |
|---------|---------|-------------|
| Single command | `validate <file>` | Simple one-purpose tools |
| Subcommand | `validate check <file>` | Multi-operation tools |
| Flag-driven | `validate --kind client --strict` | Configuration-heavy tools |
- **Config precedence**: CLI flags > environment variables > config file > defaults — explicit overrides implicit
- **Composability**: tools should work with pipes (`tool1 | tool2`) via stdin/stdout
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Missing exit codes | Calling scripts cannot detect success/failure |
| Data mixed with progress on stdout | Piping breaks; downstream parser gets noise |
| No --help flag | Users cannot discover commands or flags |
| Interactive prompts in non-TTY | Breaks automation and piping |
| State between invocations | That is a daemon, not a CLI tool |
| Verbose output by default | Pipes and scripts need quiet defaults; use --verbose |
## Application
1. Define purpose: what single task does this tool perform?
2. Design commands: single, subcommand, or flag-driven pattern
3. Specify flags: --long-form required, -short optional, with types and defaults
4. Define exit codes: 0 (success), 1 (error), and domain-specific codes
5. Set output format: text for humans, json for machines, table for both
6. Validate: stdout is clean data, stderr is diagnostics, --help works
## References
- POSIX: command-line utility conventions and exit codes
- GNU: argument syntax conventions
- 12-Factor CLI: principles for well-behaved command-line tools
- clig.dev: command-line interface guidelines
