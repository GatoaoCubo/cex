---
id: tpl_content_distribution_plan
kind: prompt_template
8f: F6_produce
pillar: P03
title: "Content Distribution Plan — NotebookLM Outputs to Multi-Channel Publishing"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: n02_marketing
mission: OPTIMIZE_FACTORY
nucleus: N02
variables:
  - name: BRAND_NAME
    type: string
    required: true
    default: null
    description: "Brand name for channel-specific adaptations"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Tone descriptor for copy consistency across channels"
  - name: TOPIC
    type: string
    required: true
    default: null
    description: "Content topic being distributed"
  - name: CONTENT_ASSETS
    type: list
    required: true
    default: null
    description: "List of generated assets (e.g. audio_overview, flashcards, quiz, mind_map, slides)"
  - name: TARGET_AUDIENCE
    type: string
    required: true
    default: null
    description: "Primary audience persona"
  - name: DISTRIBUTION_CHANNELS
    type: list
    required: true
    default: null
    description: "Target channels — youtube, spotify, instagram, linkedin, newsletter, tiktok, twitter_x, website"
  - name: LAUNCH_DATE
    type: string
    required: false
    default: null
    description: "Target publish date (ISO format) — drives the schedule"
  - name: CAMPAIGN_DURATION
    type: string
    required: false
    default: "7d"
    description: "Campaign window — 3d, 7d, 14d, 30d"
  - name: CONTENT_GOAL
    type: string
    required: true
    default: null
    description: "Primary goal — awareness, engagement, conversion, retention"
  - name: CTA
    type: string
    required: true
    default: null
    description: "Unified call-to-action across all channels"
  - name: BUDGET
    type: string
    required: false
    default: "$0"
    description: "Paid promotion budget (organic-first by default)"
variable_syntax: mustache
composable: true
domain: content_factory
quality: 9.1
tags: [prompt_template, distribution, publishing, channels, social, content_factory, N02]
tldr: "Generates a tactical distribution plan that maps NotebookLM content assets to specific channels, formats, posting times, and copy — turning one production run into a multi-channel campaign"
keywords: [distribution, publishing, social media, youtube, spotify, linkedin, instagram, newsletter, content factory]
density_score: null
related:
  - wf_kc_to_content
  - bld_schema_pitch_deck
  - bld_schema_tts_provider
  - bld_schema_rl_algorithm
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_config
  - schedule_instagram_content_plan
  - bld_schema_dataset_card
  - bld_schema_voice_pipeline
---

# Content Distribution Plan — NotebookLM Outputs to Channels

## Purpose

You produced the content. Audio overview, flashcards, quiz, mind map, slides. All sitting in a notebook, branded and formatted. Now what?

Without a distribution plan, that content dies in a folder. One brilliant podcast episode that nobody hears. Seventy-five flashcards that nobody studies. A quiz that nobody takes.

This template turns a pile of assets into a coordinated multi-channel campaign. It decides WHERE each asset goes, WHEN it publishes, WHAT copy accompanies it, and HOW the pieces cross-promote each other. The goal is simple: one production run, maximum surface area.

Used after all NotebookLM outputs are generated and formatted, and before the publishing workflows (`wf_cf_publish_*`) execute.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | -- | Brand identity |
| BRAND_VOICE | string | yes | -- | Tone control |
| TOPIC | string | yes | -- | Content subject |
| CONTENT_ASSETS | list | yes | -- | Available assets |
| TARGET_AUDIENCE | string | yes | -- | Audience persona |
| DISTRIBUTION_CHANNELS | list | yes | -- | Target channels |
| LAUNCH_DATE | string | no | -- | Publish date |
| CAMPAIGN_DURATION | string | no | 7d | Campaign window |
| CONTENT_GOAL | string | yes | -- | Primary goal |
| CTA | string | yes | -- | Unified CTA |
| BUDGET | string | no | $0 | Promo budget |

## Template Body

```
You are a content distribution strategist for {{BRAND_NAME}}. Voice: {{BRAND_VOICE}}.

CONTEXT:
Topic: "{{TOPIC}}"
Audience: {{TARGET_AUDIENCE}}
Goal: {{CONTENT_GOAL}}
Budget: {{BUDGET}}
Campaign window: {{CAMPAIGN_DURATION}} starting {{LAUNCH_DATE}}

Available content assets:
{{CONTENT_ASSETS}}

Target channels:
{{DISTRIBUTION_CHANNELS}}

Unified CTA: {{CTA}}

---

## OUTPUT: DISTRIBUTION MATRIX

### Asset-to-Channel Mapping

For EACH asset in {{CONTENT_ASSETS}}, specify:

| Asset | Channel | Format Adaptation | Post Type | Day |
|-------|---------|-------------------|-----------|-----|
| audio_overview | YouTube | Full episode + chapters + thumbnail | Long-form | D1 |
| audio_overview | Spotify | Podcast episode + show notes | Audio | D1 |
| audio_overview | Instagram | 60s highlight clip + carousel | Reel + Post | D2 |
| audio_overview | LinkedIn | Key insight quote + episode link | Text post | D2 |
| audio_overview | Newsletter | Episode summary + embedded player | Email | D3 |
| flashcards | Instagram | 5-card carousel (best-of selection) | Carousel | D3 |
| flashcards | LinkedIn | "Test yourself" interactive post | Poll/Post | D4 |
| flashcards | Website | Embedded Anki/Quizlet widget | Page | D1 |
| quiz | Instagram | Story quiz (3 questions) | Story | D5 |
| quiz | Newsletter | "How much did you learn?" CTA | Email | D5 |
| mind_map | LinkedIn | Visual + breakdown in caption | Image post | D4 |
| mind_map | Instagram | Full-size image + zoom Story | Post + Story | D6 |
| slides | LinkedIn | SlideShare/PDF carousel upload | Document | D3 |
| slides | YouTube | Narrated slideshow (TTS + slides) | Short video | D7 |

### Publishing Schedule

Generate a day-by-day schedule for {{CAMPAIGN_DURATION}}:

| Day | Time (BRT) | Channel | Content | Copy Hook | CTA |
|-----|------------|---------|---------|-----------|-----|
| D1 (Launch) | 09:00 | YouTube | Full audio episode | [HOOK: curiosity about {{TOPIC}}] | {{CTA}} |
| D1 | 09:00 | Spotify | Same audio, podcast format | [Same hook, audio-native] | {{CTA}} |
| D1 | 12:00 | LinkedIn | Launch announcement | [Authority angle] | Link to episode |
| D2 | 10:00 | Instagram | 60s audio clip (best moment) | [Scroll-stopper from episode] | Link in bio |
| D2 | 14:00 | Twitter/X | Thread: 5 key insights | [Numbered insights] | {{CTA}} |
| D3 | 08:00 | Newsletter | Episode recap + flashcards | [Value-first subject line] | {{CTA}} |
| D3 | 11:00 | Instagram | Flashcard carousel (5 cards) | [Learn this in 30 seconds] | Save + share |
| D4 | 10:00 | LinkedIn | Mind map visual | [Big picture view] | {{CTA}} |
| D4 | 15:00 | LinkedIn | Quiz question poll | [Test yourself] | Comment answer |
| D5 | 09:00 | Instagram | Story quiz (3 questions) | [Swipe to play] | Visit link |
| D5 | 12:00 | Newsletter | "Results are in" follow-up | [Engagement callback] | {{CTA}} |
| D6 | 10:00 | Instagram | Mind map zoomed + breakdown | [Deep dive visual] | Save this |
| D7 | 09:00 | YouTube | Narrated slide summary | [2-min recap for busy people] | {{CTA}} |
| D7 | 14:00 | All channels | Campaign recap + evergreen pin | [Best-performing repost] | {{CTA}} |

### Copy Guidelines Per Channel

For EACH channel in {{DISTRIBUTION_CHANNELS}}, write:

**YouTube**:
- Title: "[NUMBER] Things About {{TOPIC}} That [OUTCOME]" (max 60 chars)
- Description: 3 paragraphs — hook, chapter list, {{CTA}}
- Tags: 10-15 relevant tags
- Thumbnail text: max 4 words, high contrast on {{BRAND_COLORS}}

**Spotify**:
- Episode title: "{{TOPIC}} — [ANGLE]"
- Show notes: timestamps + key takeaways + {{CTA}}
- Episode description: 2 paragraphs max

**Instagram**:
- Reels: hook in first 3 seconds, text overlay, trending audio optional
- Carousels: 5-10 slides, first slide = hook, last slide = CTA
- Stories: interactive elements (poll, quiz, slider)
- Caption: hook line + value + {{CTA}} + 10-15 hashtags

**LinkedIn**:
- Posts: hook line (contrarian or insight) + 3-5 short paragraphs + {{CTA}}
- Documents: PDF carousel with brand header on each slide
- Polls: frame as knowledge test from flashcards

**Newsletter**:
- Subject line: curiosity-driven, under 50 chars, no spam triggers
- Preview text: complete the subject line's thought
- Body: personal greeting + value + {{CTA}} + P.S. with bonus
- Frequency: max 2 emails per campaign

**Twitter/X**:
- Thread: numbered insights, 1 idea per tweet, max 280 chars each
- Solo tweet: best single insight + link
- Quote retweet strategy: engage with audience replies

### Cross-Promotion Map

Show how each piece drives traffic to the others:

```
YouTube episode
  mentions --> "Flashcards in the description"
  mentions --> "Quiz on our Instagram Stories"
  end screen --> Next episode + Subscribe

Spotify episode
  show notes --> Website (flashcards + quiz)
  CTA --> "Share on LinkedIn"

Instagram carousel
  last slide --> "Full episode on YouTube/Spotify"
  Story --> Swipe-up to quiz

LinkedIn post
  body --> "Full breakdown in our latest episode [LINK]"
  comments --> Pin flashcard image

Newsletter
  body --> Links to YouTube + Spotify + Instagram
  P.S. --> "Share the flashcards with your team"
```

### Performance Tracking

| Metric | Channel | Target | Tool |
|--------|---------|--------|------|
| Views/Listens | YouTube, Spotify | 500+ in 7d | Platform analytics |
| Engagement rate | Instagram, LinkedIn | 5%+ | Ayrshare analytics |
| Click-through | Newsletter | 15%+ | Email provider |
| Saves/Shares | Instagram | 50+ | Platform analytics |
| Quiz completions | Instagram Stories | 100+ | Story insights |
| Flashcard imports | Website | 25+ | Supabase tracking |

## CONSTRAINTS
- NEVER publish the same copy on two channels — adapt for each platform
- Every post MUST include {{CTA}} in some form
- Organic-first strategy: only use {{BUDGET}} for boosting top-performing D1-D3 posts
- Respect platform rate limits: max 1 post/channel/day (except Stories)
- All visual assets must use {{BRAND_COLORS}} and {{BRAND_NAME}} watermark
- Schedule times optimized for {{TARGET_AUDIENCE}} timezone (default BRT)
- Cross-promotion is mandatory — every post references at least one other asset
- Campaign must have a clear beginning (launch), middle (engagement), end (recap)
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^tpl_[a-z][a-z0-9_]+$ |
| H02 | PASS | All required frontmatter fields present |
| H03 | PASS | All {{vars}} in body exist in variables list |
| H04 | PASS | All variables in list appear in template body |
| H05 | PASS | File size < 8192 bytes |
| H06 | PASS | variable_syntax is mustache consistently |

## Examples

### Example: CEX 8F Pipeline — 7-Day Distribution

Variables:
```yaml
BRAND_NAME: "CEX"
BRAND_VOICE: "technical-confident-direct"
TOPIC: "8F Pipeline"
CONTENT_ASSETS: [audio_overview, flashcards, quiz, mind_map]
TARGET_AUDIENCE: "Developers who want to monetize knowledge as digital products"
DISTRIBUTION_CHANNELS: [youtube, spotify, linkedin, instagram, newsletter]
LAUNCH_DATE: "2026-04-15"
CAMPAIGN_DURATION: "7d"
CONTENT_GOAL: "awareness"
CTA: "Start building with CEX -- type /init in Claude Code"
BUDGET: "$0"
```

Day 1 LinkedIn post (rendered):
```
Most AI frameworks give you a chatbot.
CEX gives you a factory.

5 words of input. 8 functions of reasoning.
1 production-ready artifact out the other side.

We broke down the 8F Pipeline in a new deep-dive episode:
- F1 CONSTRAIN: why boundaries create better output
- F4 REASON: where GDP gates kick in
- F7 GOVERN: the quality loop that catches what you miss

Full episode: [YOUTUBE_LINK]
75 flashcards: [WEBSITE_LINK]

Start building with CEX -- type /init in Claude Code.
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[wf_kc_to_content]] | downstream | 0.33 |
| [[bld_schema_pitch_deck]] | downstream | 0.29 |
| [[bld_schema_tts_provider]] | downstream | 0.29 |
| [[bld_schema_rl_algorithm]] | downstream | 0.29 |
| [[bld_schema_usage_report]] | downstream | 0.29 |
| [[bld_schema_quickstart_guide]] | downstream | 0.28 |
| [[bld_schema_sandbox_config]] | downstream | 0.28 |
| [[schedule_instagram_content_plan]] | related | 0.28 |
| [[bld_schema_dataset_card]] | downstream | 0.27 |
| [[bld_schema_voice_pipeline]] | downstream | 0.27 |
