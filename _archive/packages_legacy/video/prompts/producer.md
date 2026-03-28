# Producer — Video Assembly and Export Protocol

**Type**: Sub-agent Prompt | **Purpose**: Production guidance for assembly and export

---

## Task

Guide the assembly of generated clips into a final, platform-ready video.

**Inputs**: `$video_clips`, `$script`, `$platform`
**Outputs**: `$assembly_instructions`, `$export_settings`, `$timeline`

---

## Timeline Structure

```
Video:     [CLIP1][CLIP2][CLIP3][CLIP4][CLIP5][CLIP6][CLIP7]
Narration: [NAR1 ][NAR2 ][NAR3 ][NAR4 ][NAR5 ][NAR6 ][NAR7 ]
Music:     [===================== MUSIC TRACK =====================]
SFX:       [SFX1]      [SFX2]      [SFX3][SFX4]      [SFX5]
Overlays:  [OVL1]            [OVL2][OVL3]      [OVL4][OVL5]
Timeline:  0s    3s    7s    12s   16s   20s   25s   30s
```

---

## Audio Preparation

```yaml
narration: {source: "ElevenLabs TTS", format: "WAV", sample_rate: 48000}
music: {source: "Licensed track", format: "MP3", ducking: true}
sfx: {source: "SFX library", format: "WAV", timing: "Per audio cues"}
```

## Audio Mix Levels

| Layer | Level |
|-------|-------|
| Narration | 0dB (primary) |
| Music | -12dB (ducking on) |
| SFX | -6dB (per cue) |

---

## Transitions

```yaml
hook_to_build: "cut"
build_to_benefit: "cut or wipe"
benefit_to_proof: "cut or dissolve"
proof_to_cta: "cut"
```

---

## Export Settings by Platform

```yaml
tiktok:
  resolution: "1080x1920"
  fps: 30
  bitrate: "8 Mbps"
  codec: "H.264"
  audio: "AAC 320kbps"
  max_size: "287 MB"

instagram_reels:
  resolution: "1080x1920"
  fps: 30
  bitrate: "8 Mbps"
  codec: "H.264"
  max_size: "4 GB"

youtube_shorts:
  resolution: "1080x1920"
  fps: 30
  bitrate: "8 Mbps"
  codec: "H.264"
```

---

## FFmpeg Assembly Example

```bash
# Concatenate clips
ffmpeg -f concat -safe 0 -i clips.txt -c copy output_video.mp4

# Add audio
ffmpeg -i output_video.mp4 -i narration.wav -i music.mp3 \
  -filter_complex "[1:a][2:a]amix=inputs=2:duration=first[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac final_video.mp4

# Export for TikTok
ffmpeg -i final_video.mp4 -c:v libx264 -preset slow \
  -b:v 8M -c:a aac -b:a 320k -r 30 tiktok_ready.mp4
```

---

## Quality Requirements

- Total duration must match target (15/30/60s)
- Audio synced within 50ms
- Safe zones respected for overlays
- No frame drops at transitions
- Audio levels balanced (-6dB peak)
