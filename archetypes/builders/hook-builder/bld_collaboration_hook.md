---
pillar: P12
llm_function: COLLABORATE
purpose: How hook-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: hook-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what should happen before or after this system event?"
I do not define background processes. I do not build plugins.
I design event interception points so systems can react to lifecycle events without modifying core flow.

## Crew Compositions

### Crew: "Event-Driven System"
```
  1. hook-builder -> "pre/post event hooks with trigger conditions"
  2. cli-tool-builder -> "scripts invoked by hooks"
  3. daemon-builder -> "persistent process that emits events"
```

### Crew: "Lifecycle Management"
```
  1. hook-builder -> "event hooks (session start, tool use, stop)"
  2. guardrail-builder -> "safety checks triggered by hooks"
  3. bugloop-builder -> "correction cycle triggered on hook failure"
```

## Handoff Protocol

### I Receive
- seeds: event type, trigger conditions, script path or inline command
- optional: blocking behavior, timeout, error strategy, environment injection

### I Produce
- hook artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_hook_{event}_{timing}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- cli-tool-builder: provides scripts that hooks invoke on trigger

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| daemon-builder | Daemons may trigger hooks on state changes |
| guardrail-builder | Safety checks can be enforced via pre-tool hooks |
| bugloop-builder | Detection triggers may be implemented as hooks |
