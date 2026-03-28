---
kind: knowledge_card
id: bld_knowledge_card_director
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for director artifact production — atomic searchable facts
sources: director-builder MANIFEST.md + SCHEMA.md, multi-agent orchestration, DAG scheduling
---

# Domain Knowledge: director
## Executive Summary
Directors define the coordination layer for multi-builder crews — each director declares one mission outcome, the DAG of participating builders, handoff contracts between connected pairs, parallelism rules, and failure handling. Each director owns ONE mission with a named entry point and exit point. They differ from builders (individual specialists), satellite_specs (autonomous satellite definitions), patterns (abstract reusable solutions), and spawn configs (runtime launch parameters) by being the complete orchestration specification of how a crew of builders works together to produce a single deliverable.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Kind | `director` (exact literal) |
| ID pattern | `p08_dir_{slug}` |
| Required frontmatter | 24+ fields |
| Quality gates | 10 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | mission, entry_point, exit_point, builders, dag_edges, handoff_contracts |
| Parallelism limit | Max 3 concurrent builders + orchestrator (BSOD at >4) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Single mission ownership | Each director owns ONE mission outcome; no multi-mission directors |
| DAG over sequence | Model dependencies as a directed graph; enables parallelism discovery |
| Explicit handoff contracts | Every dag_edge has a named data type; no implicit passing |
| Entry/exit anchoring | Every director has exactly one entry_point and one exit_point |
| Fail-forward by default | Intermediate builders use skip or retry; only entry_point uses abort_crew |
| Explicit dependencies | No hidden couplings between builders in the crew |
| Signal-based completion | Exit_point emits completion signal enabling autonomous recovery |
| Acyclic graph validation | Topological sort must succeed; any cycle is a design defect |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Multi-mission director | Violates single-mission principle; creates coordination ambiguity |
| Missing handoff contracts | Type mismatches surface only at runtime; hard to diagnose |
| Cyclic DAG edges | Creates infinite loops; crew never terminates |
| No entry or exit anchor | Crew cannot be started or terminated reliably |
| Implicit parallelism | Unspecified concurrency causes resource conflicts and race conditions |
| > 3 parallel builders | Resource exhaustion; system instability (BSOD risk) |
| abort_crew for intermediate builders | Halts crew for recoverable failures; prefer skip or retry |
| Missing failure handling | Single builder failure cascades to full crew halt |
## Application
1. Define mission outcome (ONE deliverable, one sentence)
2. List all participating builder ids from the CEX catalog
3. Map DAG edges with explicit data descriptions (no implicit passing)
4. Validate DAG is acyclic (topological sort)
5. Define handoff contract for each dag_edge (type, required flag)
6. Identify parallel groups and forced sequences
7. Assign failure strategy per builder (abort_crew for entry, retry for exit, skip/retry for intermediate)
8. Set entry_point (no incoming edges) and exit_point (no outgoing edges)
9. Validate: 10 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- director-builder SCHEMA.md v1.0.0
- P08 architecture pillar specification
- Airflow DAG scheduling patterns (Apache Software Foundation)
- Wooldridge, Michael. Introduction to MultiAgent Systems (2009)
