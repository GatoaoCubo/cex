---
id: p03_ap_cf_generate_campaign
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate Social Media Campaign"
action: "Generate a multi-platform social media campaign with adapted posts, hashtags, and scheduling plan from content and platforms"
input_required:
  - "content: string — content to promote (course, ebook, video, product)"
  - "platforms: list[string] — target platforms (instagram, linkedin, twitter, tiktok, youtube)"
  - "campaign_days: integer — campaign duration in days (default 7)"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Platform-adapted posts with copy, hashtags, visual directions, and 7-day posting schedule"
purpose: "Transform any content asset into a ready-to-publish social campaign across all platforms via Ayrshare"
steps_count: 5
timeout: "90s"
edge_cases:
  - "Single platform — still generate 7 post variants (carousel, story, reel, static)"
  - "Content is a URL only — extract key points from URL metadata for post copy"
  - "Platform not in supported list — skip with warning, do not invent format"
constraints:
  - "Do NOT publish directly — output feeds into wf_cf_publish_social"
  - "Character limits: Twitter 280, LinkedIn 3000, Instagram caption 2200, TikTok 2200"
  - "Hashtag count: Instagram 20-30, LinkedIn 3-5, Twitter 2-3"
domain: "content_factory"
quality: null
tags: [action_prompt, content_factory, campaign, social_media, ayrshare]
tldr: "Generate multi-platform social campaign (posts + hashtags + schedule) from content for Ayrshare distribution"
density_score: 0.93
---

## Context
Every content factory output (course, video, ebook) needs social promotion. This prompt
generates platform-adapted posts, respecting each network's format, character limits,
and engagement patterns. Output feeds directly into Ayrshare for scheduled publishing.
Purpose: ensure no content is created without a corresponding distribution campaign.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| content | string | Description or reference to content asset | YES |
| platforms | list[string] | Platform identifiers | YES |
| campaign_days | integer | 1-30 | NO (default 7) |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Analyze content to extract 5-7 key hooks (pain points, benefits, quotes)
2. For each platform, generate daily posts adapted to format and character limits
3. Create hashtag sets per platform (respecting count limits)
4. Design visual direction per post (Canva template type: carousel, story, static, reel cover)
5. Build posting schedule with optimal times per platform (morning/afternoon/evening)

## Output
Format: YAML + Markdown
Structure:
```yaml
campaign:
  content_ref: "{{content}}"
  duration_days: {{days}}
  platforms:
    instagram:
      posts:
        - day: 1
          type: "carousel"
          caption: "{{caption ≤2200 chars}}"
          hashtags: ["{{h1}}", "{{h2}}"]
          visual: "brand_carousel_template"
          time: "10:00"
    linkedin:
      posts:
        - day: 1
          type: "article"
          text: "{{text ≤3000 chars}}"
          hashtags: ["{{h1}}", "{{h2}}", "{{h3}}"]
          time: "08:00"
```

## Validation
- Posts present for every platform in platforms input
- Character limits respected per platform
- Hashtag counts within platform ranges
- Schedule covers all campaign_days with at least 1 post/day/platform
- Edge case: single platform has format variety (not 7 identical posts)

## References
- Ayrshare API (publishing downstream)
- Canva API (visual asset creation)
- wf_cf_publish_social (distribution workflow)
