---
kind: tools
id: bld_tools_multimodal_prompt
pillar: P04
llm_function: CALL
purpose: Tools available for multimodal_prompt production
quality: 8.9
title: "Tools Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, tools]
tldr: "Tools available for multimodal_prompt production"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile multimodal prompt artifact to YAML output | After F6 PRODUCE |
| cex_score.py | Score prompt against 5D quality dimensions | After initial generation |
| cex_retriever.py | Retrieve similar multimodal prompt examples for F3 INJECT | During context assembly |
| cex_doctor.py | Validate builder ISO completeness and frontmatter compliance | During F7 GOVERN |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit validation: ASCII check, frontmatter, schema | Before F8 COLLABORATE |
| cex_wave_validator.py | Validate all 13 ISOs in builder package | During audit cycles |

## Industry Reference Models
| Model | Role in multimodal_prompt design |
|-------|----------------------------------|
| GPT-4V (OpenAI) | Image+text fusion, spatial reasoning prompts |
| Claude 3 vision (Anthropic) | Chart/document understanding prompt patterns |
| Gemini Pro Vision (Google) | Cross-modal grounding and interleaved content |
| LLaVA (Haotian Liu 2023) | Visual instruction tuning prompt format |
| Florence-2 (Microsoft) | Image+text unified prompt architecture |
