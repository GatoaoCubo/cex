---
id: p04_exec_python_sandbox
kind: code_executor
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Python Sandbox Executor"
runtime: python
sandbox_type: e2b
languages:
  - "python >=3.10"
timeout: 30
resource_limits:
  cpu: "1 vCPU"
  memory: "512MB"
  disk: "100MB"
network_access: false
file_io: true
persistent_session: false
quality: 9.1
tags: [code_executor, python, e2b, sandbox]
tldr: "E2B-sandboxed Python executor for untrusted code with 30s timeout and no network access"
description: "Runs arbitrary Python in an E2B cloud sandbox with resource limits"
domain: "tool integration"
title: "Code Executor Python Sandbox"
density_score: 0.9
---

# Python Sandbox Executor

## Overview
Executes untrusted Python code inside an E2B cloud sandbox. Used by agents that need to run user-generated or LLM-generated code safely without risking host compromise.

## Sandbox
Isolation: E2B cloud microVM — each invocation gets a fresh VM with no host access.
Escape prevention: gVisor kernel + network firewall blocks all egress.
Session: ephemeral — state discarded after each invocation.

## Languages
### Python
Version: >=3.10
Libraries: numpy, pandas, requests (pre-installed); pip install blocked at runtime.

## Limits
1. Timeout: 30s per invocation
2. CPU: 1 vCPU
3. Memory: 512MB
4. Disk: 100MB
5. Network: blocked — all egress denied by firewall
6. File I/O: read-write — scoped to /tmp sandbox directory only

## Examples
### Example 1: Simple computation
Input:
```json
{"code": "print(sum(range(100)))"}
```
Output:
```json
{"stdout": "4950\n", "stderr": "", "exit_code": 0, "duration_ms": 120}
```

## Cross-References

1. **Pillar**: P04 (Tools)
2. **Kind**: `code executor`
3. **Artifact ID**: `p04_exec_python_sandbox`
4. **Tags**: [code_executor, python, e2b, sandbox]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `code executor` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `code_executor` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
