---
kind: examples
id: bld_examples_code_executor
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of code_executor artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: code-executor-builder
## Golden Example
INPUT: "Create code executor for Python data analysis in Docker sandbox"
OUTPUT:
```yaml
id: p04_exec_python_docker
kind: code_executor
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
name: "Python Docker Executor"
runtime: python
sandbox_type: docker
languages:
  - "python 3.11+"
timeout: 60
resource_limits:
  cpu: "1 core"
  memory: "512MB"
  disk: "100MB"
network_access: false
file_io: true
persistent_session: false
quality: null
tags: [code_executor, python, docker, sandbox, data-analysis]
tldr: "Docker-sandboxed Python executor: 60s timeout, 512MB RAM, no network, file I/O enabled"
description: "Isolated Python 3.11+ executor in ephemeral Docker container for data analysis and computation"
```
## Overview
Executes Python code in an ephemeral Docker container for data analysis and computation.
Used by agents that need to run LLM-generated Python code safely — data processing, calculations, file transformations.
## Sandbox
Isolation: docker — each execution runs in a fresh container image, destroyed after completion.
Escape prevention: no host filesystem mount, no privileged mode, seccomp profile applied.
Session: ephemeral — no state carries between invocations.
## Languages
### Python
Version: 3.11+
Libraries: pandas, numpy, matplotlib, scipy (pre-installed in image)
## Limits
- Timeout: 60s per invocation
- CPU: 1 core (cgroup limit)
- Memory: 512MB (OOM-killed if exceeded)
- Disk: 100MB (tmpfs, wiped after execution)
- Network: blocked — no outbound connections
- File I/O: read-write within /workspace only
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_exec_ pattern (H02 pass)
- kind: code_executor (H04 pass)
- sandbox_type: docker (valid enum, H06 pass)
- languages: ["python 3.11+"] with version (H07 pass)
- timeout: 60 > 0 (H08 pass)
- Body has all 4 sections: Overview, Sandbox, Languages, Limits (H10 pass)
- resource_limits specified (S03 pass)
- network_access: false explicitly stated (S04 pass)
## Anti-Example
INPUT: "Create code executor"
BAD OUTPUT:
```yaml
id: executor
kind: runtime
name: Code Runner
languages: [any]
quality: 9.0
```
Runs code.
FAILURES:
1. id: "executor" has no `p04_exec_` prefix -> H02 FAIL
2. kind: "runtime" not "code_executor" -> H04 FAIL
3. quality: 9.0 (not null) -> H05 FAIL
4. Missing fields: sandbox_type, timeout, runtime -> H06 FAIL
5. languages: ["any"] — must be explicit language list -> H07 FAIL
6. No timeout defined — security risk -> H08 FAIL
7. No sandbox_type — bare metal execution implied -> H06 FAIL
8. Body missing Sandbox, Languages, Limits sections -> H10 FAIL
9. No resource limits — DoS risk -> S03 FAIL
10. No network policy stated -> S04 FAIL
