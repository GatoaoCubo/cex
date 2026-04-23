---
quality: 8.7
id: spec_mentor_didactic_engine
kind: constraint_spec
pillar: P06
title: "Spec -- Mentor Didactic Engine: Self-Teaching Repo"
version: 1.0.0
created: 2026-04-19
author: n07_orchestrator
domain: teaching + media production
quality_target: 9.0
status: SPEC
scope: N04 + N05 + N07
depends_on: [spec_metaphor_dictionary, cex_notebooklm.py]
tags: [mentor, didactic, teaching, notebooklm, media, multilens, infoproduct]
tldr: "Transform /mentor from vocabulary lookup into a full didactic engine that teaches CEX through multiple analogy lenses and produces media (text, audio, video, PPT) in EN + PT-BR."
density_score: 0.95
updated: "2026-04-22"
---

# Spec -- Mentor Didactic Engine

## Problem

/mentor today is a flat vocabulary lookup. Users ask "what kind for X?" and get a table.
This does not TEACH. It answers. Teaching requires narrative, analogy, discovery, and
multi-modal content. The repo should teach itself to strangers -- the code is the proof,
the methodology is the product.

## Vision

/mentor becomes a **didactic engine** with 3 layers:

```
Layer 1: LENS SYSTEM (multi-analogy translator)
  Factory lens | City lens | Biology lens | Game lens
  Each lens maps ALL 293 kinds + 8F + 12P + 8 nuclei to a coherent metaphor world

Layer 2: TEACHING MODES (storytelling + socratic hybrid)
  /mentor explain <concept>        -- narrative storytelling
  /mentor quiz <concept>           -- socratic discovery questions
  /mentor translate <concept>      -- technical -> metaphor (any lens)
  /mentor reverse <metaphor>       -- metaphor -> technical
  /mentor journey <from> <to>      -- guided learning path between concepts

Layer 3: MEDIA PIPELINE (full stack production)
  /mentor produce <concept> --format text|audio|video|ppt|all --lang en|pt|both
  Wires to N05 via NotebookLM + Playwright + PPT generation
```

## Decisions (from user)

- DP1: Storytelling + Socratic hybrid (narrative with discovery questions)
- DP2: Multi-lens (factory, city, biology, game analogy systems)
- DP3: Full stack media (text + NotebookLM audio/video + diagrams + PPTs)
- DP4: Parallel bilingual (EN + PT-BR generated natively, not translated)

## Artifacts

### Wave 1: Lens System (6 artifacts) -- N04

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N04_knowledge/P01_knowledge/kc_lens_factory.md | knowledge_card | 8KB | Factory lens: 293 kinds + 8F + 12P + nuclei mapped to factory metaphors |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_city.md | knowledge_card | 8KB | City lens: infrastructure, districts, services, governance |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_biology.md | knowledge_card | 8KB | Biology lens: organism, organs, cells, DNA, nervous system |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_game.md | knowledge_card | 8KB | Game lens: existing metaphor dictionary expanded to full world |
| CREATE | N04_knowledge/P01_knowledge/kc_lens_index.md | knowledge_card | 4KB | Master index: concept -> all 4 lens translations |
| UPDATE | _docs/specs/spec_metaphor_dictionary.md | context_doc | +3KB | Add lens references, expand coverage to 293 kinds |

### Wave 2: Teaching Engine (4 artifacts) -- N04

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N04_knowledge/P03_prompt/mentor_storyteller.md | prompt_template | 6KB | Narrative template: concept -> story with beginning/middle/end |
| CREATE | N04_knowledge/P03_prompt/mentor_socratic.md | prompt_template | 5KB | Socratic template: concept -> 5-question discovery sequence |
| CREATE | N04_knowledge/P03_prompt/mentor_journey.md | prompt_template | 5KB | Learning path template: prerequisite graph + guided walkthrough |
| CREATE | N04_knowledge/P01_knowledge/kc_concept_graph.md | knowledge_card | 6KB | Prerequisite graph: which concepts depend on which (for /mentor journey) |

### Wave 3: Mentor Skill Rewrite (2 artifacts) -- N07

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | .claude/commands/mentor.md | instruction | 8KB | Full rewrite: explain/quiz/translate/reverse/journey/produce subcommands |
| CREATE | .claude/skills/n07/mentor_engine.md | instruction | 6KB | Orchestration skill: lens selection, mode routing, media dispatch |

### Wave 4: Media Production Pipeline (5 artifacts) -- N05

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N05_operations/P04_tools/media_pipeline.md | cli_tool | 4KB | Spec for cex_media_produce.py: orchestrates text/audio/video/ppt |
| CREATE | _tools/cex_media_produce.py | (code) | 12KB | CLI tool: concept -> multi-format output via NotebookLM + Playwright |
| CREATE | N05_operations/P03_prompt/prompt_notebooklm_source.md | prompt_template | 4KB | Template: renders a CEX concept as NotebookLM-optimized source doc |
| CREATE | N05_operations/P03_prompt/prompt_ppt_generator.md | prompt_template | 4KB | Template: renders concept as slide deck (Marp markdown or reveal.js) |
| CREATE | N05_operations/P09_config/media_config.yaml | (config) | 2KB | Media pipeline config: output dirs, formats, NotebookLM notebook IDs |

### Wave 5: Bilingual Content Layer (3 artifacts) -- N04

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N04_knowledge/P03_prompt/mentor_locale_en.md | prompt_template | 3KB | EN voice: tone, idioms, cultural references for English audience |
| CREATE | N04_knowledge/P03_prompt/mentor_locale_ptbr.md | prompt_template | 3KB | PT-BR voice: tone, idioms, cultural references for Brazilian audience |
| CREATE | N04_knowledge/P01_knowledge/kc_bilingual_term_map.md | knowledge_card | 5KB | Canonical term translations: EN <-> PT-BR for all 293 kinds + 8F + 12P |

### Wave 6: Example Content + Integration Test (4 artifacts) -- N04 + N05

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | examples/06_mentor_teaching/explain_8f.md | (example) | 3KB | Full storytelling explanation of 8F pipeline (factory lens, EN) |
| CREATE | examples/06_mentor_teaching/quiz_nuclei.md | (example) | 3KB | Socratic quiz about the 7 nuclei (city lens, PT-BR) |
| CREATE | examples/06_mentor_teaching/journey_beginner.md | (example) | 4KB | Learning path: zero to first artifact (game lens, EN) |
| CREATE | examples/06_mentor_teaching/README.md | (doc) | 2KB | How to use /mentor to generate teaching content |

## Dependency Graph

```
Wave 1 (Lenses) ──────> Wave 2 (Teaching Engine) ──> Wave 3 (Skill Rewrite)
                                                         |
Wave 4 (Media Pipeline) ─────────────────────────────────┤
                                                         |
Wave 5 (Bilingual) ──────────────────────────────────────┘
                                                         |
                                                    Wave 6 (Examples)
```

- W1 and W4 are independent (can run in parallel)
- W2 depends on W1 (needs lenses)
- W3 depends on W2 + W4 (needs teaching templates + media pipeline)
- W5 depends on W2 (needs teaching templates)
- W6 depends on W3 + W5 (integration test)

## Acceptance Criteria

- [ ] `/mentor explain 8f --lens factory` produces a narrative story
- [ ] `/mentor quiz nuclei --lens city` produces 5 discovery questions
- [ ] `/mentor translate knowledge_card --lens biology` maps to biological metaphor
- [ ] `/mentor reverse "the factory assembly line"` returns "8F pipeline"
- [ ] `/mentor journey beginner` produces a guided learning path
- [ ] `/mentor produce 8f --format all --lang both` generates text + audio source + PPT in EN + PT-BR
- [ ] All 4 lens KCs have complete coverage of 8F + 12P + 8 nuclei + top 20 kinds
- [ ] `cex_media_produce.py` successfully uploads to NotebookLM and generates slide deck
- [ ] Examples in examples/06_mentor_teaching/ are complete and runnable
- [ ] All artifacts pass doctor + quality >= 9.0

## Media Pipeline Detail

```
/mentor produce <concept> --format all --lang both
  |
  v
cex_media_produce.py
  |
  |-- TEXT: render concept via mentor_storyteller.md + lens KC -> markdown
  |     |-- EN: mentor_locale_en.md voice
  |     |-- PT-BR: mentor_locale_ptbr.md voice
  |
  |-- AUDIO: render concept as NotebookLM source doc -> upload -> activate Audio Overview
  |     |-- Uses: cex_notebooklm.py --upload + --studio
  |     |-- Output: 2-host podcast discussing the concept
  |     |-- EN notebook + PT-BR notebook (separate)
  |
  |-- VIDEO: NotebookLM Video Overview (if available) or Audio + slides
  |     |-- Uses: cex_notebooklm.py --studio (video flag)
  |
  |-- PPT: render concept via prompt_ppt_generator.md -> Marp markdown -> PDF/PPTX
  |     |-- Uses: marp-cli (npx @marp-team/marp-cli slide.md --pptx)
  |     |-- Output: 10-15 slide deck with diagrams
  |
  v
Output in: _output/mentor/{concept}/{lang}/
  text.md | audio_source.md | slides.md | slides.pptx
```

## Lens Architecture

Each lens KC follows the same structure:

```markdown
## Core Mapping

| CEX Concept | {Lens} Metaphor | One-line Explanation |
|-------------|-----------------|---------------------|
| 8F pipeline | {lens-specific} | ... |
| 12 pillars  | {lens-specific} | ... |
| nucleus     | {lens-specific} | ... |
| kind        | {lens-specific} | ... |
| builder     | {lens-specific} | ... |
| ISO         | {lens-specific} | ... |
| GDP         | {lens-specific} | ... |
| sin lens    | {lens-specific} | ... |

## Extended Mapping (top 20 kinds)

| Kind | {Lens} Metaphor | Teaching Story Seed |
|------|-----------------|---------------------|
| knowledge_card | ... | ... |
| agent | ... | ... |
| ... | ... | ... |

## Discovery Questions (Socratic seeds)

1. If {lens metaphor for X} does Y, what happens when Z?
2. ...
```

## Done When

- [ ] All 24 artifacts pass doctor
- [ ] All compile successfully
- [ ] Quality >= 9.0 on all scored artifacts
- [ ] /mentor explain/quiz/translate/reverse/journey all work
- [ ] /mentor produce generates files in _output/mentor/
- [ ] Signal sent: n04 + n05 -> complete -> score
