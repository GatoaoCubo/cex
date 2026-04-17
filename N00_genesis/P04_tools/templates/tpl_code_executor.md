---
id: p04_code_executor_NAME
kind: code_executor
pillar: P04
version: 1.0.0
title: "Template — Code Executor"
tags: [template, code, executor, sandbox, runtime]
tldr: "Configures a sandboxed code execution environment. Defines language, timeout, memory limits, allowed imports, and output capture for safe code running."
quality: 9.0
domain: "tool integration"
density_score: 0.85
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Code Executor: [NAME]

## Purpose
[WHAT code gets executed — user-submitted, LLM-generated, pipeline scripts]

## Configuration
```yaml
language: [python | javascript | bash | sql]
runtime: [subprocess | docker | e2b | modal]
timeout_s: [10 | 30 | 60]
max_memory_mb: [256 | 512 | 1024]
max_output_bytes: [65536]
working_dir: "[/tmp/sandbox]"
```

## Security Sandbox

| Control | Setting | Rationale |
|---------|---------|-----------|
| Network access | [deny \| allow_list] | Prevent data exfiltration |
| File system | [read-only \| /tmp writable] | Prevent host corruption |
| Allowed imports | [ALLOW_LIST] | Only safe stdlib + specified |
| Denied imports | [os.system, subprocess, socket] | Prevent shell escapes |
| Max processes | [1] | Prevent fork bombs |

## Execution Flow
```
Input(code) → Validate(syntax) → Sandbox(limits) → Execute(timeout) → Capture(output)
                   ↓                                      ↓
              SyntaxError                           TimeoutError
              → return error                        → kill + return error
```

## Output Capture
```yaml
output:
  stdout: "[captured text, truncated to max_output_bytes]"
  stderr: "[captured text]"
  exit_code: [0 | 1 | -9]
  duration_ms: [elapsed]
  artifacts: ["[files created in working_dir]"]
```

## Error Handling
- **Syntax error**: Return error without executing
- **Timeout**: Kill process, return partial output + timeout flag
- **Memory exceeded**: OOM kill, return error
- **Import denied**: Return "import not allowed: [module]"

## Quality Gate
- [ ] Language and runtime specified
- [ ] Timeout ≤ 60s (prevent runaway)
- [ ] Memory limit set
- [ ] Network access policy defined
- [ ] Denied imports list covers dangerous modules
