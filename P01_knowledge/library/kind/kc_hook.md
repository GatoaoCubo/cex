---
id: p01_kc_hook
kind: knowledge_card
type: kind
pillar: P01
title: "Hook — Deep Knowledge for hook"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: hook
quality: 9.1
tags: [hook, P04, GOVERN, kind-kc]
tldr: "Executable code triggered on a pre/post pipeline event — synchronous, short-lived, scoped to one event boundary, with side effects but no persistent state"
when_to_use: "Building, reviewing, or reasoning about hook artifacts"
keywords: [hook, pre-post, event, middleware, lifecycle]
feeds_kinds: [hook]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Hook

## Spec
```yaml
kind: hook
pillar: P04
llm_function: GOVERN
max_bytes: 1024
naming: p04_hook_{{name}}.md
core: true
```

## What It Is
A hook is executable code that fires on a well-defined pre/post pipeline event (e.g., PreToolUse, PostLLMCall, SessionStart). It runs synchronously in the calling context and exits after producing a side effect (log, block, modify). It is NOT a lifecycle_rule (P11, which is a declarative config rule) nor a daemon (which is a persistent background process that runs indefinitely between events).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | on_llm_start / on_tool_end callbacks | AsyncCallbackHandler; event-driven |
| LlamaIndex | QueryEventHandler, on_retrieve | Event hooks on pipeline steps |
| CrewAI | step_callback, task_callback | Per-step and per-task hook injection |
| DSPy | Teleprompter callbacks | Optimization-phase hooks |
| Haystack | Pipeline event hooks | ComponentBase lifecycle events |
| OpenAI | n/a (no native hook system) | Wrapper pattern required |
| Anthropic | Claude Code hooks (settings.json) | 10 events: PreToolUse, PostToolUse, etc. |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| trigger_event | str | required | Scoped to exactly 1 event type |
| timeout_ms | int | 5000 | Lower = safe; higher = feature-rich |
| on_error | str | log | skip / abort / retry |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Audit log hook | All tool calls | Append to audit.jsonl on PostToolUse |
| Guard hook | Before LLM call | Check token budget in PreLLMCall |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Blocking I/O in hook | Stalls pipeline on every event | Async write or fire-and-forget queue |
| Stateful hook via class vars | Race conditions in parallel calls | Pass context through event payload only |

## Integration Graph
```
[pipeline_event] --> [hook] --> [side_effect / modified_context]
                       |
                [trigger_event, script_path, timeout]
```

## Decision Tree
- IF rule is declarative config THEN use lifecycle_rule (P11)
- IF process must persist across events THEN use daemon
- IF hook needs to call multiple systems THEN decompose into separate hooks
- DEFAULT: hook for any single-event executable callback with side effects

## Quality Criteria
- GOOD: single trigger_event, idempotent, logs errors with context
- GREAT: async-safe, timeout guarded, structured output, tested in isolation
- FAIL: multiple trigger_events in one hook, blocking I/O, no error handling
