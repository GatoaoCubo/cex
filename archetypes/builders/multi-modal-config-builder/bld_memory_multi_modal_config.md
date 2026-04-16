---
id: p10_lr_multi_modal_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
observation: "Multi-modal configs that fail most often use max resolution always (4K images = 2000+ tokens each, burns budget), have no format validation (unsupported format → API error at runtime), or lack audio transcription fallback."
pattern: "Always set resolution limits per use case (768px for classification, 2048px for detail). Always validate format before API call. Always have transcription fallback for audio. Always estimate token costs. quality:null always."
evidence: "Initial pattern from KC analysis — no production log yet."
confidence: 0.70
outcome: PENDING
domain: multi_modal_config
tags: [multi-modal, image, audio, resolution, routing, token-cost]
tldr: "Set resolution limits per use case. Validate formats. Transcription fallback for audio. Estimate token costs. quality:null."
impact_score: 7.0
decay_rate: 0.05
agent_group: n04_knowledge
keywords: [multi_modal, resolution, format, routing, preprocessing, token_cost]
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
quality: 8.8
title: Memory ISO - multi_modal_config
density_score: 1.0
---
## Summary
Multi-modal configs define how non-text inputs are processed in LLM pipelines. Primary failures are unlimited resolution (burns tokens), no format validation (API errors), and no fallback chains.
## Pattern
1. **Resolution per use case** — 768px classification, 1024px general, 2048px detail
2. **Format validation** — whitelist accepted formats, convert if needed
3. **Transcription fallback** — audio → Whisper → text when model lacks native audio
4. **Token cost estimates** — ~750 tokens per 1024px image, plan budget accordingly
## Anti-Pattern
- Max resolution always: 4K images burn token budget
- No format validation: unsupported format → runtime API error
- No audio fallback: silent failure when model can't process audio natively
- Ignoring token costs: 10 images = 15K tokens, blows context budget
