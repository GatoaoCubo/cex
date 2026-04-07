---
id: p01_kc_memory_cross_ide
kind: knowledge_card
pillar: P01
title: "Cross-IDE Memory Parity — One Worker API Serving Claude Code, Cursor, and OpenClaw"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: llm_engineering
quality: 9.1
tags: [cross-ide, memory, hooks, cursor, claude-code, openclaw, parity]
tldr: "Single worker API (port 37777) serves 3 IDEs via thin adapters that map IDE-specific events to universal HTTP endpoints"
when_to_use: "Building memory or context systems that must work across multiple AI coding tools"
keywords: [cross-ide, hook-parity, memory-worker, ide-adapter]
long_tails:
  - "How to build LLM memory that works across Claude Code and Cursor"
  - "How to map IDE hook events to a universal worker API"
axioms:
  - "NEVER fork core worker logic per IDE — adapters translate, worker stays universal"
  - "ALWAYS exit 0 on error — never block agent execution"
linked_artifacts:
  primary: null
  related: [p01_kc_memory_lifecycle_hooks]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
---

## TL;DR

One HTTP worker (port 37777) handles all memory operations. Each IDE (Claude Code, Cursor, OpenClaw) connects via a thin adapter script that translates IDE-specific hook events into standard HTTP calls. Core logic is never duplicated — gaps in IDE capabilities are solved by workarounds, not forks.

## Conceito Central

The cross-IDE parity pattern separates memory logic (worker) from IDE integration (adapters). The worker exposes HTTP endpoints for context injection, session init, observation capture, and summarization. Each IDE has a thin adapter (bash or JS) that maps native events to these endpoints. Where an IDE lacks a capability, the adapter implements a workaround without touching the worker.

## Arquitetura / Patterns

Hook mapping across 3 IDEs:

| Claude Code Hook | Cursor Hook | OpenClaw Event |
|-----------------|-------------|----------------|
| SessionStart | (none) | sessionStart |
| UserPromptSubmit | beforeSubmitPrompt | beforePromptBuild |
| PostToolUse | afterMCPExecution | toolResultPersist |
| Stop | stop | agentEnd |
| SessionEnd | (via stop) | sessionEnd |

Context injection per IDE:

| IDE | Method |
|-----|--------|
| Claude Code | `hookSpecificOutput` JSON via stdout |
| Cursor | `.cursor/rules/` file with alwaysApply |
| OpenClaw | `prependContext` in plugin return value |

Parity: Claude Code = full, Cursor = 95% (no transcript), OpenClaw = full (TypeScript SDK).

Cursor workarounds for missing capabilities:

| Gap | Solution |
|-----|----------|
| No SessionStart event | Context inject on every prompt submit |
| No transcript access | Summarize from observations only |
| No direct prompt injection | Write to rules file with alwaysApply |

Cursor adds capabilities Claude Code lacks: explicit shell command capture (`afterShellExecution`) and file edit capture (`afterFileEdit`) as separate hook types.

Health check is universal across all IDEs: 75 retries x 200ms = 15s timeout. Worker port 37777 shared by all adapters.

## Exemplos Praticos

```typescript
// OpenClaw plugin — thin adapter to universal worker
onBeforePromptBuild(event): BeforePromptBuildResult {
  const ctx = await fetch("http://localhost:37777/context");
  return { prependContext: ctx.text };
}

onToolResultPersist(event): void {
  fetch("http://localhost:37777/observe", {
    method: "POST",
    body: JSON.stringify({
      tool: event.name,
      output: event.result
    })
  });
}
```

## Anti-Patterns

- Fork worker logic per IDE (maintenance nightmare)
- Put business logic in adapter scripts (breaks parity)
- Block agent on hook failure (exit 0 is mandatory)
- Skip health check before calling worker API
- Assume all IDEs have SessionStart (Cursor does not)

## Referencias

- source: https://github.com/thedotmack/claude-mem
- related: p01_kc_memory_lifecycle_hooks
