---
kind: collaboration
id: bld_collaboration_daemon
pillar: P12
llm_function: COLLABORATE
purpose: How daemon-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: daemon-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what runs persistently in the background, how does it restart, and how do we monitor it?"
I do not define event hooks. I do not build CLI tools.
I specify persistent background processes so long-running services operate reliably.
## Crew Compositions
### Crew: "Background Service Stack"
```
  1. daemon-builder -> "persistent process with restart policy and health checks"
  2. hook-builder -> "event hooks triggered by daemon state changes"
  3. env-config-builder -> "environment variables for daemon configuration"
```
### Crew: "Monitoring Infrastructure"
```
  1. daemon-builder -> "background process definition"
  2. benchmark-builder -> "performance baselines for the daemon"
  3. bugloop-builder -> "auto-correction when daemon degrades"
```
## Handoff Protocol
### I Receive
- seeds: process name, schedule type (continuous, cron, interval), restart policy
- optional: signal handling config, resource limits, PID management, log rotation
### I Produce
- daemon artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_daemon_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Daemons can be defined standalone.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| connector-builder | Connectors may run as persistent daemon processes |
| bugloop-builder | Correction loops may be hosted by daemons |
| hook-builder | Hooks may trigger on daemon lifecycle events |
