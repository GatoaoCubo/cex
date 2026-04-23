---
id: p01_kc_seo_technical
kind: knowledge_card
type: domain
pillar: P01
title: "Technical SEO Patterns"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, seo, meta-tags, structured-data, core-web-vitals, search]
tldr: "Meta tags, structured data, sitemaps, Core Web Vitals. For N02 frontend output needing search visibility. Actionable checklist per page type."
when_to_use: "When generating landing pages, blog posts, product pages, or any content that must rank in search engines."
keywords: [seo, meta-tags, structured-data, core-web-vitals, schema-org, sitemap]
density_score: 0.94
related:
  - p01_kc_seo_content_strategy_ecommerce
  - bld_schema_landing_page
  - bld_system_prompt_landing_page
  - landing-page-builder
  - bld_examples_function_def
  - bld_collaboration_search_tool
  - p01_kc_vision_tool
  - bld_tools_landing_page
  - bld_knowledge_card_landing_page
  - bld_instruction_landing_page
---

# Technical SEO Patterns

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Structured markup + performance + crawlability = search visibility |
| Trigger | Any public-facing HTML output from N02 or N03 |
| Benefit | Organic traffic without ad spend; AI search readiness |
| Risk if skipped | Invisible to search engines despite quality content |

## Required Elements per Page

| Element | Constraint | Impact | Priority |
|---------|-----------|--------|----------|
| `<title>` | 50–60 chars, keyword-first | High | Required |
| `<meta description>` | 150–160 chars, CTA included | Medium | Required |
| `<h1>` | Exactly one per page, matches title intent | High | Required |
| Canonical URL | `<link rel="canonical">` | Medium | Required |
| JSON-LD (Schema.org) | Match content type (Article, Product, FAQ) | High | Recommended |
| Open Graph tags | og:title, og:description, og:image | Medium | Recommended |
| Twitter Card | twitter:card, twitter:title | Low | Optional |
| Hreflang | Multi-language sites only | Medium | Conditional |

## Core Web Vitals Targets

| Metric | Good | Needs Work | Poor | How to Fix |
|--------|------|-----------|------|-----------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s | Optimize images, preload fonts |
| INP (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms | Reduce JS, defer non-critical |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 | Set image dimensions, avoid dynamic inject |

## Structured Data Types

| Content Type | Schema.org Type | Required Properties |
|-------------|----------------|-------------------|
| Blog post | Article | headline, author, datePublished, image |
| Product page | Product | name, price, availability, review |
| FAQ page | FAQPage | mainEntity (Question + Answer pairs) |
| How-to guide | HowTo | name, step (HowToStep array) |
| Local business | LocalBusiness | name, address, telephone, openingHours |
| Software | SoftwareApplication | name, operatingSystem, applicationCategory |

## Crawlability Checklist

| Item | Check | Tool |
|------|-------|------|
| robots.txt allows crawling | `Allow: /` for key paths | robots.txt validator |
| XML sitemap exists | All indexable URLs listed | sitemap generator |
| No orphan pages | Every page reachable via internal links | Screaming Frog / Ahrefs |
| Canonical tags consistent | No conflicting canonicals | Site crawl audit |
| 404s handled | Custom 404, no broken links | Link checker |
| HTTPS everywhere | No mixed content | SSL checker |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Keyword stuffing | Penalized by search engines since 2012 |
| Duplicate titles across pages | Confuses crawlers, dilutes ranking |
| Missing alt text on images | Lost accessibility + image search traffic |
| JavaScript-only rendering | Crawlers may not execute JS |
| Ignoring mobile | Mobile-first indexing since 2021 |
| No structured data | Misses rich snippet opportunities |

## Linked Artifacts

- `p01_kc_web_scraping_ethics` — ethical considerations when scraping competitor SEO
- `p01_kc_output_formatting` — structured output templates for SEO elements
- `p01_kc_pattern_extraction` — extract SEO patterns from top-ranking pages

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_seo_content_strategy_ecommerce]] | sibling | 0.29 |
| [[bld_schema_landing_page]] | downstream | 0.21 |
| [[bld_system_prompt_landing_page]] | downstream | 0.20 |
| [[landing-page-builder]] | downstream | 0.20 |
| [[bld_examples_function_def]] | downstream | 0.19 |
| [[bld_collaboration_search_tool]] | downstream | 0.18 |
| [[p01_kc_vision_tool]] | sibling | 0.17 |
| [[bld_tools_landing_page]] | downstream | 0.17 |
| [[bld_knowledge_card_landing_page]] | sibling | 0.17 |
| [[bld_instruction_landing_page]] | downstream | 0.16 |
