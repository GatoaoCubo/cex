---
id: n02_audit_voice_pipeline_builder
kind: audit_report
pillar: P07
nucleus: n02
mission: HYBRID_REVIEW
kind_audited: voice_pipeline
wave: review
created: "2026-04-13"
author: n02_reviewer
quality: 8.7
---

# Audit: voice-pipeline-builder (13 ISOs)

## Summary

| ISO | Pre-Fix Score | Post-Fix Score | Action |
|-----|--------------|----------------|--------|
| bld_manifest | 6.5 | 8.5 | Fixed: +keywords, +Properties, updated author/density |
| bld_instruction | 6.5 | 8.5 | Fixed: removed ASCII violations (✅), updated Phase 3 gates, +Properties |
| bld_system_prompt | 7.0 | 9.0 | Fixed: INJECT->BECOME, ALWAYS/NEVER structure, +Properties |
| bld_quality_gate | 6.0 | 9.0 | REBUILT: replaced deployment performance gates with artifact quality gates |
| bld_output_template | 6.0 | 6.5 | Minimal (has {{vars}} structure, domain fields still generic) |
| bld_schema | 7.5 | 8.5 | Fixed: quality "draft"->null, +Properties |
| bld_knowledge_card | 8.5 | 9.0 | Fixed: +Properties (content was excellent, strongest of 4 kinds) |
| bld_architecture | 6.0 | 8.0 | Fixed: CEX-accurate Architectural Position, +Properties |
| bld_collaboration | 6.5 | 8.0 | Fixed: CEX builder names in Boundary (stt_provider/tts_provider/realtime_session), +Properties |
| bld_config | 6.5 | 7.5 | Fixed: +Properties |
| bld_memory | 4.5 | 9.0 | REBUILT: wrong kind (learning_record->memory), full rewrite |
| bld_tools | 4.5 | 9.0 | REBUILT: wrong tools (val_*.py->brain_query+FS+CEX tools) |
| bld_examples | 8.0 | 8.5 | Fixed: +Properties (examples were strong with good provider abstraction lesson) |

## Issues Found

### Critical (Score < 6.0 -- Rebuilt)
1. **bld_quality_gate**: Hard gates tested deployment readiness (missing `components` runtime field,
   security encryption in pipeline, concurrent user handling) -- not artifact structure.
   Also the quality_gate ID was `p04_qg_voice_pipeline` but should be `p11_qg_voice_pipeline`
   (quality gates belong to P11, not P04).
2. **bld_memory**: Wrong kind (`learning_record`). Missing memory-specific structure.
3. **bld_tools**: Referenced TensorFlow, PyAudio, Sphinx -- domain implementation tools, not CEX
   production tools. Used imaginary `val_test.py`, `val_compare.py`.

### Significant (Score 6-7 -- Fixed)
4. **bld_system_prompt**: `llm_function: INJECT` should be `BECOME`. Missing ALWAYS/NEVER.
5. **bld_instruction**: ASCII violations (`✅` emoji, `>=` as Unicode `>=`). Phase 3 tested WER and
   MOS scores -- runtime tests, not artifact structure validation.
6. **bld_manifest**: Missing `keywords`, density_score was template default.

### Minor (Properties missing -- Fixed)
7. All 13 ISOs missing `## Properties` table.
8. Schema `quality: "draft"` should be null.

## Strengths (voice_pipeline had best domain content of all 4 kinds)
- knowledge_card: Exceptional -- covered audio preprocessing, STT/NLU/TTS/dialogue management
  concepts with precise sources (W3C, ISO 23850, Amazon Polly, Interspeech)
- examples: Provider lock-in anti-example was precisely the most important lesson for voice pipelines
- manifest capabilities: Correctly covered GDPR/HIPAA compliance and provider abstraction

## Quality Distribution (Post-Fix)

| Tier | Count | ISOs |
|------|-------|------|
| 9.0+ | 4 | quality_gate, memory, tools, knowledge_card |
| 8.0-8.9 | 6 | manifest, instruction, system_prompt, schema, architecture, collaboration |
| 7.0-7.9 | 3 | output_template, config, examples |
| < 7.0 | 0 | -- |
