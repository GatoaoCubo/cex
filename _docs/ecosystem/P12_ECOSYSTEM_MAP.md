# P12 Orchestration — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| LangGraph | Stateful agent graphs | StateGraph, nodes, conditional edges, checkpoints, threads, human-in-the-loop (interrupt_before/after), subgraphs, Command pattern, Send API (map-reduce) |
| Temporal | Workflow orchestration | Workflows, activities, signals, queries, timers, sagas (compensations), child workflows, schedules, task queues, worker pools, visibility |
| Prefect | Data orchestration | Flows, tasks, deployments, blocks, artifacts, work pools, concurrency limits, retries, caching, result persistence |
| Airflow | DAG scheduling | DAGs, operators, sensors, hooks, XCom (cross-task data), pools, queues, trigger rules, SLAs, datasets, dynamic task mapping |
| Dagster | Asset orchestration | Software-defined assets, ops, graphs, jobs, schedules, sensors, partitions, IO managers, resources, asset lineage |
| CrewAI | Multi-agent crews | Crews, agents, tasks, processes (sequential/hierarchical/consensual), tools, delegation, memory, callbacks, kickoff |
| AutoGen | Conversational agents | GroupChat, ConversableAgent, UserProxyAgent, AssistantAgent, nested chats, function calling, code execution, chat termination |
| DSPy | Programmatic LLM | Programs, modules (ChainOfThought, ReAct, ProgramOfThought), signatures, optimizers (BootstrapFewShot, MIPROv2), assertions, metrics |
| A2A Protocol | Agent interop | Agent Card, Task (lifecycle: submitted/working/completed/failed), Message, Artifact, Streaming (SSE), push notifications, capability discovery |
| MCP (Model Context Protocol) | Tool integration | Resources, tools, prompts, sampling, roots, transports (stdio/SSE), server/client, capability negotiation |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Workflow / Flow | LangGraph (StateGraph), Temporal (Workflow), Prefect (Flow), Airflow (DAG), Dagster (Job/Graph), CrewAI (sequential/hierarchical process) | Directed sequence of steps with control flow (conditional, parallel, loop) | 6 |
| DAG / Dependency Graph | Airflow (DAG), Dagster (asset lineage, graph), Prefect (task dependencies), LangGraph (graph edges), Temporal (child workflow deps) | Acyclic graph of task dependencies determining execution order | 5 |
| Signal / Event | Temporal (signals), LangGraph (interrupt/Command), Airflow (sensors, datasets), Dagster (sensors), A2A (push notifications), MCP (notifications) | Asynchronous message between agents/workflows to trigger state transitions | 6 |
| Handoff / Delegation | CrewAI (delegation), AutoGen (nested chats), LangGraph (subgraphs + Send), A2A (Task submission), Temporal (child workflows) | Transferring a task from one agent/workflow to another with context | 5 |
| Dispatch / Routing Rule | CrewAI (process selection), LangGraph (conditional edges), Airflow (trigger rules), Dagster (sensors), AutoGen (GroupChat speaker selection) | Rule determining which agent/node handles a task based on conditions | 5 |
| Spawn / Worker Config | Temporal (worker pools, task queues), Prefect (work pools, deployments), Airflow (pools, queues, executors), CrewAI (crew config), Dagster (resources) | Configuration for launching and managing execution workers/agents | 5 |
| Checkpoint / State Snapshot | LangGraph (checkpoints, thread_ts), Temporal (workflow history, event sourcing), Prefect (result persistence), Dagster (IO managers) | Persisted snapshot of execution state for resume, replay, or debugging | 4 |
| Schedule / Trigger | Temporal (schedules), Airflow (timetable, dataset triggers), Dagster (schedules, sensors), Prefect (deployments with schedule) | Time-based or event-based trigger that initiates workflow execution | 4 |
| Agent Protocol / Interface | A2A (Agent Card, capability discovery), MCP (capability negotiation, tool schema), AutoGen (ConversableAgent interface), DSPy (Signature) | Standardized contract for how agents declare capabilities and communicate | 4 |
| Compensation / Rollback | Temporal (sagas, compensation), Airflow (on_failure_callback), Prefect (on_failure hooks), LangGraph (human-in-the-loop reject) | Undo or compensating action when a workflow step fails, maintaining consistency | 3 |
| Artifact / Output | A2A (Artifact), Prefect (artifacts), Dagster (software-defined assets), Airflow (XCom), DSPy (output fields) | Named, typed output produced by a workflow step, available to downstream consumers | 5 |
| Concurrency / Pool | Temporal (task queues), Airflow (pools), Prefect (concurrency limits), Dagster (concurrency config), CrewAI (max_rpm) | Limits on parallel execution to manage resources and prevent overload | 5 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| workflow | Workflow / Flow | 90% | Excellent match. CEX workflows (sequential/parallel steps) align with LangGraph StateGraph, Temporal Workflows, Prefect Flows. Gap: industry workflows support conditional branching (LangGraph conditional edges) and loop constructs more explicitly. |
| dag | DAG / Dependency Graph | 85% | Strong match to Airflow DAGs and Dagster asset lineage. Gap: industry DAGs support dynamic task mapping (Airflow) and partition-based execution (Dagster). CEX dag is static. |
| spawn_config | Spawn / Worker Config | 85% | Good match to Temporal worker pools, Prefect work pools, Airflow executors. Gap: industry configs include resource limits (CPU/memory), autoscaling rules, and worker heartbeat/health checks. |
| signal | Signal / Event | 80% | Good match to Temporal signals and LangGraph interrupts. Gap: industry signals support typed payloads with schemas (Temporal), bidirectional queries (Temporal queries), and subscription patterns (A2A push notifications). CEX signals are simple complete/error/progress. |
| handoff | Handoff / Delegation | 90% | Excellent match. CEX handoff (task+context+commit) is richer than most industry equivalents. CrewAI delegation and A2A Task submission are the closest parallels. CEX is actually ahead here with its structured commit protocol. |
| dispatch_rule | Dispatch / Routing Rule | 80% | Good match to LangGraph conditional edges and CrewAI process selection. Gap: industry dispatch supports dynamic routing based on runtime state (LangGraph state-based conditions), not just keyword matching. CEX dispatch_rule is keyword-only. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| checkpoint | Persistent snapshots of orchestration state for resume, replay, and debugging. Distinct from signal (event notification) and session_state in P10 (ephemeral conversation state). A checkpoint captures the full execution graph state at a point in time, enabling workflow recovery after failures. CEX currently has no way to snapshot and resume multi-step workflows. | LangGraph (checkpoints, thread_ts), Temporal (workflow history, event sourcing), Prefect (result persistence), Dagster (IO managers) | high |
| schedule | Time-based or event-based triggers that initiate workflow execution. Distinct from dispatch_rule (routes tasks, doesn't create them) and spawn_config (configures HOW to launch, not WHEN). Industry universally separates "when to run" from "how to run". CEX currently has no declarative scheduling kind. | Temporal (schedules), Airflow (timetable, dataset triggers), Dagster (schedules + sensors), Prefect (deployment schedules) | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| signal | KEEP (expand payload types) | Industry signals carry typed payloads with schemas. CEX should expand beyond simple complete/error/progress to support arbitrary structured payloads. Consider adding optional `payload_schema` field. |
| dispatch_rule | KEEP (add state-based routing) | Industry dispatch increasingly uses runtime state (LangGraph conditional edges) not just keywords. Consider allowing dispatch rules to reference runtime_state (P10) values as conditions, not only keyword matches. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| workflow | LangGraph StateGraph, Temporal Workflows, Prefect Flows, Airflow DAGs (execution layer), Dagster Jobs, CrewAI sequential/hierarchical process |
| dag | Airflow DAGs, Dagster asset lineage/graphs, Prefect task dependency graph, LangGraph graph structure |
| spawn_config | Temporal worker pools/task queues, Prefect work pools/deployments, Airflow pools/executors/queues, CrewAI crew config, Dagster resources |
| signal | Temporal signals/queries, LangGraph interrupts/Command, Airflow sensors/datasets, Dagster sensors, A2A push notifications, MCP notifications |
| handoff | CrewAI delegation, AutoGen nested chats, LangGraph subgraph Send, A2A Task submission, Temporal child workflows |
| dispatch_rule | LangGraph conditional edges, CrewAI process selection, Airflow trigger rules, Dagster sensor-based routing, AutoGen GroupChat speaker selection |

## 7. Summary
Current: 6 kinds → Proposed: 8 kinds (+checkpoint, +schedule) | Coverage: ~85% → ~93%

Key insight: CEX's orchestration pillar is the most mature of the five audited — all 6 existing kinds map cleanly to industry concepts, and the handoff kind is actually **ahead of industry** with its structured commit protocol. The two gaps are both infrastructure-level: **checkpoints** (every serious orchestration framework supports resume/replay — Temporal and LangGraph make it a core primitive) and **schedules** (the "when to run" dimension is universally separated from "how to run" and "what to route"). Adding these completes the orchestration lifecycle: schedule (WHEN) → dispatch_rule (WHERE) → spawn_config (HOW) → workflow (WHAT) → signal (STATUS) → checkpoint (SAVE) → handoff (DELEGATE).
