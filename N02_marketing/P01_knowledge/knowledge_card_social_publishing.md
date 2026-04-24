---
id: n02_kc_social_publishing
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Knowledge Card — Social Media Auto-Publishing"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: social-publisher-builder
domain: social_publisher
nucleus: N02
quality: 9.1
tags: [knowledge-card, social-media, auto-publishing, N02, marketing, automation]
tldr: "Everything N02 needs to know about automated social publishing: APIs, platforms, content strategy, scheduling, and quality control."
density_score: 0.92
related:
  - bld_knowledge_card_social_publisher
  - p03_sp_social_publisher_builder
  - tpl_social_publisher
  - social-publisher-builder
  - n02_tool_social_publisher
  - bld_instruction_social_publisher
  - bld_architecture_social_publisher
  - p10_lr_social-publisher-builder
  - ex_social_publisher_saas
  - bld_examples_social_publisher
---

# Knowledge Card — Social Media Auto-Publishing

## Executive Summary
Automated social publishing transforms manual posting into a config-driven pipeline. A business fills ONE YAML config (identity, platforms, schedule, content mix, catalog source, publisher API, hashtags) and gets 24/7 automated posting with quality gates, rotation, retry, and logging. The CEX social-publisher-builder distilled this from a 9352-line production system into a reusable pattern.

## Core Concepts

### Content Mix Strategy
| Type | Purpose | Typical % | Example |
|------|---------|----------|---------|
| Product | Direct sales/showcase | 25-45% | Product photo + CTA |
| Educational | Build authority | 20-40% | "Did you know?" posts |
| Tips | Engagement/utility | 15-25% | "3 ways to..." |
| Trends | Relevance/discovery | 10-20% | Seasonal, memes, cultural |

**Rule**: product-heavy feeds lose followers. The 40/30/20/10 split (product/edu/tips/trends) is the baseline — adjust per niche.

### Publisher API Landscape
| Provider | Model | Best For | Limitation |
|----------|-------|----------|-----------|
| Ayrshare | SaaS unified API | Startups, agencies | $29/mo min, vendor lock-in |
| Postiz | Self-hosted OSS | Tech companies | Self-host overhead |
| Meta Graph | Direct Facebook/IG | IG/FB only shops | No TikTok/LinkedIn/Twitter |
| Buffer | SaaS + scheduling | SMBs | Limited API, expensive |
| Hootsuite | Enterprise | Large teams | Very expensive, complex |

### Posting Time Science
| Platform | Peak Hours (local) | Why |
|----------|-------------------|-----|
| Instagram | 11-13h, 19-21h | Lunch browse, evening scroll |
| Facebook | 13-16h | Afternoon work break |
| TikTok | 19-22h | Evening entertainment |
| LinkedIn | 8-10h, 17-18h | Before work, end of day |
| Twitter/X | 9-11h, 12-13h | Morning news, lunch scroll |

### Rotation & Cooldown
Without rotation, the algorithm shows the same product repeatedly → audience fatigue → unfollows. **Cooldown** = minimum days before same item can be re-posted.

| Niche | Recommended Cooldown | Rotation Strategy | Implementation |
|-------|---------------------|------------------|----------------|
| Fashion | 4-7 days | Seasonal buckets | Group by season, rotate within bucket |
| Food | 2-3 days | Meal-type rotation | Breakfast/lunch/dinner/snack cycles |
| SaaS | 7-14 days | Feature highlighting | Rotate through product features |
| Pet | 3-5 days | Product+lifestyle mix | Alternate products with care tips |

**Platform-Specific Rules:**
- **Instagram Stories**: 24h cooldown (disappears anyway)
- **TikTok**: 3-5 day cooldown (fast-moving feed)
- **LinkedIn**: 14+ day cooldown (professional audience notices repeats)
- **Facebook**: 7-10 day cooldown (longer content lifespan)

**Technical Implementation:**
```
last_posted_date + cooldown_days < current_date = eligible
Track per item_id + platform_id combination
Fallback: if no eligible content, extend search by 1 day
```

### Caption Generation
LLM generates captions from: product data + brand persona + tone + content type + platform constraints. Fallback to template if LLM fails.

| Element | Source |
|---------|--------|
| Product info | Catalog (Supabase/Shopify/API) |
| Brand voice | config.identity.tom + persona |
| Platform limits | Platform matrix (caption length, hashtags) |
| Content type | Calendar (product/edu/tips/trend) |

## Anti-Patterns
| Pattern | Problem | Fix |
|---------|---------|-----|
| Post-and-forget | No logging = no optimization | Structured JSON logs per post |
| Same time every day | Algorithm penalizes predictability | Vary ±30min around optimal |
| Only product posts | Audience treats as spam | Content mix 40/30/20/10 |
| Manual hashtags | Inconsistent, miss trending | Brand + niche + generated |
| Single platform | All eggs in one basket | Min 2 platforms |

## References
- Ayrshare API: https://docs.ayrshare.com
- Postiz: https://postiz.com
- Meta Graph API: https://developers.facebook.com/docs/graph-api
- Instagram Content Calendar Best Practices (Hootsuite, 2025)
- Social Media Posting Time Studies (Sprout Social, Buffer, 2025)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_social_publisher]] | sibling | 0.49 |
| [[p03_sp_social_publisher_builder]] | downstream | 0.48 |
| [[tpl_social_publisher]] | downstream | 0.42 |
| [[social-publisher-builder]] | downstream | 0.38 |
| [[n02_tool_social_publisher]] | downstream | 0.36 |
| [[bld_instruction_social_publisher]] | downstream | 0.35 |
| [[bld_architecture_social_publisher]] | downstream | 0.35 |
| [[p10_lr_social-publisher-builder]] | downstream | 0.31 |
| [[ex_social_publisher_saas]] | downstream | 0.31 |
| [[bld_examples_social_publisher]] | downstream | 0.30 |
