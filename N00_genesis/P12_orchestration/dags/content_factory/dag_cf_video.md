---
id: p12_dag_cf_video
kind: dag
8f: F8_collaborate
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_video"
nodes:
  - id: "receive_longform"
    label: "Receive master longform draft and brand context from dag_cf_master"
    agent_group: "n07_orchestrator"
  - id: "extract_script"
    label: "Extract and adapt video script from longform (hook, body, CTA)"
    agent_group: "n02_marketing"
  - id: "segment_scenes"
    label: "Break script into timed scenes with visual directions and text overlays"
    agent_group: "n03_builder"
  - id: "generate_voiceover"
    label: "Convert script segments to speech via TTS (ElevenLabs/OpenAI)"
    agent_group: "n05_operations"
  - id: "generate_visuals"
    label: "Generate scene images/clips via AI (Midjourney/Runway/Sora)"
    agent_group: "n03_builder"
  - id: "generate_music"
    label: "Select or generate background music matching brand tone"
    agent_group: "n03_builder"
  - id: "assemble_video"
    label: "FFmpeg composite: visuals + voiceover + music + text overlays + transitions"
    agent_group: "n05_operations"
  - id: "add_branding"
    label: "Overlay brand intro/outro, logo watermark, color grading per brand palette"
    agent_group: "n06_brand"
  - id: "render_variants"
    label: "Render format variants: 16:9 (YouTube), 9:16 (Reels/TikTok), 1:1 (Feed)"
    agent_group: "n05_operations"
  - id: "quality_check"
    label: "Validate against cs_cf_video constraints (duration, aspect, hook timing)"
    agent_group: "n04_knowledge"
  - id: "export"
    label: "Export final renders to CDN staging and return paths to dag_cf_master"
    agent_group: "n05_operations"
edges:
  - from: "receive_longform"
    to: "extract_script"
  - from: "extract_script"
    to: "segment_scenes"
  - from: "segment_scenes"
    to: "generate_voiceover"
  - from: "segment_scenes"
    to: "generate_visuals"
  - from: "segment_scenes"
    to: "generate_music"
  - from: "generate_voiceover"
    to: "assemble_video"
  - from: "generate_visuals"
    to: "assemble_video"
  - from: "generate_music"
    to: "assemble_video"
  - from: "assemble_video"
    to: "add_branding"
  - from: "add_branding"
    to: "render_variants"
  - from: "render_variants"
    to: "quality_check"
  - from: "quality_check"
    to: "export"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, video-pipeline, tts, ffmpeg, multi-format]
tldr: "11-node video DAG: longform→script→scenes→parallel(TTS+visuals+music)→assemble→brand→render variants→export"
execution_order:
  - ["receive_longform"]
  - ["extract_script"]
  - ["segment_scenes"]
  - ["generate_voiceover", "generate_visuals", "generate_music"]
  - ["assemble_video"]
  - ["add_branding"]
  - ["render_variants"]
  - ["quality_check"]
  - ["export"]
parallel_groups:
  - ["generate_voiceover", "generate_visuals", "generate_music"]
critical_path: ["receive_longform", "extract_script", "segment_scenes", "generate_visuals", "assemble_video", "add_branding", "render_variants", "quality_check", "export"]
estimated_duration: "45min"
node_count: 11
edge_count: 12
max_parallelism: 3
keywords: [video, tts, ffmpeg, rendering, content-factory]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/dag_cf_master.md"
  related:
    - "P03_prompt/constraints/content_factory/cs_cf_video.md"
density_score: 1.0
related:
  - p12_dag_cf_course
  - p12_dag_cf_presentation
  - p12_dag_cf_social
  - p12_dag_cf_ebook
  - p12_dag_cf_master
  - wave2_quality_report
  - n04_output_monetization_curriculum
  - n01_output_cf_dags_and_specs
  - commercial_readiness_20260414c
  - commercial_readiness_20260414b
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_longform | Receive longform draft + brand context | n07_orchestrator | input |
| extract_script | Extract video script (hook, body, CTA) | n02_marketing | compute |
| segment_scenes | Break script into timed scenes with directions | n03_builder | compute |
| generate_voiceover | TTS conversion (ElevenLabs/OpenAI) | n05_operations | compute |
| generate_visuals | AI image/clip generation (Midjourney/Runway/Sora) | n03_builder | compute |
| generate_music | Background music selection/generation | n03_builder | compute |
| assemble_video | FFmpeg composite: visuals+voice+music+overlays | n05_operations | compute |
| add_branding | Logo watermark, intro/outro, color grading | n06_brand | transform |
| render_variants | Render 16:9, 9:16, 1:1 format variants | n05_operations | compute |
| quality_check | Validate against cs_cf_video constraints | n04_knowledge | gate |
| export | Export to CDN staging, return paths | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| receive_longform | extract_script | data |
| extract_script | segment_scenes | data |
| segment_scenes | generate_voiceover | data |
| segment_scenes | generate_visuals | data |
| segment_scenes | generate_music | data |
| generate_voiceover | assemble_video | data |
| generate_visuals | assemble_video | data |
| generate_music | assemble_video | data |
| assemble_video | add_branding | data |
| add_branding | render_variants | data |
| render_variants | quality_check | control |
| quality_check | export | control |

## Topological Order

receive_longform → extract_script → segment_scenes → generate_voiceover → generate_visuals → generate_music → assemble_video → add_branding → render_variants → quality_check → export

## Parallel Groups

- **Wave 1**: receive_longform
- **Wave 2**: extract_script
- **Wave 3**: segment_scenes
- **Wave 4**: generate_voiceover, generate_visuals, generate_music (max parallelism = 3)
- **Wave 5**: assemble_video (join barrier — waits for all 3)
- **Wave 6**: add_branding
- **Wave 7**: render_variants
- **Wave 8**: quality_check
- **Wave 9**: export

## Critical Path

receive_longform (1min) → extract_script (8min) → segment_scenes (5min) → generate_visuals (12min) → assemble_video (8min) → add_branding (3min) → render_variants (5min) → quality_check (2min) → export (1min) = **45min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_course]] | sibling | 0.64 |
| [[p12_dag_cf_presentation]] | sibling | 0.62 |
| [[p12_dag_cf_social]] | sibling | 0.58 |
| [[p12_dag_cf_ebook]] | sibling | 0.50 |
| [[p12_dag_cf_master]] | sibling | 0.22 |
| [[wave2_quality_report]] | upstream | 0.22 |
| [[n04_output_monetization_curriculum]] | upstream | 0.19 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.19 |
| [[commercial_readiness_20260414c]] | upstream | 0.18 |
| [[commercial_readiness_20260414b]] | upstream | 0.17 |
