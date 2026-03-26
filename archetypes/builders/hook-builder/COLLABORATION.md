---
pillar: P12
llm_function: COLLABORATE
purpose: How hook-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: hook-builder

## My Role in Crews
I am an INTERCEPTOR. I answer ONE question: "what should happen before or after this event?"
I do not define policies. I do not run persistently.
I INTERCEPT so event-driven side effects execute reliably.

## Crew Compositions

### Crew: "Observability Pipeline"
```
  1. hook-builder                  -> "intercept tool/session events for metrics"
  2. signal-builder                -> "emit signals from hook results"
  3. quality-gate-builder          -> "validate metric thresholds"
```

### Crew: "Session Lifecycle"
```
  1. spawn-config-builder          -> "define session boot parameters"
  2. hook-builder                  -> "inject context at session_start, persist at session_end"
  3. lifecycle-rule-builder        -> "declare retention/archive policies"
```

### Crew: "Permission Guard"
```
  1. hook-builder                  -> "intercept permission_request for auto-approve/deny"
  2. guardrail-builder             -> "define security boundaries"
  3. validator-builder [PLANNED]   -> "validate request against rules"
```

## Handoff Protocol

### I Receive
- seeds: trigger_event, domain, script_path
- optional: conditions (event filters)
- optional: environment variables list

### I Produce
- hook artifact: `cex/P04_tools/examples/p04_hook_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
None (hook-builder is independent — defines event interceptions from domain knowledge).

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| signal-builder | May emit signals based on hook execution results |
| lifecycle-rule-builder | May reference hooks as enforcement mechanisms |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
signal-builder references hook as potential signal emitter.
lifecycle-rule-builder may reference hook as enforcement tool.
