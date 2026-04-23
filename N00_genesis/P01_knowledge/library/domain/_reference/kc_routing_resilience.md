---
id: p01_kc_routing_resilience
kind: knowledge_card
type: domain
pillar: P01
title: "Routing & Resilience — Intent Routers, Fallback Chains, Dispatch Rules"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: routing
origin: manual
quality: 9.1
tags: [router, fallback, dispatch, resilience, intent, routing, priority, cascade, cost-aware]
tldr: "Routing and resilience patterns ensure agent requests reach the right handler via intent classification, fallback cascades, and cost-aware dispatch rules"
when_to_use: "Building or classifying components that route requests, handle failures, or manage dispatch priorities"
keywords: [router, fallback_chain, dispatch_rule, intent, cascade, priority, cost-aware]
long_tails:
  - "How to map semantic intent routers to CEX router kind"
  - "Which fallback cascade patterns map to CEX fallback_chain kind"
  - "How cost-aware dispatch rules work in multi-model agent systems"
axioms:
  - "Every request must have a fallback path — silent failures are never acceptable"
  - "Routing decisions should be transparent and loggable for debugging"
  - "Cost-aware dispatch balances quality vs budget — cheap models for simple tasks, expensive for complex"
linked_artifacts:
  primary: null
  related: [p01_kc_agent_identity, p01_kc_langchain_patterns, p01_kc_external_integrations]
feeds_kinds:
  - router           # Intent classifiers, semantic routers, keyword matchers
  - fallback_chain   # Cascading failure handlers, retry strategies, degraded modes
  - dispatch_rule    # Priority queues, cost-aware routing, agent_group assignment rules
density_score: 0.85
related:
  - router-builder
  - p01_kc_router
  - bld_architecture_dispatch_rule
  - bld_collaboration_router
  - dispatch-rule-builder
  - bld_architecture_router
  - bld_collaboration_dispatch_rule
  - p01_kc_dispatch_rule
  - p03_sp_router_builder
  - p01_kc_fallback_chain
---

# Routing & Resilience

## Quick Reference
```yaml
topic: Request Routing & Failure Resilience Patterns
scope: Intent routers, fallback chains, dispatch rules, priority queues
source: cross-domain (agent frameworks, distributed systems, organization dispatch)
criticality: high
```

## Key Concepts

| Concept | Category | CEX Kind | Role |
|---------|----------|----------|------|
| Semantic Router | Intent | router | Embedding-based intent classification to handler |
| Keyword Router | Intent | router | Pattern/regex matching for fast routing |
| LLM-as-Router | Intent | router | Use LLM to classify intent and select handler |
| Confidence Gate | Intent | router | Route only when confidence > threshold, else fallback |
| Retry Strategy | Failure | fallback_chain | Exponential backoff with jitter on transient errors |
| Model Cascade | Failure | fallback_chain | Try opus -> sonnet -> haiku on failure or budget |
| Degraded Mode | Failure | fallback_chain | Return cached/partial result when all retries exhaust |
| Circuit Breaker | Failure | fallback_chain | Stop calling failing service after N consecutive errors |
| Priority Queue | Dispatch | dispatch_rule | Ordered task execution by urgency/importance |
| Cost-Aware Router | Dispatch | dispatch_rule | Route to cheapest model that meets quality threshold |
| Agent_group Assignment | Dispatch | dispatch_rule | Map task domain to agent_group (research_agent=research, builder_agent=build) |
| Rate Limiter | Dispatch | dispatch_rule | Token/request budget enforcement per time window |
| Load Balancer | Dispatch | dispatch_rule | Distribute requests across equivalent handlers |
| Dependency Resolver | Dispatch | dispatch_rule | Topological sort of tasks before dispatch |

## Patterns

| Trigger | Action |
|---------|--------|
| Classify user intent | Embed query -> cosine similarity against intent vectors -> route to top match |
| Route with LLM | Prompt LLM with intent options + task description -> parse selected handler |
| Handle transient failure | Retry with exponential backoff (base=1s, max=30s, jitter=random) |
| Cascade across models | Try primary model -> on failure/timeout, try secondary -> then tertiary |
| Enforce budget | Track cumulative cost -> if approaching limit, downgrade model tier |
| Dispatch to agent_group | Match keywords against routing table -> assign to agent_group -> write handoff |
| Break circuit | After 5 consecutive failures, open circuit for 60s -> half-open probe -> close if success |

## Anti-Patterns

- Routing without fallback (single point of failure)
- Using expensive models (opus) for simple classification tasks
- Retrying non-idempotent operations without deduplication
- Hardcoding routing tables instead of configuration-driven dispatch
- Ignoring circuit breaker state (hammering a down service)
- Routing based solely on keywords without semantic understanding

## CEX Mapping

```text
[router: classify intent] -> [dispatch_rule: select handler + model]
    -> [execute] -> success
    -> [fallback_chain: retry/cascade/degrade] -> partial_success | escalate
```

## References

- source: Circuit Breaker (Nygard), Semantic Router (aurelio-labs), organization orchestrator dispatch
- related: p01_kc_agent_identity, p01_kc_external_integrations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[router-builder]] | downstream | 0.44 |
| [[p01_kc_router]] | sibling | 0.42 |
| [[bld_architecture_dispatch_rule]] | downstream | 0.38 |
| [[bld_collaboration_router]] | downstream | 0.38 |
| [[dispatch-rule-builder]] | downstream | 0.37 |
| [[bld_architecture_router]] | downstream | 0.36 |
| [[bld_collaboration_dispatch_rule]] | downstream | 0.35 |
| [[p01_kc_dispatch_rule]] | sibling | 0.34 |
| [[p03_sp_router_builder]] | downstream | 0.32 |
| [[p01_kc_fallback_chain]] | sibling | 0.31 |
