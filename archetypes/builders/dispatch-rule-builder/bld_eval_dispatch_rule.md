---
kind: quality_gate
id: p11_qg_dispatch_rule
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of dispatch_rule artifacts
pattern: few-shot learning for keyword-to-agent_group routing rules
quality: 9.0
title: "Gate: dispatch_rule"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, dispatch-rule, routing, keyword-mapping, P11]
tldr: "Gates for dispatch_rule artifacts: validates keyword coverage, agent_group enum, fallback logic, multilingual support, and confidence thresholds."
domain: "dispatch_rule — routing rules mapping keywords to agent_groups with fallback logic"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.92
related:
  - bld_examples_dispatch_rule
  - p03_sp_dispatch_rule_builder
  - bld_instruction_dispatch_rule
  - dispatch-rule-builder
  - p11_qg_agent-card
  - p01_kc_dispatch_rule
  - p11_qg_router
  - bld_schema_dispatch_rule
  - p11_qg_chunk_strategy
  - p11_qg_quality_gate
---

## Quality Gate

# Gate: dispatch_rule
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: dispatch_rule` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p12_dr_[a-z][a-z0-9_]+$` | "ID fails dispatch_rule namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"dispatch_rule"` | "Kind is not 'dispatch_rule'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, agent_group, model, priority, keywords, confidence_threshold, fallback, version, created, author, tags | "Missing required field(s)" |
| H07 | `agent_group` value is one of the defined agent_group enum (researcher, marketer, builder, knowledge-engine, executor, monetizer) | "Agent_group not in allowed enum" |
| H08 | `keywords` list is non-empty (>= 3 entries) | "Keyword list must have at least 3 entries" |
| H09 | `confidence_threshold` is a float between 0.0 and 1.0 | "Confidence threshold out of range [0.0, 1.0]" |
| H10 | `fallback` is defined and references a valid agent_group or literal `human` | "Fallback target undefined or invalid" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Keyword breadth | 1.0 | Keywords cover the full semantic space of the domain scope |
| Multilingual coverage | 1.0 | EN keywords required; community language keywords (PT, etc.) present |
| Priority rationale | 0.5 | Priority level (high/medium/low) explained or evident from domain |
| Confidence threshold calibration | 1.0 | Threshold value apownte for domain (not too strict/loose) |
| Fallback chain quality | 1.0 | Fallback agent_group is a logical second-choice for the domain |
| Scope fence clarity | 1.0 | What the rule does NOT route is explicitly stated |
| Model selection rationale | 0.5 | Model choice (sonnet/opus) justified by task complexity |
| Keyword specificity | 1.0 | No overly generic keywords that would cause routing collisions |
| Trigger phrase examples | 1.0 | 2+ example trigger sentences that would activate this rule |
| Boundary vs other rules | 0.5 | Non-overlap with adjacent dispatch rules documented |
| Domain precision | 1.0 | Domain field accurately describes the routing scope |
| Documentation | 0.5 | tldr captures routing intent in <= 160 characters |
Weight sum: 1.0+1.0+0.5+1.0+1.0+1.0+0.5+1.0+1.0+0.5+1.0+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | New agent_group being piloted without full keyword corpus established |
| approver | Routing system owner approval required (written) |
| audit_trail | Bypass logged to `records/audits/dispatch_rule_bypass_{date}.md` |
| expiry | 24h; routing rules in active use must be validated quickly |

## Examples

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
- `keywords` 10 terms: multilingual coverage (EN + community languages) (S10 pass)
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
12. [S10] keywords EN-only string — no community language variants for multilingual coverage

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
