---
kind: examples
id: bld_examples_dispatch_rule
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of dispatch_rule artifacts
pattern: few-shot learning for keyword-to-agent_group routing rules
quality: 9.0
title: "Examples Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: dispatch-rule-builder
## Golden Example
INPUT: "Route research, market analysis and competitor scraping to researcher"
OUTPUT (`p12_dr_research.yaml`):
```yaml
id: p12_dr_research
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: codex
domain: research
quality: null
tags: [dispatch, research, shaka, market, scrape]
tldr: Route market research and competitor analysis tasks to researcher agent_group
scope: research
keywords: [researchr, research, market, market, competitor, competitor, scrape, analysis, analysis, benchmark]
agent_group: shaka
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: pytha
conditions:
  exclude_domains: [internal_docs, knowledge_indexing]
load_balance: false
routing_strategy: hybrid
# research Dispatch Rule
## Purpose
Routes market research, competitor intelligence, and scraping to researcher.
researcher carries firecrawl MCP and research-optimized prompting.
## Keyword Rationale
Bilingual PT/EN coverage fires on both Portuguese operator commands and English
task descriptions. `analysis`/`analysis` catch adjacent sub-tasks.
## Fallback Logic
knowledge-engine handles knowledge domain when researcher is unavailable; can index and
summarize research outputs without firecrawl.
```
WHY THIS IS GOLDEN:
- filename `p12_dr_research.yaml` follows naming pattern
- `id: p12_dr_research` matches `^p12_dr_[a-z][a-z0-9_]+$`
- `kind: dispatch_rule`, `pillar: P12` present
- `quality: null` — never a score at authoring time
- `tags` includes agent_group slug `shaka`
- `tldr` <= 120 chars and specific
- `scope` matches filename segment
- `keywords` 10 terms: bilingual PT+EN coverage (S10 pass)
- `agent_group: shaka` and `fallback: pytha` are distinct lowercase slugs
- `model: sonnet` correct for researcher research domain
- `priority: 8` for high-value business domain
- `confidence_threshold: 0.70` in recommended precision range
- `routing_strategy: hybrid` for large bilingual keyword set
- `conditions` scopes out adjacent knowledge_indexing domain
- body sections present: Purpose, Keyword Rationale, Fallback Logic
- 19 frontmatter fields (all required + 3 optional: conditions, load_balance, routing_strategy)
- zero signal drift: no `status`, `timestamp`, `quality_score`
- zero handoff drift: no `tasks`, `scope_fence`, `commit`
## Anti-Example
BAD OUTPUT (`p12_dispatch_rule_research.json`):
```json
{
  "id": "dispatch-research",
  "type": "routing",
  "agent_group": "researcher",
  "keywords": "research, market",
  "quality_score": 8.5,
  "timestamp": "2026-03-26T10:00:00Z",
  "status": "complete",
  "tasks": ["scrape competitor sites", "summarize findings"],
  "scope_fence": "only touch records/research/",
  "priority": "high",
  "fallback": "researcher",
  "model": "gpt-4"
}
```
FAILURES:
1. [H01] wrong format: JSON not YAML — dispatch_rule requires `.yaml` frontmatter hybrid
2. [H03] `id: dispatch-research` — fails `^p12_dr_[a-z][a-z0-9_]+$` (no prefix, hyphen not underscore)
3. [H04] `kind` absent — type discriminator `dispatch_rule` missing
4. [H06] `quality_score: 8.5` — must be `quality: null`; scoring forbidden at authoring time
5. [H07] `keywords` is a string — must be a YAML list for routing engine iteration
6. [H09] `model: gpt-4` — not in enum (`sonnet`, `opus`, `haiku`, `flash`)
7. [H10] `priority: "high"` — must be integer 1-10, not string label
8. [H12] `fallback: researcher` equals `agent_group: researcher` — fallback must be a distinct agent_group
9. [H14] `status`, `timestamp`, `quality_score` present — signal boundary violation
10. [H15] `tasks`, `scope_fence` present — handoff boundary violation
11. [S01] `agent_group: researcher` uppercase — must be lowercase slug `shaka`
12. [S10] keywords EN-only string — no PT variants for bilingual coverage
