---
id: p02_mc_google_gemini_2_5_pro
kind: model_card
8f: F2_become
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "CODEX"
model_name: "gemini-2.5-pro"
provider: "google"
model_type: "multimodal"
status: "active"
release_date: "2025-06-17"
knowledge_cutoff: "2025-01"
context_window: 1048576
max_output: 65536
modalities:
  text_input: true
  text_output: true
  image_input: true
  audio_input: true
  pdf_input: true
features:
  tool_calling: true
  structured_output: true
  reasoning: true
  prompt_caching: true
  code_execution: true
  web_search: true
  fine_tunable: false
  batch_api: true
pricing:
  input: 1.25
  output: 10.00
  cache_read: 0.125
  cache_write: null
  unit: per_1M_tokens
domain: model_selection
quality: 9.0
tags: [model-card, google, gemini-2.5, reasoning, coding]
tldr: "Gemini 2.5 Pro - Google, 1048K ctx, $1.25/$10 per 1M at <=200K prompts, strong reasoning and multimodal analysis."
when_to_use: "Use when long-context reasoning, multimodal analysis, or tool-enabled coding matter more than lowest latency."
keywords: [google, gemini-2.5-pro, long-context, reasoning, multimodal]
linked_artifacts:
  primary: null
  related: [p02_mc_claude_opus_4]
data_source: "https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro"
density_score: 0.9
title: "Example: Model Card Google Gemini 2 5 Pro"
related:
  - bld_tools_model_card
  - smoke_test_gemini_20260415
  - bld_tools_model_provider
  - bld_examples_model_card
  - showoff_w2_n05_gemini
  - showoff_w5_n06_gemini
  - showoff_w5_n02_gemini
  - kc_env_config
  - bld_examples_model_provider
  - p01_kc_google_ai_patterns
---

## Boundary
model_card EH: spec tecnica de Gemini 2.5 Pro (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.

## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | gemini-2.5-pro | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |
| Provider | google | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |
| Context Window | 1048K tokens | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |
| Max Output | 65.5K tokens | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |
| Architecture | multimodal thinking model | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |
| Knowledge Cutoff | 2025-01 | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro |

## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
| Tool Calling | true | Function calling supported |
| Structured Output | true | Structured outputs supported |
| Reasoning | true | Thinking supported |
| Prompt Caching | true | Context caching supported |
| Code Execution | true | Built-in tool supported |
| Web Search | true | Search grounding supported |
| Fine Tuning | false | Gemini tuning shut down 2025-05-27 |
| Batch API | true | Batch API supported |

## When to Use
| Scenario | Use This Model? | Why / Alternative |
|----------|-----------------|-------------------|
| Large codebase or document analysis | YES | 1,048,576-token context is the main advantage. |
| Multimodal review with PDFs, images, audio, or video | YES | Native multimodal input beats text-only alternatives. |
| Agentic coding with tools and structured output | YES | Function calling, code execution, search, and batch are all supported. |
| Cost-sensitive high-volume classification | NO | Prefer Gemini 2.5 Flash for lower latency and lower unit cost. |
| Prompting above 200K input tokens often | MAYBE | Price rises to $2.50/$15 per 1M; compare against Claude Sonnet 4 or Gemini 2.5 Flash. |

## References
- source: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro
- pricing: https://ai.google.dev/gemini-api/docs/pricing
- release_notes: https://ai.google.dev/gemini-api/docs/changelog

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_card]] | downstream | 0.45 |
| [[smoke_test_gemini_20260415]] | downstream | 0.44 |
| [[bld_tools_model_provider]] | downstream | 0.41 |
| [[bld_examples_model_card]] | downstream | 0.35 |
| [[showoff_w2_n05_gemini]] | downstream | 0.29 |
| [[showoff_w5_n06_gemini]] | downstream | 0.29 |
| [[showoff_w5_n02_gemini]] | downstream | 0.29 |
| [[kc_env_config]] | upstream | 0.28 |
| [[bld_examples_model_provider]] | downstream | 0.26 |
| [[p01_kc_google_ai_patterns]] | upstream | 0.24 |
