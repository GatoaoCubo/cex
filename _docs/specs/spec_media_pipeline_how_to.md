---
id: spec_media_pipeline_how_to
kind: context_doc
pillar: P01
nucleus: N04
title: "CEX Mentor Media Pipeline -- How To Run"
version: 1.0.0
created: 2026-04-19
author: n04_knowledge
domain: mentor_media
quality: 8.5
tags: [pipeline, media, mentor, how-to, notebooklm, marp, infoproduct]
density_score: 1.0
---

# CEX Mentor Media Pipeline -- How To Run

> Proven stack for producing 1 concept = text + audio_source + slides + PPTX + NotebookLM notebook

## Stack

| Component | Tool | Output |
|-----------|------|--------|
| Content generation | `cex_media_produce.py` | text.md, audio_source.md, slides.md |
| Slide compilation | Marp CLI | slides.pptx, slides.pdf |
| NotebookLM upload | `notebooklm_batch_upload.py` | notebook with audio overview |
| Catalog tracking | `notebooklm_mentor_notebooks.yaml` | notebook IDs + status |

## Prerequisites

```bash
# 1. Marp CLI available
npx @marp-team/marp-cli --version

# 2. Chrome running in remote debug mode (for NotebookLM CDP)
# See: boot/chrome_cdp.ps1

# 3. Python tools available
python _tools/cex_media_produce.py --help
python _tools/notebooklm_batch_upload.py --help

# 4. Lenses and teaching templates compiled
# Located in N04_knowledge/P01_knowledge/ and N04_knowledge/P03_prompt/
```

## Step 1: Generate Content

For each concept slug, run:

```bash
python _tools/cex_media_produce.py \
  --concept {slug} \
  --format all \
  --lens {lens} \
  --lang en
```

Output written to `_output/mentor/{slug}/en/`:
- `text.md` -- long-form narrative (~1500 words, storytelling-socratic hybrid)
- `audio_source.md` -- NotebookLM-optimized podcast script (~10-14K chars)
- `slides.md` -- Marp presentation (5-7 slides)

## Step 2: Compile Slides

```bash
cd _output/mentor/{slug}/en
npx @marp-team/marp-cli slides.md --pptx -o slides.pptx
npx @marp-team/marp-cli slides.md --pdf -o slides.pdf
```

## Step 3: Upload to NotebookLM

```bash
# Single concept
python _tools/notebooklm_batch_upload.py \
  --concept {slug} \
  --lang en \
  --source _output/mentor/{slug}/en/audio_source.md

# All 10 concepts (batch)
python _tools/notebooklm_batch_upload.py --batch all --lang en
```

After upload, notebook IDs are saved to `.cex/config/notebooklm_mentor_notebooks.yaml`.

## Step 4: Update Catalog

After adding a new concept:
1. Add row to `_output/mentor/index.md` asset table
2. Create `_output/mentor/{slug}/en/index.md` with notebook ID
3. Update `.cex/config/notebooklm_mentor_notebooks.yaml`
4. Commit: `git commit -m "[N04] media: add {slug} concept (EN)"`

## Concept Registry

All produced concepts tracked in `.cex/config/notebooklm_mentor_notebooks.yaml`.

Current concepts (10 mission + 1 legacy):

| Slug | Lens | Wave | Notebook |
|------|------|------|---------|
| 8f | factory | 0 (legacy) | 20fe93b2 |
| pillars | factory | 1 | c505dc47 |
| nuclei | city | 1 | 5adda4af |
| kinds | factory | 1 | ea616590 |
| gdp | game | 2 | 355e2fe8 |
| builder | factory | 2 | 7214b567 |
| dispatch | city | 2 | 5df722ca |
| crews | game | 3 | 9dc67209 |
| signals | biology | 3 | 35dbbd37 |
| memory | biology | 3 | e4d0d9e3 |
| sin_lens | game | 3 | 9e0e7a11 |

## Adding a New Concept

1. Add concept definition to `_docs/specs/spec_infoproduct_media_scale.md`
2. Run Step 1 (generate content)
3. Run Step 2 (compile slides)
4. Run Step 3 (upload to NotebookLM)
5. Run Step 4 (update catalog)

## Lens Guide

| Lens | Best for | Metaphor |
|------|----------|---------|
| factory | Systematic processes, pipelines, production | Assembly line, machine, gears |
| city | Distributed systems, agents, coordination | Districts, infrastructure, traffic |
| game | Strategic choices, protocols, decision points | Players, rules, moves, win conditions |
| biology | Memory, signals, evolution, adaptation | Neurons, DNA, immune system, growth |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Marp not found | `npm install -g @marp-team/marp-cli` |
| Chrome CDP refused | Run `boot/chrome_cdp.ps1` first, wait 10s |
| NotebookLM upload fails | Re-auth: `mcp__notebooklm__re_auth` |
| audio_source.md too long | Check `quality.audio_source_max_chars` in `media_config.yaml` |

## Config Files

| File | Purpose |
|------|---------|
| `N05_operations/P09_config/media_config.yaml` | Pipeline config (dirs, formats, tools) |
| `.cex/config/notebooklm_mentor_notebooks.yaml` | Notebook IDs per concept |
| `.cex/config/notebooklm_notebooks.yaml` | All notebooks (includes pre-mission) |
| `_output/mentor/index.md` | Master catalog |
