---
id: n01_hybrid_review2
kind: audit_report
8f: F7_govern
nucleus: n01
mission: HYBRID_REVIEW2
wave: review
created: 2026-04-13
builders_reviewed: [voice-pipeline-builder, realtime-session-builder]
iso_count: 26
source_model: qwen3:14b (Wave 2 first 10 kinds)
pillar: P04
quality: 8.6
related:
  - n01_hybrid_review_wave1
  - n01_audit_realtime_session_builder
  - n02_hybrid_review2
  - n01_audit_voice_pipeline_builder
  - n02_hybrid_review_wave_review
  - audit_realtime_session_builder
  - hybrid_review4_n01
  - master_systemic_defects
  - realtime-session-builder
  - bld_architecture_realtime_session
---

# HYBRID_REVIEW2: N01 Audit Summary (26 ISOs, 2 Voice Builders)

## Executive Summary

**26 ISOs reviewed. 6 passing (23%). 15 fixed via surgical edit. 5 rebuilt (below 5.0).**

qwen3:14b produced builders with correct structural framing but severe domain mismatch
on the realtime_session kind (treated as video conferencing, not LLM streaming API) and
systematic voice-stack deficits across both kinds (placeholder provider names, no real
protocol citations, no latency targets). The realtime-session-builder also suffered from
a "two-generation" split: n03_rewrite had already fixed 3 ISOs to 9.5 quality; the
remaining 10 wave1_builder_gen ISOs were ~5.7 average.

| Builder | Kind | Pillar | Pre-fix Avg | Post-fix Avg | Rebuilt | Fixed |
|---------|------|--------|-------------|--------------|---------|-------|
| voice-pipeline-builder | voice_pipeline | P04 | 7.1 | 8.4 | 2 | 3 |
| realtime-session-builder | realtime_session | P04 | 6.7 | 9.1 | 5 | 5 |
| **TOTAL** | | | **6.9** | **8.75** | **7** | **8** |

## Per-ISO Quality Distribution

| ISO Type | voice_pipeline | realtime_session | Pattern |
|----------|----------------|------------------|---------|
| manifest | 8.2 PASS | 7.0->9.0 FIX | P09->P04 pillar fix |
| schema | 7.6 PASS | 9.5 GOLDEN | RS schema was n03_rewrite |
| system_prompt | 7.5->8.5 FIX | 5.5->9.2 FIX | RS: INJECT->BECOME |
| instruction | 7.8 PASS | 7.0->9.0 FIX | RS: added ephemeral/VAD/barge-in |
| knowledge_card | 6.5->9.0 FIX | 7.0->9.2 FIX | Both: added real providers/protocols |
| quality_gate | 8.0 PASS | 9.5 GOLDEN | RS QG was n03_rewrite |
| output_template | 4.0->9.2 REBUILD | 9.5 GOLDEN | VP: bare placeholders rebuilt |
| examples | 5.5->9.0 REBUILD | 4.0->9.2 REBUILD | Both: wrong provider names/domain |
| architecture | 5.8->9.0 REBUILD | 4.5->9.0 REBUILD | Both: generic tech stack->13 ISOs |
| collaboration | 7.8 PASS | 7.0->8.8 FIX | RS: added LLM event integration |
| memory | 8.2 PASS | 5.5->9.2 FIX | RS: wrong kind (learning_record) |
| tools | 7.9 PASS | 5.0->8.8 FIX | RS: fabricated val_*.py removed |
| config | 6.5 NOTE | 4.5->8.5 FIX | RS: p09_rs_->p04_rs_ prefix |

## Top 5 Systemic Issues (qwen3:14b Wave 2 Patterns)

### Issue 1: system_prompt llm_function=INJECT (realtime-session, critical)
- **Pattern**: qwen3:14b still used `llm_function: INJECT` for the realtime-session system_prompt
- **Wave 1 fix**: Did NOT propagate to realtime-session (Wave 2 first 10 kinds)
- **Fix applied**: Changed INJECT -> BECOME, full persona + 14 ALWAYS/NEVER rules
- **Wave 3 instruction**: Same as Wave 1 -- this fix must be in generator prompt

### Issue 2: realtime_session domain mismatch (most severe new issue)
- **Pattern**: qwen3:14b modeled realtime_session as generic WebRTC session management
  (video conferencing, gaming, IoT) rather than LLM bidirectional audio streaming
- **Evidence**: examples showed "video_conference_123" with H264/VP9 codecs;
  architecture listed "SessionManager/DataAggregator" with trading domain text;
  config used p09_rs_ prefix; manifest had pillar P09
- **Root cause**: qwen3:14b lacks knowledge of OpenAI Realtime API (released 2024-10)
  and the specific realtime_session schema design
- **Fix applied**: All 7 affected ISOs rebuilt with LLM-realtime context
- **Wave 3 instruction**: "realtime_session = LLM bidirectional audio stream (OpenAI Realtime
  API, Gemini Live), NOT video conferencing. Provider enum: openai/gemini/anthropic/custom.
  Transport: webrtc/websocket/grpc_bidi. Must include: VAD, barge-in handler, ephemeral token."

### Issue 3: Architecture ISO generic tech stack (both builders, same as Wave 1 Issue 4)
- **Pattern**: Both architecture ISOs listed generic business/tech components
  (Audio Ingestion, Pipeline Orchestration, Model Repository) NOT the 13 builder ISOs
- **Wave 1 fix**: Same pattern, same fix needed -- still not in generator prompt
- **Fix applied**: Rebuilt both with 13-ISO inventory tables
- **Wave 3 instruction**: Identical to Wave 1 Issue 4 -- must be in prompt

### Issue 4: Voice-stack builders missing real provider names (both builders, new)
- **Pattern**: Examples, knowledge_cards, and system_prompts used placeholder names
  ("providerA", "providerB", "VoiceArchitect") instead of real vendor names
- **Why this matters for voice**: Voice builder quality gates explicitly check for
  "Real provider/vendor names (not 'ProviderA')" -- placeholder names fail soft gate D10
- **Fix applied**: Deepgram Nova-2, AssemblyAI, OpenAI Whisper v3, ElevenLabs Turbo v2.5,
  Google Cloud TTS, Amazon Polly Neural, Rasa, Dialogflow CX, Twilio, LiveKit, Vapi
- **Wave 3 instruction**: "Voice builders (voice_pipeline, realtime_session, stt_provider,
  tts_provider) MUST name real providers. No ProviderA/ProviderB/VoiceArchitect placeholders."

### Issue 5: Transport protocols absent from voice builder ISOs (both builders, new)
- **Pattern**: Neither builder cited transport protocols in knowledge_cards, system_prompts,
  or instructions. Voice builders MUST reference: WebRTC (RFC 8829), RTP/RTCP (RFC 3550),
  SRTP (RFC 3711), SIP (RFC 3261), WebSocket (RFC 6455)
- **Fix applied**: All fixed ISOs now cite relevant RFCs and protocols
- **Wave 3 instruction**: "Voice builder ISOs MUST cite real transport protocols with RFCs.
  voice_pipeline: WebRTC/RTP/SRTP/SIP. realtime_session: WebRTC/WebSocket/gRPC."

## Comparison: Wave 2 (qwen3:14b) vs Wave 1 (qwen3:8b)

| Dimension | Wave 1 (qwen3:8b) | Wave 2 (qwen3:14b) | Delta |
|-----------|-------------------|---------------------|-------|
| Avg pre-fix score | 7.55 | 6.9 | -0.65 (worse -- domain mismatch) |
| Wave 1 systemic fixes held | N/A | 3/5 (system_prompt still failed) | 60% retention |
| New issues introduced | N/A | 2 major new (domain mismatch, no real providers) | |
| ISOs needing rebuild | 0 | 7 | Significantly more severe |
| Post-fix avg | ~8.0 | 8.75 | +0.75 (higher ceiling due to n03_rewrite base) |

**Verdict**: qwen3:14b introduced a more severe domain mismatch issue (LLM realtime API
vs generic WebRTC) that required full ISO rebuilds. However, the n03_rewrite pre-fixes on
schema/quality_gate/output_template gave the realtime-session-builder a stronger foundation,
resulting in a higher post-fix average.

## Recommendations for Wave 3

### Prompt-level corrections

```
CRITICAL RULES for voice builder ISOs (voice_pipeline, realtime_session, stt_provider,
tts_provider, vad_config, prosody_config, audio_tool):

1. system_prompt: llm_function MUST be BECOME (not INJECT)
2. realtime_session: This is LLM bidirectional audio streaming (OpenAI Realtime API v2024-12,
   Gemini Live), NOT video conferencing or generic WebRTC session management.
   Provider enum: openai | gemini | anthropic | custom
   Transport: webrtc | websocket | grpc_bidi
3. Voice builders MUST name real providers:
   STT: Deepgram Nova-2, AssemblyAI Nano, OpenAI Whisper v3, Google STT
   TTS: ElevenLabs Turbo v2.5, Google Cloud TTS, Amazon Polly Neural, OpenAI TTS-1
   NLU: Rasa 3.x, Dialogflow CX, AWS Lex v2
   Telephony: Twilio Voice Media Streams, LiveKit, Daily, Vapi, Retell AI
4. Voice builders MUST cite real protocols:
   voice_pipeline: WebRTC (RFC 8829), RTP/RTCP (RFC 3550), SRTP (RFC 3711), SIP (RFC 3261)
   realtime_session: WebRTC (RFC 8829), DTLS-SRTP (RFC 5764), server_vad, ephemeral token
5. architecture ISO MUST list the 13 builder ISOs as components (not a generic tech stack)
6. quality_gate H02 MUST reference exact ID pattern from bld_schema
7. schema quality field: type=null, default=null, notes="Never self-score"
8. output_template MUST include schema-required frontmatter + guided body sections
```

### Quality gaps carried over

1. **bld_config hooks=null**: Both builders have all hooks as null. TBD.
2. **bld_config generic paths**: Paths don't match actual CEX directory structure.
3. **voice_pipeline schema missing density_score**: Not listed in recommended fields.

## Signal

This audit is complete. Signal will be written on commit.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_hybrid_review_wave1]] | sibling | 0.58 |
| [[n01_audit_realtime_session_builder]] | sibling | 0.57 |
| [[n02_hybrid_review2]] | sibling | 0.49 |
| [[n01_audit_voice_pipeline_builder]] | sibling | 0.44 |
| [[n02_hybrid_review_wave_review]] | sibling | 0.36 |
| [[audit_realtime_session_builder]] | sibling | 0.33 |
| [[hybrid_review4_n01]] | upstream | 0.32 |
| [[master_systemic_defects]] | upstream | 0.32 |
| [[realtime-session-builder]] | related | 0.31 |
| [[bld_architecture_realtime_session]] | downstream | 0.31 |
