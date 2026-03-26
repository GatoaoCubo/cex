---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for hook production
sources: CEX taxonomy, event-driven architecture, hook patterns, lifecycle management
---

# Domain Knowledge: hook

## Foundational Concept
A hook is an event interception artifact that executes code before or after a system event.
In agent-powered systems, hooks provide extensibility without modifying core behavior — they
observe events (tool use, session lifecycle, prompt submission) and execute side effects
(logging, metrics, validation, context injection). The CEX hook (P04) defines trigger
configuration with conditions, timeout, blocking behavior, and error handling.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Git hooks | pre-commit, post-merge scripts | trigger_event + script_path pattern |
| Claude Code hooks | PreToolUse, PostToolUse, SessionStart, Stop | trigger_event enum values |
| Webpack plugins | compiler hooks (tap/call pattern) | blocking + async execution |
| React lifecycle | componentDidMount, useEffect | pre/post execution timing |
| Kubernetes admission | Validating/Mutating webhooks | blocking hooks with timeout |

## Key Patterns
- Single responsibility: one hook = one event = one action
- Blocking hooks must be fast: timeout <= 10s, minimize I/O
- Async hooks for heavy work: logging, metrics, notifications
- Conditions gate execution: not every event instance triggers the hook
- Fail-safe defaults: error_handling "log" is safest (does not block on failure)
- Environment injection: pass context via env vars, not script arguments
- Idempotency: hooks may fire multiple times for same event (retries)
- No state mutation: hooks observe and augment, never modify core state

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| conditions | CEX hooks support conditional execution per event properties | Git hook exit codes |
| timeout | CEX mandates explicit timeout to prevent system hangs | K8s webhook timeout |
| error_handling | CEX requires declared failure behavior | Git hook --no-verify bypass |
| execution (pre/post/both) | CEX hooks can fire on both sides of an event | Middleware pattern |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT hook |
|------|------------|-------------------|
| lifecycle_rule (P11) | Declarative policy (archive after 90 days) | DECLARES rules, does not EXECUTE code |
| daemon (P04) | Persistent background process | RUNS continuously, hook fires per-event |
| plugin (P04) | Full system extension with API surface | EXTENDS system broadly, hook intercepts one event |
| skill (P04) | Multi-phase reusable capability | Has PHASES and workflow, hook is single action |
| signal (P12) | Runtime event notification | REPORTS what happened, hook REACTS to events |

## References
- CEX TAXONOMY_LAYERS.yaml — hook in runtime layer
- CEX SEED_BANK.yaml — P04_hook seeds
- Claude Code hooks documentation
- Git hooks: git-scm.com/docs/githooks
