---
kind: examples
id: bld_examples_agent_computer_interface
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent_computer_interface artifacts
quality: 9.1
title: "Examples Agent Computer Interface"
version: "1.0.0"
author: n01_review
tags: [agent_computer_interface, builder, examples]
tldr: "Golden and anti-examples for ACI artifacts: terminal JSON-RPC interface vs bare untyped command list."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

## Golden Example: Terminal ACI via JSON-RPC

```markdown
---
id: p08_aci_bash_executor
kind: agent_computer_interface
pillar: P08
title: "Bash Executor ACI"
version: "1.0.0"
domain: terminal
protocol: json_rpc
quality: null
tldr: "JSON-RPC 2.0 ACI for executing bash commands with structured stdout/stderr observation."
---

## Overview
| Attribute | Value |
|-----------|-------|
| Interface type | terminal |
| Protocol | JSON-RPC 2.0 |
| Transport | Unix domain socket (/var/run/agent_exec.sock) |
| Auth method | token (bearer) |

## Action Space
| Action | Input Schema | Output Schema | Error States |
|--------|-------------|--------------|--------------|
| bash_exec | {cmd: string, timeout_ms: int} | {stdout: string, stderr: string, exit_code: int} | timeout / permission_denied |
| file_read | {path: string} | {content: string, size_bytes: int} | not_found / permission_denied |
| file_write | {path: string, content: string} | {written_bytes: int} | disk_full / permission_denied |

## Observation Schema
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| stdout | string | subprocess stdout | Truncated at 65536 chars |
| stderr | string | subprocess stderr | Truncated at 8192 chars |
| exit_code | int | process exit status | 0 = success |

## Error Protocol
| Code | Meaning | Recovery |
|------|---------|---------|
| -32600 | Invalid request JSON | Retry with corrected schema |
| timeout | Command exceeded timeout_ms | Reduce scope or increase budget |
| permission_denied | Action outside sandbox scope | Check sandbox_config constraints |

## Security & Sandboxing
| Constraint | Value | Enforcement |
|-----------|-------|------------|
| Execution scope | /tmp and /workspace only | seccomp allowlist |
| Auth required | Yes -- bearer token | Verified per request |
| Rate limit | 60 requests/min | Token bucket |
```

## Anti-Examples

| Anti-pattern | Problem | Correct Approach |
|-------------|---------|-----------------|
| action: "run any command" | No schema, unbounded scope | Define typed actions with input/output schemas |
| Missing error_protocol | Agent cannot recover from failures | Document all error codes and recovery strategies |
| protocol: "custom" without spec | Unimplementable, ambiguous | Use named standard (JSON-RPC / MCP / REST) |
| No auth_method field | Security gap for autonomous agents | Always specify auth_method, even if "none" |
| Observation as raw text blob | LLM cannot parse reliably | Structure observations as typed fields |
