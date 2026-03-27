---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries recurring session patterns
---

# Memory: session-state-builder

## Recurrent Patterns
- Most useful session snapshots include `active_tasks` and `context_window_used`
- `checkpoints` are better than prose descriptions for recovery scenarios
- `errors` list should have both `code` and `message` for debugging
- Keep `tools_called` as unique list, use `tool_call_count` for total

## Common Mistakes
1. Using `runtime_state` kind instead of `session_state`
2. Including persistent routing decisions (belongs in runtime_state)
3. Accumulating scores across sessions (belongs in learning_record)
4. Forgetting `started_at` timestamp
5. Using `quality` instead of `quality: null` (never self-score)

## State Between Sessions
This builder is stateless per invocation.
After production, update only if a new recurring session field or consumer
constraint becomes stable across multiple snapshots.
