---
id: p01_kc_cli_tool
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "CLI Tool — Deep Knowledge for cli_tool"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: cli_tool
quality: 9.1
tags: [cli_tool, P04, CALL, kind-kc]
tldr: "Command-line tool wrapper enabling agents to execute shell commands as discrete, fire-and-forget operations"
when_to_use: "Building, reviewing, or reasoning about cli_tool artifacts"
keywords: [cli, shell-command, bash-tool]
feeds_kinds: [cli_tool]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - cli-tool-builder
  - bld_collaboration_cli_tool
  - bld_architecture_cli_tool
  - p03_sp_cli_tool_builder
  - p10_lr_cli_tool_builder
  - p11_qg_cli_tool
  - bld_examples_cli_tool
  - bld_schema_cli_tool
  - bld_instruction_cli_tool
  - bld_knowledge_card_cli_tool
---

# CLI Tool

## Spec
```yaml
kind: cli_tool
pillar: P04
llm_function: CALL
max_bytes: 1024
naming: p04_cli_{{tool}}.md
core: false
```

## What It Is
A CLI tool is a wrapper around a command-line utility that an agent can invoke as a discrete, fire-and-forget operation. It executes a shell command, captures stdout/stderr, and returns the result. It is NOT a skill (which has phases and lifecycle) nor a daemon (which persists in the background). A CLI tool runs once, returns output, and terminates.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ShellTool` / `BashProcess` | Execute shell commands as agent tools |
| LlamaIndex | Custom `FunctionTool` wrapping `subprocess` | Shell execution exposed as callable tool |
| CrewAI | `BaseTool` running `subprocess.run()` | Agent tool executing CLI commands |
| DSPy | Python `subprocess` call in `forward()` | Direct shell execution within module |
| Haystack | Custom `@component` with subprocess execution | Component wrapping CLI tool for pipeline use |
| OpenAI | `code_interpreter` (sandboxed Python) | Limited: Python execution, not arbitrary shell |
| Anthropic | `bash_20250124` tool type | Native bash tool for command execution in computer_use |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| command | string | required | Hardcoded = safe; dynamic = flexible but injection risk |
| timeout_s | int | 30 | Higher = tolerant of slow commands but blocks agent |
| allowed_commands | list | [] | Allowlist = safe; open = flexible but dangerous |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Allowlisted commands | Security-sensitive environments | Only permit `git`, `python`, `npm` commands |
| Output parsing | Structured data from CLI output | Run `git log --format=json` → parse JSON output |
| Chained commands | Multi-step shell operations | `git add . && git commit -m "msg"` as single invocation |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Unsanitized user input in commands | Command injection vulnerability | Use allowlist + parameterized commands, never string concat |
| No timeout on CLI calls | Agent hangs on stuck commands | Always set timeout_s; kill process on timeout |

## Integration Graph
```
[action_prompt] --> [cli_tool] --> [output_template]
                       |
                 [code_executor]
```

## Decision Tree
- IF command is simple and one-shot THEN cli_tool
- IF command needs sandboxing THEN use code_executor instead
- IF command runs in background THEN use daemon instead
- DEFAULT: Allowlisted cli_tool with 30s timeout

## Quality Criteria
- GOOD: Command defined, timeout set, output captured
- GREAT: Allowlisted commands, input sanitization, error code handling
- FAIL: No timeout; unsanitized input; no output capture; >1024 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cli-tool-builder]] | related | 0.47 |
| [[bld_collaboration_cli_tool]] | downstream | 0.40 |
| [[bld_architecture_cli_tool]] | downstream | 0.38 |
| [[p03_sp_cli_tool_builder]] | related | 0.35 |
| [[p10_lr_cli_tool_builder]] | downstream | 0.33 |
| [[p11_qg_cli_tool]] | downstream | 0.33 |
| [[bld_examples_cli_tool]] | downstream | 0.33 |
| [[bld_schema_cli_tool]] | downstream | 0.29 |
| [[bld_instruction_cli_tool]] | upstream | 0.29 |
| [[bld_knowledge_card_cli_tool]] | sibling | 0.28 |
