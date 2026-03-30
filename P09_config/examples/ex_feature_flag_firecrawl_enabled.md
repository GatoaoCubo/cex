---
id: p09_ff_firecrawl_enabled
kind: feature_flag
pillar: P09
title: "Flag: FIRECRAWL_ENABLED"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.0
tags: [firecrawl, feature-flag, enrichment, config]
tldr: "Master switch for Firecrawl web scraping enrichment in marketplace research"
density_score: 0.90
source: organization-core/Railway env vars
---

# Flag: FIRECRAWL_ENABLED

## Definition

| Property | Value |
|----------|-------|
| Flag | `FIRECRAWL_ENABLED` |
| State | on |
| Rollout | 100% |
| Owner | operations_agent agent_node |
| Expires | never |

## Behavior

| State | Effect |
|-------|--------|
| `true` | Research enriches marketplace data via Firecrawl REST API. Consumes 1-3 credits per source. Conservation mode activates at <20% monthly credits. |
| `false` | All enrichment skipped. Research uses Serper-only pipeline. No credit consumption. Planner aliases shopee->shopee_serper, amazon->amazon_serper. |

## Guard

- Enable condition: `FIRECRAWL_API_KEY` is set and valid, monthly budget > 0
- Disable condition: Credits exhausted or API key revoked
- Rollback: Set `FIRECRAWL_ENABLED=false` in Railway dashboard, takes effect on next request (no restart needed)

---
*Migrated from: organization MEMORY.md (Architecture State section)*
