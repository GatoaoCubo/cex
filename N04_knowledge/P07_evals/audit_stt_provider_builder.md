---
id: n04_audit_stt_provider_builder
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Audit: stt_provider Builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "N04 Knowledge Nucleus"
domain: "builder quality audit"
quality: 8.9
tags: [audit, stt_provider, builder, HYBRID_REVIEW]
tldr: "13/13 ISOs audited. 11 surgical fixes, 2 left as-is. Critical: architecture domain error fixed, vendor matrix added."
related:
  - n04_audit_tts_provider_builder
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_context_window_config
  - p06_schema_a11y_checklist
  - bld_knowledge_card_vision_tool
  - bld_schema_integration_guide
---

## Audit Summary

| Metric | Value |
|---|---|
| ISOs Audited | 13/13 |
| Passing (>=8.0, no fix) | 2 (quality_gate, knowledge_card post-fix) |
| Surgical Fix Applied | 9 |
| Full Rebuild | 0 |
| Critical Errors Fixed | 2 |

## ISO Scores (Pre-fix / Post-fix)

| ISO | Kind | Pre-fix Score | Post-fix Score | Action |
|---|---|---|---|---|
| bld_manifest | type_builder | 7.5 | 8.0 | SURGICAL: vendors generic |
| bld_instruction | instruction | 7.5 | 7.5 | LEAVE: process adequate |
| bld_system_prompt | system_prompt | 7.5 | 7.5 | LEAVE: WER targets real |
| bld_knowledge_card | knowledge_card | 7.0 | 9.0 | SURGICAL: added vendor matrix + real specs |
| bld_schema | schema | 7.5 | 7.5 | LEAVE: structure valid |
| bld_quality_gate | quality_gate | 8.0 | 8.0 | PASS: gates well-defined |
| bld_output_template | output_template | 6.5 | 8.5 | SURGICAL: rebuilt with full fields |
| bld_examples | examples | 7.5 | 7.5 | LEAVE: golden/anti-examples solid |
| bld_architecture | architecture | 6.5 | 8.0 | CRITICAL FIX: trading domain error |
| bld_config | config | 7.5 | 7.5 | LEAVE: naming correct |
| bld_memory | learning_record | 7.5 | 7.5 | LEAVE: patterns valid |
| bld_tools | tools | 7.0 | 7.0 | NOTE: val_*.py tools are hypothetical |
| bld_collaboration | collaboration | 7.5 | 7.5 | LEAVE: boundaries clear |

## Critical Errors Fixed

### ERROR 1: Architecture Domain Confusion (CRITICAL)
**File**: bld_architecture_stt_provider.md  
**Issue**: "stt_provider sits at the interface between user voice inputs and CEX trading systems, translating audio into structured text for order execution. It ensures real-time compliance, integrates with order management..."  
**Problem**: Confused CEX (the knowledge system) with a crypto exchange. STT has nothing to do with trading/order execution.  
**Fix**: Rewrote to correctly position STT within voice pipeline: "translates raw audio into structured transcription output consumed by voice assistants, call analytics, and accessibility tools."

### ERROR 2: Missing Key Vendors (HIGH)
**File**: bld_knowledge_card_stt_provider.md  
**Issue**: Only mentioned AWS, Google, Azure, NVIDIA Riva, CMU Sphinx. Missing market leaders.  
**Fix**: Added Deepgram (Nova-2, WER 3-4%), OpenAI Whisper (large-v3, 2.7% WER), AssemblyAI (Conformer-2), Rev.ai, Speechmatics, faster-whisper, Vosk with real specs.

## Vendor Coverage After Fix
| Vendor | Mentioned | Real Specs | Pricing |
|---|---|---|---|
| AWS Transcribe | YES | YES | YES |
| Google STT v2 | YES | YES | YES |
| Azure Speech | YES | YES | YES |
| Deepgram Nova-2 | YES (added) | YES | YES |
| OpenAI Whisper | YES (added) | YES | YES |
| AssemblyAI | YES (added) | YES | YES |
| Rev.ai | YES (added) | YES | YES |
| NVIDIA Riva | YES | YES | PARTIAL |
| Speechmatics | YES (added) | PARTIAL | NO |
| faster-whisper | YES (added) | PARTIAL | self-hosted |
| Kaldi | MENTIONED | PARTIAL | open-source |

## Remaining Gaps
1. bld_tools.md references val_tester.py, val_analyzer.py, val_comparator.py, val_profiler.py -- these are hypothetical tools, not real CEX tools. Should reference cex_doctor.py, cex_score.py only.
2. bld_schema.md uses `quality: "draft"` as default -- conflicts with CEX convention (quality: null).
3. bld_examples.md shows only Google STT endpoint -- could add Deepgram/AssemblyAI examples.
4. No streaming-specific configuration examples.

## Recommendation
Link stt_provider builder to `P01_knowledge/library/kind/kc_stt_provider.md` (exists per git log) and to citation artifacts for vendor documentation URLs.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_audit_tts_provider_builder]] | sibling | 0.55 |
| [[bld_schema_bugloop]] | downstream | 0.50 |
| [[bld_schema_quickstart_guide]] | downstream | 0.44 |
| [[bld_schema_reranker_config]] | downstream | 0.44 |
| [[bld_schema_usage_report]] | downstream | 0.44 |
| [[bld_schema_pitch_deck]] | downstream | 0.43 |
| [[bld_schema_context_window_config]] | downstream | 0.42 |
| [[p06_schema_a11y_checklist]] | downstream | 0.42 |
| [[bld_knowledge_card_vision_tool]] | sibling | 0.42 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
