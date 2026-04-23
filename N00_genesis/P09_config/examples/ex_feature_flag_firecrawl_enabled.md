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
domain: "config"
related:
  - p09_env_firecrawl
  - bld_tools_research_pipeline
  - n01_kc_source_catalog
  - n06_content_factory_pricing
  - bld_examples_entity_memory
  - bld_examples_agent_card
  - bld_memory_runtime_state
  - p01_kc_feature_flag
  - runtime-state-builder
  - p07_dataset_rag_qa_v1
---

# Flag: FIRECRAWL_ENABLED

## Definition

| Property | Value |
|----------|-------|
| Flag | `FIRECRAWL_ENABLED` |
| State | on |
| Rollout | 100% |
| Owner | operations_agent agent_group |
| Expires | never |

## Behavior

| State | Effect |
|-------|--------|
| `true` | Research enriches marketplace data via Firecrawl REST API. Consumes 1-3 credits per source. Conservation mode activates at <20% monthly credits. |
| `false` | All enrichment skipped. Research uses Serper-only pipeline. No credit consumption. Planner aliases shopee->shopee_serper, amazon->amazon_serper. |

## Guard

1. Enable condition: `FIRECRAWL_API_KEY` is set and valid, monthly budget > 0
2. Disable condition: Credits exhausted or API key revoked
3. Rollback: Set `FIRECRAWL_ENABLED=false` in Railway dashboard, takes effect on next request (no restart needed)

---
*Migrated from: organization MEMORY.md (Architecture State section)*

## Metadata

```yaml
id: p09_ff_firecrawl_enabled
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p09-ff-firecrawl-enabled.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_env_firecrawl]] | related | 0.44 |
| [[bld_tools_research_pipeline]] | upstream | 0.21 |
| [[n01_kc_source_catalog]] | upstream | 0.21 |
| [[n06_content_factory_pricing]] | downstream | 0.21 |
| [[bld_examples_entity_memory]] | upstream | 0.19 |
| [[bld_examples_agent_card]] | upstream | 0.19 |
| [[bld_memory_runtime_state]] | downstream | 0.19 |
| [[p01_kc_feature_flag]] | related | 0.17 |
| [[runtime-state-builder]] | downstream | 0.16 |
| [[p07_dataset_rag_qa_v1]] | upstream | 0.16 |
