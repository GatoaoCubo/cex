---
id: p03_ins_workflow
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Workflow Builder Instructions
target: "workflow-builder agent"
phases_count: 5
prerequisites:
  - "Mission goal is defined in one sentence"
  - "At least 2 agents or steps are identified"
  - "Execution mode is known: sequential, parallel, or mixed"
  - "Completion signals are specified or can be derived from step outputs"
validation_method: checklist
domain: workflow
quality: 9.0
tags: [instruction, workflow, orchestration, multi-step, P12]
idempotent: true
atomic: false
rollback: "Delete generated workflow YAML file; revert any spawn_configs created for this workflow"
dependencies: []
logging: true
tldr: "Build a workflow YAML that orchestrates agents in sequential, parallel, or mixed waves with dependency resolution, signals, and error recovery."
density_score: 0.93
llm_function: REASON
related:
  - bld_knowledge_card_workflow
  - p11_qg_workflow
  - p10_lr_chain_builder
  - bld_memory_workflow
  - bld_architecture_chain
  - bld_instruction_chain
  - p01_kc_workflow
  - p03_sp_workflow-builder
  - p12_wf_builder_8f_pipeline
  - workflow-builder
---
## Context
The workflow-builder produces a `workflow` artifact -- a structured YAML that defines how agents are orchestrated at runtime. A workflow decomposes a mission into steps, assigns agents to each step, maps dependencies between steps, specifies completion signals, and defines error recovery strategy.
**Critical distinction**: a `workflow` is runtime orchestration with execution semantics (waves, signals, dependencies). It is NOT a prompt chain (`chain` -- sequential prompt calls without agent coordination), NOT a static dependency graph (`dag` -- structure only, no execution), and NOT a routing rule (`dispatch_rule` -- keyword-to-agent routing). Confusing these produces orchestration that cannot be executed.
**Input contract**:
- `mission_name`: string -- kebab-case mission identifier (e.g. `onboard-new-agent`, `research-and-publish`)
- `goal`: string -- one sentence describing the end-to-end outcome
- `steps`: list of step definition objects (see Phase 2)
- `execution_mode`: enum -- `sequential` | `parallel` | `mixed`
- `error_recovery`: enum -- `abort` | `skip_failed` | `retry`
- `max_retries`: integer -- retry attempts per step (default 2)
- `timeout_ms`: integer -- total workflow timeout (default 600000)
**Output contract**: a single `workflow` YAML with all required fields, stored at `records/workflows/{mission_name}.yaml`.
**Variables**:
- `{{mission_name}}` -- kebab-case mission identifier
- `{{goal}}` -- mission outcome sentence
- `{{step_N_id}}` -- Nth step identifier
- `{{step_N_agent}}` -- agent assigned to Nth step
- `{{step_N_signal}}` -- completion signal for Nth step
## Phases
### Phase 1: Decompose Mission into Steps
**Action**: Break the mission goal into discrete, assignable steps.
```
FOR the given mission_goal:
    1. Identify distinct deliverables (each deliverable = one step)
    2. Assign one agent per step (steps are not shared between agents)
    3. Name each step as: verb_noun (e.g. research_competitors, build_component)
Step granularity rules:
    - One step = one agent = one deliverable
    - Steps that can run independently -> parallel candidates
    - Steps that need prior output -> sequential, add depends_on
    - Max 12 steps per workflow; split into sub-workflows if larger
steps_count = len(steps)
ASSERT steps_count >= 2
```
Verifiable exit: each step has a name, an assigned agent, and one deliverable; steps_count >= 2.
### Phase 2: Define Each Step Object
**Action**: Build a complete step definition for each step.
Step object schema:
```
{
  id: string -- snake_case step identifier
  agent: string -- agent id responsible for this step
  action: string -- one-sentence description of what the agent does
  input: string or object -- what the agent receives as input
  output: string -- the deliverable produced (file path, signal, or artifact id)
  signal: string -- completion signal name emitted when step finishes
  depends_on: list of step ids or [] -- steps that must complete first
  timeout_ms: integer -- step-level timeout (overrides workflow default)
  on_failure: enum -- abort | skip | retry (overrides workflow error_recovery)
}
```
Dependency rules:
```
IF step B needs step A's output:
    step_B.depends_on = [step_A.id]
IF steps A and B are independent:
    both have depends_on = []
    both can run in parallel (if execution_mode != sequential)
IF execution_mode == "sequential":
    each step implicitly depends on the previous step (no explicit depends_on needed)
Cycle detection: depends_on must form a DAG (no circular dependencies)
```
Verifiable exit: each step has all 9 fields; depends_on forms a valid DAG (no cycles).
### Phase 3: Plan Wave Ordering
**Action**: Group steps into execution waves based on dependency resolution.
```
wave_0 = steps with depends_on == []
wave_1 = steps whose depends_on are all in wave_0
wave_N = steps whose depends_on are all in wave_0..wave_(N-1)
IF execution_mode == "sequential":
    each wave has exactly 1 step
IF execution_mode == "parallel":
    all steps with no dependencies are in wave_0
    all remaining steps form subsequent waves
IF execution_mode == "mixed":
    apply dependency resolution; group independent steps per wave
```
Wave planning rules:
- Steps in the same wave run concurrently
- A step can only start when all its depends_on steps have emitted their signals
- spawn_delay_ms=5000 is applied between wave launches (prevents terminal race conditions)
Verifiable exit: all steps are assigned to a wave; no step appears in a wave before its dependencies.
### Phase 4: Compose workflow YAML
**Action**: Assemble all resolved values into the 20-field YAML structure.
Required fields:
1. `id` -- `workflow_{{mission_name}}`
2. `kind` -- `workflow`
3. `pillar` -- `P12`
4. `version` -- `1.0.0`
5. `mission_name` -- `{{mission_name}}`
6. `goal` -- `{{goal}}`
7. `execution_mode` -- `{{execution_mode}}`
8. `steps_count` -- integer matching actual steps list length
9. `steps` -- list of step objects from Phase 2
10. `waves` -- wave groupings from Phase 3
11. `error_recovery` -- `{{error_recovery}}`
12. `max_retries` -- integer
13. `timeout_ms` -- integer
14. `spawn_delay_ms` -- `5000` (always)


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_workflow]] | upstream | 0.57 |
| [[p11_qg_workflow]] | downstream | 0.53 |
| [[p10_lr_chain_builder]] | downstream | 0.52 |
| [[bld_memory_workflow]] | downstream | 0.52 |
| [[bld_architecture_chain]] | downstream | 0.48 |
| [[bld_instruction_chain]] | sibling | 0.47 |
| [[p01_kc_workflow]] | downstream | 0.47 |
| [[p03_sp_workflow-builder]] | related | 0.46 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.44 |
| [[workflow-builder]] | downstream | 0.41 |
