# Video Agent — Architecture

**Version**: 1.0.0 | **Pattern**: Brief → Storyboard → Script → Prompts

---

## System Architecture

```
+-------------------------------------------------------------+
|                    video_agent v1.0.0                        |
|              BRIEF -> STORYBOARD -> SCRIPT -> PROMPTS        |
+-------------------------------------------------------------+
|                                                             |
|  +-----------+   +-----------+   +-----------+   +-------+  |
|  |   INPUT   |-->| STORYBOARD|-->|  SCRIPT   |-->|PROMPTS|  |
|  |  (Brief)  |   |  (Shots)  |   | (Narration)|  | (AI)  |  |
|  +-----------+   +-----------+   +-----------+   +-------+  |
|        |               |               |             |       |
|        v               v               v             v       |
|  product_brief    6-8 shots      narration      1 prompt    |
|  duration         timing         overlays       per shot    |
|  benefits         phases         audio          settings    |
|  style            camera         word counts               |
|                                                             |
+-------------------------------------------------------------+
```

---

## Component Dependencies

```
instructions.md (entry point)
       |
       +---> prompts/storyboarder.md
       |           |
       |           v
       |    {shots, timing, phases}
       |           |
       +---> prompts/script_writer.md
       |           |
       |           +-- data/narrative_templates.yaml
       |           |
       |           v
       |    {narration, overlays, audio}
       |           |
       +---> prompts/visual_prompter.md
                   |
                   +-- data/production_config.yaml
                   |
                   +-- data/platform_specs.yaml
                   |
                   v
            {prompts, settings}
```

---

## Style System

| Style | Motion | Camera | Lighting |
|-------|--------|--------|----------|
| energetic | 0.9 | Fast zoom, slam | High contrast |
| calm | 0.5 | Slow push | Soft, warm |
| dramatic | 0.6 | Slow reveal | Low-key |
| minimal | 0.3 | Static/subtle | Clean, even |

---

## Platform Specifications

| Platform | Aspect | Duration | Hook Time |
|----------|--------|----------|-----------|
| TikTok | 9:16 | 15-60s | 1-2s |
| Instagram Reels | 9:16 | 15-90s | 2-3s |
| YouTube Shorts | 9:16 | 15-60s | 3s |
| Instagram Feed | 1:1 | 15-60s | 3s |
| YouTube | 16:9 | 30-180s | 5s |

---

## 5D Validation System

```
+-------------------+--------+---------------------------+
| Dimension         | Weight | Criteria                  |
+-------------------+--------+---------------------------+
| narrative_arc     | 25%    | Hook 3s, phases, CTA      |
| visual_quality    | 25%    | Camera, style, prompts    |
| platform_comply   | 20%    | Duration, aspect, zones   |
| engagement_pot    | 15%    | Hook strength, loops      |
| production_feas   | 15%    | AI-compatible, realistic  |
+-------------------+--------+---------------------------+

Score: sum(dimension_score * weight), pass >= 7.0
```

---

## Token Budget

| Component | Tokens | % Total |
|-----------|--------|---------|
| Core docs | 4,500 | 30% |
| Config | 3,200 | 21% |
| Execution | 2,500 | 17% |
| Prompts | 3,500 | 23% |
| Validation | 1,300 | 9% |
| **TOTAL** | **15,000** | **100%** |

---

## AI Generator Compatibility

| Generator | Tier | Notes |
|-----------|------|-------|
| Runway Gen-3 | Primary | Best motion quality |
| Pika 1.5 | Secondary | Fast generation |
| Kling | Alternative | Good for certain styles |
| ElevenLabs | TTS | Voice narration |
| FFmpeg | Assembly | Final video |

---

## Integration Points

**Upstream**: pesquisa (market insights), anuncio (copy hooks), marca (brand profile)
**Downstream**: Runway Gen-3 (prompts), ElevenLabs (narration), FFmpeg (assembly)
