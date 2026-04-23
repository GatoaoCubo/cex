---
kind: quality_gate
id: p11_qg_voice_pipeline
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for voice_pipeline artifacts
quality: 9.1
title: "Quality Gate: Voice Pipeline"
version: "1.0.0"
author: n02_reviewer
tags: [voice_pipeline, builder, quality_gate, P11]
tldr: "Quality gate for voice pipeline architecture artifacts defining STT/NLU/TTS components, flow, and error handling."
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p03_sp_voice_pipeline_builder
  - bld_examples_voice_pipeline
  - bld_memory_voice_pipeline
  - p11_qg_quality_gate
  - p11_qg_collaboration_pattern
  - p11_qg_action_paradigm
  - p11_qg_thinking_config
  - p11_qg_response_format
  - p11_qg_prompt_template
  - bld_output_template_voice_pipeline
---

## Quality Gate
## Definition
A `voice_pipeline` artifact defines the end-to-end architecture for voice agent processing:
STT, NLU, dialogue management, TTS components, their data flows, and error recovery strategies.
It describes system-level architecture -- NOT provider-specific tuning or implementation code.

Scope: files with `kind: voice_pipeline`. Does NOT apply to stt_provider (single STT config),
tts_provider (single TTS config), or realtime_session (live session state).

## HARD Gates
Failure on any single gate means REJECT regardless of soft score.

| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p04_vp_*` | `id.startswith("p04_vp_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `voice_pipeline` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | At least 2 pipeline components declared (STT and TTS minimum) | component list has >= 2 entries |
| H08 | Data flow direction declared between components | body defines input/output or flow between stages |

## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.

| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | All 4 core stages present: STT, NLU, dialogue management, TTS | 1.0 |
| 3  | Fallback and error recovery mechanisms documented | 1.0 |
| 4  | Multi-provider or provider-agnostic design declared | 1.0 |
| 5  | Latency budget or performance targets specified | 0.5 |
| 6  | Audio preprocessing stage documented | 0.5 |
| 7  | Tags include `voice_pipeline` | 0.5 |
| 8  | Boundary note: distinguishes from stt_provider, tts_provider, and realtime_session | 1.0 |
| 9  | At least one concrete domain use case or deployment scenario | 1.0 |
| 10 | Privacy/compliance requirements referenced (GDPR, HIPAA) | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |

**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Score range: 0.0 to 10.0.

## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool; add to curated pipeline library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required |

## Bypass
| Field | Value |
|-------|-------|
| condition | Pipeline is a proof-of-concept with documented lifespan under 30 days |
| approver | Domain lead must approve in writing |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, reason |
| expiry | 30 days from bypass grant; pipeline must be retired or brought to full compliance |

## Properties
| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P11 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Examples
## Golden Example: Contact Center Voice Pipeline
```yaml
---
kind: voice_pipeline
id: p04_vp_contact_center_en
pillar: P04
title: "Contact Center Voice Pipeline (English)"
version: "1.0.0"
created: 2026-04-13
updated: 2026-04-13
author: n03_builder
domain: "customer support"
language: en
sample_rate: 16000
quality: null
tags: [voice_pipeline, customer_support, deepgram, rasa, elevenlabs]
tldr: "5-stage English contact center pipeline: RNNoise+VAD preprocessing, Deepgram Nova-2 STT, Rasa NLU, LangChain DM, ElevenLabs TTS."
---
```

### Pipeline Stages
| Stage | Provider | Input | Output |
|-------|----------|-------|--------|
| Audio Preprocessing | RNNoise + WebRTC VAD | Raw PCM 16kHz | Cleaned PCM 16kHz |
| STT | Deepgram Nova-2 (WebSocket streaming) | Cleaned PCM | JSON transcript |
| NLU | Rasa Open Source 3.x | Transcript text | Intent + entities |
| Dialogue Management | LangChain + GPT-4o | Intent + session history | Response text |
| TTS | ElevenLabs Turbo v2.5 (streaming) | Response text | MP3/PCM audio stream |

### Why it passes
- All 5 stages present including audio preprocessing ✓
- Real provider names (Deepgram Nova-2, Rasa, ElevenLabs Turbo) ✓
- Provider abstraction: each stage uses interface, not hardcoded API ✓
- `quality: null` in frontmatter ✓
- ID matches `^p04_vp_[a-z0-9_]+$` ✓

---

## Anti-Example 1: Placeholder Provider Names
```yaml
---
kind: voice_pipeline
id: p04_vp_basic
pillar: P04
title: "Basic Voice Pipeline"
quality: null
---
components:
  - name: speech_recognition
    type: stt
    providers: [providerA, providerB]
  - name: text_to_speech
    type: tts
    providers: [providerX, providerY]
```

### Why it fails
`providerA`, `providerB`, `providerX`, `providerY` are placeholders.
They provide zero production guidance. Engineers cannot instantiate this pipeline.
Must use real names: Deepgram Nova-2, AssemblyAI, OpenAI Whisper for STT;
ElevenLabs, Google Cloud TTS, Amazon Polly for TTS.

**Also fails**: Missing NLU, dialogue management, and audio preprocessing stages.

---

## Anti-Example 2: Missing Audio Preprocessing
```yaml
---
kind: voice_pipeline
id: p04_vp_no_preproc
pillar: P04
title: "Unprocessed Voice Pipeline"
quality: null
---
stages:
  - name: stt
    provider: deepgram_nova2
  - name: nlu
    provider: dialogflow_cx
  - name: tts
    provider: google_cloud_tts
```

### Why it fails
No audio preprocessing stage. In noisy environments (call center background noise,
mobile ambient sound), WER increases by 25-60% without preprocessing.
RNNoise or WebRTC VAD MUST precede STT. Also missing dialogue management stage.

---

## Anti-Example 3: Single-Provider, No Fallback
```yaml
---
kind: voice_pipeline
id: p04_vp_locked
pillar: P04
title: "Single-Provider Pipeline"
quality: null
---
stages:
  - name: stt
    provider: deepgram_nova2        # only provider, no fallback
  - name: nlu
    provider: dialogflow_cx         # only provider, no fallback
  - name: tts
    provider: elevenlabs_turbo      # only provider, no fallback
```

### Why it fails
No fallback chains defined. When Deepgram has an outage (avg 2-3x/year for any SaaS),
pipeline goes down completely. Recovery time: 15+ minutes mean (manual intervention).
With fallback to OpenAI Whisper v3: zero-downtime automatic failover.

## Properties
| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
