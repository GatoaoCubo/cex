---
id: p01_kc_runway_api
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Runway Gen-4 API — Video Generation for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: runway_api
quality: 9.1
tags: [runway, api, video, gen4, ai-video, content-factory, integration, INJECT]
tldr: "REST API for text-to-video and image-to-video generation with Gen-4 models — async job-based workflow"
when_to_use: "When any nucleus needs to generate AI video clips from text prompts or reference images"
keywords: [runway, gen4, text-to-video, image-to-video, video-generation, ai-video]
feeds_kinds: [api_client, workflow, dag]
linked_artifacts: [kc_ffmpeg_patterns, kc_elevenlabs_tts, kc_youtube_api]
density_score: null
related:
  - p01_kc_ayrshare_api
  - n06_content_factory_pricing
  - p01_kc_canva_connect_api
  - p01_kc_elevenlabs_tts
  - n06_pricing_content_factory
  - bld_knowledge_card_multi_modal_config
  - p01_kc_multi_modal_config
  - p01_kc_ffmpeg_patterns
  - kc_multimodal_prompt
  - bld_output_template_multi_modal_config
---

# Runway Gen-4 API

## Quick Reference
```yaml
base_url: https://api.dev.runwayml.com/v1
auth: "Authorization: Bearer RUNWAY_API_SECRET" header
models:
  - gen4_turbo         # Fastest. ~30s for 5s clip. Lower quality.
  - gen4               # Best quality. ~90s for 5s clip.
rate_limit: 5 concurrent jobs (Standard), 20 concurrent (Enterprise)
output_format: mp4 (H.264)
resolutions: [1280x768, 768x1280, 1024x1024]   # landscape, portrait, square
durations: [5, 10]  # seconds
```

## Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/image_to_video` | POST | Generate video from reference image + prompt |
| `/text_to_video` | POST | Generate video from text prompt only |
| `/tasks/{id}` | GET | Poll task status + get output URL |
| `/tasks/{id}` | DELETE | Cancel in-progress task |

## Image-to-Video Example (Most Common)

```python
import httpx, time, base64

headers = {
    "Authorization": f"Bearer {RUNWAY_API_SECRET}",
    "Content-Type": "application/json",
    "X-Runway-Version": "2024-11-06"
}

# Encode reference image
with open("product_hero.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

# 1. Submit generation job
resp = httpx.post(f"{base_url}/image_to_video", headers=headers, json={
    "model": "gen4",
    "promptImage": f"data:image/png;base64,{img_b64}",
    "promptText": "Camera slowly zooms in, product rotates 45 degrees, soft studio lighting, professional commercial",
    "duration": 10,
    "ratio": "1280:768",
    "seed": 42,         # Reproducibility. Omit for random.
    "watermark": False   # Paid plans only
}, timeout=30)

task_id = resp.json()["id"]

# 2. Poll until complete
while True:
    status = httpx.get(f"{base_url}/tasks/{task_id}", headers=headers).json()
    if status["status"] == "SUCCEEDED":
        video_url = status["output"][0]  # Temporary URL, download immediately
        break
    elif status["status"] == "FAILED":
        raise Exception(f"Generation failed: {status.get('failure', 'unknown')}")
    time.sleep(10)  # Gen4 takes 60-120s typically

# 3. Download
video = httpx.get(video_url).content
with open("product_clip.mp4", "wb") as f:
    f.write(video)
```

## Text-to-Video Example

```python
resp = httpx.post(f"{base_url}/text_to_video", headers=headers, json={
    "model": "gen4_turbo",
    "promptText": "Aerial drone shot of São Paulo skyline at golden hour, cinematic 4K quality",
    "duration": 5,
    "ratio": "1280:768",
    "watermark": False
})
task_id = resp.json()["id"]
# Poll same as above
```

## Pricing

| Duration | Credits | Cost (Standard Plan) |
|----------|---------|---------------------|
| 5s gen4_turbo | 25 credits | ~$0.25 |
| 5s gen4 | 50 credits | ~$0.50 |
| 10s gen4_turbo | 50 credits | ~$0.50 |
| 10s gen4 | 100 credits | ~$1.00 |

Standard plan: $12/mo for 625 credits. Unlimited plan: $28/mo. Enterprise: custom.

Estimate for content factory: 10 clips/week × 10s gen4 = 1000 credits/week = ~$16/week or Unlimited plan.

## Prompt Engineering Tips

- **Be cinematic**: use camera language — "dolly in", "tracking shot", "crane up", "slow zoom"
- **Specify lighting**: "golden hour", "studio softbox", "neon rim light"
- **Keep motion simple**: Gen-4 handles slow camera moves well; fast action causes artifacts
- **Image reference dominates**: when using image-to-video, the prompt modifies motion/camera, not content
- **Negative concepts**: describe what you want, not what to avoid. "Static camera" not "no movement"

## Gotchas

- **Output URLs expire in 24h.** Download immediately after status=SUCCEEDED.
- **No audio in output.** All generated videos are silent. Combine with ElevenLabs via FFmpeg.
- **10s is the max duration.** For longer videos, generate multiple clips and concatenate with FFmpeg.
- **Image input requirements**: JPEG or PNG, max 16MB, minimum 256px on shortest side. Aspect ratio should match requested `ratio` or it gets cropped.
- **FAILED tasks still consume credits** if they ran partially. Check balance after failures.
- **Seed + identical prompt ≠ identical output.** Seed improves consistency but generation is not perfectly deterministic.
- **Rate limit 429**: standard plan allows only 5 concurrent jobs. Queue and batch.
- **Content moderation**: API rejects prompts with violence, NSFW, real people by name. Fails silently — check task status.

## Docs
- API Reference: https://docs.dev.runwayml.com/
- Models: https://docs.dev.runwayml.com/models

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_ayrshare_api]] | sibling | 0.32 |
| [[n06_content_factory_pricing]] | downstream | 0.25 |
| [[p01_kc_canva_connect_api]] | sibling | 0.24 |
| [[p01_kc_elevenlabs_tts]] | sibling | 0.23 |
| [[n06_pricing_content_factory]] | downstream | 0.22 |
| [[bld_knowledge_card_multi_modal_config]] | sibling | 0.20 |
| [[p01_kc_multi_modal_config]] | sibling | 0.18 |
| [[p01_kc_ffmpeg_patterns]] | sibling | 0.18 |
| [[kc_multimodal_prompt]] | sibling | 0.17 |
| [[bld_output_template_multi_modal_config]] | downstream | 0.17 |
