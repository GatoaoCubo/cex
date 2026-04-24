---
id: media_pipeline
kind: cli_tool
8f: F5_call
pillar: P04
title: "Media Production Pipeline"
version: 1.0.0
created: 2026-04-19
author: n05_operations
domain: media_production
quality: 8.7
tags: [cli_tool, media, mentor, notebooklm, marp, playwright, teaching]
tldr: "Orchestrates multi-format content production (text, audio, video, PPT) from CEX concepts via NotebookLM + Marp + Playwright."
density_score: 0.90
entry_point: _tools/cex_media_produce.py
runtime: python3
related:
  - p12_wf_notebooklm_pipeline
  - p01_kc_marp_cli
  - p01_kc_notebooklm_integration
  - p04_fn_cf_slides_generate
  - spec_notebooklm_pipeline
  - n04_output_cf_integration_kcs
  - wf_kc_to_content
  - bld_collaboration_audio_tool
  - spec_content_factory_v1
  - p03_ch_kc_to_notebooklm
updated: "2026-04-22"
---

## Purpose

`cex_media_produce.py` is the CLI entry point for the Mentor Didactic Engine's media
layer (Wave 4). It takes a CEX concept name, resolves its teaching content through
lens KCs and prompt templates, then produces output in one or more formats.

## Commands

| Subcommand | Description | Example |
|------------|-------------|---------|
| `text` | Render concept as long-form markdown via storyteller template | `--concept 8f --format text --lens factory --lang en` |
| `audio` | Generate NotebookLM source doc, upload, activate Audio Overview | `--concept 8f --format audio --lang en` |
| `video` | Generate NotebookLM source doc, activate Video Overview | `--concept 8f --format video --lang en` |
| `ppt` | Render Marp slide deck, compile to PPTX/PDF | `--concept 8f --format ppt --lens city --lang pt-br` |
| `all` | Produce all formats for a concept | `--concept 8f --format all --lang both` |

## CLI Interface

```
python _tools/cex_media_produce.py --concept <name> --format <fmt> [options]

Required:
  --concept <name>      CEX concept to produce (e.g., 8f, knowledge_card, nuclei)
  --format <fmt>        Output format: text|audio|video|ppt|all

Options:
  --lens <name>         Analogy lens: factory|city|biology|game (default: factory)
  --lang <code>         Language: en|pt-br|both (default: en)
  --output-dir <path>   Override output directory (default: _output/mentor/)
  --dry-run             Show what would be produced without executing
  --skip-upload         Skip NotebookLM upload (audio/video only)
  --config <path>       Override media_config.yaml path
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All formats produced successfully |
| 1 | Missing dependency (Marp, Playwright, NotebookLM auth) |
| 2 | Lens KC not found (Wave 1 not complete) |
| 3 | Template rendering failed |
| 4 | NotebookLM upload/studio activation failed |
| 5 | Marp compilation failed |

## Pipeline Flow

```
concept name
  |
  v
Resolve concept -> find lens KC + teaching template + locale voice
  |
  +--> TEXT: render storyteller template -> write markdown
  |
  +--> AUDIO: render notebooklm_source template -> upload via cex_notebooklm.py -> activate Audio Overview
  |
  +--> VIDEO: render notebooklm_source template -> upload -> activate Video Overview
  |
  +--> PPT: render ppt_generator template -> write .md -> marp-cli -> .pptx + .pdf
  |
  v
Output: _output/mentor/{concept}/{lang}/
  text.md | audio_source.md | slides.md | slides.pptx | slides.pdf
```

## Dependencies

| Dependency | Purpose | Install |
|------------|---------|---------|
| PyYAML | Config parsing | `pip install pyyaml` |
| cex_notebooklm.py | NotebookLM upload + studio | internal tool |
| @marp-team/marp-cli | Slide compilation | `npm install -g @marp-team/marp-cli` |
| Playwright (optional) | Browser automation for NotebookLM | `pip install playwright` |

## Config

Source: `N05_operations/P09_config/media_config.yaml`

Key fields: `output_dir`, `formats`, `languages`, `lenses` (paths to W1 KCs),
`teaching` (paths to W2 templates), `locales` (paths to W5 locale voices),
`marp` (CLI command + theme), `notebooklm` (tool path + domain prefix).

## Integration Points

| System | Interface | Direction |
|--------|-----------|-----------|
| /mentor produce | CLI dispatch | mentor skill calls this tool |
| cex_notebooklm.py | subprocess | audio/video format upload + studio |
| marp-cli | subprocess | ppt format compilation |
| W1 lens KCs | file read | concept-to-metaphor mappings |
| W2 teaching templates | file read | storyteller/socratic/journey prompts |
| W5 locale voices | file read | language-specific tone instructions |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_notebooklm_pipeline]] | downstream | 0.26 |
| [[p01_kc_marp_cli]] | upstream | 0.26 |
| [[p01_kc_notebooklm_integration]] | upstream | 0.26 |
| [[p04_fn_cf_slides_generate]] | related | 0.25 |
| [[spec_notebooklm_pipeline]] | downstream | 0.24 |
| [[n04_output_cf_integration_kcs]] | upstream | 0.24 |
| [[wf_kc_to_content]] | downstream | 0.23 |
| [[bld_collaboration_audio_tool]] | downstream | 0.21 |
| [[spec_content_factory_v1]] | downstream | 0.21 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.20 |
