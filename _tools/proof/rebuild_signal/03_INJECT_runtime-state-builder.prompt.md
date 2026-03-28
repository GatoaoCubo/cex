# CEX Crew Runner -- Builder Execution
**Builder**: `runtime-state-builder`
**Function**: INJECT
**Intent**: reconstroi signal-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:33:56.820518

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_runtime_state.md
---
id: runtime-state-builder
kind: type_builder
pillar: P10
parent: null
domain: runtime_state
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, runtime-state, P10, specialist, runtime, memory]
---

# runtime-state-builder
## Identity
Especialista em construir runtime_states — estados mentais variaveis que agentes acumulam durante sessoes de runtime.
Conhece padroes de state machines, decision trees, routing heuristics, e a diferenca entre runtime_state (P10), mental_model (P02), session_state (P10), e learning_record (P10).
## Capabilities
- Definir estado mental de agente com routing rules e decision trees
- Produzir runtime_state com priorities, heuristics, e tool preferences
- Especificar state transitions e update conditions
- Documentar persistence scope (within-session vs cross-session)
- Capturar domain_map e constraint evolution
## Routing
keywords: [runtime-state, mental-model, agent-state, routing, decisions, priorities, heuristics, state-machine]
triggers: "define agent runtime state", "what decisions does this agent make", "create runtime mental model"
## Crew Role
In a crew, I handle RUNTIME STATE DEFINITION.
I answer: "what routing rules, priorities, and heuristics does this agent use at runtime?"
I do NOT handle: design-time identity (mental-model-builder), ephemeral snapshots (session-state-builder), search indexes (brain-index-builder).

### bld_instruction_runtime_state.md
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

### bld_knowledge_card_runtime_state.md
---
kind: knowledge_card
id: bld_knowledge_card_runtime_state
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for runtime_state production — atomic searchable facts
sources: runtime-state-builder MANIFEST.md + SCHEMA.md, state machine theory, BDI architecture
---

# Domain Knowledge: runtime_state
## Executive Summary
Runtime states are mutable cognitive contexts that agents accumulate during execution — live routing rules, decision trees, priorities, and heuristics that evolve based on inputs and outcomes. Each runtime state captures ONE agent's current decision-making context with explicit state transitions and persistence scope. They differ from mental models (P02, static design-time blueprints), session states (ephemeral snapshots lost on session end), learning records (persistent cross-session experience), and axioms (immutable truths) by being mutable, accumulative decision contexts that can persist within or across sessions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| Kind | `runtime_state` (exact literal) |
| ID pattern | `p10_rs_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 9 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Persistence | within_session or cross_session |
| Key sections | Routing Rules, Decision Tree, Priorities, Heuristics, State Transitions |
## Patterns
| Pattern | Application |
|---------|-------------|
| Mutable state | Runtime state evolves during execution; design-time identity does not |
| Concrete routing conditions | Keywords as concrete nouns/verbs with confidence thresholds |
| Decision tree depth | Max 3 levels to avoid reasoning complexity |
| Ordered priorities | Explicit rank order; tie-breaking requires explicit rules |
| Explicit triggers | State transitions have named triggers, not implicit changes |
| Persistence declaration | within_session (default) or cross_session (requires justification) |
| Update frequency | Event-driven (on task completion) or polling (interval-based) |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `pillar: P02` on runtime_state | P02 is design-time; runtime_state is P10 |
| Mixing identity with state | Agent identity belongs in agent/mental_model, not runtime_state |
| No state transitions defined | State without transitions is a static snapshot, not runtime state |
| Implicit persistence | Must declare within_session or cross_session explicitly |
| Routing without confidence thresholds | Ambiguous dispatch; no fallback logic possible |
| cross_session without justification | Most state is session-scoped; persistence needs rationale |
## Application
1. Identify the target agent and its runtime decision requirements
2. Define routing_rules with keywords, actions, confidence thresholds
3. Define decision_tree with max 3 levels of if/then/else
4. Set priorities in explicit rank order
5. Write heuristics for edge cases specific to this agent's domain
6. Define state transitions with named triggers and conditions
7. Set persistence scope (within_session or cross_session)
8. Validate: 9 HARD + 10 SOFT gates, body <= 3072 bytes
## References
- runtime-state-builder SCHEMA.md v1.0.0
- Finite State Machine theory
- BDI architecture (Belief-Desire-Intention)
- Blackboard architecture (shared multi-agent state)

### bld_quality_gate_runtime_state.md
---
id: p11_qg_runtime_state
kind: quality_gate
pillar: P11
title: "Gate: Runtime State"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: runtime_state
quality: null
density_score: 0.85
tags:
  - quality-gate
  - runtime-state
  - p11
  - agent-state
  - routing
tldr: "Quality gate for agent runtime mental state: verifies routing rules, state transitions, persistence scope, and conflict resolution."
---

## Definition
A runtime state artifact captures the live decision-making configuration of an agent: its routing rules (with conditions and confidence), state transitions (with trigger events), priority ordering, and heuristics. It applies only during execution — it contains no design-time content such as capability descriptions or architectural diagrams. Persistence scope declares whether state survives across sessions or resets each time.
Scope: files with `kind: runtime_state`. Does not apply to mental models (design-time identity), system prompts (static instructions), or session state (ephemeral task context).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p10_rs_*` | `id.startswith("p10_rs_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `runtime_state` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, agent, persistence all present |
| H07 | Routing rules section present with >= 2 rules each having a condition | count routing rule entries >= 2; each has a condition field |
| H08 | State transitions section present with >= 1 named transition and a trigger event | count transitions >= 1; each has trigger field non-empty |
| H09 | `persistence` field is one of: within-session, cross-session | enum membership check |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every routing rule has an explicit condition (not a vague keyword) | 1.0 |
| 3  | Every state transition has a named trigger event (not just a description) | 1.0 |
| 4  | Priority ordering present with rationale for each rank | 1.0 |
| 5  | Heuristics section present with at least 2 rules of thumb and their confidence levels | 1.0 |
| 6  | Domain map present with explicit boundary (what this agent handles vs. what it defers) | 1.0 |
| 7  | Tags list includes `runtime-state` | 0.5 |
| 8  | Update conditions explicit (what triggers a state change, not just that state can change) | 1.0 |
| 9  | Conflict resolution described for cases where two routing rules could both fire | 1.0 |
| 10 | No design-time content present (no capability lists, architecture notes, or setup instructions) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 10.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for agent state design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Agent is in early bootstrapping and fewer than 2 routing rules have been observed in practice |
| approver | Domain lead must approve in writing before bypass takes effect |

### bld_schema_runtime_state.md
---
kind: schema
id: bld_schema_runtime_state
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for runtime_state
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: runtime_state
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_rs_{agent_slug}) | YES | — | Namespace compliance |
| kind | literal "runtime_state" | YES | — | Type integrity |
| pillar | literal "P10" | YES | — | Pillar assignment |
| title | string "Runtime State: {agent}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| agent | string | YES | — | Which agent this state belongs to |
| persistence | enum (session, cross_session) | YES | — | How long state lives |
| domain | string | YES | — | Domain this agent operates in |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
| routing_mode | enum (keyword, semantic, hybrid, rule_based) | YES | — | How routing decisions are made |
| priority_count | integer >= 1 | YES | — | Number of priorities defined |
| update_frequency | enum (per_task, per_session, on_trigger) | YES | — | When state updates |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| fallback_agent | string | REC | — | Who handles if this agent fails |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
| constraint_count | integer | REC | — | Number of constraints |
## ID Pattern
Regex: `^p10_rs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Agent Context` — which agent and its domain
2. `## Routing Rules` — how the agent routes tasks at runtime
3. `## Decision Tree` — branch conditions and outcomes
4. `## Priorities` — ordered list of optimization targets
5. `## Heuristics` — rules of thumb for ambiguous cases
6. `## Constraints` — limits on agent behavior
7. `## State Transitions` — what triggers state changes
## Constraints
- max_bytes: 3072 (body only)
- naming: p10_rs_{agent_slug}.md
- id == filename stem
- persistence MUST be valid enum
- routing_mode MUST be valid enum
- quality: null always

### bld_examples_runtime_state.md
---
kind: examples
id: bld_examples_runtime_state
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_state artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: runtime-state-builder
## Golden Example
INPUT: "Cria runtime_state para o agente de pesquisa (researcher) definindo routing e prioridades em runtime"
OUTPUT:
```yaml
id: p10_rs_researcher
kind: runtime_state
pillar: P10
title: "Runtime State: Researcher Agent"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
agent: "researcher"
persistence: "cross_session"
domain: "market research"
quality: null
tags: [runtime-state, researcher, routing, priorities, heuristics]
tldr: "Researcher agent runtime state with keyword routing, 4 priorities, and source selection heuristics"
routing_mode: "hybrid"
priority_count: 4
update_frequency: "per_task"
fallback_agent: "general_assistant"
density_score: 0.88
constraint_count: 4
linked_artifacts:
  primary: "p02_mm_researcher"
  related: [p10_lr_research_patterns, p10_bi_knowledge_pool]
## Agent Context
Researcher agent operates in market research domain. Routes incoming
research tasks to appropriate sources (web, pool, API) based on
query type and confidence thresholds. Accumulates source reliability
scores and routing preferences during execution.
## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| Pool-first | Query matches existing knowledge card | Return from pool, skip web | >= 0.85 |
| Web-fallback | Pool confidence < threshold | Search web sources | >= 0.60 |
| API-direct | Query is structured data request | Call API connector directly | >= 0.90 |
| Multi-source | Complex query, no single source sufficient | Fan out to pool + web + API | >= 0.70 |
## Decision Tree
```text
incoming_query
  ├── is_structured_data? -> API-direct route
  ├── pool_match >= 0.85? -> Pool-first route
  ├── pool_match >= 0.60? -> Web-fallback route
  └── complex_query? -> Multi-source route
```
## Priorities
1. Accuracy — prefer verified sources over speed
2. Freshness — prefer recent data over cached (max 7d stale)
3. Cost efficiency — minimize API calls when pool suffices
4. Completeness — cover all facets of multi-part queries
## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| Prefer pool for domain queries | Domain matches existing KC tags | 0.85 |
| Prefer web for trending topics | Query contains date-sensitive terms | 0.75 |
| Skip API for qualitative research | Query is opinion/analysis type | 0.80 |
| Fan-out for competitive analysis | Query mentions competitors | 0.70 |
## Constraints
1. Max 3 concurrent web requests per task
2. API budget: max 10 calls per session
3. Pool results must have quality >= 7.0 to be used
4. Web sources must be from allowlisted domains
## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| High pool hit rate | web_preferred | pool_preferred | 5+ consecutive pool hits |
| Pool staleness detected | pool_preferred | web_preferred | 3+ stale results in row |
| Budget exhaustion | any | pool_only | API calls >= budget limit |
| Quality drop | any | escalate | 3+ results below quality threshold |
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p10_rs_ pattern (H02 pass)
- kind: runtime_state (H04 pass)
- 19 frontmatter fields present (H08 pass)
- persistence: "cross_session" valid enum (H07 pass)
- routing_mode: "hybrid" valid enum (H09 pass)
- 4 routing rules with conditions and confidence (S03 pass)
- Decision tree with 4 branches (S04 pass)
- 4 ordered priorities with rationale (S05 pass)
- 4 heuristics with confidence levels (S06 pass)
## Anti-Example
INPUT: "Make agent state"
BAD OUTPUT:
```yaml
id: agent_state
kind: runtime_state
title: "State"
quality: 8.0
agent: researcher
## Rules
- Route queries to the best source
- Prioritize accuracy
- Use fallbacks when needed
```
FAILURES:
1. id: no p10_rs_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL

### bld_config_runtime_state.md
---
kind: config
id: bld_config_runtime_state
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for runtime_state production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: runtime_state Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p10_rs_{agent_slug}.md | p10_rs_researcher.md |
| Builder dir | kebab-case | runtime-state-builder/ |
| Fields | snake_case | routing_mode, update_frequency |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P10_memory/examples/p10_rs_{agent_slug}.md
- Compiled: cex/P10_memory/compiled/p10_rs_{agent_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Density: >= 0.80
## Persistence Modes
| Mode | Lifetime | Use case |
|------|----------|----------|
| session | Reset on session end | Ephemeral routing preferences |
| cross_session | Survives across sessions | Accumulated routing intelligence |
## Routing Mode Reference
| Mode | Mechanism | Best for |
|------|-----------|----------|
| keyword | Exact keyword matching | Simple, deterministic routing |
| semantic | Embedding similarity | Fuzzy, meaning-based routing |
| hybrid | Keyword + semantic combined | Balanced accuracy + recall |
| rule_based | Explicit if-then rules | Complex multi-condition routing |

### bld_output_template_runtime_state.md
---
kind: output_template
id: bld_output_template_runtime_state
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for runtime_state production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: runtime_state
```yaml
id: p10_rs_{{agent_slug}}
kind: runtime_state
pillar: P10
title: "Runtime State: {{agent_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent: "{{agent_name}}"
persistence: "{{session_or_cross_session}}"
domain: "{{domain_value}}"
quality: null
tags: [runtime-state, {{agent}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
routing_mode: "{{keyword_or_semantic_or_hybrid_or_rule_based}}"
priority_count: {{number}}
update_frequency: "{{per_task_or_per_session_or_on_trigger}}"
fallback_agent: "{{who_handles_failure}}"
density_score: {{0.80_to_1.00}}
constraint_count: {{number}}
linked_artifacts:
  primary: "{{related_mental_model_or_agent}}"
  related: [{{related_refs}}]
## Agent Context
{{which_agent_and_domain_context}}
## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| {{rule_1}} | {{when_triggered}} | {{what_happens}} | {{threshold}} |
| {{rule_2}} | {{when_triggered}} | {{what_happens}} | {{threshold}} |
## Decision Tree
```text
{{input_condition}}
  ├── {{branch_1}} -> {{outcome_1}}
  ├── {{branch_2}} -> {{outcome_2}}
  └── {{fallback}} -> {{default_outcome}}
```
## Priorities
1. {{highest_priority}} — {{rationale}}
2. {{second_priority}} — {{rationale}}
3. {{third_priority}} — {{rationale}}
## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| {{rule_of_thumb_1}} | {{ambiguous_situation}} | {{confidence_level}} |
| {{rule_of_thumb_2}} | {{ambiguous_situation}} | {{confidence_level}} |
## Constraints
1. {{limit_1}}
2. {{limit_2}}
3. {{limit_3}}
## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| {{event_1}} | {{state_a}} | {{state_b}} | {{when}} |
| {{event_2}} | {{state_b}} | {{state_c}} | {{when}} |
```

### bld_architecture_runtime_state.md
---
kind: architecture
id: bld_architecture_runtime_state
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of runtime_state — inventory, dependencies, and architectural position
---

# Architecture: runtime_state in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_agent, persistence_scope, etc.) | runtime-state-builder | active |
| routing_rules | Active routing decisions accumulated during runtime | agent | active |
| decision_history | Log of decisions made with context and outcomes | agent | active |
| priorities | Current priority ordering that may shift during execution | agent | active |
| heuristics | Runtime-adapted rules of thumb based on recent experience | agent | active |
| tool_preferences | Learned tool selection biases from recent success/failure | agent | active |
| state_transitions | Conditions that trigger state updates during execution | author | active |
## Dependency Graph
```
mental_model    --initializes-->  runtime_state  --consumed_by-->  agent
session_state   --feeds-->        runtime_state  --produces-->     updated_decisions
runtime_state   --signals-->      state_update
```
| From | To | Type | Data |
|------|----|------|------|
| mental_model (P02) | runtime_state | data_flow | design-time model provides initial state values |
| session_state (P10) | runtime_state | data_flow | ephemeral session data feeds runtime updates |
| runtime_state | agent (P02) | consumes | agent uses current runtime state for decisions |
| runtime_state | updated_decisions | produces | refined routing and priority decisions |
| runtime_state | state_update (P12) | signals | emitted when state transitions occur |
| learning_record (P10) | runtime_state | dependency | past learnings inform initial heuristics |
## Boundary Table
| runtime_state IS | runtime_state IS NOT |
|------------------|----------------------|
| A variable mental state accumulated during agent runtime | A design-time cognitive map (mental_model P02) |
| Contains routing rules, priorities, and heuristics that evolve | An ephemeral snapshot discarded after session (session_state P10) |
| Persists within or across sessions based on scope | A permanent record of past experience (learning_record P10) |
| Updated by state transitions triggered at runtime | A static configuration loaded once at boot |
| Scoped to one agent with specific update conditions | A search index or vector store (brain_index P01) |
| Reflects current operational intelligence | A historical changelog |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Initialization | mental_model, learning_record | Supply design-time defaults and past learnings |
| State | frontmatter, routing_rules, priorities, heuristics, tool_preferences | Current runtime values the agent operates with |
| Transitions | state_transitions, session_state | Define when and how state values update |
| Decisions | decision_history, updated_decisions | Record and produce routing decisions |
| Events | state_update | Signal state changes to observers |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `runtime-state-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
