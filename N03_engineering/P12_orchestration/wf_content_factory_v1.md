---
id: p12_wf_content_factory_v1
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-08"
updated: "2026-04-08"
author: "n03_builder"
title: "Content Factory v1 -- Brief to Published Multi-Format Content"
steps_count: 13
execution: mixed
agent_groups: [n01_intelligence, n02_marketing, n03_engineering, n04_knowledge, n05_operations, n06_commercial, n07_admin]
timeout: 14400
retry_policy: per_step
depends_on: [brand_config_yaml]
signals: [complete, error]
spawn_configs: [p12_spawn_grid]
domain: "content_factory"
quality: 9.0
tags: [workflow, content-factory, multi-format, autonomous, pipeline]
tldr: "5-wave workflow: brief+brand -> research -> author -> produce -> validate -> publish. 13 steps, 7 nuclei, zero human intervention."
density_score: 0.94
---

## Purpose

Orchestrates the full Content Factory pipeline from a single user brief to 7+ published
content formats (course, video, ebook, presentation, podcast, social posts, landing page).
Implements the dag_cf_master dependency graph as an executable workflow with wave-based
scheduling, inter-nucleus signaling, and quality gates between production and publication.
Designed for zero-touch autonomous operation after initial brief + brand injection.

## Steps

### Step 1: Parse Brief [n01_intelligence]
- **Agent**: n01_intelligence
- **Action**: Parse and validate content brief -- extract topic, audience, formats requested, constraints, brand_ref
- **Input**: User brief (free text or structured YAML with topic, audience, formats fields)
- **Output**: Validated brief manifest (brief_manifest.yaml) with normalized fields
- **Signal**: parse_brief_complete
- **Depends on**: none
- **Timeout**: 60s
- **On failure**: abort (no brief = no pipeline)

### Step 2: Inject Brand [n06_commercial]
- **Agent**: n06_commercial
- **Action**: Load brand_config.yaml, inject voice/palette/logo/fonts into pipeline context
- **Input**: brief_manifest.yaml + .cex/brand/brand_config.yaml
- **Output**: Branded context object (brand_context.yaml) with resolved BRAND_* variables
- **Signal**: brand_inject_complete
- **Depends on**: Step 1
- **Timeout**: 30s
- **On failure**: abort (unbranded content violates core principle)

### Step 3: Deep Research [n01_intelligence]
- **Agent**: n01_intelligence
- **Action**: Research topic in depth -- competitors, trends, keywords, sources, audience pain points
- **Input**: brief_manifest.yaml + brand_context.yaml
- **Output**: Research KCs (3-5 knowledge_cards in P01_knowledge/) + source bibliography
- **Signal**: research_complete
- **Depends on**: Step 1
- **Timeout**: 1800s
- **On failure**: retry (max 2, research is recoverable)

### Step 4: Content Strategy [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Define content angle, hook structure, CTA strategy, distribution channel plan
- **Input**: brief_manifest.yaml + brand_context.yaml + research KCs from Step 3
- **Output**: Strategy document (strategy.yaml) with angle, hooks, CTAs, channel map
- **Signal**: strategy_complete
- **Depends on**: Steps 2, 3
- **Timeout**: 600s
- **On failure**: retry (max 1, creative decisions may need reset)

### Step 5: Author Longform Draft [n03_engineering]
- **Agent**: n03_engineering
- **Action**: Write master longform content from research + strategy (canonical source for all formats)
- **Input**: strategy.yaml + research KCs + brand_context.yaml
- **Output**: Master draft (master_longform.md) -- 3000-8000 words, structured with headers
- **Signal**: longform_complete
- **Depends on**: Step 4
- **Timeout**: 1200s
- **On failure**: retry (max 1)

### Step 6: Generate Course [n03_engineering]
- **Agent**: n03_engineering
- **Action**: Produce course outline + lesson scripts + quiz using p03_pt_cf_course_outline + p03_pt_cf_lesson_script + p03_pt_cf_quiz
- **Input**: master_longform.md + brand_context.yaml + cs_cf_course constraints
- **Output**: Course package (outline.yaml + 5-12 lesson scripts + quiz per module)
- **Signal**: course_complete
- **Depends on**: Step 5
- **Timeout**: 2400s
- **On failure**: retry (max 1)

### Step 7: Generate Video Script [n03_engineering]
- **Agent**: n03_engineering
- **Action**: Write 90s video script using p03_pt_cf_video_script with hook/build/benefit/proof/CTA structure
- **Input**: master_longform.md + brand_context.yaml + cs_cf_video constraints
- **Output**: Video script (video_script.yaml) + storyboard outline
- **Signal**: video_script_complete
- **Depends on**: Step 5
- **Timeout**: 600s
- **On failure**: retry (max 1)

### Step 8: Generate eBook [n03_engineering]
- **Agent**: n03_engineering
- **Action**: Produce eBook chapters using p03_pt_cf_ebook_chapter with intro/body/examples/summary structure
- **Input**: master_longform.md + brand_context.yaml + cs_cf_ebook constraints
- **Output**: eBook manuscript (5-15 chapters as .md files) + cover brief
- **Signal**: ebook_complete
- **Depends on**: Step 5
- **Timeout**: 1800s
- **On failure**: retry (max 1)

### Step 9: Generate Presentation + Social [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Produce slide deck content (p03_pt_cf_slide_deck) + 7-day social campaign (p03_pt_cf_social_post)
- **Input**: master_longform.md + brand_context.yaml + cs_cf_presentation + strategy.yaml
- **Output**: Slide content (10-30 slides with speaker notes) + 7 social posts per platform
- **Signal**: presentation_social_complete
- **Depends on**: Step 5
- **Timeout**: 1200s
- **On failure**: retry (max 1)

### Step 10: Produce Media Assets [n03_engineering]
- **Agent**: n03_engineering
- **Action**: Execute tool pipeline -- Canva API (slides/thumbnails), Marp (alt slides), Typst/Pandoc (eBook PDF/EPUB), ElevenLabs (TTS narration), FFmpeg (video assembly)
- **Input**: Course scripts + video script + eBook manuscript + slide content + brand_context
- **Output**: Binary assets (PPTX, PDF, EPUB, MP3, MP4, PNG thumbnails)
- **Signal**: media_assets_complete
- **Depends on**: Steps 6, 7, 8, 9
- **Timeout**: 3600s
- **On failure**: skip (partial asset set is acceptable, flag missing)

### Step 11: NotebookLM Integration [n04_knowledge]
- **Agent**: n04_knowledge
- **Action**: Upload research KCs to NotebookLM via cex_notebooklm.py --upload, activate Studio (flashcards + audio overview + quiz)
- **Input**: Research KCs from Step 3 + notebooklm_notebooks.yaml config
- **Output**: NotebookLM outputs (75+ flashcards, podcast audio 10-30min, quiz 10-20 questions)
- **Signal**: notebooklm_complete
- **Depends on**: Step 3
- **Timeout**: 3600s
- **On failure**: skip (NotebookLM is supplementary, browser auth may expire)

### Step 12: Quality Gate [n07_admin]
- **Agent**: n07_admin
- **Action**: Validate all outputs against brand consistency, constraint specs, and quality >= 8.5
- **Input**: All outputs from Steps 6-11 + brand_context.yaml + constraint specs
- **Output**: Quality report (quality_gate.yaml) with per-asset scores and pass/fail
- **Signal**: quality_gate_complete
- **Depends on**: Steps 10, 11
- **Timeout**: 600s
- **On failure**: abort (quality failures require re-dispatch of failing steps)

### Step 13: Publish [n05_operations + n06_commercial + n02_marketing]
- **Agent**: n05_operations (YouTube, GitHub), n06_commercial (Hotmart, Stripe), n02_marketing (Ayrshare social, email)
- **Action**: Distribute approved content to target channels via existing publishing workflows
- **Input**: Quality-approved assets + channel configs + API credentials
- **Output**: Published URLs per channel + publication manifest
- **Signal**: wf_content_factory_v1_complete
- **Depends on**: Step 12
- **Timeout**: 1800s
- **On failure**: retry (max 2, API calls may fail transiently)

## Wave Plan

| Wave | Steps | Mode | Nuclei | Est. Duration |
|------|-------|------|--------|---------------|
| 1: Ingest | 1 (Parse Brief) | sequential | N01 | 1 min |
| 2: Context | 2 (Brand), 3 (Research) | parallel | N06, N01 | 30 min |
| 3: Strategy + Author | 4 (Strategy), 5 (Longform) | sequential | N02, N03 | 30 min |
| 4: Produce | 6-11 (Course, Video, eBook, Pres/Social, Media, NotebookLM) | parallel | N03, N02, N04 | 60 min |
| 5: Gate + Publish | 12 (Quality), 13 (Publish) | sequential | N07, N05+N06+N02 | 30 min |

**Total estimated**: ~150 min (2.5 hours) for full pipeline.

## Dependencies

1. `.cex/brand/brand_config.yaml` must exist and pass `brand_validate.py` (13 required fields)
2. Prompt templates in `P03_prompts/templates/content_factory/` (7 templates from Wave 2)
3. Action prompts in `P03_prompts/actions/content_factory/` (7 actions from Wave 2)
4. Constraint specs in `P03_prompts/constraints/content_factory/` (6 specs from Wave 2)
5. Function defs in `P04_tools/functions/content_factory/` (7 tool functions from Wave 2)
6. API credentials configured in `.cex/brand/api_keys` (Canva, YouTube, ElevenLabs, Ayrshare)
7. dag_cf_master and 5 sub-DAGs in `P12_orchestration/dags/content_factory/`

## Signals

1. **Per-step completion**: `{step_name}_complete` emitted by assigned nucleus
2. **Wave boundary**: N07 dispatches next wave only after all current-wave signals received
3. **On workflow complete**: `wf_content_factory_v1_complete` with publication manifest
4. **On error**: `wf_content_factory_v1_error` with failed step, error type, recovery suggestion

## Error Recovery

| Strategy | When | Behavior |
|----------|------|----------|
| abort | Brief missing, brand invalid, quality gate fail | Stop pipeline, report to user |
| retry (max 2) | API failures, research timeout, publish failure | Retry step with exponential backoff |
| skip | NotebookLM auth expired, partial media assets | Continue with reduced output set, flag gaps |

## References

1. `_docs/specs/spec_content_factory_v1.md` -- master spec for this workflow
2. `_docs/specs/spec_notebooklm_pipeline.md` -- NotebookLM integration spec
3. `P12_orchestration/dags/content_factory/dag_cf_master.md` -- dependency graph this workflow implements
4. `P12_orchestration/workflows/content_factory/` -- 5 publishing sub-workflows
5. `P03_prompts/templates/content_factory/` -- 7 prompt templates
6. `P03_prompts/actions/content_factory/` -- 7 action prompts
7. `P03_prompts/constraints/content_factory/` -- 6 constraint specs
