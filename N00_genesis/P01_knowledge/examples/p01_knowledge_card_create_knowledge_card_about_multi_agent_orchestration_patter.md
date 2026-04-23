---
id: p01_kc_multi_agent_orchestration_patterns
kind: knowledge_card
pillar: P01
title: "Multi-Agent Orchestration Patterns for Distributed AI Systems"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: multi_agent_systems
quality: 9.1
tags: [multi-agent, orchestration, coordination, distributed-systems, knowledge]
tldr: "Multi-agent orchestration uses 4 core patterns: hierarchical (coordinator-worker), peer-to-peer (consensus), pipeline (sequential), and marketplace (auction-based)"
when_to_use: "When designing systems with multiple autonomous AI agents that need coordination"
keywords: [multi-agent, orchestration, coordination, consensus, hierarchical]
long_tails:
  - How to implement hierarchical multi-agent coordination
  - Peer-to-peer consensus mechanisms for AI agent systems
  - Task distribution strategies in multi-agent orchestration
axioms:
  - ALWAYS define clear agent roles and responsibilities before orchestration
  - NEVER allow circular dependencies in hierarchical orchestration
  - IF agents share state THEN implement conflict resolution protocols
linked_artifacts:
  primary: null
  related: [p01_kc_distributed_systems_patterns]
density_score: 0.87
data_source: "Multi-agent systems research, distributed computing patterns"
related:
  - kc_n07_orchestrator
  - bld_memory_collaboration_pattern
  - collaboration-pattern-builder
  - bld_knowledge_card_collaboration_pattern
  - p03_sp_collaboration_pattern_builder
  - p01_kc_agent
  - kc_collaboration_pattern
  - bld_collaboration_agent
  - agent-builder
  - p01_kc_coordination
---
# Multi-Agent Orchestration Patterns for Distributed AI Systems

## Quick Reference
```yaml
topic: multi_agent_orchestration
scope: coordination patterns for autonomous AI agents
owner: system_architect
criticality: high
```

## Key Concepts
- **Hierarchical Pattern**: coordinator assigns tasks, workers execute, results aggregate up
- **Peer-to-Peer Pattern**: agents negotiate directly, consensus via voting/blockchain
- **Pipeline Pattern**: sequential processing, agent N+1 receives output from agent N
- **Marketplace Pattern**: auction-based task assignment, agents bid on work packages
- **Publish-Subscribe**: event-driven coordination via message bus/topic routing
- **Circuit Breaker**: fault tolerance mechanism stopping cascading agent failures

## Strategy Phases
1. **Role Definition**: assign agent capabilities, input/output contracts, authority levels
2. **Communication Protocol**: select message format (JSON-RPC, gRPC, REST), routing topology
3. **Task Distribution**: implement work assignment (round-robin, load-based, capability-matching)
4. **State Management**: define shared state scope, conflict resolution, eventual consistency
5. **Monitoring**: track agent health, task completion rates, bottleneck identification
6. **Fault Recovery**: implement retries, failover, graceful degradation strategies

## Golden Rules
- COORDINATOR agents never execute business logic, only orchestrate
- WORKER agents report status every 30-60 seconds during long tasks
- IMPLEMENT timeout mechanisms for all inter-agent communications
- PARTITION work to minimize cross-agent data dependencies
- DESIGN for partial failures - some agents down, system continues

## Flow
```text
[Task Request] -> [Coordinator] -> [Work Distribution]
                       |              |
                 [Health Check] -> [Agent Pool] -> [Results]
                       |              |
                 [Load Balance] <- [Status Updates]
```

## Comparativo
| Pattern | Coordination | Fault Tolerance | Scalability | Use Case |
|---------|-------------|----------------|-------------|----------|
| Hierarchical | Centralized | Single point failure | Vertical | Command-control systems |
| Peer-to-Peer | Distributed | High resilience | Horizontal | Blockchain, consensus |
| Pipeline | Sequential | Chain failure risk | Limited | Data processing flows |
| Marketplace | Economic | Market-driven | High | Resource allocation |
| Pub-Sub | Event-driven | Topic-based isolation | Very high | Real-time systems |

## References
- Related: Distributed systems consensus algorithms (Raft, PBFT)
- Source: "Multi-Agent Systems: Algorithmic, Game-Theoretic Foundations" (Shoham & Leyton-Brown)
- Implementation: Actor model patterns, microservices orchestration

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_n07_orchestrator]] | sibling | 0.35 |
| [[bld_memory_collaboration_pattern]] | downstream | 0.34 |
| [[collaboration-pattern-builder]] | downstream | 0.31 |
| [[bld_knowledge_card_collaboration_pattern]] | sibling | 0.30 |
| [[p03_sp_collaboration_pattern_builder]] | downstream | 0.28 |
| [[p01_kc_agent]] | sibling | 0.28 |
| [[kc_collaboration_pattern]] | sibling | 0.28 |
| [[bld_collaboration_agent]] | downstream | 0.28 |
| [[agent-builder]] | downstream | 0.26 |
| [[p01_kc_coordination]] | sibling | 0.25 |
