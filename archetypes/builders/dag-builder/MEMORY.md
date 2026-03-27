---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries recurring DAG patterns
---

# Memory: dag-builder

## Recurrent Patterns
- Most useful DAGs include `execution_order` for immediate scheduling
- `critical_path` helps estimate total duration
- Fan-out patterns (1 node -> N parallel nodes) are common in CODEXA missions
- Fan-in patterns (N nodes -> 1 review node) ensure quality gates

## Common Mistakes
1. Creating cycles (A -> B -> A)
2. Referencing non-existent node ids in edges
3. Including runtime execution logic (belongs in workflow)
4. Using `steps` instead of `nodes` + `edges` graph structure
5. Forgetting to compute `execution_order` from the graph

## State Between Sessions
This builder is stateless per invocation.
After production, update only if a new recurring graph pattern or
constraint becomes stable across multiple DAG artifacts.
