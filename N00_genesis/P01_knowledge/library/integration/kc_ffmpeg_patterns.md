---
id: p01_kc_ffmpeg_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "FFmpeg Patterns — Media Processing Recipes for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: ffmpeg
quality: 9.0
tags: [ffmpeg, video, audio, media, content-factory, integration, cli, INJECT]
tldr: "Battle-tested FFmpeg commands for concatenation, audio mixing, subtitles, thumbnails, and format conversion in content pipelines"
when_to_use: "When any nucleus needs to process, combine, or convert media files — the glue between all content factory tools"
keywords: [ffmpeg, video-processing, audio-mixing, concatenation, subtitles, thumbnail, transcode]
feeds_kinds: [cli_tool, workflow, dag, code_executor]
linked_artifacts: [kc_elevenlabs_tts, kc_runway_api, kc_canva_connect_api, kc_youtube_api]
density_score: null
related:
  - p04_fn_cf_video_assemble
  - p01_kc_ayrshare_api
  - p01_kc_runway_api
  - n04_output_cf_integration_kcs
  - p12_wf_cf_publish_youtube
  - p04_fn_cf_canva_export
  - spec_content_factory_v1
  - output_content_factory_internal_audit
  - p01_kc_multi_modal_config
---

# FFmpeg Patterns

## Quick Reference
```yaml
binary: ffmpeg
install: winget install Gyan.FFmpeg  # Windows
version_check: ffmpeg -version
global_flags:
  -y           # Overwrite output without asking
  -hide_banner # Suppress version/config info
  -loglevel warning  # Only show warnings+errors
hw_accel: -hwaccel cuda  # NVIDIA GPU acceleration (optional)
```

## Recipe 1: Concatenate Video Clips

Combine multiple Runway-generated clips into one continuous video.

```bash
# 1. Create file list
cat > concat_list.txt << 'EOF'
file 'clip_01.mp4'
file 'clip_02.mp4'
file 'clip_03.mp4'
EOF

# 2. Concatenate (same codec/resolution — use demuxer, fastest)
ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy output.mp4

# 3. If clips have different resolutions/codecs — re-encode:
ffmpeg -y -f concat -safe 0 -i concat_list.txt \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k output.mp4
```

## Recipe 2: Add Audio Track to Silent Video

Combine Runway video (silent) + ElevenLabs narration.

```bash
# Replace audio entirely
ffmpeg -y -i video.mp4 -i narration.mp3 \
  -c:v copy -c:a aac -b:a 192k \
  -map 0:v:0 -map 1:a:0 \
  -shortest output.mp4

# Mix background music + narration (music at 20% volume)
ffmpeg -y -i video.mp4 -i narration.mp3 -i bgm.mp3 \
  -filter_complex "[1:a]volume=1.0[narr];[2:a]volume=0.2[bgm];[narr][bgm]amix=inputs=2:duration=first[aout]" \
  -map 0:v:0 -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k \
  -shortest output.mp4
```

## Recipe 3: Burn SRT Subtitles

```bash
# Hardcode subtitles (burned into video pixels — no player support needed)
ffmpeg -y -i video.mp4 \
  -vf "subtitles=captions.srt:force_style='FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,MarginV=30'" \
  -c:v libx264 -preset medium -crf 18 -c:a copy output.mp4

# Soft subtitles (separate track — player can toggle)
ffmpeg -y -i video.mp4 -i captions.srt \
  -c:v copy -c:a copy -c:s mov_text \
  -map 0:v -map 0:a -map 1:s output.mp4
```

## Recipe 4: Generate Thumbnail from Video

```bash
# Single frame at timestamp
ffmpeg -y -i video.mp4 -ss 00:00:03 -frames:v 1 -q:v 2 thumbnail.jpg

# Best frame from first 10 seconds (highest scene change score)
ffmpeg -y -i video.mp4 -vf "select='gt(scene,0.3)',scale=1280:720" \
  -frames:v 1 -vsync vfr thumbnail.jpg

# Grid of thumbnails (4x4)
ffmpeg -y -i video.mp4 \
  -vf "fps=1/15,scale=320:180,tile=4x4" \
  -frames:v 1 contact_sheet.jpg
```

## Recipe 5: Format Conversion

```bash
# MP4 → WebM (for web embedding)
ffmpeg -y -i input.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus output.webm

# MP4 → GIF (for social/preview — max 15s, 480px wide)
ffmpeg -y -i input.mp4 -t 15 \
  -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  output.gif

# WAV/FLAC → MP3 (narration post-processing)
ffmpeg -y -i narration.wav -c:a libmp3lame -b:a 192k -ar 44100 narration.mp3

# Extract audio from video
ffmpeg -y -i video.mp4 -vn -c:a libmp3lame -b:a 192k audio_only.mp3
```

## Recipe 6: Trim / Cut

```bash
# Cut segment (no re-encode — instant, but may have keyframe imprecision)
ffmpeg -y -ss 00:01:30 -to 00:02:45 -i input.mp4 -c copy segment.mp4

# Precise cut (re-encode for frame-accurate start)
ffmpeg -y -i input.mp4 -ss 00:01:30 -to 00:02:45 \
  -c:v libx264 -preset fast -crf 18 -c:a aac segment.mp4
```

## Recipe 7: Overlay Image on Video (Watermark / Logo)

```bash
ffmpeg -y -i video.mp4 -i logo.png \
  -filter_complex "overlay=W-w-20:H-h-20:enable='between(t,0,999)'" \
  -c:v libx264 -preset medium -crf 18 -c:a copy output.mp4
# Position: W-w-20 = 20px from right edge, H-h-20 = 20px from bottom
```

## Recipe 8: Speed Up / Slow Down

```bash
# 2x speed (with audio pitch correction)
ffmpeg -y -i input.mp4 \
  -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" \
  -map "[v]" -map "[a]" output.mp4

# 0.5x slow motion (no audio — Runway clips are silent anyway)
ffmpeg -y -i input.mp4 -filter:v "setpts=2.0*PTS" -an output.mp4
```

## Gotchas

- **`-ss` BEFORE `-i` = fast seek (stream copy OK). AFTER `-i` = slow but frame-accurate.** For precise cuts, put `-ss` after `-i` and re-encode.
- **Concat demuxer requires identical codecs/resolutions.** Mismatched clips need re-encode (recipe 1 option 3).
- **Windows paths need escaping in filter strings.** Use forward slashes or double backslashes: `subtitles=C\\:/path/to/srt`.
- **`-shortest` is essential when mixing audio+video of different lengths.** Without it, FFmpeg continues until the longest stream ends.
- **CRF 18 ≈ visually lossless.** CRF 23 = default (good quality, smaller). CRF 28+ = noticeable artifacts. Never go below 15 for distribution.
- **GPU acceleration (`-hwaccel cuda`)** only helps decode. Encoding with NVENC (`-c:v h264_nvenc`) is faster but larger files than libx264.
- **GIF recipe uses palettegen** for high quality. Without it, GIFs look terrible (256 color dithering).

## Docs
- Official docs: https://ffmpeg.org/ffmpeg.html
- Filter reference: https://ffmpeg.org/ffmpeg-filters.html

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_cf_video_assemble]] | downstream | 0.59 |
| [[p01_kc_ayrshare_api]] | sibling | 0.23 |
| [[p01_kc_runway_api]] | sibling | 0.23 |
| [[n04_output_cf_integration_kcs]] | related | 0.22 |
| [[p12_wf_cf_publish_youtube]] | downstream | 0.21 |
| [[p04_fn_cf_canva_export]] | downstream | 0.18 |
| [[spec_content_factory_v1]] | downstream | 0.17 |
| [[output_content_factory_internal_audit]] | related | 0.16 |
| [[p01_kc_multi_modal_config]] | sibling | 0.16 |
