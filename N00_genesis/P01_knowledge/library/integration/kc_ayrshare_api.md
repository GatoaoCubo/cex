---
id: p01_kc_ayrshare_api
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Ayrshare Social API — Multi-Platform Publishing for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: ayrshare_api
quality: 9.1
tags: [ayrshare, social-media, api, publishing, scheduling, content-factory, integration, INJECT]
tldr: "Single API to post, schedule, and track content across Instagram, TikTok, LinkedIn, Twitter/X, Facebook, and YouTube"
when_to_use: "When any nucleus needs to publish or schedule content across multiple social media platforms simultaneously"
keywords: [ayrshare, social-media, multi-platform, scheduling, instagram, tiktok, linkedin, twitter]
feeds_kinds: [api_client, workflow, dag, schedule]
linked_artifacts: [kc_youtube_api, kc_canva_connect_api]
density_score: null
related:
  - p01_kc_canva_connect_api
  - p01_kc_runway_api
  - bld_tools_social_publisher
  - p12_wf_cf_publish_social
  - kc_api_reference
  - bld_knowledge_card_social_publisher
  - p01_kc_elevenlabs_tts
  - p01_kc_social_publisher
  - bld_output_template_integration_guide
  - n06_api_access_pricing
---

# Ayrshare Social API

## Quick Reference
```yaml
base_url: https://api.ayrshare.com/api
auth: "Authorization: Bearer AYRSHARE_API_KEY" header
platforms: [instagram, tiktok, linkedin, twitter, facebook, youtube, pinterest, telegram, reddit, threads]
rate_limit: 100 requests/min (Premium), 30/min (Business)
content_type: application/json
```

## Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/post` | POST | Publish or schedule a post |
| `/post` | GET | List posts (with filters) |
| `/post/{id}` | GET | Get post details + analytics |
| `/delete` | DELETE | Delete a published post |
| `/analytics/post` | POST | Get post-level analytics |
| `/analytics/social` | GET | Get platform-level analytics |
| `/media/upload` | POST | Upload media (returns URL for use in /post) |
| `/user` | GET | Get connected accounts info |
| `/history` | GET | Post history with status |

## Publish to Multiple Platforms at Once

```python
import httpx

headers = {
    "Authorization": f"Bearer {AYRSHARE_API_KEY}",
    "Content-Type": "application/json"
}

# Post image + caption to 4 platforms simultaneously
resp = httpx.post("https://api.ayrshare.com/api/post", headers=headers, json={
    "post": "5 dicas de produtividade com IA que vão transformar seu workflow 🚀\n\n1. Automatize a criação de thumbnails\n2. Use TTS para narração\n3. Gere clips com IA\n4. Agende posts em lote\n5. Monitore métricas automaticamente\n\n#ia #produtividade #contentcreator",
    "platforms": ["instagram", "linkedin", "twitter", "facebook"],
    "mediaUrls": ["https://storage.example.com/post_image.jpg"],
    "hashtags": {
        "instagram": ["#ia", "#produtividade", "#marketingdigital", "#contentcreator"],
    },
    "shortenLinks": True
})

result = resp.json()
# Returns: { "id": "abc123", "postIds": [{"platform": "instagram", "id": "..."}, ...] }
```

## Schedule Future Post

```python
resp = httpx.post("https://api.ayrshare.com/api/post", headers=headers, json={
    "post": "Novo vídeo no canal! Link na bio 👆",
    "platforms": ["instagram", "twitter", "linkedin"],
    "mediaUrls": ["https://storage.example.com/promo.jpg"],
    "scheduleDate": "2026-04-07T13:00:00Z",   # UTC — 10:00 BRT
    "autoSchedule": False   # True = Ayrshare picks optimal time per platform
})
```

## Platform-Specific Content

```python
resp = httpx.post("https://api.ayrshare.com/api/post", headers=headers, json={
    "platforms": ["instagram", "linkedin", "tiktok"],

    # Default post (used if no platform override)
    "post": "Check out our new AI guide!",
    "mediaUrls": ["https://storage.example.com/video.mp4"],

    # Platform overrides
    "instagramOptions": {
        "post": "Novo guia de IA! 🤖 Salva pra depois ☝️\n\n#ia #guia",
        "reels": True,           # Post as Reel instead of feed post
        "shareReelToFeed": True,
        "coverUrl": "https://storage.example.com/cover.jpg"
    },
    "linkedinOptions": {
        "post": "Acabamos de lançar nosso guia completo de IA para criadores de conteúdo.\n\nO que você vai encontrar:\n→ Workflow completo\n→ Ferramentas testadas\n→ ROI real medido\n\nLink no primeiro comentário.",
        "visibility": "PUBLIC",
        "mediaDescription": "AI Guide for Content Creators"
    },
    "tiktokOptions": {
        "post": "O guia que faltava 🎯 #ia #dicasdeconteudo #produtividade",
        "privacy": "PUBLIC_TO_EVERYONE",
        "disableDuet": False,
        "disableStitch": False
    }
})
```

## Upload Media (before posting)

```python
# Upload image or video first, get hosted URL
resp = httpx.post("https://api.ayrshare.com/api/media/upload", headers=headers, json={
    "file": "https://your-server.com/video.mp4"   # URL to fetch from
    # OR use multipart upload for local files
})
media_url = resp.json()["url"]   # Use this in mediaUrls

# For local files:
with open("video.mp4", "rb") as f:
    resp = httpx.post("https://api.ayrshare.com/api/media/upload",
        headers={"Authorization": f"Bearer {AYRSHARE_API_KEY}"},
        files={"file": ("video.mp4", f, "video/mp4")}
    )
```

## Get Analytics

```python
# Post-level analytics
resp = httpx.post("https://api.ayrshare.com/api/analytics/post", headers=headers, json={
    "id": "post_abc123",
    "platforms": ["instagram", "linkedin"]
})
# Returns: likes, comments, shares, impressions, reach per platform

# Platform-level analytics (overall account)
resp = httpx.get("https://api.ayrshare.com/api/analytics/social?platforms=instagram,linkedin",
    headers=headers)
# Returns: followers, engagement rate, top posts
```

## Media Requirements by Platform

| Platform | Image | Video | Max Duration | Max File Size |
|----------|-------|-------|-------------|---------------|
| Instagram Feed | JPG/PNG 1080x1080 | MP4 H.264 | 60min | 100MB |
| Instagram Reels | — | MP4 9:16 1080x1920 | 90s | 100MB |
| TikTok | — | MP4 9:16 1080x1920 | 10min | 72MB |
| LinkedIn | JPG/PNG | MP4 | 10min | 200MB |
| Twitter/X | JPG/PNG/GIF | MP4 | 2:20 | 512MB |
| Facebook | JPG/PNG | MP4 | 240min | 4GB |
| YouTube | — | MP4 | 12h | 256GB |

## Pricing

| Plan | Profiles | Posts/mo | Cost |
|------|----------|---------|------|
| Premium | 1 | 100 | $49/mo |
| Business | 3 | 300 | $99/mo |
| Enterprise | 10+ | Unlimited | Custom |

Content Factory estimate: Business plan at $99/mo covers 3 brand profiles × 100 posts each = plenty for weekly content.

## Gotchas

- **Instagram requires a linked Facebook Business Page.** Connect via Ayrshare dashboard. Personal IG accounts cannot use the API.
- **TikTok videos must be 9:16 vertical.** Landscape videos get rejected or awkwardly cropped. Always export from FFmpeg in 1080x1920.
- **`scheduleDate` is UTC.** Brazil is UTC-3. Schedule for 13:00Z to post at 10:00 BRT.
- **Reel vs Feed**: set `instagramOptions.reels: true` explicitly. Default is feed post.
- **LinkedIn text max: 3,000 chars.** Twitter: 280 chars. Instagram caption: 2,200 chars. Tailor per platform.
- **Media URLs must be publicly accessible.** Ayrshare fetches the URL server-side. Pre-signed S3 URLs or public CDN URLs work.
- **Auto-delete**: posts scheduled then deleted via API are removed from schedule but not from platforms if already published.
- **Rate limit 429**: Premium = 100 req/min. Batch your posts rather than sending one at a time.
- **Analytics lag**: Instagram/TikTok analytics may take 24-48h to populate. Don't poll immediately after posting.

## Docs
- API Reference: https://docs.ayrshare.com/
- Platform setup: https://docs.ayrshare.com/social-networks
- Webhooks: https://docs.ayrshare.com/webhooks (get notified on post success/failure)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_canva_connect_api]] | sibling | 0.29 |
| [[p01_kc_runway_api]] | sibling | 0.28 |
| [[bld_tools_social_publisher]] | downstream | 0.27 |
| [[p12_wf_cf_publish_social]] | downstream | 0.26 |
| [[kc_api_reference]] | sibling | 0.24 |
| [[bld_knowledge_card_social_publisher]] | sibling | 0.24 |
| [[p01_kc_elevenlabs_tts]] | sibling | 0.23 |
| [[p01_kc_social_publisher]] | sibling | 0.23 |
| [[bld_output_template_integration_guide]] | downstream | 0.22 |
| [[n06_api_access_pricing]] | downstream | 0.22 |
