---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: workflow-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p12_wf_my_flow not p12_wf_my-flow)
3. steps_count not matching actual numbered steps in body (H08 catches mismatch)
4. Including prompt chaining in workflow steps (belongs in chain, P03)
5. Missing signal definitions per step (each step should emit a signal)
6. Steps without agent assignment (every step needs an explicit agent)
7. Circular dependencies between steps (must be acyclic)
8. Timeout too short for parallel workflows (should be max of parallel steps, not sum)

### Workflow Patterns

| Pattern | Execution | Satellites | Use case |
|---------|-----------|------------|----------|
| Research-Build | sequential | shaka -> edison | Feature development |
| Multi-Research | parallel | shaka, lily, pytha | Broad intelligence gathering |
| Research-Build-Deploy | mixed | shaka -> edison -> atlas | Full lifecycle |
| Content Factory | mixed | shaka -> lily + york | Content production |
| Review Chain | sequential | edison -> atlas | Code review + validation |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | chain vs workflow boundary, dependency ordering, signal contracts |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a workflow, update:
- New common mistake (if encountered)
- New workflow pattern (if discovered)
- Production counter increment
