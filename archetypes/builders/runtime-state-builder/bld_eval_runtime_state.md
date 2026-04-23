---
kind: quality_gate
id: p11_qg_runtime_state
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_state artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Runtime State'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for agent runtime mental state: verifies routing rules, state
  transitions, persistence scope, and conflict resolution.'
domain: runtime_state
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p11_qg_quality_gate
  - p11_qg_mental_model
  - runtime-state-builder
  - bld_memory_runtime_state
  - p11_qg_response_format
  - bld_collaboration_runtime_state
  - bld_knowledge_card_runtime_state
  - p03_ins_runtime_state
  - p11_qg_runtime_rule
  - p11_qg_router
---

## Quality Gate

## Definition
A runtime state artifact captures the live decision-making configuration of an agent: its routing rules (with conditions and confidence), state transitions (with trigger events), priority ordering, and heuristics. It applies only during execution — it contains no design-time content such as capability descriptions or architectural diagrams. Persistence scope declares whether state survives across sessions or resets each time.
Scope: files with `kind: runtime_state`. Does not apply to mental models (design-time identity), system prompts (static instructions), or session state (ephemeral task context).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p10_rs_*` | `id.startswith("p10_rs_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `runtime_state` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, agent, persistence all present |
| H07 | Routing rules section present with >= 2 rules each having a condition | count routing rule entries >= 2; each has a condition field |
| H08 | State transitions section present with >= 1 named transition and a trigger event | count transitions >= 1; each has trigger field non-empty |
| H09 | `persistence` field is one of: within-session, cross-session | enum membership check |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every routing rule has an explicit condition (not a vague keyword) | 1.0 |
| 3  | Every state transition has a named trigger event (not just a description) | 1.0 |
| 4  | Priority ordering present with rationale for each rank | 1.0 |
| 5  | Heuristics section present with at least 2 rules of thumb and their confidence levels | 1.0 |
| 6  | Domain map present with explicit boundary (what this agent handles vs. what it defers) | 1.0 |
| 7  | Tags list includes `runtime-state` | 0.5 |
| 8  | Update conditions explicit (what triggers a state change, not just that state can change) | 1.0 |
| 9  | Conflict resolution described for cases where two routing rules could both fire | 1.0 |
| 10 | No design-time content present (no capability lists, architecture notes, or setup instructions) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 10.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for agent state design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Agent is in early bootstrapping and fewer than 2 routing rules have been observed in forctice |
| approver | Domain lead must approve in writing before bypass takes effect |

## Examples

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
quality: 8.9
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
