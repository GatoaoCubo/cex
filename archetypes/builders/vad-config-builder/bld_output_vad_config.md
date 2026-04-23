---
kind: output_template
id: bld_output_template_vad_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for vad_config production
quality: 9.0
title: "Output Template Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, output_template]
tldr: "Template with vars for vad_config production"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_vad_config_builder
  - bld_schema_vad_config
  - p09_qg_vad_config
  - bld_examples_vad_config
  - n04_audit_vad_config_builder
  - bld_instruction_vad_config
  - bld_knowledge_card_vad_config
  - kc_vad_config
  - vad-config-builder
  - bld_collaboration_vad_config
---

```yaml
---
id: p09_vad_{{name}}
kind: vad_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [vad_config, {{engine}}, speech_detection]
tldr: "VAD config for {{use_case}}"
sensitivity: {{sensitivity_0_to_1}}
threshold: {{energy_threshold_db}}
---

## Configuration Parameters
```yaml
# VAD Engine: `{{engine}}`  # webrtc | silero | kaldi | custom
aggressiveness: `{{aggressiveness_0_to_3}}`  # WebRTC mode: 0=least, 3=most aggressive
sensitivity: `{{sensitivity_0_to_1}}`         # Speech detection probability floor
noise_floor_db: `{{noise_floor_db}}`          # Background noise floor (dBFS, typical: -60 to -30)
frame_size_ms: `{{frame_size_ms}}`            # Analysis window (10, 20, or 30ms for WebRTC)
min_speech_duration_ms: `{{min_speech_ms}}`   # Minimum speech segment length (typical: 250-500ms)
max_silence_duration_ms: `{{max_silence_ms}}` # Silence before end-of-utterance (typical: 500-2000ms)
speech_pad_ms: `{{speech_pad_ms}}`            # Padding around detected speech (typical: 30-100ms)
```

## Environment Profile
| Property | Value |
|---|---|
| Use Case | {{use_case}} |
| Noise Environment | {{noise_env}} |
| Target Language(s) | {{languages}} |
| Sample Rate | {{sample_rate_hz}} Hz |
| Engine | {{engine}} |

## Sensitivity Settings
```yaml
# Tune per environment
quiet_room:
  sensitivity: 0.3
  aggressiveness: 1
noisy_office:
  sensitivity: 0.6
  aggressiveness: 2
call_center:
  sensitivity: 0.75
  aggressiveness: 3
```

## Validation Rules
- sensitivity MUST be in range [0.1, 1.0]
- aggressiveness MUST be integer in {0, 1, 2, 3} (WebRTC standard)
- frame_size_ms MUST be one of {10, 20, 30} for WebRTC compatibility
- noise_floor_db MUST be in range [-70, -10] dBFS

## Notes
{{notes_content}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_vad_config_builder]] | upstream | 0.51 |
| [[bld_schema_vad_config]] | downstream | 0.47 |
| [[p09_qg_vad_config]] | downstream | 0.46 |
| [[bld_examples_vad_config]] | downstream | 0.36 |
| [[n04_audit_vad_config_builder]] | upstream | 0.31 |
| [[bld_instruction_vad_config]] | upstream | 0.28 |
| [[bld_knowledge_card_vad_config]] | upstream | 0.27 |
| [[kc_vad_config]] | upstream | 0.26 |
| [[vad-config-builder]] | downstream | 0.24 |
| [[bld_collaboration_vad_config]] | downstream | 0.19 |
