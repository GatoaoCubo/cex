---
quality: 8.7
id: spec_infoproduct_media_scale
kind: constraint_spec
pillar: P06
title: "Spec -- Infoproduct Media at Scale (10 Concepts x 3 Formats x EN)"
version: 1.0.0
created: 2026-04-19
author: n07_orchestrator
domain: mentor_media
quality_target: 9.0
status: SPEC
scope: N04 + N05
depends_on: [spec_mentor_didactic_engine, spec_notebooklm_chrome_cdp]
tags: [infoproduct, media, mentor, notebooklm, scale]
tldr: "Produce 10 infoproduct packages (text + audio_source + slides) for core CEX concepts, then batch-upload to NotebookLM"
density_score: 0.93
updated: "2026-04-22"
---

# Infoproduct Media at Scale

## Problem

CEX's monetization strategy is: open source the repo, sell teaching content about the methodology.
The 8F pipeline infoproduct was proven today (text + audio podcast + video + slides via NotebookLM).
Now we need to scale this to the 10 most valuable CEX concepts for users.

## Vision

A complete teaching library covering the 10 core CEX concepts, each with:
- text.md (long-form narrative, factory lens, EN)
- audio_source.md (NotebookLM-optimized, conversation-ready)
- slides.md + slides.pptx + slides.pdf (Marp presentation, 5-7 slides)

Total: 10 concepts x 3 formats = 30 content assets + 10 NotebookLM notebooks

## Proven Stack

| Component | Tool | Status |
|-----------|------|--------|
| Text generation | cex_media_produce.py --format text | PROVEN (8F) |
| Audio source | cex_media_produce.py --format audio | PROVEN (8F) |
| Slides | cex_media_produce.py --format ppt | PROVEN (8F) |
| NotebookLM upload | Chrome CDP + Playwright MCP | PROVEN (8F) |
| PPTX compilation | Marp CLI | PROVEN (8F) |

## Concepts (Priority Order)

### Wave 1: Foundations (3 concepts)

| # | Concept | Slug | Description | Lens |
|---|---------|------|-------------|------|
| 1 | 12 Pillars | pillars | The 12-domain architecture P01-P12 | factory |
| 2 | Nuclei | nuclei | The 7 sin-driven agents N01-N07 | city |
| 3 | Kinds | kinds | The 293-type artifact taxonomy | factory |

### Wave 2: Mechanics (3 concepts)

| # | Concept | Slug | Description | Lens |
|---|---------|------|-------------|------|
| 4 | GDP | gdp | Guided Decision Protocol: user decides WHAT | game |
| 5 | Builder | builder | 12-ISO agent that produces one kind | factory |
| 6 | Dispatch | dispatch | Grid orchestration: solo/grid/swarm | city |

### Wave 3: Advanced (4 concepts)

| # | Concept | Slug | Description | Lens |
|---|---------|------|-------------|------|
| 7 | Crews | crews | Multi-role team composition | game |
| 8 | Signals | signals | Inter-agent completion protocol | biology |
| 9 | Memory | memory | 4-type persistent knowledge system | biology |
| 10 | Sin Lens | sin_lens | Cultural DNA per nucleus | game |

## Artifacts

### Wave 1: Content Generation (N04, 9 artifacts)

N04 runs cex_media_produce.py for each concept in Wave 1.

| Action | Path | Format | Est. Size |
|--------|------|--------|-----------|
| CREATE | _output/mentor/pillars/en/text.md | text | 8KB |
| CREATE | _output/mentor/pillars/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/pillars/en/slides.md | ppt | 4KB |
| CREATE | _output/mentor/nuclei/en/text.md | text | 8KB |
| CREATE | _output/mentor/nuclei/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/nuclei/en/slides.md | ppt | 4KB |
| CREATE | _output/mentor/kinds/en/text.md | text | 8KB |
| CREATE | _output/mentor/kinds/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/kinds/en/slides.md | ppt | 4KB |

Command per concept:
```bash
python _tools/cex_media_produce.py --concept {slug} --format all --lens {lens} --lang en
```

### Wave 2: Content Generation (N04, 9 artifacts)

Same pattern for GDP, builder, dispatch concepts.

| Action | Path | Format | Est. Size |
|--------|------|--------|-----------|
| CREATE | _output/mentor/gdp/en/text.md | text | 8KB |
| CREATE | _output/mentor/gdp/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/gdp/en/slides.md | ppt | 4KB |
| CREATE | _output/mentor/builder/en/text.md | text | 8KB |
| CREATE | _output/mentor/builder/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/builder/en/slides.md | ppt | 4KB |
| CREATE | _output/mentor/dispatch/en/text.md | text | 8KB |
| CREATE | _output/mentor/dispatch/en/audio_source.md | audio | 12KB |
| CREATE | _output/mentor/dispatch/en/slides.md | ppt | 4KB |

### Wave 3: Content Generation (N04, 12 artifacts)

Same pattern for crews, signals, memory, sin_lens.

### Wave 4: NotebookLM Batch Upload (N05, 10 uploads)

N05 connects to Chrome CDP and uploads all 10 audio_source.md files to NotebookLM,
creating one notebook per concept. Triggers Audio Overview on each.

| Action | Source | NotebookLM |
|--------|--------|------------|
| UPLOAD | _output/mentor/pillars/en/audio_source.md | notebook: "12 Pillars - Factory Lens" |
| UPLOAD | _output/mentor/nuclei/en/audio_source.md | notebook: "Nuclei - City Lens" |
| UPLOAD | _output/mentor/kinds/en/audio_source.md | notebook: "Kinds - Factory Lens" |
| UPLOAD | _output/mentor/gdp/en/audio_source.md | notebook: "GDP - Game Lens" |
| UPLOAD | _output/mentor/builder/en/audio_source.md | notebook: "Builder - Factory Lens" |
| UPLOAD | _output/mentor/dispatch/en/audio_source.md | notebook: "Dispatch - City Lens" |
| UPLOAD | _output/mentor/crews/en/audio_source.md | notebook: "Crews - Game Lens" |
| UPLOAD | _output/mentor/signals/en/audio_source.md | notebook: "Signals - Biology Lens" |
| UPLOAD | _output/mentor/memory/en/audio_source.md | notebook: "Memory - Biology Lens" |
| UPLOAD | _output/mentor/sin_lens/en/audio_source.md | notebook: "Sin Lens - Game Lens" |

### Wave 5: PPTX Compilation (N05, 10 compilations)

```bash
npx @marp-team/marp-cli _output/mentor/{slug}/en/slides.md --pptx -o _output/mentor/{slug}/en/slides.pptx
npx @marp-team/marp-cli _output/mentor/{slug}/en/slides.md --pdf -o _output/mentor/{slug}/en/slides.pdf
```

## Decisions (from manifest)

- Execution: pipeline (cex_media_produce.py CLI, not crew)
- Batch: 3 concepts per wave, sequential
- Language: EN first (global launch priority)
- Quality: trust template, human review after Wave 1
- Catalog: _output/mentor/{concept}/{lang}/

## Dependencies

```
Wave 1 (N04: pillars, nuclei, kinds)
    |
Wave 2 (N04: gdp, builder, dispatch)
    |
Wave 3 (N04: crews, signals, memory, sin_lens)
    |
Wave 4 (N05: NotebookLM upload x10)
    |
Wave 5 (N05: PPTX/PDF compile x10)
```

Waves 1-3 are independent content generation (could run in parallel, but sequential
avoids git contention). Wave 4-5 depend on content existing.

## Done When

- [ ] All 30 content files exist in _output/mentor/
- [ ] All 10 PPTX files compiled
- [ ] All 10 NotebookLM notebooks created with Audio Overview triggered
- [ ] media_config.yaml updated with all notebook IDs
- [ ] Quality >= 9.0 on all scored artifacts
- [ ] Signal sent: n04 -> complete, n05 -> complete
