---
pillar: P10
llm_function: INJECT
purpose: Standards and domain knowledge for learning_record production
sources: experiential learning theory, retrospective patterns, CEX memory system
---

# Domain Knowledge: learning_record

## Core Concept

Learning records capture what worked/failed from concrete experience. Unlike KCs (external facts), LRs are INTERNAL — emerging from system operation. Pipeline: `EXPERIENCE -> OBSERVATION -> PATTERN -> EVIDENCE -> CONFIDENCE`

## Four Required Elements

| Element | What | Good Example | Bad Example |
|---------|------|-------------|-------------|
| Observation | Raw facts, no judgment | "3 requests each triggered /auth/refresh" | "Auth had problems" |
| Pattern | Reproducible rule | "Mutex: `if (_refreshPromise) return`" | "Handle gracefully" |
| Evidence | Metrics, before/after | "Before: 3/5 failed. After: 0/50" | "Seemed better" |
| Confidence | 0.0-1.0 trust score | Based on observation count | Arbitrary number |

## Confidence Scale

| Score | Meaning | Basis |
|-------|---------|-------|
| 0.9-1.0 | Near-certain | 10+ observations, consistent |
| 0.7-0.8 | High | 5-9 observations |
| 0.5-0.6 | Moderate | 2-4 observations |
| 0.3-0.4 | Low | 1 observation |
| 0.0-0.2 | Speculative | Theoretical only |

Increases with: frequency, recency, consistency. Decreases with: time, contradictions, narrow context.

## Entity Tracking

- One entity = one identifiable component (tool, service, agent)
- Facts are append-only with timestamp + content hash for dedup
- Entity files = single source of truth for that subject

```yaml
entity: TOOL_NAME
facts:
  - {id: 1, relation: performance_metric, value: "p95: 800ms->120ms", hash: "273ecac786c2"}
```

## Semantic Links

| Relation | Meaning | Example |
|----------|---------|---------|
| depends_on | A requires B | auth_refresh depends_on jwt_validation |
| enables | A makes B possible | connection_pooling enables high_throughput |
| contradicts | A and B conflict | eager_loading contradicts lazy_init |
| refines | A specializes B | mutex_refresh refines token_management |
| caused_by | A is effect of B | thundering_herd caused_by concurrent_refresh |

Rules: bidirectionally meaningful, no orphans, contradictions are most valuable.

## Memory Decay

```
effective_confidence = base_confidence * exp(-decay_rate * days_since_last_use)
```

| Decay Rate | Half-Life | Use Case |
|-----------|-----------|----------|
| 0.01 | ~69 days | Stable infra patterns |
| 0.03 | ~23 days | API behaviors, lib versions |
| 0.05 | ~14 days | Market data, pricing |
| 0.10 | ~7 days | Ephemeral config, session state |

Refresh: successful re-application resets `last_used` + boosts confidence. Failed = -0.1 to -0.2.

## Outcome Classification

| Outcome | When | Score Range |
|---------|------|-------------|
| SUCCESS | Reliable result | 7.0-10.0 |
| PARTIAL | Worked with caveats | 5.0-6.9 |
| FAILURE | Did not achieve result | 0.0-4.9 |

## Body: 7 Required Sections

Summary, Pattern, Anti-Pattern, Context, Impact, Reproducibility, References.

## Writing Rules

- Lead with result: "SUCCESS (9.0): Mutex eliminated 100% of failures"
- Both sides always: every pattern has a failure mode
- Quantify: time, errors, quality scores, cost deltas

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| No evidence | Add metrics, before/after |
| Vague pattern | Specific mechanism: tool, config, code |
| Missing outcome | Always set SUCCESS/PARTIAL/FAILURE |
| No timestamp | ISO 8601 on every record |
| Confidence without basis | Score must reflect evidence quantity |

## Boundary

| Type | NOT a learning record because |
|------|------------------------------|
| Knowledge card | Comes from research, not experience |
| Session state | Ephemeral, dies with session |
| Mental model | Decides routing, doesn't record outcomes |
| Axiom | Immutable; LR evolves with evidence |

## Self-Improvement

- Score >= 9.0: promote pattern to shared pool
- Score < 7.0: add anti-pattern to failure registry
- 3+ successes: solidify (increase confidence, reduce decay)
