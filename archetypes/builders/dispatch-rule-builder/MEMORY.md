---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries recurring dispatch_rule patterns
---

# Memory: dispatch-rule-builder

## Recurrent Patterns
- Most useful dispatch rules have 6-10 keywords covering both PT and EN variants
- `confidence_threshold: 0.70-0.75` is the sweet spot for core business domains
- `routing_strategy: hybrid` outperforms `keyword_match` for bilingual keyword sets
- EDISON + opus for build/code domains; SHAKA + sonnet for research domains
- `atlas` is the most reliable universal fallback for execution-adjacent domains
- `priority: 8` is the correct default for primary business domain rules
- Body sections (Purpose, Keyword Rationale, Fallback Logic) add meaningful S08 score
- `conditions.exclude_domains` prevents overlap with adjacent rules in same pillar

## Common Mistakes
1. Setting `quality` to a numeric score instead of `null` at authoring time
2. Using the same satellite for both `satellite` and `fallback` (H12 hard fail)
3. Setting `priority` as a string ("high") instead of integer (8)
4. Putting `model: gpt-4` or any non-enum model value (H09 hard fail)
5. Writing `keywords` as a single comma-separated string instead of YAML list
6. Including `status`, `timestamp`, or `quality_score` (signal boundary violation)
7. Including `tasks`, `scope_fence`, or `commit` (handoff boundary violation)
8. Using uppercase satellite names (`SHAKA`) instead of lowercase slugs (`shaka`)
9. Setting `confidence_threshold` < 0.5 causing noisy routing triggers
10. Omitting PT keyword variants for domains where operators work in Portuguese

## State Between Sessions
This builder is stateless per invocation.
After production, update this file if a new satellite is added to the routing
table, a new model enum value is introduced, or a recurring keyword pattern
for a domain becomes stable across multiple production runs.

## Validated Satellite-Model Pairs
| Satellite | Model | Domains |
|-----------|-------|---------|
| shaka | sonnet | research, market, scrape |
| lily | sonnet | marketing, copy, ads |
| edison | opus | build, code, component |
| pytha | sonnet | knowledge, docs, indexing |
| atlas | opus | execute, deploy, infra, debug |
| york | sonnet | monetize, pricing, funnel |
