---
pillar: P12
llm_function: COLLABORATE
purpose: How runtime-state-builder works in crews
---

# Collaboration: runtime-state-builder

## My Role
I define WHAT routing rules, priorities, and heuristics an agent uses at RUNTIME.
I do not define design-time identity (mental-model-builder).
I do not manage search indexes (brain-index-builder).

## Crew: "Full Agent Definition"
```
  1. mental-model-builder      -> defines design-time identity (P02)
  2. runtime-state-builder     -> defines runtime decisions (P10)
  3. session-state-builder     -> defines ephemeral snapshot format (P10)
```

## Crew: "Agent Memory Stack"
```
  1. runtime-state-builder     -> defines live state
  2. learning-record-builder   -> defines what gets remembered
  3. brain-index-builder       -> defines how knowledge is searched
```

## Handoff Protocol
### I Receive
- seeds: agent name, domain, routing hints, priority list
- optional: mental_model (P02), existing learning_records, domain constraints

### I Produce
- runtime_state artifact in P10_memory/examples/
- committed to: cex/P10_memory/examples/p10_rs_{agent_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
| Builder | Why |
|---------|-----|
| mental-model-builder | Runtime state initializes from design-time mental model |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| session-state-builder | Session state snapshots runtime state |
| brain-index-builder | Brain index may use runtime state for search context |
