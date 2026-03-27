---
pillar: P12
llm_function: COLLABORATE
purpose: How session-state-builder works with other builders and runtime actors
pattern: each builder must know its role in a team, what it receives, and what it emits
---

# Collaboration: session-state-builder

## My Role in Crews
I am an EPHEMERAL STATE CAPTURE specialist.
I record what is happening right now in a session so monitors, recovery tools,
and post-session analysis can reference the snapshot.

## Typical Collaboration Chain

```text
agent boot -> execution -> session_state capture -> session end -> learning_record extraction
```

I sit during active execution, providing observability into agent sessions.

## I Receive
- agent or satellite identity
- session start time and current status
- optional runtime metrics: tasks, tokens, tools, errors

## I Produce
- one YAML session_state snapshot
- suitable for `P10_memory/compiled/` or monitoring tools

## I Inform Downstream
- `learning_record`: post-session analysis extracts patterns from my snapshots
- `runtime_state`: persistent state may update based on session outcomes
- `signal` (P12): status events may reference session data from my snapshots

## Builders / Actors Adjacent to Me
| Actor | Relationship |
|-------|--------------|
| runtime-state-builder | produces persistent state; I produce ephemeral snapshots |
| learning-record-builder | accumulates patterns; may extract from my snapshots |
| brain-index-builder | indexes artifacts; independent of my session capture |
| signal-builder | reports events; may reference session data from my snapshots |
| monitors / STELLA | consume my output for real-time observability |

## Cross-Reference Obligations (per BUILDER_NORM 12)
- signal-builder references session data -> signal-builder MUST ref session-state-builder
- learning-record-builder extracts from session snapshots -> learning-record-builder MUST ref session-state-builder
