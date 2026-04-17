---
id: wf_kc_to_content
kind: workflow
pillar: P12
title: "KC to Published Content — End-to-End NotebookLM Pipeline Workflow"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: n02_marketing
mission: OPTIMIZE_FACTORY
nucleus: N02
domain: content_factory
execution_mode: mixed
steps_count: 7
estimated_duration: "45-90min per KC batch"
trigger: "manual | F8_hook | mission_wave"
inputs:
  - name: kc_paths
    type: list
    required: true
    description: "Paths to knowledge card .md files to process"
  - name: domain
    type: string
    required: false
    description: "NotebookLM domain for notebook routing"
  - name: outputs
    type: list
    required: false
    default: ["flashcards", "audio_summary", "quiz"]
    description: "Which NotebookLM Studio outputs to generate"
  - name: distribution_channels
    type: list
    required: false
    default: ["youtube", "spotify", "instagram", "linkedin", "newsletter"]
    description: "Where to publish formatted content"
outputs:
  - name: published_manifest
    type: object
    description: "Record of all published assets with URLs and metrics targets"
quality: 9.0
tags: [workflow, notebooklm, content_factory, pipeline, kc, publishing, N02, P12]
tldr: "Complete workflow from raw KC to published multi-channel content — 7 steps covering upload, generation, formatting, distribution planning, assembly, publishing, and tracking"
keywords: [workflow, kc, notebooklm, content factory, publishing, distribution, end-to-end]
density_score: null
---

# KC to Published Content — The Full Pipeline

## Overview

A knowledge card is a compressed unit of expertise. It sits in a markdown file, dense with insight, and does absolutely nothing for your audience. They'll never read it. They'll never find it. It exists for machines.

This workflow turns that machine-readable knowledge into human-consumable content across every channel your audience inhabits. One KC in, seven content formats out, distributed across five channels, with branded packaging that makes every piece unmistakably yours.

The magic is in the sequencing: NotebookLM does the heavy transformation (KC to audio, flashcards, quiz), N02 does the branding and distribution strategy, and the publishing workflows handle the last mile. No human intervention required between start and publish.

## Workflow Diagram

```
KC .md files (1 or more)
    |
    v
[STEP 1] UPLOAD ─── cex_notebooklm.py --upload
    |  KC pasted as source into domain notebook
    |  Domain resolved from KC frontmatter
    |
    v
[STEP 2] GENERATE ─── cex_notebooklm.py --studio
    |  NotebookLM Estudio activated
    |  Outputs: audio_overview + flashcards + quiz (configurable)
    |  Wait: audio 2-10min, flashcards ~30s, quiz ~30s
    |
    v
[STEP 3] FORMAT ─── N02 templates (parallel)
    |  tpl_notebooklm_audio_wrapper   → branded intro/outro scripts
    |  tpl_notebooklm_flashcard_format → Anki/Quizlet/PDF exports
    |  tpl_content_distribution_plan   → channel mapping + schedule
    |
    v
[STEP 4] ASSEMBLE ─── N03 tools (parallel)
    |  ElevenLabs TTS  → narrate intro/outro scripts
    |  FFmpeg           → stitch jingle + intro + audio + outro
    |  Typst/WeasyPrint → render flashcard PDF
    |  Canva API        → create visual assets (thumbnails, carousels)
    |
    v
[STEP 5] VALIDATE ─── N07 quality gate
    |  Brand consistency check (voice, colors, CTA)
    |  Audio quality check (levels, silence, glitches)
    |  Flashcard accuracy check (facts match KC source)
    |  Distribution plan completeness check
    |
    v
[STEP 6] PUBLISH ─── wf_cf_publish_* (parallel)
    |  wf_cf_publish_youtube   → upload episode + metadata
    |  wf_cf_publish_social    → Ayrshare scheduling
    |  wf_cf_email_launch      → newsletter sequence
    |  wf_cf_publish_hotmart   → course module (if applicable)
    |
    v
[STEP 7] TRACK ─── analytics + feedback loop
    |  Monitor first 48h metrics
    |  Flag top-performing assets for boost
    |  Log results to campaign_performance_memory
    |  Feed learnings back to N02 for next batch
    |
    v
DONE — KC knowledge is now live across all channels
```

## Step Details

### Step 1: UPLOAD (Sequential)

**Tool**: `python _tools/cex_notebooklm.py --upload <kc_path>`
**Nucleus**: N04 (or automated via F8 hook)
**Duration**: 30-60s per KC

| Input | Output | Error Handling |
|-------|--------|----------------|
| KC .md file path | `{notebook_id, domain, source_title, status}` | AUTH_EXPIRED: run `--reauth` |
| Domain (auto-resolved from KC frontmatter) | Config updated with new source | Source limit (50): warn, create spillover notebook |
| Cookies from MCP state | Playwright session | Timeout: screenshot + retry once |

**Pre-flight checks**:
1. KC exists and has valid frontmatter (`kind`, `domain`, `title`)
2. NotebookLM config exists (`.cex/P09_config/notebooklm_notebooks.yaml`)
3. Auth cookies valid (`check_auth_valid()`)
4. Source count < 45 for target notebook (warn at 45, block at 50)

**Batch mode**: For multiple KCs, upload sequentially with 10s delay between uploads to avoid rate limiting. NotebookLM processes ~5 sources/hour reliably.

### Step 2: GENERATE (Sequential per output type)

**Tool**: `python _tools/cex_notebooklm.py --studio <notebook_id> --outputs flashcards,audio_summary,quiz`
**Nucleus**: N04
**Duration**: 2-15min depending on outputs

| Output Type | PT-BR Label | Generation Time | Result |
|-------------|-------------|-----------------|--------|
| flashcards | Cartoes didaticos | ~30s | 20-75 cards |
| audio_summary | Resumo em audio | 2-10min | 5-30min podcast |
| quiz | Teste | ~30s | 10-20 questions |
| mind_map | Mapa mental | ~15s | Concept diagram |
| briefing | Documento de resumo | ~30s | Summary doc |
| timeline | Linha do tempo | ~15s | Chronological view |
| faq | Perguntas frequentes | ~15s | Q&A pairs |

**Polling**: Audio generation requires polling every 30s with 15min timeout. Other outputs are near-instant.

**Status check**: `python _tools/cex_notebooklm.py --status <notebook_id>` confirms all outputs generated.

### Step 3: FORMAT (Parallel — N02)

Three templates execute simultaneously on the raw NotebookLM outputs:

| Template | Input | Output | Path |
|----------|-------|--------|------|
| `tpl_notebooklm_audio_wrapper` | Audio topic + brand config | Intro/outro scripts (2 variants: formal + casual) | N02 LLM call |
| `tpl_notebooklm_flashcard_format` | Raw flashcards + brand config | Formatted decks (Anki + PDF) | N02 LLM call |
| `tpl_content_distribution_plan` | All assets + channels + brand | Day-by-day publishing schedule | N02 LLM call |

**Dependencies**: Step 2 must complete. All three templates run in parallel since they operate on different outputs.

**Brand injection**: All templates read `{{BRAND_*}}` variables from `.cex/brand/brand_config.yaml`. If not bootstrapped, templates produce generic output (functional but unbranded).

### Step 4: ASSEMBLE (Parallel — N03 tools)

Physical production of publishable files:

| Task | Tool | Input | Output |
|------|------|-------|--------|
| Narrate intro/outro | ElevenLabs API | Script text from Step 3 | intro.mp3, outro.mp3 |
| Stitch audio | FFmpeg | jingle + intro + NLM audio + outro | episode.mp3 |
| Render flashcard PDF | Typst or WeasyPrint | Formatted markdown from Step 3 | flashcards.pdf |
| Create thumbnail | Canva API | Episode title + brand colors | thumbnail.png (1280x720) |
| Create carousel | Canva API | Top 5 flashcards + brand template | carousel.png (1080x1080 x5) |

**FFmpeg assembly command**:
```bash
ffmpeg -i jingle.mp3 -i intro.mp3 -i notebooklm_audio.mp3 -i outro.mp3 \
  -filter_complex "[0][1][2][3]concat=n=4:v=0:a=1" \
  -metadata title="{{TOPIC}}" -metadata artist="{{BRAND_NAME}}" \
  episode_final.mp3
```

**Canva API calls**:
```
POST /v1/designs (type: custom, 1280x720) → thumbnail
POST /v1/designs (type: custom, 1080x1080) → carousel slides
POST /v1/exports (format: png) → download URLs
```

### Step 5: VALIDATE (Sequential — N07)

Quality gate before anything goes live:

| Check | Pass Criteria | Action if Fail |
|-------|---------------|----------------|
| Brand voice match | Intro/outro match brand_config tone | Regenerate with corrected VARIANT |
| Audio quality | No silence >2s, levels normalized | Re-stitch with FFmpeg normalization |
| Flashcard accuracy | All facts traceable to source KC | Flag cards for manual review |
| Visual consistency | Brand colors + logo on all assets | Regenerate via Canva with correct template |
| Distribution plan completeness | All channels covered, all days scheduled | Fill gaps in schedule |
| CTA presence | Every asset includes CTA | Append CTA to missing assets |

### Step 6: PUBLISH (Parallel — N05 + N06 + N02)

Each publishing workflow is independent and runs in parallel:

| Workflow | Nucleus | Channel | Key Actions |
|----------|---------|---------|-------------|
| `wf_cf_publish_youtube` | N05 | YouTube | Upload MP3 as video + thumbnail + description + tags |
| `wf_cf_publish_social` | N02 | Instagram, LinkedIn, Twitter/X | Ayrshare API scheduling per distribution plan |
| `wf_cf_email_launch` | N02 | Newsletter | Email sequence: announce + recap + flashcards |
| `wf_cf_publish_hotmart` | N06 | Hotmart | Upload as course module (if course context) |

**Ayrshare integration**: Single API call schedules posts across all social platforms simultaneously. Each post has platform-specific copy from the distribution plan.

### Step 7: TRACK (Ongoing — 48h window)

| Metric | Source | Check Interval | Action Threshold |
|--------|--------|-----------------|------------------|
| YouTube views | YouTube API | 6h, 24h, 48h | <100 at 24h: boost thumbnail/title |
| Spotify listens | Spotify for Podcasters | 24h, 48h | <50 at 48h: cross-promote more |
| Instagram engagement | Ayrshare analytics | 6h, 24h | <3% rate: boost top post |
| LinkedIn impressions | Ayrshare analytics | 24h | <500: reshare with different hook |
| Newsletter opens | Email provider | 6h, 24h | <20% open: test new subject line |
| Flashcard imports | Supabase tracking | 48h | <10: promote in next newsletter |

**Feedback loop**: Top-performing content formats and hooks are logged to `N02_marketing/P10_memory/campaign_performance_memory.md` for future optimization.

## Integration Points

| System | Role | Interface |
|--------|------|-----------|
| N03 Engineering | Tool execution (FFmpeg, Typst, Canva) | Handoff with asset specs |
| N04 Knowledge | NotebookLM upload + studio activation | cex_notebooklm.py CLI |
| N05 Operations | YouTube upload, deployment | wf_cf_publish_youtube |
| N06 Commercial | Hotmart course upload, pricing | wf_cf_publish_hotmart |
| N07 Orchestrator | Quality gate, wave coordination | Signal on complete |
| Ayrshare | Social scheduling | API via social_publisher_marketing |
| ElevenLabs | TTS narration | API via fn_cf_elevenlabs_tts |
| Canva | Visual assets | API via fn_cf_canva_create |

## Error Recovery

| Failure Point | Detection | Recovery |
|---------------|-----------|----------|
| NotebookLM auth expired | `[AUTH_EXPIRED]` in upload output | `cex_notebooklm.py --reauth` then retry |
| Audio generation timeout | No output after 15min polling | Retry once, then skip audio and proceed |
| ElevenLabs rate limit | 429 response | Wait 60s, retry with exponential backoff |
| Canva API error | Non-200 response | Retry once, fallback to Marp for slides |
| Ayrshare scheduling fail | API error response | Queue for manual publishing, alert user |
| Quality gate fail | Score < 8.0 on any check | Return to Step 3 with correction notes |

## Execution Modes

| Mode | Trigger | Human Involvement |
|------|---------|-------------------|
| **Manual** | User runs workflow directly | User monitors each step |
| **F8 Hook** | KC saved in F8 COLLABORATE | Zero — auto-uploads, waits for batch |
| **Mission Wave** | Part of Content Factory mission | Zero — N07 dispatches and monitors |
| **Batch** | Multiple KCs queued | Zero — sequential upload, parallel format |

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^wf_[a-z][a-z0-9_]+$ |
| H02 | PASS | All frontmatter fields present |
| H03 | PASS | steps_count matches actual steps (7) |
| H04 | PASS | All integration points documented |
| H05 | PASS | Error recovery for each failure mode |
| H06 | PASS | Execution modes cover all triggers |
