---
kind: instruction
id: bld_instruction_tts_provider
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for tts_provider
quality: 8.9
title: "Instruction Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, instruction]
tldr: "Step-by-step production process for tts_provider"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_instruction_stt_provider
  - kc_tts_provider
  - p10_lr_tts_provider_builder
  - p03_sp_tts_provider_builder
  - bld_instruction_sdk_example
  - p03_ins_model_provider
  - p01_kc_audio_tool
  - bld_knowledge_card_tts_provider
  - bld_instruction_integration_guide
  - bld_instruction_audio_tool
---

## Phase 1: RESEARCH  
1. Identify TTS provider API requirements (authentication, endpoints, rate limits)  
2. Research available TTS providers (AWS Polly, Google Cloud TTS, Azure Cognitive Services)  
3. Evaluate voice models, language support, and audio format compatibility  
4. Analyze schema in SCHEMA.md for required input/output parameters  
5. Review use cases for text-to-speech integration (e.g., IVR, accessibility features)  
6. Document provider-specific error codes and fallback strategies  

## Phase 2: COMPOSE  
1. Set up development environment with provider SDKs and dependencies  
2. Implement provider class per SCHEMA.md (e.g., `class TTSProvider`)  
3. Write method to convert text to speech using provider API  
4. Add authentication handling (API keys, OAuth tokens)  
5. Integrate audio format conversion per OUTPUT_TEMPLATE.md  
6. Implement error handling for network failures and invalid inputs  
7. Write unit tests for core functionality (text-to-speech conversion)  
8. Document API usage in README.md with code examples  
9. Final code review against SCHEMA.md and OUTPUT_TEMPLATE.md  

## Phase 3: VALIDATE  
- [ ] Validate audio output matches OUTPUT_TEMPLATE.md format  
- [ ] Test provider API authentication and error recovery  
- [ ] Verify compatibility with all supported languages/voices  
- [ ] Confirm schema compliance for input/output parameters  
- [ ] Run end-to-end integration tests with mock and live providers


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_stt_provider]] | sibling | 0.37 |
| [[kc_tts_provider]] | upstream | 0.30 |
| [[p10_lr_tts_provider_builder]] | downstream | 0.29 |
| [[p03_sp_tts_provider_builder]] | related | 0.29 |
| [[bld_instruction_sdk_example]] | sibling | 0.28 |
| [[p03_ins_model_provider]] | sibling | 0.27 |
| [[p01_kc_audio_tool]] | downstream | 0.27 |
| [[bld_knowledge_card_tts_provider]] | upstream | 0.26 |
| [[bld_instruction_integration_guide]] | sibling | 0.26 |
| [[bld_instruction_audio_tool]] | sibling | 0.25 |
