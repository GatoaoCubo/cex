---
id: p04_browser_awesome_list
kind: browser_tool
8f: F5_call
name: awesome_list_crawler
pillar: P04
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [scraper, github, awesome-list, curation]
updated: "2026-04-07"
domain: "tool integration"
title: "Browser Tool Awesome List"
density_score: 0.92
tldr: "Defines browser tool for browser tool awesome list, with validation gates and integration points."
related:
  - skill
  - research_then_build
  - tpl_validation_schema
  - p03_up_dispatch_agent_group
  - p04_webhook_NAME
---

# Scraper: awesome_list_crawler

## Target
1. Source: GitHub awesome-lists (curated link collections)
2. Data wanted: tool name, URL, description, stars, category
3. Cadence: on_demand (via research_agent research pipeline)

## Extraction Plan
1. Discover awesome-lists via GitHub search API (topic + min_stars)
2. Parse README.md (## headers = categories, - links = entries)
3. Enrich with GitHub API metadata (stars, language, last_updated)
4. Classify into organization domains and quality tiers

## Output
```yaml
items:
  - name: "langchain"
    url: "https://github.com/langchain-ai/langchain"
    description: "Building LLM apps"
    stars: 82000
    category: "frameworks"
    organization_domain: "build"
    tier: "gold"
```

Tiers: gold (>10K stars, active), silver (>1K), bronze (<1K or stale).

## Properties

| Property | Value |
|----------|-------|
| Kind | `browser_tool` |
| Pillar | P04 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | downstream | 0.18 |
| [[research_then_build]] | downstream | 0.17 |
| [[tpl_validation_schema]] | downstream | 0.17 |
| [[p03_up_dispatch_agent_group]] | upstream | 0.16 |
| [[p04_webhook_NAME]] | related | 0.15 |
