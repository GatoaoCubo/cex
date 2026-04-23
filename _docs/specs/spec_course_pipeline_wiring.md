---
id: spec_course_pipeline_wiring
kind: constraint_spec
pillar: P06
title: "Spec -- Course Pipeline End-to-End Wiring"
version: 1.0.0
created: "2026-04-21"
author: n07_orchestrator
domain: infoproduct
quality: 8.7
status: SPEC
scope: n04_knowledge + n05_operations
depends_on:
  - spec_courses_driver_tier
  - spec_oss_wiring_final
tags: [spec, courses, infoproduct, pipeline, wiring, templates]
tldr: "Fix 10 wiring gaps between course modules, teaching templates, media pipeline, and lens index so source content flows end-to-end."
density_score: 0.93
updated: "2026-04-22"
---

# Spec: Course Pipeline End-to-End Wiring

## Problem

The course pipeline has all components built but they are not wired together:
- 4 course modules exist (`_courses/driver/*.md`) with rich PT-BR content
- 3 new lens KCs exist (bible, car, technical)
- `resolve_source_module()` in `cex_media_produce.py` correctly reads source content
- BUT: all 5 teaching templates lack `{{source_content}}` -- content is resolved then silently dropped
- Lens index is stale (4 of 7 lenses)
- Audio and PPT producers never call `resolve_source_module()`

This means the media pipeline produces identical generic output regardless of which
course module is being rendered. The 7-lens x 4-module matrix produces 28 files
that all say the same thing.

## Vision

After this spec executes:
1. `cex_media_produce.py --concept structured_thinking --lens bible --format text`
   produces a Bible-framed lesson about structured thinking (not a generic concept overview)
2. `cex_media_produce.py --concept seven_sins --format audio_source`
   produces audio script with actual 7-sins module content injected
3. `cex_media_produce.py --concept twelve_pillars --format ppt`
   produces slides with real pillar descriptions from the module
4. Lens index covers all 7 lenses with cross-reference table

## Decisions (from manifest)

- Source: decision_manifest_courses.yaml
- DP5: Format pipeline = text -> slides -> audio -> video
- DP6: All 7 lenses scaffolded
- DP7: No code, PT-BR, quality: null

## Artifacts

### Wave 1: Template Wiring (5 edits, 1 update)

| # | Action | Path | Kind | Notes |
|---|--------|------|------|-------|
| 1 | EDIT | N04_knowledge/P03_prompt/mentor_storyteller.md | prompt_template | Add `{{source_content}}` section between concept_definition and body |
| 2 | EDIT | N04_knowledge/P03_prompt/mentor_socratic.md | prompt_template | Add `{{source_content}}` for quiz grounding |
| 3 | EDIT | N04_knowledge/P03_prompt/mentor_journey.md | prompt_template | Add `{{source_content}}` for path context |
| 4 | EDIT | N05_operations/P03_prompt/prompt_notebooklm_source.md | prompt_template | Add `{{source_content}}` for podcast grounding |
| 5 | EDIT | N05_operations/P03_prompt/prompt_ppt_generator.md | prompt_template | Add `{{source_content}}` for slide content |
| 6 | EDIT | N04_knowledge/P01_knowledge/kc_lens_index.md | knowledge_card | Add bible, car, technical columns to cross-ref table |

Dependencies: None. Wave 1 is self-contained.

### Wave 2: Pipeline Code Wiring (1 edit)

| # | Action | Path | Kind | Notes |
|---|--------|------|------|-------|
| 7 | EDIT | _tools/cex_media_produce.py | cli_tool | Add resolve_source_module() calls to produce_audio_source() and produce_ppt() |

Dependencies: Wave 1 (templates must have the variable before pipeline injects it).

### Wave 3: Validation (dry-run)

| # | Action | Path | Kind | Notes |
|---|--------|------|------|-------|
| 8 | TEST | _output/courses/driver/01_structured_thinking/ | output | Dry-run: text x bible, text x car, text x factory |
| 9 | TEST | (stdout) | validation | Verify word counts differ per concept (not identical) |
| 10 | TEST | (stdout) | validation | Verify source_content appears in rendered output |

Dependencies: Wave 2 (code must be wired before testing).

## Acceptance Criteria

- [ ] All 5 templates contain `{{source_content}}` or `{{#source_content}}...{{/source_content}}`
- [ ] kc_lens_index.md lists all 7 lenses with mappings
- [ ] produce_audio_source() calls resolve_source_module()
- [ ] produce_ppt() calls resolve_source_module()
- [ ] Dry-run: structured_thinking x bible != structured_thinking x factory (word counts differ)
- [ ] Dry-run: structured_thinking x bible != seven_sins x bible (content differs)
- [ ] Zero Python errors on any dry-run

## Nucleus Assignments

| Wave | Nucleus | Role |
|------|---------|------|
| W1 | N04 (knowledge) + N05 (operations) | Edit templates + lens index |
| W2 | N05 (operations) | Pipeline code fix |
| W3 | N07 (orchestrator) | Validation |

N07 executes W1+W2 via in-session subagents (template edits are surgical, not full builds).
N07 validates W3 directly.
