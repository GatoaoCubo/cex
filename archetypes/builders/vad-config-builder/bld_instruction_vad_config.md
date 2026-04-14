---
kind: instruction
id: bld_instruction_vad_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for vad_config
quality: 8.8
title: "Instruction Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, instruction]
tldr: "Step-by-step production process for vad_config"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify use case (e.g., noise suppression, call center)  
2. Gather audio sample metadata (sample rate, language, environment)  
3. Study existing vad_config schemas for P09 compatibility  
4. Analyze false positive/negative rates from prior deployments  
5. Benchmark algorithm performance (e.g., WebRTC, Kaldi)  
6. Document regulatory constraints (e.g., GDPR audio handling)  

## Phase 2: COMPOSE  
1. Set schema version in SCHEMA.md (e.g., v1.2.3)  
2. Define sensitivity thresholds (0.1–0.9) for voice detection  
3. Specify window size (e.g., 320 samples @ 16kHz)  
4. Map parameters to OUTPUT_TEMPLATE.md fields  
5. Add silence timeout (e.g., 0.8s) and speech hold (e.g., 0.4s)  
6. Embed language-specific noise profiles (e.g., "en-us", "zh-cn")  
7. Apply P09 constraint rules (e.g., max 200ms silence gaps)  
8. Validate JSON structure against SCHEMA.md  
9. Annotate config with deployment environment tags  

## Phase 3: VALIDATE  
- [ ] Schema validation (jsonschema)  
- [ ] Template field coverage (100%)  
- [ ] Constraint rule enforcement  
- [ ] Audio sample stress test (500+ files)  
- [ ] Cross-platform compatibility (Linux/Windows)
