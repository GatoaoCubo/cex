---
kind: knowledge_card
id: bld_knowledge_card_hook
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for hook production — event interception specification
sources: Git hooks, Claude Code hooks, Kubernetes admission webhooks, React lifecycle
quality: 9.1
title: "Knowledge Card Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_hook
  - bld_collaboration_hook
  - p03_sp_hook_builder
  - bld_architecture_hook
  - bld_knowledge_card_hook_config
  - p10_lr_hook_builder
  - hook-builder
  - p11_qg_hook
  - bld_examples_hook_config
  - p01_kc_hook_config
---

# Domain Knowledge: hook
## Executive Summary
Hooks are event interception points that execute code before or after system events (tool use, session lifecycle, prompt submission, stop). They provide extensibility without modifying core behavior — observing events and executing side effects like logging, validation, metrics, or context injection. Hooks differ from daemons (persistent processes), lifecycle rules (declarative policies), and signals (status notifications).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| Frontmatter fields | 16 required |
| Quality gates | 9 HARD + 10 SOFT |
| Execution timing | pre, post, both |
| Blocking behavior | blocking (waits) or async (fire-and-forget) |
| Error handling | log (safest), fail, retry |
| Timeout | Mandatory; <= 10s for blocking hooks |
## Patterns
- **Single responsibility**: one hook = one event = one action — no multi-event hooks
- **Blocking vs async**: blocking hooks must be fast (<=10s); use async for heavy work (logging, metrics)
| Source | Concept | Application |
|--------|---------|-------------|
| Git hooks | pre-commit, post-merge scripts | trigger_event + script_path |
| Claude Code | PreToolUse, PostToolUse, SessionStart, Stop | trigger_event enum |
| Kubernetes | Validating/Mutating admission webhooks | blocking hooks with timeout |
| React | componentDidMount, useEffect | pre/post execution timing |
- **Event types in agent systems**:
| Event | Timing | Common use |
|-------|--------|-----------|
| SessionStart | pre | Context injection, environment setup |
| PreToolUse | pre (blocking) | Validation, permission check |
| PostToolUse | post | Logging, metrics, audit trail |
| UserPromptSubmit | pre | Input validation, routing hints |
| Stop | post | Cleanup, signal writing, summary |
- **Condition gating**: not every event instance triggers the hook — conditions filter by event properties
- **Environment injection**: pass context via env vars, not script arguments — more portable
- **Idempotency**: hooks may fire multiple times for same event (retries); design for repeat safety
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Blocking hook > 10s | System hangs; user experience degrades |
| No timeout declared | Hook can hang indefinitely |
| Multi-event hook | Violates single responsibility; hard to debug |
| Error handling not declared | Undefined behavior on failure |
| State mutation in hook | Hooks observe and augment; never modify core state |
| No conditions (fires on everything) | Performance waste; irrelevant executions |
## Application
1. Identify event: which system event triggers this hook?
2. Choose timing: pre (before event), post (after), or both
3. Set blocking: blocking (waits for result) or async (fire-and-forget)
4. Define conditions: when should this hook actually fire?
5. Configure timeout: mandatory; <= 10s for blocking
6. Set error handling: log (safest), fail, or retry
## References
- Git: hooks documentation (git-scm.com/docs/githooks)
- Claude Code: hook system (PreToolUse, PostToolUse, etc.)
- Kubernetes: admission webhook configuration
- Webpack: compiler hooks and plugin tap pattern

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_hook]] | downstream | 0.59 |
| [[bld_collaboration_hook]] | downstream | 0.56 |
| [[p03_sp_hook_builder]] | downstream | 0.55 |
| [[bld_architecture_hook]] | downstream | 0.49 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.48 |
| [[p10_lr_hook_builder]] | downstream | 0.48 |
| [[hook-builder]] | downstream | 0.47 |
| [[p11_qg_hook]] | downstream | 0.45 |
| [[bld_examples_hook_config]] | downstream | 0.44 |
| [[p01_kc_hook_config]] | sibling | 0.43 |
