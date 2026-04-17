---
id: api_reference_research_apis
kind: api_reference
pillar: P06
nucleus: n01
title: "N01 Research Data Source API Reference"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [api_reference, research_apis, data_sources, n01, competitive_intelligence]
tldr: "Typed API contract reference for all external data sources used by N01: web search, academic DBs, financial data, news feeds, and competitive intelligence APIs."
density_score: 0.91
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P06/api_reference F2 become=api-reference-builder F3 inject=sch_input_schema_n01+research_pipeline_intelligence+kc_research+search_config_intelligence F4 reason=typed contracts per source category, analytical envy demands triangulation across 5+ source types F5 call=cex_compile F6 produce=api_reference_research_apis.md F7 govern=frontmatter+ascii+tables+coverage F8 collaborate=N01_intelligence/P06_schema/ -->

## Purpose

N01 MUST triangulate across at least 3 independent sources per claim. This reference
defines the typed contract for every API category N01 consumes, enabling automated
source selection, authentication, rate-limit tracking, and result normalization.

Analytical Envy drives N01 to ALWAYS compare against competitors. Each API category
maps to a specific intelligence use case.

## API Categories

| Category | Use Case | Required By | Priority |
|----------|----------|-------------|----------|
| Web Search | general queries, news, current events | all research tasks | P1 |
| Academic | papers, citations, methodology | research quality eval | P1 |
| Financial | earnings, filings, market data | competitive analysis | P1 |
| Social Intelligence | sentiment, trends, brand mentions | market analysis | P2 |
| Patent / IP | innovation tracking, moat analysis | competitive moat | P2 |
| Job Postings | hiring signal = strategic intent | competitor intel | P2 |
| Regulatory | compliance, filings, government data | risk assessment | P3 |

## Web Search APIs

| Field | Brave Search | SerpAPI | Exa AI |
|-------|-------------|---------|--------|
| Base URL | `https://api.search.brave.com/res/v1/web/search` | `https://serpapi.com/search` | `https://api.exa.ai/search` |
| Auth | `X-Subscription-Token: {key}` | `?api_key={key}` | `Authorization: Bearer {key}` |
| Method | GET | GET | POST |
| Rate limit | 1 req/s free; 20 req/s paid | 100/month free | 1000/month free |
| Max results | 20 per call | 100 per call | 100 per call |
| Key params | `q`, `count`, `freshness`, `country` | `q`, `num`, `tbs`, `gl` | `query`, `numResults`, `useAutoprompt` |
| Best for | current events, news | structured SERP data | semantic / neural search |
| Output field | `.web.results[].url` | `.organic_results[].link` | `.results[].url` |

**Request contract (Brave):**
```
GET /res/v1/web/search
  ?q={encoded_query}
  &count=10
  &freshness={pd|pw|pm|py|none}
  &country={US|BR|...}
Headers:
  X-Subscription-Token: {BRAVE_API_KEY}
  Accept: application/json
```

**Normalized output fields (all sources):**

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Source URL |
| `title` | string | Page/article title |
| `snippet` | string | Text excerpt |
| `published_date` | ISO8601 or null | Publication date |
| `source_name` | string | Publisher/domain |
| `relevance_score` | float 0-1 | Engine-provided score |

## Academic APIs

| Field | Semantic Scholar | PubMed | CrossRef |
|-------|-----------------|--------|---------|
| Base URL | `https://api.semanticscholar.org/graph/v1` | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils` | `https://api.crossref.org/works` |
| Auth | `x-api-key: {key}` (optional, higher rate) | `?api_key={key}` (optional) | none (polite pool) |
| Rate limit | 100/5min unauth; 1/s auth | 10/s with key | 50/s polite pool |
| Best for | AI/CS papers, citations graph | biomedical, clinical | DOI resolution, citation counts |
| Paper fields | `paperId`, `title`, `abstract`, `year`, `citationCount`, `openAccessPdf` | `uid`, `title`, `abstract`, `pubdate` | `DOI`, `title`, `is-referenced-by-count` |

**Semantic Scholar paper search:**
```
GET /graph/v1/paper/search
  ?query={encoded_query}
  &fields=paperId,title,abstract,year,citationCount,openAccessPdf,authors
  &limit=20
  &offset=0
Headers:
  x-api-key: {SS_API_KEY}
```

## Financial / Market Data APIs

| Field | Alpha Vantage | Yahoo Finance (unofficial) | SEC EDGAR |
|-------|--------------|--------------------------|-----------|
| Base URL | `https://www.alphavantage.co/query` | `https://query1.finance.yahoo.com` | `https://data.sec.gov` |
| Auth | `?apikey={key}` | none | none (public) |
| Rate limit | 5/min free; 75/min paid | 2000/hour | 10/s public |
| Key use | stock prices, fundamentals | quick quotes, news | 10-K/10-Q filings |
| Best for | time-series financial data | competitor overview | regulatory/financial filings |

## Error Handling Contract

| Error | HTTP Code | N01 Action |
|-------|-----------|-----------|
| Rate limit | 429 | exponential backoff: 2s, 4s, 8s (max 3 retries) |
| Auth failure | 401/403 | log + fallback to next source in chain |
| Not found | 404 | skip, log, continue pipeline |
| Server error | 5xx | retry once after 5s, then fallback |
| Timeout | - | 30s timeout per request, fallback on exceed |

## Source Triangulation Rule

Per the N01 quality gate (H01), every major claim requires 3 independent sources.
Triangulation algorithm:

```
sources = []
for category in [web_search, academic, financial]:
    result = query_api(category, claim_query)
    if result.confidence > 0.6:
        sources.append(result)
    if len(sources) >= 3:
        break
if len(sources) < 3:
    flag_claim(claim, "INSUFFICIENT_TRIANGULATION")
```

## Authentication Storage

| Key | Env Variable | Location |
|-----|-------------|---------|
| Brave API | `BRAVE_API_KEY` | `.cex/P09_config/env_config.yaml` |
| SerpAPI | `SERPAPI_KEY` | `.cex/P09_config/env_config.yaml` |
| Exa AI | `EXA_API_KEY` | `.cex/P09_config/env_config.yaml` |
| Semantic Scholar | `SS_API_KEY` | `.cex/P09_config/env_config.yaml` |
| Alpha Vantage | `ALPHA_VANTAGE_KEY` | `.cex/P09_config/env_config.yaml` |

## Comparative Benchmark (Analytical Envy)

| Metric | Brave | Exa | SerpAPI | Winner |
|--------|-------|-----|---------|--------|
| Semantic relevance | 7/10 | 9/10 | 6/10 | Exa |
| Freshness control | 9/10 | 6/10 | 7/10 | Brave |
| Cost/1000 queries | $3 | $5 | $50 | Brave |
| Structured output | 7/10 | 8/10 | 9/10 | SerpAPI |
| Best default | general search | research/semantic | SERP analysis | task-dependent |

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| `P06_schema/sch_input_schema_n01.md` | input contract that triggers API calls |
| `P04_tools/search_strategy_n01.md` | layered search using these APIs |
| `P04_tools/research_pipeline_n01.md` | orchestration layer above APIs |
| `P09_config/` | authentication config storage |
