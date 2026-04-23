---
id: tpl_search_tool_business_discovery
kind: template
pillar: P04
title: "Search Tool — Business Discovery Configuration"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/P04 search artifacts
variables: [INDUSTRY, REGION, SEARCH_PROVIDERS, VERTICALS, CITIES]
density_score: 0.95
tags: [template, search-tool, business-discovery, research, instance-extraction]
tldr: "Search tool configuration for multi-source business discovery — optimized queries by vertical and region."
updated: "2026-04-13"
related:
  - tpl_research_batch_maps
  - tpl_research_batch_directories
  - tpl_workflow_research_pipeline
  - bld_schema_model_registry
  - bld_knowledge_card_search_tool
  - n06_schema_brand_config
  - search-tool-builder
  - bld_schema_search_tool
  - bld_schema_experiment_tracker
  - bld_schema_training_method
---

# Business Discovery — Search Configuration

## Search Provider Stack

| Priority | Provider | Capability | Rate Limit |
|:--------:|----------|-----------|:----------:|
{{#SEARCH_PROVIDERS}}
| {{priority}} | {{name}} | {{capability}} | {{rate_limit}} |
{{/SEARCH_PROVIDERS}}

**Default stack** (if not specified):
1. SERPER (Google Search API) — web + maps + news
2. EXA (semantic search) — deep web, academic, niche
3. FIRECRAWL (scraper) — structured extraction from pages

---

## Search Terms by Vertical

{{#VERTICALS}}
### {{name}} (`{{slug}}`)

**Primary queries**:
```
{{#primary_terms}}
"{{term}}" "{{city}}" {{state}}
{{/primary_terms}}
```

**Long-tail queries**:
```
{{#longtail_terms}}
{{term}}
{{/longtail_terms}}
```

**Negative keywords** (filter out):
```
{{#negative_terms}}
-"{{term}}"
{{/negative_terms}}
```

{{/VERTICALS}}

---

## Regional Variations

| Region Type | Query Modifier | Example |
|------------|----------------|---------|
| Metropolitan | `near "{{CITY}}"` | `"{{INDUSTRY}}" near "São Paulo"` |
| Interior | `"{{CITY}}" {{STATE}}` | `"{{INDUSTRY}}" "Campinas" SP` |
| National | `"{{COUNTRY}}"` | `"{{INDUSTRY}}" "Brasil"` |
| By radius | `within {{KM}}km of` | `within 15km of "center"` |

---

## Output Schema

Each discovered business → JSON object:

```json
{
  "nome": "string (required)",
  "cidade": "string (required)",
  "segmento": "string (required)",
  "vertical": "string (from VERTICALS)",
  "telefone": "string",
  "endereco": "string",
  "website": "string",
  "fonte": "string (search provider)",
  "query_used": "string (for audit trail)",
  "confidence": "high | medium | low"
}
```

---

## Discovery Pipeline Sequence

```
Phase 1: Broad sweep (SERPER)
  → {{VERTICALS.count}} verticals × {{CITIES.count}} cities
  → Collect URLs + snippets

Phase 2: Deep extraction (FIRECRAWL)
  → Top results from Phase 1
  → Structured data from business pages

Phase 3: Semantic fill (EXA)
  → Gaps from Phase 1+2
  → Niche sources, blogs, directories

Phase 4: Dedup + merge
  → Normalize names
  → Match by name + city
  → Merge data from multiple sources
```

---

## Rate Limiting

| Provider | Requests/min | Daily cap | Backoff |
|----------|:------------:|:---------:|---------|
| SERPER | 60 | 10,000 | exponential 2s→60s |
| EXA | 30 | 5,000 | linear 1s→30s |
| FIRECRAWL | 10 | 1,000 | fixed 3s |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_research_batch_maps]] | sibling | 0.36 |
| [[tpl_research_batch_directories]] | sibling | 0.33 |
| [[tpl_workflow_research_pipeline]] | sibling | 0.32 |
| [[bld_schema_model_registry]] | downstream | 0.31 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.30 |
| [[n06_schema_brand_config]] | downstream | 0.27 |
| [[search-tool-builder]] | related | 0.27 |
| [[bld_schema_search_tool]] | downstream | 0.27 |
| [[bld_schema_experiment_tracker]] | downstream | 0.26 |
| [[bld_schema_training_method]] | downstream | 0.25 |
