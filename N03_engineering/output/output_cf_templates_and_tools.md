---
id: n03_output_cf_templates_and_tools
kind: context_doc
pillar: P01
mission: MISSION_content_factory_wave2
nucleus: N03
task: build_prompt_templates_and_tools
status: COMPLETE
artifacts_created: 14
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
quality: 9.1
tags: [output, content_factory, wave2, N03]
tldr: "Build report for Content Factory wave2 — 14 artifacts (7 prompt_templates + 7 function_defs)"
density_score: 1.0
---

# Output: Content Factory — Prompt Templates + Production Tools

## Summary
14 artifacts created for the Content Factory pipeline. 7 prompt_template (P03) + 7 function_def (P04). All follow 8F pipeline, all have quality: null (peer-review pending).

## Prompt Templates (P03)

| # | File | ID | Status |
|---|------|----|--------|
| 1 | `P03_prompts/templates/content_factory/p03_pt_cf_video_script.md` | p03_pt_cf_video_script | DONE |
| 2 | `P03_prompts/templates/content_factory/p03_pt_cf_lesson_script.md` | p03_pt_cf_lesson_script | DONE |
| 3 | `P03_prompts/templates/content_factory/p03_pt_cf_course_outline.md` | p03_pt_cf_course_outline | DONE |
| 4 | `P03_prompts/templates/content_factory/p03_pt_cf_ebook_chapter.md` | p03_pt_cf_ebook_chapter | DONE |
| 5 | `P03_prompts/templates/content_factory/p03_pt_cf_slide_deck.md` | p03_pt_cf_slide_deck | DONE |
| 6 | `P03_prompts/templates/content_factory/p03_pt_cf_quiz.md` | p03_pt_cf_quiz | DONE |
| 7 | `P03_prompts/templates/content_factory/p03_pt_cf_social_post.md` | p03_pt_cf_social_post | DONE |

## Function Definitions (P04)

| # | File | ID | Tool/API | Status |
|---|------|----|----------|--------|
| 1 | `P04_tools/functions/content_factory/p04_fn_cf_canva_create.md` | p04_fn_cf_canva_create | Canva API | DONE |
| 2 | `P04_tools/functions/content_factory/p04_fn_cf_canva_export.md` | p04_fn_cf_canva_export | Canva API | DONE |
| 3 | `P04_tools/functions/content_factory/p04_fn_cf_elevenlabs_tts.md` | p04_fn_cf_elevenlabs_tts | ElevenLabs API | DONE |
| 4 | `P04_tools/functions/content_factory/p04_fn_cf_pdf_generate.md` | p04_fn_cf_pdf_generate | Typst/Pandoc/WeasyPrint | DONE |
| 5 | `P04_tools/functions/content_factory/p04_fn_cf_slides_generate.md` | p04_fn_cf_slides_generate | Marp CLI | DONE |
| 6 | `P04_tools/functions/content_factory/p04_fn_cf_video_assemble.md` | p04_fn_cf_video_assemble | FFmpeg | DONE |
| 7 | `P04_tools/functions/content_factory/p04_fn_cf_ebook_compile.md` | p04_fn_cf_ebook_compile | Pandoc | DONE |

## Pipeline Coverage

```
Brief → Course Outline → Lesson Scripts → Slide Decks → Video Scripts
                                              ↓              ↓
                                         Marp (slides)   ElevenLabs (TTS)
                                              ↓              ↓
                                         Canva (design)  FFmpeg (video)
                                              ↓              ↓
                                         Export (PDF/PPTX) Ebook (Pandoc)
                                                            ↓
                                                     Social Posts (promo)
                                                            ↓
                                                     Quiz (assessment)
```

## Dependencies Identified
- `p03_pt_cf_course_outline` → feeds into `p03_pt_cf_lesson_script` (per-lesson generation)
- `p03_pt_cf_lesson_script` → feeds into `p03_pt_cf_slide_deck` + `p03_pt_cf_video_script`
- `p03_pt_cf_video_script` → feeds into `p04_fn_cf_elevenlabs_tts` → `p04_fn_cf_video_assemble`
- `p03_pt_cf_slide_deck` → feeds into `p04_fn_cf_slides_generate` or `p04_fn_cf_canva_create`
- `p03_pt_cf_ebook_chapter` → feeds into `p04_fn_cf_ebook_compile`
- All content → feeds into `p03_pt_cf_social_post` (promotion)
- All content → feeds into `p03_pt_cf_quiz` (assessment)

## Missing (out of scope for this wave)
- DAG/workflow artifact connecting templates → tools in execution order
- Chain artifact for multi-step content generation
- Brand template IDs (requires Canva API bootstrap)
- ElevenLabs voice_id registry (requires voice cloning setup)
