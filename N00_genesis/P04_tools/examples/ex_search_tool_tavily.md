---
id: p04_search_tavily
kind: search_tool
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Tavily Web Search"
provider: "tavily"
search_type: web
max_results: 5
result_fields:
  - title
  - url
  - snippet
  - score
date_range: true
domain_filter: true
language: [en, pt]
cost_per_query: "$0.01"
rate_limit: "1000/month (free tier)"
quality: 9.0
tags: [search_tool, tavily, web, RAG]
tldr: "Tavily web search optimized for LLM agents — returns ranked results with relevance scores"
description: "Web search via Tavily API returning structured results for RAG and agent workflows"
domain: "tool integration"
title: "Search Tool Tavily"
density_score: 0.93
---

# Tavily Web Search

## Overview
Tavily is a search API purpose-built for LLM agents. Returns clean, structured results with relevance scores, optimized for grounding LLM outputs with real-time web data.

## Query
### Parameters
- `query` (string, required): Natural language search query, max 400 chars
- `max_results` (integer, optional, default: 5): Results to return, 1-20
- `search_type` (enum, optional): web | news

### Filtering
- Date range: supports `days` parameter to limit recency (e.g., last 7 days)
- Domain filter: `include_domains` / `exclude_domains` arrays
- Language: auto-detected from query; bias via `include_domains`

## Results
### Structure
Each result contains:
- `title` (string): Page title
- `url` (string): Canonical URL
- `snippet` (string): Relevant excerpt, max 200 chars
- `score` (float 0-1): Tavily relevance score

### Ranking
Results ranked by Tavily's proprietary relevance model, optimized for factual accuracy.

## Provider
- API: `https://api.tavily.com/search`
- Auth: env var `TAVILY_API_KEY` (NEVER hardcode)
- Rate limit: 1000/month free, unlimited on paid plans
- Cost: ~$0.01/query on paid tier
- Free tier: 1000 queries/month

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `search tool`
- **Artifact ID**: `p04_search_tavily`
- **Tags**: [search_tool, tavily, web, RAG]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `search tool` | Artifact type |
| Pipeline | 8F (F1→F8) |
