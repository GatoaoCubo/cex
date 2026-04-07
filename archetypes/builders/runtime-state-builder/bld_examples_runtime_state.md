---
kind: examples
id: bld_examples_runtime_state
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_state artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: runtime-state-builder
## Golden Example
INPUT: "Create runtime_state for the research agent (researcher) defining routing and priorities at runtime"
OUTPUT:
```yaml
id: p10_rs_researcher
kind: runtime_state
pillar: P10
title: "Runtime State: Researcher Agent"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
agent: "researcher"
persistence: "cross_session"
domain: "market research"
quality: null
tags: [runtime-state, researcher, routing, priorities, heuristics]
tldr: "Researcher agent runtime state with keyword routing, 4 priorities, and source selection heuristics"
routing_mode: "hybrid"
priority_count: 4
update_frequency: "per_task"
fallback_agent: "general_assistant"
density_score: 0.88
constraint_count: 4
linked_artifacts:
  primary: "p02_mm_researcher"
  related: [p10_lr_research_patterns, p10_bi_knowledge_pool]
## Agent Context
Researcher agent operates in market research domain. Routes incoming
research tasks to apownte sources (web, pool, API) based on
query type and confidence thresholds. Accumulates source reliability
scores and routing preferences during execution.
## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| Pool-first | Query matches existing knowledge card | Return from pool, skip web | >= 0.85 |
| Web-fallback | Pool confidence < threshold | Search web sources | >= 0.60 |
| API-direct | Query is structured data request | Call API connector directly | >= 0.90 |
| Multi-source | Complex query, no single source sufficient | Fan out to pool + web + API | >= 0.70 |
## Decision Tree
```text
incoming_query
  ├── is_structured_data? -> API-direct route
  ├── pool_match >= 0.85? -> Pool-first route
  ├── pool_match >= 0.60? -> Web-fallback route
  └── complex_query? -> Multi-source route
```
## Priorities
1. Accuracy — prefer verified sources over speed
2. Freshness — prefer recent data over cached (max 7d stale)
3. Cost efficiency — minimize API calls when pool suffices
4. Completeness — cover all facets of multi-part queries
## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| Prefer pool for domain queries | Domain matches existing KC tags | 0.85 |
| Prefer web for trending topics | Query contains date-sensitive terms | 0.75 |
| Skip API for qualitative research | Query is opinion/analysis type | 0.80 |
| Fan-out for competitive analysis | Query mentions competitors | 0.70 |
## Constraints
1. Max 3 concurrent web requests per task
2. API budget: max 10 calls per session
3. Pool results must have quality >= 7.0 to be used
4. Web sources must be from allowlisted domains
## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| High pool hit rate | web_preferred | pool_preferred | 5+ consecutive pool hits |
| Pool staleness detected | pool_preferred | web_preferred | 3+ stale results in row |
| Budget exhaustion | any | pool_only | API calls >= budget limit |
| Quality drop | any | escalate | 3+ results below quality threshold |
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p10_rs_ pattern (H02 pass)
- kind: runtime_state (H04 pass)
- 19 frontmatter fields present (H08 pass)
- persistence: "cross_session" valid enum (H07 pass)
- routing_mode: "hybrid" valid enum (H09 pass)
- 4 routing rules with conditions and confidence (S03 pass)
- Decision tree with 4 branches (S04 pass)
- 4 ordered priorities with rationale (S05 pass)
- 4 heuristics with confidence levels (S06 pass)
## Anti-Example
INPUT: "Make agent state"
BAD OUTPUT:
```yaml
id: agent_state
kind: runtime_state
title: "State"
quality: 8.0
agent: researcher
## Rules
- Route queries to the best source
- Prioritize accuracy
- Use fallbacks when needed
```
FAILURES:
1. id: no p10_rs_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL
