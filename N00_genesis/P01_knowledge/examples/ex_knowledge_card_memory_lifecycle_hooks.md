---
id: p01_kc_memory_lifecycle_hooks
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Memory Lifecycle Hooks — 5-Stage Capture-Compress-Inject Loop for Persistent LLM Memory"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: llm_engineering
quality: 9.1
tags: [memory, lifecycle-hooks, capture, compression, context-injection, llm-memory]
tldr: "5 lifecycle hooks form a capture-compress-inject loop: Setup, SessionStart, PostToolUse, Stop, and SessionEnd"
when_to_use: "Building persistent memory for agentic IDE/CLI tools with hook-based event systems"
keywords: [lifecycle-hooks, memory-worker, session-management, observation-capture]
long_tails:
  - "How to implement persistent memory using lifecycle hooks"
  - "What is the capture-compress-inject pattern for LLM memory"
axioms:
  - "NEVER mix capture and compression in the same hook"
  - "ALWAYS exit 0 on error — hooks must never block the agent"
linked_artifacts:
  primary: null
  related: [p01_kc_memory_cross_ide]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p10_ax_lifecycle_hooks
  - p01_kc_memory_cross_ide
  - p01_kc_memory_privacy_controls
  - p03_sp_hook_builder
  - bld_architecture_hook
  - bld_knowledge_card_hook
  - p01_kc_memory_worker_service
  - hook-builder
  - p12_wf_advisory_hooks
  - hook-config-builder
---

## TL;DR

Five lifecycle hooks form a complete memory pipeline: Setup checks dependencies, SessionStart injects past context, UserPromptSubmit initializes session records, PostToolUse captures observations, and Stop/SessionEnd triggers AI compression and finalization. Each hook has a single responsibility and communicates via HTTP to a background worker on port 37777.

## Conceito Central

The pattern separates memory concerns across hook boundaries. Each hook fires at a specific lifecycle moment, does one thing, and delegates to the worker via HTTP. This prevents coupling between capture (PostToolUse) and compression (Stop) — expensive AI summarization runs once per session, not per tool call. Hooks are thin scripts with no business logic; the worker holds all state and intelligence.

## Arquitetura / Patterns

| Hook | Trigger | Responsibility | Matcher |
|------|---------|---------------|---------|
| Setup | Pre-lifecycle | Dep check (Bun, uv, SQLite) | -- |
| SessionStart | Session opens | Inject past memory into context | startup/clear/compact |
| UserPromptSubmit | Every prompt | Create session record, privacy check | * |
| PostToolUse | Every tool call | Capture tool name + input + output | * |
| Stop | Agent stops | AI compression of observations | * |
| SessionEnd | Session closes | Finalize session record | * |

Hook execution flow:

```
Hook fires (IDE event)
  -> node bun-runner.js worker-service.cjs hook {ide} {type}
  -> Worker receives stdin JSON payload
  -> Worker processes (DB write / AI call / context fetch)
  -> Worker returns JSON response to stdout
  -> Hook exits 0 (success) / 1 (non-blocking) / 2 (blocking)
```

Key metrics:

| Parameter | Value |
|-----------|-------|
| Total hooks | 5 + 1 pre-hook (Setup) |
| Worker port | 37777 |
| Health check | 75 retries x 200ms = 15s |
| Setup timeout | 300s |
| SessionStart timeout | 60s |
| PostToolUse timeout | 120s |
| Stop timeout | 120s |
| SessionEnd timeout | 30s |

Exit code semantics: 0 = success/graceful, 1 = non-blocking warning (stderr to user), 2 = blocking error (stderr to Claude). All hooks default to exit 0 on failure to prevent terminal tab accumulation.

SessionStart uses matcher `startup|clear|compact` to inject context only on real session starts. PostToolUse and Stop use wildcard matcher to capture every event without filtering.

## Exemplos Praticos

```bash
#!/bin/bash
# Hook script — thin, no business logic
node bun-runner.js worker-service.cjs hook claude-code PostToolUse
exit $?

# Worker handles the actual logic:
# 1. Parse stdin JSON (tool_name, input, output)
# 2. Store observation in SQLite
# 3. Return acknowledgment JSON to stdout
```

## Anti-Patterns

- Mix capture + compression in one hook (adds latency)
- Put business logic in hook scripts (breaks portability)
- Use filesystem for hook-worker communication (fragile)
- Run AI summarization per tool call instead of per session
- Ignore exit code semantics (1 vs 2 matters)
- Skip health check before worker calls (75x200ms pattern)

## Referencias

- source: https://github.com/thedotmack/claude-mem
- related: p01_kc_memory_cross_ide

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_ax_lifecycle_hooks]] | downstream | 0.57 |
| [[p01_kc_memory_cross_ide]] | sibling | 0.44 |
| [[p01_kc_memory_privacy_controls]] | sibling | 0.43 |
| [[p03_sp_hook_builder]] | downstream | 0.42 |
| [[bld_architecture_hook]] | downstream | 0.41 |
| [[bld_knowledge_card_hook]] | sibling | 0.40 |
| [[p01_kc_memory_worker_service]] | sibling | 0.40 |
| [[hook-builder]] | downstream | 0.39 |
| [[p12_wf_advisory_hooks]] | downstream | 0.37 |
| [[hook-config-builder]] | downstream | 0.34 |
