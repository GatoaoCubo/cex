---
kind: output_template
id: bld_output_template_tts_provider
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for tts_provider production
quality: 9.1
title: "Output Template Tts Provider"
version: "1.1.0"
author: wave2_review
tags: [tts_provider, builder, output_template]
tldr: "Template with vars for tts_provider production"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

```yaml
---
id: p04_tts_{{name}}
kind: tts_provider
pillar: P04
title: "{{title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [tts_provider, {{provider_slug}}, voice_synthesis]
tldr: "TTS provider config for {{provider_name}} -- {{use_case}}"
supported_languages: {{language_list}}
---
```

## Overview
<!-- What this TTS provider does and when to use it.
     Example: "ElevenLabs Turbo v2.5 integration for real-time customer service voice bots.
     Optimized for <300ms TTFB with English/Spanish bilingual support." -->
`{{overview}}`

## Provider Specifications

| Property | Value |
|---|---|
| Provider | `{{provider_name}}` |
| API Model | `{{model_id}}` |
| MOS Score | `{{mos_score}}`/5 |
| TTFB (latency) | `{{ttfb_ms}}`ms |
| Price | `{{price_per_1k_chars}}` per 1K chars |
| Voice Cloning | `{{yes_or_no}}` |
| Languages | `{{language_count}}` |
| Audio Formats | `{{formats}}` |
| Streaming | `{{streaming_support}}` |

## API Configuration

```yaml
# Authentication
api_key: "{{api_key_env_var}}"   # Load from env: e.g., ELEVENLABS_API_KEY
endpoint: "{{api_endpoint_url}}" # e.g., https://api.elevenlabs.io/v1/text-to-speech

# Voice selection
voice_id: "{{voice_id}}"         # Provider-specific ID (e.g., ElevenLabs: "21m00Tcm4TlvDq8ikWAM")
model_id: "{{model_id}}"         # e.g., eleven_turbo_v2_5, tts-1-hd, neural2-A

# Audio output
output_format: "{{format}}"      # mp3_44100_128 | pcm_16000 | wav_22050
sample_rate_hz: {{sample_rate}}  # 8000 | 16000 | 22050 | 44100

# Streaming (for real-time use)
streaming: {{true_or_false}}
chunk_size_bytes: {{chunk_size}} # Typical: 1024-4096 bytes
```

## SSML Support

```xml
<!-- Supported SSML tags for this provider -->
<!-- Example: pause, prosody, phoneme, break, emphasis -->
<speak>
  <prosody rate="{{rate}}" pitch="{{pitch}}">
    {{text_input}}
  </prosody>
</speak>
```

| SSML Feature | Supported |
|---|---|
| `<prosody>` (rate/pitch) | `{{yes_no}}` |
| `<break>` (pause injection) | `{{yes_no}}` |
| `<phoneme>` (pronunciation) | `{{yes_no}}` |
| `<emphasis>` | `{{yes_no}}` |
| `<say-as>` (number/date formatting) | `{{yes_no}}` |

## Voice Model Selection

| Voice ID | Name | Gender | Accent | MOS | Use Case |
|---|---|---|---|---|---|
| `{{voice_id_1}}` | {{voice_name_1}} | {{gender}} | {{accent}} | {{mos}} | `{{use_case}}` |
| `{{voice_id_2}}` | {{voice_name_2}} | {{gender}} | {{accent}} | {{mos}} | `{{use_case}}` |

## Latency Optimization

```yaml
# Streaming: minimize TTFB by requesting audio chunks
streaming_enabled: true
flush_on_sentence: true   # Deliver audio per sentence, not full text

# Caching: avoid re-synthesizing identical phrases
cache_enabled: true
cache_ttl_seconds: 3600
cache_key_strategy: "text_hash_voice_model"

# Retry policy
max_retries: 3
retry_delay_ms: 500
timeout_ms: 5000
```

## Fallback Chain

```yaml
# If primary provider fails, cascade to fallback
fallback:
  - provider: "{{fallback_provider_1}}"
    trigger: [rate_limit, timeout, 5xx]
  - provider: "{{fallback_provider_2}}"
    trigger: [all_errors]
```

## Error Handling

| HTTP Code | Meaning | Action |
|---|---|---|
| 400 | Invalid request (bad SSML, unsupported lang) | Fix input, do not retry |
| 401 | Auth failure | Refresh API key |
| 429 | Rate limit | Exponential backoff (start 1s) |
| 500/503 | Provider outage | Activate fallback chain |

## Validation Rules
- id MUST match `^p04_tts_[a-zA-Z0-9_-]+$`
- supported_languages MUST be ISO 639-1 codes (e.g., "en", "es", "pt")
- sample_rate_hz MUST be one of {8000, 16000, 22050, 44100}
- quality MUST be null (never self-score)
- api_key MUST reference an environment variable, never a hardcoded string
