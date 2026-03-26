---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: mental-model-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Setting pillar to P10 instead of P02 (P10 is runtime state, P02 is design-time)
3. Using hyphens in id slug (must be underscores: p02_mm_my_agent not p02_mm_my-agent)
4. routing_rules as string instead of structured object list (H08 requires objects)
5. decision_tree as prose instead of condition/then/else objects (H09 requires structure)
6. Vague keywords ("general", "anything", "all tasks") instead of specific terms (S12)
7. Fewer than 3 routing rules (H08 minimum)
8. Circular decision tree references (condition A -> B -> A)
9. Missing domain_map.routes_to (only covers without delegation targets)
10. Personality traits inconsistent (direct tone + verbose = contradiction)

### Cognitive Design Patterns
- Routing confidence bands: 0.8+ direct, 0.5-0.8 tentative, <0.5 fallback
- Priority cap: max 5-7 items (Miller's law — beyond 7 humans lose track)
- Heuristic format: "when X, prefer Y because Z" — always give the WHY
- Domain map symmetry: every routes_to target should be a real agent or [PLANNED]
- Decision tree max depth: 3 levels — deeper = harder to maintain
- Fallback rule: always define escalate_to — never let requests silently drop

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | P02/P10 confusion, vague keywords, string-vs-object |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a mental_model, update:
- New common mistake (if encountered)
- New cognitive design pattern (if discovered)
- Production counter increment
