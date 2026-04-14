---
kind: output_template
id: bld_output_template_prosody_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for prosody_config production
quality: null
title: "Output Template Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, output_template]
tldr: "Template with vars for prosody_config production"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
---
name: {{name}}
kind: prosody_config
pillar: P09
version: 1.0.0
---
parameters:
  pitch_range: {{pitch_range}}
  speaking_rate: {{speaking_rate}}
  volume_level: {{volume_level}}
language_settings:
  language: {{language}}
  voice_type: {{voice_type}}
advanced:
  pause_duration: {{pause_duration}}
  intonation_curve: {{intonation_curve}}
notes:
  - {{note_1}}
  - {{note_2}}
```
