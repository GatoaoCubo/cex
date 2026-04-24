---
id: p01_kc_web_scraping_ethics
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Web Scraping Ethics"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, scraping, ethics, robots-txt, rate-limit, attribution, legal]
tldr: "Respect robots.txt, rate limits, ToS. Prefer APIs over scraping. Cache results. Attribute sources. Never scrape PII. Legal compliance is non-negotiable."
when_to_use: "Before any automated web data collection, competitor research, or content aggregation task."
keywords: [scraping, ethics, robots-txt, rate-limit, attribution, legal, compliance]
density_score: 0.94
related:
  - p04_tool_scraping_config
  - bld_collaboration_prompt_cache
  - p04_browser_web_scraping
  - kc_ai_compliance_gdpr
  - prompt-cache-builder
  - kc_api_reference
  - p04_browser_tool_NAME
  - bld_tools_prompt_cache
  - p03_sp_prompt_cache_builder
  - ex_knowledge_card_prompt_caching
---

# Web Scraping Ethics

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Scrape responsibly: respect site rules, minimize impact, attribute sources |
| Trigger | Any task requiring automated web data collection |
| Benefit | Legal compliance, sustainable access, ethical reputation |
| Risk if skipped | IP bans, legal action, terms of service violations, data quality issues |

## Golden Rules

| # | Rule | Enforcement |
|---|------|------------|
| 1 | Check robots.txt before scraping | Automated pre-flight check |
| 2 | Max 1 request/second per domain | Rate limiter in code |
| 3 | Prefer official APIs over scraping | API discovery as first step |
| 4 | Cache results aggressively | Local cache with TTL |
| 5 | Attribute all sources | Source URL in artifact metadata |
| 6 | Never scrape PII | Content filter post-scrape |
| 7 | Respect Terms of Service | Manual ToS review for new domains |
| 8 | Use descriptive User-Agent | Identify bot, provide contact |

## Decision Tree: Scrape or Not?

| Question | Yes → | No → |
|----------|-------|------|
| Is there an official API? | Use API instead | Continue |
| Does robots.txt allow it? | Continue | **Stop** |
| Does ToS prohibit scraping? | **Stop** | Continue |
| Is content behind auth/paywall? | **Stop** | Continue |
| Does it contain PII? | **Stop** (or anonymize) | Continue |
| Can you rate-limit to 1 req/sec? | Proceed with scraping | Reduce scope |

## Rate Limiting Standards

| Scenario | Max Rate | Rationale |
|----------|----------|-----------|
| Small site (< 1K pages) | 1 req / 2 sec | Low server capacity |
| Medium site (1K–100K) | 1 req / sec | Standard courtesy |
| Large site (> 100K) | 2 req / sec | Can handle load |
| API with rate limit header | Follow header | Site-specified |
| During off-peak hours | 2x normal rate | Lower server load |

## Caching Strategy

| Cache Layer | TTL | Use Case |
|-------------|-----|----------|
| Local file cache | 24 hours | Repeated analysis of same pages |
| Database cache | 7 days | Cross-session research |
| CDN/proxy cache | Varies | Large-scale collection |
| No cache | — | Real-time price monitoring (use API) |

## Legal Framework

| Jurisdiction | Key Regulation | Impact on Scraping |
|-------------|---------------|-------------------|
| US | CFAA, hiQ v LinkedIn | Public data generally OK; auth bypass = risky |
| EU | GDPR | PII scraping requires consent or legitimate interest |
| Brazil | LGPD | Similar to GDPR; PII requires legal basis |
| General | Copyright | Scraping content ≠ right to republish |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Ignoring robots.txt | Legal risk + IP ban |
| No rate limiting | Server overload, IP ban, potential DDoS liability |
| Scraping login-required content | ToS violation, potential CFAA violation |
| Storing PII without consent | GDPR/LGPD fines |
| No attribution | Ethical violation + potential copyright claim |
| Scraping when API exists | Fragile selectors vs stable endpoints |

## Linked Artifacts

- `p01_kc_source_triangulation` — ethical sourcing feeds triangulation quality
- `p01_kc_seo_technical` — understanding site structure aids ethical scraping
- `p01_kc_confidence_scoring` — scraped data gets lower initial confidence

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_scraping_config]] | downstream | 0.26 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.20 |
| [[p04_browser_web_scraping]] | downstream | 0.19 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.18 |
| [[prompt-cache-builder]] | downstream | 0.18 |
| [[kc_api_reference]] | sibling | 0.17 |
| [[p04_browser_tool_NAME]] | downstream | 0.17 |
| [[bld_tools_prompt_cache]] | downstream | 0.17 |
| [[p03_sp_prompt_cache_builder]] | downstream | 0.17 |
| [[ex_knowledge_card_prompt_caching]] | sibling | 0.17 |
