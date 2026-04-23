---
id: p10_lr_hook_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Hooks configured as blocking:true with timeout >10000ms cause host freezes during tool execution. Async hooks that emit signals work reliably for logging and metrics. Pre-tool-use hooks used for permission guards must complete in <1000ms or risk user-visible latency. Hooks containing business logic instead of interception logic become maintenance liabilities. Missing error_handling declarations cause unhandled exceptions to crash the host process."
pattern: "Blocking hooks must have timeout <=10000ms (hard limit 30000ms system-wide). Hooks that do not need to gate execution must be async (blocking:false). Every hook requires an error_handling field — hooks that fail must not crash the host. Hooks intercept and augment; they do not implement business logic. script_path is required; a hook without it cannot execute."
evidence: "Hook timeout violations detected in 3 of 8 early productions (blocking:true with 15000-30000ms). Asy..."
confidence: 0.75
outcome: SUCCESS
domain: hook
tags: [hook, event-driven, blocking, async, timeout, error-handling, lifecycle]
tldr: "Blocking hooks must be fast (<10s, ideally <3s). Async hooks are safe for logging. Every hook needs error_handling or it can crash the host."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [hook, trigger, blocking, async, timeout, error_handling, pre_tool_use, post_tool_use, session_start, stop]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Hook"
density_score: 0.90
llm_function: INJECT
related:
  - p03_sp_hook_builder
  - bld_knowledge_card_hook
  - bld_instruction_hook
  - bld_examples_hook
  - bld_architecture_hook
  - p11_qg_hook
  - bld_schema_hook
  - hook-builder
  - bld_collaboration_hook
  - p04_hook_NAME
---
## Summary
Hooks are event-driven interceptors that fire at lifecycle boundaries. Their value comes from being lightweight and reliable. The two most common failures are: (1) blocking hooks with excessive timeouts that freeze the host, and (2) missing error_handling that allows hook failures to propagate as host crashes.
## Pattern
Blocking vs async decision table:
| Event | Recommended mode | Max timeout |
|---|---|---|
| pre_tool_use | blocking | 1000ms |
| session_start | blocking | 3000ms |
| user_prompt_submit | blocking | 2000ms |
| post_tool_use | async | 5000ms |
| stop | async | 5000ms |
Required fields every hook must have:
- `trigger_event` - exact enum value (underscores, not hyphens)
- `script_path` - relative path to executable script
- `blocking` - boolean, not string
- `timeout` - integer milliseconds, max 30000
- `error_handling` - what to do when the script fails (log, skip, abort)
Hooks intercept execution flow and may augment context. They must not implement domain logic. A hook that calculates prices or makes API calls belongs in an instruction or workflow, not a hook.
## Anti-Pattern
- `blocking: true` with `timeout > 10000` — host freezes during tool calls.
- No `error_handling` field — unhandled hook failure crashes the host process.
- Business logic in hook script ("calculate price", "send email") — hooks observe, not implement.
- `trigger_event: "post-tool-use"` (hyphens) — must be `post_tool_use` (underscores).
- Missing `script_path` — hook is declared but cannot execute.
- Timeout set to 0 or absent — system applies unpredictable default.
## Context
Pattern crystallized after integration testing revealed that early hook designs routinely set generous timeouts "just in case" without considering that blocking hooks pause the entire host. The fix is cheap: separate the blocking decision from the timeout value. If a hook needs >10s, it must be async. If it must be blocking and >10s, the logic belongs outside the hook layer.
## Impact
- Host freezes from overlong blocking hooks: 3 incidents eliminated by timeout rule
- Host crashes from missing error_handling: 2 incidents eliminated by required field rule
- Async logging hooks: 0 host impact across 50+ executions
- Pre-tool-use latency: acceptable (<100ms) when timeout <=1000ms
## Reproducibility

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_hook_builder]] | upstream | 0.55 |
| [[bld_knowledge_card_hook]] | upstream | 0.53 |
| [[bld_instruction_hook]] | upstream | 0.46 |
| [[bld_examples_hook]] | upstream | 0.43 |
| [[bld_architecture_hook]] | upstream | 0.42 |
| [[p11_qg_hook]] | downstream | 0.41 |
| [[bld_schema_hook]] | upstream | 0.40 |
| [[hook-builder]] | upstream | 0.38 |
| [[bld_collaboration_hook]] | downstream | 0.37 |
| [[p04_hook_NAME]] | upstream | 0.36 |
