---
id: p01_kc_code_executor
kind: knowledge_card
type: kind
pillar: P04
title: "Code Executor — Deep Knowledge for code_executor"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: code_executor
quality: 9.1
tags: [code_executor, P04, CALL, kind-kc]
tldr: "Sandboxed runtime environment for executing LLM-generated code safely with resource limits and output capture"
when_to_use: "Building, reviewing, or reasoning about code_executor artifacts"
keywords: [sandbox, runtime, code-execution]
feeds_kinds: [code_executor]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_knowledge_card_code_executor
  - p03_sp_code_executor_builder
  - code-executor-builder
  - p04_exec_python_sandbox
  - bld_collaboration_code_executor
  - bld_examples_code_executor
  - p10_lr_code_executor_builder
  - bld_architecture_code_executor
  - sandbox-config-builder
  - bld_instruction_code_executor
---

# Code Executor

## Spec
```yaml
kind: code_executor
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_exec_{{runtime}}.md + .yaml
core: true
```

## What It Is
A code executor is a sandboxed runtime environment where LLM-generated code runs safely with resource limits, output capture, and isolation from the host system. It supports languages like Python, JavaScript, or shell scripts. It is NOT a cli_tool (which runs a pre-defined command without sandboxing) nor a daemon (which persists in the background). A code executor runs user/agent-generated code in isolation and returns results.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `PythonREPLTool` / `E2B` integration | Execute Python in REPL or cloud sandbox |
| LlamaIndex | `CodeInterpreterToolSpec` | Code execution as a tool spec for agents |
| CrewAI | `BaseTool` wrapping execution sandbox | Agent tool running code in isolated environment |
| DSPy | `ProgramOfThought` module | Generates and executes code as reasoning strategy |
| Haystack | Custom `@component` with sandboxed execution | Code execution component in pipeline |
| OpenAI | `code_interpreter` tool (Assistants API) | Sandboxed Python execution on OpenAI infrastructure |
| Anthropic | `code_execution` server tool | Code execution on Anthropic infrastructure (server-side) |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| runtime | enum | "python" | Python = rich ecosystem; JS = web-native; shell = system ops |
| sandbox_type | enum | "docker" | Docker = strong isolation; E2B = managed cloud; local = fast but risky |
| timeout_s | int | 60 | Higher = handles complex computation but risk of runaway code |
| memory_limit_mb | int | 256 | Higher = handles large datasets but risk of resource exhaustion |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Docker sandbox | Self-hosted, strong isolation needed | Spawn container per execution, destroy after |
| Cloud sandbox (E2B) | No infra management desired | API call to E2B, code runs in managed sandbox |
| REPL loop | Interactive code refinement | Agent writes code → executes → reads output → iterates |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Executing LLM code on host without sandbox | Arbitrary code execution vulnerability | Always use sandbox: Docker, E2B, or serverless |
| No resource limits | Infinite loops or memory bombs crash host | Set timeout_s and memory_limit_mb on every execution |

## Integration Graph
```
[action_prompt] --> [code_executor] --> [output_template]
                         |
                   [cli_tool, api_client]
```

## Decision Tree
- IF code is LLM-generated THEN always use sandboxed code_executor
- IF code is trusted/pre-defined THEN cli_tool may suffice
- IF need managed infrastructure THEN use cloud sandbox (E2B, OpenAI, Anthropic)
- IF need self-hosted control THEN use Docker sandbox
- DEFAULT: Docker sandbox with Python runtime, 60s timeout, 256MB limit

## Quality Criteria
- GOOD: Runtime specified, sandbox type defined, resource limits set
- GREAT: Output capture with structured format, error isolation, cleanup on timeout
- FAIL: No sandbox; no resource limits; executes on host directly; >2048 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_code_executor]] | sibling | 0.49 |
| [[p03_sp_code_executor_builder]] | related | 0.46 |
| [[code-executor-builder]] | related | 0.46 |
| [[p04_exec_python_sandbox]] | related | 0.45 |
| [[bld_collaboration_code_executor]] | downstream | 0.42 |
| [[bld_examples_code_executor]] | downstream | 0.41 |
| [[p10_lr_code_executor_builder]] | downstream | 0.37 |
| [[bld_architecture_code_executor]] | downstream | 0.37 |
| [[sandbox-config-builder]] | downstream | 0.33 |
| [[bld_instruction_code_executor]] | upstream | 0.32 |
