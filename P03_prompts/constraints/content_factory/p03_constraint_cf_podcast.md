---
id: p03_constraint_cf_podcast
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
name: "Content Factory Podcast Format Constraints"
constraint_type: "format_rules"
pattern: "multi_rule_set"
quality: null
tags: [constraint_spec, content-factory, podcast, audio, tts]
tldr: "Podcast constraints: 10-30min duration, intro/corpo/outro structure, audio specs, RSS metadata"
description: "Governs all podcast outputs from Content Factory for audio quality and distribution compliance"
provider_compat: "elevenlabs, ffmpeg, rss_feed"
fallback: "Manual audio review if automated validation unavailable"
temperature_override: "0.4"
max_tokens: "2048"
---

## Overview

Constrains all podcast artifacts produced by the Content Factory audio pipeline. Ensures every episode meets podcast platform requirements (Spotify, Apple Podcasts, Google Podcasts), professional audio standards, and brand voice consistency. Applied during audio assembly and pre-distribution QA.

## Constraint Definition

### Duration Tiers
| Tier | Duration | Use Case |
|------|----------|----------|
| micro | 5-10min | Quick tip, single insight |
| standard | 10-20min | Topic deep-dive, interview segment |
| long | 20-30min | Full episode, multi-topic coverage |

### Structure Rules
| Segment | Duration | Content |
|---------|----------|---------|
| intro | 15-45s | Brand jingle + episode title + host welcome |
| topic_tease | 30-60s | Preview key takeaways to retain listeners |
| body | 80-90% of total | Core content, segmented by subtopics |
| mid_cta | 15-30s | Sponsor or cross-promo (if applicable) |
| outro | 30-60s | Summary, CTA (subscribe/share), brand jingle |

### MUST Rules
- Episode MUST follow intro → tease → body → outro structure
- Audio MUST be normalized to -16 LUFS (podcast standard)
- Sample rate MUST be 44.1kHz or 48kHz
- Bit depth MUST be 16-bit minimum
- Export format MUST be MP3 (192kbps) for distribution + WAV for archive
- Episode MUST include complete RSS metadata (title, description, duration, date)
- Brand intro/outro jingle MUST bookend every episode
- Show notes MUST accompany every episode (timestamps, links, summary)

### MUST NOT Rules
- MUST NOT exceed 30 minutes total duration
- MUST NOT have silence gaps > 2 seconds (except intentional pauses < 1s)
- MUST NOT clip audio (peaks must stay below -1 dBTP)
- MUST NOT publish without show notes and chapter markers
- MUST NOT mix voice and music at competing volume levels

### Audio Specs
| Parameter | Value |
|-----------|-------|
| format_distribution | MP3, 192kbps CBR |
| format_archive | WAV, 48kHz/16-bit |
| loudness_target | -16 LUFS |
| peak_ceiling | -1 dBTP |
| voice_eq | High-pass 80Hz, presence boost 2-4kHz |
| music_level | -20 LUFS (background), duck during speech |

### Quality Metrics
| Metric | Min | Target | Max |
|--------|-----|--------|-----|
| loudness_lufs | -18 | -16 | -14 |
| silence_ratio | 0% | 2% | 5% |
| show_notes_words | 100 | 250 | 500 |

## Provider Compatibility

| Provider | Support | Method |
|----------|---------|--------|
| ElevenLabs | native | TTS with voice cloning, LUFS control |
| FFmpeg | native | Audio normalization, format conversion, concatenation |
| Spotify | native | RSS feed ingestion with metadata |
| Apple Podcasts | native | RSS feed with iTunes-specific tags |

## Integration

- Consumed by: audio pipeline quality_check node
- Validates outputs from: audio assembly and mastering nodes
- Cross-references: brand_config.yaml (jingle, voice profile, tone)
- Feeds: quality_gate node in dag_cf_master for final approval
