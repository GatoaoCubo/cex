---
id: p09_env_firecrawl
kind: env_config
pillar: P09
title: "Env: FIRECRAWL_API_KEY"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.0
tags: [firecrawl, api-key, env, config]
tldr: "Firecrawl API key for web scraping enrichment of marketplace research"
density_score: 0.88
source: organization-core/.claude/projects/memory/MEMORY.md
domain: "config"
---

# Env: FIRECRAWL_API_KEY

## Variable

| Property | Value |
|----------|-------|
| Name | `FIRECRAWL_API_KEY` |
| Value | `fc-...` (secret, 40 chars) |
| Scope | prod |
| Required | true |
| Format | string (prefix `fc-`) |

## Source

1. Where defined: Railway environment variables (operations_agent agent_group)
2. How to obtain: Sign up at firecrawl.dev, $19/mo tier, copy API key from dashboard

## Fallback

| Condition | Behavior |
|-----------|----------|
| Absent | Enrichment skipped, research uses Serper-only fallback |
| Default | none (no free tier fallback) |

## Consumers

1. `api/core/erp_connector.py`: Enriches marketplace product data (shopee 3 credits, amazon 3 credits, magalu/americanas/casas_bahia/shein 1 each)
2. `api/v1/pesquisas.py`: Marketplace research with `formats: ["extract"]` + `extract: {schema, prompt}` pattern

## Dependencies

1. Requires: `FIRECRAWL_ENABLED=true`, `FIRECRAWL_MONTHLY_BUDGET=3000`, `FIRECRAWL_PER_RESEARCH_BUDGET=10`
2. Conflicts: none (Serper runs independently)

---
*Migrated from: organization MEMORY.md (Firecrawl integration 2026-03-01)*

## Metadata

```yaml
id: p09_env_firecrawl
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p09-env-firecrawl.md
```
