---
id: p03_ch_brief_to_multiformat
kind: chain
pillar: P03
version: "1.0.0"
created: "2026-04-08"
updated: "2026-04-08"
author: "n03_builder"
title: "Brief to Multi-Format Content Chain"
steps_count: 7
flow: sequential
input_format: "User brief (free text or YAML: topic, audience, formats, tone)"
output_format: "7 format-specific content drafts (course outline, video script, ebook manuscript, slide deck, podcast brief, social posts, landing page copy)"
context_passing: full
error_strategy: fail_fast
domain: "content_factory"
quality: 9.2
tags: [chain, content-factory, multi-format, brief-expansion, prompt-pipeline]
tldr: "7-step prompt chain: raw brief -> validated brief -> research prompt -> content plan -> longform draft -> format fan-out -> format-specific drafts"
density_score: 0.92
---

## Purpose

Decomposes a raw user brief into 7 publishable content format drafts through a sequence
of prompt calls. Each step is exactly one LLM call that refines, expands, or transforms
the content progressively. This chain defines the PROMPT logic (what the LLM generates at
each step); the RUNTIME orchestration (which nucleus executes, signals, waves) lives in
wf_content_factory_v1.md (P12 workflow). The chain references existing prompt templates
from P03_prompts/templates/content_factory/.

## Steps

### Step 1: Validate and Normalize Brief
1. **Input**: Raw user brief (string, 10-500 words) + brand_config.yaml reference
2. **Prompt**: Extract and normalize: topic (string), audience (string), requested_formats (list from: course, video, ebook, presentation, podcast, social, landing_page), tone (enum: technical, casual, inspirational, formal), constraints (max duration, word count limits). If any field is missing, infer from context and flag as inferred. Validate topic is specific enough for content production (reject "something about tech"). Output as structured YAML.
3. **Output**: Validated brief YAML (topic, audience, formats[], tone, constraints{}, inferred_fields[])

### Step 2: Expand Brief with Research Questions
1. **Input**: Validated brief YAML from Step 1
2. **Prompt**: For the given topic and audience, generate: 5-8 research questions that would produce comprehensive coverage, 3-5 competitor/reference content URLs to analyze, 10-15 target keywords for SEO, audience pain points (3-5) and desired outcomes (3-5). Structure as research_plan.yaml.
3. **Output**: Research plan YAML (questions[], references[], keywords[], pain_points[], outcomes[])

### Step 3: Generate Content Plan
1. **Input**: Validated brief YAML + research plan YAML from Steps 1-2
2. **Prompt**: Create a unified content plan that maps the topic across all requested formats. For each format, define: angle (what unique value this format delivers), structure (sections/modules/slides count), estimated length, key messages (3-5 per format), CTA per format. The plan must ensure consistency -- all formats tell the same story from different angles. Reference constraint specs: cs_cf_video, cs_cf_course, cs_cf_ebook, cs_cf_presentation, cs_cf_podcast.
3. **Output**: Content plan YAML (formats[]{format, angle, structure, length, messages[], cta})

### Step 4: Author Master Longform Draft
1. **Input**: Content plan YAML + research plan YAML + brand_config context
2. **Prompt**: Write a comprehensive longform article (3000-8000 words) that serves as the canonical source for all format adaptations. Structure with H2/H3 headers matching the content plan. Include: introduction with hook, core argument sections, data/examples sections, practical applications, conclusion with CTA. Apply brand voice from brand_config (tone, personality, vocabulary). This is the "trunk" from which all format "branches" derive.
3. **Output**: Master longform draft (Markdown, 3000-8000 words, structured headers)

### Step 5: Adapt to Course Format
1. **Input**: Master longform draft + content plan (course section) + cs_cf_course constraints
2. **Prompt**: Transform the longform into a course structure using p03_pt_cf_course_outline template. Produce: course title, 5-12 modules, 3-8 lessons per module, learning objectives per module, quiz questions per module (5-10 multiple choice), estimated duration per lesson. Each lesson script follows p03_pt_cf_lesson_script template with objectives, key points, exercises, and summary.
3. **Output**: Course outline YAML + lesson script stubs (module_N_lesson_M.md format)

### Step 6: Adapt to Short Formats
1. **Input**: Master longform draft + content plan (video, social, podcast sections) + constraint specs
2. **Prompt**: From the longform, extract and transform into 3 short formats simultaneously: (a) Video script (90s) using p03_pt_cf_video_script -- hook(5s)/build(30s)/benefit(25s)/proof(20s)/CTA(10s); (b) Social campaign (7 posts) using p03_pt_cf_social_post -- per-platform hooks for IG, LinkedIn, X, YouTube; (c) Podcast episode brief -- key talking points, intro/body/outro structure, estimated 15-25 min. Output all three as structured YAML.
3. **Output**: Short format bundle YAML (video_script{}, social_posts[], podcast_brief{})

### Step 7: Adapt to Long Formats
1. **Input**: Master longform draft + content plan (ebook, presentation, landing_page sections) + constraint specs
2. **Prompt**: From the longform, produce 3 long formats: (a) eBook manuscript using p03_pt_cf_ebook_chapter -- 5-15 chapters, 2K-5K words each, intro/body/examples/summary per chapter; (b) Slide deck using p03_pt_cf_slide_deck -- 10-30 slides, 3-5 bullets each, speaker notes; (c) Landing page copy -- hero section, problem/solution, features, testimonials placeholder, pricing placeholder, CTA. Output as structured YAML + Markdown.
3. **Output**: Long format bundle (ebook_chapters[], slides[], landing_page{})

## Data Flow

```text
Step 1 (brief YAML) --> Step 2 (research plan) --> Step 3 (content plan)
    --> Step 4 (master longform) --> Step 5 (course)
                                 --> Step 6 (video + social + podcast)
                                 --> Step 7 (ebook + slides + landing page)
```

Context passing: full accumulation. Each step receives all prior outputs as context.
Steps 5, 6, 7 share the same input (master longform) and can execute as parallel
prompt calls within this chain if the runtime supports it (see wf_content_factory_v1
Wave 4 for parallel dispatch).

## Error Handling

1. **Strategy**: fail_fast for Steps 1-4 (sequential dependency, no recovery)
2. **On failure at Step 1**: Reject brief with specific missing-field error, request user resubmit
3. **On failure at Steps 2-4**: Log error, surface to orchestrator for retry decision
4. **On failure at Steps 5-7**: Skip failing format, continue with remaining formats, flag gap in output manifest
5. **Retry policy**: Steps 5-7 may retry once if output fails constraint spec validation (length, structure)

## Prompt Template References

| Step | Template | Constraint Spec |
|------|----------|-----------------|
| 1 | (inline validation prompt) | cs_cf_brief |
| 2 | (inline research expansion) | -- |
| 3 | (inline content planning) | all cs_cf_* |
| 4 | (inline longform authoring) | -- |
| 5 | p03_pt_cf_course_outline + p03_pt_cf_lesson_script + p03_pt_cf_quiz | cs_cf_course |
| 6 | p03_pt_cf_video_script + p03_pt_cf_social_post | cs_cf_video + cs_cf_podcast |
| 7 | p03_pt_cf_ebook_chapter + p03_pt_cf_slide_deck | cs_cf_ebook + cs_cf_presentation |

## References

1. `_docs/specs/spec_content_factory_v1.md` -- parent spec defining the pipeline
2. `P03_prompts/templates/content_factory/` -- 7 prompt templates consumed by Steps 5-7
3. `P03_prompts/constraints/content_factory/` -- 6 constraint specs governing format output
4. `N03_engineering/workflows/wf_content_factory_v1.md` -- runtime workflow that executes this chain
5. `P12_orchestration/dags/content_factory/dag_cf_master.md` -- dependency graph
