---
id: entity_memory_n01
kind: entity_memory
pillar: P10
nucleus: n01
title: "N01 Research Entity Memory"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [entity_memory, n01, entities, research, competitor_tracking, persistence]
tldr: "Typed entity memory for N01: tracks companies, people, products, papers, and market events across research sessions. Prevents re-researching known entities. Enables compound intelligence over time."
density_score: 0.89
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P10/entity_memory F2 become=entity-memory-builder F3 inject=mem_entity_memory_n01+knowledge_index_intelligence+retriever_n01 F4 reason=Analytical Envy demands compounding -- each session builds on prior; entity memory prevents N01 from starting from zero each time F5 call=cex_compile F6 produce=entity_memory_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P10_memory/ -->

## Purpose

Without entity memory, N01 researches the same companies from scratch every session.
This erases the compound advantage that Analytical Envy demands.

Entity memory creates persistent profiles for:
- Companies (competitors, partners, targets)
- People (founders, executives, key voices)
- Products (tracked over time)
- Papers (known academic works)
- Events (funding rounds, acquisitions, launches)

## Entity Schema

### Company Entity

| Field | Type | Description |
|-------|------|-------------|
| `entity_id` | string | `co_{slug}` |
| `name` | string | canonical company name |
| `slug` | string | URL-safe lowercase |
| `category` | string | competitor / partner / target / supplier |
| `domain` | string | primary business domain |
| `founded` | year | founding year |
| `stage` | string | seed / series-A / ... / public |
| `employees` | int | last known count |
| `funding_total` | USD | total funding raised |
| `last_funding` | ISO8601 | date of last funding round |
| `products` | string[] | product names |
| `pricing_tier` | string | free / freemium / paid / enterprise |
| `pricing_snapshot` | dict | pricing at last observation |
| `pricing_date` | ISO8601 | when pricing was captured |
| `strengths` | string[] | analytical strengths |
| `weaknesses` | string[] | analytical weaknesses |
| `strategic_moves` | event[] | tracked strategic events |
| `hiring_signals` | signal[] | job posting trends |
| `last_updated` | ISO8601 | entity last updated |
| `sources` | string[] | URLs used to populate |

### Person Entity

| Field | Type | Description |
|-------|------|-------------|
| `entity_id` | string | `pe_{slug}` |
| `name` | string | full name |
| `current_role` | string | title at current company |
| `current_company` | string | company entity_id |
| `domain_expertise` | string[] | areas of expertise |
| `publications` | string[] | notable papers/posts |
| `social_profiles` | dict | linkedin / twitter / github |
| `influence_score` | float | 0-1 estimate |

### Market Event

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | `ev_{type}_{slug}_{date}` |
| `event_type` | string | funding / acquisition / launch / partnership |
| `entities` | string[] | companies involved |
| `date` | ISO8601 | event date |
| `summary` | string | 1-paragraph summary |
| `sources` | string[] | source URLs |
| `implications` | string | N01 analysis of implications |

## Storage

| Location | Format | Index |
|----------|--------|-------|
| `N01_intelligence/P10_memory/entities/co_{slug}.yaml` | YAML | `knowledge_index_n01.md` |
| `N01_intelligence/P10_memory/entities/pe_{slug}.yaml` | YAML | `knowledge_index_n01.md` |
| `N01_intelligence/P10_memory/events/ev_{type}_{date}.yaml` | YAML | `knowledge_index_n01.md` |

## Write Protocol

When N01 researches a company for the first time:
1. Check entity memory: `retriever.query(company_name)`
2. If found: LOAD existing profile, update with new findings
3. If not found: CREATE new entity profile from research
4. After session: SAVE updated profile with new `last_updated`

Entity update policy:
- Overwrite: pricing, employee count, stage, last_funding
- Append: strategic_moves, hiring_signals, products, sources
- Merge: strengths, weaknesses (union, not replace)

## Retrieval Protocol

```
get_entity(name: str) -> Entity | None:
  # 1. exact match on slug
  slug = slugify(name)
  if exists(f"entities/co_{slug}.yaml"):
    return load(f"entities/co_{slug}.yaml")
  # 2. fuzzy match via retriever
  results = retriever.query(name, top_k=3)
  if results[0].score > 0.85:
    return load(results[0].doc_id)
  return None
```

## Anti-Staleness

| Field Age | Action |
|-----------|--------|
| < 30 days | use without warning |
| 30-90 days | use with [POSSIBLY STALE] tag |
| > 90 days | trigger re-research for that entity |
| > 365 days | archive, re-research from scratch |

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| `P10_memory/knowledge_index_n01.md` | indexes all entities |
| `P04_tools/retriever_n01.md` | retrieves entities by query |
| `P04_tools/competitor_monitor_n01.md` | updates company entities from monitoring |
| `P10_memory/mem_entity_memory_n01.md` | predecessor, generic entity schema |
