---
kind: knowledge_card
id: bld_knowledge_card_social_publisher
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for social publisher pipeline design
sources: Ayrshare API docs, Meta Graph API, Postiz docs, social media best forctices, {{BRAND_NAME}} production system (9352 lines)
quality: 9.1
title: "Knowledge Card Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: social_publisher

## Executive Summary
A social publisher is a config-driven pipeline that automates posting to social networks. It reads a product/content catalog, generates captions via LLM, optimizes posting times per platform, publishes via API, logs results, and rotates content to prevent repetition. The CEX social-publisher-builder distills a 9352-line hardcoded system into a reusable pattern where any business fills 1 YAML config and gets automated posting.

## Pipeline — 10 Steps
| Step | Name | Input | Output | Failure Mode |
|------|------|-------|--------|-------------|
| 1 | LOAD | config YAML path | parsed config object | FileNotFound → abort |
| 2 | FETCH | catalog source URL/path | product/content list | API timeout → retry 3x |
| 3 | SELECT | content list + rotation state | next item (respects cooldown) | empty queue → skip cycle |
| 4 | GENERATE | item + persona + tone | caption text | LLM error → fallback template |
| 5 | OPTIMIZE | platform + timezone | best posting datetime | missing data → default schedule |
| 6 | HASHTAGS | niche + brand tags + limits | hashtag string | over limit → truncate |
| 7 | PUBLISH | caption + media + platform + API | post ID + URL | API error → retry + backoff |
| 8 | LOG | post result + metadata | structured JSON log | log failure → stderr + continue |
| 9 | NOTIFY | post URL + channel config | notification sent | channel down → skip |
| 10 | ROTATE | posted item ID + cooldown | rotation state updated | state corrupt → rebuild |

## Platform Matrix
| Platform | API | Max Caption | Max Hashtags | Image Sizes | Best Times |
|----------|-----|------------|--------------|-------------|------------|
| Instagram | Meta Graph / Ayrshare | 2200 chars | 30 (rec: 5-10) | 1080×1080, 1080×1350 | 11-13h, 19-21h |
| Facebook | Meta Graph / Ayrshare | 63206 chars | no limit (rec: 3-5) | 1200×630 | 13-16h |
| TikTok | Ayrshare / Postiz | 2200 chars | 5-8 | 1080×1920 (video) | 19-22h |
| LinkedIn | Ayrshare / Postiz | 3000 chars | 3-5 | 1200×627 | 8-10h, 17-18h |
| Twitter/X | Ayrshare / Postiz | 280 chars | 2-3 | 1200×675 | 9-11h, 12-13h |

## Publisher APIs
| Provider | Type | Networks | Pricing | Key Feature |
|----------|------|----------|---------|-------------|
| Ayrshare | SaaS | 6+ (IG,FB,TT,LI,TW,YT) | $29-399/mo | Unified API, scheduling, analytics |
| Postiz | Self-hosted OSS | 6+ | Free (self-host) | Full control, no vendor lock-in |
| Meta Graph | Direct API | IG, FB only | Free (rate limited) | No middleman, full IG/FB features |

## Anti-Patterns
| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Hardcoded company names | Zero reusability; every new client = fork |
| API keys in config files | Security breach; must use ENV_VAR |
| No cooldown/rotation | Same product posted repeatedly → unfollows |
| Single API provider | Vendor lock-in; Ayrshare outage = total stop |
| Posting without quality gate | Low-quality captions damage brand |
| Ignoring timezone | Posts at 3am local time → zero engagement |
