---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: router-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p02_router_my_router not p02_router_my-router)
3. routes_count not matching actual rows in Routes table (H07 catches this)
4. Omitting fallback_route or setting to empty string (must be concrete destination)
5. confidence_threshold outside 0.0-1.0 range or omitted entirely
6. Creating 1-route routers (that is a dispatch_rule, not a router)
7. Including execution logic ("then run the agent") — router only DECIDES destination
8. Generic patterns like "all tasks" or "everything else" — each route needs specific patterns
9. Missing Decision Logic section — describing HOW routing works is mandatory
10. Confusing router (P02, decision logic) with dispatch_rule (P12, keyword map)

### Routing Domain Patterns
| Domain | Typical Routes | Complexity |
|--------|---------------|------------|
| satellite_dispatch | 5-7 routes by task domain | MEDIUM |
| model_selection | 3-5 routes by task complexity | MEDIUM |
| api_gateway | 10+ routes by endpoint pattern | COMPLEX |
| fallback_selection | 2-3 routes by quality requirement | SIMPLE |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | routes_count mismatch, missing fallback, boundary drift to dispatch_rule |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a router artifact, update:
- New common mistake (if encountered)
- New routing domain pattern (if discovered)
- Production counter increment
