---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of router — inventory, dependencies, and architectural position
---

# Architecture: router in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 14-field metadata header (id, kind, pillar, domain, routes_count, etc.) | router-builder | active |
| route_table | Ordered list of routes with pattern, destination, and priority | author | active |
| confidence_thresholds | Minimum confidence levels required for route activation | author | active |
| fallback_routes | Default destinations when no pattern matches above threshold | author | active |
| escalation_policy | What happens when routing fails or confidence is too low | author | active |
| load_balancing | Distribution strategy across destinations when multiple match | author | active |
| timeout_policy | Maximum time allowed for route resolution before fallback | author | active |

## Dependency Graph

```
incoming_task   --routed_by-->   router  --dispatches_to-->  satellite/agent
mental_model    --configures-->  router  --signals-->        routing_decision
router          --depends-->     dispatch_rule
```

| From | To | Type | Data |
|------|----|------|------|
| incoming_task | router | data_flow | task description and metadata for pattern matching |
| mental_model (P02) | router | data_flow | routing rules and decision trees informing route table |
| router | satellite/agent (P02) | produces | task dispatched to matched destination |
| router | routing_decision (P12) | signals | emitted with route, confidence, and fallback status |
| dispatch_rule (P12) | router | dependency | simple keyword mappings referenced by router |
| router | escalation_policy | data_flow | unmatched tasks escalated per policy |

## Boundary Table

| router IS | router IS NOT |
|-----------|---------------|
| A routing logic with route tables, confidence, and fallback | A simple keyword-to-destination mapping (dispatch_rule P12) |
| Pattern-based matching with priority ordering | A multi-step execution sequence (workflow P12) |
| Includes fallback routes and escalation for unmatched tasks | An agent identity with capabilities (agent P02) |
| Configured with confidence thresholds per route | A design-time cognitive map (mental_model P02) |
| Supports load balancing across multiple destinations | A static configuration of one destination |
| Produces routing decisions as observable signals | A silent dispatch without audit trail |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Input | incoming_task, mental_model | Supply task data and routing intelligence |
| Matching | route_table, confidence_thresholds | Pattern matching with confidence evaluation |
| Resolution | load_balancing, timeout_policy | Resolve ties and enforce time limits |
| Fallback | fallback_routes, escalation_policy | Handle unmatched or low-confidence tasks |
| Output | satellite/agent, routing_decision | Dispatch task and signal the routing result |
