---
kind: schema
id: bld_schema_multi_modal_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for multi_modal_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: multi_modal_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_mmc_{slug}) | YES | — | Namespace compliance |
| kind | literal "multi_modal_config" | YES | — | Type integrity |
| pillar | literal "P04" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| title | string | YES | — | Human-readable config name |
| supported_modalities | list[enum] | YES | [image, text] | image/audio/video/document |
| image_max_resolution | string | REC | 2048x2048 | WxH pixel limit |
| image_format | list[string] | REC | [png, jpg, webp] | Accepted image formats |
| audio_format | list[string] | REC | [mp3, wav] | Accepted audio formats |
| audio_max_duration_s | int | REC | 600 | Max audio seconds |
| video_max_duration_s | int | REC | 60 | Max video seconds |
| preprocessing | list[string] | REC | [] | resize/compress/transcribe |
| routing_model | map | REC | {} | Modality → model mapping |
| token_cost_estimate | map | REC | {} | Modality → token cost |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "multi_modal_config" |
| tldr | string <= 160ch | YES | — | Dense summary |
## ID Pattern
Regex: `^p04_mmc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Supported Modalities` — table of modality → format → limits
2. `## Preprocessing Pipeline` — steps per modality before LLM call
3. `## Routing Map` — which model handles which modality
4. `## Token Cost Estimates` — per-modality token costs for budget
5. `## Fallback Chain` — what happens when a modality isn't supported
## Constraints
- max_bytes: 2048
- naming: p04_mmc_{capability}.yaml
- supported_modalities values: image, audio, video, document, text
- image_max_resolution format: WxH (e.g., 2048x2048)
