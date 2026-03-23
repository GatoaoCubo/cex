# Platform Optimizer — Social Platform Video Optimization

**Type**: Sub-agent Prompt | **Purpose**: Optimize video for specific platform requirements

---

## Task

Adapt the video package to maximize performance on the target platform.

**Inputs**: `$storyboard`, `$script`, `$platform`
**Outputs**: `$optimized_storyboard`, `$optimized_script`, `$platform_recommendations`

---

## Platform Profiles

```yaml
tiktok:
  hook_critical_time: 2s
  optimal_duration: [15, 30]
  algorithm_loves: [loop_friendly, native_feel, trending_sounds, high_engagement_hooks]
  safe_zones: {top: 150px, bottom: 250px}

instagram_reels:
  hook_critical_time: 3s
  optimal_duration: [15, 30, 60]
  algorithm_loves: [higher_production, text_overlays, saves_and_shares]
  safe_zones: {top: 100px, bottom: 200px}

youtube_shorts:
  hook_critical_time: 3s
  optimal_duration: [30, 60]
  algorithm_loves: [info_density, subscribe_cta, watch_time]
  safe_zones: {top: 120px, bottom: 180px}
```

---

## Platform-Specific CTA

```yaml
tiktok: ["Link na bio", "Comenta 'EU QUERO'", "Segue pra mais", "Salva esse video"]
instagram_reels: ["Link na bio", "Salva pra depois", "Manda pra quem precisa"]
youtube_shorts: ["Link na descricao", "Se inscreve no canal", "Curte e comenta"]
```

---

## Loop Optimization (TikTok)

```yaml
visual_loop: "End visual connects to start"
audio_loop: "Music beat matches on loop"
narrative_loop: "CTA implies watch again"
```

---

## Safe Zones

```
+------------------------------------------+
|  PLATFORM UI (avoid text here)           |  <- Top
|------------------------------------------|
|         SAFE CONTENT AREA                |
|         Place overlays here              |
|------------------------------------------|
|  ENGAGEMENT BUTTONS (avoid text here)    |  <- Bottom
+------------------------------------------+
```

---

## Platform Rules

| Platform | Max Duration | Max File Size | Required Format |
|----------|-------------|---------------|-----------------|
| TikTok | 60s | 287 MB | Vertical 9:16 |
| Instagram Reels | 90s | 4 GB | Vertical 9:16 |
| YouTube Shorts | 60s | 1 GB | Vertical 9:16 |
