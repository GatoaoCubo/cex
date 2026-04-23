---
kind: quality_gate
id: p09_qg_prosody_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prosody_config
quality: 9.1
title: "Quality Gate Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prosody_config"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_prosody_config
  - bld_knowledge_card_prosody_config
  - bld_output_template_prosody_config
  - hybrid_review2_n03
  - bld_instruction_prosody_config
  - p11_qg_content_filter
  - p04_qg_tts_provider
  - bld_output_template_tts_provider
  - p06_qg_edit_format
  - p03_sp_prosody_config_builder
---

## Quality Gate

## Definition  
| metric         | threshold      | operator | scope         |  
|----------------|----------------|----------|---------------|  
| prosody_config | must exist     | exists   | each config file |  

## HARD Gates  
| ID   | Check                  | Fail Condition                          |  
|------|------------------------|-----------------------------------------|  
| H01  | YAML valid             | Invalid YAML syntax                     |  
| H02  | ID matches pattern     | ID does not match `^[a-zA-Z0-9_]+$`   |  
| H03  | kind matches           | kind is not `prosody_config`          |  
| H04  | voice_personality exists | Missing voice_personality field       |  
| H05  | emotion_settings valid | Emotion values not in allowed list    |  
| H06  | no duplicate IDs       | Duplicate ID detected                 |  
| H07  | config not empty       | Empty or whitespace-only config       |  

## SOFT Scoring (weights sum to 1.00)
| Dim | Dimension              | Weight | Scoring Guide                              |
|-----|------------------------|--------|--------------------------------------------|
| D1  | Voice personality      | 0.15   | 1.0=clear emotion map, 0.5=ambiguous, 0.0=missing |
| D2  | Emission path validity | 0.15   | 1.0=SSML or provider-native correct, 0.5=partial, 0.0=mismatch |
| D3  | Provider coverage      | 0.15   | 1.0=target providers declared + tested, 0.5=one, 0.0=none |
| D4  | SSML/tag syntax        | 0.10   | 1.0=valid per W3C SSML 1.1, 0.5=minor, 0.0=broken |
| D5  | Naturalness            | 0.10   | 1.0=natural, 0.5=stiff, 0.0=mechanical     |
| D6  | Cultural/language fit  | 0.10   | 1.0=locale-appropriate pitch/rate, 0.5=neutral, 0.0=mismatched |
| D7  | Technical validity     | 0.10   | 1.0=valid numeric/enum, 0.5=partial, 0.0=subjective strings |
| D8  | Boundary hygiene       | 0.15   | 1.0=no tts_provider/agent_profile bleed, 0.5=minor, 0.0=mixed |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | Auto-approve, deploy immediately|  
| PUBLISH   | Manual review, schedule deploy  |  
| REVIEW    | Flag for stakeholder feedback   |  
| REJECT    | Block, require rework           |  

## Bypass  
| conditions                          | approver              | audit trail         |  
|------------------------------------|-----------------------|---------------------|  
| Urgent release required            | Senior Product Manager| JIRA-12345          |  
| Legacy system compatibility override | CTO                 | SLA-6789            |

## Examples

## Golden Example 1 -- SSML (Azure/Google/AWS portable)
```yaml
---
id: p09_prs_calm_professional
kind: prosody_config
pillar: P09
version: 1.0.0
---
baseline:
  pitch: "+0%"
  rate: "100%"
  volume: "medium"
emotions:
  calm_professional:
    ssml: |
      <prosody pitch="+2%" rate="95%" volume="medium">
        <break time="300ms"/>
        {{text}}
      </prosody>
  urgent_alert:
    ssml: |
      <prosody pitch="+8%" rate="115%" volume="loud">
        <emphasis level="strong">{{text}}</emphasis>
      </prosody>
target_providers: [azure, google, aws]
```

## Golden Example 2 -- ElevenLabs v3 native
```yaml
---
id: p09_prs_elevenlabs_warm
kind: prosody_config
pillar: P09
version: 1.0.0
---
provider: elevenlabs
voice_settings:
  stability: 0.35          # low = expressive
  similarity_boost: 0.75
  style: 0.45              # moderate style exaggeration
  use_speaker_boost: true
model_id: eleven_multilingual_v2
```

## Golden Example 3 -- Cartesia Sonic inline directives
```yaml
---
id: p09_prs_cartesia_excited
kind: prosody_config
pillar: P09
version: 1.0.0
---
provider: cartesia
model: sonic-english
speed: normal
text_template: "[excited] {{text}} [pause:200ms]"
language: en
```

## Anti-Example 1 -- Mixing provider settings with prosody
```yaml
---
id: p09_prs_bad_provider
prosody_config: "aggressive_sales"
tts_provider: "azure"          # FAIL: belongs in tts_provider kind
api_key: "Ak2hG..."            # FAIL: belongs in secret_config
---
```
## Why it fails
Embeds provider integration + credentials. Prosody_config defines voice characteristics only; provider wiring belongs in tts_provider, secrets in secret_config. Violates pillar boundary (P09 vs P04 vs P09).

## Anti-Example 2 -- Vague, unmeasurable parameters
```yaml
---
id: p09_prs_mysterious
emotion: "unclear"             # FAIL: not a valid emotion label
speech_rate: "fast"            # FAIL: non-numeric, non-SSML
pitch: "high-ish"              # FAIL: subjective
---
```
## Why it fails
Uses ambiguous strings. Prosody requires either SSML-compliant values (x-fast, +10%, 120Hz) OR provider-native enums (ElevenLabs sliders 0.0-1.0, Cartesia `[excited]`). No downstream system can interpret "high-ish".

## Anti-Example 3 -- SSML tags to non-SSML provider
```yaml
---
id: p09_prs_wrong_target
provider: elevenlabs
ssml: "<prosody rate='120%'>Hello</prosody>"   # FAIL: ElevenLabs ignores SSML
---
```
## Why it fails
ElevenLabs v3 does not parse SSML -- it consumes `voice_settings` JSON. Tags are silently passed through as literal text, corrupting output. Always validate emission path matches target provider (see provider matrix in KC).

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
