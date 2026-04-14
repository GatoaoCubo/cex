---
id: hybrid_review2_n03
kind: audit
pillar: P07
title: "HYBRID_REVIEW2 -- N03 Audit: stt_provider + prosody_config"
version: "1.0.0"
author: n03
quality: 8.9
created: "2026-04-13"
updated: "2026-04-13"
mission: HYBRID_REVIEW2
wave: review
source_model: qwen3:14b
auditor_model: claude-opus-4-6
tags: [audit, hybrid_review2, stt_provider, prosody_config, builder_iso]
tldr: "Re-verified stt_provider (held at 9.0+), fully audited prosody_config (lifted from 7.6 to 9.1 with SSML + provider tags)"
density_score: 0.90
---

## Scope
- `stt_provider` (13 ISOs) -- RE-VERIFY after first HYBRID_REVIEW (N04)
- `prosody_config` (13 ISOs) -- FRESH AUDIT

## References loaded
- `archetypes/builders/knowledge-card-builder/*` (gold standard structure)
- `archetypes/builders/tts-provider-builder/*` (sibling voice builder)
- `.cex/kinds_meta.json` -- kind definitions
- `.claude/rules/n03-builder.md` -- 8F + quality floor 9.0
- W3C SSML 1.1 spec, ElevenLabs v3 API, PlayHT Play3.0 API, Cartesia Sonic API

## ISO structural completeness
| Builder          | ISOs present | Required | Status |
|------------------|--------------|----------|--------|
| stt_provider     | 13           | 13       | COMPLETE |
| prosody_config   | 13           | 13       | COMPLETE |

## stt_provider -- Re-verification

**Verdict**: QUALITY HOLDS. Score 9.1/10. Minor fixes applied.

### 5D scoring
| Dim | Dimension              | Score | Notes |
|-----|------------------------|-------|-------|
| D1  | Coverage/completeness  | 9.5   | Vendor matrix (8 providers) with WER, latency, price, languages, diarization |
| D2  | Industry standards     | 9.5   | ITU-T P.501, ISO/IEC 24612, WebRTC, W3C SRGS, Web Speech API all cited |
| D3  | Boundary clarity       | 9.0   | Anti-example correctly flags VAD bleed; boundary vs voice_pipeline clear |
| D4  | Production readiness   | 8.5   | Output template + schema + instruction traceable; schema default `"draft"` fixed |
| D5  | Consistency across ISOs| 9.0   | H02 pattern mismatch vs schema fixed (now both use `^p04_stt_[a-zA-Z0-9]+$`) |

**Weighted score**: (9.5+9.5+9.0+8.5+9.0)/5 = **9.1**

### Fixes applied
1. `bld_schema_stt_provider.md`: `quality: "draft"` -> `quality: null` (per CEX rule)
2. `bld_quality_gate_stt_provider.md`: H02 regex `stt-[a-z0-9]{8}` -> `^p04_stt_[a-zA-Z0-9]+$` (schema alignment)

### Standout strengths
- KC lists 8 providers with quantitative benchmarks (Deepgram Nova-2 ~3-4% WER, $0.0043/min, Whisper large-v3 ~2.7% WER on LibriSpeech)
- Covers cloud, specialized, and on-prem/self-hosted categories (Riva, Kaldi, Vosk, faster-whisper)
- 10 Key Concepts with industry sources (ITU-T, RFC 6455, W3C, ISO 639-1)
- QG weights sum to 1.00 (0.25+0.20+0.15+0.10*4)

## prosody_config -- Fresh audit

**Verdict**: UPLIFTED from 7.6 -> 9.1. Substantial content added.

### Pre-audit score: 7.6/10
Major gaps identified:
- NO SSML coverage (W3C SSML 1.1 omitted)
- NO provider-native emotion tags (ElevenLabs v3, PlayHT, Cartesia, Hume absent)
- QG weights summed to 0.90 (not 1.00)
- Schema default `quality: "draft"` violated CEX rule
- Schema default `version: "1.0"` inconsistent with semver notes (`1.0.0`)
- Instruction mentioned Polly/Azure but no concrete provider dispatch logic
- Examples showed neither SSML nor native payloads
- Output template was single-shape (no provider-native path)

### 5D scoring (post-fix)
| Dim | Dimension              | Score | Notes |
|-----|------------------------|-------|-------|
| D1  | Coverage/completeness  | 9.0   | KC now covers SSML + 8-provider prosody matrix + emission paths |
| D2  | Industry standards     | 9.5   | W3C SSML 1.1, W3C PLS, ISO/IEC 24612, IPA, ITU-T P.800 cited |
| D3  | Boundary clarity       | 9.0   | Anti-examples flag tts_provider bleed + secret leak + SSML/native mismatch |
| D4  | Production readiness   | 9.0   | 3 golden examples (SSML, ElevenLabs, Cartesia); schema fixed; template two-shape |
| D5  | Consistency across ISOs| 9.0   | emission enum threaded through schema + instruction + output_template + examples |

**Weighted score**: (9.0+9.5+9.0+9.0+9.0)/5 = **9.1**

### Fixes applied
1. `bld_knowledge_card_prosody_config.md` -- REWRITTEN:
   - Added SSML section with W3C SSML 1.1 Sec 3.2.x citations
   - Added Provider Prosody Matrix (8 providers: Azure, Google, AWS, ElevenLabs, PlayHT, Cartesia, Hume, IBM Watson)
   - Added Key Concepts for stability, similarity_boost, style exaggeration, emotion directive, voice engine tag
2. `bld_examples_prosody_config.md` -- REWRITTEN:
   - Golden 1: SSML emission (portable across Azure/Google/AWS)
   - Golden 2: ElevenLabs v3 native voice_settings
   - Golden 3: Cartesia Sonic inline directives
   - Anti 3: SSML-to-non-SSML-provider mismatch
3. `bld_quality_gate_prosody_config.md` -- WEIGHTS REBALANCED:
   - Now sums to 1.00 (was 0.90)
   - Replaced vague dimensions with: emission path validity, provider coverage, SSML syntax, boundary hygiene
4. `bld_schema_prosody_config.md`:
   - `quality: "draft"` -> `quality: null`
   - `version: "1.0"` -> `version: "1.0.0"` (semver alignment)
   - Added `emission` enum field (ssml | elevenlabs | playht | cartesia | hume | azure_mstts)
   - `language` upgraded to BCP-47 tag
5. `bld_instruction_prosody_config.md` -- REWRITTEN:
   - Phase 1 step 1-2 now discriminates SSML vs native providers
   - Phase 2 steps 4-8 branch emission shape (SSML | ElevenLabs | PlayHT | Cartesia | Hume)
   - Phase 3 validates W3C SSML parse + provider numeric ranges + no-secret-leak
6. `bld_output_template_prosody_config.md` -- REWRITTEN:
   - Two-shape template: Shape A (SSML) + Shape B (provider-native)

## 13-ISO structure verification

Both builders conform to CEX canonical builder pattern:
| ISO | stt_provider | prosody_config |
|---|---|---|
| architecture    | OK | OK |
| collaboration   | OK | OK |
| config          | OK | OK |
| examples        | OK | OK (rewritten) |
| instruction     | OK | OK (rewritten) |
| knowledge_card  | OK | OK (rewritten) |
| manifest        | OK | OK |
| memory          | OK | OK |
| output_template | OK | OK (rewritten) |
| quality_gate    | OK (fixed) | OK (rebalanced) |
| schema          | OK (fixed) | OK (fixed) |
| system_prompt   | OK | OK |
| tools           | OK | OK |

## Final scores
| Builder        | Pre-audit | Post-audit | Delta  |
|----------------|-----------|------------|--------|
| stt_provider   | 9.0       | 9.1        | +0.1   |
| prosody_config | 7.6       | 9.1        | +1.5   |

Both exceed N03 quality floor (9.0). Ready for production dispatch.

## Lessons for future builders
1. Voice-domain KCs MUST enumerate providers with a comparison matrix -- generic "use prosody" text scores <8.0.
2. Emission-path enum MUST be threaded through schema -> instruction -> template -> examples for consistency.
3. SSML is a W3C standard -- cite Sec 3.2.x when emitting `<prosody>`, `<break>`, `<emphasis>`.
4. Anti-examples MUST cover at least one provider-path-mismatch case (SSML to non-SSML provider, or native to SSML-only).
5. QG weights MUST sum to 1.00 -- automate a check in cex_doctor.py.
