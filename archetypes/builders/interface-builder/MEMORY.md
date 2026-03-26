---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: interface-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p06_iface_brain_search, not p06_iface_brain-search)
3. Writing methods as a string instead of list[object] (must be structured objects)
4. Forgetting provider or consumer field (both required — bilateral contract)
5. Using backward_compatible as string ("yes") instead of boolean (true/false)
6. Defining only input OR output for a method (both required)
7. Writing mock payloads that don't match the method signatures
8. Drifting into runtime behavior — adding event handling (that is signal P12)

### Interface Patterns

| Pattern | When to use | Complexity |
|---------|-------------|------------|
| Query-response | Consumer asks, provider answers | Simple |
| Command-acknowledge | Consumer commands, provider confirms | Simple |
| Data pipeline | Provider streams, consumer processes | Medium |
| Bidirectional | Both parties send and receive | Complex |
| Versioned migration | Old methods deprecated, new methods added | Medium |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | method typing, bilateral vs unilateral confusion |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an interface, update:
- New common mistake (if encountered)
- New interface pattern (if discovered)
- Production counter increment
