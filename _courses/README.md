---
id: courses_index
kind: dashboard
title: "CEXAI Infoproduct Source"
version: 1.0.0
quality: 7.4
density_score: 1.0
updated: "2026-04-22"
related:
  - spec_courses_driver_tier
  - media_pipeline
  - spec_content_factory_v1
  - p01_kc_notebooklm_integration
  - spec_course_pipeline_wiring
  - bld_collaboration_audio_tool
  - cex_doctor_command
  - spec_mentor_didactic_engine
  - spec_media_pipeline_how_to
  - audio-tool-builder
---

# CEXAI Courses -- Source Directory

> Source markdown for educational infoproducts. Rendered output (video, audio, PDF)
> goes to `rendered/` (gitignored) or external platforms (Hotmart, YouTube, Spotify).

## Audience Tiers

| Tier | Analogy | What they learn | What they NEVER touch |
|------|---------|-----------------|----------------------|
| **Driver** | Uses the car | Think in 8 steps, organize in 12 pillars, name things by kind | Python, ISOs, schemas, git |
| **Mechanic** | Customizes the car | Nucleus rules, sin lenses, crew templates, brand config | cex_sdk internals, dispatch scripts |
| **Engineer** | Builds new cars | Builders, pillar schemas, kind genesis, vertical nuclei | (this is the CONTRIBUTING.md audience) |

## Content Pipeline

```
concept_registry.yaml       -- 10 registered concepts
        |
cex_media_produce.py        -- concept x format x lens x lang
        |
_courses/{tier}/{module}/   -- source markdown
        |
rendered/                   -- gitignored output (video, slides, audio)
        |
External platforms          -- Hotmart, YouTube, Spotify, NotebookLM
```

## Directory Convention

```
_courses/
  driver/                   -- Tier 1: non-technical users
    01_what_is_ai_brain/
    02_eight_steps/
    03_twelve_pillars/
    04_naming_things/
  mechanic/                 -- Tier 2: power users / AI practitioners
    01_customize_nucleus/
    02_sin_lenses/
    03_brand_config/
    04_crew_templates/
  engineer/                 -- Tier 3: contributors (points to CONTRIBUTING.md)
  rendered/                 -- gitignored: video, audio, PDF output
```

## Generating Content

```bash
# List available concepts
python _tools/cex_media_produce.py --list

# Generate a module
python _tools/cex_media_produce.py --concept 8f_pipeline --format slides --lang pt-br

# Audio via NotebookLM (requires auth)
python _tools/cex_media_produce.py --concept artificial_sins --format audio --lang pt-br
```

## This directory is STRIPPED from the public OSS export

`cex_export_public.sh` removes `_courses/` automatically. The open-source repo
is dev-only. Monetized content lives here, published to external platforms.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_courses_driver_tier]] | related | 0.32 |
| [[media_pipeline]] | related | 0.28 |
| [[spec_content_factory_v1]] | related | 0.22 |
| [[p01_kc_notebooklm_integration]] | related | 0.20 |
| [[spec_course_pipeline_wiring]] | related | 0.20 |
| [[bld_collaboration_audio_tool]] | related | 0.20 |
| [[cex_doctor_command]] | related | 0.20 |
| [[spec_mentor_didactic_engine]] | related | 0.18 |
| [[spec_media_pipeline_how_to]] | related | 0.18 |
| [[audio-tool-builder]] | related | 0.18 |
