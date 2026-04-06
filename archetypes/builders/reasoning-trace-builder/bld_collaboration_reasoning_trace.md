---
kind: collaboration
id: bld_collaboration_reasoning_trace
pillar: P02
llm_function: COLLABORATE
purpose: How reasoning-trace-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: reasoning-trace-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "why did the agent choose this path, what evidence supported it, and what alternatives were rejected?"
I produce structured YAML traces for agent decision chains: step-evidence-confidence triplets, rejected alternatives, and confidence-scored conclusions. I do NOT carry execution instructions (instruction-builder), define agent identity (system-prompt-builder), or model workflow steps (workflow-primitive-builder).
## Crew Compositions
### Crew: "Reasoned Build Pipeline"
```
  1. instruction-builder       -> "defines WHAT the agent should do and in what phases"
  2. reasoning-trace-builder   -> "records WHY the agent chose specific approaches during F4 REASON"
  3. quality-gate-builder      -> "validates the reasoning trace for completeness and confidence calibration"
```
### Crew: "Decision Audit System"
```
  1. reasoning-trace-builder   -> "captures the complete decision chain with evidence and alternatives"
  2. memory-builder            -> "persists low-confidence traces as learning records for future improvement"
  3. feedback-loop-builder     -> "routes trace insights back into agent behavior calibration"
```
### Crew: "Agent Development Lifecycle"
```
  1. system-prompt-builder     -> "defines WHO the agent is — identity, rules, boundaries"
  2. instruction-builder       -> "defines WHAT the agent does — phases, inputs, outputs"
  3. reasoning-trace-builder   -> "records WHY the agent decided things — audit trail for iteration"
  4. quality-gate-builder      -> "validates the quality of both output and reasoning process"
```
## Handoff Protocol
### I Receive
- seeds: agent identifier, decision intent/question, available evidence (metrics, data, prior results)
- optional: timing data (duration_ms), list of alternatives considered, context from prior traces
### I Produce
- reasoning_trace artifact (YAML, fields: agent, intent, steps, conclusion, alternatives_rejected, confidence, max 8192 bytes)
- committed to: `cex/P03_prompt/compiled/p03_rt_{agent}_{timestamp}.yaml`
### I Signal
- signal: complete (with confidence score from trace)
- if overall confidence < 0.5: signal feedback_needed with low-confidence steps
## Builders I Depend On
- instruction-builder: provides the instruction context that triggered the decision being traced
- system-prompt-builder: provides agent identity context for understanding decision perspective
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| memory-builder             | persists low-confidence traces as learning records |
| quality-gate-builder       | validates trace completeness and confidence calibration |
| feedback-loop-builder      | routes trace insights into agent behavior improvement |
| agent-builder              | references traces to understand agent decision patterns |
| session-state-builder      | includes trace references in session checkpoint data |
