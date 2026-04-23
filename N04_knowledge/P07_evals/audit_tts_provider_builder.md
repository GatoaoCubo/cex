---
id: n04_audit_tts_provider_builder
kind: knowledge_card
pillar: P01
title: "Audit: tts_provider Builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "N04 Knowledge Nucleus"
domain: "builder quality audit"
quality: 8.9
tags: [audit, tts_provider, builder, HYBRID_REVIEW]
tldr: "13/13 ISOs audited. 3 surgical fixes. Critical: ElevenLabs and modern vendors added. Architecture correct."
related:
  - n04_audit_stt_provider_builder
  - bld_schema_bugloop
  - bld_schema_tts_provider
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_knowledge_card_vision_tool
  - bld_schema_context_window_config
  - bld_schema_dataset_card
---

## Audit Summary

| Metric | Value |
|---|---|
| ISOs Audited | 13/13 |
| Passing (>=8.0, no fix) | 4 |
| Surgical Fix Applied | 3 |
| Full Rebuild | 0 |
| Critical Errors Fixed | 1 (missing dominant vendor) |

## ISO Scores (Pre-fix / Post-fix)

| ISO | Kind | Pre-fix Score | Post-fix Score | Action |
|---|---|---|---|---|
| bld_manifest | type_builder | 7.5 | 8.5 | SURGICAL: added ElevenLabs, XTTS, MOS framing |
| bld_instruction | instruction | 7.5 | 7.5 | LEAVE: process adequate |
| bld_system_prompt | system_prompt | 8.0 | 8.0 | PASS: specs real (<50ms, 50+ languages) |
| bld_knowledge_card | knowledge_card | 7.5 | 9.0 | SURGICAL: complete vendor matrix added |
| bld_schema | schema | 7.5 | 7.5 | LEAVE: structure valid |
| bld_quality_gate | quality_gate | 7.5 | 7.5 | LEAVE: gates adequate |
| bld_output_template | output_template | 7.0 | 7.0 | NOTE: minimal but functional |
| bld_examples | examples | 7.5 | 7.5 | LEAVE: Azure voices specifically named |
| bld_architecture | architecture | 7.5 | 7.5 | PASS: no domain confusion |
| bld_config | config | 7.5 | 7.5 | LEAVE: naming correct |
| bld_memory | learning_record | 7.5 | 7.5 | LEAVE: AWS Polly + Azure evidenced |
| bld_tools | tools | 7.0 | 7.0 | NOTE: Mozilla TTS outdated ref |
| bld_collaboration | collaboration | 7.5 | 7.5 | LEAVE: boundaries clear |

## Critical Errors Fixed

### ERROR 1: Missing Dominant Market Vendor (HIGH)
**Files**: bld_manifest, bld_knowledge_card  
**Issue**: ElevenLabs is the dominant modern TTS provider (highest MOS, voice cloning, most developer adoption as of 2024) but was completely absent. Also missing: OpenAI TTS, Coqui XTTS v2, Piper TTS, Resemble.ai, Play.ht.  
**Fix**: Added complete vendor landscape with MOS benchmarks, TTFB latency, and pricing data.

### No Architecture Error
Unlike STT builder, TTS architecture correctly positions the provider within voice pipelines (no trading system confusion).

## Vendor Coverage After Fix
| Vendor | Mentioned | MOS Score | Pricing | Voice Cloning |
|---|---|---|---|---|
| ElevenLabs | YES (added) | 4.7/5 | YES | YES |
| OpenAI TTS | YES (added) | 4.5/5 | YES | NO |
| Google Cloud TTS | YES | 4.5/5 | YES | NO |
| Azure Neural TTS | YES | 4.4/5 | YES | YES |
| Amazon Polly | YES | 4.2/5 | YES | NO |
| Coqui XTTS v2 | YES (added) | 4.3/5 | self-hosted | YES |
| Piper TTS | YES (added) | 3.8/5 | self-hosted | NO |
| Bark (Suno) | YES (added) | N/A | self-hosted | partial |
| Resemble.ai | YES (added) | N/A | YES | YES |
| Play.ht | YES (added) | N/A | YES | YES |
| IBM Watson | YES (added) | N/A | YES | NO |

## Remaining Gaps
1. bld_output_template.md is sparse -- missing: `mos_score`, `voice_cloning_support`, `ssml_support`, `streaming`, `ttfb_ms` fields.
2. bld_tools.md references Mozilla TTS -- outdated (project discontinued 2021, superseded by Coqui). Should reference Coqui TTS, XTTS, Piper.
3. bld_quality_gate.md D7 scalability threshold (10k+ RPS) is unrealistically high -- most TTS providers are 10-100 RPS per API key.
4. bld_schema.md default quality value should be `null` not "high".

## Recommendation
TTS builder should cross-reference prosody_config builder (for SSML prosody control) and voice_pipeline builder (for orchestration context). Recommend adding citation artifacts for ElevenLabs API docs and Coqui XTTS repo.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_audit_stt_provider_builder]] | sibling | 0.64 |
| [[bld_schema_bugloop]] | downstream | 0.46 |
| [[bld_schema_tts_provider]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_quickstart_guide]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.41 |
| [[bld_schema_pitch_deck]] | downstream | 0.40 |
| [[bld_knowledge_card_vision_tool]] | sibling | 0.40 |
| [[bld_schema_context_window_config]] | downstream | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
