---
id: p11_qg_audio_tool
kind: quality_gate
pillar: P11
title: "Gate: audio_tool"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "audio processing tool — STT, TTS, and audio analysis with declared direction, models, formats, and language coverage"
quality: 9.0
tags: [quality-gate, audio-tool, P04, speech, stt, tts, direction, formats, languages]
tldr: "Pass/fail gate for audio_tool artifacts: direction declaration, model validity, format enum compliance, BCP-47 language codes, streaming declaration."
density_score: 0.91
llm_function: GOVERN
---
# Gate: audio_tool
## Definition
| Field | Value |
|---|---|
| metric | audio_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: audio_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_audio_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, missing prefix, or wrong namespace |
| H03 | ID equals filename stem | `id: p04_audio_stt` but file is `p04_audio_transcription.md` |
| H04 | Kind equals literal `audio_tool` | `kind: tool`, `kind: cli_tool`, or any non-audio_tool value |
| H05 | Quality field is null | `quality: 8.5` or any non-null value |
| H06 | All required fields present | Missing any of: direction, models, formats, languages, name, tldr |
| H07 | Direction is valid enum value | `direction: stt` or `direction: speech` — must be input/output/analysis/bidirectional |
| H08 | Models list is non-empty and uses exact provider identifiers | `models: [Whisper]` (marketing name) or `models: []` (empty) |
| H09 | Formats list uses only allowed enum values | `formats: [audio/mpeg]` (MIME type) or `formats: [mp4]` (video format) |
| H10 | Languages use BCP-47 codes | `languages: [English]` or `languages: [Brazilian Portuguese]` — must be en, pt-BR, etc. |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Direction clarity | 1.0 | Direction declared + processing flow described in ## Direction section |
| Model documentation | 1.0 | Each model has provider, accuracy tier, latency class, cost tier in ## Models table |
| Format compatibility | 1.0 | ## Formats section shows input/output matrix; formats match frontmatter list |
| Language coverage | 1.0 | ## Languages section lists BCP-47 codes with quality tier per model |
| Streaming declaration | 0.5 | streaming: true/false declared; if true, streaming protocol described |
| Sample rate specificity | 0.5 | sample_rate declared with Hz value apownte to direction |
| Max duration declared | 0.5 | max_duration (seconds) declared; affects caller integration |
| Word timestamps (STT) | 0.5 | word_timestamps declared for direction: input tools |
| Voice identity (TTS) | 0.5 | voice_id declared for direction: output tools |
| Provider boundary | 1.0 | Tool is NOT vision_tool (image/video), NOT notifier (delivery), NOT cli_tool (terminal) |
| Model-format alignment | 1.0 | Formats declared match what listed models actually accept/produce |
| tldr density | 0.5 | tldr <= 160ch, includes direction + model count + key capability |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal prototype tool used only during provider evaluation, never shipped |
| approver | Author self-certification with comment explaining prototype-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — prototype tools must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML), H05 (self-scored quality), H07 (invalid direction) |
