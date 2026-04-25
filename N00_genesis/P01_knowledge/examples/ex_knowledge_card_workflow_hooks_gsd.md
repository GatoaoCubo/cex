---
id: p01_kc_workflow_hooks_gsd
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "GSD Workflow Hooks — Advisory Enforcement for Claude Code Agents"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: hook_engineering
quality: 9.1
tags: [hooks, workflow, advisory, context-monitor, prompt-guard, claude-code]
tldr: "5 JS hooks enforce workflow without blocking — advisory via additionalContext, timeout guard, silent fail"
when_to_use: "Design hooks for Claude Code that guide agents without blocking execution"
keywords: [gsd-hooks, advisory-hooks, context-monitor, prompt-guard, workflow-guard]
long_tails:
  - "How to create advisory hooks for Claude Code without blocking execution"
  - "What is the timeout guard pattern for hooks on Windows"
axioms:
  - "NEVER block agent execution — hooks are advisory"
  - "ALWAYS include timeout guard (3-10s) against hang"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/claude-code/hooks"
related:
  - p12_wf_advisory_hooks
  - p01_kc_memory_lifecycle_hooks
  - p03_sp_hook_builder
  - bld_knowledge_card_hook
  - p10_ax_lifecycle_hooks
  - bld_tools_hook
  - bld_collaboration_hook
  - bld_architecture_hook
  - p01_kc_hook_config
  - bld_instruction_hook
---

## TL;DR

GSD implements 5 JavaScript hooks for Claude Code that enforce process via `additionalContext`.
Injected messages that the agent sees but never block execution.
Core pattern: stdin JSON, timeout guard (3-10s), process, stdout JSON or exit(0).

## Core Concept

Advisory hooks solve the enforcement vs autonomy dilemma: they guide the agent without interrupting flow. Each hook receives data via stdin JSON, processes with timeout guard (3-10s), and returns `additionalContext` or does a silent `process.exit(0)`. The 5 hooks cover: visual status (statusline), context alerts (context-monitor), workflow guard (workflow-guard), injection detection (prompt-guard) and version check (check-update).

Inter-hook communication uses bridge pattern via filesystem -- statusline writes metrics to tmpdir JSON, context-monitor reads that file to calculate thresholds. This decoupling allows hooks to operate independently: statusline runs in PreProcess, context-monitor in PostToolUse, each in its own lifecycle event without direct dependency.

Each hook is configurable via config file (opt-in/opt-out per hook). Workflow-guard is disabled by default -- only activates for those using GSD workflow. Prompt-guard and statusline are always active as they protect context integrity.

## Architecture/Patterns

| Hook | Event | Function | Config |
|------|--------|--------|--------|
| statusline | PreProcess | Bar: model, task, context% | Always |
| context-monitor | PostToolUse | Warning <=35%, critical <=25% | opt-out |
| workflow-guard | PreToolUse | Warns edits outside workflow | opt-in |
| prompt-guard | PreToolUse | Detects injection in planning | Always |
| check-update | SessionStart | Checks version in background | Always |

Context-monitor normalizes to usable context: Claude reserves 16.5% for autocompact.
Formula: `usable = (remaining - 16.5) / (100 - 16.5) * 100`.
Debounce: 5 tool uses between warnings; severity escalation (WARNING to CRITICAL) bypasses debounce.
Prompt-guard detects injection regex (ignore previous, pretend you are, invisible unicode) and warns without blocking -- false positive in blocking hook causes deadlock.

## Exemplos

```javascript
// Pattern universal dos hooks GSD — timeout + advisory
const timeout = setTimeout(() => process.exit(0), 3000);
let input = '';
process.stdin.on('data', c => input += c);
process.stdin.on('end', () => {
  clearTimeout(timeout);
  try {
    const data = JSON.parse(input);
    const msg = processHook(data);
    if (msg) {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: { additionalContext: msg }
      }));
    }
  } catch (e) { process.exit(0); }
});
```

Inter-hook communication flow via bridge file:
- SessionStart: check-update escreve cache/update-check.json (detached, unref)
- PreProcess: statusline escreve /tmp/claude-ctx-{id}.json com used_pct
- PostToolUse: context-monitor le /tmp/claude-ctx-{id}.json e injeta warning

## Anti-Patterns

- Hook that blocks with exit(1) -- causes deadlock in agent
- Logging hook errors to user -- noise without possible action
- Omitting timeout guard -- freezes terminal on Windows indefinitely
- Hardcoded thresholds without config -- prevents project customization
- Prompt guard blocking instead of advisory -- false positive freezes everything
- Bridge file without session_id -- collision between parallel sessions

## References

- source: https://docs.anthropic.com/en/docs/claude-code/hooks
- source: https://www.npmjs.com/package/get-shit-done-cc
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_advisory_hooks]] | downstream | 0.57 |
| [[p01_kc_memory_lifecycle_hooks]] | sibling | 0.26 |
| [[p03_sp_hook_builder]] | downstream | 0.26 |
| [[bld_knowledge_card_hook]] | sibling | 0.26 |
| [[p10_ax_lifecycle_hooks]] | downstream | 0.24 |
| [[bld_tools_hook]] | downstream | 0.23 |
| [[bld_collaboration_hook]] | downstream | 0.22 |
| [[bld_architecture_hook]] | downstream | 0.21 |
| [[p01_kc_hook_config]] | sibling | 0.21 |
| [[bld_instruction_hook]] | downstream | 0.21 |
