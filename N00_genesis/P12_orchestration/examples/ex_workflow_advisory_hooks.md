---
id: p12_wf_advisory_hooks
kind: workflow
pillar: P12
title: "Workflow: 5 Advisory Hooks (Context Injection)"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
quality: 9.0
tags: [hooks, advisory, orchestration, workflow, context-injection]
tldr: "5 advisory hook types that inject context without blocking: statusline, context-monitor, workflow-guard, prompt-guard, check-update. All exit 0 always."
density_score: 0.93
related:
  - p01_kc_workflow_hooks_gsd
  - p03_sp_hook_builder
  - p10_ax_lifecycle_hooks
  - hook-builder
  - p01_kc_memory_lifecycle_hooks
  - bld_architecture_hook
  - bld_knowledge_card_hook
  - bld_collaboration_hook
  - hook-config-builder
  - bld_collaboration_hook_config
---

# Workflow: 5 Advisory Hooks (Context Injection)

## Overview

| Property | Value |
|----------|-------|
| Trigger | Hook events (PreToolUse, PostToolUse, UserPromptSubmit, Stop) |
| Input | stdin JSON from hook system |
| Output | additionalContext string injected into conversation |
| Timeout | Per-hook (3-10s); universal timeout-guard wraps all |

## Universal Pattern

```
timeout-guard (Ns) → read stdin JSON → compute advisory → inject context → exit 0
```

Advisory hooks NEVER block execution. Always exit 0.

## Steps

### Hook 1: Statusline (PostToolUse, 3s)
Update terminal status bar: agent_group state, progress, token usage.
Output: display string, no additionalContext. Value: LOW (cosmetic).

### Hook 2: Context Monitor (PostToolUse, 5s, debounced every 5 calls)
Track context window usage, warn when running low.
- `>35%` remaining: silent
- `<=35%`: `[WARN] Context at 32% — consider committing`
- `<=25%`: `[CRITICAL] Context at 18% — commit NOW and signal`
Value: HIGH — prevents lost work from context overflow.

### Hook 3: Workflow Guard (PreToolUse, 3s)
Validate tool calls against scope fence (paths in handoff).
Output: warning if tool targets path outside scope. Value: MEDIUM.

### Hook 4: Prompt Guard (UserPromptSubmit, 5s)
Scan handoff content for injection patterns, validate plan structure.
Output: warning if suspicious patterns detected. Value: MEDIUM.

### Hook 5: Check Update (Notification, 10s)
Check for queued handoffs, config changes, system updates.
Output: advisory about available work. Value: LOW.

## Error Handling
- ALL hooks exit 0 regardless of internal errors
- Errors logged to `.claude/logs/hooks/`
- Timeout-guard kills hung hooks silently
- No hook adds > 200ms to tool call latency (p95)

## Success Criteria
- All 5 hooks exit 0 consistently in production
- Context monitor triggers at <=35% threshold
- Workflow guard catches 100% out-of-scope Write/Edit calls
- Total hook overhead < 200ms per tool call (p95)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_workflow_hooks_gsd]] | upstream | 0.42 |
| [[p03_sp_hook_builder]] | upstream | 0.40 |
| [[p10_ax_lifecycle_hooks]] | upstream | 0.35 |
| [[hook-builder]] | upstream | 0.35 |
| [[p01_kc_memory_lifecycle_hooks]] | upstream | 0.33 |
| [[bld_architecture_hook]] | upstream | 0.32 |
| [[bld_knowledge_card_hook]] | upstream | 0.32 |
| [[bld_collaboration_hook]] | related | 0.32 |
| [[hook-config-builder]] | upstream | 0.31 |
| [[bld_collaboration_hook_config]] | related | 0.31 |
