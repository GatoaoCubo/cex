---
kind: schema
id: bld_schema_knowledge_index
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for knowledge_index
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: knowledge_index
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_bi_{index_slug}) | YES | — | Namespace compliance |
| kind | literal "knowledge_index" | YES | — | Type integrity |
| pillar | literal "P10" | YES | — | Pillar assignment |
| title | string "Brain Index: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| scope | string | YES | — | What content this index covers |
| algorithm | enum (bm25, faiss, hybrid) | YES | — | Primary search algorithm |
| corpus_type | enum (text, vector, structured) | YES | — | Type of indexed content |
| domain | string | YES | — | Domain this index serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
| rebuild_schedule | enum (on_change, hourly, daily, weekly, manual) | YES | — | When index rebuilds |
| freshness_max_days | integer >= 0 | YES | — | Max staleness in days |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| embedding_model | string | REC | — | Embedding model used (if FAISS/hybrid) |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
| corpus_size_estimate | string | REC | — | Approximate corpus size |
## ID Pattern
Regex: `^p10_bi_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Scope` — what content is indexed and why
2. `## Algorithm Config` — BM25, FAISS, or hybrid parameters
3. `## Filters` — pre-search and post-search filters
4. `## Ranking` — scoring formula, boosts, and reranking
5. `## Rebuild` — schedule, triggers, and freshness policy
6. `## Monitoring` — health checks, quality metrics, alerting
## Constraints
- max_bytes: 3072 (body only)
- naming: p10_bi_{index_slug}.md
- id == filename stem
- algorithm MUST be valid enum
- corpus_type MUST be valid enum
- rebuild_schedule MUST be valid enum
- quality: null always
