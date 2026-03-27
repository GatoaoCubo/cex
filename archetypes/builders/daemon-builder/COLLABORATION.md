---
pillar: P12
llm_function: COLLABORATE
purpose: How daemon-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: daemon-builder

## My Role in Crews
I am a BACKGROUND PROCESS SPECIALIST. I answer ONE question: "what runs persistently
in the background, how does it restart, and how do we monitor it?"
I do not define agent identity. I do not write skill phases. I do not implement code.
I DEFINE PROCESS LIFECYCLE SPECS so operators know exactly how the daemon behaves.

## Crew Compositions

### Crew: "Background Infrastructure"
```
  1. env-config-builder      -> "environment variables the daemon needs"
  2. daemon-builder           -> "daemon spec: schedule, restart, signals, monitoring"
  3. signal-builder [EXISTS]  -> "signals emitted by daemon (heartbeat, complete, error)"
  4. quality-gate-builder     -> "quality gate for daemon health metrics"
```

### Crew: "Persistent Integration"
```
  1. connector-builder       -> "bidirectional service integration spec"
  2. daemon-builder           -> "daemon that runs connector sync loop in background"
  3. knowledge-card-builder  -> "capture integration patterns as knowledge"
```

### Crew: "Scheduled Pipeline"
```
  1. client-builder          -> "API client for data fetching"
  2. daemon-builder           -> "daemon that runs client on cron schedule"
  3. workflow-builder         -> "workflow that orchestrates daemon outputs"
```

## Handoff Protocol

### I Receive
- seeds: task name, schedule type, why background (not one-shot)
- optional: resource limits, restart requirements, monitoring stack
- optional: upstream connector/client to wrap

### I Produce
- daemon artifact: `p04_daemon_{name_slug}.md` + `.yaml`
- committed to: `cex/P04_tools/examples/p04_daemon_{name_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- env-config-builder: provides environment variables daemon needs at runtime
- connector-builder: if daemon wraps a connector sync loop
- client-builder: if daemon wraps API polling via client

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| signal-builder [EXISTS] | Signals emitted by daemon need signal spec |
| workflow-builder | Workflows may depend on daemon being alive |
| quality-gate-builder | Quality gates may check daemon health metrics |
| knowledge-card-builder | Capture daemon operational patterns |
