---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for workflow production
sources: CODEXA ADW system, LangGraph, Temporal, Airflow, multi-agent orchestration
---

# Domain Knowledge: workflow

## Foundational Concept
Workflows define how multiple agents coordinate to accomplish a mission. Unlike
prompt chains (text-to-text), workflows involve agent spawning, tool usage, signal
exchange, and dependency management. In CODEXA, workflows map to the ADW pattern
(Automated Directed Workflow) and are executed via STELLA dispatch.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Apache Airflow | DAG-based task orchestration with operators | Analogous: our steps with agents |
| Temporal.io | Durable workflow execution with signals | Direct: our signal-based completion |
| LangGraph | Stateful multi-agent graph execution | Similar: our mixed execution mode |
| CrewAI | Multi-agent crew coordination | Related: our crew type (P12) |
| CODEXA ADW | Automated Directed Workflows (~240 existing) | Direct: our workflow formalizes ADW |

## Key Patterns
- Wave planning: group independent steps into parallel waves, sequential between waves
- Dependency resolution: step N starts only after all depends_on steps complete
- Signal contracts: every step emits a signal on completion (see signal-builder)
- Spawn integration: each satellite step references a spawn_config
- Error boundaries: per_step retry isolates failures from healthy steps
- Timeout budgeting: workflow timeout >= sum of step timeouts (sequential) or max (parallel)
- Idempotent steps: steps should be safe to retry without side effects

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| satellites | Explicit satellite list for resource planning | Airflow pool assignment |
| spawn_configs | References to spawn parameters | Kubernetes pod specs |
| signals | Signal contract per step | Temporal signal channels |
| execution | Explicit execution mode (sequential/parallel/mixed) | Airflow trigger rules |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT workflow |
|------|------------|----------------------|
| chain (P03) | Prompt sequence (text transformations) | Chains are text-only, no agents/tools |
| dag (P12) | Dependency graph without execution | DAGs define order, workflows execute |
| crew (P12) | Agent collaboration protocol | Crews define HOW agents interact, workflows define WHEN |
| handoff (P12) | Single-satellite task instruction | Handoff is ONE task, workflow is MANY |
| dispatch_rule (P12) | Keyword-to-satellite routing | Dispatch routes, workflow orchestrates |

## References
- Apache Airflow: DAG orchestration patterns
- Temporal.io: Durable execution and signals
- LangGraph: Multi-agent stateful graphs
- CODEXA: records/pool/workflows/ADW_*.md (~240 implicit workflows)
