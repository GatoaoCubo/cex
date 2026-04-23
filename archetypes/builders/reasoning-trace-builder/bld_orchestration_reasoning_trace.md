---
kind: collaboration
id: bld_collaboration_reasoning_trace
pillar: P02
llm_function: COLLABORATE
purpose: How reasoning-trace-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - reasoning-trace-builder
  - p03_sp_reasoning_trace_builder
  - bld_collaboration_agent
  - p01_kc_reasoning_trace
  - bld_knowledge_card_reasoning_trace
  - bld_collaboration_system_prompt
  - bld_memory_reasoning_trace
  - p03_ins_reasoning_trace_builder
  - bld_config_reasoning_trace
  - bld_architecture_reasoning_trace
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[reasoning-trace-builder]] | downstream | 0.52 |
| [[p03_sp_reasoning_trace_builder]] | downstream | 0.49 |
| [[bld_collaboration_agent]] | sibling | 0.49 |
| [[p01_kc_reasoning_trace]] | downstream | 0.48 |
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.45 |
| [[bld_collaboration_system_prompt]] | sibling | 0.42 |
| [[bld_memory_reasoning_trace]] | downstream | 0.41 |
| [[p03_ins_reasoning_trace_builder]] | downstream | 0.41 |
| [[bld_config_reasoning_trace]] | downstream | 0.41 |
| [[bld_architecture_reasoning_trace]] | downstream | 0.39 |
