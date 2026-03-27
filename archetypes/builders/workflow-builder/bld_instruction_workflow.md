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
quality: null
tags: [instruction, workflow, orchestration, multi-step, P12]
idempotent: true
atomic: false
rollback: "Delete generated workflow YAML file; revert any spawn_configs created for this workflow"
dependencies: []
logging: true
tldr: "Build a workflow YAML that orchestrates agents in sequential, parallel, or mixed waves with dependency resolution, signals, and error recovery."
density_score: 0.93
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

---

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
15. `signals_emitted` -- list of all signal names from steps
16. `spawn_configs` -- list of spawn_config ids required (one per unique agent)
17. `prerequisites` -- list of artifacts that must exist before workflow starts
18. `quality` -- `null`
19. `created` -- ISO date
20. `updated` -- ISO date

Verifiable exit: YAML parses cleanly; all 20 fields present; steps_count matches actual steps list length.

### Phase 5: Validate Against Quality Gates

**Action**: Run 8 HARD gates before emitting; log 12 SOFT gates as warnings.

```
HARD gates (all must pass):
  H1: steps_count >= 2 and matches actual steps list length
  H2: each step has id, agent, action, input, output, signal, depends_on
  H3: depends_on references form a valid DAG (no cycles)
  H4: execution_mode is one of sequential, parallel, mixed
  H5: error_recovery is one of abort, skip_failed, retry
  H6: spawn_delay_ms == 5000
  H7: quality is null
  H8: all 20 YAML fields are present

SOFT gates (log warnings):
  S1-S4: each step has a unique signal name (4 step samples)
  S5-S8: agent ids reference known agent artifacts (4 agent samples)
  S9: spawn_configs list matches unique agents in steps
  S10: timeout_ms is reasonable for the number of steps
  S11: prerequisites list all artifacts steps depend on at start
  S12: waves are optimal (no step placed later than necessary)
```

Verifiable exit: 8/8 HARD gates pass.

---

## Output Contract

```yaml
id: workflow_{{mission_name}}
kind: workflow
pillar: P12
version: 1.0.0
mission_name: {{mission_name}}
goal: "{{goal}}"
execution_mode: {{execution_mode}}
steps_count: {{steps_count}}
steps:
  - id: {{step_1_id}}
    agent: {{step_1_agent}}
    action: "{{step_1_action}}"
    input: "{{step_1_input}}"
    output: "{{step_1_output}}"
    signal: {{step_1_signal}}
    depends_on: []
    timeout_ms: {{step_1_timeout_ms}}
    on_failure: {{step_1_on_failure}}
waves:
  - wave: 0
    steps: [{{step_1_id}}]
error_recovery: {{error_recovery}}
max_retries: {{max_retries}}
timeout_ms: {{timeout_ms}}
spawn_delay_ms: 5000
signals_emitted:
  - {{step_1_signal}}
spawn_configs:
  - {{spawn_config_1_id}}
prerequisites: {{prerequisites}}
quality: null
created: "{{created}}"
updated: "{{updated}}"
```

---

## Validation

- [ ] H1: steps_count >= 2 and matches actual steps list length
- [ ] H2: each step has id, agent, action, input, output, signal, depends_on
- [ ] H3: depends_on references form a valid DAG (no cycles)
- [ ] H4: execution_mode is one of sequential, parallel, mixed
- [ ] H5: error_recovery is one of abort, skip_failed, retry
- [ ] H6: spawn_delay_ms equals 5000
- [ ] H7: quality is null
- [ ] H8: all 20 YAML fields are present

---

## Metacognition

**Does**:
- Produce a runtime-executable workflow with wave ordering and dependency resolution
- Enforce that each step has one agent and one deliverable
- Always set spawn_delay_ms=5000 to prevent terminal race conditions
- Validate 8 HARD gates including DAG cycle detection before emitting

**Does NOT**:
- Define sequential prompt chains without agent coordination (chain handles that)
- Produce static dependency graphs without execution semantics (dag handles that)
- Route keywords to agents (dispatch_rule handles that)
- Execute the workflow -- it defines the orchestration plan only

**Chaining**: workflow-builder output is the orchestration plan consumed by spawn scripts. Pair with spawn-config-builder (how each agent is launched) and signal-builder (what completion signals are emitted). Build workflow after all agents and spawn_configs are defined.
