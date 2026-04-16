---
kind: knowledge_card
id: bld_knowledge_card_workflow_node
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for workflow_node production
quality: 9.2
title: "Knowledge Card Workflow Node"
version: "1.1.0"
author: n03_hybrid_review4
tags: [workflow_node, builder, knowledge_card]
tldr: "Workflow nodes are the atomic units of a DAG or state graph. Canonical references: LangGraph StateGraph, Prefect tasks, Temporal activities, Dagster ops, Airflow operators."
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
---

## Domain Overview

A workflow_node is the atomic execution unit inside a directed workflow -- a DAG (Airflow, Prefect, Dagster), a state graph (LangGraph), or a compensable activity graph (Temporal, AWS Step Functions). A node declares its inputs, outputs, side effects, retry behavior, and its successors. The orchestrator owns scheduling, state persistence, and observability; the node owns the atomic unit of work.

In modern LLM agent systems, LangGraph made the state-graph model the de facto standard: every node reads from and writes to a shared State object, and edges (including conditional edges) route control. Prior art: Airflow operators, Prefect flows/tasks, Dagster ops/assets, Temporal activities, AWS Step Functions tasks. These systems differ in state model (shared dict vs typed I/O), but share node primitives: typed in/out, retry_policy, timeout, conditional routing.

## Key Concepts

| Concept | Definition | Canonical Source |
|---------|-----------|------------------|
| Node | Atomic execution unit with typed inputs/outputs | LangGraph `StateGraph.add_node`, Airflow Operator |
| Edge | Transition from one node to the next | LangGraph `add_edge`, `add_conditional_edges` |
| State | Shared or passed-through data flowing through the graph | LangGraph State (TypedDict/Pydantic), Prefect Result |
| Retry policy | Rules for re-invoking a failed node | Prefect `retries`+`retry_delay_seconds`, Temporal RetryPolicy |
| Timeout | Hard cap on node execution time | Airflow `execution_timeout`, Temporal schedule_to_close_timeout |
| Trigger rule | Predicate deciding if a node should run given upstream status | Airflow trigger_rule (all_success, one_failed, ...) |
| Heartbeat | Long-running activity liveness signal | Temporal activity heartbeat |
| Compensation | Undo action for a failed saga | Temporal SAGA pattern, Step Functions catch/rollback |
| Cache key | Memoization key for deterministic nodes | Prefect cache_key_fn, Dagster @memoizable |
| Resource | Declared external dependency (DB conn, model client) | Dagster resource_defs, Airflow Connection |
| Fan-out / fan-in | Parallel node expansion + subsequent join | Dagster dynamic graphs, Airflow TaskGroup + dynamic task mapping |
| Human-in-the-loop | Node awaiting human input | LangGraph interrupt, Step Functions Wait for task token |

## Industry Standards

- LangGraph (LangChain) -- dominant LLM agent state-graph framework
- Prefect -- Python workflow engine (2.x flows/tasks model)
- Temporal -- durable activity + workflow execution
- Dagster -- asset-oriented data graph with typed I/O
- Apache Airflow -- DAG + Operator + XCom
- AWS Step Functions -- state machine (ASL JSON)
- Google Cloud Workflows, Azure Durable Functions -- cloud-native equivalents
- CNCF Argo Workflows -- Kubernetes-native DAG execution

## Common Patterns

1. Typed input/output contracts (Pydantic models or TypedDict) enforced at graph compile time
2. Explicit retry policy per node: max_attempts, backoff, retry_on_exception allow-list
3. Conditional edges with named predicates over current state (LangGraph pattern)
4. Long-running activities use heartbeat + activity cancellation (Temporal pattern)
5. Compensation (undo) actions paired with forward actions for SAGA-style rollback
6. Human-in-the-loop interrupt nodes that pause the graph until resumed
7. Deterministic cache keys to memoize idempotent nodes and enable replay

## Pitfalls

- Implicit state mutation -- nodes writing to shared state outside their declared state_update keys; breaks replay and causes race conditions in parallel fan-outs
- No retry_policy -- transient failures propagate as graph failures
- Long-running sync calls without timeout_s or heartbeat -- hang the whole workflow
- Missing compensation -- partial state leaks when a downstream node fails
- Over-granular nodes (one per function call) explode the DAG; under-granular nodes hide retry boundaries
- Routers without a catch-all / default edge leave state-space holes
- Cross-node dependencies via global state instead of typed outputs break local reasoning
