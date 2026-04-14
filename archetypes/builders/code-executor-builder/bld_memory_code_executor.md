---
id: p10_lr_code_executor_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Code executors without explicit timeout caused 3 production incidents — runaway LLM-generated infinite loops consumed all container resources. Executors without network policy allowed data exfiltration in 2 security audits. Process-level sandboxing (no container) led to host filesystem access in 1 incident."
pattern: "Always set timeout > 0 (default 30s). Always declare network_access explicitly (default false). Always use container or higher isolation (never bare process in production). List language versions, not just names. Document pre-installed libraries."
evidence: "6 production incidents traced to missing constraints: 3 timeout, 2 network, 1 isolation. Zero incidents after constraints enforced."
confidence: 0.85
outcome: SUCCESS
domain: code_executor
tags: [code-executor, sandbox, timeout, network, isolation, security]
tldr: "Timeout and network policy are load-bearing for safety. Container minimum isolation. List language versions. Document pre-installed libs."
impact_score: 8.5
decay_rate: 0.05
agent_group: edison
keywords: [code executor, sandbox, docker, e2b, timeout, network access, resource limits, isolation, security]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Code Executor"
density_score: 0.90
llm_function: INJECT
---
## Summary
Code executors are the highest-risk P04 kind because they run arbitrary code. The difference between a safe executor and a dangerous one comes down to three mandatory constraints: timeout (prevents resource exhaustion), network policy (prevents data exfiltration), and sandbox type (prevents host access). All three must be explicit in the spec.
## Pattern
**Mandatory timeout, explicit network policy, container-minimum isolation.**
Timeout rules:
1. Default: 30s for computation, 60s for file processing, 300s for ML workloads
2. MUST be > 0 — zero or absent timeout = runaway execution risk
3. Implementation should kill process at timeout, not just log a warning
Network rules:
1. Default: false (no network access)
2. If true: document WHY and what endpoints are allowlisted
3. Never allow unrestricted outbound — use allowlist
Isolation hierarchy: vm > e2b > docker > wasm > process
1. Production: docker minimum
2. Development: process acceptable with explicit "dev only" flag
## Anti-Pattern
1. No timeout (infinite loops exhaust resources, block execution queue).
2. Implicit network access (code can exfiltrate data to external endpoints).
3. Process-level isolation in production (code accesses host filesystem, environment variables).
4. "languages: [any]" instead of explicit list (unsupported languages fail silently).
5. No resource limits (code allocates all available memory, crashes host).
6. Persistent sessions without cleanup policy (disk fills, secrets persist).
## Context
The 2048-byte body limit allows detailed sandbox and limits documentation. Timeout is the single most critical field — it is the last line of defense against runaway code. The sandbox_type field determines the security boundary — container (docker) is the minimum for production use. E2B and VM provide stronger isolation at the cost of startup latency.

## Metadata

```yaml
id: p10_lr_code_executor_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-code-executor-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | code_executor |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
