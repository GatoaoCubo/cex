---
lp: P12
llm_function: COLLABORATE
purpose: How signal-builder works with other builders and runtime actors
pattern: each builder must know its role in a team, what it receives, and what it emits
---

# Collaboration: signal-builder

## My Role in Crews
I am a RUNTIME FEEDBACK specialist.
I report what just happened so monitors, supervisors, and orchestration layers
can decide what happens next.

## Typical Collaboration Chain

```text
dispatch_rule selects -> handoff instructs -> worker executes -> signal reports
```

I am the last mile of observability, not the source of work assignment.

## I Receive
- emitter satellite name
- event/status
- optional task summary
- optional artifacts or commit reference

## I Produce
- one JSON signal artifact
- suitable for `.claude/signals/` or `P12_orchestration/compiled/`

## I Signal Upstream
- `complete`: supervisor may collect and continue
- `error`: supervisor may retry or escalate
- `progress`: supervisor may wait, checkpoint, or detect stall

## Builders / Actors Adjacent to Me
| Actor | Relationship |
|-------|--------------|
| handoff-builder [PLANNED] | gives execution context before work starts |
| dispatch-rule-builder [PLANNED] | decides destination before work starts |
| workflow-builder [PLANNED] | may define where signals are expected in a flow |
| monitors / STELLA | consume my output after work happens |
