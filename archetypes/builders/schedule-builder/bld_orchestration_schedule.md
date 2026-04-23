---
kind: collaboration
id: bld_collaboration_schedule
pillar: P12
llm_function: COLLABORATE
purpose: How schedule-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - schedule-builder
  - bld_collaboration_workflow
  - bld_collaboration_checkpoint
  - bld_collaboration_builder
  - bld_architecture_schedule
  - p03_sp_schedule_builder
  - workflow-builder
  - bld_architecture_kind
  - bld_collaboration_hook_config
  - bld_collaboration_hook
---

# Collaboration: schedule-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "when does this workflow run, at what cadence, in what timezone, with what overlap and catch-up policy?"
I do not define what the workflow does. I do not route keywords to workflows. I do not react to events as side effects.
I specify temporal triggers so orchestrators, agents, and runtime schedulers know exactly when to start a workflow.
## Crew Compositions
### Crew: "Scheduled Workflow System"
```
  1. workflow-builder    -> "workflow definition (steps, logic, outputs)"
  2. schedule-builder    -> "temporal trigger (when, timezone, policy)"
  3. guardrail-builder   -> "execution constraints (timeout, retry, resource caps)"
```
### Crew: "Orchestration Layer"
```
  1. schedule-builder    -> "when to start (cron, interval, event)"
  2. dispatch_rule-builder -> "which workflow handles a message (keyword routing)"
  3. monitor-builder     -> "observe fires, skips, failures, durations"
```
### Crew: "Data Pipeline"
```
  1. schedule-builder    -> "daily/hourly trigger for ETL workflow"
  2. workflow-builder    -> "ETL steps (extract, transform, load)"
  3. hook-builder        -> "post-load side effects (notify, invalidate cache)"
```
## Handoff Protocol
### I Receive
- seeds: workflow_ref id, desired cadence, business timezone, domain context
- optional: catch_up requirement, concurrency constraints, infrastructure sharing context
### I Produce
- schedule artifact (.md with YAML frontmatter)
- committed to: `cex/P12_orchestration/examples/p12_sched_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures listed
## Builders I Depend On
| Builder | Why |
|---------|-----|
| workflow-builder | workflow_ref must resolve to an existing workflow artifact |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| guardrail-builder | Guardrails apply timeout and resource caps to schedule-triggered runs |
| monitor-builder | Monitors subscribe to schedule fire events to track execution history |
| hook-builder | Hooks may fire on schedule completion events as post-run side effects |
| instruction-builder | Recipes reference schedules as the activation mechanism for workflows |
## Boundary Enforcement
When a request arrives that is NOT a schedule, redirect explicitly:
| Request | Correct builder | Reason |
|---------|----------------|--------|
| "route keyword X to workflow Y" | dispatch_rule-builder | That is routing, not timing |
| "define steps for the report" | workflow-builder | That is execution logic, not trigger |
| "fire when file arrives in S3" | hook-builder | That is event reaction, not cron schedule |
| "run this once on deploy" | hook-builder | One-time deploy event, not a schedule |
| "keep polling every 5s forever" | daemon-builder | Persistent loop, not a schedule artifact |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[schedule-builder]] | related | 0.49 |
| [[bld_collaboration_workflow]] | sibling | 0.44 |
| [[bld_collaboration_checkpoint]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_architecture_schedule]] | upstream | 0.37 |
| [[p03_sp_schedule_builder]] | upstream | 0.36 |
| [[workflow-builder]] | related | 0.35 |
| [[bld_architecture_kind]] | upstream | 0.34 |
| [[bld_collaboration_hook_config]] | sibling | 0.33 |
| [[bld_collaboration_hook]] | sibling | 0.33 |
