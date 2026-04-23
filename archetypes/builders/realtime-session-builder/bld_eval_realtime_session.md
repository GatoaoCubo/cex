---
kind: quality_gate
id: p04_qg_realtime_session
pillar: P11
llm_function: GOVERN
purpose: Quality gate (HARD + SOFT) for realtime_session artifacts
quality: 9.1
title: "Quality Gate Realtime Session"
version: "1.1.0"
author: n03_rewrite
tags: [realtime_session, builder, quality_gate, vad, barge_in, latency]
tldr: "Gates specific to LLM realtime sessions: provider/model pair, VAD, barge-in handler, ephemeral auth, latency budget."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_realtime_session
  - bld_instruction_realtime_session
  - p03_sp_realtime_session_builder
  - bld_output_template_realtime_session
  - bld_schema_realtime_session
  - bld_knowledge_card_realtime_session
  - p10_mem_realtime_session_builder
  - realtime-session-builder
  - audit_realtime_session_builder
  - bld_tools_realtime_session
---

## Quality Gate
## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| HARD gates passed | 10/10 | equals | per artifact |
| SOFT score | >= 8.0 | gte | per artifact |
| Publish floor | 9.0 | gte | peer-reviewed |

## HARD Gates (blocking)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Parse error or missing required field |
| H02 | ID pattern | Does not match `^p04_rs_[a-z0-9_]{3,48}\.md$` |
| H03 | kind | `kind != realtime_session` |
| H04 | Provider / model pair | `provider` absent, or `model` is generic (e.g. `gpt-4o` not `gpt-4o-realtime-preview-*`) |
| H05 | Transport declared | `transport` not in `{webrtc, websocket, grpc_bidi}` |
| H06 | Codec-transport match | `webrtc` with non-{opus, pcm16}, or `websocket` with non-{pcm16, g711_ulaw} |
| H07 | Turn detection specified | `turn_detection.type` missing or not in `{server_vad, semantic_vad, none}` |
| H08 | Interruption policy | No barge-in handler documented (`input_audio_buffer.speech_started` -> `response.cancel`) |
| H09 | Ephemeral auth | Raw API key present in body, or no mint endpoint described |
| H10 | Latency budget table | Missing, or no target for "first audio delta after speech_stopped" |

## SOFT Scoring (0.0-1.0 per dim, weighted)
| Dim | Dimension | Weight | 1.0 | 0.5 | 0.0 |
|---|---|---|---|---|---|
| D1 | Density | 0.10 | >=0.88, no filler | 0.80-0.87 | <0.80 |
| D2 | Latency specificity | 0.15 | targets in ms + measurement method | targets only | qualitative |
| D3 | VAD config | 0.10 | threshold + padding + silence_ms set | partial | defaults/omitted |
| D4 | Barge-in robustness | 0.15 | cancel + flush + truncate | cancel only | not handled |
| D5 | Tool mid-stream spec | 0.10 | full event flow documented | partial | absent |
| D6 | Reconnect strategy | 0.10 | retries + backoff + state resume | retries only | absent |
| D7 | Event coverage | 0.10 | all 7 lifecycle events handled | 4-6 handled | <=3 |
| D8 | Auth hygiene | 0.10 | ephemeral token + TTL + server mint | ephemeral only | raw key |
| D9 | Observability | 0.05 | event log + PII redaction | event log only | absent |
| D10 | Provider fidelity | 0.05 | provider-pinned endpoints/fields | generic OK | mismatched |

Score = sum(weight_i * score_i) * 10.

## Actions
| Score | Action |
|---|---|
| >= 9.5 | GOLDEN: auto-approve, reference in KC |
| >= 9.0 | PUBLISH: ship as-is |
| 8.0-8.9 | REVIEW: peer fix of flagged dims |
| 7.0-7.9 | REWORK: back to F6 (max 2 retries) |
| < 7.0 | REJECT: rebuild from F2 |

## Bypass (documented only)
| Condition | Approver | Required artifact |
|---|---|---|
| Prototype / spike | N03 lead | `spike:true` tag + expiry date |
| Provider in preview (no fixed version) | N07 | Linked provider changelog URL |

## Examples
## Golden Example: OpenAI Realtime API via WebSocket
```yaml
---
kind: realtime_session
id: p04_rs_support_voicebot
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: websocket
version: "1.0.0"
created: 2026-04-13
updated: 2026-04-13
quality: null
tags: [realtime_session, openai, websocket, vad, support]
tldr: "Customer support voicebot: OpenAI Realtime WebSocket, server_vad, pcm16@24kHz, barge-in."
---
```

### Session Config
```json
{
  "model": "gpt-4o-realtime-preview-2024-12-17",
  "modalities": ["audio", "text"],
  "voice": "alloy",
  "instructions": "You are a customer support agent for Acme Corp. Be concise.",
  "input_audio_format": "pcm16",
  "output_audio_format": "pcm16",
  "input_audio_transcription": {"model": "whisper-1"},
  "turn_detection": {
    "type": "server_vad",
    "threshold": 0.5,
    "prefix_padding_ms": 300,
    "silence_duration_ms": 500
  },
  "tools": [],
  "tool_choice": "auto",
  "temperature": 0.8,
  "max_response_output_tokens": 1024
}
```

### Why it passes
- Provider + model pinned to realtime-capable version ✓
- Transport `websocket` paired with `pcm16` codec ✓
- `server_vad` with explicit threshold, padding, silence_ms ✓
- `quality: null` in frontmatter ✓
- ID matches `^p04_rs_[a-z0-9_]{3,48}\.md$` ✓

---

## Anti-Example 1: Generic model ID (H04 fail)
```yaml
---
kind: realtime_session
id: p04_rs_chat_agent
pillar: P04
provider: openai
model: gpt-4o
transport: websocket
quality: null
---
```

### Why it fails
`model: gpt-4o` is the chat-completion model. It does NOT support the Realtime API.
Must use `gpt-4o-realtime-preview-2024-12-17` or a pinned realtime-capable version.
**Gate**: H04 -- `model` must be a realtime-capable pinned version.

---

## Anti-Example 2: Missing VAD and barge-in (H07 + H08 fail)
```yaml
---
kind: realtime_session
id: p04_rs_demo
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: websocket
quality: null
---
```

```json
{
  "model": "gpt-4o-realtime-preview-2024-12-17",
  "modalities": ["audio"],
  "voice": "alloy"
}
```

### Why it fails
No `turn_detection` field -> H07 FAIL. No interruption policy -> H08 FAIL.
Without VAD, the server never knows when the user stopped speaking.
Without barge-in handling, the model keeps speaking over the user.

---

## Anti-Example 3: Raw API key exposed (H09 fail)
```yaml
---
kind: realtime_session
id: p04_rs_insecure
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: webrtc
quality: null
---
```

```js
const pc = new RTCPeerConnection();
// WRONG: api_key shipped to browser
const ws = new WebSocket("wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview",
  ["realtime", `openai-insecure-api-key-${process.env.OPENAI_API_KEY}`]);
```

### Why it fails
Raw `OPENAI_API_KEY` is exposed in the browser. **Gate**: H09 -- API key MUST NOT appear
in artifact. Instead: mint ephemeral token server-side via `POST /v1/realtime/sessions`
(60s TTL), pass `client_secret.value` to browser only.

## Properties
| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | realtime_session construction |
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
