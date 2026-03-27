---
id: p03_ins_runtime_state
kind: instruction
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Runtime State Builder Instructions
target: "runtime-state-builder agent"
phases_count: 4
prerequisites:
  - "The agent whose runtime state needs definition is identified by name"
  - "The agent's decision points during execution are known or can be mapped"
  - "Persistence scope is known: within-session (ephemeral) or cross-session (persistent)"
validation_method: checklist
domain: runtime_state
quality: null
tags: [instruction, runtime-state, P10, agent-state, routing, heuristics, state-machine]
idempotent: true
atomic: false
rollback: "Delete the produced state file. No agent behavior changes until the state is loaded at runtime."
dependencies: []
logging: true
tldr: "Define the routing rules, priorities, heuristics, and decision tree an agent uses at runtime — the variable mental state accumulated during sessions."
density_score: 0.91
---

## Context

A **runtime_state** captures the variable mental state an agent accumulates and consults during execution. It is distinct from an agent's design-time identity (mental_model) and from ephemeral in-flight snapshots (session_state). A runtime_state contains routing rules that change based on experience, priority orderings, decision heuristics for ambiguous situations, and the domain map the agent navigates.

**Inputs**

| Field | Type | Description |
|---|---|---|
| `agent` | string | The agent whose state is being defined (e.g. `rag-source-builder`, `router-builder`) |
| `persistence_scope` | enum | `within_session` (reset each session) \| `cross_session` (persists across sessions) |
| `domain_map` | list | Domains this agent covers at runtime (e.g. `[llm_providers, benchmarks, tooling]`) |
| `decision_points` | list | Key decision junctions the agent encounters during execution |

**Output**

A single `.md` file with YAML frontmatter (17 required + 4 recommended fields) + body sections defining: routing_rules, decision_tree, priorities, heuristics, domain_map, tools_available, constraints, fallback, and update_triggers.

**Boundary rules**
- runtime_state = variable state the agent builds and consults during runtime (this builder)
- mental_model = design-time identity, values, and personality (different builder)
- session_state = ephemeral snapshot of a single in-flight conversation (different builder)
- learning_record = accumulated cross-session improvement patterns (different builder)

---

## Phases

### Phase 1: Research — Decision Mapping

Map the agent's runtime decision landscape before writing.

```
FOR the named agent:
  identify decision points:
    routing decisions:  "should I proceed or route this to another builder?"
    format decisions:   "which output structure fits this input?"
    scope decisions:    "is this within my domain or a boundary case?"
    tool decisions:     "which tool best serves this step?"

  FOR each decision point:
    map the branch conditions (IF x THEN y ELSE z)
    identify what signals trigger each branch (input features, context flags)
    note what happens at each leaf (action, route, error)

  priorities: what does this agent optimize for, in strict order?
    example: correctness > completeness > brevity > speed

  heuristics: rules of thumb for situations where the decision tree is ambiguous
    example: "when domain is unclear, prefer the narrower scope over the broader"

  tools_available: which tools can this agent invoke during execution?
    list tool names + one-line description of when each is used

  constraints: what limits apply to this agent's runtime behavior?
    example: max retries, forbidden actions, required audit steps

  update_triggers: what events cause this state to be updated?
    example: "after each successful artifact delivery", "on schema version change"

Check brain_query [IF MCP] for existing runtime_states for the same agent.
Generate state_slug: snake_case, matches agent name pattern.
```

Deliverable: decision map with branches, priorities, heuristics, and update triggers.

### Phase 2: Classify — Boundary Check

Confirm the artifact belongs to `runtime_state` and not a sibling kind.

```
IF the artifact defines the agent's identity, personality, or design-time values:
  RETURN "Route to mental-model-builder — that defines what the agent IS, not its runtime state."
IF the artifact captures a snapshot of a single in-flight conversation:
  RETURN "Route to session-state-builder — that is ephemeral, not accumulated state."
IF the artifact records patterns learned across many sessions for future improvement:
  RETURN "Route to learning-record-builder."
IF the artifact defines routing, decision logic, priorities, and heuristics that the
  agent consults and may update during execution:
  PROCEED as runtime_state
```

Deliverable: confirmed `kind: runtime_state` with one-line justification.

### Phase 3: Compose — Build the State Artifact

Assemble frontmatter and body following SCHEMA.md and OUTPUT_TEMPLATE.md.

```
ID generation:
  id = "p10_rs_" + state_slug
  state_slug typically mirrors the agent slug (e.g. p10_rs_router_builder)

Frontmatter (17 required + 4 recommended fields from SCHEMA.md):
  Required: id, kind (= runtime_state), pillar (= P10), title, version,
            created, updated, author, agent, persistence_scope,
            domain_map (list), priorities (ordered list),
            tools_available (list), constraints (list),
            fallback, update_triggers, quality (= null)
  Recommended: tags, tldr, keywords, density_score

Body structure (all sections required):

  ## Routing Rules
  How the agent routes incoming requests at runtime.
  Format as a decision table or IF/THEN list:
    IF {signal or condition}: ROUTE TO {destination or action}
    IF {signal or condition}: PROCEED with {approach}
  Each rule must be concrete and actionable — no abstract directives.

  ## Decision Tree
  Branch logic for the agent's key decision points.
  Format as nested conditions with explicit leaf outcomes:
    root condition
    ├── branch A condition -> outcome A
    ├── branch B condition -> outcome B
    │   ├── sub-branch B1 -> outcome B1
    │   └── sub-branch B2 -> outcome B2
    └── fallback -> default outcome
  Cover at least 2 decision points identified in Phase 1.

  ## Priorities
  Ordered list of what the agent optimizes for (1 = highest):
    1. {primary optimization target}
    2. {secondary optimization target}
    3. ...
  No ties — priorities must be strictly ordered.

  ## Heuristics
  Rules of thumb for ambiguous situations not fully covered by the decision tree:
    - "When X is unclear, prefer Y over Z because ..."
    - "If two approaches are equivalent, choose the one with fewer dependencies."
  Minimum 3 heuristics.

  ## Domain Map
  Domains this agent covers at runtime (table or list):
    domain: {domain_name} | scope: {what the agent does within this domain}
  Also: domains explicitly excluded from this agent's scope.

  ## Tools Available
  | Tool | When Used |
  |---|---|
  | {tool_name} | {specific condition triggering its use} |

  ## Constraints
  Hard limits on runtime behavior:
    - {constraint description — specific, not vague}
  Examples: max retries before escalation, forbidden output types, required audit steps.

  ## Fallback
  What happens when all primary paths fail:
    - Action taken
    - Error returned to caller
    - Escalation path (if any)

  ## Update Triggers
  Events that cause this state to be updated:
    - {trigger}: {what changes in state}
```

Deliverable: complete `.md` file with frontmatter + all 9 body sections.

### Phase 4: Validate — Gate Check

Run all quality gates before delivering.

```
HARD gates (all must pass — fix before delivering):
  H01: YAML frontmatter parses without errors
  H02: id follows p10_rs_ pattern
  H03: kind == "runtime_state"
  H04: pillar == "P10"
  H05: quality == null
  H06: agent field is non-empty and identifies a specific agent
  H07: persistence_scope is "within_session" or "cross_session"
  H08: all 9 required body sections are present

SOFT gates (target >= 5/8):
  S01: routing_rules are concrete IF/THEN statements (not abstract directives)
  S02: decision_tree has at least 2 root decision points with branching
  S03: priorities are strictly ordered with no ties
  S04: at least 3 heuristics are defined
  S05: domain_map includes both covered and excluded domains
  S06: tools_available specifies the condition that triggers each tool (not just "when needed")
  S07: constraints are specific (not "be careful" or "use good judgment")
  S08: update_triggers describe what in the state changes, not just "update state"

IF any HARD gate fails: fix the violation and re-check.
IF soft_score < 5: add "Known gaps" note.
Verify: state is RUNTIME (not design-time identity, not ephemeral snapshot).
Set quality: null — never self-score.
```

---

## Output Contract

```
---
id: p10_rs_{{state_slug}}
kind: runtime_state
pillar: P10
title: "{{title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
agent: {{agent_name}}
persistence_scope: {{within_session|cross_session}}
domain_map: [{{domain_1}}, {{domain_2}}]
priorities: [{{priority_1}}, {{priority_2}}, {{priority_3}}]
tools_available: [{{tool_1}}, {{tool_2}}]
constraints: [{{constraint_1}}, {{constraint_2}}]
fallback: "{{fallback_description}}"
update_triggers: [{{trigger_1}}, {{trigger_2}}]
quality: null
tags: [runtime-state, {{agent_name}}, P10]
tldr: "{{<=160_char_summary}}"
---

## Routing Rules

{{concrete_if_then_routing_rules}}

## Decision Tree

{{branching_decision_logic_with_leaf_outcomes}}

## Priorities

1. {{primary_optimization_target}}
2. {{secondary_optimization_target}}
3. {{tertiary_optimization_target}}

## Heuristics

- {{heuristic_1}}
- {{heuristic_2}}
- {{heuristic_3}}

## Domain Map

| Domain | Scope |
|---|---|
| {{domain_name}} | {{what_agent_does_here}} |

## Tools Available

| Tool | When Used |
|---|---|
| {{tool_name}} | {{specific_trigger_condition}} |

## Constraints

- {{specific_constraint_1}}
- {{specific_constraint_2}}

## Fallback

Action: {{what_happens_on_all_paths_failing}}
Error: {{what_caller_receives}}
Escalation: {{escalation_path_if_any}}

## Update Triggers

- {{trigger_event}}: {{what_changes_in_state}}
```

---

## Validation

- [ ] All 8 HARD gates pass (H01-H08)
- [ ] Soft score >= 5/8 or "Known gaps" block present
- [ ] All 9 body sections present and non-empty
- [ ] Routing rules are concrete IF/THEN statements — no abstract directives
- [ ] Decision tree has genuine branching (not a linear list)
- [ ] Priorities are strictly ordered with no ties
- [ ] `quality: null` — never self-scored
- [ ] State is runtime-variable, not design-time identity (mental_model boundary confirmed)

---

## Metacognition

**Does**
- Define the routing rules, decision logic, priorities, and heuristics an agent applies at runtime
- Capture what changes during execution (accumulated routing experience, updated priorities)
- Specify the persistence scope — whether state resets each session or carries across sessions
- Distinguish runtime state (variable, accumulated) from design-time identity (fixed, definitional)

**Does NOT**
- Define the agent's identity, values, or personality (mental-model-builder)
- Capture ephemeral in-flight conversation snapshots (session-state-builder)
- Record cross-session learning patterns for future improvement (learning-record-builder)
- Build a search or retrieval index (brain-index-builder)

**Chaining**
- Upstream: agent definition (mental_model) establishes identity; this builder adds the variable runtime layer
- Downstream: runtime state is loaded by the agent at session start and updated after key decision points
- Complement pair: runtime_state (routing + decisions) + mental_model (identity + values) = complete agent specification
