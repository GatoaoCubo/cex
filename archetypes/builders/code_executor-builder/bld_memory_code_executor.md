---
id: p10_lr_code_executor_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
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
satellite: edison
keywords: [code executor, sandbox, docker, e2b, timeout, network access, resource limits, isolation, security]
---

## Summary
Code executors are the highest-risk P04 kind because they run arbitrary code. The difference between a safe executor and a dangerous one comes down to three mandatory constraints: timeout (prevents resource exhaustion), network policy (prevents data exfiltration), and sandbox type (prevents host access). All three must be explicit in the spec.
## Pattern
**Mandatory timeout, explicit network policy, container-minimum isolation.**
Timeout rules:
- Default: 30s for computation, 60s for file processing, 300s for ML workloads
- MUST be > 0 — zero or absent timeout = runaway execution risk
- Implementation should kill process at timeout, not just log a warning
Network rules:
- Default: false (no network access)
- If true: document WHY and what endpoints are allowlisted
- Never allow unrestricted outbound — use allowlist
Isolation hierarchy: vm > e2b > docker > wasm > process
- Production: docker minimum
- Development: process acceptable with explicit "dev only" flag
## Anti-Pattern
- No timeout (infinite loops exhaust resources, block execution queue).
- Implicit network access (code can exfiltrate data to external endpoints).
- Process-level isolation in production (code accesses host filesystem, environment variables).
- "languages: [any]" instead of explicit list (unsupported languages fail silently).
- No resource limits (code allocates all available memory, crashes host).
- Persistent sessions without cleanup policy (disk fills, secrets persist).
## Context
The 2048-byte body limit allows detailed sandbox and limits documentation. Timeout is the single most critical field — it is the last line of defense against runaway code. The sandbox_type field determines the security boundary — container (docker) is the minimum for production use. E2B and VM provide stronger isolation at the cost of startup latency.
