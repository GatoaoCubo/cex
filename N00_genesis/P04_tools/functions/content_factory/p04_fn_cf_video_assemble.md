---
id: p04_fn_cf_video_assemble
kind: function_def
8f: F6_produce
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: assemble_video
description: "Assemble a video from clips, audio narration, and subtitle tracks using FFmpeg. Call when the Content Factory has generated all component assets (video clips, TTS audio, SRT captions) and needs them merged into a final deliverable."
parameters:
  type: object
  properties:
    video_tracks:
      type: array
      items:
        type: object
        properties:
          path:
            type: string
            description: "Path to video clip file"
          start_time:
            type: string
            description: "Timestamp to start clip (HH:MM:SS.ms)"
          duration:
            type: string
            description: "Duration to use from clip (HH:MM:SS.ms)"
        required: [path]
      description: "Ordered list of video clips to concatenate"
    audio_track:
      type: string
      description: "Path to narration audio file (MP3, WAV, PCM)"
    subtitle_track:
      type: string
      description: "Path to SRT or VTT subtitle file for burned-in captions"
    output_path:
      type: string
      description: "Destination path for final video"
    output_format:
      type: string
      description: "Video container format"
      enum: [mp4, webm, mov]
    resolution:
      type: string
      description: "Output resolution"
      enum: ["1920x1080", "1280x720", "1080x1920", "1080x1080"]
    background_music:
      type: object
      properties:
        path:
          type: string
          description: "Path to background music file"
        volume:
          type: number
          description: "Volume level 0.0-1.0 relative to narration"
      description: "Optional background music track mixed under narration"
    subtitle_style:
      type: string
      description: "ASS subtitle style for burned-in captions"
  required: [video_tracks, output_path]
returns:
  type: object
  description: "Video assembly result"
  properties:
    output_path:
      type: string
      description: "Path to the assembled video file"
    duration_seconds:
      type: number
      description: "Total video duration"
    file_size_bytes:
      type: integer
      description: "Output file size"
    resolution:
      type: string
      description: "Final output resolution"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, ffmpeg, video, assemble, montage, content_factory]
tldr: "LLM-callable function to assemble video from clips + audio + subtitles via FFmpeg"
examples:
  - input: {"video_tracks": [{"path": "clips/intro.mp4"}, {"path": "clips/main.mp4"}], "audio_track": "audio/narration.mp3", "subtitle_track": "subs/captions.srt", "output_path": "output/final.mp4"}
    output: {"output_path": "output/final.mp4", "duration_seconds": 62.5, "file_size_bytes": 15728640, "resolution": "1920x1080"}
error_types: [file_not_found, ffmpeg_not_installed, codec_error, incompatible_resolution]
density_score: 0.92
related:
  - p01_kc_ffmpeg_patterns
  - p04_fn_cf_elevenlabs_tts
  - p03_ch_content_pipeline
  - n06_schema_brand_config
  - bld_schema_research_pipeline
  - p06_is_quality_audit
  - bld_schema_model_registry
  - p01_kc_ayrshare_api
  - p04_fn_cf_canva_export
  - bld_schema_input_schema
---

# Video Assembler Function (FFmpeg)

## Overview
Assembles a final video from component assets using FFmpeg. The LLM calls this as the final step in the Content Factory video pipeline — after script generation, TTS narration, and clip creation. Concatenates video clips, mixes narration with optional background music, and burns in subtitles.

## Parameters

### video_tracks
Type: array of objects | Required: yes
Ordered list of video clips. Each object has `path` (required), optional `start_time` and `duration` for trimming. Clips are concatenated in order.

### audio_track
Type: string | Required: no
Path to narration audio (from ElevenLabs TTS). Mixed as primary audio. If omitted, video clips' original audio is kept.

### subtitle_track
Type: string | Required: no
Path to SRT or VTT caption file. Burned into the video for platform compatibility (no separate track dependence).

### output_path
Type: string | Required: yes
Destination for the final video file.

### output_format
Type: string (enum) | Required: no | Default: mp4
Container format. `mp4` (H.264) for universal compatibility, `webm` (VP9) for web, `mov` for Apple ecosystems.

### resolution
Type: string (enum) | Required: no | Default: 1920x1080
Output resolution. `1080x1920` for vertical (Reels/TikTok), `1080x1080` for square (Instagram feed).

### background_music
Type: object | Required: no
Background music mixed under narration. `volume` 0.05-0.15 recommended for narration clarity.

### subtitle_style
Type: string | Required: no
ASS style string for burned-in captions. Controls font, size, position, outline.

## Returns
Type: object with `output_path`, `duration_seconds`, `file_size_bytes`, `resolution`.

## CLI Command (generated)
```bash
ffmpeg -i clips/intro.mp4 -i clips/main.mp4 -i audio/narration.mp3 \
  -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[v];[2:a]volume=1.0[a]" \
  -map "[v]" -map "[a]" -vf "subtitles=subs/captions.srt" \
  -s 1920x1080 -c:v libx264 -preset medium output/final.mp4
```

## Examples

### Example 1: Course lesson with narration and subtitles
```json
{
  "video_tracks": [{"path": "clips/lesson_intro.mp4", "duration": "00:00:05"}, {"path": "clips/screencast.mp4"}, {"path": "clips/outro.mp4"}],
  "audio_track": "audio/lesson_narration.mp3",
  "subtitle_track": "subs/lesson.srt",
  "output_path": "output/lesson_03.mp4",
  "resolution": "1920x1080"
}
```

### Example 2: Vertical social clip
```json
{
  "video_tracks": [{"path": "clips/hook.mp4"}, {"path": "clips/demo.mp4"}],
  "audio_track": "audio/hook_narration.mp3",
  "output_path": "output/reel.mp4",
  "output_format": "mp4",
  "resolution": "1080x1920",
  "background_music": {"path": "music/upbeat.mp3", "volume": 0.08}
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_ffmpeg_patterns]] | upstream | 0.51 |
| [[p04_fn_cf_elevenlabs_tts]] | sibling | 0.26 |
| [[p03_ch_content_pipeline]] | upstream | 0.21 |
| [[n06_schema_brand_config]] | downstream | 0.21 |
| [[bld_schema_research_pipeline]] | downstream | 0.20 |
| [[p06_is_quality_audit]] | downstream | 0.20 |
| [[bld_schema_model_registry]] | downstream | 0.20 |
| [[p01_kc_ayrshare_api]] | upstream | 0.20 |
| [[p04_fn_cf_canva_export]] | sibling | 0.20 |
| [[bld_schema_input_schema]] | downstream | 0.20 |
