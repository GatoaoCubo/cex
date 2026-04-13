---
kind: instruction
id: bld_instruction_prosody_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prosody_config
quality: null
title: "Instruction Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, instruction]
tldr: "Step-by-step production process for prosody_config"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing voice personality profiles for emotional range and tone consistency.  
2. Identify key prosodic parameters (pitch, rhythm, stress, pause) affecting emotional expression.  
3. Study linguistic and cultural nuances in speech patterns for target demographics.  
4. Benchmark against industry-standard emotion classification frameworks (e.g., Ekman, Plutchik).  
5. Collect user feedback on preferred voice personas for constrained use cases (e.g., customer service).  
6. Document technical constraints (e.g., TTS engine limitations, audio bitrate requirements).  

## Phase 2: COMPOSE  
1. Set up working directory with SCHEMA.md and OUTPUT_TEMPLATE.md as reference files.  
2. Define core emotional states (e.g., calm, urgent, empathetic) and map to prosodic ranges.  
3. Assign numerical values to pitch (Hz), duration (ms), and intensity (dB) per emotional state.  
4. Write config blocks for each persona, ensuring alignment with schema-defined fields.  
5. Apply constraints: limit pitch variation to ±15% of baseline, pauses < 500ms unless specified.  
6. Use OUTPUT_TEMPLATE.md to structure YAML keys (e.g., `emotion: {state}`, `prosody: {pitch: ...}`).  
7. Validate parameter interoperability with downstream systems (e.g., TTS, voice cloning APIs).  
8. Add metadata for versioning, author, and use-case scope in config header.  
9. Finalize by cross-referencing with research notes and schema compliance checks.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema validation: `yamllint` confirms no syntax errors or schema mismatches.  
- [ ] ✅ Constraint enforcement: All prosodic values fall within defined technical limits.  
- [ ] ✅ Emotional accuracy: User tests confirm persona alignment with intended emotion.  
- [ ] ✅ Cross-platform compatibility: Config works across TTS engines (e.g., Amazon Polly, Azure).  
- [ ] ✅ Documentation completeness: All parameters and constraints are traceable to research.
