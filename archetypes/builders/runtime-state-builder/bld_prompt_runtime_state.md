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
quality: 9.1
tags: [instruction, runtime-state, P10, agent-state, routing, heuristics, state-machine]
idempotent: true
atomic: false
rollback: "Delete the produced state file. No agent behavior changes until the state is loaded at runtime."
dependencies: []
logging: true
tldr: "Define the routing rules, priorities, heuristics, and decision tree an agent uses at runtime — the variable mental state accumulated during sessions."
density_score: 0.91
llm_function: REASON
related:
  - bld_collaboration_runtime_state
  - p03_ins_mental_model
  - runtime-state-builder
  - p03_sp_runtime_state_builder
  - bld_architecture_runtime_state
  - bld_collaboration_agent
  - bld_collaboration_mental_model
  - bld_knowledge_card_runtime_state
  - agent-builder
  - bld_memory_runtime_state
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


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_runtime_state]] | related | 0.50 |
| [[p03_ins_mental_model]] | sibling | 0.50 |
| [[runtime-state-builder]] | related | 0.47 |
| [[p03_sp_runtime_state_builder]] | upstream | 0.43 |
| [[bld_architecture_runtime_state]] | upstream | 0.42 |
| [[bld_collaboration_agent]] | downstream | 0.39 |
| [[bld_collaboration_mental_model]] | upstream | 0.38 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.37 |
| [[agent-builder]] | upstream | 0.35 |
| [[bld_memory_runtime_state]] | related | 0.34 |
