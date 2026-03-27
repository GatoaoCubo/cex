---
id: p04_scraper_awesome_list
kind: scraper
name: awesome_list_crawler
pillar: P04
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [scraper, github, awesome-list, curation]
---

# Scraper: awesome_list_crawler

## Target
- Source: GitHub awesome-lists (curated link collections)
- Data wanted: tool name, URL, description, stars, category
- Cadence: on_demand (via SHAKA research pipeline)

## Extraction Plan
1. Discover awesome-lists via GitHub search API (topic + min_stars)
2. Parse README.md (## headers = categories, - links = entries)
3. Enrich with GitHub API metadata (stars, language, last_updated)
4. Classify into CODEXA domains and quality tiers

## Output
```yaml
items:
  - name: "langchain"
    url: "https://github.com/langchain-ai/langchain"
    description: "Building LLM apps"
    stars: 82000
    category: "frameworks"
    codexa_domain: "build"
    tier: "gold"
```

Tiers: gold (>10K stars, active), silver (>1K), bronze (<1K or stale).
