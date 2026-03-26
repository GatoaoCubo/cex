---
lp: P12
llm_function: COLLABORATE
purpose: How quality-gate-builder works in crews
---

# Collaboration: quality-gate-builder

## My Role
I define WHAT must pass. I do not implement HOW (validator-builder [PLANNED]).
I do not define evaluation DIMENSIONS (scoring-rubric-builder [PLANNED]).

## Crew: "Add Quality to New Type"
```
  1. quality-gate-builder   -> defines HARD/SOFT gates
  2. validator-builder [PLANNED] -> implements in Python
  3. scoring-rubric-builder [PLANNED] -> defines criteria
```

## Crew: "Archetype Builder Quality"
Every type-builder's QUALITY_GATES.md is produced by me.

## Handoff Protocol
### I Receive
- domain: what type of artifact
- severity: how strict (production vs experimental)

### I Produce
- quality_gate artifact in P11_feedback/examples/

## Builders I Depend On
None. Independent.

## Builders That Depend On Me [PLANNED]
| Builder | Why |
|---------|-----|
| validator-builder | Needs gate definitions |
| Every type-builder | Each QUALITY_GATES.md is my product |
