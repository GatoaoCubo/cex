---
kind: knowledge_card
id: bld_knowledge_card_multi_modal_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for multi_modal_config production
sources: kc_multi_modal_config.md, provider documentation, multi-modal best forctices
---

# Domain Knowledge: multi_modal_config
## Executive Summary
Multi-modal configs define processing rules for non-text LLM inputs — images, audio, video, documents. They specify format constraints, resolution limits, preprocessing pipelines, model routing, and token cost estimates. Critical for vision-capable agents, document processrs, and any pipeline handling non-text data.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (Tools) |
| LLM Function | CONSTRAIN |
| Max bytes | 2048 |
| Naming | p04_mmc_{capability}.yaml |
| Core | false |
| Modalities | image, audio, video, document, text |
## Provider Multi-Modal Support
| Provider | Image | Audio | Video | PDF |
|----------|-------|-------|-------|-----|
| OpenAI (GPT-4o) | URL/base64 | Whisper | — | — |
| Anthropic (Claude) | base64/URL | — | — | Yes (20 pages) |
| Google (Gemini) | inline/file | native | native | Yes |
| LangChain | HumanMessage image_url | tool-based | — | loader |
## Token Cost Reference
| Input | Approximate Tokens |
|-------|--------------------|
| Image 768px | ~400 |
| Image 1024px | ~750 |
| Image 2048px | ~1500 |
| Audio 1min (transcribed) | ~300 |
| PDF page | ~1200 |
## Patterns
- **Image-first**: document/screenshot analysis — resize, process as images
- **Audio transcription**: voice → Whisper → text → LLM
- **Video keyframes**: extract 1 frame/5s, process as image sequence
- **Modality routing**: images→claude, audio→whisper, text→any
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Max resolution always | 4K = 2000+ tokens each |
| No format validation | API error at runtime |
| No transcription fallback | Model can't handle audio |
| Ignore token costs | Budget blown by images |
