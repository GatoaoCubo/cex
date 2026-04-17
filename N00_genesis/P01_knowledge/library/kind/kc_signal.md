---
id: p01_kc_signal
kind: knowledge_card
type: kind
pillar: P12
title: "Signal — Deep Knowledge for signal"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: signal
quality: 9.1
tags: [signal, P12, COLLABORATE, kind-kc]
tldr: "Lightweight inter-agent event notification (complete/error/progress) enabling asynchronous coordination without polling"
when_to_use: "Building, reviewing, or reasoning about signal artifacts"
keywords: [event, notification, async]
feeds_kinds: [signal]
density_score: null
---

# Signal

## Spec
```yaml
kind: signal
pillar: P12
llm_function: COLLABORATE
max_bytes: 4096
naming: p12_sig_{{event}}.json
core: true
```

## What It Is
A signal is a lightweight JSON event file written by one agent and read by another (or orchestrator) to communicate task completion, error, or progress without synchronous coupling. It carries event type, source agent, score, and optional payload. It is NOT handoff (P12 — complete instruction set with tasks, context, scope; signal is a simple event notification) nor interface (P06 — schema contract defining API structure; signal is a runtime event, not a contract).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableLambda` callback / LangSmith trace event | Post-run callback as completion notification |
| LlamaIndex | `Workflow` event system (`emit`, `@step` events) | Native event-driven coordination between workflow steps |
| CrewAI | Task completion callback / `CrewStreamingOutput` | Task outputs emit completion events; streaming for progress |
| DSPy | N/A — custom callback hooks | No native event system; implement via Python callbacks |
| Haystack | `@component` output propagation | Component output triggers next component execution |
| OpenAI | Streaming events (delta, done) / webhook | SSE stream emits delta events; webhook for async completion |
| Anthropic | `stream` event types (content_block_delta, message_stop) | Native SSE streaming with typed events |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| event_type | enum | required | complete/error/progress/blocked — precise typing enables routing |
| source | string | required | Emitting agent/agent_group name |
| score | float | null | Optional quality score; required for complete events going to pool |
| payload | map | {} | Minimal supplementary data; avoid large payloads in signal |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Complete + score | Task finished, orchestrator monitors | `{event: complete, source: shaka, score: 9.0, ts: ...}` |
| Error + context | Failure with recovery hint | `{event: error, source: atlas, error: "railway timeout", retry: true}` |
| Progress heartbeat | Long-running tasks > 10 min | `{event: progress, source: edison, step: 3, total: 8}` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Storing task output in signal | Signal grows large; defeats lightweight design | Store outputs in files; signal carries only path reference |
| Polling for signal (busy wait) | CPU waste; locks up terminal | Use `find .claude/signals -newer timestamp` or inotify |
| Signal without timestamp | Cannot determine signal age or ordering | Always include `ts: ISO8601` field |

## Integration Graph
```
[workflow] --> [signal] --> [orchestrator / orchestrator]
[bugloop] ------^      |
                  [dispatch_rule]
                  [checkpoint]
```

## Decision Tree
- IF task completes successfully THEN emit `event: complete` with score
- IF task fails after max_retries THEN emit `event: error` with retry hint
- IF task >10 min runtime THEN emit `event: progress` every 5 steps
- DEFAULT: Always emit complete or error; never finish silently

## Quality Criteria
- GOOD: Has event_type, source, ts (ISO8601), score (for complete); valid JSON; under 4096 bytes
- GREAT: Progress heartbeats for long tasks; error includes retry hint; payload is minimal reference only
- FAIL: No timestamp; payload stores full task output; complete event missing score; never emitted
