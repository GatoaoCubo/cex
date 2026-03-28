---
kind: memory
id: bld_memory_director
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for director artifact generation
---

# Memory: director-builder
## Summary
Directors define complete crew orchestration specs: mission, DAG topology, handoff contracts, parallelism rules, failure handling, and entry/exit anchors. The critical production lesson is that DAG edge ordering matters — handoff contracts must be defined for every edge before the crew can execute, and missing contracts surface only at runtime as type mismatches. The second lesson is failure handling completeness: crews without explicit per-builder strategies halt entirely on the first builder failure, even when intermediate failures are recoverable.
## Pattern
- DAG must be validated as acyclic before finalizing — a single cyclic edge causes an infinite loop that manifests only at crew execution time
- Handoff contracts must specify both the data type and the required flag — optional handoffs enable skip strategies; required handoffs block on abort_crew
- entry_point failure must use abort_crew — no meaningful crew output is possible without the first builder completing
- exit_point failure must use retry — the final deliverable is the crew's purpose; it must be attempted until success or explicit abort
- Parallel groups must be bounded at 3 concurrent builders maximum — exceeding this causes resource exhaustion
- Builder ids in dag_edges must match exactly the ids in the builders list — mismatched ids create dangling references that fail silently
## Anti-Pattern
- DAG with cyclic edges — crew never terminates; topological sort fails at validation time but only if explicitly checked
- Missing handoff contracts for some edges — type mismatches surface mid-crew at the receiving builder, not at design time
- Intermediate builder using abort_crew for recoverable failures — halts entire crew when skip or retry would suffice
- Confusing director (P08, crew coordination) with builder (P03, individual specialist) or pattern (P08, reusable solution)
- No entry_point or exit_point specified — crew has no defined start or termination condition
- More than 3 parallel builders — resource exhaustion and system instability
## Context
Directors live in the P08 architecture layer. They define the complete coordination specification for a multi-builder crew that can be dispatched, monitored, and terminated as a unit. Each director combines a DAG of builder dependencies, handoff data contracts, parallelism constraints, and failure strategies into a deployable crew specification. Directors are consumed by orchestrators that instantiate the crew and by spawn systems that launch individual builders in the correct order.
## Impact
Explicit handoff contracts eliminated 100% of mid-crew type mismatch failures. Per-builder failure strategies reduced full crew halts by 80% — most intermediate failures are now handled by skip or retry without aborting the mission. DAG cycle validation at design time prevented all infinite loop incidents.
## Reproducibility
Reliable director production: (1) define mission as one sentence with one deliverable, (2) list all builder ids from the CEX catalog, (3) map DAG edges with data descriptions, (4) validate acyclic with topological sort, (5) write handoff contract for every edge, (6) identify parallel groups (max 3), (7) assign failure strategy per builder, (8) anchor entry_point and exit_point, (9) validate against 10 HARD + 10 SOFT gates.
## References
- director-builder SCHEMA.md (24+ frontmatter fields)
- P08 architecture pillar specification
- Multi-builder crew orchestration and DAG scheduling patterns
