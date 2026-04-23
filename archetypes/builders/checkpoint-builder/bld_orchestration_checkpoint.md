---
kind: collaboration
id: bld_collaboration_checkpoint
pillar: P12
llm_function: COLLABORATE
purpose: How checkpoint-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_checkpoint_builder
  - checkpoint-builder
  - bld_architecture_checkpoint
  - bld_collaboration_workflow
  - bld_knowledge_card_checkpoint
  - p01_kc_checkpoint
  - bld_instruction_checkpoint
  - bld_collaboration_session_state
  - p11_qg_checkpoint
  - bld_schema_checkpoint
---

# Collaboration: checkpoint-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what state does this checkpoint capture, and how does a workflow resume from here?"
I do not define signals (stateless events). I do not define the workflow graph itself.
I produce checkpoint artifacts that bind saved state to a specific workflow step, enabling resume, rollback, and audit.
## Crew Compositions
### Crew: "Resumable Workflow"
```
  1. workflow-builder      -> "workflow definition (steps, graph, inputs/outputs)"
  2. checkpoint-builder    -> "checkpoint artifacts at key steps (state schema, TTL, resume protocol)"
  3. signal-builder        -> "completion and failure signals emitted after each step"
```
### Crew: "Fault-Tolerant Pipeline"
```
  1. workflow-builder      -> "pipeline DAG with retry policy"
  2. checkpoint-builder    -> "checkpoints at expensive or slow steps"
  3. guardrail-builder     -> "state size caps and TTL enforcement rules"
  4. notifier-builder      -> "alerts on checkpoint failure or TTL expiry"
```
### Crew: "Human-in-the-Loop Workflow"
```
  1. workflow-builder      -> "workflow with interrupt_before/interrupt_after steps"
  2. checkpoint-builder    -> "checkpoints at human review steps (resumable: true)"
  3. session-state-builder -> "ephemeral UI session state during human review window"
```
## Handoff Protocol
### I Receive
- seeds: workflow_ref, step name, state keys needed for resume
- optional: parent_checkpoint id, TTL requirement, retry policy, error context
### I Produce
- checkpoint artifact (.md with yaml frontmatter)
- committed to: `cex/P12_orchestration/examples/p12_ckpt_{workflow}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| Builder | Why |
|---------|-----|
| workflow-builder | workflow_ref must reference a valid workflow artifact; step must match workflow step names |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| signal-builder | Signals may reference checkpoint id as the state context for a workflow event |
| guardrail-builder | Guardrails enforce checkpoint state size caps and TTL compliance |
| notifier-builder | Notifiers may trigger on checkpoint TTL expiry or resume failure events |
| instruction-builder | Recipes reference checkpoint creation and resume as named steps in workflow instructions |
## Boundary Contracts
| I am NOT | Redirect to |
|----------|-------------|
| A signal (stateless event) | signal-builder |
| A session_state (ephemeral, no workflow_ref) | session-state-builder (P10) |
| A workflow definition or DAG | workflow-builder |
| A task result or output artifact | output artifact builder for the relevant domain |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_checkpoint_builder]] | upstream | 0.58 |
| [[checkpoint-builder]] | related | 0.55 |
| [[bld_architecture_checkpoint]] | upstream | 0.50 |
| [[bld_collaboration_workflow]] | sibling | 0.49 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.46 |
| [[p01_kc_checkpoint]] | related | 0.45 |
| [[bld_instruction_checkpoint]] | upstream | 0.45 |
| [[bld_collaboration_session_state]] | sibling | 0.44 |
| [[p11_qg_checkpoint]] | upstream | 0.43 |
| [[bld_schema_checkpoint]] | upstream | 0.40 |
