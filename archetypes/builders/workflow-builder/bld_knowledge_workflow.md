---
kind: knowledge_card
id: bld_knowledge_card_workflow
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for workflow production — atomic searchable facts
sources: workflow-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Workflow"
version: "1.0.0"
author: n03_builder
tags: [workflow, builder, examples]
tldr: "Golden and anti-examples for workflow construction, demonstrating ideal structure and common pitfalls."
domain: "workflow construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_workflow
  - bld_memory_workflow
  - p03_ins_workflow
  - workflow-builder
  - p01_kc_workflow
  - bld_architecture_workflow
  - bld_collaboration_workflow
  - p03_sp_workflow-builder
  - bld_instruction_chain
  - p10_lr_chain_builder
---

# Domain Knowledge: workflow
## Executive Summary
A `workflow` (P12) is a runtime orchestration plan — numbered steps with agents, dependencies, signals, and execution mode (sequential/parallel/mixed). It differs from `chain` (text-only prompt sequence), `dag` (dependency graph without execution), `crew` (collaboration protocol), and `handoff` (single-agent_group instruction) by specifying WHEN and HOW agents run, what signals they emit, and how failures are handled across multiple agent_groups.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 |
| Kind | `workflow` |
| ID pattern | `^p12_wf_[a-z][a-z0-9_]+$` |
| Naming | `p12_wf_{name_slug}.md` |
| Max body | 3072 bytes |
| Machine format | yaml (frontmatter) + markdown (body) |
| Required frontmatter fields | 11 |
| Recommended fields | 8 |
| `execution` values | `sequential`, `parallel`, `mixed` |
| `retry_policy` values | `none`, `per_step`, `global` |
| `quality` field | always `null` |
| `steps_count` | must exactly match numbered steps in body |
## Patterns
| Pattern | Rule |
|---------|------|
| Wave planning | Group independent steps into parallel waves; sequential between waves |
| Dependency resolution | Step N only starts after all `depends_on` steps emit completion signal |
| Signal contract | Every step emits a signal on completion; references signal-builder conventions |
| Spawn integration | Each agent_group step references a `spawn_config` ID |
| `per_step` retry | Isolates failures — one failed step does not abort healthy parallel steps |
| Timeout budgeting | Sequential: `timeout >= sum(step timeouts)`; parallel: `timeout >= max(step timeouts)` |
| Idempotent steps | Steps must be safe to retry without side effects |
| `steps_count` integrity | Count numbered steps in body and set `steps_count` to match exactly |
**Execution modes**:
| Mode | When to use |
|------|------------|
| `sequential` | Steps have strict ordering; each waits for previous |
| `parallel` | Steps are independent; all run simultaneously |
| `mixed` | Waves: parallel within wave, sequential between waves |
**Body sections (required order)**:
| Section | Content |
|---------|---------|
| `## Purpose` | Why this workflow exists; what mission it accomplishes |
| `## Steps` | Numbered steps — each defines `agent`, `action`, `input`, `output`, `signal` |
| `## Dependencies` | What must exist before workflow starts |
| `## Signals` | What signals are emitted and when |
**Boundary — what workflow is NOT**:
| kind | Why NOT workflow |
|------|----------------|
| `chain` | Text-only prompt sequence — no agents, no tools, no signals |
| `dag` | Defines dependency order only — no execution, no agent_groups |
| `crew` | Defines HOW agents collaborate — not WHEN they run |
| `handoff` | Single-agent_group task instruction — one task, not many steps |
| `dispatch_rule` | Routes keywords to agent_groups — does not orchestrate execution |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `steps_count` mismatch | HARD gate: count must match body steps exactly |
| Steps without `agent` field | Each step must define which agent executes it |
| No signals defined | Runtime has no completion contract; orchestrator cannot chain steps |
| Dependent steps without `depends_on` | Race condition — step may start before prerequisite finishes |
| `timeout` smaller than step sum | Workflow times out before steps can complete |
| `quality` set to a score | Never self-score; governance assigns |
| Business logic in step descriptions | Steps define orchestration, not implementation |
## Application
1. Define the mission in `title` and `domain`
2. Set `execution` mode: `sequential`, `parallel`, or `mixed`
3. Decompose mission into discrete steps — each with one agent and one action

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_workflow]] | downstream | 0.58 |
| [[bld_memory_workflow]] | downstream | 0.55 |
| [[p03_ins_workflow]] | downstream | 0.53 |
| [[workflow-builder]] | downstream | 0.52 |
| [[p01_kc_workflow]] | sibling | 0.52 |
| [[bld_architecture_workflow]] | downstream | 0.50 |
| [[bld_collaboration_workflow]] | downstream | 0.47 |
| [[p03_sp_workflow-builder]] | downstream | 0.47 |
| [[bld_instruction_chain]] | downstream | 0.46 |
| [[p10_lr_chain_builder]] | downstream | 0.44 |
