---
pillar: P10
llm_function: INJECT
purpose: Standards and domain knowledge for learning_record production
sources: experiential learning theory, retrospective patterns, CEX memory system
---

# Domain Knowledge: learning_record

## Foundational Concept
A learning record captures what was learned from a concrete experience — what worked,
what failed, and under what conditions. Unlike knowledge cards (external facts),
learning records are INTERNAL: they emerge from system operation and accumulate
over time. Rooted in Kolb's Experiential Learning Cycle (1984): experience ->
reflection -> abstraction -> application.

## The Learning Pipeline

```
EXPERIENCE -> OBSERVATION -> PATTERN EXTRACTION -> EVIDENCE -> CONFIDENCE SCORE
     |              |              |                   |              |
  (what happened)  (raw data)   (what worked/failed)  (proof)     (0.0-1.0)
```

Every learning record follows this pipeline. Skip a stage and the record
becomes unreliable noise instead of actionable intelligence.

## Structured Learning: The Four Required Elements

### 1. Observation (what happened)
Raw factual account. No interpretation, no judgment.
- "3 concurrent requests with expired token each triggered /auth/refresh independently"
- NOT "The auth system had problems" (vague, no specifics)

### 2. Pattern (what worked or what the data implies)
Reproducible rule extracted from the observation.
- "Single-promise mutex on refresh prevents thundering herd: `if (_refreshPromise) return _refreshPromise`"
- NOT "Handle concurrent requests gracefully" (no concrete mechanism)

### 3. Evidence (proof that the pattern holds)
Concrete data points: metrics, test results, before/after comparisons.
- "Before: 3 of 5 requests failed with 'token already used'. After: 0 failures in 50 requests"
- NOT "It seemed to work better" (no measurable data)

### 4. Confidence Score (how much to trust this)
Float 0.0-1.0 based on evidence strength:

| Score | Meaning | Basis |
|-------|---------|-------|
| 0.9-1.0 | Near-certain | 10+ observations, consistent results, no contradictions |
| 0.7-0.8 | High confidence | 5-9 observations, mostly consistent |
| 0.5-0.6 | Moderate | 2-4 observations, some variation |
| 0.3-0.4 | Low | 1 observation, plausible but unverified |
| 0.0-0.2 | Speculative | Theoretical, no direct evidence |

**Confidence increases** with: frequency of observation, recency, consistency across contexts.
**Confidence decreases** with: time since last observation (decay), contradictory evidence, narrow context.

## Entity Tracking

Entities are the subjects of learning — agents, tools, processes, configurations.
Each entity accumulates facts over time.

```yaml
entity: TOOL_NAME
facts:
  - id: 1
    relation: performance_metric
    value: "Response time p95 dropped from 800ms to 120ms after connection pooling"
    timestamp: "2026-02-05T12:11:56"
    hash: "273ecac786c2"  # content hash for dedup
```

**Entity tracking rules**:
- One entity = one identifiable component (tool, service, agent, pattern)
- Facts are append-only (never mutate historical facts)
- Each fact has a timestamp for temporal analysis
- Content hash prevents duplicate fact insertion
- Entity files serve as the single source of truth for that subject

## Semantic Links: The Knowledge Graph

Learning records connect to each other through typed relationships:

```
Entity A --[relation_type]--> Entity B
```

| Relation Type | Meaning | Example |
|--------------|---------|---------|
| depends_on | A requires B to function | auth_refresh depends_on jwt_validation |
| enables | A makes B possible | connection_pooling enables high_throughput |
| contradicts | A and B cannot both be true | eager_loading contradicts lazy_init |
| refines | A is a more specific version of B | mutex_refresh refines token_management |
| caused_by | A is an effect of B | thundering_herd caused_by concurrent_refresh |

**Link quality rules**:
- Every link must be bidirectionally meaningful
- Avoid orphan entities (no incoming or outgoing links)
- Contradiction links are the most valuable — they prevent repeating mistakes
- Links should reference specific facts, not entire entities

## Memory Decay: Time-Aware Confidence

Learning degrades over time. A pattern observed 6 months ago in a different
environment may no longer hold.

```
effective_confidence = base_confidence * decay_factor
decay_factor = exp(-decay_rate * days_since_last_use)
```

| Decay Rate | Half-Life | Use Case |
|-----------|-----------|----------|
| 0.01 | ~69 days | Stable infrastructure patterns |
| 0.03 | ~23 days | API behaviors, library versions |
| 0.05 | ~14 days | Market data, pricing, trends |
| 0.10 | ~7 days | Ephemeral config, session state |

**Refresh mechanisms**:
- Successful re-application resets `last_used` and boosts confidence
- Failed re-application reduces confidence by 0.1-0.2
- Periodic validation against current state catches drift

## Outcome Classification

Every learning record MUST classify its outcome:

| Outcome | When to Use | Score Range |
|---------|-------------|-------------|
| SUCCESS | Pattern achieved intended result reliably | 7.0-10.0 |
| PARTIAL | Pattern worked but with caveats or limitations | 5.0-6.9 |
| FAILURE | Pattern did not achieve intended result | 0.0-4.9 |

**Score is impact magnitude** (0.0-10.0):
- 9.0+: Transformative (10x improvement, critical bug prevention)
- 7.0-8.9: Significant (measurable quality or efficiency gain)
- 5.0-6.9: Moderate (worked but marginal benefit)
- 3.0-4.9: Minimal (barely noticeable effect)
- 0.0-2.9: Negligible or harmful

## Body Structure (7 required sections)

| Section | Purpose | Density Target |
|---------|---------|---------------|
| Summary | Dense overview, 2-3 sentences | Every word carries information |
| Pattern | What worked — concrete, reproducible steps | Code, config, or numbered steps |
| Anti-Pattern | What failed or should be avoided | Specific failure + WHY + alternative |
| Context | Environment, constraints, timing | Table of variables that matter |
| Impact | Measurable outcomes | Numbers: time saved, errors avoided, delta |
| Reproducibility | Conditions for repeating this outcome | Prerequisites + variations tested |
| References | Related records, artifacts, commits | Links, not descriptions |

## Patterns from High-Scoring Records

### Concrete Over Abstract
- GOOD: "Used retry with 3s exponential backoff, max 5 attempts, jitter 0-500ms"
- BAD: "Handle errors gracefully with appropriate retry logic"

### Outcome-First Writing
Lead with the result, then explain how you got there:
- GOOD: "SUCCESS (9.0): Mutex pattern eliminated 100% of concurrent refresh failures"
- BAD: "We investigated the auth system and found some issues with token refresh..."

### Both Sides Always
Every pattern has a failure mode. Every failure teaches a pattern.
- Pattern: "Single-promise mutex on token refresh"
- Anti-pattern: "Each request independently calling /auth/refresh"
- They are the same learning, viewed from two angles.

### Measurable Impact
Quantify everything possible:
- Time: "Reduced from 45min manual to 3min automated"
- Errors: "Error rate dropped from 12% to 0.3%"
- Quality: "Score improved from 7.2 to 8.8 average"
- Cost: "Token usage reduced 40% via caching"

## Anti-Patterns (from real low-quality records)

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No evidence | Confidence is meaningless without data | Add metrics, test results, before/after |
| Vague pattern | "Handle errors better" teaches nothing | Specific mechanism: tool, config, code |
| Missing outcome | Cannot classify or route the learning | Always set SUCCESS/PARTIAL/FAILURE |
| No timestamp | Cannot track decay or trends | ISO 8601 datetime on every record |
| Orphan links | Entity with no connections to knowledge graph | Add at least one semantic link |
| Confidence without basis | Score of 0.9 with one observation | Score must reflect evidence quantity |
| Missing anti-pattern | Only documenting what worked | Every success implies a failure mode |
| Stale records | Pattern from 6 months ago, never re-validated | Apply decay, re-validate periodically |

## Boundary: What Is NOT a Learning Record

| Type | What It Is | Why It Is NOT a Learning Record |
|------|------------|-------------------------------|
| Knowledge card | External fact, atomically distilled | KC comes from research, LR from experience |
| Session state | Ephemeral snapshot of current work | Session dies with session, LR persists |
| Mental model | Decision map for routing | Model decides, LR records outcomes |
| Axiom | Immutable truth/principle | Axiom never changes, LR evolves with evidence |
| Test case | Reference validation input/output | Test validates, LR documents what happened |

## Self-Improvement Protocol

Learning records feed back into the system:

```
[New Experience] -> [Create LR] -> [Link to entities]
                                        |
                    [Score >= 9.0] -> [Promote pattern to shared pool]
                    [Score < 7.0]  -> [Add anti-pattern to failure registry]
                    [3+ successes]  -> [Solidify: increase confidence, reduce decay]
                    [Contradiction] -> [Flag for review, link as contradicts]
```

**Propagation threshold**: Only share learnings scoring >= 9.0 with other domains.
Lower-scoring records stay local until they accumulate more evidence.
