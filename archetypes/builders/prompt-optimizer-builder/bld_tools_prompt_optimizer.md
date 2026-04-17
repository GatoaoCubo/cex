---
kind: tools
id: bld_tools_prompt_optimizer
pillar: P04
llm_function: CALL
purpose: Tools available for prompt_optimizer production
quality: 8.9
title: "Tools Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, tools]
tldr: "Tools available for prompt_optimizer production"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile prompt_optimizer artifact to YAML output | After F6 PRODUCE |
| cex_score.py | Score artifact against 5D quality dimensions | After generation |
| cex_retriever.py | Retrieve similar prompt_optimizer examples for F3 INJECT | During context assembly |
| cex_doctor.py | Validate builder ISO completeness and frontmatter | During F7 GOVERN |
| cex_prompt_optimizer.py | Analyze builder ISO quality, suggest improvements | During optimization cycles |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit validation: ASCII check, frontmatter, schema | Before F8 COLLABORATE |
| cex_wave_validator.py | Validate all 13 ISOs in builder package | During audit cycles |

## Industry Reference Frameworks
| Framework | Contribution to prompt_optimizer design |
|-----------|----------------------------------------|
| DSPy (Stanford, Khattab 2023) | Declarative prompt optimization via compiled signatures |
| OPRO (DeepMind, Yang 2023) | Optimization by prompting -- LLM as optimizer |
| APE (Zhou 2023) | Automatic prompt engineer -- candidate generation + scoring |
| PromptWizard (Microsoft) | Feedback-driven iterative prompt refinement |
