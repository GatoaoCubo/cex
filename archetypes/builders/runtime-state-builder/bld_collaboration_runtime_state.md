---
kind: collaboration
id: bld_collaboration_runtime_state
pillar: P10
llm_function: COLLABORATE
purpose: How runtime-state-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: runtime-state-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what routing rules, priorities, and heuristics does this agent use at runtime?"
I define variable mental state agents accumulate during sessions — decision trees, tool preferences, priority ordering. I do not define design-time identity or ephemeral session snapshots.
## Crew Compositions
### Crew: "Full Agent Definition Pack"
```
  1. agent-builder            -> "static identity: name, domain, capabilities"
  2. mental-model-builder     -> "design-time knowledge map and domain constraints"
  3. runtime-state-builder    -> "runtime routing rules, priorities, and heuristics"
  4. session-state-builder    -> "ephemeral snapshot of in-flight session variables"
```
### Crew: "Adaptive Routing Agent"
```
  1. router-builder           -> "static route table for task dispatch"
  2. runtime-state-builder    -> "dynamic heuristics that adjust routing at runtime"
  3. learning-record-builder  -> "patterns captured from routing decisions for future sessions"
```
### Crew: "Stateful Agent Bootstrap"
```
  1. boot-config-builder      -> "initialization sequence and startup parameters"
  2. runtime-state-builder    -> "initial state: priorities, tool preferences, decision trees"
  3. runtime-rule-builder     -> "operational limits applied to the booted agent"
```
## Handoff Protocol
### I Receive
- seeds: agent domain, routing heuristics, priority ordering, tool preferences, decision criteria
- optional: mental model to seed from, observed routing patterns, cross-session persistence requirements
### I Produce
- runtime_state artifact (YAML frontmatter + priorities list + heuristics + decision trees + tool preferences, max 4096 bytes)
- committed to: `cex/P10/examples/p10_rs_{agent}_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- mental-model-builder: provides design-time domain map that seeds my runtime routing heuristics
- agent-builder: provides agent identity context that scopes which heuristics are relevant
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| session-state-builder | Initializes ephemeral session variables using my persistent state as baseline |
| learning-record-builder | Records state transitions and heuristic updates discovered at runtime |
| router-builder | References my heuristics to augment static route tables with dynamic priority weights |
| boot-config-builder | Loads my state as the initial agent configuration at boot time |
