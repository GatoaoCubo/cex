---
kind: collaboration
id: bld_collaboration_signal
pillar: P12
llm_function: COLLABORATE
purpose: How signal-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: signal-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what happened, who emitted it, and when?"
I produce minimal JSON payloads for atomic inter-agent status events: complete, error, and progress. I do NOT carry full task instructions (handoff-builder), define routing policy (dispatch-rule-builder), or model workflows and DAGs.
## Crew Compositions
### Crew: "Task Completion Lifecycle"
```
  1. handoff-builder    -> "delivers full instructions and context to the executing agent"
  2. signal-builder     -> "emits atomic complete/error JSON when the agent finishes or fails"
  3. dispatch-rule-builder -> "reads the completion signal and routes next work to the correct agent"
```
### Crew: "Parallel Agent Coordination"
```
  1. dag-builder        -> "defines which agents run in parallel and their dependency edges"
  2. signal-builder     -> "produces the completion signals that unblock downstream DAG nodes"
  3. chain-builder      -> "consumes signals to advance the execution chain to the next step"
```
### Crew: "Progress Monitoring Pipeline"
```
  1. session-state-builder -> "captures current checkpoint and tokens_used from live execution"
  2. signal-builder        -> "wraps checkpoint data into a progress signal with percentage and ETA"
  3. runtime-state-builder -> "persists signal history for audit and retry decisions"
```
## Handoff Protocol
### I Receive
- seeds: emitter agent ID, signal type (complete/error/progress), quality score or error reason
- optional: payload extensions (percentage, eta, artifact path, retry count)
### I Produce
- signal artifact (JSON, fields: id, type, emitter, timestamp, payload, max 40 lines)
- committed to: `cex/P12/examples/signal-{type}-{emitter}-{timestamp}.json`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- session-state-builder: provides checkpoint and progress data used in progress signal payloads
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder   | reads completion signals to trigger next routing decision |
| chain-builder           | advances to next chain step only after receiving a complete signal |
| dag-builder             | uses signal semantics to define edge conditions between DAG nodes |
| fallback-chain-builder  | reads error signals to decide which fallback path to activate |
| runtime-state-builder   | persists signal history for audit trails and retry logic |
