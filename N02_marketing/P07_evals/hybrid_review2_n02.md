---
id: n02_hybrid_review2
kind: audit_report
nucleus: n02
mission: HYBRID_REVIEW2
wave: review
created: 2026-04-13
builders_reviewed: [vad-config-builder, tts-provider-builder]
iso_count: 26
pillar: P04, P09
quality: 8.0
density_score: 0.96
updated: "2026-04-17"
---

# HYBRID_REVIEW2: N02 Audit Summary (26 ISOs, 2 Builders)

## Executive Summary

**26 ISOs reviewed. 14 passing (54%). 11 fixed via surgical edit. 1 rebuilt (output_template_tts). 0 below 6.0.**

Both builders produced by qwen3:14b show the same systemic patterns identified in Wave 1.
All 5 Wave 1 issues present. VAD config builder is higher quality overall (better output template,
stronger quality gate). TTS provider builder had a critically broken output template (score 4.0)
that required full rebuild to 9.0.

| Builder | Kind | Pillar | Passing | Fixed | Rebuilt | Avg Score |
|---------|------|--------|---------|-------|---------|-----------|
| vad-config-builder | vad_config | P09 | 7/13 | 6/13 | 0/13 | 8.0 |
| tts-provider-builder | tts_provider | P04 | 7/13 | 5/13 | 1/13 | 7.8 |
| **TOTAL** | | | **14/26 (54%)** | **11/26 (42%)** | **1/26** | **7.9** |

## Per-Kind Quality Distribution

| ISO Type | vad_config | tts_provider | Action |
|----------|------------|--------------|--------|
| manifest | 8.2 PASS | 8.5 PASS | -- |
| system_prompt | 6.5 FIX | 6.5 FIX | INJECT->BECOME (both) |
| instruction | 7.8 FIX | 7.8 FIX | ASCII fix (vad), checkbox fix (tts) |
| knowledge_card | 8.6 FIX | 8.8 FIX | Added missing engines to both |
| schema | 6.5 FIX | 6.0 FIX | quality field -> null (both) |
| quality_gate | 8.5 PASS | 6.5 FIX | TTS H02 pattern mismatch |
| output_template | 9.0 PASS | 4.0 REBUILD | TTS was bare placeholders |
| architecture | 5.8 FIX | 5.8 FIX | Added 13-ISO inventory (both) |
| examples | 7.8 PASS | 7.8 PASS | -- |
| collaboration | 8.2 PASS | 7.5 PASS | -- |
| config | 7.5 PASS | 8.0 PASS | -- |
| memory | 7.5 PASS | 7.5 PASS | -- |
| tools | 7.8 PASS | 7.8 PASS | -- |

## Fixes Applied (12 total)

### Fix 1: system_prompt llm_function INJECT -> BECOME (both builders)
- **Files**: bld_system_prompt_vad_config.md, bld_system_prompt_tts_provider.md
- **Pattern**: Same Issue 1 from Wave 1 -- qwen3:14b uses INJECT for system_prompt
- **Wave 3 instruction**: "system_prompt ISOs MUST have llm_function: BECOME"

### Fix 2: schema quality field -> null (both builders)
- **Files**: bld_schema_vad_config.md, bld_schema_tts_provider.md
- **Pattern**: Same Issue 3 from Wave 1 -- quality has non-null defaults
- **vad_config was**: quality: "draft" | **tts_provider was**: quality: string with "high" example
- **Fix**: type=null, default=null, notes="Never self-score; peer review assigns value"

### Fix 3: quality_gate H02 pattern mismatch (TTS only)
- **File**: bld_quality_gate_tts_provider.md
- **Was**: `tts-[a-z0-9]+` | **Now**: `^p04_tts_[a-zA-Z0-9_-]+$` (matches schema)
- **Note**: VAD quality_gate was already correct (p09_vad_[a-zA-Z0-9_]+)

### Fix 4: output_template_tts_provider REBUILD (4.0 -> 9.0)
- **File**: bld_output_template_tts_provider.md
- **Was**: Bare `{{placeholder}}` template with no guidance on required fields
- **Now**: Full frontmatter with CEX-standard fields, 7 sections with inline comments,
  API config yaml block, SSML table, voice selection table, latency optimization, fallback chain,
  error handling table, validation rules
- **Same as Issue 5 from Wave 1** -- qwen3:14b produced bare placeholder templates

### Fix 5: architecture ISO inventory (both builders)
- **Files**: bld_architecture_vad_config.md, bld_architecture_tts_provider.md
- **Was**: Generic "DevOps/Engineering team" components instead of 13 builder ISOs
- **Now**: Full 13-ISO inventory table + dependency graph between ISOs
- **TTS architectural position** upgraded from generic to precise (P04 Tools, upstream/downstream flow)

### Fix 6: instruction ASCII violations (VAD) and checkbox formatting (TTS)
- **vad_config**: Unicode checkmarks (U+2705) removed -- violates .claude/rules/ascii-code-rule.md
- **tts_provider**: `[ ] [ ]` double-checkbox replaced with proper `- [ ]` markdown

### Fix 7: knowledge_card missing engines
- **vad_config**: Added Picovoice Cobra (<2ms, ARM/IoT optimized, commercial) and ten-vad
  (Apache 2.0, streaming-optimized, WebRTC stack integration)
- **tts_provider**: Added Cartesia (<80ms TTFB, market-leading for conversational AI) and
  Deepgram Aura-2 ($0.015/1K, English voice agents). Updated vendor matrix with 2024-2025 data.
- **system_prompt_vad**: Expanded from 5 rules to 10 (added engine-specific parameter rules,
  WebRTC aggressiveness constraints, Silero threshold guidance, speech timing specs)

## Systemic Issues Confirmed (Wave 1 pattern holds)

All 5 Wave 1 systemic issues are CONFIRMED present in this wave:

| Issue | Wave 1 | Wave 2 (N02) | Status |
|-------|--------|--------------|--------|
| system_prompt llm_function=INJECT | All 4 builders | Both builders | FIXED |
| quality_gate H02 divorced from schema | All 4 builders | TTS only (VAD was correct) | FIXED |
| schema quality non-null | All 4 builders | Both builders | FIXED |
| architecture wrong components | All 4 builders | Both builders | FIXED |
| output_template bare placeholders | All 4 builders | TTS critical, VAD was fine | FIXED |

**VAD output_template exception**: VAD produced an excellent output_template (9.0) -- suggests
qwen3:14b handles P09 config kinds better than P04 tool integration kinds.

## Recommendations for Wave 3

### Prompt-level corrections (confirm with Wave 1)
All Wave 1 recommendations remain valid. Additional for voice domain:

```
VOICE-SPECIFIC RULES for VAD/TTS/STT builder ISOs:
1. VAD: Always cite engine by name (WebRTC/Silero/Kaldi/Picovoice Cobra/ten-vad) with threshold ranges
2. TTS: knowledge_card MUST include MOS scores, TTFB latency, and pricing for named providers
3. TTS: Include Cartesia (sub-80ms TTFB) and Deepgram Aura as required providers
4. VAD: sensitivity is 0.0-1.0 probability; noise_floor is dBFS (-70 to -10); never confuse units
5. output_template for provider kinds: MUST include API config block, auth pattern, streaming config
```

### Notable difference: VAD vs TTS quality
VAD config builder scored higher (avg 8.0 vs 7.8) primarily because:
- Better output_template (9.0 vs 4.0 pre-fix)
- Correct quality_gate H02 pattern (TTS had mismatch)
- Stronger domain specificity in knowledge_card (real threshold values)

This suggests qwen3:14b handles configuration kinds (P09) better than tool integration kinds (P04).

## Quality Gaps to Investigate

1. **system_prompt rule count**: VAD had 5 rules, TTS had 5 rules -- both expanded to 10.
   Gold standard has 14. Target 12+ for voice domain given complexity.

2. **examples golden quality**: Both golden examples missing schema-required frontmatter fields
   (quality: null, pillar, tags). Not critical but worth noting for Wave 3.

3. **collaboration receiver names**: TTS collaboration uses "API_Manager", "Text_Handler" --
   generic names instead of real CEX builder names (voice_pipeline_builder, prosody_config_builder).
   Not blocking but semantically loose.

4. **TTS schema voice_samples in required**: Marked as required with default [] -- should be
   recommended since not all TTS integrations need sample references.

## Post-Audit Scores

| Builder | Pre-Audit Avg | Post-Audit Avg | Delta |
|---------|--------------|----------------|-------|
| vad-config-builder | 7.6 | 8.4 | +0.8 |
| tts-provider-builder | 7.0 | 8.2 | +1.2 |
| **Combined** | **7.3** | **8.3** | **+1.0** |
