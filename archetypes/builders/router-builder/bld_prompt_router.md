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
  - "Routing domain is identified (e.g. task-to-agent_group, intent-to-agent, request-to-service)"
  - "All possible destination targets are enumerated (agent_groups, agents, or services)"
  - "Patterns or signals that distinguish each destination are known or inferable"
validation_method: checklist
domain: router
quality: 9.1
tags: [instruction, router, P02, routing, dispatch, route-table]
idempotent: true
atomic: false
rollback: "Delete the produced router file. No routing behavior changes until the router is wired to a dispatcher."
dependencies: []
logging: true
tldr: "Build a route table with patterns, confidence thresholds, fallback, and escalation logic for task-to-destination dispatch."
density_score: 0.91
llm_function: REASON
related:
  - bld_collaboration_router
  - bld_knowledge_card_router
  - bld_memory_router
  - p03_sp_router_builder
  - p11_qg_router
  - router-builder
  - bld_architecture_router
  - bld_schema_router
  - bld_examples_router
  - bld_config_router
---
## Context
A **router** artifact defines task-to-destination routing logic: given an incoming task, which agent_group, agent, or service should handle it? It contains a route table (pattern → destination mappings), confidence thresholds per route, a fallback destination for unmatched tasks, and an escalation policy for ambiguous matches.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `routing_domain` | string | Category of tasks being routed (e.g. `agent_group_task_routing`, `intent_dispatch`) |
| `destinations` | list | All valid routing targets (agent_group names, agent IDs, or service endpoints) |
| `patterns` | list | Signals that distinguish each destination (keywords, regex, intent labels) |
| `confidence_threshold` | float | Default minimum confidence to commit to a route (0.0–1.0, default 0.7) |
| `fallback_route` | string | Destination for tasks that match no route |
**Output**
A single `.md` file with YAML frontmatter (14 required fields) + body containing: Routes table, Decision Logic, Fallback section, Escalation section, Integration section. Body must be <= 4096 bytes.
**Boundary rules**
- router = full routing logic with confidence thresholds, fallback, escalation (this builder)
- dispatch_rule = simple keyword-to-agent_group mapping without confidence scoring (different builder)
- workflow = multi-step orchestration sequence (different builder)
- agent = identity definition for a single specialized executor (different builder)
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
Generate router_slug: snake_case, lowercase, no hyphens (e.g. agent_group_task_router)
```
Deliverable: route map with patterns, confidence thresholds, priority, and fallback identified.
### Phase 2: Classify — Boundary Check
Confirm the artifact belongs to `router` and not a sibling kind.
```
IF caller needs only a simple keyword → agent_group table with no confidence scoring:
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


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_router]] | related | 0.58 |
| [[bld_knowledge_card_router]] | related | 0.56 |
| [[bld_memory_router]] | downstream | 0.55 |
| [[p03_sp_router_builder]] | downstream | 0.55 |
| [[p11_qg_router]] | downstream | 0.52 |
| [[router-builder]] | related | 0.50 |
| [[bld_architecture_router]] | downstream | 0.50 |
| [[bld_schema_router]] | downstream | 0.49 |
| [[bld_examples_router]] | downstream | 0.45 |
| [[bld_config_router]] | downstream | 0.39 |
