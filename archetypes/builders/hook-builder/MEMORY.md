---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: hook-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p04_hook_my_hook not p04_hook_my-hook)
3. trigger_event not in enum (must be exact: post_tool_use not post-tool-use)
4. timeout exceeding 30000ms (hard limit for system safety)
5. blocking: true with timeout > 10000ms (blocking hooks must be fast)
6. Confusing hook (P04, event interception) with lifecycle_rule (P11, policy)
7. Including business logic ("calculate price") — hooks intercept, not implement
8. Missing script_path — a hook without a script cannot execute
9. No error_handling declared — hooks fail and must not crash the host
10. Attempting to modify core state from hook — hooks observe and augment only

### Effective Hook Patterns
| Event | Pattern | Blocking | Typical Timeout |
|-------|---------|----------|-----------------|
| post_tool_use | metrics logging | false | 5000 |
| session_start | context injection | true | 3000 |
| user_prompt_submit | input routing hint | true | 2000 |
| stop | signal emission | false | 5000 |
| pre_tool_use | permission guard | true | 1000 |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | blocking vs async decision, timeout selection, event enum confusion |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a hook artifact, update:
- New common mistake (if encountered)
- New hook pattern (if discovered)
- Production counter increment
