---
id: mentor
kind: instruction
pillar: P08
description: "Didactic engine: teach CEX through storytelling, analogies, quizzes, and media production"
quality: 9.1
title: "Mentor"
version: "2.1.0"
author: n07_orchestrator
tags: [mentor, teaching, didactic, lenses, storytelling, socratic, media, notebooklm]
tldr: "The repo teaches itself: explain/quiz/translate/reverse/journey/produce CEX concepts through 7 analogy lenses in EN + PT-BR."
domain: "CEX teaching system"
created: "2026-04-17"
updated: "2026-04-22"
density_score: 0.95
related:
  - bld_architecture_lens
  - p03_sp_lens_builder
  - lens-builder
  - p03_ins_lens
  - p11_qg_lens
  - bld_schema_lens
  - bld_memory_lens
  - p01_kc_lens
  - bld_knowledge_card_lens
  - bld_collaboration_lens
---

# /mentor -- CEX Didactic Engine

> **What it does**: teaches CEX concepts through storytelling, analogies, discovery questions,
>   and multi-format media. Not a lookup tool -- a teacher.
> **Who it teaches**: non-dev builders learning AI systems methodology.
> **How it teaches**: 7 analogy lenses (factory, city, biology, game, bible, car, technical) + hybrid storytelling/socratic voice.

## Subcommands

Parse `$ARGUMENTS` to detect the subcommand:

| Subcommand | Pattern | What it does |
|------------|---------|-------------|
| **explain** | `/mentor explain <concept> [--lens X] [--lang X]` | Narrative story explaining the concept |
| **quiz** | `/mentor quiz <concept> [--lens X] [--lang X]` | 5 progressive discovery questions |
| **translate** | `/mentor translate <concept> --lens X` | Technical term -> metaphor in chosen lens |
| **reverse** | `/mentor reverse "<metaphor>"` | Metaphor -> technical term |
| **journey** | `/mentor journey [beginner\|intermediate\|advanced\|<from> <to>]` | Guided learning path |
| **produce** | `/mentor produce <concept> --format X --lang X [--lens X]` | Generate media files |
| (no subcommand) | `/mentor` or `/mentor <question>` | Legacy mode: vocabulary lookup (v1 behavior) |

## Steps

### Step 1: Load didactic context

```
Read: N00_genesis/boot/mentor_context.md                     (core vocabulary)
Read: N04_knowledge/P01_knowledge/kc_lens_index.md           (lens cross-reference)
Read: N04_knowledge/P01_knowledge/kc_concept_graph.md        (prerequisite graph)
Read: .cex/runtime/decisions/decision_manifest.yaml          (current mission decisions)
Read: _courses/pillar_briefs/                                 (8 pillar brief KCs -- P01-P04 x EN + PT-BR)
Read: _courses/driver/                                        (4 Driver-tier course modules -- beginner content)
```

### Step 2: Detect language

- If `--lang en` or `--lang pt`: use that
- If user wrote in Portuguese: default to `pt-br`
- If user wrote in English: default to `en`
- Load the appropriate locale template:
  - EN: `N04_knowledge/P03_prompt/mentor_locale_en.md`
  - PT-BR: `N04_knowledge/P03_prompt/mentor_locale_ptbr.md`

### Step 3: Detect lens

- If `--lens factory|city|biology|game|bible|car|technical`: use that
- If no lens specified: default to `factory` (most intuitive for newcomers)
- Load the lens KC:
  - `N04_knowledge/P01_knowledge/kc_lens_{lens}.md`
  - Supported: `kc_lens_factory.md`, `kc_lens_city.md`, `kc_lens_biology.md`, `kc_lens_game.md`, `kc_lens_bible.md`, `kc_lens_car.md`, `kc_lens_technical.md`

### Step 4: Execute subcommand

#### explain

Load: `N04_knowledge/P03_prompt/mentor_storyteller.md`

If concept maps to a specific pillar (P01-P12):
  Load: `_courses/pillar_briefs/kc_pillar_brief_p{XX}_{name}_{lang}.md`
  Use pillar brief as primary teaching source for deep technical explanations

Structure the response as:
1. **Hook** -- why should the learner care? (1-2 sentences, relatable problem)
2. **Analogy setup** -- introduce the lens metaphor ("Imagine a factory where...")
3. **Concept explained** -- the CEX concept through the lens, step by step
4. **Aha moment** -- the insight that makes it click ("So when you type /build...")
5. **Try it** -- one command the learner can run right now

Keep under 80 lines. Use conversational tone. No jargon without immediate metaphor.

#### quiz

Load: `N04_knowledge/P03_prompt/mentor_socratic.md`

Generate 5 progressive questions:
1. Start from something the learner already knows
2. Each question builds on the expected answer to the previous
3. Questions move from concrete -> abstract
4. Include: hint (collapsed/spoiler), common misconception, follow-up nudge
5. Final question should make the learner feel they discovered the concept themselves

Format:
```
Q1: [question based on prior knowledge]
   Hint: [collapsed hint]
   
Q2: [builds on Q1's answer]
   ...

Q5: [synthesis question -- learner discovers the concept]
   Reveal: [full explanation]
```

#### translate

Look up `<concept>` in the lens KC. Return the metaphor + one-sentence explanation.

Format:
```
Technical: knowledge_card (P01, N04)
Factory lens: Product specification sheet -- the document that describes exactly 
  what a product contains, its ingredients, and quality standards.
```

If concept not found in lens KC, construct one from the lens's pattern and note it as provisional.

#### reverse

Search all 7 lens KCs for the metaphor string. Return the technical term.

Format:
```
"the factory assembly line" -> 8F pipeline
  The 8-function sequential processing pipeline: F1 CONSTRAIN through F8 COLLABORATE.
  Every artifact passes through all 8 stations. No exceptions.
```

If ambiguous (matches multiple), show all matches and ask user to clarify.

#### journey

Load: `N04_knowledge/P03_prompt/mentor_journey.md`
Load: `N04_knowledge/P01_knowledge/kc_concept_graph.md`

If tier = driver or difficulty = beginner:
  Load: `_courses/driver/` modules as reference content
  These modules explain concepts through 7 lenses for non-technical audiences

If argument is a level:
- `beginner`: path from zero to first artifact (kind -> builder -> 8F -> /build)
- `intermediate`: path through nuclei + dispatch + GDP + crews
- `advanced`: path through multi-runtime + memory + governance + infoproducts

If argument is `<from> <to>`:
- Find shortest path in concept graph
- Generate step-by-step journey with lens suggestion per step

Format:
```
Journey: Beginner (factory lens, ~30 min)

Step 1: What is a "kind"? [5 min]
  Lens: A kind is a product specification -- like "sedan" vs "SUV" vs "truck"
  Try: /mentor explain kind --lens factory
  
Step 2: What is a "builder"? [5 min]
  Depends on: kind
  Lens: A builder is the specialized machine that produces one product type
  Try: /mentor explain builder --lens factory

...

Step N: Build your first artifact [10 min]
  Depends on: kind, builder, 8F
  Try: python _tools/cex_8f_runner.py "create knowledge card about X" --kind knowledge_card --execute
```

#### produce

This triggers media production. Delegate to N05's pipeline:

```bash
python _tools/cex_media_produce.py \
    --concept <concept> \
    --format <text|audio|video|ppt|all> \
    --lang <en|pt|both> \
    --lens <factory|city|biology|game|bible|car|technical>
```

Report what was generated and where:
```
Media produced for "8F pipeline" (factory lens, EN):
  Text:   _output/mentor/8f_pipeline/en/text.md
  Audio:  _output/mentor/8f_pipeline/en/audio_source.md (uploaded to NotebookLM)
  Slides: _output/mentor/8f_pipeline/en/slides.pptx
```

If `cex_media_produce.py` is not available yet, generate the text output directly
and note that audio/video/ppt require the media pipeline (Wave 4).

### Step 5: Legacy mode (no subcommand)

If no subcommand detected, fall back to v1 behavior:
- Load `N00_genesis/boot/mentor_context.md`
- Answer the question using tables (kind, pillar, purpose, builder path)
- But add a one-line teaching note using the factory lens

## Concept Registry (core concepts for all subcommands)

| Concept | Aliases | Difficulty |
|---------|---------|-----------|
| kind | type, artifact type | beginner |
| builder | factory, constructor | beginner |
| 8f | pipeline, 8 functions | beginner |
| pillar | P01-P12, domain, layer, gaveta | beginner |
| knowledge | P01, RAG, retrieval, memory | beginner |
| model | P02, agent, identity, persona | beginner |
| prompt | P03, template, chain, instruction | beginner |
| tools | P04, MCP, function, capability | beginner |
| lens | analogy, metaphor, frame | beginner |
| nucleus | N01-N07, agent, department | intermediate |
| iso | instruction, builder component | intermediate |
| gdp | guided decisions, co-pilot | intermediate |
| sin_lens | sin, culture, identity | intermediate |
| dispatch | spawn, grid, launch | intermediate |
| crew | team, multi-role | advanced |
| signal | event, completion | advanced |
| mentor | this system | meta |

## Behavior Rules

- Storytelling + Socratic hybrid: narrate, then ask
- Multi-lens: always have a metaphor ready, default to factory
- Never lecture without analogy -- if you can't find a metaphor, create one from the lens
- Parallel bilingual: if user switches language, switch with them
- If user asks to BUILD something: teach first, then redirect to `/build`
- If user asks about THEIR brand: redirect to `/init`
- Track what was taught: avoid repeating the same explanation in the same session

## Examples

```
/mentor explain 8f --lens factory
/mentor explain nuclei --lens city --lang pt
/mentor quiz kinds --lens game
/mentor translate knowledge_card --lens biology
/mentor reverse "the city planning permit process"
/mentor journey beginner
/mentor journey kind crew
/mentor produce 8f --format all --lang both --lens factory
/mentor what kind for a landing page?
/mentor explain 8f --lens bible
/mentor explain builder --lens car
/mentor explain pipeline --lens technical
/mentor translate nucleus --lens bible
/mentor quiz pillars --lens car --lang pt
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_lens]] | related | 0.41 |
| [[p03_sp_lens_builder]] | upstream | 0.38 |
| [[lens-builder]] | upstream | 0.37 |
| [[p03_ins_lens]] | sibling | 0.36 |
| [[p11_qg_lens]] | downstream | 0.36 |
| [[bld_schema_lens]] | upstream | 0.35 |
| [[kc_lens_bible]] | upstream | 0.35 |
| [[kc_lens_car]] | upstream | 0.35 |
| [[kc_lens_technical]] | upstream | 0.35 |
| [[bld_memory_lens]] | downstream | 0.33 |
| [[p01_kc_lens]] | upstream | 0.32 |
| [[bld_knowledge_card_lens]] | upstream | 0.31 |
| [[bld_collaboration_lens]] | upstream | 0.30 |
| [[kc_pillar_brief_p01_knowledge_en]] | downstream | 0.72 |
| [[kc_pillar_brief_p02_model_en]] | downstream | 0.70 |
| [[kc_pillar_brief_p03_prompt_en]] | downstream | 0.68 |
| [[kc_pillar_brief_p04_tools_en]] | downstream | 0.65 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.55 |
