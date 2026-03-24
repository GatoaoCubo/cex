---
id: p04_scraper_awesome_list
name: awesome_list_crawler
description: "Web scraper that mines GitHub awesome-lists for curated tools, libraries, and resources with quality tier classification"
target: github_awesome_lists
output_format: categorized_entries
lp: P04
type: scraper
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: research
quality: 9.0
tags: [scraper, github, awesome-list, crawler, curation, resources]
---

# Awesome List Crawler — Curated Resource Discovery

## Purpose
Scraper agent that mines GitHub awesome-lists for tools, libraries, and resources. Only CODEXA agent with quality tier system and domain mapping for curated lists. Satellite: SHAKA (INVEJA ANALITICA).

## Workflow
```
1. RECEIVE  --> Topics + optional filters (max_lists, min_stars)
2. EXECUTE  --> list_discovery -> entry_extraction -> category_mapping
3. DELIVER  --> Categorized entries mapped to CODEXA domains
```

## Trigger Phrases
- "Find awesome-lists for..."
- "Crawl GitHub awesome resources about..."
- "Discover tools/libraries in X domain"
- "Map curated resources to CODEXA domains"

## Capabilities
- Discovers awesome-lists by topic via GitHub search
- Extracts individual entries with descriptions and URLs
- Classifies entries into quality tiers (starred, recommended, listed)
- Maps categories to CODEXA satellite domains
- Respects max_lists and min_stars filters

## Output
Categorized entries with:
- Resource name, URL, description
- Quality tier classification
- CODEXA domain mapping (SHAKA, EDISON, PYTHA, etc.)
