---
id: p01_kc_memory_worker_service
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Background Worker Service Pattern for LLM Memory Daemons"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: llm_memory
quality: 9.1
tags: [worker-service, daemon, bun, express, async, memory, hooks]
tldr: "Persistent Bun/Express daemon on port 37777 handles AI ops async — hooks POST as thin clients, auto-restart via health polling"
when_to_use: "Building memory or AI processing layer that multiple hooks/triggers share without blocking the main agent"
keywords: [worker-service, daemon, bun, express, health-check, detached-process]
long_tails:
  - "How to build a persistent background worker for Claude Code hooks"
  - "What is the daemon pattern for async AI operations in LLM tools"
axioms:
  - "SEMPRE fazer health check antes de chamar endpoint do worker"
  - "NUNCA propagar erros do worker para o exit code do hook"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p01_kc_memory_lifecycle_hooks
  - p01_kc_memory_privacy_controls
  - p01_kc_memory_cross_ide
  - p10_ax_lifecycle_hooks
  - n06_api_access_pricing
  - p03_sp_hook_builder
  - hook-builder
  - kc_api_reference
  - self_audit_newpc
  - bld_architecture_hook
---

## Summary

Persistent Express API daemon running on Bun (port 37777) centralizes AI processing
for LLM tool hooks: summarization, embedding generation, context retrieval.
Hooks act as thin HTTP clients — POST data, GET context, never run AI locally.
Worker spawns detached at session start; bun-runner.js auto-restarts on failure.
Supports three AI providers: Claude (default), Gemini, OpenRouter.

## Spec

| Parameter | Value | Config |
|-----------|-------|--------|
| Default port | 37777 | CLAUDE_MEM_WORKER_PORT env |
| Data directory | ~/.claude-mem | CLAUDE_MEM_DATA_DIR env |
| Health poll (hook) | 75 x 200ms = 15s | Hardcoded in bun-runner |
| Health poll (install) | 30 x 1000ms = 30s | Hardcoded in installer |
| Runtime | Bun (auto-installed) | Path detection |
| Worker script | worker-service.cjs | Fixed path |
| Launcher | bun-runner.js | Fixed path |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | /api/health | Liveness probe before every hook call |
| GET | /api/readiness | Full readiness check for operations |
| POST | /api/sessions/init | Create or resume session record |
| POST | /api/sessions/observations | Store tool observation for memory |
| POST | /api/sessions/summarize | Trigger AI summary generation |
| GET | /api/context/inject | Retrieve relevant context for injection |

## Patterns

| Trigger | Action |
|---------|--------|
| Multiple hooks need shared state | Use daemon with shared SQLite + Chroma |
| AI operation would block hook | Queue async in worker, return fast |
| Worker process dies mid-session | bun-runner.js auto-detects and restarts |
| Need visual memory inspection | Web UI served at same port (37777) |
| Adding new AI provider | Extend provider map (claude/gemini/openrouter) |

## Anti-Patterns

- Spawning worker per-hook call (state loss, resource waste)
- Running AI ops synchronously in hook (blocks agent loop)
- Propagating worker errors to hook exit codes (breaks agent)
- Using stdio pipe on detached process (prevents parent exit)
- Hardcoding port without env var config (blocks multi-instance)

## Code

<!-- lang: typescript | purpose: detached worker spawn + health poll -->
```typescript
const child = spawn(bunPath, [workerScript], {
  cwd: projectDir,
  detached: true,
  stdio: 'ignore',
  env: {
    ...process.env,
    CLAUDE_MEM_WORKER_PORT: workerPort,
    CLAUDE_MEM_DATA_DIR: expandedDataDir,
  },
});
child.unref();

const alive = await pollHealthEndpoint(port, 30);
if (!alive) throw new Error('Worker failed to start');
```

## References

- source: https://github.com/thedotmack/claude-mem
- source: https://bun.sh/docs/api/spawn
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_lifecycle_hooks]] | sibling | 0.40 |
| [[p01_kc_memory_privacy_controls]] | sibling | 0.38 |
| [[p01_kc_memory_cross_ide]] | sibling | 0.28 |
| [[p10_ax_lifecycle_hooks]] | downstream | 0.24 |
| [[n06_api_access_pricing]] | downstream | 0.24 |
| [[p03_sp_hook_builder]] | downstream | 0.23 |
| [[hook-builder]] | downstream | 0.21 |
| [[kc_api_reference]] | sibling | 0.21 |
| [[self_audit_newpc]] | related | 0.21 |
| [[bld_architecture_hook]] | downstream | 0.21 |
