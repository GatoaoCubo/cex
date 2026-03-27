---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for cli_tool production
sources: POSIX conventions, CLI design principles, real tool examples
---

# Domain Knowledge: cli_tool

## Foundational Concept
A cli_tool artifact defines the CONTRACT for a command-line tool that executes a task
and terminates. It specifies commands, flags, args, output format, and exit codes.
CLI tools are ATOMIC: they run, produce output, and exit. They do not persist
in background, do not accept connections, and do not maintain state between invocations.

## Command Design Patterns

| Pattern | Example | When |
|---------|---------|------|
| Single command | `cex-validate <file>` | Simple, one-purpose tools |
| Subcommand | `cex-validate check <file>` | Multi-purpose tools |
| Flag-driven | `cex-validate --kind client --strict` | Configuration-heavy |

Rule: prefer subcommands over flag-driven for distinct operations.

## Flag Conventions

| Convention | Example | Rule |
|-----------|---------|------|
| Long form | `--verbose`, `--output-format` | Always provide, kebab-case |
| Short form | `-v`, `-o` | Optional, single letter |
| Boolean | `--strict` (no value) | True if present, false if absent |
| Value | `--format json` or `--format=json` | Space or equals separator |

## Exit Code Standards (POSIX)

| Range | Meaning |
|-------|---------|
| 0 | Success |
| 1-125 | Application-defined errors |
| 126 | Cannot execute (permission) |
| 127 | Command not found |
| 128+N | Killed by signal N |

Rule: always define 0 (success) and 1 (general error) at minimum.

## Output Patterns

| Stream | Content | Consumer |
|--------|---------|----------|
| stdout | Primary output (data, results) | Piping, parsing, display |
| stderr | Progress, warnings, errors | Human reading, logging |

Rule: structured data to stdout only. Never mix progress with data output.

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT cli_tool |
|------|------------|----------------------|
| skill | Reusable capability with phases | cli_tool has no phases, just commands |
| daemon | Persistent background process | cli_tool executes and terminates |
| plugin | Pluggable system extension | cli_tool is standalone, not pluggable |
| hook | Event-triggered script | cli_tool is explicitly invoked |
| mcp_server | Protocol server exposing tools | cli_tool is invoked directly, no protocol |
