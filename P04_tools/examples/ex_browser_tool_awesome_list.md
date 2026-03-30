---
id: p04_browser_awesome_list
kind: browser_tool
name: awesome_list_crawler
pillar: P04
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [scraper, github, awesome-list, curation]
---

# Scraper: awesome_list_crawler

## Target
- Source: GitHub awesome-lists (curated link collections)
- Data wanted: tool name, URL, description, stars, category
- Cadence: on_demand (via research_agent research pipeline)

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
