---
kind: collaboration
id: bld_collaboration_workflow_primitive
pillar: P02
llm_function: COLLABORATE
purpose: How workflow-primitive-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: workflow-primitive-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is this single workflow operation, what does it consume, and what does it produce?"
I produce YAML atomic blocks for orchestration composition: step, condition, loop, parallel, router, gate, and merge primitives with typed I/O contracts. I do NOT produce full workflow graphs (workflow-builder), DAG edge definitions (dag-builder), inter-agent signals (signal-builder), or task instructions (handoff-builder).
## Crew Compositions
### Crew: "Workflow Assembly Pipeline"
```
  1. workflow-primitive-builder -> "defines each atomic building block with typed I/O"
  2. workflow-builder           -> "composes primitives into a full multi-step workflow graph"
  3. quality-gate-builder       -> "validates composition rules: parallel-merge pairing, loop guards"
```
### Crew: "Mission Execution System"
```
  1. workflow-primitive-builder -> "defines step, parallel, gate, and merge primitives for waves"
  2. dag-builder                -> "defines dependency edges between composed primitives"
  3. signal-builder             -> "emits completion signals that feed into gate thresholds"
  4. handoff-builder            -> "creates task instructions for agents executing each step"
```
### Crew: "Research-Then-Build Pattern"
```
  1. workflow-primitive-builder -> "defines the research step primitive (inputs: query, outputs: findings)"
  2. workflow-primitive-builder -> "defines the gate primitive (threshold: research quality >= 8.0)"
  3. workflow-primitive-builder -> "defines the build step primitive (inputs: findings, outputs: artifact)"
  4. workflow-builder           -> "composes the three primitives into a research-then-build workflow"
```
## Handoff Protocol
### I Receive
- seeds: primitive type, input/output field definitions, guard clause values
- optional: composition context (what precedes/follows), branch references, naming
### I Produce
- workflow_primitive artifact (YAML, fields: type, inputs, outputs, guards, max 4096 bytes)
- committed to: `cex/P12_orchestration/compiled/p12_wp_{type}.yaml`
### I Signal
- signal: complete (with primitive type and I/O field count)
- if composition rules violated (e.g. parallel without merge_ref): signal error with violation details
## Builders I Depend On
- signal-builder: signals feed into gate primitives as threshold inputs
- handoff-builder: handoffs provide task context for step primitives
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder            | composes primitives into full workflow graphs |
| dag-builder                 | defines edges between primitives in a DAG |
| mission-runner              | executes primitives in wave order |
| coordinator                 | manages synthesis gates between workflow waves |
| quality-gate-builder        | validates primitive composition rules |
