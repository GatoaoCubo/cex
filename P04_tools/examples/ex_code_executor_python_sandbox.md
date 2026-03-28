---
id: p04_exec_python_sandbox
kind: code_executor
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
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
quality: null
tags: [code_executor, python, e2b, sandbox]
tldr: "E2B-sandboxed Python executor for untrusted code with 30s timeout and no network access"
description: "Runs arbitrary Python in an E2B cloud sandbox with resource limits"
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
- Timeout: 30s per invocation
- CPU: 1 vCPU
- Memory: 512MB
- Disk: 100MB
- Network: blocked — all egress denied by firewall
- File I/O: read-write — scoped to /tmp sandbox directory only

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
