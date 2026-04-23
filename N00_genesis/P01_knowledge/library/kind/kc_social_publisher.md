---
id: p01_kc_social_publisher
kind: knowledge_card
type: kind
pillar: P04
title: "Social Publisher — Deep Knowledge for social_publisher"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: social_publisher
quality: 9.1
tags: [social_publisher, P04, PRODUCE, kind-kc, social-media, automation]
tldr: "10-stage auto-posting pipeline (LOAD>FETCH>SELECT>GENERATE>OPTIMIZE>HASHTAGS>PUBLISH>LOG>NOTIFY>ROTATE) that transforms content into platform-optimized social posts with scheduling and analytics"
when_to_use: "Building, reviewing, or reasoning about social_publisher artifacts"
keywords: [social_publisher, social_media, auto_posting, scheduling, instagram, linkedin, twitter]
feeds_kinds: [social_publisher]
density_score: null
related:
  - n02_tool_social_publisher
  - p03_sp_social_publisher_builder
  - social-publisher-builder
  - bld_knowledge_card_social_publisher
  - bld_instruction_social_publisher
  - n02_kc_social_publishing
  - p01_kc_ayrshare_api
  - n02_leverage_map_v2_iteration2
  - tpl_social_publisher
  - p11_qg_social_publisher
---

# Social Publisher

## Spec
```yaml
kind: social_publisher
pillar: P04
llm_function: PRODUCE
max_bytes: 5120
naming: p04_sp_{{name}}.md
core: false
```

## What It Is
A social_publisher is a 10-stage automated posting pipeline that transforms source content into platform-optimized social media posts. Stages: LOAD (ingest content), FETCH (pull platform context/trends), SELECT (choose content piece + platform), GENERATE (create post copy), OPTIMIZE (platform-specific formatting), HASHTAGS (research + attach tags), PUBLISH (post via API), LOG (record result), NOTIFY (alert on success/failure), ROTATE (schedule next batch). It is NOT a notifier (which sends alerts to users, not public posts) nor a schedule (which defines timing, not content generation). The social_publisher answers "how does content become social posts?" — notifier answers "how do I alert someone?" and schedule answers "when does something run?".

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| Buffer | Queue + Publish + Analytics | PUBLISH+LOG+ROTATE stages |
| Hootsuite | Composer + Scheduler + Analytics | GENERATE+PUBLISH+LOG pipeline |
| Later | Media Library + Calendar + Linkin.bio | LOAD+SELECT+PUBLISH with visual-first |
| Meta Business Suite | Creator Studio + Scheduler | Native PUBLISH+LOG for Instagram/Facebook |
| Typefully | Thread composer + scheduling | Twitter/X focused GENERATE+OPTIMIZE+PUBLISH |
| Zapier + Make | Trigger -> Format -> Post | Automation-based LOAD+GENERATE+PUBLISH |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| platforms | list[str] | required | instagram, linkedin, twitter, tiktok, youtube |
| content_source | str | required | RSS, CMS, manual, knowledge_card pool |
| posting_frequency | str | daily | More frequent = more reach but content fatigue |
| optimization_level | str | basic | basic / platform_native / ai_rewrite |
| hashtag_strategy | str | trending | trending / niche / branded / mixed |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Content repurposing pipeline | One source, many platforms | Blog post -> Twitter thread + LinkedIn post + IG carousel |
| Trend-responsive posting | Maximize engagement | FETCH trending topics; GENERATE timely content |
| Evergreen rotation | Consistent posting without new content | ROTATE through top-performing past posts |
| A/B post testing | Optimize copy/format | GENERATE 2 variants; PUBLISH to segments; LOG winner |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Same copy everywhere | Platform mismatch kills engagement | OPTIMIZE per platform (280 chars Twitter vs 3000 LinkedIn) |
| No LOG stage | Cannot measure or improve | Log impressions, clicks, engagement per post |
| Manual hashtags | Stale tags, missed trends | Use HASHTAGS stage with trend API or AI research |

## Integration Graph
```
[content_source] --> [LOAD] --> [FETCH] --> [SELECT]
                                               |
                   [NOTIFY] <-- [LOG] <-- [PUBLISH] <-- [HASHTAGS] <-- [OPTIMIZE] <-- [GENERATE]
                      |
                   [ROTATE] --> [next cycle]
```

## Decision Tree
- IF need user-facing alerts (Slack, email, SMS) THEN use notifier
- IF need time-based trigger only THEN use schedule
- IF need ad campaign management THEN use content_monetization
- IF need automated social media posting pipeline THEN social_publisher
- DEFAULT: social_publisher when content needs to reach social platforms automatically

## Quality Criteria
- GOOD: At least 2 platforms; content_source defined; PUBLISH stage with API integration
- GREAT: All 10 stages; per-platform OPTIMIZE; hashtag research; A/B testing; analytics LOG with engagement tracking; ROTATE with evergreen strategy
- FAIL: No platform optimization; missing LOG; no PUBLISH API integration; hardcoded hashtags

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_tool_social_publisher]] | related | 0.36 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.35 |
| [[social-publisher-builder]] | related | 0.32 |
| [[bld_knowledge_card_social_publisher]] | sibling | 0.32 |
| [[bld_instruction_social_publisher]] | upstream | 0.31 |
| [[n02_kc_social_publishing]] | sibling | 0.28 |
| [[p01_kc_ayrshare_api]] | sibling | 0.27 |
| [[n02_leverage_map_v2_iteration2]] | downstream | 0.27 |
| [[tpl_social_publisher]] | related | 0.26 |
| [[p11_qg_social_publisher]] | downstream | 0.26 |
