---
id: p03_ins_router
kind: instruction
pillar: P02
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Router Builder Instructions
target: "router-builder agent"
phases_count: 4
prerequisites:
  - "Routing domain is identified (e.g. task-to-satellite, intent-to-agent, request-to-service)"
  - "All possible destination targets are enumerated (satellites, agents, or services)"
  - "Patterns or signals that distinguish each destination are known or inferable"
validation_method: checklist
domain: router
quality: null
tags: [instruction, router, P02, routing, dispatch, route-table]
idempotent: true
atomic: false
rollback: "Delete the produced router file. No routing behavior changes until the router is wired to a dispatcher."
dependencies: []
logging: true
tldr: "Build a route table with patterns, confidence thresholds, fallback, and escalation logic for task-to-destination dispatch."
density_score: 0.91
---

## Context

A **router** artifact defines task-to-destination routing logic: given an incoming task, which satellite, agent, or service should handle it? It contains a route table (pattern → destination mappings), confidence thresholds per route, a fallback destination for unmatched tasks, and an escalation policy for ambiguous matches.

**Inputs**

| Field | Type | Description |
|---|---|---|
| `routing_domain` | string | Category of tasks being routed (e.g. `satellite_task_routing`, `intent_dispatch`) |
| `destinations` | list | All valid routing targets (satellite names, agent IDs, or service endpoints) |
| `patterns` | list | Signals that distinguish each destination (keywords, regex, intent labels) |
| `confidence_threshold` | float | Default minimum confidence to commit to a route (0.0–1.0, default 0.7) |
| `fallback_route` | string | Destination for tasks that match no route |

**Output**

A single `.md` file with YAML frontmatter (14 required fields) + body containing: Routes table, Decision Logic, Fallback section, Escalation section, Integration section. Body must be <= 4096 bytes.

**Boundary rules**
- router = full routing logic with confidence thresholds, fallback, escalation (this builder)
- dispatch_rule = simple keyword-to-satellite mapping without confidence scoring (different builder)
- workflow = multi-step orchestration sequence (different builder)
- agent = identity definition for a single specialized executor (different builder)

---

## Phases

### Phase 1: Research — Route Analysis

Map tasks to destinations and determine routing logic before writing.

```
FOR each destination in destinations:
  identify 2-5 patterns that signal "this task goes here":
    pattern types: keyword match, regex, intent label, domain tag, priority signal
  assign confidence_min per route (can vary from global default):
    critical destinations: higher threshold (e.g. 0.85)
    general destinations:  default threshold (e.g. 0.70)
  assign priority (integer, 1 = highest) for tie-breaking

Fallback route:
  SELECT one destination that handles "everything else"
  Fallback must always be a valid destination (not null, not "none")

Escalation scenarios:
  ambiguous match:   multiple routes exceed confidence_min simultaneously
  low confidence:    best match is below confidence_min for all routes
  conflict:          two routes have equal priority and equal confidence

Check brain_query [IF MCP] for existing routers in the same domain to avoid duplicates.
Generate router_slug: snake_case, lowercase, no hyphens (e.g. satellite_task_router)
```

Deliverable: route map with patterns, confidence thresholds, priority, and fallback identified.

### Phase 2: Classify — Boundary Check

Confirm the artifact belongs to `router` and not a sibling kind.

```
IF caller needs only a simple keyword → satellite table with no confidence scoring:
  RETURN "Route to dispatch-rule-builder — simpler artifact, no confidence logic needed."
IF caller needs a multi-step execution sequence with dependencies:
  RETURN "Route to workflow-builder — workflows orchestrate steps, not dispatch."
IF caller needs to define what an agent IS rather than where to route TO:
  RETURN "Route to agent-builder — agent identity is a different artifact kind."
IF caller needs routing logic with confidence thresholds AND fallback AND escalation:
  PROCEED as router
```

Deliverable: confirmed `kind: router` with one-line justification.

### Phase 3: Compose — Build the Router Artifact

Assemble frontmatter and all 5 required body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.

```
ID generation:
  id = "p02_router_" + router_slug
  must match: ^p02_router_[a-z][a-z0-9_]+$

Frontmatter (all 14 required fields from SCHEMA.md):
  id, kind (= router), pillar (= P02), title, version,
  created, updated, author, routing_domain, destinations (list),
  fallback_route, confidence_threshold (global default),
  routes_count (must match actual route table rows), quality (= null)

Body sections (in this order):

  ## Routes
  Table: pattern | destination | priority | confidence_min
  One row per route. Pattern column: keyword list, regex, or intent label.
  Destination column: exact target name from destinations list.
  Priority column: integer (1 = highest, evaluated first on tie).
  confidence_min: per-route override, or "default" if same as global.
  routes_count in frontmatter MUST equal the number of rows in this table.

  ## Decision Logic
  Prose + pseudocode describing the routing algorithm:
    1. Evaluate all patterns against incoming task
    2. Collect routes where confidence >= confidence_min
    3. If multiple matches: select highest priority; tie-break by confidence
    4. If no match above threshold: use fallback_route
    5. If ambiguous (step 3 tie unresolvable): escalate (see Escalation)

  ## Fallback
  Destination: {fallback_route}
  Trigger condition: no pattern matches above threshold
  Behavior: what the fallback destination does with unmatched tasks

  ## Escalation
  Trigger conditions: ambiguous match, persistent low confidence, destination unavailable
  Escalation path: where to route when escalation fires
  Timeout policy: how long to wait before forcing fallback

  ## Integration
  How this router connects to dispatch infrastructure:
    - Input contract: what fields the router receives per task
    - Output contract: what fields the router returns (destination, confidence, route_id)
    - Downstream: which dispatch_rules or agents consume the routing decision

Body size check: must be <= 4096 bytes.
```

Deliverable: complete `.md` file with frontmatter + 5 body sections, body <= 4096 bytes.

### Phase 4: Validate — Gate Check

Run all quality gates before delivering.

```
HARD gates (all must pass — fix before delivering):
  H01: YAML frontmatter parses without errors
  H02: id matches ^p02_router_[a-z][a-z0-9_]+$
  H03: kind == "router"
  H04: quality == null
  H05: routes_count == actual number of rows in Routes table
  H06: confidence_threshold is in range [0.0, 1.0]
  H07: fallback_route is set and is a valid destination (not blank, not null)
  H08: body <= 4096 bytes

SOFT gates (target >= 6/10):
  S01: each route has a unique, specific pattern (no duplicate patterns)
  S02: confidence_min values are differentiated by destination criticality
  S03: Decision Logic section includes explicit tie-breaking rule
  S04: Escalation section covers at least 2 distinct trigger conditions
  S05: fallback_route is different from the highest-priority route
  S06: Integration section specifies input AND output contracts
  S07: all destinations in route table are listed in frontmatter destinations field
  S08: priority values are contiguous integers starting at 1
  S09: tags include routing_domain
  S10: routes_count >= 2 (a single-route router is a dispatch_rule, not a router)

IF any HARD gate fails: fix and re-check.
IF soft_score < 6: add "Known gaps" note.
Set quality: null — never self-score.
```

---

## Output Contract

```
---
id: p02_router_{{router_slug}}
kind: router
pillar: P02
title: "{{title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
routing_domain: {{routing_domain}}
destinations: [{{destination_1}}, {{destination_2}}]
fallback_route: {{fallback_destination}}
confidence_threshold: {{0.0_to_1.0}}
routes_count: {{integer}}
quality: null
---

## Routes

| Pattern | Destination | Priority | Confidence Min |
|---|---|---|---|
| {{pattern_1}} | {{destination_1}} | 1 | {{confidence_min}} |
| {{pattern_2}} | {{destination_2}} | 2 | {{confidence_min}} |

## Decision Logic

{{routing_algorithm_pseudocode_and_prose}}

## Fallback

Destination: {{fallback_route}}
Trigger: No pattern matches above confidence threshold.
Behavior: {{what_fallback_does_with_unmatched_task}}

## Escalation

Triggers: {{ambiguous_match_conditions}}
Escalation path: {{where_to_route_on_escalation}}
Timeout: {{how_long_before_forcing_fallback}}

## Integration

Input: {{fields_router_receives}}
Output: {{destination, confidence, route_id}}
Downstream: {{dispatch_rules_or_agents_that_consume_routing_decision}}
```

---

## Validation

- [ ] All 8 HARD gates pass (H01-H08)
- [ ] Soft score >= 6/10 or "Known gaps" block present
- [ ] `routes_count` matches actual row count in Routes table (verified by counting)
- [ ] `fallback_route` is a valid, named destination — never null
- [ ] `confidence_threshold` is numeric and in [0.0, 1.0]
- [ ] Decision Logic includes tie-breaking rule
- [ ] Escalation covers at least 2 trigger conditions
- [ ] `quality: null` — never self-scored
- [ ] Body <= 4096 bytes

---

## Metacognition

**Does**
- Define where incoming tasks are routed based on pattern matching and confidence scoring
- Produce a route table with per-route confidence thresholds and priority ordering
- Specify fallback and escalation behavior for unmatched and ambiguous cases
- Validate internal consistency (routes_count, destination list, confidence range)

**Does NOT**
- Execute routing decisions (the router is a specification; a dispatcher reads and applies it)
- Define simple keyword → satellite mappings without confidence logic (dispatch-rule-builder)
- Orchestrate multi-step task execution sequences (workflow-builder)
- Define what any destination agent IS or HOW it executes (agent-builder)

**Chaining**
- Upstream: domain analysis identifies which tasks go where and what distinguishes them
- Downstream: router artifact is consumed by a dispatcher that evaluates incoming tasks at runtime
- Common pair: router (routing logic) + dispatch_rule (simple overrides) = layered routing system
